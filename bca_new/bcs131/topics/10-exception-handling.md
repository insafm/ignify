# 10. Exception Handling

> **Syllabus Unit:** Block 3 Unit 3 | **Rank:** #10 | **Frequency Score:** 54.9 | **Offered Marks:** 212 | **Papers Present:** 26/30 | **Importance:** Medium
> **Coverage:** 9 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q194: What is an exception? Explain the purpose of exception handling and how exceptions are handled in C++ (try, throw, catch) with an example program. :id=q194

🔴 **Very High Priority** • **14 (101 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Runtime anomaly; try encloses risky code, throw raises error object, catch handles matching type; separates error handling from normal business logic.

**📝 Example PQP Question (2026-06 1(a)):**

What is an Exception ? How is it handled in C++ ? Explain with the help of an example. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2015-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2016-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2018-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2021-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2022-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2022-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [BCAOL S3-16](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2024-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2024-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore'), [2025-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2025-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore'), [2026-06 1(a)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q195: Explain exception handling in C++ with a program, and describe what happens if an exception is thrown outside of a try block and why. :id=q195

🟠 **High Priority** • **3 (30 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Unhandled outside try (no active catch handler on call stack) invokes std::terminate(), which calls abort() and ends the program.

**📝 Example PQP Question (2020-12 2(a)):**

What is exception ? Explain, how exception handling is done in C++, with the help of a program. Also discuss, what will happen if an exception is thrown outside of a try block. *(10 marks)*

> **🗓️ Asked In Papers:** [2012-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2017-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2020-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q196: What is exception handling? Name the keywords used and write a C++ program to handle a divide-by-zero exception. :id=q196

🟠 **High Priority** • **3 (26 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Keywords: try, throw, catch; check if (den == 0) throw runtime_error("Div by 0"); (or throw den;) inside try and handle in catch.

**📝 Example PQP Question (2019-06 3(b)):**

What is exception handling ? What are the keywords, used to handle the exception in C++ ? Write a C++ program to handle divide by zero exception. *(6 marks)*

> **🗓️ Asked In Papers:** [2014-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2016-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2019-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

### Q197: Write syntax of try, throw, catch, and write a program to catch all exceptions (catch(...)). What happens if an exception is not caught? :id=q197

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

catch(...) acts as wildcard handler placed last; uncaught exceptions propagate out of main() triggering std::terminate().

**📝 Example PQP Question (2017-06 2(a)):**

Write a program to demonstrate the catching of all exceptions. What happens when a raised exception is not caught by catch-block (in the absence of catching all exception blocks) ? *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2017-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore')

### Q198: What is the need for exception handling? Explain with an example and describe the hierarchy of exception classes in the C++ standard library. :id=q198

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Diagram / Long Answer*

**💡 Key Answer Points:**

<exception>: std::exception base → logic_error (invalid_argument, out_of_range), runtime_error (overflow_error), bad_alloc, bad_cast.

**📝 Example PQP Question (2013-06 4(a)):**

What is need of exception handling in C++ programming ? Explain with an example how exceptions are handled in C++. Briefly describe the hierarchy of exception classes in C++ standard library. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore')

### Q199: Explain exception handling while executing constructors and destructors, and how exception types are specified in C++. :id=q199

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Throwing in constructor prevents destructor call for that object (already-built members/bases still destroyed); destructors must not throw; specification via throw(type) (legacy) or noexcept.

**📝 Example PQP Question (2017-12S 2(b)):**

What is an Exception ? Explain briefly about the exception handling process while executing constructors and destructors. Also explain with an example, how exception types are specified in a C++ program. *(10 marks)*

> **🗓️ Asked In Papers:** [2017-12S 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

### Q200: Explain a situation when you will use multiple catch statements in a C++ program for exception handling. :id=q200

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

When one try block can throw different exception types (e.g., int for invalid index, const char* for file error, ... fallback) needing distinct recovery.

**📝 Example PQP Question (2014-12 5(b)):**

Explain a situation when you will use multiple catch statements in a C++ program for exception handling. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore')

### Q201: List any five common examples of exceptions. :id=q201

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Division by zero, array index out of bounds, memory allocation failure (bad_alloc), file open failure, invalid type conversion/input.

**📝 Example PQP Question (2015-12 1(g)):**

List any five common examples of exceptions. *(5 marks)*

> **🗓️ Asked In Papers:** [2015-12 1(g)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q202: Briefly discuss the functioning of try, throw, and catch expressions with a suitable block diagram. :id=q202

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Diagram / Short Answer*

**💡 Key Answer Points:**

Draw flow: try block → error detected → throw → control transfers out of try → matching catch block executes.

**📝 Example PQP Question (2021-06 1(h)):**

What are Exceptions in C++ ? How is exception handling done in C++ ? Briefly discuss the functioning of Try, Throw and Catch expressions with suitable block diagram. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

