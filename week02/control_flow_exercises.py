# control_flow_calculator.py

def menu():
    print("===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

while True:
    menu()
    choice = input("Chọn thao tác (1-5): ")

    if choice == "5":
        print("Tạm biệt nha!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ!\n")
        continue

    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!\n")
        continue

    if choice == "1":
        print(f"Kết quả: {a} + {b} = {a + b}\n")
    elif choice == "2":
        print(f"Kết quả: {a} - {b} = {a - b}\n")
    elif choice == "3":
        print(f"Kết quả: {a} * {b} = {a * b}\n")
    elif choice == "4":
        if b == 0:
            print("Không thể chia cho 0!\n")
        else:
            print(f"Kết quả: {a} / {b} = {a / b}\n")
