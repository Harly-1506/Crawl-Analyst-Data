import pandas as pd
from nltk.tokenize import word_tokenize
import numpy as np

# đọc file
df = pd.read_excel("Data.xls")
df.head(5)

# các bước remove stop words

# Tokenĩation
import re


def tokenize(txt):
    tokens = re.split("\W+", txt)
    return tokens


df["Tiêu Đề"] = df["Tiêu Đề"].apply(lambda x: tokenize(str(x)))
df["Mô tả"] = df["Mô tả"].apply(lambda x: tokenize(str(x)))
df.head(5)

# remove stop words
import nltk

# nltk.download('stopwords')
# nltk.download('punkt')
stopwords = nltk.corpus.stopwords.words("vietnamese.txt")
stopwords[0:10]


def remove_stopwords(text):
    text_clean = " ".join([word for word in text if word not in stopwords])
    return text_clean


df["New_Tiêu_Đề"] = df["Tiêu Đề"].apply(lambda x: remove_stopwords((x)))
df["New_Mô_Tả"] = df["Mô tả"].apply(lambda x: remove_stopwords((x)))
df.head(5)

# thống kê số lượng tin tức của mỗi nhóm
a = df.groupby("Thể Loại")["Thể Loại"].count()
a.sort_values(ascending=False).head(10)

# thống kê từ nào xuất hiện nhiều nhất trong các chủ đề
df["Str_max"] = 0
df["Number_count"] = 0

for i in range(len(df["Tiêu Đề"])):
    max = 1
    for j in range(1, len(df["Tiêu Đề"][i]) - 1, 1):
        a = df["Tiêu Đề"][i].count(df["Tiêu Đề"][i][j])
        if a > max:
            max = a
    for j in range(1, len(df["Tiêu Đề"][i]) - 1, 1):
        if df["Tiêu Đề"][i].count(df["Tiêu Đề"][i][j]) == max:
            df["Number_count"][i] = max
            df["Str_max"][i] = df["Tiêu Đề"][i][j]
        else:
            pass

b = df.groupby(["Thể Loại", "Str_max"])["Str_max"].count()
b.sort_values(ascending=False).head(50)


# tìm tin tức được nhập vào bàn phím
n = input("nhập từ khóa: ")
n = n.split(" ")

for k in range(len(n)):
    for i in range(len(df["Tiêu Đề"])):
        for j in range(len(df["Tiêu Đề"][i])):
            if n[k] == df["Tiêu Đề"][i][j]:
                print(" ".join(df["Tiêu Đề"][i]), end="")
                print("--Thể Loại:", df["Thể Loại"][i])
