# scripts/predict.py
import torch
import os, sys
import yaml
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.transformer_model import MiniTransformer

label2id = {"O": 0, "B-ORG": 1, "I-ORG": 2}
id2label = {v: k for k, v in label2id.items()}
MAX_VOCAB = 1000

def encode_text(text):
    return torch.tensor([min(ord(c), MAX_VOCAB - 1) for c in text], dtype=torch.long).unsqueeze(0)

def predict(text, model_path="models/transformer.pt"):
    model = MiniTransformer()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    x = encode_text(text)
    with torch.no_grad():
        logits = model(x)         # [1, T, C]
        pred_ids = torch.argmax(logits, dim=-1)[0]  # 去掉 batch 维

    pred_labels = [id2label[int(i)] for i in pred_ids]
    return list(zip(text, pred_labels))

if __name__ == "__main__":
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
    text = input("请输入一句话进行预测：\n")
    results = predict(text)
    print("🧾 预测结果：")
    print(json.dumps(results, ensure_ascii=False, indent=2))
