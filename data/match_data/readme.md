# 数据转换
## train和val转换
从csv转到jsonl

每一条格式为：
```json
{'seq': 'GGATACGTCTACGCTCAGTGACGGACTCTCTTCGGAGAGTCTGACATCCG',
 'label': [-5.499000072479248, 8.520000457763672, 8.604999542236328]}
```

表示ran序列和最后一个残基的坐标


## test数据转换

从csv转到jsonl

每一条格式为：
```json
('GGCGUAAGGAUUACCUAUGCC',
 array([[ 35.85699844, -10.76900005,  -7.54799986],
        [ 30.22999954, -12.07499981,  -8.61400032],
        [ 23.96800041, -11.35599995,  -7.69000006],
        [ 19.29599953,  -9.8739996 ,  -4.77799988],
...]))
```

所有ran序列和每个残基的坐标