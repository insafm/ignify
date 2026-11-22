# 11. Operator Overloading

> **Syllabus Unit:** Block 2 Unit 2 | **Rank:** #11 | **Frequency Score:** 43.5 | **Offered Marks:** 163 | **Papers Present:** 20/30 | **Importance:** Medium-Low

---

## 📋 Topic Overview

This module covers **9 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q203](#q203) | What is operator overloading? Explain its advantages and general rules. | **7x** | 42 marks | Theory / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q204](#q204) | Write a C++ program (with comments) to overload the binary + operator to ad... | **3x** | 25 marks | Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q205](#q205) | List the C++ operators that cannot be overloaded, and give reasons for why ... | **3x** | 16 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q206](#q206) | What is operator overloading? List operators that cannot be overloaded and ... | **2x** | 20 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q207](#q207) | Write a C++ program to overload stream insertion (<<) and extraction (>>) o... | **2x** | 20 marks | Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q208](#q208) | Explain the need for operator overloading, why some operators cannot be ove... | **2x** | 15 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q209](#q209) | Explain the need for operator overloading, why some operators cannot be ove... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q210](#q210) | Write a C++ program to overload += and *= operators for a Complex number cl... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q211](#q211) | What are the limitations of Operator Overloading and Function Overloading? | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q203">

### <span class="badge-qid">Q203</span> What is operator overloading? Explain its advantages and general rules.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 7 (42 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Redefines existing C++ operators for user-defined types (operator@); rules: cannot create new tokens, cannot change arity/precedence, at least one operand must be user-defined.

> **🗓️ Asked In Papers:** `2013-06 1(e), 2013-12 5(c), 2015-12 5(b), 2019-06 1(d), 2020-06 1(g), 2023-12 1(c), 2023-12 1(h)`

</div>

<div class="question-box" id="q204">

### <span class="badge-qid">Q204</span> Write a C++ program (with comments) to overload the binary + operator to add two complex numbers.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (25 marks)</span> <span class="badge badge-topic">Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Complex operator+(const Complex& c) { return Complex(real + c.real, imag + c.imag); }

> **🗓️ Asked In Papers:** `2016-12 3(a), 2022-12 3(a), 2025-06 1(f)`

</div>

<div class="question-box" id="q205">

### <span class="badge-qid">Q205</span> List the C++ operators that cannot be overloaded, and give reasons for why they cannot be overloaded.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (16 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

:: (scope resolution), . (member access), .* (pointer-to-member), ?: (ternary), sizeof (and typeid); operate on names/types at compile time rather than runtime values.

> **🗓️ Asked In Papers:** `2016-06 1(d), 2017-12 2(b), BCAOL S1-4`

</div>

<div class="question-box" id="q206">

### <span class="badge-qid">Q206</span> What is operator overloading? List operators that cannot be overloaded and write a C++ program to overload unary minus (-).

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

void operator-() { x = -x; y = -y; } (or returns negated copy) + list of 5 non-overloadable operators.

> **🗓️ Asked In Papers:** `2015-06 3(a), 2019-06 3(a)`

</div>

<div class="question-box" id="q207">

### <span class="badge-qid">Q207</span> Write a C++ program to overload stream insertion (<<) and extraction (>>) operators (e.g., for a Date class dd, mm, yy).

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Must be non-member friend functions: friend ostream& operator<<(ostream& out, const Date& d) and friend istream& operator>>(istream& in, Date& d).

> **🗓️ Asked In Papers:** `2017-06 2(b), 2024-12 4(a)`

</div>

<div class="question-box" id="q208">

### <span class="badge-qid">Q208</span> Explain the need for operator overloading, why some operators cannot be overloaded, and write a program overloading + to add two complex numbers.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (15 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Combines rules/non-overloadable list (::, ., .*, ?:, sizeof) with Complex::operator+ code.

> **🗓️ Asked In Papers:** `2014-12 3(a), 2021-12 1(f)`

</div>

<div class="question-box" id="q209">

### <span class="badge-qid">Q209</span> Explain the need for operator overloading, why some operators cannot be overloaded, and write a C++ program overloading + to concatenate two character strings.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

String class holding char str[100]; operator+ uses strcpy/strcat to concatenate and return new String.

> **🗓️ Asked In Papers:** `2012-12 4(a)`

</div>

<div class="question-box" id="q210">

### <span class="badge-qid">Q210</span> Write a C++ program to overload += and *= operators for a Complex number class (real, imaginary).

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Complex& operator+=(const Complex& c) updates real += c.real; imag += c.imag; return *this;; *= computes (ac - bd) + (ad + bc)i and returns *this.

> **🗓️ Asked In Papers:** `2024-06 5(b)`

</div>

<div class="question-box" id="q211">

### <span class="badge-qid">Q211</span> What are the limitations of Operator Overloading and Function Overloading?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Operator: fixed arity/precedence, 5 operators barred, cannot alter built-in type behavior; Function: cannot overload by return type alone, ambiguity with default args.

> **🗓️ Asked In Papers:** `2021-06 4(c)`

</div>

