# Week 1 · Day 3 学习日志  (YYYY-MM-DD)

## 今日目标
- [x] 扩充 NER 数据集到 100 条
- [x] 跑通 `train.py` 2 epoch、不再断言
- [x] 初步验证 loss 下降

## 关键操作记录
| 时间 | 内容 |
|------|------|
| 20:15 | 使用 Python 脚本批量生成含 ORG 的句子 → `data/news_dataset.jsonl` |
| 20:45 | 运行 `bash run.sh`，loss 从 **1.88 → 0.78** |
| 21:30 | 手动预测 `阿里巴巴今日发布财报`，仍全 `O` ——> 确认需要类权重与验证集 |
| 22:00 | 阅读注意力论文第 3.2 节，记录 sin/cos 位置编码公式 |

## 遇到的问题 & 解决
| 问题 | 快速结论 |
|------|---------|
| 预测全 O | 类别失衡，下一步引入 `class_weight` / `FocalLoss` |
| Transformer 警告 `batch_first` | 待在模型层设置 `batch_first=True` |

## 明日计划 (Day 4)
1. 写 `split_dataset.py`，8:2 切分 train/val  
2. 加权 CE，验证集 F1 输出  
3. 补上 `PositionalEncoding`  
4. commit & tensorboard 监控曲线

---

> _今日体会_：跑通基础管线比花哨架构更重要，明天专注让模型**真正识别实体**。
