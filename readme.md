# rna三级结构预测

## 基本代码
- gpt2_rna_train3.ipynb: 微调模型，包含0的数据
- gpt2_rna_train3_no_none.ipynb ：微调模型，不包含None的数据
- gpt2_rna_predict_bench2： 评估代码
- predict_formal.ipynb: 预测代码，提交正式数据，1组复制5组
- predict_formal_dropout.ipynb: 预测代码，提交正式数据，5组预测数据
- predict_formal_right.ipynb.ipynb: 预测代码，使用last token预测


## 基本数据
- rna_pos_1024_train_no_none.jsonl: 微调训练数据，空数据均删除
- rna_pos_1024_val_no_none.jsonl: 微调验证数据，空数据均删除
- rna_pos_1024_train.jsonl: 微调训练数据，空数据设置为0
- rna_pos_1024_val.jsonl: 微调验证数据，空数据设置为0
- rna_pos_all_test.jsonl: 本地使用的测试数据，基于验证集生成
- test_sequences.csv: 比赛正式测试数据的序列