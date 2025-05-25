# 🐍 Python 100 Days Challenge

## 📅 Day 2: Data Types, Numbers, Operations, Type Conversion & f-String

---

### 🔹 Data Types (Built-in)
- `int` → পূর্ণসংখ্যা → `10`
- `float` → দশমিক সংখ্যা → `3.14`
- `str` → স্ট্রিং → `"hello"`
- `bool` → সত্য/মিথ্যা → `True`, `False`
- `None` → কিছুই নেই → `None`

---

### 🔹 Numbers Example
```python
a = 10      # int
b = 3.14    # float


⸻

🔹 Arithmetic Operations

x = 10 + 5     # addition
y = 10 - 3     # subtraction
z = 4 * 2      # multiplication
q = 8 / 2      # division (always float)
r = 5 // 2     # floor division => 2
m = 5 % 2      # modulus => 1
p = 2 ** 3     # exponentiation => 8


⸻

🔹 Type Conversion

age = "25"
age_int = int(age)     # "25" → 25

pi = 3.14
pi_str = str(pi)       # 3.14 → "3.14"

is_active = True
num = int(is_active)   # True → 1


⸻

🔹 f-String (String Interpolation)

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

✅ f"..." এর মধ্যে {}-এ যেকোনো variable বা expression বসানো যায়।

⸻

✅ Summary Tips
	•	Python is dynamically typed — variable type লেখা লাগে না।
	•	f-String ব্যবহার করুন ক্লিন ও readable স্ট্রিং তৈরির জন্য।
	•	সব ইনপুট input() থেকে string আসে, তাই প্রয়োজনে type conversion করতে হয়।

⸻