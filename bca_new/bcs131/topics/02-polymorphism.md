# 02. Polymorphism, Virtual & Abstract Classes

> **Syllabus Unit:** Block 2 Unit 3 | **Rank:** #2 | **Frequency Score:** 120.0 | **Offered Marks:** 520 | **Papers Present:** 30/30 | **Importance:** Very High
> **Coverage:** 19 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q040: Why do abstract classes play an important role in OOP? Implement an abstract class using a pure virtual function in C++ (and explain why it cannot be instantiated). :id=q040

🔴 **Very High Priority** • **8 (73 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Abstract class has ≥ 1 pure virtual function (virtual void f() = 0;); defines common interface/contract; cannot instantiate because vtable entry is incomplete.

> **🗓️ Asked In Papers:** `2014-12 3(b), 2015-06 1(d), 2015-12 4(a), 2017-06 4(a), 2017-12S 2(a), 2023-12 4(c), BCAOL S2-11, 2024-06 5(a)`

### Q041: What is the difference between function overloading and function overriding in C++? Explain with example code for each. :id=q041

🔴 **Very High Priority** • **7 (60 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Overloading: same scope, same name, different parameter list (compile-time); Overriding: base-derived inheritance, identical signature + virtual in base (run-time).

> **🗓️ Asked In Papers:** `2013-06 5(a), 2017-12 4(a), 2020-12 3(a), 2022-06 3(a), 2023-06 2(d), 2023-12 4(b), 2024-06 2(b)`

### Q042: Write a C++ program defining a base class (Doctor / Teacher / Employee) with a virtual function salary() and derive a subclass (Visiting_Doctor / Associate_Professor / Assistant Professor / Manager) implementing salary(). :id=q042

🔴 **Very High Priority** • **6 (58 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Base class defines virtual void salary(); derived class overrides salary(); invoke via Base* ptr = &derivedObj; ptr->salary(); for runtime dispatch.

> **🗓️ Asked In Papers:** `2013-06 1(d), 2018-06 1(e), 2020-12 3(b), 2022-06 2(a), 2025-06 3(a), 2025-12 3(a)`

### Q043: How does a virtual function differ from a pure virtual function? Explain with an example of each. :id=q043

🔴 **Very High Priority** • **6 (36 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Virtual function has a body in base and allows base instantiation; pure virtual (= 0) usually has no body, forces override in concrete subclasses, and makes class abstract.

> **🗓️ Asked In Papers:** `2016-12 1(f), 2021-12 2(b), 2022-06 1(f), 2024-12 2(c), 2025-06 1(e), 2026-06 1(b)`

### Q044: What is an abstract class? Justify why it "provides a base upon which other classes may be built" and list its advantages with an example. :id=q044

🔴 **Very High Priority** • **6 (35 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Enforces uniform interface across derived types, prevents invalid partial object creation, and enables polymorphic base pointers.

> **🗓️ Asked In Papers:** `2013-12 5(a), 2016-12 1(b), 2022-12 1(e), 2024-12 1(b), 2025-12 1(b), 2026-06 5(b)`

### Q045: What is a virtual function? Explain its need, advantages, and limitations in C++ with an example. :id=q045

🔴 **Very High Priority** • **6 (30 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Enables runtime polymorphism via vtable/vptr; limitations include slight memory/call overhead and inability to make constructors or static functions virtual.

> **🗓️ Asked In Papers:** `2013-12 1(f), 2014-06 4(b), 2021-06 5(c-ii), 2023-06 1(a), 2023-12 5(c), 2025-12 5(a)`

### Q046: What is polymorphism? List three or more advantages of polymorphism in OOP. :id=q046

🟠 **High Priority** • **5 (23 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

"One interface, multiple implementations"; advantages: extensibility, code maintainability, loose coupling, and uniform handling via base pointers.

> **🗓️ Asked In Papers:** `2013-12 4(b), 2018-12S 5(b), 2019-12 2(c), 2025-06 1(h), 2025-12 5(b)`

### Q047: Compare compile-time polymorphism and run-time polymorphism with examples. :id=q047

🟠 **High Priority** • **4 (33 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Compile-time (static/early binding): function & operator overloading; Run-time (dynamic/late binding): virtual functions resolved via base pointer/reference.

> **🗓️ Asked In Papers:** `2014-12 4(a), 2019-12 4(b), 2020-06 3(a), 2021-06 4(d)`

### Q048: What happens if we do not use a virtual function in inheritance? Explain its importance with an example. :id=q048

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Calls through a Base* pointer statically bind to Base::func() based on pointer type rather than the actual Derived object type.

> **🗓️ Asked In Papers:** `2014-12 2(b), 2019-12 3(a), 2020-06 3(b)`

### Q049: Explain the characteristics of virtual/pure virtual functions and illustrate a pure virtual function with an example program. :id=q049

🟠 **High Priority** • **3 (28 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Syntax virtual ret func() = 0;; derived class must override or remain abstract; demonstrate with Shape → Circle/Rectangle area().

> **🗓️ Asked In Papers:** `2015-06 3(b), 2017-12S 3(b), BCAOL S2-9`

### Q050: Define polymorphism, its advantages, and explain the various types of polymorphism supported by C++ with examples. :id=q050

🟠 **High Priority** • **3 (20 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Static (function overloading, operator overloading, templates) and Dynamic (virtual function overriding).

> **🗓️ Asked In Papers:** `2016-06 4(b), 2021-12 4(c), 2023-12 4(a)`

### Q051: Explain the association between dynamic binding and run-time polymorphism with a suitable example. :id=q051

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Dynamic binding defers function address resolution until runtime via vtable lookup, which is the underlying mechanism enabling run-time polymorphism.

> **🗓️ Asked In Papers:** `2016-12 3(c), 2022-06 1(g), 2025-12 2(b)`

### Q052: Briefly discuss function overriding in C++ with suitable example code. :id=q052

🟠 **High Priority** • **3 (15 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Redefining a base class virtual function in a derived class with identical name, parameters, and return type.

> **🗓️ Asked In Papers:** `2019-06 5(a), 2021-12 4(d), 2025-12 1(e)`

### Q053: Compare Early Binding and Late Binding in C++, and explain when to use each. :id=q053

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Early: compile-time resolution, faster (use for fixed types/overloads); Late: runtime via virtual, flexible (use for extensible polymorphic hierarchies).

> **🗓️ Asked In Papers:** `2021-06 1(g), 2023-06 1(e), 2025-06 4(c)`

### Q054: Write a short note on Pure Virtual Function with an example. :id=q054

🟠 **High Priority** • **3 (14 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Declared with = 0 specifier; acts as a placeholder contract in an abstract base class.

> **🗓️ Asked In Papers:** `2016-12 5(d), 2017-06 5(b), 2022-12 5(i)`

### Q055: What is Runtime Polymorphism? Explain its utility and how it is achieved in C++. :id=q055

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Achieved via inheritance + virtual functions + base class pointer/reference; allows adding new subclasses without altering caller code.

> **🗓️ Asked In Papers:** `2023-06 1(g), 2024-06 1(c)`

### Q056: Explain polymorphism, its advantages, and write a C++ program demonstrating virtual functions. :id=q056

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Base pointer pointing to derived class object invoking overridden virtual display/compute method.

> **🗓️ Asked In Papers:** `2012-12 5(a)`

### Q057: What is polymorphism? Explain its advantages and write a C++ program to demonstrate polymorphism. :id=q057

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Demonstrate both compile-time (overloading) or runtime (virtual dispatch) polymorphism with complete main().

> **🗓️ Asked In Papers:** `2018-06 1(b)`

### Q058: How does a virtual function differ from a regular (non-virtual) member function in C++? :id=q058

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Regular functions bind statically via pointer type; virtual functions bind dynamically via object's vptr.

> **🗓️ Asked In Papers:** `2019-06 1(c)`

