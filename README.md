# 🧮 Sasta Maths Programs

> **Making Math Easy, Fun & Interactive** ✨

A collection of 10th-class mathematics calculators designed to solve real problems. Built with a beautiful, colorful terminal UI that actually makes learning enjoyable!

---

## 👋 About Me

**Hi! I'm Atharva** 🙋‍♂️

- 🎂 **Age:** 15 years old
- 📚 **Grade:** 10th Standard
- 💻 **Passion:** Building tools that make math less scary
- 🎯 **Goal:** Help students like me understand math better

I created these programs because I got tired of solving repetitive math problems. These calculators not only give you answers but also show you **WHY** the answer is correct! Perfect for homework, exam prep, and understanding concepts. 🚀

---

## 🎯 What's Inside?

Three powerful calculators that solve the most common 10th-grade math problems:

### 1️⃣ **quad.py** - Quadratic Equation Solver

Solves any quadratic equation instantly using the **discriminant method**.

**What it does:**
- Input any number → Get a complete quadratic equation
- Shows you the discriminant (D = b² - 4ac)
- Tells you the roots based on D value

**How roots work:**
- **D > 0** → Two different real roots ✅
- **D = 0** → One repeated real root ✅
- **D < 0** → No real roots ❌

**Example:**
```
Input: 5
Equation: 5x² + 10x + 25 = 0
Discriminant: -400
Result: No real roots!
```

---

### 2️⃣ **angle.py** - Trigonometry Calculator

Your personal trig tutor! Calculate ANY angle's trigonometric values instantly.

**What it gives you:**
- **Decimal values** (0.7071, 1.732, etc.)
- **Exact fractions** (1/√2, √3, 1/2, etc.)
- All 6 ratios: sin, cos, tan, cosec, sec, cot

**Special angles** (memorize these!)

| Angle | sin θ | cos θ | tan θ |
|:---:|:---:|:---:|:---:|
| 0° | 0 | 1 | 0 |
| 30° | 1/2 | √3/2 | 1/√3 |
| 45° | 1/√2 | 1/√2 | 1 |
| 60° | √3/2 | 1/2 | √3 |
| 90° | 1 | 0 | ∞ |

**Example:**
```
Input: 45
sin(45°) = 0.7071 OR 1/√2
cos(45°) = 0.7071 OR 1/√2
tan(45°) = 1.0 OR 1
```

---

### 3️⃣ **trigonometry.py** - Triangle Ratio Calculator

Have triangle measurements? Get ALL trigonometric ratios instantly!

**How it works:**
1. Enter Hypotenuse, Perpendicular, Base (in cm)
2. Choose which ratio you want (sin, cos, tan, etc.)
3. Get both decimal AND fractional answer

**Example:**
```
Hypotenuse: 10 cm
Perpendicular: 6 cm
Base: 8 cm

sin θ = 0.6 OR 6/10 = 3/5 ✅
```

---

## 🎨 Key Features

🌈 **Beautiful Terminal UI**
- Colorful boxes and tables
- Easy-to-read formatting
- Works on Windows, Mac, Linux

⚡ **Super Fast**
- Instant calculations
- No waiting time
- Perfect for exam halls

🛡️ **Error Proof**
- Won't crash on wrong input
- Clear error messages
- Validates everything

📚 **Student Friendly**
- Made BY a student FOR students
- Simple menu-driven
- No technical jargon

---

## 🚀 How to Use (Easy!)

### Step 1: Get the Code
```bash
git clone https://github.com/Atharva393688/Sasta_maths_programs.git
cd Sasta_maths_programs
```

### Step 2: Run Any Program

**Windows:**
```bash
python quad.py
python angle.py
python trigonometry.py
```

**Mac/Linux:**
```bash
python3 quad.py
python3 angle.py
python3 trigonometry.py
```

That's it! 🎉

---

## 📖 The Math You Need to Know

### Quadratic Equations
```
Standard Form: ax² + bx + c = 0

Discriminant: D = b² - 4ac

Roots: x = (-b ± √D) / 2a
```

### Trigonometric Ratios
```
sin θ = Opposite / Hypotenuse
cos θ = Adjacent / Hypotenuse  
tan θ = Opposite / Adjacent

Reciprocals:
cosec θ = 1/sin θ
sec θ = 1/cos θ
cot θ = 1/tan θ
```

### Important Identity
```
sin²θ + cos²θ = 1
```

---

## 💡 When to Use Each Tool

| Your Problem | Use This | Why |
|---|---|---|
| "Solve 2x² + 5x + 3 = 0" | `quad.py` | Instant roots with discriminant |
| "Find sin(30°)" | `angle.py` | Shows exact value + decimal |
| "Right triangle with sides 3-4-5, find sin" | `trigonometry.py` | Perfect for real measurements |
| "Check my homework answer" | Any tool! | Compare your manual work |

