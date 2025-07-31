print("Dừng tại số chia hết cho 3:")
for i in range(25, 125):
    if i % 3 == 0:
        break
    print(i)

print("Bỏ qua số chẵn:")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
