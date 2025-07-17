#temp_classifier.py
c = float(input("Nhap nhiet do"))

if c>= 30:
    status = "Nong 🥵"
elif c < 18:
    status ="Lanh 🧊"
else:
    status = "Binh Thuong 🙂"
print(f"{c} °C ⇒ {status}")