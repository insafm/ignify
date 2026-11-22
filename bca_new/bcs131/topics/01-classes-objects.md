# 01. Classes, Objects, Access, Friend & Static

> **Syllabus Unit:** Block 1 Unit 3 | **Rank:** #1 | **Frequency Score:** 155.3 | **Offered Marks:** 680 | **Papers Present:** 29/30 | **Importance:** Very High

---

## 📋 Topic Overview

This module covers **39 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q001](#q001) | What are access control specifiers (public, private, protected) in C++? Exp... | **15x** | 79 marks | Theory (+ Coding in 2015-06) / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q002](#q002) | What is a friend function in C++? Explain its properties, advantages, and i... | **10x** | 54 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q003](#q003) | What is an object in C++? Explain how an object can be passed as an argumen... | **7x** | 37 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q004](#q004) | What are static data members and static member functions of a class? Explai... | **6x** | 47 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q005](#q005) | What is the this pointer in C++? Explain its significance and usage with an... | **6x** | 31 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q006](#q006) | How is a struct (structure) different from a class in C++? Discuss their sy... | **4x** | 20 marks | Theory + Coding / Short Answer | <span class="badge badge-high">High</span> |
| [Q007](#q007) | How do we declare and define static data members of a class? Explain their ... | **4x** | 19 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q008](#q008) | Write a C++ program using a Matrix class (with constructor, destructor, and... | **3x** | 32 marks | Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q009](#q009) | Write a C++ program to implement a simple calculator (+, -, *, /) on two op... | **3x** | 30 marks | Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q010](#q010) | Write a C++ program to find the largest of three numbers using a member fun... | **3x** | 25 marks | Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q011](#q011) | How is memory allocation performed in C++ when a class is declared versus w... | **3x** | 25 marks | Theory / Long Answer | <span class="badge badge-high">High</span> |
| [Q012](#q012) | Define class and object. How are they related? Explain with an example. | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q013](#q013) | What is a static member function in C++? Explain how the static keyword cha... | **3x** | 14 marks | Theory + Coding / Short Answer | <span class="badge badge-high">High</span> |
| [Q014](#q014) | Write a C++ program to add two complex numbers by defining a Complex class ... | **2x** | 20 marks | Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q015](#q015) | Write a C++ program to multiply two complex numbers using a Complex class a... | **2x** | 20 marks | Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q016](#q016) | Explain two merits and two demerits of using friend functions with an examp... | **2x** | 18 marks | Theory / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q017](#q017) | Write a C++ program to create a Book class (publisher/title, author, price)... | **2x** | 17 marks | Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q018](#q018) | Write a C++ program to find the sum of n given numbers using a friend funct... | **2x** | 17 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q019](#q019) | Define a member function and briefly discuss its purpose in C++ with a suit... | **2x** | 10 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q020](#q020) | Write a C++ program to define class Circle with a constructor, a method for... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q021](#q021) | Write a C++ program to find the sum of n numbers by defining a proper class... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q022](#q022) | How does a friend function differ from a member function? Explain friend fu... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q023](#q023) | Write a C++ program for the subtraction of two matrices. | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q024](#q024) | Write a C++ program to create a STUDENT class (Name, Enrollment No, Program... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q025](#q025) | Write a program to add and subtract two instances of a Complex class using ... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q026](#q026) | Compare friend function with member function. Write a program to add two Di... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q027](#q027) | Create an Employee class allowing multiple constructors and methods to gene... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q028](#q028) | Differentiate between member functions defined inside vs. outside the body ... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q029](#q029) | What is an object? Explain creation and destruction using a Bank-Account cl... | **1x** | 8 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q030](#q030) | Define Member function and Friend function, and write the purpose of each. | **1x** | 8 marks | Theory / Long Answer | <span class="badge badge-low">Low</span> |
| [Q031](#q031) | How does a function behave differently when an object is passed by value ve... | **1x** | 6 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q032](#q032) | Write a C++ program to find the average of three given numbers by defining ... | **1x** | 5 marks | Coding / Short Answer | <span class="badge badge-low">Low</span> |
| [Q033](#q033) | Compare structures and classes, and explain what empty classes are and thei... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q034](#q034) | What is the utility of a friend function? Does it violate the rule of encap... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q035](#q035) | Differentiate between member functions and global functions with an example... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q036](#q036) | What is the this pointer? What happens on the statement delete this; inside... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q037](#q037) | Write a short note on array of objects with an example. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q038](#q038) | How does the working of a member function differ from a friend function and... | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q039](#q039) | What is an Object? Explain with an example how an object is instantiated in... | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q001">

### <span class="badge-qid">Q001</span> What are access control specifiers (public, private, protected) in C++? Explain their need, accessibility rules, and usage with examples.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 15 (79 marks)</span> <span class="badge badge-topic">Theory (+ Coding in 2015-06) / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

private (class/friends only; default in class), protected (class + derived classes), public (anywhere); enforces encapsulation and controlled data access.

> **🗓️ Asked In Papers:** `2012-12 3(a), 2014-06 4(c), 2015-06 2(b), 2017-06 1(e), 2019-06 2(b), 2019-12 1(b), 2020-06 1(d), 2020-12 5(ii), 2021-06 3(c), 2022-06 1(a), 2023-12 2(c), BCAOL S1-7, 2024-06 1(b), 2024-12 1(c), 2025-06 2(d)`

</div>

<div class="question-box" id="q002">

### <span class="badge-qid">Q002</span> What is a friend function in C++? Explain its properties, advantages, and implementation with an example program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 10 (54 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Declared inside class with friend keyword; non-member function accessing private/protected data; invoked without object; bridges two classes; not inherited or transitive.

> **🗓️ Asked In Papers:** `2012-12 4(c), 2014-12 4(c), 2017-06 5(c), 2017-12 1(e), 2018-06 4(a), 2019-12 1(d), 2020-12 1(f), 2021-06 1(d), 2021-12 3(a), 2023-12 3(d)`

</div>

<div class="question-box" id="q003">

### <span class="badge-qid">Q003</span> What is an object in C++? Explain how an object can be passed as an argument to a function with an example.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 7 (37 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Object is an instance of a class; passed by value (copy created), by reference (&), or by pointer (*) to manipulate or compare object states.

> **🗓️ Asked In Papers:** `2014-12 1(f), 2017-06 3(b), 2018-12S 3(b), 2019-06 1(f), 2020-12 1(e), 2021-06 1(c), 2024-06 1(f)`

</div>

<div class="question-box" id="q004">

### <span class="badge-qid">Q004</span> What are static data members and static member functions of a class? Explain their utility with an example program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (47 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

static data shared across all objects (initialized outside class using ::); static function accesses only static members and can be called via ClassName::func().

> **🗓️ Asked In Papers:** `2013-12 3(b), 2019-06 4(a), 2020-06 2(b), 2021-12 1(d), 2024-06 2(a), 2025-06 1(c)`

</div>

<div class="question-box" id="q005">

### <span class="badge-qid">Q005</span> What is the this pointer in C++? Explain its significance and usage with an example program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (31 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Implicit constant pointer passed to non-static member functions holding the invoking object's address; resolves variable shadowing and enables method chaining (return *this).

> **🗓️ Asked In Papers:** `2015-06 4(a), 2017-12 2(c), 2019-12 5(b), 2022-12 1(g), 2025-06 4(b), 2025-12 5(e)`

</div>

<div class="question-box" id="q006">

### <span class="badge-qid">Q006</span> How is a struct (structure) different from a class in C++? Discuss their syntax with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (20 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

Default member/inheritance access is public in struct vs. private in class; both support methods, constructors, and inheritance in C++.

> **🗓️ Asked In Papers:** `2014-06 1(f), 2019-06 3(c), 2020-12 1(d), 2025-12 1(a)`

</div>

<div class="question-box" id="q007">

### <span class="badge-qid">Q007</span> How do we declare and define static data members of a class? Explain their syntax, rules, and characteristics.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (19 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Declared inside class with static; defined once at file scope (type Class::var = val;); zero-initialized by default; lifetime equals entire program.

> **🗓️ Asked In Papers:** `2017-06 3(a), 2017-12 1(f), 2022-12 1(h), 2023-12 4(d)`

</div>

<div class="question-box" id="q008">

### <span class="badge-qid">Q008</span> Write a C++ program using a Matrix class (with constructor, destructor, and methods) to input and add two 3x3 matrices.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (32 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Class holds int m[3][3]; constructor initializes elements; destructor cleans up/logs; input(), add(Matrix), and display() nested loops.

> **🗓️ Asked In Papers:** `2012-12 2(a), 2017-06 1(c), 2020-06 4(b)`

</div>

<div class="question-box" id="q009">

### <span class="badge-qid">Q009</span> Write a C++ program to implement a simple calculator (+, -, *, /) on two operands using class methods for reading data and arithmetic operations.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (30 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Calculator class with a, b; read() method; switch(op) dispatching add(), sub(), mul(), div() with zero-divisor check.

> **🗓️ Asked In Papers:** `2013-06 2(c), 2017-12 5(b), 2020-12 4(b)`

</div>

<div class="question-box" id="q010">

### <span class="badge-qid">Q010</span> Write a C++ program to find the largest of three numbers using a member function (and constructor in NUMBER class) defined in a class.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (25 marks)</span> <span class="badge badge-topic">Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Class NUMBER with int a, b, c, constructor initializing values, and largest() using if-else comparisons.

> **🗓️ Asked In Papers:** `2013-06 1(b), 2013-12 3(a), 2019-12 1(f)`

</div>

<div class="question-box" id="q011">

### <span class="badge-qid">Q011</span> How is memory allocation performed in C++ when a class is declared versus when a class is instantiated (covering classes, objects, data members, member functions, and friend functions)?

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (25 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

Class declaration allocates no memory (blueprint only); instantiation allocates per-object memory for non-static data members, while member functions reside once in the code segment.

> **🗓️ Asked In Papers:** `2015-12 3(a), 2023-06 4(d), 2025-12 4(c)`

</div>

<div class="question-box" id="q012">

### <span class="badge-qid">Q012</span> Define class and object. How are they related? Explain with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Class is a user-defined blueprint bundling data and methods; object is a runtime instance allocating storage for that blueprint.

> **🗓️ Asked In Papers:** `2013-12 5(d), 2015-12 1(e), 2023-06 4(a)`

</div>

<div class="question-box" id="q013">

### <span class="badge-qid">Q013</span> What is a static member function in C++? Explain how the static keyword changes a function with a program.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (14 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

Belongs to the class rather than any object; lacks this pointer; accesses only static data/functions; invoked via Class::func().

> **🗓️ Asked In Papers:** `2021-06 3(a), 2023-06 4(b), BCAOL S1-6`

</div>

<div class="question-box" id="q014">

### <span class="badge-qid">Q014</span> Write a C++ program to add two complex numbers by defining a Complex class and proper constructor.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Complex class (float real, imag); constructor initializes; add(Complex) sums real and imaginary parts separately and returns/displays result.

> **🗓️ Asked In Papers:** `2015-06 1(e), 2026-06 3(a)`

</div>

<div class="question-box" id="q015">

### <span class="badge-qid">Q015</span> Write a C++ program to multiply two complex numbers using a Complex class and constructor.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Formula (a + bi)(c + di) = (ac - bd) + (ad + bc)i; Complex class with parameterized constructor and multiply(Complex) method.

> **🗓️ Asked In Papers:** `2017-12S 5(b), 2022-06 4(b)`

</div>

<div class="question-box" id="q016">

### <span class="badge-qid">Q016</span> Explain two merits and two demerits of using friend functions with an example.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (18 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

Merits: accesses private data of multiple classes, enables symmetrical binary operator overloading; Demerits: breaks strict encapsulation/data hiding, not inherited by subclasses.

> **🗓️ Asked In Papers:** `2013-12 1(d), 2020-06 5(b)`

</div>

<div class="question-box" id="q017">

### <span class="badge-qid">Q017</span> Write a C++ program to create a Book class (publisher/title, author, price) with proper constructor, destructor, and member functions to input/display records.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (17 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Book class with string title, author, publisher; float price;, constructor/destructor, getDetails(), and showDetails().

> **🗓️ Asked In Papers:** `2012-12 3(c), 2016-12 4(b)`

</div>

<div class="question-box" id="q018">

### <span class="badge-qid">Q018</span> Write a C++ program to find the sum of n given numbers using a friend function.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (17 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Class stores array/n; declares friend int calcSum(Series s); which loops 0..n-1 over s.arr[i] and returns sum.

> **🗓️ Asked In Papers:** `2015-06 2(a), 2019-06 2(a)`

</div>

<div class="question-box" id="q019">

### <span class="badge-qid">Q019</span> Define a member function and briefly discuss its purpose in C++ with a suitable example.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (10 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Function declared inside a class representing object behavior; operates directly on class data members via implicit this pointer.

> **🗓️ Asked In Papers:** `2015-12 2(b), 2022-12 1(f)`

</div>

<div class="question-box" id="q020">

### <span class="badge-qid">Q020</span> Write a C++ program to define class Circle with a constructor, a method for area (πr²), and a method for circumference (2πr).

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Circle(double r) constructor; area() returns 3.14159*r*r; circumference() returns 2*3.14159*r.

> **🗓️ Asked In Papers:** `2018-06 3(a)`

</div>

<div class="question-box" id="q021">

### <span class="badge-qid">Q021</span> Write a C++ program to find the sum of n numbers by defining a proper class, constructor, and methods.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Class takes n in constructor, reads n values into array/vector, and computes sum in a sum() method.

> **🗓️ Asked In Papers:** `2018-12S 2(b)`

</div>

<div class="question-box" id="q022">

### <span class="badge-qid">Q022</span> How does a friend function differ from a member function? Explain friend function implementation with a program.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Member function uses dot/arrow operator and this; friend function is non-member, takes object arguments explicitly, and bypasses private restriction.

> **🗓️ Asked In Papers:** `2022-12 3(b)`

</div>

<div class="question-box" id="q023">

### <span class="badge-qid">Q023</span> Write a C++ program for the subtraction of two matrices.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Input dimensions and two 2D arrays (or Matrix objects); subtract element-wise C[i][j] = A[i][j] - B[i][j] and print.

> **🗓️ Asked In Papers:** `BCAOL S2-8`

</div>

<div class="question-box" id="q024">

### <span class="badge-qid">Q024</span> Write a C++ program to create a STUDENT class (Name, Enrollment No, Programme) with constructor and member functions.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

STUDENT class with parameterized/default constructor, getDetails(), and displayDetails().

> **🗓️ Asked In Papers:** `BCAOL S2-10`

</div>

<div class="question-box" id="q025">

### <span class="badge-qid">Q025</span> Write a program to add and subtract two instances of a Complex class using a friend function and parameterized constructor.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Complex(float r, float i); friend Complex add(Complex, Complex); and friend Complex sub(Complex, Complex);

> **🗓️ Asked In Papers:** `2024-06 3(b)`

</div>

<div class="question-box" id="q026">

### <span class="badge-qid">Q026</span> Compare friend function with member function. Write a program to add two Distance instances (km, m) using a friend function and parameterized constructor.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Convert excess m >= 1000 into km += m / 1000; m %= 1000; inside friend addDist(Distance, Distance).

> **🗓️ Asked In Papers:** `2024-12 3(a)`

</div>

<div class="question-box" id="q027">

### <span class="badge-qid">Q027</span> Create an Employee class allowing multiple constructors and methods to generate a salary report for 5 employees.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Overloaded constructors (default + parameterized); array Employee emp[5]; calculateNetSalary() and displayReport().

> **🗓️ Asked In Papers:** `2024-12 3(b)`

</div>

<div class="question-box" id="q028">

### <span class="badge-qid">Q028</span> Differentiate between member functions defined inside vs. outside the body of a class. How are inline member functions defined outside the class?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Inside-class definitions are implicitly inline; outside-class definitions use ReturnType ClassName::func() and require explicit inline keyword to be inlined.

> **🗓️ Asked In Papers:** `2024-12 4(b)`

</div>

<div class="question-box" id="q029">

### <span class="badge-qid">Q029</span> What is an object? Explain creation and destruction using a Bank-Account class (name, account-number, balance, display balance).

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (8 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Objects created via constructor upon declaration/new and destroyed via destructor at scope exit/delete; demonstrate with BankAccount class.

> **🗓️ Asked In Papers:** `2012-12 1(d)`

</div>

<div class="question-box" id="q030">

### <span class="badge-qid">Q030</span> Define Member function and Friend function, and write the purpose of each.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (8 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

Member function defines intrinsic object behavior; friend function provides controlled external access across unrelated classes or symmetric operations.

> **🗓️ Asked In Papers:** `2018-12S 3(a)`

</div>

<div class="question-box" id="q031">

### <span class="badge-qid">Q031</span> How does a function behave differently when an object is passed by value versus passed by reference?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (6 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

By value invokes copy constructor and modifies only local copy; by reference aliases caller's object (no copy, changes persist).

> **🗓️ Asked In Papers:** `2017-12 2(a)`

</div>

<div class="question-box" id="q032">

### <span class="badge-qid">Q032</span> Write a C++ program to find the average of three given numbers by defining an appropriate class and methods.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Coding / Short Answer</span>

**💡 Key Answer Points:**

Average class reading 3 floats, computing (a+b+c)/3.0 in a method, and displaying result.

> **🗓️ Asked In Papers:** `2020-12 2(c)`

</div>

<div class="question-box" id="q033">

### <span class="badge-qid">Q033</span> Compare structures and classes, and explain what empty classes are and their purpose in C++.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Empty class (class E {};) has no data members (sizeof(E) == 1 for unique address); used as tag/marker types, traits, or placeholders.

> **🗓️ Asked In Papers:** `2021-12 1(c)`

</div>

<div class="question-box" id="q034">

### <span class="badge-qid">Q034</span> What is the utility of a friend function? Does it violate the rule of encapsulation?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Allows controlled non-member access; technically relaxes strict encapsulation, though declared explicitly by the class designer (so trust boundary stays intact).

> **🗓️ Asked In Papers:** `2023-06 1(d)`

</div>

<div class="question-box" id="q035">

### <span class="badge-qid">Q035</span> Differentiate between member functions and global functions with an example.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Member functions sit in class scope with this and access private members; global functions live in global namespace without class access.

> **🗓️ Asked In Papers:** `2023-06 4(c)`

</div>

<div class="question-box" id="q036">

### <span class="badge-qid">Q036</span> What is the this pointer? What happens on the statement delete this; inside a class?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

delete this; deallocates the object if allocated via new; valid only if no member data/virtual calls are accessed afterward (otherwise undefined behavior; crashes on stack objects).

> **🗓️ Asked In Papers:** `2024-12 1(d)`

</div>

<div class="question-box" id="q037">

### <span class="badge-qid">Q037</span> Write a short note on array of objects with an example.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

ClassName arr[N]; creates N contiguous objects calling default constructor N times; accessed via arr[i].method().

> **🗓️ Asked In Papers:** `2024-12 1(g)`

</div>

<div class="question-box" id="q038">

### <span class="badge-qid">Q038</span> How does the working of a member function differ from a friend function and a non-member function?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Member: obj.f(), has this, full private access; Friend: f(obj), no this, private access; Non-member: f(obj), no this, public access only.

> **🗓️ Asked In Papers:** `2017-12S 1(f)`

</div>

<div class="question-box" id="q039">

### <span class="badge-qid">Q039</span> What is an Object? Explain with an example how an object is instantiated in C++.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Instantiated statically on stack (Student s1;) or dynamically on heap (Student* s2 = new Student();).

> **🗓️ Asked In Papers:** `2017-12S 1(i)`

</div>

