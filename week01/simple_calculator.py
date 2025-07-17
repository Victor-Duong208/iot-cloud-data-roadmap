#simple_calculator.py
def calc(a: float, op: str, b: float) -> float:
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            raise ValueError("Phép toán không hợp lệ")
        
print("Máy tính (+ - * /). Nhập q để thoát.")

while True:
    exp = input("> ")          #VD "5 * 9"
    if exp.lower() == "q":
        break

    try:
        num1, oper, num2 = exp.split()
        result = calc(float(num1), oper, float(num2))
        print("Kết quả:", result)
    except Exception as e:
        print("Lỗi:", e)