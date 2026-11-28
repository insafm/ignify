# 05. Templates & Standard Template Library (STL)

> **Syllabus Unit:** Block 3 Unit 2 | **Rank:** #5 | **Frequency Score:** 83.0 | **Offered Marks:** 340 | **Papers Present:** 30/30 | **Importance:** High
> **Coverage:** 19 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q115: What are Containers (Containership) in C++? List the main types of containers with examples, their importance, and common member functions. :id=q115

🔴 **Very High Priority** • **7 (54 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Sequence (vector, list, deque), Associative (set, map), Container Adapters (stack, queue, priority_queue); common functions: size(), empty(), begin(), end(), clear().

**📝 Example PQP Question (2020-06 2(a)):**

What is a container in C++? List main types of container in C++. Also list some common member functions of Container class. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2014-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2015-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2015-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2019-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2025-06 5(e)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q116: What is a class template? Explain its concept, advantages, and utility. :id=q116

🟠 **High Priority** • **5 (23 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

template <class T> class Box {...}; creates type-independent generic data structures/classes, eliminating code duplication while preserving type safety.

**📝 Example PQP Question (2020-12 2(b)):**

What is template class? Explain the advantages of template class. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2020-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q117: Differentiate between a class template and a function template with an example for each. :id=q117

🟠 **High Priority** • **4 (31 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Function template parameterizes a single algorithm (template<typename T> T add(T,T)); class template parameterizes an entire class's data members and methods.

**📝 Example PQP Question (2019-12 2(a)):**

What is a Class template? How it is different from function template? Give example for each. *(8 marks)*

> **🗓️ Asked In Papers:** [2014-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2016-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2019-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2021-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q118: What is a function template in C++? Explain its advantages with an example. :id=q118

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Blueprint for generic functions deduced at compile time (template <class T>); reduces redundancy and maintenance effort.

**📝 Example PQP Question (2026-06 3(b)):**

What is template function in C++? What are its advantages? Give an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2019-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2021-12 5(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2026-06 3(b)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q119: Explain the use of the STL list container class with an example program. :id=q119

🟠 **High Priority** • **4 (21 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Doubly-linked list (<list>); O(1) insertion/deletion anywhere via push_back(), push_front(), sort(), reverse(), and iterators.

**📝 Example PQP Question (2025-12 4(b)):**

What are containers in C++? Explain the use of ‘list’ container class with the help of an example. 5 A–24/BCS–031/BCS–131 P. T. O.

> **🗓️ Asked In Papers:** [2018-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2022-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2025-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q120: What is a template class? Give its advantages and create a template class for the Linked List data structure. :id=q120

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> struct Node { T data; Node* next; }; inside template<class T> class LinkedList with insert(), deleteNode(), display().

**📝 Example PQP Question (2022-12 2(b)):**

What is a class template? Give two advantages of class template. Create a class template for a linked list data structure. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2017-12S 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2022-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q121: What is a class template? Create a class template for a Stack data structure. :id=q121

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class Stack with T arr[MAX]; int top;, push(T), pop(), peek(), overflow/underflow checks.

**📝 Example PQP Question (2025-12 3(b)):**

What is class template? Create a class template for stack data structure. *(10 marks)*

> **🗓️ Asked In Papers:** [2018-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2022-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q122: What is STL (Standard Template Library)? Briefly discuss its components and importance in C++. :id=q122

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Core components: Containers (data storage), Algorithms (sort, find), Iterators (pointer-like traversal), and Function Objects/Functors.

**📝 Example PQP Question (2025-06 1(d)):**

What is Standard Template Library (STL)? Briefly discuss the components of STL. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2023-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2025-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q123: What is a template function? Write a template function to swap the values of two numbers. :id=q123

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template <typename T> void mySwap(T& a, T& b) { T temp = a; a = b; b = temp; }

**📝 Example PQP Question (2024-06 3(a)):**

What do you mean by template function? What are its benefits? Write down code for a template function to swap values of two numbers. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2024-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q124: What is a function template? Write a function template SUM to add two numbers. :id=q124

🔵 **Medium Priority** • **2 (11 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

template <class T> T SUM(T a, T b) { return a + b; } tested with int and float/double.

**📝 Example PQP Question (2020-12 1(b)):**

What is function template? Write a function template SUM to add two numbers. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2020-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q125: What are templates in C++? Explain their advantages with an example. :id=q125

⚪ **Low Priority** • **1 (15 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Generic programming mechanism enabling type-parameterized functions and classes compiled on demand.

**📝 Example PQP Question (BCAOL S3-17):**

What are templates in C++? Explain their advantages with example. *(15 marks)*

> **🗓️ Asked In Papers:** [BCAOL S3-17](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q126: Write an OOP program in C++ to read n integers and print the array in reverse order using a class template. :id=q126

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class ArrayRev storing dynamic/fixed array T a[] and printing from n-1 down to 0.

**📝 Example PQP Question (2013-12 2(b)):**

Write an object oriented program in C++ to read a set of integer numbers. Upto n, where n is defined by the user and print the contents of the array in the reverse order using a class template. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore')

### Q127: Write a C++ program using a class/operator template for binary numbers to perform simple arithmetic operations (add and subtract). :id=q127

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class representing binary representations with add() and sub() methods/overloads.

**📝 Example PQP Question (2014-06 2(b)):**

Write a program in C++ using operator template for the binary numbers to perform a simple arithmetic operations such as add and subtract. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore')

### Q128: Write a function template printarray to display integer, float, and character arrays passed as arguments. :id=q128

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> void printarray(T arr[], int size) iterating 0..size-1

**📝 Example PQP Question (2015-12 1(d)):**

Write the appropriate statements to create a function template printarray that can display the values contained in array passed as parameter to the function. The function must be able to accept integer, float and character arrays as arguments. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q129: Explain class templates and function templates with illustrations. :id=q129

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Show syntax and instantiation of both template<class T> T maxVal(T,T) and template<class T> class Pair.

**📝 Example PQP Question (2018-12S 1(e)):**

Explain class templates and function templates with illustrations. *(10 marks)*

> **🗓️ Asked In Papers:** [2018-12S 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q130: What is a template class? Write a generic class to sort an array into ascending order. :id=q130

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

template<class T> class Sorter implementing bubble/selection sort over T arr[n]

**📝 Example PQP Question (2024-12 5(b)):**

What do you mean by template class? Write a generic class to sort an array into ascending order. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q131: Define the Standard Template Library (STL) and explain how a class template differs from a function template. :id=q131

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

STL provides generic containers/algorithms/iterators; function templates generalize algorithms, class templates generalize data structures.

**📝 Example PQP Question (2017-06 1(d)):**

Define the Standard Template Library. How is the class template different from the function template? Explain. *(6 marks)*

> **🗓️ Asked In Papers:** [2017-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore')

### Q132: Distinguish between an overloaded function and a function template with a suitable program. :id=q132

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Overloading writes separate bodies for distinct types/signatures; function template writes one generic body instantiated per type.

**📝 Example PQP Question (2024-12 2(a)):**

Distinguish between the overloaded function and function template with the help of a suitable program. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q133: What are Iterators? List the five types of iterators supported by STL in C++. :id=q133

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Smart pointer-like abstractions decoupling algorithms from containers: Input, Output, Forward, Bidirectional, Random-Access.

**📝 Example PQP Question (2017-12 1(j)):**

What are Iterators? List the five types of iterators supported by STL in C++. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(j)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

