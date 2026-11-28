# 09. Functions, Overloading & Parameter Passing

> **Syllabus Unit:** Block 1 Unit 2 / Block 2 | **Rank:** #9 | **Frequency Score:** 56.9 | **Offered Marks:** 218 | **Papers Present:** 21/30 | **Importance:** Medium
> **Coverage:** 10 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q184: What are inline functions? How does their execution differ from normal functions, and what are their importance and advantages? Write an example program. :id=q184

🔴 **Very High Priority** • **13 (77 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Compiler replaces call with body at compile time (when small); eliminates stack-frame/jump overhead improving speed for short, frequently called functions.

**📝 Example PQP Question (2026-06 2(b)):**

What is an Inline Function ? How do they differ from standard functions ? Give examples. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2018-06 5(c-ii)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2018-12S 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2019-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2021-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2022-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2022-12 5(iii)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2024-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2025-06 2(c)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2026-06 2(b)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q185: What is function overloading? Give its advantages and explain how it is implemented with a C++ program. :id=q185

🔴 **Very High Priority** • **6 (46 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Multiple functions sharing same name with distinct parameter count/types/order (return type alone insufficient); provides clean intuitive APIs.

**📝 Example PQP Question (2026-06 2(a)):**

What is Function Overloading ? What are its advantages ? Explain how it is implemented in C++ with an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2016-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2018-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2022-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2025-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore'), [2026-06 2(a)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q186: How are function calls matched with overloaded functions in C++? Explain with an example program. :id=q186

🟠 **High Priority** • **4 (35 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Overload resolution order: (1) Exact match, (2) Integral/floating promotion, (3) Standard conversion, (4) User-defined conversion; error if ambiguous.

**📝 Example PQP Question (2021-06 1(f)):**

What is Function Overloading ? How are function calls matched with overloaded functions ? Explain with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2017-12S 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2020-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q187: Differentiate between call-by-value and call-by-reference in user-defined functions with an example. :id=q187

🟠 **High Priority** • **3 (28 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Call-by-value copies arguments (caller unaffected); call-by-reference passes aliases (int&) allowing in-place mutation (e.g., swap) without copy overhead.

**📝 Example PQP Question (2022-12 4(b)):**

What is the difference between call by value and call by reference in a user defined function in C++ ? Give an example to illustrate the difference. *(10 marks)*

> **🗓️ Asked In Papers:** [2017-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2019-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2022-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q188: Explain Reference Variable and the principal reason for passing arguments by reference. Differentiate passing by pointer vs. reference with a program. :id=q188

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Reference avoids large-object copy overhead and cannot be null/rebound; pointer can be nullptr, reassigned, and requires explicit * dereferencing.

**📝 Example PQP Question (2024-12 2(b)):**

Explain Reference Variable with an example. What is the principle reason of passing arguments by Reference ? Differentiate between passing arguments by using pointer variables and reference variables. Explain with a C++ program. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q189: Differentiate C++ from C in terms of parameter passing in functions. :id=q189

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

C supports only pass-by-value (and simulated reference via pointers); C++ adds native reference parameters (&), default arguments, and strict prototyping.

**📝 Example PQP Question (2013-06 2(a)):**

Differentiate C++ programming language from C programming language in terms of parameter passing in functions. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore')

### Q190: What is the signature of a method? Briefly discuss its components. :id=q190

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Unique identifier for overload resolution: function name + number, types, and order of parameters (plus const/ref qualifiers; excludes return type).

**📝 Example PQP Question (2021-12 2(a)):**

What do you understand by the signature of a method ? Briefly discuss the components of the signature of a method. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q191: What is function overloading? Compare default arguments with function overloading. :id=q191

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Default arguments (f(int a, int b=0)) use one body when logic is identical; overloading uses separate bodies when types or algorithms differ.

**📝 Example PQP Question (2017-12 1(h)):**

What is Function Overloading ? Compare default arguments with function overloading. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q192: Give the advantages and disadvantages of an inline function. :id=q192

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Pros: faster execution, type-safe alternative to #define macros; Cons: code bloat (executable size increases) and compiler may ignore inline for loops/recursion.

**📝 Example PQP Question (2017-12S 1(e)):**

What are inline functions ? Give the advantages and disadvantages of an inline function. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

### Q193: What is Recursion? Explain it with an example. :id=q193

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Function calling itself with a smaller subproblem until reaching a terminating base case (e.g., fact(n) = n * fact(n-1)).

**📝 Example PQP Question (BCAOL S1-3):**

What is Recursion? Explain it with an example. *(4 marks)*

> **🗓️ Asked In Papers:** [BCAOL S1-3](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

