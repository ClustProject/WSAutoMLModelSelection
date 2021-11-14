## Module

실제 사용 예시는 demo.ipynb에서 확인



### 1. 모듈 import

```python
from naomi import NAOMIimputation
```

&nbsp;



### 2. 모델 생성

```python
#path: csv파일의 경로
#window_size: 학습 데이터를 만들 때 사용할 window의 크기 (default: 50)
#use_gpu: gpu 사용 여부 (default: gpu가 사용가능하면 True, 아니면 False)
model = NAOMIimputation(path="csvfile.csv", window_size = 50, use_gpu=False)
```

csv파일은 time과 value column을 포함해야 하며 결측치는 빈칸으로 되어 있어야 합니다.

&nbsp;

csv파일 예시

|      |       time |  value |
| ---: | ---------: | -----: |
|    0 | 2021050100 |  98.63 |
|    1 | 2021050101 | 100.53 |
|    2 | 2021050102 |  99.86 |
|    3 | 2021050103 |    NaN |
|    4 | 2021050104 |    NaN |

&nbsp;



### 3. Imputation

```python
epoch = 200

#epoch만큼 학습을 진행
model.imputation(epoch)

#결과를 plot
model.plot()

#결과 dataframe
result_df = model.df

#결과값의 numpy array
result_numpy = model.result

#결과를 csv로 저장
result_df.to_csv("result.csv")
```

&nbsp;



## CLI

```
python naomi.py --path traffic_missing.csv --window_size 50 --epoch 200
```

--path: csv파일의 경로

--window_size: 학습 데이터를 만들 때 사용할 윈도우의 크기 (default:50)

--epoch: 학습 epoch (default:200)

