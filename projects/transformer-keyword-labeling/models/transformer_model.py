# ✅ transformer_model.py
import torch.nn as nn

class MiniTransformer(nn.Module):
    def __init__(self, vocab_size=1000, num_classes=5):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 32)
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=32, nhead=4),
            num_layers=2
        )
        self.classifier = nn.Linear(32, num_classes)

    def forward(self, x):  # x: [batch, seq_len]
        x = self.embedding(x)         # [batch, seq_len, 32]
        x = x.permute(1, 0, 2)        # [seq_len, batch, 32]
        x = self.encoder(x)           # [seq_len, batch, 32]
        x = x.permute(1, 0, 2)        # [batch, seq_len, 32]
        logits = self.classifier(x)   # [batch, seq_len, num_classes]
        return logits