---

## 🔥 Real Output Examples

### Quadratic Solver Output:
```
🎯 DYNAMIC QUADRATIC GENERATOR

👉 Enter a number: 2

════════════════════════════════════════════════════════════
✨ The quadratic equation is : 2x² + 4x + 4 = 0
════════════════════════════════════════════════════════════

🔹 Discriminant (D) = -16

╔══════════════════════════════════════════════════════════╗
║ ❌ The quadratic equation has no real roots.             ║
╚══════════════════════════════════════════════════════════╝
```

### Angle Calculator Output:
```
📐 T-CALCULATOR V3 PRO

🎯 RESULTS FOR 30°

╔═════════════╦══════════════════╦═════════════════╣
║ Ratio       ║ Decimal Value    ║ Exact Fraction  ║
╠═════════════╬══════════════════╬═════════════════╣
║ Sin(30°)    ║ 0.5              ║ 1/2             ║
║ Cos(30°)    ║ 0.866            ║ √3/2            ║
║ Tan(30°)    ║ 0.577            ║ 1/√3            ║
║ Cosec(30°)  ║ 2.0              ║ 2               ║
║ Sec(30°)    ║ 1.155            ║ 2/√3            ║
║ Cot(30°)    ║ 1.732            ║ √3              ║
╚═════════════╩══════════════════╩═════════════════╝
```

### Triangle Calculator Output:
```
🎯 SINE THETA RESULT

╔══════════════════════════════════════════════════════════╗
║ Decimal Value: 0.6000                                   ║
║ Fraction Value: 6/10 (or 3/5)                           ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎓 Perfect For

- 📚 **Homework** - Verify your answers
- 🧪 **Exam Prep** - Practice different values
- 🔍 **Learning** - Understand concepts better
- 💻 **Physics** - Solve triangle-based problems
- 👨‍🎓 **Board Exams** - Build confidence
- 🤔 **Self-Study** - Learn at your own pace

---

## ⚠️ Common Issues & Fixes

**Problem:** "python: command not found"
```bash
Solution: Try python3 instead of python
python3 quad.py
```

**Problem:** "Colors look weird"
```
Solution: That's okay! Older terminals don't support colors
The calculator still works perfectly!
```

**Problem:** "Invalid choice error"
```
Solution: Make sure you:
- Enter numbers (not letters)
- Enter positive values for triangle sides
- Choose valid menu options (0-6)
```

---

## 🌟 Why This Project is Awesome

✅ **No Dependencies** - Just Python! No pip installs needed
✅ **Open Source** - See the code, learn from it, improve it
✅ **By a Student** - I know what YOU struggle with
✅ **Fast & Reliable** - No crashes, instant results
✅ **Beautiful UI** - Actually fun to use
✅ **Well Commented** - Understand how it works

---

## 🛠️ What's Inside Each File

| File | Lines | Purpose |
|---|---|---|
| `quad.py` | ~80 | Solves quadratic equations |
| `angle.py` | ~120 | Calculates trig ratios for angles |
| `trigonometry.py` | ~150 | Calculates trig ratios from triangle measurements |
| `README.md` | This file | Documentation & guide |
| `.gitignore` | - | Keeps repo clean |

---

## 🚀 Future Ideas

I'm thinking about adding:
- 📊 Visual graphs of quadratic equations
- 🎮 Quiz mode to test your knowledge
- 📱 Web version (if you ask nicely!)
- 📈 More advanced formulas
- 🌐 Support for multiple languages

---

## 💬 Feedback & Help

Found a bug? Have a suggestion? Want to contribute?

**Open an issue on GitHub:** [Sasta_maths_programs/issues](https://github.com/Atharva393688/Sasta_maths_programs/issues)

I read every single issue and suggestion! 💯

---

## 📜 License

**MIT License** - Use it however you want for learning!

---

## ❤️ A Personal Note

These calculators took me days to build and refine. If they help you:
- Score better on tests
- Understand concepts faster
- Complete homework quicker
- Build confidence in math

...then it was all worth it! 🎉

**Please give it a ⭐ on GitHub if it helped you!** It really motivates me to add more features! ✨

---

## 📞 Connect With Me

- **GitHub:** [@Atharva393688](https://github.com/Atharva393688)
- **This Repo:** [Sasta_maths_programs](https://github.com/Atharva393688/Sasta_maths_programs)

---

<div align="center">

### **Made with ❤️ by Atharva**
### *15 years old, 10th Grade Student*

#### *"Mathematics is not about numbers, it's about understanding."*

**⭐ Star this repo if it helped you!**

**Happy Calculating! 🧮✨**

</div>
