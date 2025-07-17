# grade_average.py
scores = []                 # danh sách điểm

print("Nhập điểm từng môn (gõ q để xong):")
while True:
    s = input("> ")
    if s.lower() == "q":
        break
    try:
        val = float(s)
        if 0 <= val <= 10:
            scores.append(val)
        else:
            print("Điểm phải 0–10")
    except ValueError:
        print("Nhập số hoặc q.")

avg = sum(scores)/len(scores)
print("Điểm trung bình:", round(avg, 2))

if avg >= 8.5:
    print("Xếp loại: Giỏi 🎉")
elif avg >= 6.5:
    print("Xếp loại: Khá 🙂")
elif avg >= 5:
    print("Xếp loại: Trung bình 😐")
else:
    print("Xếp loại: Yếu 😢")
