

# 🔁 Day 4: Loops in Python (with JavaScript Comparison)

---

## 🎯 Overview

Loops allow repeating a block of code multiple times. Both Python and JavaScript support `for`, `while`, and loop control statements like `break`, `continue`. Python has some unique features as well.

---

## 🔹 1. `for` Loop Over List/Array

### ✅ Python
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

✅ JavaScript

const fruits = ["apple", "banana", "cherry"];

for (let fruit of fruits) {
  console.log(fruit);
}


⸻

🔹 2. Loop with Index (range vs for)

✅ Python

for index in range(5):
    print(index)

✅ JavaScript

for (let i = 0; i < 5; i++) {
  console.log(i);
}


⸻

🔹 3. while Loop

✅ Python

i = 0
while i < 5:
    print(i)
    i += 1

✅ JavaScript

let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}


⸻

🔹 4. Loop Control: break, continue

✅ Python

for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print(num)

✅ JavaScript

for (let num = 0; num < 10; num++) {
  if (num === 5) break;
  if (num % 2 === 0) continue;
  console.log(num);
}


⸻

🔹 5. Loop with else (Python Only)

✅ Python

for n in range(3):
    print(n)
else:
    print("Loop finished")

❌ JavaScript does not support else with loops.

⸻

🧠 Summary Table

Feature	Python	JavaScript
Basic for loop	for item in list:	for (let item of array)
Index loop	for i in range(n):	for (let i = 0; i < n; i++)
While loop	while condition:	while (condition) {}
Loop control	break, continue	break, continue
Loop with else	✅ Yes	❌ No


⸻

✅ Practice Ideas
	•	Loop over a list of numbers and print even ones.
	•	Write a loop that stops when it sees “STOP” in a list.
	•	Try nested loops (e.g., multiplication table).
	•	Use else with a loop to print “all done” if loop completed.

⸻
