#fibonacci.py
limit = int(input("In day Fibonacci toi gia tri toi da: "))
a, b = 0, 1    # hai so dau tien
print(a, b, end=" ")

while True:
    a, b = b, a + b    # cap nhat cap so
    if b > limit:
        break
    print(b, end=" ")

print()               #xuong dong duoi