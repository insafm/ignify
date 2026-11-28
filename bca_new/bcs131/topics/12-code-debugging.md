# 12. Code Debugging & Output Tracing

> **Syllabus Unit:** Block 1 & 2 Applied | **Rank:** #12 | **Frequency Score:** 6.1 | **Offered Marks:** 16 | **Papers Present:** 2/30 | **Importance:** Low
> **Coverage:** 4 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q212: Identify the errors in the code segment: cin >> num >> auuto; float area = length * breadth;. :id=q212

⚪ **Low Priority** • **1 (4 marks)** • *Debugging / Short Answer*

**💡 Key Answer Points:**

Missing #include <iostream>/using namespace std;; undeclared variables (num, auuto, length, breadth); missing return 0;.

**📝 Example PQP Question (2017-12 1(c)):**

Identify the errors in the following code segment :

```cpp
int main( )
{
    cout << "Enter two numbers";
    cin >> num >> auto;
    float area = length * breadth;
}
```

*(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q213: Why will the function fragment (float sum(float, float); declared inside main(), called inside calc()) not work, and how do you fix it? :id=q213

⚪ **Low Priority** • **1 (4 marks)** • *Debugging / Short Answer*

**💡 Key Answer Points:**

sum() prototype has block scope local to main() and is invisible inside calc(); fix by moving prototype to global scope above main() and calc() (and adding missing ; in calc).

**📝 Example PQP Question (2017-12 1(d)):**

Why will the function given in the following code fragment not work ? What should be done to make it work ?

```cpp
int main( )
{
    float sum (float, float);
}
void calc(void)
{
    float x, y, s;
    cin >> x >> y;
    s = sum (x, y);
}
```

*(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q214: Given int ch=20; cout << ++ch << "\n" << ch << "\n";, what output does it produce, and what is the effect of replacing ++ch with ch+1? :id=q214

⚪ **Low Priority** • **1 (4 marks)** • *Debugging / Output / Short Answer*

**💡 Key Answer Points:**

In standard IGNOU left-to-right tracing, ++ch mutates ch to print 21 then 21 (note: unsequenced modification/read in chained << is undefined in pre-C++17); replacing with ch+1 prints 21 then 20 (ch stays unchanged).

**📝 Example PQP Question (2017-12S 1(c)):**

Given the following code fragment :

```cpp
int ch = 20;
cout << ++ch << "\n"
     << ch << "\n";
```

(i) What output does the above code fragment produce ?
(ii) What is the effect of replacing `++ch` with `ch + 1` ? *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

### Q215: Identify the problem with void large(int &a, int &b); called as large(5, 7); and suggest a fix. :id=q215

⚪ **Low Priority** • **1 (4 marks)** • *Debugging / Short Answer*

**💡 Key Answer Points:**

Non-const lvalue reference (int&) cannot bind to rvalue integer literals (5, 7); fix by passing variables (int x=5, y=7; large(x,y);) or changing parameters to value (int a, int b) / const int& (if not mutating).

**📝 Example PQP Question (2017-12S 1(d)):**

Identify the problem with the following code. Suggest the way to correct the problem.

```cpp
void large (int &a, int &b);
int main( )
{ large (5, 7); }
void large (int &a, int &b)
{ if (a > b)
      a = -1;
   else
      b = -1; }
```

*(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

