# 07. Inheritance & Code Reusability

> **Syllabus Unit:** Block 2 Unit 1 | **Rank:** #7 | **Frequency Score:** 74.2 | **Offered Marks:** 284 | **Papers Present:** 27/30 | **Importance:** High
> **Coverage:** 22 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q145: What is inheritance? Explain the different types of inheritance supported by C++. :id=q145

🔴 **Very High Priority** • **6 (41 marks)** • *Theory (+ Diagram) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Mechanism for a derived class to acquire properties/methods of base class(es); 5 types: Single, Multilevel, Multiple, Hierarchical, Hybrid.

**📝 Example PQP Question (2025-06 3(b)):**

What is inheritance in C++ ? Explain different types of inheritance in C++. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2022-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2023-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2024-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2024-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore'), [2025-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q146: What are visibility modes (public, private, protected) in inheritance? Explain their meaning and when to derive publicly or privately with examples. :id=q146

🟠 **High Priority** • **4 (24 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

public inheritance preserves public/protected; protected turns base public into protected; private turns both into private (base private never directly accessible).

**📝 Example PQP Question (2021-12 4(a)):**

Explain the access specifiers used in inheritance in C++ with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2016-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2017-12 1(i)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2021-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q147: Compare multiple inheritance with multilevel inheritance with an example. :id=q147

🟠 **High Priority** • **4 (24 marks)** • *Theory (+ Diagram) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Multiple: one child inherits from ≥ 2 bases (class C : public A, public B); Multilevel: chain of inheritance (A → B → C); diamond ambiguity risk in multiple.

**📝 Example PQP Question (2026-06 1(c)):**

What is Multiple Inheritance ? How does it differ from Multilevel Inheritance ? Explain with example. *(10 marks)*

> **🗓️ Asked In Papers:** [2021-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [BCAOL S1-2](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2025-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore'), [2026-06 1(c)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q148: What is multiple inheritance? Explain its advantages and drawbacks with an example. :id=q148

🟠 **High Priority** • **4 (21 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Combines features from multiple base classes (e.g., TeachingAssistant : Teacher, Student); drawbacks: name ambiguity and diamond problem (solved via virtual base).

**📝 Example PQP Question (2023-12 3(b)):**

What is multiple inheritance ? What are its drawbacks ? Explain with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2017-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2023-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q149: What is inheritance? Explain its types and how inheritance is implemented in C++ (class Derived : access Base). :id=q149

🟠 **High Priority** • **3 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Syntax class Derived : public Base { ... };; detail 5 types with class syntax and code snippet.

**📝 Example PQP Question (2023-06 3(a)):**

What is inheritance ? Explain, how inheritance is implemented in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2018-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2022-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q150: What is software/code reusability in the context of C++, and how is it implemented? Explain with an example. :id=q150

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Reusing tested classes/functions via Inheritance (is-a), Composition (has-a), and Templates without rewriting code.

**📝 Example PQP Question (2023-12 3(a)):**

What is concept of reusability ? Explain how this concept is implemented in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2019-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2023-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q151: List the merits and demerits of single inheritance over multiple inheritance. :id=q151

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Single is simpler, conflict-free, and easier to debug; lacks ability to compose orthogonal behaviors from multiple independent parents.

**📝 Example PQP Question (2020-12 1(c)):**

List the merits and demerits of single inheritance over multiple inheritance. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2020-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q152: Explain the benefits/advantages of inheritance in C++ with an example. :id=q152

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Code reusability, extensibility, reduced redundancy, hierarchical classification, and foundation for runtime polymorphism.

**📝 Example PQP Question (2021-06 4(a)):**

What is Inheritance ? What are the advantages of inheritance ? Explain with the help of example. *(5 marks)*

> **🗓️ Asked In Papers:** [2018-12S 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2021-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q153: Write an interactive C++ program modeling IGNOU BCA result declaration: Student → Exam (6 subjects) → Result (total marks) and print all members. :id=q153

⚪ **Low Priority** • **1 (15 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Multilevel hierarchy; Student (roll, name), Exam (marks[6]), Result computes total and displays full report.

**📝 Example PQP Question (2015-12 2(a)):**

Consider an example of declaring the examination result of BCA students of IGNOU. Design three classes : Student, Exam and Result. The Student class has data members such as those representing roll no., name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in 6 subjects. Derive the Result from the Exam class, and it has its own fields such as total marks. Write an interactive program to model this relationship by showing the three classes. Also, show how you can print out the values of each member of these classes. *(15 marks)*

> **🗓️ Asked In Papers:** [2015-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q154: What are istream and ostream member functions? Create base class QUEUE and derived class AQUEUE with an interactive Queue program. :id=q154

⚪ **Low Priority** • **1 (15 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

istream (get, getline, read, ignore), ostream (put, write, flush); QUEUE holds buffer/front/rear, AQUEUE adds interactive enqueue/dequeue/display.

**📝 Example PQP Question (BCAOL S3-15):**

What are istream and ostream member functions? Create a base class named QUEUE and a derived class AQUEUE. Write a program in C++ to show the operations on the Queue. Make necessary assumptions. *(15 marks)*

> **🗓️ Asked In Papers:** [BCAOL S3-15](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q155: What is reusability of code? Create student (name, address, age) and inherit PG_student with a function displaying name, address, subject. :id=q155

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Inherit PG_student : public student; add subject and display().

**📝 Example PQP Question (2013-06 3(b)):**

What is reusability of code ? Write a C++ program to create a class student, with basic data members such as name, address, age. Create a class PG_student by inheriting from student class. PG_student class should have a function to display, name, address, subject of the student. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore')

### Q156: Write a C++ program creating a Vehicle base class and deriving Car, Truck, and Bike with proper constructors. :id=q156

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Hierarchical inheritance; Vehicle(int wheels, float speed) invoked via initializer lists in Car, Truck, Bike.

**📝 Example PQP Question (2014-06 4(a)):**

Write a C++ program to create vehicle class and derive Car, Truck and Bike classes from the Vehicle class. Also define proper constructors for each of these classes. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore')

### Q157: Explain inheritance and multi-inheritance (multiple inheritance) with an example and C++ program. :id=q157

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Demonstrate single and class C : public A, public B with distinct base properties combined in C.

**📝 Example PQP Question (2015-12 5(a)):**

Explain Inheritance and Multi-Inheritance with an example. Write a C++ program which has Inheritance and Multi-Inheritance. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q158: What are base and derived classes? Create a base class Stack and derived class Mystack with an interactive C++ program showing stack operations. :id=q158

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Stack defines array/top and push/pop; Mystack adds overflow/underflow checks and menu loop.

**📝 Example PQP Question (2016-06 4(a)):**

What are base and derived classes ? Create a base class called Stack and a derived class called Mystack. Write an interactive C++ program to show the operations of a stack. *(10 marks)*

> **🗓️ Asked In Papers:** [2016-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore')

### Q159: Create Employee (name, address, age) and derive Part_time employee with a function displaying name, address, and payment. :id=q159

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Part_time : public Employee adds payment (or hours × rate) and display().

**📝 Example PQP Question (2017-12 5(a)):**

Write a program in C++ to create a class Employee with basic data members such as name, address, age. Create a class Part_time employee which inherits from the Employee class. Part_time class should have a function to display the name, address and payment of the part-time employee. *(10 marks)*

> **🗓️ Asked In Papers:** [2017-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q160: Explain ambiguity resolution in multiple inheritance, and what happens if a virtual function is not used in inheritance. :id=q160

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Ambiguity resolved via obj.BaseA::func() or virtual base class inheritance; omitting virtual on overridden methods causes static binding to base.

**📝 Example PQP Question (2017-06 1(b)):**

Explain ambiguity resolution in multiple inheritance. What happens if we don't use a virtual function in the inheritance ? *(6 marks)*

> **🗓️ Asked In Papers:** [2017-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore')

### Q161: Write a C++ program to implement multilevel inheritance with comments clarifying member availability across classes. :id=q161

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

A → B → C showing how private stops at A, protected flows to B/C, public stays public.

**📝 Example PQP Question (2014-12 1(e)):**

Write C++ program to implement multilevel inheritance. Provide the necessary comments to clarify the availability of data members and member functions in different classes. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore')

### Q162: Explain the usage of single inheritance and multiple inheritance. :id=q162

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Single extends specialized behavior (Animal → Dog); multiple combines orthogonal capabilities (Printer + Scanner → AllInOne).

**📝 Example PQP Question (2019-12 1(h)):**

Explain the usage of single inheritance and multiple inheritance. *(5 marks)*

> **🗓️ Asked In Papers:** [2019-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore')

### Q163: Compare multiple inheritance with multilevel and hierarchical inheritance. :id=q163

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Multiple: N parents → 1 child; Multilevel: chain A → B → C; Hierarchical: 1 parent → N children.

**📝 Example PQP Question (2021-12 4(b)):**

Compare multiple inheritance with multilevel inheritance and hierarchical inheritance. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q164: How is the protected access specifier different from public? Explain its usage for a subclass. :id=q164

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

public is accessible everywhere; protected hides members from external callers while keeping them accessible inside subclasses.

**📝 Example PQP Question (2023-06 1(b)):**

How is protected access specifier different from public access specifier ? Explain its usage for a subclass. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q165: How are parameterized constructors of a base class invoked by derived class constructors? :id=q165

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Using member initializer list: Derived(int x, int y) : Base(x) { ... }

**📝 Example PQP Question (2024-06 1(h)):**

How are the constructors of base class invoked by derived class constructors ? Discuss with reference to parameterized constructors. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q166: Can a derived class get access privilege for a private member of its base class? If yes, how? :id=q166

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Not directly via inheritance; possible via base's public/protected getter/setter methods or by declaring derived class/method as a friend.

**📝 Example PQP Question (2017-12S 1(j)):**

Can a derived class get access privilege for a private member of the base class ? If yes, how ? *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(j)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

