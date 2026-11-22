# 12. Code Debugging & Output Tracing

> **Syllabus Unit:** Block 1 & 2 Applied | **Rank:** #12 | **Frequency Score:** 6.1 | **Offered Marks:** 16 | **Papers Present:** 2/30 | **Importance:** Low

---

## 📋 Topic Overview

This module covers **4 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q212](#q212) | Identify the errors in the code segment: cin >> num >> auuto; float area = ... | **1x** | 4 marks | Debugging / Short Answer | <span class="badge badge-low">Low</span> |
| [Q213](#q213) | Why will the function fragment (float sum(float, float); declared inside ma... | **1x** | 4 marks | Debugging / Short Answer | <span class="badge badge-low">Low</span> |
| [Q214](#q214) | Given int ch=20; cout << ++ch << "\n" << ch << "\n";, what output does it p... | **1x** | 4 marks | Debugging / Output / Short Answer | <span class="badge badge-low">Low</span> |
| [Q215](#q215) | Identify the problem with void large(int &a, int &b); called as large(5, 7)... | **1x** | 4 marks | Debugging / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q212">

### <span class="badge-qid">Q212</span> Identify the errors in the code segment: cin >> num >> auuto; float area = length * breadth;.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Debugging / Short Answer</span>

**💡 Key Answer Points:**

Missing #include <iostream>/using namespace std;; undeclared variables (num, auuto, length, breadth); missing return 0;.

> **🗓️ Asked In Papers:** `2017-12 1(c)`

</div>

<div class="question-box" id="q213">

### <span class="badge-qid">Q213</span> Why will the function fragment (float sum(float, float); declared inside main(), called inside calc()) not work, and how do you fix it?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Debugging / Short Answer</span>

**💡 Key Answer Points:**

sum() prototype has block scope local to main() and is invisible inside calc(); fix by moving prototype to global scope above main() and calc() (and adding missing ; in calc).

> **🗓️ Asked In Papers:** `2017-12 1(d)`

</div>

<div class="question-box" id="q214">

### <span class="badge-qid">Q214</span> Given int ch=20; cout << ++ch << "\n" << ch << "\n";, what output does it produce, and what is the effect of replacing ++ch with ch+1?

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Debugging / Output / Short Answer</span>

**💡 Key Answer Points:**

In standard IGNOU left-to-right tracing, ++ch mutates ch to print 21 then 21 (note: unsequenced modification/read in chained << is undefined in pre-C++17); replacing with ch+1 prints 21 then 20 (ch stays unchanged).

> **🗓️ Asked In Papers:** `2017-12S 1(c)`

</div>

<div class="question-box" id="q215">

### <span class="badge-qid">Q215</span> Identify the problem with void large(int &a, int &b); called as large(5, 7); and suggest a fix.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Debugging / Short Answer</span>

**💡 Key Answer Points:**

Non-const lvalue reference (int&) cannot bind to rvalue integer literals (5, 7); fix by passing variables (int x=5, y=7; large(x,y);) or changing parameters to value (int a, int b) / const int& (if not mutating).

> **🗓️ Asked In Papers:** `2017-12S 1(d)`

</div>

