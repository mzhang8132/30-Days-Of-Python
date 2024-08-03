# Day 25: 30 Days of python programming

import pandas as pd
import numpy as np

file = "/mnt/c/Users/mzhan/Desktop/30-Days-Of-Python/data"
df = pd.read_csv(file + "/hacker_news.csv")

print(df.head())

print(df.tail())

print(pd.Series(df.columns))

print(df.shape)
print(df[df["title"].str.contains("python")])

print(df[df["title"].str.contains("JavaScript")])