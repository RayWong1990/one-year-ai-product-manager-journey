import yaml
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import json
import os, sys

# 解决相对路径导入问题
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.transformer_model import MiniTransformer

# 超参数定义
MAX_VOCAB = 1000
label2id = {"O": 0, "B-ORG": 1, "I-ORG": 2}
PAD_LABEL_ID = -100

print("🚀 Transformer Keyword Labeling Training Started")

# 读取配置
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)
print(f"📄 Using data: {config['train_file']}")

# 数据集定义
class MyDataset(Dataset):
    def __init__(self, path):
        self.data = [json.loads(line) for line in open(path, encoding="utf-8")]

    def __getitem__(self, idx):
        x = self.data[idx]["text"]
        y = self.data[idx]["labels"]
        assert len(x) == len(y), f"样本 {idx} 的输入与标签长度不一致"  # 校验数据对齐
        x_tensor = torch.tensor([min(ord(c), MAX_VOCAB - 1) for c in x], dtype=torch.long)
        y_tensor = torch.tensor([label2id[label] for label in y], dtype=torch.long)
        return x_tensor, y_tensor

    def __len__(self):
        return len(self.data)

# 统一填充的 pad 函数
def pad(batch):
    x, y = zip(*batch)
    max_len = max(max(len(xi) for xi in x), max(len(yi) for yi in y))
    x_pad = torch.stack([
        torch.cat([xi, torch.zeros(max_len - len(xi), dtype=xi.dtype)]) for xi in x
    ])
    y_pad = torch.stack([
        torch.cat([yi, torch.full((max_len - len(yi),), PAD_LABEL_ID, dtype=yi.dtype)]) for yi in y
    ])
    return x_pad, y_pad

# 数据加载器
train_loader = DataLoader(
    MyDataset(config["train_file"]),
    batch_size=2,
    shuffle=True,
    collate_fn=pad
)

# 模型、损失函数、优化器
model = MiniTransformer()
criterion = nn.CrossEntropyLoss(ignore_index=PAD_LABEL_ID)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 训练循环
for epoch in range(2):
    for i, (x, y) in enumerate(train_loader):
        out = model(x)                          # [B, T, C]
        logits = out.view(-1, out.shape[-1])    # [B*T, C]
        labels = y.view(-1)                     # [B*T]
        mask = labels != PAD_LABEL_ID           # [B*T]

        logits = logits[mask]                   # [有效位置, C]
        labels = labels[mask]                   # [有效位置]

        loss = criterion(logits, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"📘 Epoch {epoch+1} | Step {i+1} | Loss: {loss.item():.4f}")
        print(f"   ➷ logits shape: {logits.shape} | labels shape: {labels.shape}")

# 保存模型
torch.save(model.state_dict(), "models/transformer.pt")
print("✅ Model saved to models/transformer.pt")
