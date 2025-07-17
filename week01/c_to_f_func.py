# c_to_f_func.py
def c_to_f(celsius: float) -> float:
    """
    Chuyển °C sang °F.
    F = C * 9/5 + 32
    """
    return celsius * 9 / 5 + 32


print("Nhập nhiệt độ °C (gõ q để thoát):")
while True:
    inp = input("> ")

    if inp.lower() == "q":          # thoát vòng lặp
        print("Kết thúc, tạm biệt!")
        break

    try:
        c = float(inp)
    except ValueError:
        print("Vui lòng nhập số hoặc q.")
        continue

    f = c_to_f(c)                   # gọi hàm
    print(f"{c} °C = {f:.1f} °F")