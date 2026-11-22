# 05. Templates & Standard Template Library (STL)

> **Syllabus Unit:** Block 3 Unit 2 | **Rank:** #5 | **Frequency Score:** 83.0 | **Offered Marks:** 340 | **Papers Present:** 30/30 | **Importance:** High

---

## 📋 Topic Overview

This module covers **19 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q115](#q115) | What are Containers (Containership) in C++? List the main types of containe... | **7x** | 54 marks | Theory / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q116](#q116) | What is a class template? Explain its concept, advantages, and utility. | **5x** | 23 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q117](#q117) | Differentiate between a class template and a function template with an exam... | **4x** | 31 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q118](#q118) | What is a function template in C++? Explain its advantages with an example. | **4x** | 25 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q119](#q119) | Explain the use of the STL list container class with an example program. | **4x** | 21 marks | Theory + Coding / Short Answer | <span class="badge badge-high">High</span> |
| [Q120](#q120) | What is a template class? Give its advantages and create a template class f... | **3x** | 30 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q121](#q121) | What is a class template? Create a class template for a Stack data structur... | **3x** | 30 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q122](#q122) | What is STL (Standard Template Library)? Briefly discuss its components and... | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q123](#q123) | What is a template function? Write a template function to swap the values o... | **2x** | 20 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q124](#q124) | What is a function template? Write a function template SUM to add two numbe... | **2x** | 11 marks | Theory + Coding / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q125](#q125) | What are templates in C++? Explain their advantages with an example. | **1x** | 15 marks | Theory / Long Answer | <span class="badge badge-low">Low</span> |
| [Q126](#q126) | Write an OOP program in C++ to read n integers and print the array in rever... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q127](#q127) | Write a C++ program using a class/operator template for binary numbers to p... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q128](#q128) | Write a function template printarray to display integer, float, and charact... | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q129](#q129) | Explain class templates and function templates with illustrations. | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q130](#q130) | What is a template class? Write a generic class to sort an array into ascen... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q131](#q131) | Define the Standard Template Library (STL) and explain how a class template... | **1x** | 6 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q132](#q132) | Distinguish between an overloaded function and a function template with a s... | **1x** | 5 marks | Theory + Coding / Short Answer | <span class="badge badge-low">Low</span> |
| [Q133](#q133) | What are Iterators? List the five types of iterators supported by STL in C+... | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q115">

### <span class="badge-qid">Q115</span> What are Containers (Containership) in C++? List the main types of containers with examples, their importance, and common member functions.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 7 (54 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Sequence (vector, list, deque), Associative (set, map), Container Adapters (stack, queue, priority_queue); common functions: size(), empty(), begin(), end(), clear().

> **🗓️ Asked In Papers:** `2013-12 4(c), 2014-12 5(a), 2015-06 5(a), 2015-12 1(f), 2019-12 5(c), 2020-06 2(a), 2025-06 5(e)`

</div>

<div class="question-box" id="q116">

### <span class="badge-qid">Q116</span> What is a class template? Explain its concept, advantages, and utility.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 5 (23 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

template <class T> class Box {...}; creates type-independent generic data structures/classes, eliminating code duplication while preserving type safety.

> **🗓️ Asked In Papers:** `2016-12 5(c), 2020-12 2(b), 2021-12 5(d), 2023-12 5(b), 2025-06 5(a)`

</div>

<div class="question-box" id="q117">

### <span class="badge-qid">Q117</span> Differentiate between a class template and a function template with an example for each.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (31 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Function template parameterizes a single algorithm (template<typename T> T add(T,T)); class template parameterizes an entire class's data members and methods.

> **🗓️ Asked In Papers:** `2014-12 1(d), 2016-06 3(a), 2019-12 2(a), 2021-06 5(b)`

</div>

<div class="question-box" id="q118">

### <span class="badge-qid">Q118</span> What is a function template in C++? Explain its advantages with an example.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (25 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Blueprint for generic functions deduced at compile time (template <class T>); reduces redundancy and maintenance effort.

> **🗓️ Asked In Papers:** `2014-06 1(d), 2019-06 4(c), 2021-12 5(e), 2026-06 3(b)`

</div>

<div class="question-box" id="q119">

### <span class="badge-qid">Q119</span> Explain the use of the STL list container class with an example program.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (21 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

Doubly-linked list (<list>); O(1) insertion/deletion anywhere via push_back(), push_front(), sort(), reverse(), and iterators.

> **🗓️ Asked In Papers:** `2018-06 5(a), 2022-12 1(c), 2023-12 1(f), 2025-12 4(b)`

</div>

<div class="question-box" id="q120">

### <span class="badge-qid">Q120</span> What is a template class? Give its advantages and create a template class for the Linked List data structure.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (30 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> struct Node { T data; Node* next; }; inside template<class T> class LinkedList with insert(), deleteNode(), display().

> **🗓️ Asked In Papers:** `2013-06 4(b), 2017-12S 4(a), 2022-12 2(b)`

</div>

<div class="question-box" id="q121">

### <span class="badge-qid">Q121</span> What is a class template? Create a class template for a Stack data structure.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (30 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> class Stack with T arr[MAX]; int top;, push(T), pop(), peek(), overflow/underflow checks.

> **🗓️ Asked In Papers:** `2018-06 4(b), 2022-06 2(b), 2025-12 3(b)`

</div>

<div class="question-box" id="q122">

### <span class="badge-qid">Q122</span> What is STL (Standard Template Library)? Briefly discuss its components and importance in C++.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Core components: Containers (data storage), Algorithms (sort, find), Iterators (pointer-like traversal), and Function Objects/Functors.

> **🗓️ Asked In Papers:** `2021-12 1(g), 2023-06 1(h), 2025-06 1(d)`

</div>

<div class="question-box" id="q123">

### <span class="badge-qid">Q123</span> What is a template function? Write a template function to swap the values of two numbers.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

template <typename T> void mySwap(T& a, T& b) { T temp = a; a = b; b = temp; }

> **🗓️ Asked In Papers:** `2015-06 4(c), 2024-06 3(a)`

</div>

<div class="question-box" id="q124">

### <span class="badge-qid">Q124</span> What is a function template? Write a function template SUM to add two numbers.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (11 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

template <class T> T SUM(T a, T b) { return a + b; } tested with int and float/double.

> **🗓️ Asked In Papers:** `2012-12 1(f), 2020-12 1(b)`

</div>

<div class="question-box" id="q125">

### <span class="badge-qid">Q125</span> What are templates in C++? Explain their advantages with an example.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (15 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

Generic programming mechanism enabling type-parameterized functions and classes compiled on demand.

> **🗓️ Asked In Papers:** `BCAOL S3-17`

</div>

<div class="question-box" id="q126">

### <span class="badge-qid">Q126</span> Write an OOP program in C++ to read n integers and print the array in reverse order using a class template.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> class ArrayRev storing dynamic/fixed array T a[] and printing from n-1 down to 0.

> **🗓️ Asked In Papers:** `2013-12 2(b)`

</div>

<div class="question-box" id="q127">

### <span class="badge-qid">Q127</span> Write a C++ program using a class/operator template for binary numbers to perform simple arithmetic operations (add and subtract).

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> class representing binary representations with add() and sub() methods/overloads.

> **🗓️ Asked In Papers:** `2014-06 2(b)`

</div>

<div class="question-box" id="q128">

### <span class="badge-qid">Q128</span> Write a function template printarray to display integer, float, and character arrays passed as arguments.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> void printarray(T arr[], int size) iterating 0..size-1

> **🗓️ Asked In Papers:** `2015-12 1(d)`

</div>

<div class="question-box" id="q129">

### <span class="badge-qid">Q129</span> Explain class templates and function templates with illustrations.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Show syntax and instantiation of both template<class T> T maxVal(T,T) and template<class T> class Pair.

> **🗓️ Asked In Papers:** `2018-12S 1(e)`

</div>

<div class="question-box" id="q130">

### <span class="badge-qid">Q130</span> What is a template class? Write a generic class to sort an array into ascending order.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

template<class T> class Sorter implementing bubble/selection sort over T arr[n]

> **🗓️ Asked In Papers:** `2024-12 5(b)`

</div>

<div class="question-box" id="q131">

### <span class="badge-qid">Q131</span> Define the Standard Template Library (STL) and explain how a class template differs from a function template.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (6 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

STL provides generic containers/algorithms/iterators; function templates generalize algorithms, class templates generalize data structures.

> **🗓️ Asked In Papers:** `2017-06 1(d)`

</div>

<div class="question-box" id="q132">

### <span class="badge-qid">Q132</span> Distinguish between an overloaded function and a function template with a suitable program.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer</span>

**💡 Key Answer Points:**

Overloading writes separate bodies for distinct types/signatures; function template writes one generic body instantiated per type.

> **🗓️ Asked In Papers:** `2024-12 2(a)`

</div>

<div class="question-box" id="q133">

### <span class="badge-qid">Q133</span> What are Iterators? List the five types of iterators supported by STL in C++.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Smart pointer-like abstractions decoupling algorithms from containers: Input, Output, Forward, Bidirectional, Random-Access.

> **🗓️ Asked In Papers:** `2017-12 1(j)`

</div>

