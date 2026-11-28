# 02. Polymorphism, Virtual & Abstract Classes

> **Syllabus Unit:** Block 2 Unit 3 | **Rank:** #2 | **Frequency Score:** 120.0 | **Offered Marks:** 520 | **Papers Present:** 30/30 | **Importance:** Very High
> **Coverage:** 19 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q040: Why do abstract classes play an important role in OOP? Implement an abstract class using a pure virtual function in C++ (and explain why it cannot be instantiated). :id=q040

🔴 **Very High Priority** • **8 (73 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Abstract class has ≥ 1 pure virtual function (virtual void f() = 0;); defines common interface/contract; cannot instantiate because vtable entry is incomplete.

**📝 Example PQP Question (BCAOL S2-11):**

What is an Abstract Class? Explain use of it with an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2015-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2015-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2017-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2017-12S 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2023-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [BCAOL S2-11](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2024-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q041: What is the difference between function overloading and function overriding in C++? Explain with example code for each. :id=q041

🔴 **Very High Priority** • **7 (60 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Overloading: same scope, same name, different parameter list (compile-time); Overriding: base-derived inheritance, identical signature + virtual in base (run-time).

**📝 Example PQP Question (2024-06 2(b)):**

Differentiate between function overloading and function overriding. Explain with the help of C++ program. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2017-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2020-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2022-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2023-06 2(d)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2023-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2024-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q042: Write a C++ program defining a base class (Doctor / Teacher / Employee) with a virtual function salary() and derive a subclass (Visiting_Doctor / Associate_Professor / Assistant Professor / Manager) implementing salary(). :id=q042

🔴 **Very High Priority** • **6 (58 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Base class defines virtual void salary(); derived class overrides salary(); invoke via Base* ptr = &derivedObj; ptr->salary(); for runtime dispatch.

**📝 Example PQP Question (2025-12 3(a)):**

Write a program in C++ to define a class ‘Employee’ with a virtual function ‘Salary’. Derive the class ‘Manager’ from the class ‘Employee’ and implement the salary function. Make necessary assumptions. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2018-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2020-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2022-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2025-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q043: How does a virtual function differ from a pure virtual function? Explain with an example of each. :id=q043

🔴 **Very High Priority** • **6 (36 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Virtual function has a body in base and allows base instantiation; pure virtual (= 0) usually has no body, forces override in concrete subclasses, and makes class abstract.

**📝 Example PQP Question (2026-06 1(b)):**

What is a Virtual Function? How does it differ from a Pure Virtual Function? Explain with example. *(10 marks)*

> **🗓️ Asked In Papers:** [2016-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2021-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2022-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2024-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore'), [2025-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2026-06 1(b)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q044: What is an abstract class? Justify why it "provides a base upon which other classes may be built" and list its advantages with an example. :id=q044

🔴 **Very High Priority** • **6 (35 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Enforces uniform interface across derived types, prevents invalid partial object creation, and enables polymorphic base pointers.

**📝 Example PQP Question (2025-12 1(b)):**

What are abstract classes? Explain the purpose of abstract class with suitable example. 5 A–24/BCS–031/BCS–131 P. T. O.

> **🗓️ Asked In Papers:** [2013-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2016-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2022-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2024-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore'), [2025-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore'), [2026-06 5(b)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q045: What is a virtual function? Explain its need, advantages, and limitations in C++ with an example. :id=q045

🔴 **Very High Priority** • **6 (30 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Enables runtime polymorphism via vtable/vptr; limitations include slight memory/call overhead and inability to make constructors or static functions virtual.

**📝 Example PQP Question (2023-06 1(a)):**

What are virtual functions and what are its uses? Explain with example. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2014-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2021-06 5(c-ii)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2023-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2023-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q046: What is polymorphism? List three or more advantages of polymorphism in OOP. :id=q046

🟠 **High Priority** • **5 (23 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

"One interface, multiple implementations"; advantages: extensibility, code maintainability, loose coupling, and uniform handling via base pointers.

**📝 Example PQP Question (2025-06 1(h)):**

What is polymorphism? Give advantages of polymorphism. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2018-12S 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2019-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2025-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2025-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q047: Compare compile-time polymorphism and run-time polymorphism with examples. :id=q047

🟠 **High Priority** • **4 (33 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Compile-time (static/early binding): function & operator overloading; Run-time (dynamic/late binding): virtual functions resolved via base pointer/reference.

**📝 Example PQP Question (2021-06 4(d)):**

Compare Compile-time Polymorphism with Run-time Polymorphism. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2019-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2021-06 4(d)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q048: What happens if we do not use a virtual function in inheritance? Explain its importance with an example. :id=q048

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Calls through a Base* pointer statically bind to Base::func() based on pointer type rather than the actual Derived object type.

**📝 Example PQP Question (2020-06 3(b)):**

What is a virtual function? How virtual function relates to inheritance? What happens if we don't use the virtual function in the inheritance? Explain with the help of an example and program. 10

> **🗓️ Asked In Papers:** [2014-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2019-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore')

### Q049: Explain the characteristics of virtual/pure virtual functions and illustrate a pure virtual function with an example program. :id=q049

🟠 **High Priority** • **3 (28 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Syntax virtual ret func() = 0;; derived class must override or remain abstract; demonstrate with Shape → Circle/Rectangle area().

**📝 Example PQP Question (BCAOL S2-9):**

What is a pure virtual funtion in C++? Explain with an example program. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2017-12S 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [BCAOL S2-9](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q050: Define polymorphism, its advantages, and explain the various types of polymorphism supported by C++ with examples. :id=q050

🟠 **High Priority** • **3 (20 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Static (function overloading, operator overloading, templates) and Dynamic (virtual function overriding).

**📝 Example PQP Question (2023-12 4(a)):**

Explain the term polymorphism. Explain the types of polymorphism supported by C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2021-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q051: Explain the association between dynamic binding and run-time polymorphism with a suitable example. :id=q051

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Dynamic binding defers function address resolution until runtime via vtable lookup, which is the underlying mechanism enabling run-time polymorphism.

**📝 Example PQP Question (2025-12 2(b)):**

Explain the association of dynamic binding and runtime polymorphism with suitable example. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2022-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q052: Briefly discuss function overriding in C++ with suitable example code. :id=q052

🟠 **High Priority** • **3 (15 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Redefining a base class virtual function in a derived class with identical name, parameters, and return type.

**📝 Example PQP Question (2025-12 1(e)):**

Explain the term function overriding with the help of a suitable example code in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2019-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2021-12 4(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2025-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q053: Compare Early Binding and Late Binding in C++, and explain when to use each. :id=q053

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Early: compile-time resolution, faster (use for fixed types/overloads); Late: runtime via virtual, flexible (use for extensible polymorphic hierarchies).

**📝 Example PQP Question (2025-06 4(c)):**

Differentiate between early binding and late binding with an example for each. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2023-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2025-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q054: Write a short note on Pure Virtual Function with an example. :id=q054

🟠 **High Priority** • **3 (14 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Declared with = 0 specifier; acts as a placeholder contract in an abstract base class.

**📝 Example PQP Question (2022-12 5(i)):**

Write a short note on: Pure virtual functions *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2017-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2022-12 5(i)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q055: What is Runtime Polymorphism? Explain its utility and how it is achieved in C++. :id=q055

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Achieved via inheritance + virtual functions + base class pointer/reference; allows adding new subclasses without altering caller code.

**📝 Example PQP Question (2024-06 1(c)):**

What do you mean by runtime polymorphism? How is it achieved? *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2024-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q056: Explain polymorphism, its advantages, and write a C++ program demonstrating virtual functions. :id=q056

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Base pointer pointing to derived class object invoking overridden virtual display/compute method.

**📝 Example PQP Question (2012-12 5(a)):**

What is polymorphism? Explain advantage of polymorphism. Also write a C++ program to explain use of virtual function. *(10 marks)*

> **🗓️ Asked In Papers:** [2012-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore')

### Q057: What is polymorphism? Explain its advantages and write a C++ program to demonstrate polymorphism. :id=q057

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Demonstrate both compile-time (overloading) or runtime (virtual dispatch) polymorphism with complete main().

**📝 Example PQP Question (2018-06 1(b)):**

What is polymorphism? Explain its advantages. Write a C++ program to demonstrate polymorphism. *(10 marks)*

> **🗓️ Asked In Papers:** [2018-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore')

### Q058: How does a virtual function differ from a regular (non-virtual) member function in C++? :id=q058

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Regular functions bind statically via pointer type; virtual functions bind dynamically via object's vptr.

**📝 Example PQP Question (2019-06 1(c)):**

What is a virtual function? How does virtual function differ from function in C++? Explain with example. 5 (A..27) P. T. 0.

> **🗓️ Asked In Papers:** [2019-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

