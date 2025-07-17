# basics.py
name = "Vinh"           # chuỗi (string)
age = 22                # số nguyên (int)
height_cm = 170.5       # số thực (float)
weight_kg = 70          # giả sử 70 kg

bmi = weight_kg / (height_cm/100)**2      # công thức BMI
print("Tên:", name)
print("Tuổi:", age)
print("Chiều cao:", height_cm, "cm")
print("Cân nặng:", weight_kg, "kg")
print("BMI ước tính:", round(bmi, 1))
print("\n--- Kiểu dữ liệu ---")
print("name:", type(name))
print("age:", type(age))
print("height_cm:", type(height_cm))
print("bmi:", type(bmi))