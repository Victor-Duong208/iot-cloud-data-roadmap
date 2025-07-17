# currency_converter.py
VND_TO_USD = 0.00004     # ví dụ 1 VND ≈ 0.00004 USD
VND_TO_EUR = 0.000036
VND_TO_JPY = 0.0063

amount = float(input("Nhập số tiền VND: "))

print(f"{amount:,.0f} VND ≈ {amount*VND_TO_USD:,.2f} USD")
print(f"{amount:,.0f} VND ≈ {amount*VND_TO_EUR:,.2f} EUR")
print(f"{amount:,.0f} VND ≈ {amount*VND_TO_JPY:,.0f} JPY")
