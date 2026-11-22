# 09. Functions, Overloading & Parameter Passing

> **Syllabus Unit:** Block 1 Unit 2 / Block 2 | **Rank:** #9 | **Frequency Score:** 56.9 | **Offered Marks:** 218 | **Papers Present:** 21/30 | **Importance:** Medium

---

## 📋 Topic Overview

This module covers **10 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q184](#q184) | What are inline functions? How does their execution differ from normal func... | **13x** | 77 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q185](#q185) | What is function overloading? Give its advantages and explain how it is imp... | **6x** | 46 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q186](#q186) | How are function calls matched with overloaded functions in C++? Explain wi... | **4x** | 35 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q187](#q187) | Differentiate between call-by-value and call-by-reference in user-defined f... | **3x** | 28 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q188](#q188) | Explain Reference Variable and the principal reason for passing arguments b... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q189](#q189) | Differentiate C++ from C in terms of parameter passing in functions. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q190](#q190) | What is the signature of a method? Briefly discuss its components. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q191](#q191) | What is function overloading? Compare default arguments with function overl... | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q192](#q192) | Give the advantages and disadvantages of an inline function. | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q193](#q193) | What is Recursion? Explain it with an example. | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q184">

### <span class="badge-qid">Q184</span> What are inline functions? How does their execution differ from normal functions, and what are their importance and advantages? Write an example program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 13 (77 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Compiler replaces call with body at compile time (when small); eliminates stack-frame/jump overhead improving speed for short, frequently called functions.

> **🗓️ Asked In Papers:** `2014-12 1(c), 2018-06 5(c-ii), 2018-12S 2(a), 2019-12 2(b), 2020-12 1(g), 2021-06 1(b), 2021-12 5(b), 2022-06 1(h), 2022-12 5(iii), 2023-06 3(b), 2024-06 1(d), 2025-06 2(c), 2026-06 2(b)`

</div>

<div class="question-box" id="q185">

### <span class="badge-qid">Q185</span> What is function overloading? Give its advantages and explain how it is implemented with a C++ program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (46 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Multiple functions sharing same name with distinct parameter count/types/order (return type alone insufficient); provides clean intuitive APIs.

> **🗓️ Asked In Papers:** `2014-06 5(c), 2016-12 1(e), 2018-06 3(b), 2022-12 2(a), 2025-12 5(d), 2026-06 2(a)`

</div>

<div class="question-box" id="q186">

### <span class="badge-qid">Q186</span> How are function calls matched with overloaded functions in C++? Explain with an example program.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (35 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Overload resolution order: (1) Exact match, (2) Integral/floating promotion, (3) Standard conversion, (4) User-defined conversion; error if ambiguous.

> **🗓️ Asked In Papers:** `2013-06 5(b), 2017-12S 4(b), 2020-12 4(a), 2021-06 1(f)`

</div>

<div class="question-box" id="q187">

### <span class="badge-qid">Q187</span> Differentiate between call-by-value and call-by-reference in user-defined functions with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (28 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Call-by-value copies arguments (caller unaffected); call-by-reference passes aliases (int&) allowing in-place mutation (e.g., swap) without copy overhead.

> **🗓️ Asked In Papers:** `2017-12 3(a), 2019-12 4(a), 2022-12 4(b)`

</div>

<div class="question-box" id="q188">

### <span class="badge-qid">Q188</span> Explain Reference Variable and the principal reason for passing arguments by reference. Differentiate passing by pointer vs. reference with a program.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Reference avoids large-object copy overhead and cannot be null/rebound; pointer can be nullptr, reassigned, and requires explicit * dereferencing.

> **🗓️ Asked In Papers:** `2024-12 2(b)`

</div>

<div class="question-box" id="q189">

### <span class="badge-qid">Q189</span> Differentiate C++ from C in terms of parameter passing in functions.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

C supports only pass-by-value (and simulated reference via pointers); C++ adds native reference parameters (&), default arguments, and strict prototyping.

> **🗓️ Asked In Papers:** `2013-06 2(a)`

</div>

<div class="question-box" id="q190">

### <span class="badge-qid">Q190</span> What is the signature of a method? Briefly discuss its components.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Unique identifier for overload resolution: function name + number, types, and order of parameters (plus const/ref qualifiers; excludes return type).

> **🗓️ Asked In Papers:** `2021-12 2(a)`

</div>

<div class="question-box" id="q191">

### <span class="badge-qid">Q191</span> What is function overloading? Compare default arguments with function overloading.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Default arguments (f(int a, int b=0)) use one body when logic is identical; overloading uses separate bodies when types or algorithms differ.

> **🗓️ Asked In Papers:** `2017-12 1(h)`

</div>

<div class="question-box" id="q192">

### <span class="badge-qid">Q192</span> Give the advantages and disadvantages of an inline function.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Pros: faster execution, type-safe alternative to #define macros; Cons: code bloat (executable size increases) and compiler may ignore inline for loops/recursion.

> **🗓️ Asked In Papers:** `2017-12S 1(e)`

</div>

<div class="question-box" id="q193">

### <span class="badge-qid">Q193</span> What is Recursion? Explain it with an example.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Function calling itself with a smaller subproblem until reaching a terminating base case (e.g., fact(n) = n * fact(n-1)).

> **🗓️ Asked In Papers:** `BCAOL S1-3`

</div>

