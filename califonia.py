import pandas as pd
import numpy as np
#2.Data Understanding
train_dir = "D:\AI_py\CalifoniaPricePrediction\california_housing_train.csv"
test_dir = "D:\AI_py\CalifoniaPricePrediction\california_housing_test.csv"

train = pd.read_csv(train_dir)
test = pd.read_csv(test_dir)

print(train.shape)
print(train.columns)
print(train.describe())

#3.Data Preprocession
sample = "D:\AI_py\CalifoniaPricePrediction\sample.csv"
sample_data = pd.read_csv(sample)
sample_data_list = [i.strip() for i in sample_data.columns]
# print(sample_data)
sample_data.dropna(axis=0,inplace=True)
print(sample_data)
