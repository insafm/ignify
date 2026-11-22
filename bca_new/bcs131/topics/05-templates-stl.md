# 05. Templates & Standard Template Library (STL)

> **Syllabus Unit:** Block 3 Unit 2 | **Rank:** #5 | **Frequency Score:** 83.0 | **Offered Marks:** 340 | **Papers Present:** 30/30 | **Importance:** High
> **Coverage:** 19 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q115: What are Containers (Containership) in C++? List the main types of containers with examples, their importance, and common member functions. :id=q115

🔴 **Very High Priority** • **7 (54 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Sequence (vector, list, deque), Associative (set, map), Container Adapters (stack, queue, priority_queue); common functions: size(), empty(), begin(), end(), clear().

> **🗓️ Asked In Papers:** `2013-12 4(c), 2014-12 5(a), 2015-06 5(a), 2015-12 1(f), 2019-12 5(c), 2020-06 2(a), 2025-06 5(e)`

### Q116: What is a class template? Explain its concept, advantages, and utility. :id=q116

🟠 **High Priority** • **5 (23 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

template <class T> class Box {...}; creates type-independent generic data structures/classes, eliminating code duplication while preserving type safety.

> **🗓️ Asked In Papers:** `2016-12 5(c), 2020-12 2(b), 2021-12 5(d), 2023-12 5(b), 2025-06 5(a)`

### Q117: Differentiate between a class template and a function template with an example for each. :id=q117

🟠 **High Priority** • **4 (31 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Function template parameterizes a single algorithm (template<typename T> T add(T,T)); class template parameterizes an entire class's data members and methods.

> **🗓️ Asked In Papers:** `2014-12 1(d), 2016-06 3(a), 2019-12 2(a), 2021-06 5(b)`

### Q118: What is a function template in C++? Explain its advantages with an example. :id=q118

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Blueprint for generic functions deduced at compile time (template <class T>); reduces redundancy and maintenance effort.

> **🗓️ Asked In Papers:** `2014-06 1(d), 2019-06 4(c), 2021-12 5(e), 2026-06 3(b)`

### Q119: Explain the use of the STL list container class with an example program. :id=q119

🟠 **High Priority** • **4 (21 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Doubly-linked list (<list>); O(1) insertion/deletion anywhere via push_back(), push_front(), sort(), reverse(), and iterators.

> **🗓️ Asked In Papers:** `2018-06 5(a), 2022-12 1(c), 2023-12 1(f), 2025-12 4(b)`

### Q120: What is a template class? Give its advantages and create a template class for the Linked List data structure. :id=q120

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> struct Node { T data; Node* next; }; inside template<class T> class LinkedList with insert(), deleteNode(), display().

> **🗓️ Asked In Papers:** `2013-06 4(b), 2017-12S 4(a), 2022-12 2(b)`

### Q121: What is a class template? Create a class template for a Stack data structure. :id=q121

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class Stack with T arr[MAX]; int top;, push(T), pop(), peek(), overflow/underflow checks.

> **🗓️ Asked In Papers:** `2018-06 4(b), 2022-06 2(b), 2025-12 3(b)`

### Q122: What is STL (Standard Template Library)? Briefly discuss its components and importance in C++. :id=q122

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Core components: Containers (data storage), Algorithms (sort, find), Iterators (pointer-like traversal), and Function Objects/Functors.

> **🗓️ Asked In Papers:** `2021-12 1(g), 2023-06 1(h), 2025-06 1(d)`

### Q123: What is a template function? Write a template function to swap the values of two numbers. :id=q123

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template <typename T> void mySwap(T& a, T& b) { T temp = a; a = b; b = temp; }

> **🗓️ Asked In Papers:** `2015-06 4(c), 2024-06 3(a)`

### Q124: What is a function template? Write a function template SUM to add two numbers. :id=q124

🔵 **Medium Priority** • **2 (11 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

template <class T> T SUM(T a, T b) { return a + b; } tested with int and float/double.

> **🗓️ Asked In Papers:** `2012-12 1(f), 2020-12 1(b)`

### Q125: What are templates in C++? Explain their advantages with an example. :id=q125

⚪ **Low Priority** • **1 (15 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Generic programming mechanism enabling type-parameterized functions and classes compiled on demand.

> **🗓️ Asked In Papers:** `BCAOL S3-17`

### Q126: Write an OOP program in C++ to read n integers and print the array in reverse order using a class template. :id=q126

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class ArrayRev storing dynamic/fixed array T a[] and printing from n-1 down to 0.

> **🗓️ Asked In Papers:** `2013-12 2(b)`

### Q127: Write a C++ program using a class/operator template for binary numbers to perform simple arithmetic operations (add and subtract). :id=q127

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class representing binary representations with add() and sub() methods/overloads.

> **🗓️ Asked In Papers:** `2014-06 2(b)`

### Q128: Write a function template printarray to display integer, float, and character arrays passed as arguments. :id=q128

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> void printarray(T arr[], int size) iterating 0..size-1

> **🗓️ Asked In Papers:** `2015-12 1(d)`

### Q129: Explain class templates and function templates with illustrations. :id=q129

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Show syntax and instantiation of both template<class T> T maxVal(T,T) and template<class T> class Pair.

> **🗓️ Asked In Papers:** `2018-12S 1(e)`

### Q130: What is a template class? Write a generic class to sort an array into ascending order. :id=q130

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class Sorter implementing bubble/selection sort over T arr[n]

> **🗓️ Asked In Papers:** `2024-12 5(b)`

### Q131: Define the Standard Template Library (STL) and explain how a class template differs from a function template. :id=q131

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

STL provides generic containers/algorithms/iterators; function templates generalize algorithms, class templates generalize data structures.

> **🗓️ Asked In Papers:** `2017-06 1(d)`

### Q132: Distinguish between an overloaded function and a function template with a suitable program. :id=q132

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Overloading writes separate bodies for distinct types/signatures; function template writes one generic body instantiated per type.

> **🗓️ Asked In Papers:** `2024-12 2(a)`

### Q133: What are Iterators? List the five types of iterators supported by STL in C++. :id=q133

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Smart pointer-like abstractions decoupling algorithms from containers: Input, Output, Forward, Bidirectional, Random-Access.

> **🗓️ Asked In Papers:** `2017-12 1(j)`

