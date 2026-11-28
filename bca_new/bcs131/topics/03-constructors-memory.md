# 03. Constructors, Destructors & Memory Management

> **Syllabus Unit:** Block 1 Unit 4 | **Rank:** #3 | **Frequency Score:** 91.5 | **Offered Marks:** 331 | **Papers Present:** 27/30 | **Importance:** Very High
> **Coverage:** 20 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q059: Explain the concept of a copy constructor in C++ with an example program. :id=q059

🔴 **Very High Priority** • **9 (55 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

ClassName(const ClassName& obj); initializes a new object from an existing one; prevents shallow-copy pointer bugs.

**📝 Example PQP Question (BCAOL S2-13):**

What is a copy constructor? Explain its use with an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2014-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2018-12S 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2019-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2020-12 5(i)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [BCAOL S2-13](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2025-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q060: What is a destructor in C++? Explain its role in memory management and its need with an example program. :id=q060

🔴 **Very High Priority** • **7 (32 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

~ClassName() invoked automatically when object leaves scope or is deleted; frees dynamic heap resources (delete/delete[]) preventing memory leaks.

**📝 Example PQP Question (2025-06 1(g)):**

What are destructors in C++? Explain the role of destructors in memory management with suitable example code in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2017-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2018-06 5(c-i)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2019-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2021-12 3(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2022-12 5(iv)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q061: Differentiate between a default constructor and a parameterized constructor with an example. :id=q061

🟠 **High Priority** • **4 (26 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Default takes zero arguments (or all defaults); parameterized accepts arguments to initialize distinct object states at creation.

**📝 Example PQP Question (2019-06 2(c)):**

Differentiate between default constructor and parameterized constructor with the help of an example program in C++. 7 (A-27) I3/ BCS-031

> **🗓️ Asked In Papers:** [2015-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2017-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2019-06 2(c)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2021-06 5(c-i)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q062: What are constructors? List five characteristics and discuss the limitations of constructors. :id=q062

🟠 **High Priority** • **4 (25 marks)** • *Theory (+ Coding in 2014-12) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Characteristics: same name as class, no return type, public normally, auto-invoked, overloadable; Limitations: cannot be virtual, static, const, or inherited directly.

**📝 Example PQP Question (2025-12 1(c)):**

What are constructors? Write the characteristics of constructors. Also discuss the limitations of constructors. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2021-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2025-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q063: What is constructor overloading in C++? Explain with an example. :id=q063

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Defining multiple constructors in one class differing in parameter count or types to allow flexible object initialization.

**📝 Example PQP Question (2025-06 2(b)):**

Explain, how constructor overloading is performed in C++ with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2018-12S 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2022-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2023-12 2(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q064: What is the need for memory management in C++, and how is the memory management process performed? :id=q064

🟠 **High Priority** • **4 (19 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Allocates exact runtime sizes on heap (free store) and prevents leaks/exhaustion using new, new[], delete, and delete[].

**📝 Example PQP Question (2020-06 1(e)):**

Explain, how memory management is performed in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2019-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2025-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q065: Differentiate between a copy constructor and a default constructor with an example for each. :id=q065

🟠 **High Priority** • **3 (22 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Default initializes with zero/default values; copy constructor takes const ClassName& to clone an existing object's state.

**📝 Example PQP Question (2026-06 4(b)):**

What is a Copy Constructor? How does it differ from Default Constructor? Explain with an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2016-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2022-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2026-06 4(b)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q066: What is meant by object initialization, and why is it required? Explain with suitable examples. :id=q066

🟠 **High Priority** • **3 (16 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Assigning valid initial values upon creation; prevents garbage/uninitialized state errors; automated cleanly by constructors.

**📝 Example PQP Question (2019-12 1(g)):**

What is Object initialization? Why it is required, explain with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2019-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2019-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore')

### Q067: What is a constructor? Explain the advantages of using constructors with an example. :id=q067

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Special member function invoked automatically at instantiation; guarantees valid initialization, supports overloading and dynamic allocation.

**📝 Example PQP Question (2020-12 1(a)):**

What is construction? Explain the advantages of construction with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2018-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2020-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q068: Explain the role of new and delete operators in C++ memory management. :id=q068

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

new allocates heap memory and calls constructor (type-safe, no sizeof/cast needed); delete calls destructor and frees memory.

**📝 Example PQP Question (2023-06 5(c)):**

What is the role of new operator in C++? Explain. Also explain delete operator. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2021-12 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q069: Write a C++ program to calculate the factorial of a given number using a copy constructor (with comments). :id=q069

🔵 **Medium Priority** • **2 (18 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Class stores n; copy constructor copies obj.n into a second object; method loops 1..n to compute fact.

**📝 Example PQP Question (2017-06 4(b)):**

Write a program to calculate the factorial of a given number by using copy constructor. Also write comments in your program wherever required. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2017-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore')

### Q070: Explain the process of memory deallocation in C++ with an example. :id=q070

🔵 **Medium Priority** • **2 (15 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Releasing heap objects via delete ptr; and arrays via delete[] arr;, triggering destructors and setting pointer to nullptr to avoid dangling pointers.

**📝 Example PQP Question (2026-06 1(d)):**

Explain the process of memory deallocation in C++ with the help of an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2023-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2026-06 1(d)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q071: Discuss the situations when a copy constructor is automatically invoked in C++. :id=q071

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

(1) Initializing one object from another (A b = a; or A b(a);), (2) Passing object by value, (3) Returning object by value.

**📝 Example PQP Question (2017-12S 1(g)):**

What is a Copy Constructor? Discuss the situations when a copy constructor is automatically invoked. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2023-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q072: Write a C++ program to print Student details (Name, Father's Name, Mother's Name, Address, Zip code, Roll No) using constructor and destructor. :id=q072

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Student class initializing all 6 fields in constructor and displaying/cleaning up via method and destructor.

**📝 Example PQP Question (2015-12 3(b)):**

Write a C++ program to print Student details: Student Name, Father's Name, Mother's Name, Student Address, Zip code, Student Roll No. using constructor and destructor. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q073: Write a short note on Parameterized Constructor. :id=q073

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Constructor accepting one or more arguments to assign user-supplied values during object creation.

**📝 Example PQP Question (2016-12 5(b)):**

Write a short note on: Parameterized Constructor *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore')

### Q074: How does a constructor differ from automatic initialization? Briefly discuss copy constructor. :id=q074

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Built-in types lack automatic non-zero initialization (int x; holds garbage); constructors enforce deterministic initialization of complex classes.

**📝 Example PQP Question (2021-06 1(e)):**

How does Constructor differ from Automatic Initialization? Briefly discuss the term Copy Constructor. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q075: Discuss naming conventions of destructors. Do constructors and destructors have a return type? :id=q075

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Tilde prefix (~ClassName()); takes no arguments, cannot be overloaded; neither constructors nor destructors have any return type (not even void).

**📝 Example PQP Question (2021-06 3(b)):**

What is a Destructor in C++? Discuss the naming conventions of destructor. Do constructors and destructors have return type? *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q076: What are private constructors and destructors? How do they differ from non-private ones? :id=q076

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Prevent direct external instantiation/destruction; used in Singleton patterns, factory methods, or heap-only objects.

**📝 Example PQP Question (2023-06 5(b)):**

What are private constructors and destructors? How are they different from constructors and destructors which are not private? Explain. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q077: Discuss the order of constructor and destructor calls in an inheritance hierarchy with a program. :id=q077

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Constructors execute top-down (Base then Derived); destructors execute in strict reverse order (Derived then Base).

**📝 Example PQP Question (2023-12 3(c)):**

For classes in inheritance hierarchy, discuss the order of constructor and destructor call with the help of a program. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-12 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q078: What is a Default Constructor? How is a default constructor equivalent to a constructor with default arguments? :id=q078

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

A constructor where every parameter has a default value (A(int x=0)) can be called with zero arguments, acting identically to a default constructor.

**📝 Example PQP Question (2017-12 1(g)):**

What do you understand by a Default Constructor? How is a default constructor equivalent to a constructor with default arguments? *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

