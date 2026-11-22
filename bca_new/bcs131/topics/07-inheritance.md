# 07. Inheritance & Code Reusability

> **Syllabus Unit:** Block 2 Unit 1 | **Rank:** #7 | **Frequency Score:** 74.2 | **Offered Marks:** 284 | **Papers Present:** 27/30 | **Importance:** High
> **Coverage:** 22 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q145: What is inheritance? Explain the different types of inheritance supported by C++. :id=q145

🔴 **Very High Priority** • **6 (41 marks)** • *Theory (+ Diagram) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Mechanism for a derived class to acquire properties/methods of base class(es); 5 types: Single, Multilevel, Multiple, Hierarchical, Hybrid.

> **🗓️ Asked In Papers:** `2015-06 1(b), 2022-06 3(b), 2023-12 1(a), 2024-06 4(b), 2024-12 1(h), 2025-06 3(b)`

### Q146: What are visibility modes (public, private, protected) in inheritance? Explain their meaning and when to derive publicly or privately with examples. :id=q146

🟠 **High Priority** • **4 (24 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

public inheritance preserves public/protected; protected turns base public into protected; private turns both into private (base private never directly accessible).

> **🗓️ Asked In Papers:** `2016-06 1(b), 2016-12 2(b), 2017-12 1(i), 2021-12 4(a)`

### Q147: Compare multiple inheritance with multilevel inheritance with an example. :id=q147

🟠 **High Priority** • **4 (24 marks)** • *Theory (+ Diagram) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Multiple: one child inherits from ≥ 2 bases (class C : public A, public B); Multilevel: chain of inheritance (A → B → C); diamond ambiguity risk in multiple.

> **🗓️ Asked In Papers:** `2021-06 4(b), BCAOL S1-2, 2025-12 1(g), 2026-06 1(c)`

### Q148: What is multiple inheritance? Explain its advantages and drawbacks with an example. :id=q148

🟠 **High Priority** • **4 (21 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Combines features from multiple base classes (e.g., TeachingAssistant : Teacher, Student); drawbacks: name ambiguity and diamond problem (solved via virtual base).

> **🗓️ Asked In Papers:** `2016-12 1(c), 2017-06 5(d), 2023-12 3(b), 2025-06 5(d)`

### Q149: What is inheritance? Explain its types and how inheritance is implemented in C++ (class Derived : access Base). :id=q149

🟠 **High Priority** • **3 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Syntax class Derived : public Base { ... };; detail 5 types with class syntax and code snippet.

> **🗓️ Asked In Papers:** `2018-06 2(b), 2022-12 4(a), 2023-06 3(a)`

### Q150: What is software/code reusability in the context of C++, and how is it implemented? Explain with an example. :id=q150

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Reusing tested classes/functions via Inheritance (is-a), Composition (has-a), and Templates without rewriting code.

> **🗓️ Asked In Papers:** `2016-06 1(a), 2019-12 5(a), 2023-12 3(a)`

### Q151: List the merits and demerits of single inheritance over multiple inheritance. :id=q151

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Single is simpler, conflict-free, and easier to debug; lacks ability to compose orthogonal behaviors from multiple independent parents.

> **🗓️ Asked In Papers:** `2013-12 4(a), 2020-12 1(c)`

### Q152: Explain the benefits/advantages of inheritance in C++ with an example. :id=q152

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Code reusability, extensibility, reduced redundancy, hierarchical classification, and foundation for runtime polymorphism.

> **🗓️ Asked In Papers:** `2018-12S 1(f), 2021-06 4(a)`

### Q153: Write an interactive C++ program modeling IGNOU BCA result declaration: Student → Exam (6 subjects) → Result (total marks) and print all members. :id=q153

⚪ **Low Priority** • **1 (15 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Multilevel hierarchy; Student (roll, name), Exam (marks[6]), Result computes total and displays full report.

> **🗓️ Asked In Papers:** `2015-12 2(a)`

### Q154: What are istream and ostream member functions? Create base class QUEUE and derived class AQUEUE with an interactive Queue program. :id=q154

⚪ **Low Priority** • **1 (15 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

istream (get, getline, read, ignore), ostream (put, write, flush); QUEUE holds buffer/front/rear, AQUEUE adds interactive enqueue/dequeue/display.

> **🗓️ Asked In Papers:** `BCAOL S3-15`

### Q155: What is reusability of code? Create student (name, address, age) and inherit PG_student with a function displaying name, address, subject. :id=q155

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Inherit PG_student : public student; add subject and display().

> **🗓️ Asked In Papers:** `2013-06 3(b)`

### Q156: Write a C++ program creating a Vehicle base class and deriving Car, Truck, and Bike with proper constructors. :id=q156

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Hierarchical inheritance; Vehicle(int wheels, float speed) invoked via initializer lists in Car, Truck, Bike.

> **🗓️ Asked In Papers:** `2014-06 4(a)`

### Q157: Explain inheritance and multi-inheritance (multiple inheritance) with an example and C++ program. :id=q157

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Demonstrate single and class C : public A, public B with distinct base properties combined in C.

> **🗓️ Asked In Papers:** `2015-12 5(a)`

### Q158: What are base and derived classes? Create a base class Stack and derived class Mystack with an interactive C++ program showing stack operations. :id=q158

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Stack defines array/top and push/pop; Mystack adds overflow/underflow checks and menu loop.

> **🗓️ Asked In Papers:** `2016-06 4(a)`

### Q159: Create Employee (name, address, age) and derive Part_time employee with a function displaying name, address, and payment. :id=q159

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Part_time : public Employee adds payment (or hours × rate) and display().

> **🗓️ Asked In Papers:** `2017-12 5(a)`

### Q160: Explain ambiguity resolution in multiple inheritance, and what happens if a virtual function is not used in inheritance. :id=q160

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Ambiguity resolved via obj.BaseA::func() or virtual base class inheritance; omitting virtual on overridden methods causes static binding to base.

> **🗓️ Asked In Papers:** `2017-06 1(b)`

### Q161: Write a C++ program to implement multilevel inheritance with comments clarifying member availability across classes. :id=q161

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

A → B → C showing how private stops at A, protected flows to B/C, public stays public.

> **🗓️ Asked In Papers:** `2014-12 1(e)`

### Q162: Explain the usage of single inheritance and multiple inheritance. :id=q162

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Single extends specialized behavior (Animal → Dog); multiple combines orthogonal capabilities (Printer + Scanner → AllInOne).

> **🗓️ Asked In Papers:** `2019-12 1(h)`

### Q163: Compare multiple inheritance with multilevel and hierarchical inheritance. :id=q163

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Multiple: N parents → 1 child; Multilevel: chain A → B → C; Hierarchical: 1 parent → N children.

> **🗓️ Asked In Papers:** `2021-12 4(b)`

### Q164: How is the protected access specifier different from public? Explain its usage for a subclass. :id=q164

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

public is accessible everywhere; protected hides members from external callers while keeping them accessible inside subclasses.

> **🗓️ Asked In Papers:** `2023-06 1(b)`

### Q165: How are parameterized constructors of a base class invoked by derived class constructors? :id=q165

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Using member initializer list: Derived(int x, int y) : Base(x) { ... }

> **🗓️ Asked In Papers:** `2024-06 1(h)`

### Q166: Can a derived class get access privilege for a private member of its base class? If yes, how? :id=q166

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Not directly via inheritance; possible via base's public/protected getter/setter methods or by declaring derived class/method as a friend.

> **🗓️ Asked In Papers:** `2017-12S 1(j)`

