# 03. Constructors, Destructors & Memory Management

> **Syllabus Unit:** Block 1 Unit 4 | **Rank:** #3 | **Frequency Score:** 91.5 | **Offered Marks:** 331 | **Papers Present:** 27/30 | **Importance:** Very High

---

## 📋 Topic Overview

This module covers **20 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q059](#q059) | Explain the concept of a copy constructor in C++ with an example program. | **9x** | 55 marks | Theory + Coding / Short Answer & Long Answer | 🔴 **Very High** |
| [Q060](#q060) | What is a destructor in C++? Explain its role in memory management and its ... | **7x** | 32 marks | Theory + Coding / Short Answer | 🔴 **Very High** |
| [Q061](#q061) | Differentiate between a default constructor and a parameterized constructor... | **4x** | 26 marks | Theory + Coding / Short Answer & Long Answer | 🟠 **High** |
| [Q062](#q062) | What are constructors? List five characteristics and discuss the limitation... | **4x** | 25 marks | Theory (+ Coding in 2014-12) / Short Answer & Long Answer | 🟠 **High** |
| [Q063](#q063) | What is constructor overloading in C++? Explain with an example. | **4x** | 25 marks | Theory + Coding / Short Answer & Long Answer | 🟠 **High** |
| [Q064](#q064) | What is the need for memory management in C++, and how is the memory manage... | **4x** | 19 marks | Theory / Short Answer | 🟠 **High** |
| [Q065](#q065) | Differentiate between a copy constructor and a default constructor with an ... | **3x** | 22 marks | Theory + Coding / Short Answer & Long Answer | 🟠 **High** |
| [Q066](#q066) | What is meant by object initialization, and why is it required? Explain wit... | **3x** | 16 marks | Theory / Short Answer | 🟠 **High** |
| [Q067](#q067) | What is a constructor? Explain the advantages of using constructors with an... | **3x** | 15 marks | Theory / Short Answer | 🟠 **High** |
| [Q068](#q068) | Explain the role of new and delete operators in C++ memory management. | **3x** | 15 marks | Theory / Short Answer | 🟠 **High** |
| [Q069](#q069) | Write a C++ program to calculate the factorial of a given number using a co... | **2x** | 18 marks | Coding / Long Answer | 🔵 **Medium** |
| [Q070](#q070) | Explain the process of memory deallocation in C++ with an example. | **2x** | 15 marks | Theory + Coding / Short Answer & Long Answer | 🔵 **Medium** |
| [Q071](#q071) | Discuss the situations when a copy constructor is automatically invoked in ... | **2x** | 9 marks | Theory / Short Answer | 🔵 **Medium** |
| [Q072](#q072) | Write a C++ program to print Student details (Name, Father's Name, Mother's... | **1x** | 10 marks | Coding / Long Answer | ⚪ **Low** |
| [Q073](#q073) | Write a short note on Parameterized Constructor. | **1x** | 5 marks | Theory / Short Answer | ⚪ **Low** |
| [Q074](#q074) | How does a constructor differ from automatic initialization? Briefly discus... | **1x** | 5 marks | Theory / Short Answer | ⚪ **Low** |
| [Q075](#q075) | Discuss naming conventions of destructors. Do constructors and destructors ... | **1x** | 5 marks | Theory / Short Answer | ⚪ **Low** |
| [Q076](#q076) | What are private constructors and destructors? How do they differ from non-... | **1x** | 5 marks | Theory / Short Answer | ⚪ **Low** |
| [Q077](#q077) | Discuss the order of constructor and destructor calls in an inheritance hie... | **1x** | 5 marks | Theory + Coding / Short Answer | ⚪ **Low** |
| [Q078](#q078) | What is a Default Constructor? How is a default constructor equivalent to a... | **1x** | 4 marks | Theory / Short Answer | ⚪ **Low** |

---

## ❓ Detailed Question Bank & Answers

### [Q059] Explain the concept of a copy constructor in C++ with an example program.

🔴 **Very High Priority** • **9 (55 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

ClassName(const ClassName& obj); initializes a new object from an existing one; prevents shallow-copy pointer bugs.

> **🗓️ Asked In Papers:** `2012-12 1(e), 2014-06 1(b), 2018-12S 4(b), 2019-12 1(c), 2020-06 1(c), 2020-12 5(i), 2021-12 3(b), BCAOL S2-13, 2025-06 5(c)`

### [Q060] What is a destructor in C++? Explain its role in memory management and its need with an example program.

🔴 **Very High Priority** • **7 (32 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

~ClassName() invoked automatically when object leaves scope or is deleted; frees dynamic heap resources (delete/delete[]) preventing memory leaks.

> **🗓️ Asked In Papers:** `2017-06 5(a), 2018-06 5(c-i), 2019-12 4(c), 2021-12 3(d), 2022-12 5(iv), 2023-12 1(g), 2025-06 1(g)`

### [Q061] Differentiate between a default constructor and a parameterized constructor with an example.

🟠 **High Priority** • **4 (26 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Default takes zero arguments (or all defaults); parameterized accepts arguments to initialize distinct object states at creation.

> **🗓️ Asked In Papers:** `2015-06 1(c), 2017-06 1(f), 2019-06 2(c), 2021-06 5(c-i)`

### [Q062] What are constructors? List five characteristics and discuss the limitations of constructors.

🟠 **High Priority** • **4 (25 marks)** • *Theory (+ Coding in 2014-12) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Characteristics: same name as class, no return type, public normally, auto-invoked, overloadable; Limitations: cannot be virtual, static, const, or inherited directly.

> **🗓️ Asked In Papers:** `2014-12 2(a), 2021-12 1(e), 2023-06 1(f), 2025-12 1(c)`

### [Q063] What is constructor overloading in C++? Explain with an example.

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Defining multiple constructors in one class differing in parameter count or types to allow flexible object initialization.

> **🗓️ Asked In Papers:** `2018-12S 4(a), 2022-06 1(d), 2023-12 2(d), 2025-06 2(b)`

### [Q064] What is the need for memory management in C++, and how is the memory management process performed?

🟠 **High Priority** • **4 (19 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Allocates exact runtime sizes on heap (free store) and prevents leaks/exhaustion using new, new[], delete, and delete[].

> **🗓️ Asked In Papers:** `2013-06 1(c), 2019-06 1(b), 2020-06 1(e), 2025-12 5(c)`

### [Q065] Differentiate between a copy constructor and a default constructor with an example for each.

🟠 **High Priority** • **3 (22 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Default initializes with zero/default values; copy constructor takes const ClassName& to clone an existing object's state.

> **🗓️ Asked In Papers:** `2016-12 1(d), 2022-12 1(d), 2026-06 4(b)`

### [Q066] What is meant by object initialization, and why is it required? Explain with suitable examples.

🟠 **High Priority** • **3 (16 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Assigning valid initial values upon creation; prevents garbage/uninitialized state errors; automated cleanly by constructors.

> **🗓️ Asked In Papers:** `2013-12 1(c), 2019-06 5(d), 2019-12 1(g)`

### [Q067] What is a constructor? Explain the advantages of using constructors with an example.

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Special member function invoked automatically at instantiation; guarantees valid initialization, supports overloading and dynamic allocation.

> **🗓️ Asked In Papers:** `2012-12 3(b), 2018-06 1(d), 2020-12 1(a)`

### [Q068] Explain the role of new and delete operators in C++ memory management.

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

new allocates heap memory and calls constructor (type-safe, no sizeof/cast needed); delete calls destructor and frees memory.

> **🗓️ Asked In Papers:** `2016-12 5(a), 2021-12 3(c), 2023-06 5(c)`

### [Q069] Write a C++ program to calculate the factorial of a given number using a copy constructor (with comments).

🔵 **Medium Priority** • **2 (18 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Class stores n; copy constructor copies obj.n into a second object; method loops 1..n to compute fact.

> **🗓️ Asked In Papers:** `2014-12 1(b), 2017-06 4(b)`

### [Q070] Explain the process of memory deallocation in C++ with an example.

🔵 **Medium Priority** • **2 (15 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Releasing heap objects via delete ptr; and arrays via delete[] arr;, triggering destructors and setting pointer to nullptr to avoid dangling pointers.

> **🗓️ Asked In Papers:** `2023-12 1(d), 2026-06 1(d)`

### [Q071] Discuss the situations when a copy constructor is automatically invoked in C++.

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

(1) Initializing one object from another (A b = a; or A b(a);), (2) Passing object by value, (3) Returning object by value.

> **🗓️ Asked In Papers:** `2017-12S 1(g), 2023-06 5(a)`

### [Q072] Write a C++ program to print Student details (Name, Father's Name, Mother's Name, Address, Zip code, Roll No) using constructor and destructor.

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Student class initializing all 6 fields in constructor and displaying/cleaning up via method and destructor.

> **🗓️ Asked In Papers:** `2015-12 3(b)`

### [Q073] Write a short note on Parameterized Constructor.

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Constructor accepting one or more arguments to assign user-supplied values during object creation.

> **🗓️ Asked In Papers:** `2016-12 5(b)`

### [Q074] How does a constructor differ from automatic initialization? Briefly discuss copy constructor.

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Built-in types lack automatic non-zero initialization (int x; holds garbage); constructors enforce deterministic initialization of complex classes.

> **🗓️ Asked In Papers:** `2021-06 1(e)`

### [Q075] Discuss naming conventions of destructors. Do constructors and destructors have a return type?

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Tilde prefix (~ClassName()); takes no arguments, cannot be overloaded; neither constructors nor destructors have any return type (not even void).

> **🗓️ Asked In Papers:** `2021-06 3(b)`

### [Q076] What are private constructors and destructors? How do they differ from non-private ones?

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Prevent direct external instantiation/destruction; used in Singleton patterns, factory methods, or heap-only objects.

> **🗓️ Asked In Papers:** `2023-06 5(b)`

### [Q077] Discuss the order of constructor and destructor calls in an inheritance hierarchy with a program.

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Constructors execute top-down (Base then Derived); destructors execute in strict reverse order (Derived then Base).

> **🗓️ Asked In Papers:** `2023-12 3(c)`

### [Q078] What is a Default Constructor? How is a default constructor equivalent to a constructor with default arguments?

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

A constructor where every parameter has a default value (A(int x=0)) can be called with zero arguments, acting identically to a default constructor.

> **🗓️ Asked In Papers:** `2017-12 1(g)`

