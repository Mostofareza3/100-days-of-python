
# 🔧 Day 6: Functions, While Loops, and Code Blocks in Python (with JavaScript Comparison)

---

## 📦 1. Functions

Functions are reusable blocks of code used to perform a specific task.

---

### ✅ Python
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

✅ JavaScript

function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet("Alice");

🔁 Key Differences:

Feature	Python	JavaScript
Define function	def function_name():	function functionName() {}
Return value	return value	return value;
Arrow function	❌ Not available	const fn = () => {}
First-class fn	✅ Yes	✅ Yes


⸻

🔁 2. While Loops

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

Both work similarly. Just remember: Python uses indentation instead of {}.

⸻

🔁 Python while with else:

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop ended.")

JavaScript has no else clause for loops.

⸻

🧱 3. Code Blocks & Indentation

Python uses indentation instead of {} to define blocks.

✅ Python

def say_hi():
    print("Hi")      # inside function
print("Outside")      # outside function

✅ JavaScript

function sayHi() {
  console.log("Hi");   // inside
}
console.log("Outside"); // outside

🔁 Summary:

Feature	Python	JavaScript
Block start	Indentation (4 spaces or tab)	{ } curly braces
Scope control	Via indentation	Via {}
Missing indent	❌ SyntaxError	✅ still works


⸻

🧠 Pro Tips:
	•	Python indentation is mandatory (usually 4 spaces).
	•	Functions in Python are objects (can be passed around).
	•	Use return in functions when a value is needed.
	•	Be careful with infinite while loops.

⸻

✅ Practice Ideas:
	•	Write a function to check if a number is even or odd.
	•	Use a while loop to guess a random number.
	•	Write a function with default arguments.
	•	Play with nested loops and functions.

⸻
