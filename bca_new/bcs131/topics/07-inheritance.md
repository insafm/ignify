# 07. Inheritance & Code Reusability

> **Syllabus Unit:** Block 2 Unit 1 | **Rank:** #7 | **Frequency Score:** 74.2 | **Offered Marks:** 284 | **Papers Present:** 27/30 | **Importance:** High

---

## 📋 Topic Overview

This module covers **22 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q145](#q145) | What is inheritance? Explain the different types of inheritance supported b... | **6x** | 41 marks | Theory (+ Diagram) / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q146](#q146) | What are visibility modes (public, private, protected) in inheritance? Expl... | **4x** | 24 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q147](#q147) | Compare multiple inheritance with multilevel inheritance with an example. | **4x** | 24 marks | Theory (+ Diagram) / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q148](#q148) | What is multiple inheritance? Explain its advantages and drawbacks with an ... | **4x** | 21 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q149](#q149) | What is inheritance? Explain its types and how inheritance is implemented i... | **3x** | 25 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q150](#q150) | What is software/code reusability in the context of C++, and how is it impl... | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q151](#q151) | List the merits and demerits of single inheritance over multiple inheritanc... | **2x** | 10 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q152](#q152) | Explain the benefits/advantages of inheritance in C++ with an example. | **2x** | 9 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q153](#q153) | Write an interactive C++ program modeling IGNOU BCA result declaration: Stu... | **1x** | 15 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q154](#q154) | What are istream and ostream member functions? Create base class QUEUE and ... | **1x** | 15 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q155](#q155) | What is reusability of code? Create student (name, address, age) and inheri... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q156](#q156) | Write a C++ program creating a Vehicle base class and deriving Car, Truck, ... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q157](#q157) | Explain inheritance and multi-inheritance (multiple inheritance) with an ex... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q158](#q158) | What are base and derived classes? Create a base class Stack and derived cl... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q159](#q159) | Create Employee (name, address, age) and derive Part_time employee with a f... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q160](#q160) | Explain ambiguity resolution in multiple inheritance, and what happens if a... | **1x** | 6 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q161](#q161) | Write a C++ program to implement multilevel inheritance with comments clari... | **1x** | 5 marks | Coding / Short Answer | <span class="badge badge-low">Low</span> |
| [Q162](#q162) | Explain the usage of single inheritance and multiple inheritance. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q163](#q163) | Compare multiple inheritance with multilevel and hierarchical inheritance. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q164](#q164) | How is the protected access specifier different from public? Explain its us... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q165](#q165) | How are parameterized constructors of a base class invoked by derived class... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q166](#q166) | Can a derived class get access privilege for a private member of its base c... | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q145">

### <span class="badge-qid">Q145</span> What is inheritance? Explain the different types of inheritance supported by C++.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (41 marks)</span> <span class="badge badge-topic">Theory (+ Diagram) / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Mechanism for a derived class to acquire properties/methods of base class(es); 5 types: Single, Multilevel, Multiple, Hierarchical, Hybrid.

> **🗓️ Asked In Papers:** `2015-06 1(b), 2022-06 3(b), 2023-12 1(a), 2024-06 4(b), 2024-12 1(h), 2025-06 3(b)`

</div>

<div class="question-box" id="q146">

### <span class="badge-qid">Q146</span> What are visibility modes (public, private, protected) in inheritance? Explain their meaning and when to derive publicly or privately with examples.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (24 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

public inheritance preserves public/protected; protected turns base public into protected; private turns both into private (base private never directly accessible).

> **🗓️ Asked In Papers:** `2016-06 1(b), 2016-12 2(b), 2017-12 1(i), 2021-12 4(a)`

</div>

<div class="question-box" id="q147">

### <span class="badge-qid">Q147</span> Compare multiple inheritance with multilevel inheritance with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (24 marks)</span> <span class="badge badge-topic">Theory (+ Diagram) / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Multiple: one child inherits from ≥ 2 bases (class C : public A, public B); Multilevel: chain of inheritance (A → B → C); diamond ambiguity risk in multiple.

> **🗓️ Asked In Papers:** `2021-06 4(b), BCAOL S1-2, 2025-12 1(g), 2026-06 1(c)`

</div>

<div class="question-box" id="q148">

### <span class="badge-qid">Q148</span> What is multiple inheritance? Explain its advantages and drawbacks with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (21 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Combines features from multiple base classes (e.g., TeachingAssistant : Teacher, Student); drawbacks: name ambiguity and diamond problem (solved via virtual base).

> **🗓️ Asked In Papers:** `2016-12 1(c), 2017-06 5(d), 2023-12 3(b), 2025-06 5(d)`

</div>

<div class="question-box" id="q149">

### <span class="badge-qid">Q149</span> What is inheritance? Explain its types and how inheritance is implemented in C++ (class Derived : access Base).

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (25 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Syntax class Derived : public Base { ... };; detail 5 types with class syntax and code snippet.

> **🗓️ Asked In Papers:** `2018-06 2(b), 2022-12 4(a), 2023-06 3(a)`

</div>

<div class="question-box" id="q150">

### <span class="badge-qid">Q150</span> What is software/code reusability in the context of C++, and how is it implemented? Explain with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Reusing tested classes/functions via Inheritance (is-a), Composition (has-a), and Templates without rewriting code.

> **🗓️ Asked In Papers:** `2016-06 1(a), 2019-12 5(a), 2023-12 3(a)`

</div>

<div class="question-box" id="q151">

### <span class="badge-qid">Q151</span> List the merits and demerits of single inheritance over multiple inheritance.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (10 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Single is simpler, conflict-free, and easier to debug; lacks ability to compose orthogonal behaviors from multiple independent parents.

> **🗓️ Asked In Papers:** `2013-12 4(a), 2020-12 1(c)`

</div>

<div class="question-box" id="q152">

### <span class="badge-qid">Q152</span> Explain the benefits/advantages of inheritance in C++ with an example.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (9 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Code reusability, extensibility, reduced redundancy, hierarchical classification, and foundation for runtime polymorphism.

> **🗓️ Asked In Papers:** `2018-12S 1(f), 2021-06 4(a)`

</div>

<div class="question-box" id="q153">

### <span class="badge-qid">Q153</span> Write an interactive C++ program modeling IGNOU BCA result declaration: Student → Exam (6 subjects) → Result (total marks) and print all members.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (15 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Multilevel hierarchy; Student (roll, name), Exam (marks[6]), Result computes total and displays full report.

> **🗓️ Asked In Papers:** `2015-12 2(a)`

</div>

<div class="question-box" id="q154">

### <span class="badge-qid">Q154</span> What are istream and ostream member functions? Create base class QUEUE and derived class AQUEUE with an interactive Queue program.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (15 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

istream (get, getline, read, ignore), ostream (put, write, flush); QUEUE holds buffer/front/rear, AQUEUE adds interactive enqueue/dequeue/display.

> **🗓️ Asked In Papers:** `BCAOL S3-15`

</div>

<div class="question-box" id="q155">

### <span class="badge-qid">Q155</span> What is reusability of code? Create student (name, address, age) and inherit PG_student with a function displaying name, address, subject.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Inherit PG_student : public student; add subject and display().

> **🗓️ Asked In Papers:** `2013-06 3(b)`

</div>

<div class="question-box" id="q156">

### <span class="badge-qid">Q156</span> Write a C++ program creating a Vehicle base class and deriving Car, Truck, and Bike with proper constructors.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Hierarchical inheritance; Vehicle(int wheels, float speed) invoked via initializer lists in Car, Truck, Bike.

> **🗓️ Asked In Papers:** `2014-06 4(a)`

</div>

<div class="question-box" id="q157">

### <span class="badge-qid">Q157</span> Explain inheritance and multi-inheritance (multiple inheritance) with an example and C++ program.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Demonstrate single and class C : public A, public B with distinct base properties combined in C.

> **🗓️ Asked In Papers:** `2015-12 5(a)`

</div>

<div class="question-box" id="q158">

### <span class="badge-qid">Q158</span> What are base and derived classes? Create a base class Stack and derived class Mystack with an interactive C++ program showing stack operations.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Stack defines array/top and push/pop; Mystack adds overflow/underflow checks and menu loop.

> **🗓️ Asked In Papers:** `2016-06 4(a)`

</div>

<div class="question-box" id="q159">

### <span class="badge-qid">Q159</span> Create Employee (name, address, age) and derive Part_time employee with a function displaying name, address, and payment.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Part_time : public Employee adds payment (or hours × rate) and display().

> **🗓️ Asked In Papers:** `2017-12 5(a)`

</div>

<div class="question-box" id="q160">

### <span class="badge-qid">Q160</span> Explain ambiguity resolution in multiple inheritance, and what happens if a virtual function is not used in inheritance.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (6 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Ambiguity resolved via obj.BaseA::func() or virtual base class inheritance; omitting virtual on overridden methods causes static binding to base.

> **🗓️ Asked In Papers:** `2017-06 1(b)`

</div>

<div class="question-box" id="q161">

### <span class="badge-qid">Q161</span> Write a C++ program to implement multilevel inheritance with comments clarifying member availability across classes.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Coding / Short Answer</span>

**💡 Key Answer Points:**

A → B → C showing how private stops at A, protected flows to B/C, public stays public.

> **🗓️ Asked In Papers:** `2014-12 1(e)`

</div>

<div class="question-box" id="q162">

### <span class="badge-qid">Q162</span> Explain the usage of single inheritance and multiple inheritance.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Single extends specialized behavior (Animal → Dog); multiple combines orthogonal capabilities (Printer + Scanner → AllInOne).

> **🗓️ Asked In Papers:** `2019-12 1(h)`

</div>

<div class="question-box" id="q163">

### <span class="badge-qid">Q163</span> Compare multiple inheritance with multilevel and hierarchical inheritance.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Multiple: N parents → 1 child; Multilevel: chain A → B → C; Hierarchical: 1 parent → N children.

> **🗓️ Asked In Papers:** `2021-12 4(b)`

</div>

<div class="question-box" id="q164">

### <span class="badge-qid">Q164</span> How is the protected access specifier different from public? Explain its usage for a subclass.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

public is accessible everywhere; protected hides members from external callers while keeping them accessible inside subclasses.

> **🗓️ Asked In Papers:** `2023-06 1(b)`

</div>

<div class="question-box" id="q165">

### <span class="badge-qid">Q165</span> How are parameterized constructors of a base class invoked by derived class constructors?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Using member initializer list: Derived(int x, int y) : Base(x) { ... }

> **🗓️ Asked In Papers:** `2024-06 1(h)`

</div>

<div class="question-box" id="q166">

### <span class="badge-qid">Q166</span> Can a derived class get access privilege for a private member of its base class? If yes, how?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Not directly via inheritance; possible via base's public/protected getter/setter methods or by declaring derived class/method as a friend.

> **🗓️ Asked In Papers:** `2017-12S 1(j)`

</div>

