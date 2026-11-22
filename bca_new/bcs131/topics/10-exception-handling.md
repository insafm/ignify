# 10. Exception Handling

> **Syllabus Unit:** Block 3 Unit 3 | **Rank:** #10 | **Frequency Score:** 54.9 | **Offered Marks:** 212 | **Papers Present:** 26/30 | **Importance:** Medium

---

## 📋 Topic Overview

This module covers **9 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q194](#q194) | What is an exception? Explain the purpose of exception handling and how exc... | **14x** | 101 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q195](#q195) | Explain exception handling in C++ with a program, and describe what happens... | **3x** | 30 marks | Theory + Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q196](#q196) | What is exception handling? Name the keywords used and write a C++ program ... | **3x** | 26 marks | Theory + Coding / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q197](#q197) | Write syntax of try, throw, catch, and write a program to catch all excepti... | **2x** | 20 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q198](#q198) | What is the need for exception handling? Explain with an example and descri... | **1x** | 10 marks | Theory + Diagram / Long Answer | <span class="badge badge-low">Low</span> |
| [Q199](#q199) | Explain exception handling while executing constructors and destructors, an... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q200](#q200) | Explain a situation when you will use multiple catch statements in a C++ pr... | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q201](#q201) | List any five common examples of exceptions. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q202](#q202) | Briefly discuss the functioning of try, throw, and catch expressions with a... | **1x** | 5 marks | Theory + Diagram / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q194">

### <span class="badge-qid">Q194</span> What is an exception? Explain the purpose of exception handling and how exceptions are handled in C++ (try, throw, catch) with an example program.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 14 (101 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Runtime anomaly; try encloses risky code, throw raises error object, catch handles matching type; separates error handling from normal business logic.

> **🗓️ Asked In Papers:** `2013-12 2(a), 2015-12 4(b), 2016-06 5(a), 2018-06 5(b), 2021-12 5(c), 2022-06 5(d), 2022-12 1(b), 2023-12 1(b), BCAOL S3-16, 2024-06 4(a), 2024-12 1(f), 2025-06 5(b), 2025-12 1(h), 2026-06 1(a)`

</div>

<div class="question-box" id="q195">

### <span class="badge-qid">Q195</span> Explain exception handling in C++ with a program, and describe what happens if an exception is thrown outside of a try block and why.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (30 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Unhandled outside try (no active catch handler on call stack) invokes std::terminate(), which calls abort() and ends the program.

> **🗓️ Asked In Papers:** `2012-12 5(b), 2017-12 4(b), 2020-12 2(a)`

</div>

<div class="question-box" id="q196">

### <span class="badge-qid">Q196</span> What is exception handling? Name the keywords used and write a C++ program to handle a divide-by-zero exception.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (26 marks)</span> <span class="badge badge-topic">Theory + Coding / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Keywords: try, throw, catch; check if (den == 0) throw runtime_error("Div by 0"); (or throw den;) inside try and handle in catch.

> **🗓️ Asked In Papers:** `2014-06 2(a), 2016-12 2(a), 2019-06 3(b)`

</div>

<div class="question-box" id="q197">

### <span class="badge-qid">Q197</span> Write syntax of try, throw, catch, and write a program to catch all exceptions (catch(...)). What happens if an exception is not caught?

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

catch(...) acts as wildcard handler placed last; uncaught exceptions propagate out of main() triggering std::terminate().

> **🗓️ Asked In Papers:** `2015-06 5(b), 2017-06 2(a)`

</div>

<div class="question-box" id="q198">

### <span class="badge-qid">Q198</span> What is the need for exception handling? Explain with an example and describe the hierarchy of exception classes in the C++ standard library.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Diagram / Long Answer</span>

**💡 Key Answer Points:**

<exception>: std::exception base → logic_error (invalid_argument, out_of_range), runtime_error (overflow_error), bad_alloc, bad_cast.

> **🗓️ Asked In Papers:** `2013-06 4(a)`

</div>

<div class="question-box" id="q199">

### <span class="badge-qid">Q199</span> Explain exception handling while executing constructors and destructors, and how exception types are specified in C++.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Throwing in constructor prevents destructor call for that object (already-built members/bases still destroyed); destructors must not throw; specification via throw(type) (legacy) or noexcept.

> **🗓️ Asked In Papers:** `2017-12S 2(b)`

</div>

<div class="question-box" id="q200">

### <span class="badge-qid">Q200</span> Explain a situation when you will use multiple catch statements in a C++ program for exception handling.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

When one try block can throw different exception types (e.g., int for invalid index, const char* for file error, ... fallback) needing distinct recovery.

> **🗓️ Asked In Papers:** `2014-12 5(b)`

</div>

<div class="question-box" id="q201">

### <span class="badge-qid">Q201</span> List any five common examples of exceptions.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Division by zero, array index out of bounds, memory allocation failure (bad_alloc), file open failure, invalid type conversion/input.

> **🗓️ Asked In Papers:** `2015-12 1(g)`

</div>

<div class="question-box" id="q202">

### <span class="badge-qid">Q202</span> Briefly discuss the functioning of try, throw, and catch expressions with a suitable block diagram.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory + Diagram / Short Answer</span>

**💡 Key Answer Points:**

Draw flow: try block → error detected → throw → control transfers out of try → matching catch block executes.

> **🗓️ Asked In Papers:** `2021-06 1(h)`

</div>

