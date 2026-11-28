# 01. Classes, Objects, Access, Friend & Static

> **Syllabus Unit:** Block 1 Unit 3 | **Rank:** #1 | **Frequency Score:** 155.3 | **Offered Marks:** 680 | **Papers Present:** 29/30 | **Importance:** Very High
> **Coverage:** 39 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q001: What are access control specifiers (public, private, protected) in C++? Explain their need, accessibility rules, and usage with examples. :id=q001

🔴 **Very High Priority** • **15 (79 marks)** • *Theory (+ Coding in 2015-06) / Short Answer & Long Answer*

**💡 Key Answer Points:**

private (class/friends only; default in class), protected (class + derived classes), public (anywhere); enforces encapsulation and controlled data access.

**📝 Example PQP Question (2025-06 2(d)):**

What is an access specifier? Explain different types of access specifiers available in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2014-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2015-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2017-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2019-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2019-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2020-12 5(ii)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 3(c)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2022-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2023-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [BCAOL S1-7](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2024-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2024-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore'), [2025-06 2(d)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q002: What is a friend function in C++? Explain its properties, advantages, and implementation with an example program. :id=q002

🔴 **Very High Priority** • **10 (54 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Declared inside class with friend keyword; non-member function accessing private/protected data; invoked without object; bridges two classes; not inherited or transitive.

**📝 Example PQP Question (2023-12 3(d)):**

What is friend function? Explain the advantage of friend function. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2014-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2017-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2017-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2018-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2019-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2021-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-12 3(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q003: What is an object in C++? Explain how an object can be passed as an argument to a function with an example. :id=q003

🔴 **Very High Priority** • **7 (37 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Object is an instance of a class; passed by value (copy created), by reference (&), or by pointer (*) to manipulate or compare object states.

**📝 Example PQP Question (2024-06 1(f)):**

What is an object? How is it passed as a parameter? *(5 marks)*

> **🗓️ Asked In Papers:** [2014-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2017-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2018-12S 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2019-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2024-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q004: What are static data members and static member functions of a class? Explain their utility with an example program. :id=q004

🔴 **Very High Priority** • **6 (47 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

static data shared across all objects (initialized outside class using ::); static function accesses only static members and can be called via ClassName::func().

**📝 Example PQP Question (2025-06 1(c)):**

What are the static members of a class? Discuss the utility of having static members with the help of an example. 5

> **🗓️ Asked In Papers:** [2013-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2019-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2021-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2024-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2025-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q005: What is the this pointer in C++? Explain its significance and usage with an example program. :id=q005

🔴 **Very High Priority** • **6 (31 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Implicit constant pointer passed to non-static member functions holding the invoking object's address; resolves variable shadowing and enables method chaining (return *this).

**📝 Example PQP Question (2025-06 4(b)):**

What is ‘this’ pointer in C++? Explain the significance of ‘this’ pointer with the help of an example program. *(5 marks)*

> **🗓️ Asked In Papers:** [2015-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2017-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2019-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2022-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2025-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2025-12 5(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q006: How is a struct (structure) different from a class in C++? Discuss their syntax with an example. :id=q006

🟠 **High Priority** • **4 (20 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Default member/inheritance access is public in struct vs. private in class; both support methods, constructors, and inheritance in C++.

**📝 Example PQP Question (2025-12 1(a)):**

Compare structure and classes in C++. Discuss the syntax of both with suitable code. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2019-06 3(c)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2025-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q007: How do we declare and define static data members of a class? Explain their syntax, rules, and characteristics. :id=q007

🟠 **High Priority** • **4 (19 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Declared inside class with static; defined once at file scope (type Class::var = val;); zero-initialized by default; lifetime equals entire program.

**📝 Example PQP Question (2023-12 4(d)):**

What is the purpose of static keyword in C++? What happens when it is appended before a variable in C++? Explain. *(5 marks)*

> **🗓️ Asked In Papers:** [2017-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2017-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2022-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-12 4(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q008: Write a C++ program using a Matrix class (with constructor, destructor, and methods) to input and add two 3x3 matrices. :id=q008

🟠 **High Priority** • **3 (32 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Class holds int m[3][3]; constructor initializes elements; destructor cleans up/logs; input(), add(Matrix), and display() nested loops.

**📝 Example PQP Question (2020-06 4(b)):**

Write a program in C++ to add two 3 x. 3 matrices. Define proper class, constructor, destructor and methods in the program. 12

> **🗓️ Asked In Papers:** [2012-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2017-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2020-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore')

### Q009: Write a C++ program to implement a simple calculator (+, -, *, /) on two operands using class methods for reading data and arithmetic operations. :id=q009

🟠 **High Priority** • **3 (30 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Calculator class with a, b; read() method; switch(op) dispatching add(), sub(), mul(), div() with zero-divisor check.

**📝 Example PQP Question (2020-12 4(b)):**

Write a C++ program to implement simple calculator to perform ‘+’, ‘–’, ‘*’, ‘/’ on two operands. Your program should have methods for reading data and for performing arithmetic operations. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 2(c)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2017-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2020-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q010: Write a C++ program to find the largest of three numbers using a member function (and constructor in NUMBER class) defined in a class. :id=q010

🟠 **High Priority** • **3 (25 marks)** • *Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Class NUMBER with int a, b, c, constructor initializing values, and largest() using if-else comparisons.

**📝 Example PQP Question (2019-12 1(f)):**

Write a program in C++, to find the largest of given three numbers by using a member function defined in a class. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2013-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2019-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore')

### Q011: How is memory allocation performed in C++ when a class is declared versus when a class is instantiated (covering classes, objects, data members, member functions, and friend functions)? :id=q011

🟠 **High Priority** • **3 (25 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Class declaration allocates no memory (blueprint only); instantiation allocates per-object memory for non-static data members, while member functions reside once in the code segment.

**📝 Example PQP Question (2025-12 4(c)):**

In C++, how memory allocation is performed: *(5 marks)*

> **🗓️ Asked In Papers:** [2015-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2023-06 4(d)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2025-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q012: Define class and object. How are they related? Explain with an example. :id=q012

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Class is a user-defined blueprint bundling data and methods; object is a runtime instance allocating storage for that blueprint.

**📝 Example PQP Question (2023-06 4(a)):**

Define the term class. How are class and object related? Explain with example. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2015-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2023-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q013: What is a static member function in C++? Explain how the static keyword changes a function with a program. :id=q013

🟠 **High Priority** • **3 (14 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Belongs to the class rather than any object; lacks this pointer; accesses only static data/functions; invoked via Class::func().

**📝 Example PQP Question (BCAOL S1-6):**

What is a static member function in C++? Explain with an example. *(4 marks)*

> **🗓️ Asked In Papers:** [2021-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2023-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [BCAOL S1-6](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q014: Write a C++ program to add two complex numbers by defining a Complex class and proper constructor. :id=q014

🔵 **Medium Priority** • **2 (20 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Complex class (float real, imag); constructor initializes; add(Complex) sums real and imaginary parts separately and returns/displays result.

**📝 Example PQP Question (2026-06 3(a)):**

Write a program in C++ for addition of two complex numbers. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2026-06 3(a)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q015: Write a C++ program to multiply two complex numbers using a Complex class and constructor. :id=q015

🔵 **Medium Priority** • **2 (20 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Formula (a + bi)(c + di) = (ac - bd) + (ad + bc)i; Complex class with parameterized constructor and multiply(Complex) method.

**📝 Example PQP Question (2022-06 4(b)):**

Write a program in C++ to multiply two complex numbers. In this program you need to create a complex class and define a proper constructor for object initialization. Give suitable comments in your program. *(10 marks)*

> **🗓️ Asked In Papers:** [2017-12S 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2022-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore')

### Q016: Explain two merits and two demerits of using friend functions with an example. :id=q016

🔵 **Medium Priority** • **2 (18 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Merits: accesses private data of multiple classes, enables symmetrical binary operator overloading; Demerits: breaks strict encapsulation/data hiding, not inherited by subclasses.

**📝 Example PQP Question (2013-12 1(d)):**

What are friend functions? Explain two merits and two demerits of using friend functions, with the help of an example. *(8 marks)*

> **🗓️ Asked In Papers:** [2013-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2020-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore')

### Q017: Write a C++ program to create a Book class (publisher/title, author, price) with proper constructor, destructor, and member functions to input/display records. :id=q017

🔵 **Medium Priority** • **2 (17 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Book class with string title, author, publisher; float price;, constructor/destructor, getDetails(), and showDetails().

**📝 Example PQP Question (2016-12 4(b)):**

Write a C++ program to create a Book class. Define constructor and destructor for this class. Also define the methods to show the title and price of the books.

> **🗓️ Asked In Papers:** [2012-12 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2016-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore')

### Q018: Write a C++ program to find the sum of n given numbers using a friend function. :id=q018

🔵 **Medium Priority** • **2 (17 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Class stores array/n; declares friend int calcSum(Series s); which loops 0..n-1 over s.arr[i] and returns sum.

**📝 Example PQP Question (2019-06 2(a)):**

What do you understand by friend function? Write a C++ program, to find out the sum of n given numbers using friend function. 7

> **🗓️ Asked In Papers:** [2015-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2019-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

### Q019: Define a member function and briefly discuss its purpose in C++ with a suitable example. :id=q019

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Function declared inside a class representing object behavior; operates directly on class data members via implicit this pointer.

**📝 Example PQP Question (2022-12 1(f)):**

What is a member function? Briefly discuss the purpose of member function in C++, with suitable example. *(5 marks)*

> **🗓️ Asked In Papers:** [2015-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2022-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q020: Write a C++ program to define class Circle with a constructor, a method for area (πr²), and a method for circumference (2πr). :id=q020

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Circle(double r) constructor; area() returns 3.14159*r*r; circumference() returns 2*3.14159*r.

**📝 Example PQP Question (2018-06 3(a)):**

Write a C++ program to define class "Circle" and implement the following: *(10 marks)*

> **🗓️ Asked In Papers:** [2018-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore')

### Q021: Write a C++ program to find the sum of n numbers by defining a proper class, constructor, and methods. :id=q021

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Class takes n in constructor, reads n values into array/vector, and computes sum in a sum() method.

**📝 Example PQP Question (2018-12S 2(b)):**

Write a C++ program to find out the sum of n numbers, by defining proper class, constructor and methods. *(10 marks)*

> **🗓️ Asked In Papers:** [2018-12S 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q022: How does a friend function differ from a member function? Explain friend function implementation with a program. :id=q022

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Member function uses dot/arrow operator and this; friend function is non-member, takes object arguments explicitly, and bypasses private restriction.

**📝 Example PQP Question (2022-12 3(b)):**

What is a friend function? How does it differ from the member function? Explain the implementation of friend function in C++, with the help of an example program. *(10 marks)*

> **🗓️ Asked In Papers:** [2022-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q023: Write a C++ program for the subtraction of two matrices. :id=q023

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Input dimensions and two 2D arrays (or Matrix objects); subtract element-wise C[i][j] = A[i][j] - B[i][j] and print.

**📝 Example PQP Question (BCAOL S2-8):**

Write a Program in C++ for the substraction of two matrices. *(10 marks)*

> **🗓️ Asked In Papers:** [BCAOL S2-8](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q024: Write a C++ program to create a STUDENT class (Name, Enrollment No, Programme) with constructor and member functions. :id=q024

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

STUDENT class with parameterized/default constructor, getDetails(), and displayDetails().

**📝 Example PQP Question (BCAOL S2-10):**

Write a program in C++ to create a class STUDENT to keep information of all students in a university. The program should have constructor and member functions to get the details such as Name of the student, His/Her Enrollment Number, His/Her Programme of study etc. Make necessary assumptions. *(10 marks)*

> **🗓️ Asked In Papers:** [BCAOL S2-10](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q025: Write a program to add and subtract two instances of a Complex class using a friend function and parameterized constructor. :id=q025

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Complex(float r, float i); friend Complex add(Complex, Complex); and friend Complex sub(Complex, Complex);

**📝 Example PQP Question (2024-06 3(b)):**

Write a program to add and subtract two instances of a complex number class (having data members real and imaginary). Make use of a friend function for the same. The class should make use of a parameterized constructor for creating and initializing the data members. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q026: Compare friend function with member function. Write a program to add two Distance instances (km, m) using a friend function and parameterized constructor. :id=q026

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Convert excess m >= 1000 into km += m / 1000; m %= 1000; inside friend addDist(Distance, Distance).

**📝 Example PQP Question (2024-12 3(a)):**

What is the friend function? Compare friend function with a member function. Write a program to add two instances of distance class (having data members kilometres and metres). Make use of a friend function for the same. The class should make use of parameterized construct for creating and initializing the data members. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q027: Create an Employee class allowing multiple constructors and methods to generate a salary report for 5 employees. :id=q027

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Overloaded constructors (default + parameterized); array Employee emp[5]; calculateNetSalary() and displayReport().

**📝 Example PQP Question (2024-12 3(b)):**

Create a class named employee. Allow multiple constructors in it. Create methods to generate salary report of each employee. The program in C++ should display the details of 5 employees. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q028: Differentiate between member functions defined inside vs. outside the body of a class. How are inline member functions defined outside the class? :id=q028

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Inside-class definitions are implicitly inline; outside-class definitions use ReturnType ClassName::func() and require explicit inline keyword to be inlined.

**📝 Example PQP Question (2024-12 4(b)):**

What is the difference between member function defined inside and outside the body of a class? How are inline member functions defined outside the body of a class? Explain with example. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q029: What is an object? Explain creation and destruction using a Bank-Account class (name, account-number, balance, display balance). :id=q029

⚪ **Low Priority** • **1 (8 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Objects created via constructor upon declaration/new and destroyed via destructor at scope exit/delete; demonstrate with BankAccount class.

**📝 Example PQP Question (2012-12 1(d)):**

What is an object? Explain how objects in C++ are created and destroyed, with the help of program to create Bank-Account Class, having data members name, accountnumber, balance and member function display balance. *(8 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore')

### Q030: Define Member function and Friend function, and write the purpose of each. :id=q030

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Member function defines intrinsic object behavior; friend function provides controlled external access across unrelated classes or symmetric operations.

**📝 Example PQP Question (2018-12S 3(a)):**

Define Member function and Friend function. Write the purpose of each. *(8 marks)*

> **🗓️ Asked In Papers:** [2018-12S 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q031: How does a function behave differently when an object is passed by value versus passed by reference? :id=q031

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

By value invokes copy constructor and modifies only local copy; by reference aliases caller's object (no copy, changes persist).

**📝 Example PQP Question (2017-12 2(a)):**

How does the functioning of a function differ when

> **🗓️ Asked In Papers:** [2017-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q032: Write a C++ program to find the average of three given numbers by defining an appropriate class and methods. :id=q032

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Average class reading 3 floats, computing (a+b+c)/3.0 in a method, and displaying result.

**📝 Example PQP Question (2020-12 2(c)):**

Write a C++ program to find the average three given numbers. Define appropriate class and methods in the program. *(5 marks)*

> **🗓️ Asked In Papers:** [2020-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q033: Compare structures and classes, and explain what empty classes are and their purpose in C++. :id=q033

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Empty class (class E {};) has no data members (sizeof(E) == 1 for unique address); used as tag/marker types, traits, or placeholders.

**📝 Example PQP Question (2021-12 1(c)):**

Compare structures and classes in C++. What are empty classes? Explain the purpose of empty classes. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q034: What is the utility of a friend function? Does it violate the rule of encapsulation? :id=q034

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Allows controlled non-member access; technically relaxes strict encapsulation, though declared explicitly by the class designer (so trust boundary stays intact).

**📝 Example PQP Question (2023-06 1(d)):**

What is the utility of friend function? Does it violate the rule of encapsulation? *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q035: Differentiate between member functions and global functions with an example. :id=q035

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Member functions sit in class scope with this and access private members; global functions live in global namespace without class access.

**📝 Example PQP Question (2023-06 4(c)):**

Differentiate between member functions and global functions with help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q036: What is the this pointer? What happens on the statement delete this; inside a class? :id=q036

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

delete this; deallocates the object if allocated via new; valid only if no member data/virtual calls are accessed afterward (otherwise undefined behavior; crashes on stack objects).

**📝 Example PQP Question (2024-12 1(d)):**

What is this pointer? What happens on the statement: “delete this” in a class? 5

> **🗓️ Asked In Papers:** [2024-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q037: Write a short note on array of objects with an example. :id=q037

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

ClassName arr[N]; creates N contiguous objects calling default constructor N times; accessed via arr[i].method().

**📝 Example PQP Question (2024-12 1(g)):**

Write a short note on array of objects with example. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q038: How does the working of a member function differ from a friend function and a non-member function? :id=q038

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Member: obj.f(), has this, full private access; Friend: f(obj), no this, private access; Non-member: f(obj), no this, public access only.

**📝 Example PQP Question (2017-12S 1(f)):**

How is the working of a member function different from a friend function and a non-member function? *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

### Q039: What is an Object? Explain with an example how an object is instantiated in C++. :id=q039

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Instantiated statically on stack (Student s1;) or dynamically on heap (Student* s2 = new Student();).

**📝 Example PQP Question (2017-12S 1(i)):**

What is an Object? Explain with an example, how an object is instantiated. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(i)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

