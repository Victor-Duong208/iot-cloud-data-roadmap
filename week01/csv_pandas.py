import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv("week01/data.csv", encoding="utf-8")

# Hiển thị nội dung
print("Nội dung DataFrame:")
print(df)

# Lưu ra file mới
df.to_csv("week01/data_copy.csv", index=False, encoding="utf-8")
