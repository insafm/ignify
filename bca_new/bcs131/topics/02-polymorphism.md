# 02. Polymorphism, Virtual & Abstract Classes

> **Syllabus Unit:** Block 2 Unit 3 | **Rank:** #2 | **Frequency Score:** 120.0 | **Offered Marks:** 520 | **Papers Present:** 30/30 | **Importance:** Very High

---

## 📋 Topic Overview

This module covers **19 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q040](#q040) | Why do abstract classes play an important role in OOP? Implement an abstrac... | **8x** | 73 marks | Theory + Coding / Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q041](#q041) | What is the difference between function overloading and function overriding... | **7x** | 60 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q042](#q042) | Write a C++ program defining a base class (Doctor / Teacher / Employee) wit... | **6x** | 58 marks | Coding / Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q043](#q043) | How does a virtual function differ from a pure virtual function? Explain wi... | **6x** | 36 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q044](#q044) | What is an abstract class? Justify why it "provides a base upon which other... | **6x** | 35 marks | Theory / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q045](#q045) | What is a virtual function? Explain its need, advantages, and limitations i... | **6x** | 30 marks | Theory / Short Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q046](#q046) | What is polymorphism? List three or more advantages of polymorphism in OOP. | **5x** | 23 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q047](#q047) | Compare compile-time polymorphism and run-time polymorphism with examples. | **4x** | 33 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q048](#q048) | What happens if we do not use a virtual function in inheritance? Explain it... | **3x** | 30 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q049](#q049) | Explain the characteristics of virtual/pure virtual functions and illustrat... | **3x** | 28 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q050](#q050) | Define polymorphism, its advantages, and explain the various types of polym... | **3x** | 20 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q051](#q051) | Explain the association between dynamic binding and run-time polymorphism w... | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q052](#q052) | Briefly discuss function overriding in C++ with suitable example code. | **3x** | 15 marks | Theory + Coding / Short Answer | <span class="badge badge-high">High</span> |
| [Q053](#q053) | Compare Early Binding and Late Binding in C++, and explain when to use each... | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q054](#q054) | Write a short note on Pure Virtual Function with an example. | **3x** | 14 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q055](#q055) | What is Runtime Polymorphism? Explain its utility and how it is achieved in... | **2x** | 10 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q056](#q056) | Explain polymorphism, its advantages, and write a C++ program demonstrating... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q057](#q057) | What is polymorphism? Explain its advantages and write a C++ program to dem... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q058](#q058) | How does a virtual function differ from a regular (non-virtual) member func... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q040">

### <span class="badge-qid">Q040</span> Why do abstract classes play an important role in OOP? Implement an abstract class using a pure virtual function in C++ (and explain why it cannot be instantiated).

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 8 (73 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Abstract class has ≥ 1 pure virtual function (virtual void f() = 0;); defines common interface/contract; cannot instantiate because vtable entry is incomplete.

> **🗓️ Asked In Papers:** `2014-12 3(b), 2015-06 1(d), 2015-12 4(a), 2017-06 4(a), 2017-12S 2(a), 2023-12 4(c), BCAOL S2-11, 2024-06 5(a)`

</div>

<div class="question-box" id="q041">

### <span class="badge-qid">Q041</span> What is the difference between function overloading and function overriding in C++? Explain with example code for each.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 7 (60 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Overloading: same scope, same name, different parameter list (compile-time); Overriding: base-derived inheritance, identical signature + virtual in base (run-time).

> **🗓️ Asked In Papers:** `2013-06 5(a), 2017-12 4(a), 2020-12 3(a), 2022-06 3(a), 2023-06 2(d), 2023-12 4(b), 2024-06 2(b)`

</div>

<div class="question-box" id="q042">

### <span class="badge-qid">Q042</span> Write a C++ program defining a base class (Doctor / Teacher / Employee) with a virtual function salary() and derive a subclass (Visiting_Doctor / Associate_Professor / Assistant Professor / Manager) implementing salary().

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (58 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Base class defines virtual void salary(); derived class overrides salary(); invoke via Base* ptr = &derivedObj; ptr->salary(); for runtime dispatch.

> **🗓️ Asked In Papers:** `2013-06 1(d), 2018-06 1(e), 2020-12 3(b), 2022-06 2(a), 2025-06 3(a), 2025-12 3(a)`

</div>

<div class="question-box" id="q043">

### <span class="badge-qid">Q043</span> How does a virtual function differ from a pure virtual function? Explain with an example of each.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (36 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Virtual function has a body in base and allows base instantiation; pure virtual (= 0) usually has no body, forces override in concrete subclasses, and makes class abstract.

> **🗓️ Asked In Papers:** `2016-12 1(f), 2021-12 2(b), 2022-06 1(f), 2024-12 2(c), 2025-06 1(e), 2026-06 1(b)`

</div>

<div class="question-box" id="q044">

### <span class="badge-qid">Q044</span> What is an abstract class? Justify why it "provides a base upon which other classes may be built" and list its advantages with an example.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (35 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Enforces uniform interface across derived types, prevents invalid partial object creation, and enables polymorphic base pointers.

> **🗓️ Asked In Papers:** `2013-12 5(a), 2016-12 1(b), 2022-12 1(e), 2024-12 1(b), 2025-12 1(b), 2026-06 5(b)`

</div>

<div class="question-box" id="q045">

### <span class="badge-qid">Q045</span> What is a virtual function? Explain its need, advantages, and limitations in C++ with an example.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (30 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Enables runtime polymorphism via vtable/vptr; limitations include slight memory/call overhead and inability to make constructors or static functions virtual.

> **🗓️ Asked In Papers:** `2013-12 1(f), 2014-06 4(b), 2021-06 5(c-ii), 2023-06 1(a), 2023-12 5(c), 2025-12 5(a)`

</div>

<div class="question-box" id="q046">

### <span class="badge-qid">Q046</span> What is polymorphism? List three or more advantages of polymorphism in OOP.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 5 (23 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

"One interface, multiple implementations"; advantages: extensibility, code maintainability, loose coupling, and uniform handling via base pointers.

> **🗓️ Asked In Papers:** `2013-12 4(b), 2018-12S 5(b), 2019-12 2(c), 2025-06 1(h), 2025-12 5(b)`

</div>

<div class="question-box" id="q047">

### <span class="badge-qid">Q047</span> Compare compile-time polymorphism and run-time polymorphism with examples.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (33 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Compile-time (static/early binding): function & operator overloading; Run-time (dynamic/late binding): virtual functions resolved via base pointer/reference.

> **🗓️ Asked In Papers:** `2014-12 4(a), 2019-12 4(b), 2020-06 3(a), 2021-06 4(d)`

</div>

<div class="question-box" id="q048">

### <span class="badge-qid">Q048</span> What happens if we do not use a virtual function in inheritance? Explain its importance with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (30 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Calls through a Base* pointer statically bind to Base::func() based on pointer type rather than the actual Derived object type.

> **🗓️ Asked In Papers:** `2014-12 2(b), 2019-12 3(a), 2020-06 3(b)`

</div>

<div class="question-box" id="q049">

### <span class="badge-qid">Q049</span> Explain the characteristics of virtual/pure virtual functions and illustrate a pure virtual function with an example program.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (28 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Syntax virtual ret func() = 0;; derived class must override or remain abstract; demonstrate with Shape → Circle/Rectangle area().

> **🗓️ Asked In Papers:** `2015-06 3(b), 2017-12S 3(b), BCAOL S2-9`

</div>

<div class="question-box" id="q050">

### <span class="badge-qid">Q050</span> Define polymorphism, its advantages, and explain the various types of polymorphism supported by C++ with examples.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (20 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Static (function overloading, operator overloading, templates) and Dynamic (virtual function overriding).

> **🗓️ Asked In Papers:** `2016-06 4(b), 2021-12 4(c), 2023-12 4(a)`

</div>

<div class="question-box" id="q051">

### <span class="badge-qid">Q051</span> Explain the association between dynamic binding and run-time polymorphism with a suitable example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Dynamic binding defers function address resolution until runtime via vtable lookup, which is the underlying mechanism enabling run-time polymorphism.

> **🗓️ Asked In Papers:** `2016-12 3(c), 2022-06 1(g), 2025-12 2(b)`

</div>

<div class="question-box" id="q052">

### <span class="badge-qid">Q052</span> Briefly discuss function overriding in C++ with suitable example code.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

Redefining a base class virtual function in a derived class with identical name, parameters, and return type.

> **🗓️ Asked In Papers:** `2019-06 5(a), 2021-12 4(d), 2025-12 1(e)`

</div>

<div class="question-box" id="q053">

### <span class="badge-qid">Q053</span> Compare Early Binding and Late Binding in C++, and explain when to use each.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Early: compile-time resolution, faster (use for fixed types/overloads); Late: runtime via virtual, flexible (use for extensible polymorphic hierarchies).

> **🗓️ Asked In Papers:** `2021-06 1(g), 2023-06 1(e), 2025-06 4(c)`

</div>

<div class="question-box" id="q054">

### <span class="badge-qid">Q054</span> Write a short note on Pure Virtual Function with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (14 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Declared with = 0 specifier; acts as a placeholder contract in an abstract base class.

> **🗓️ Asked In Papers:** `2016-12 5(d), 2017-06 5(b), 2022-12 5(i)`

</div>

<div class="question-box" id="q055">

### <span class="badge-qid">Q055</span> What is Runtime Polymorphism? Explain its utility and how it is achieved in C++.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (10 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Achieved via inheritance + virtual functions + base class pointer/reference; allows adding new subclasses without altering caller code.

> **🗓️ Asked In Papers:** `2023-06 1(g), 2024-06 1(c)`

</div>

<div class="question-box" id="q056">

### <span class="badge-qid">Q056</span> Explain polymorphism, its advantages, and write a C++ program demonstrating virtual functions.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Base pointer pointing to derived class object invoking overridden virtual display/compute method.

> **🗓️ Asked In Papers:** `2012-12 5(a)`

</div>

<div class="question-box" id="q057">

### <span class="badge-qid">Q057</span> What is polymorphism? Explain its advantages and write a C++ program to demonstrate polymorphism.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Demonstrate both compile-time (overloading) or runtime (virtual dispatch) polymorphism with complete main().

> **🗓️ Asked In Papers:** `2018-06 1(b)`

</div>

<div class="question-box" id="q058">

### <span class="badge-qid">Q058</span> How does a virtual function differ from a regular (non-virtual) member function in C++?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Regular functions bind statically via pointer type; virtual functions bind dynamically via object's vptr.

> **🗓️ Asked In Papers:** `2019-06 1(c)`

</div>

