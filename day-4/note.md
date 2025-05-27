# 🐍 Day 4: Randomisation & Python List (with JavaScript Comparison)

---

## 🎲 1. Randomisation in Python vs JavaScript

### ✅ Python
```python
import random

num = random.randint(1, 10)  # inclusive of both ends
print(num)

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))       # Random single item
print(random.shuffle(fruits))      # In-place shuffle (returns None)

✅ JavaScript

const num = Math.floor(Math.random() * 10) + 1;

const fruits = ["apple", "banana", "cherry"];
const randomFruit = fruits[Math.floor(Math.random() * fruits.length)];

// Shuffle (manual using Fisher-Yates)
fruits.sort(() => Math.random() - 0.5);

🔁 Key Differences:

Feature	Python	JavaScript
Random Integer	random.randint(a, b)	Math.floor(Math.random() * (b - a + 1)) + a
Random Item	random.choice(list)	array[Math.floor(Math.random()*array.length)]
Shuffle	random.shuffle(list) (in-place)	array.sort(() => Math.random() - 0.5) (not true shuffle)


⸻

📚 2. Lists in Python vs Arrays in JavaScript

✅ Python

my_list = ["apple", "banana", "cherry"]
my_list.append("mango")       # Add item
my_list.remove("banana")      # Remove item
print(my_list[1])             # Access item
print(len(my_list))           # Length

✅ JavaScript

const myList = ["apple", "banana", "cherry"];
myList.push("mango");        // Add item
myList.splice(1, 1);         // Remove item at index
console.log(myList[1]);      // Access item
console.log(myList.length);  // Length

🔁 Key Differences:

Feature	Python	JavaScript
Declare list	my_list = [1, 2, 3]	let arr = [1, 2, 3]
Add item	append()	push()
Remove item	remove("value") / pop()	splice(index, 1) / pop()
Insert at index	insert(index, value)	splice(index, 0, value)
Slice	list[1:3]	list.slice(1, 3)
Length	len(list)	list.length


⸻

🧠 Summary Tips
	•	Python lists ≈ JavaScript arrays
	•	Python uses import random for randomness
	•	JavaScript’s shuffle is less accurate than Python’s random.shuffle()
	•	Python list methods are more “readable” (append, remove, etc.)

⸻

✅ Next Step: Try building a random “coin flip” or “password generator” using both languages!

---
