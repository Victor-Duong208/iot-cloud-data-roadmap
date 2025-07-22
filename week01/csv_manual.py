# Mở file CSV để đọc
with open("week01/data.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Dòng đầu tiên là tiêu đề (header)
header = lines[0].strip().split(",")
print("Header:", header)

# Các dòng còn lại là dữ liệu
for line in lines[1:]:
    values = line.strip().split(",")
    name = values[0]
    age = int(values[1])         # ép kiểu sang số nguyên
    score = float(values[2])     # ép kiểu sang số thực
    print(f"{name} ({age} tuổi) - điểm: {score}")
