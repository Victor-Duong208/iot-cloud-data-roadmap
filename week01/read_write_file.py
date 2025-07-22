# Đọc nội dung từ file
with open("week01/example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Nội dung file:")
    for line in lines:
        print(line.strip())

# Ghi nội dung mới vào file khác
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2\n")
