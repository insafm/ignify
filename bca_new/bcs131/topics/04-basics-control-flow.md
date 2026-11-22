# 04. C++ Basics, Operators & Control Flow

> **Syllabus Unit:** Block 1 Unit 2 | **Rank:** #4 | **Frequency Score:** 91.0 | **Offered Marks:** 321 | **Papers Present:** 27/30 | **Importance:** High
> **Coverage:** 36 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q079: Explain the use of break and continue statements in C++ with an example program. :id=q079

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

break terminates the enclosing loop/switch immediately; continue skips remaining statements in current iteration and jumps to next iteration.

> **🗓️ Asked In Papers:** `2014-06 3(b), 2016-06 2(a), 2019-12 1(a), 2021-06 2(d)`

### Q080: What is the scope resolution operator (::)? Explain its uses with a C++ program. :id=q080

🟠 **High Priority** • **4 (19 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Accesses hidden global variables (::x), defines class member functions outside class (Class::f()), and resolves multiple inheritance ambiguity.

> **🗓️ Asked In Papers:** `2013-12 1(e), 2019-06 1(g), 2020-06 1(h), 2020-12 5(v)`

### Q081: What is an operator? List and explain the various types of operators available in C++. :id=q081

🟠 **High Priority** • **3 (26 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Arithmetic, Relational, Logical, Bitwise, Assignment, Increment/Decrement, Ternary (?:), Scope resolution (::), sizeof, and new/delete.

> **🗓️ Asked In Papers:** `2013-12 1(b), 2018-06 2(a), 2018-12S 1(c)`

### Q082: What is the scope of a variable? Compare global variables and local variables in C++ with example code. :id=q082

🟠 **High Priority** • **3 (15 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Local: declared inside block/function, stack-allocated, limited visibility; Global: declared outside functions, data-segment lifetime, file-wide access.

> **🗓️ Asked In Papers:** `2016-06 1(g), 2021-12 1(b), 2025-06 1(b)`

### Q083: What is type conversion? Differentiate between automatic (implicit) type conversion and explicit type casting with examples. :id=q083

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Implicit: compiler promotes smaller to larger types (int to double); Explicit casting: programmer forces conversion ((int)x or static_cast<int>(x)).

> **🗓️ Asked In Papers:** `2018-12S 5(c), 2021-06 2(c), 2023-06 2(b)`

### Q084: What is the difference between a keyword and an identifier? Explain with a simple C++ program. :id=q084

🟠 **High Priority** • **3 (13 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Keywords are compiler-reserved words with fixed meaning (int, class, return); identifiers are programmer-defined names for variables/functions/classes.

> **🗓️ Asked In Papers:** `2017-12S 1(a), 2022-06 5(c), 2025-12 2(c)`

### Q085: What is a data type? List built-in data types (and sizes) with examples, and explain the need for derived data types. :id=q085

🔵 **Medium Priority** • **2 (11 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Built-in: char (1B), int (4B), float (4B), double (8B), bool (1B), void; Derived (arrays, pointers, references) model collections/indirection.

> **🗓️ Asked In Papers:** `2012-12 1(c), 2025-12 1(d)`

### Q086: Write a C++ program to demonstrate the use of the switch statement. :id=q086

🔵 **Medium Priority** • **2 (11 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

switch(choice) with case labels, break; after each case, and default: fallback (e.g., day-of-week or menu).

> **🗓️ Asked In Papers:** `2015-12 1(c), 2018-12S 1(d)`

### Q087: Discuss and draw the taxonomy/hierarchy of data types in C++. :id=q087

🔵 **Medium Priority** • **2 (10 marks)** • *Theory + Diagram / Short Answer*

**💡 Key Answer Points:**

Three branches: Built-in (int, char, float, double, void), Derived (array, function, pointer, reference), User-defined (class, struct, union, enum).

> **🗓️ Asked In Papers:** `2013-06 2(b), 2021-12 2(c)`

### Q088: Write a program in C++ to calculate the factorial of a given number. :id=q088

🔵 **Medium Priority** • **2 (10 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read n; initialize long long fact = 1; loop i = 1..n multiplying fact *= i; handle n=0 -> 1.

> **🗓️ Asked In Papers:** `2016-12 3(b), 2018-12S 3(c)`

### Q089: What are breaking statements? Give the syntax of break, continue, goto, and exit. :id=q089

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

break;, continue;, goto label; ... label:, and exit(status); (from <cstdlib>, terminates entire process).

> **🗓️ Asked In Papers:** `2021-12 2(d), 2025-12 1(f)`

### Q090: Explain relational and logical operators in C++ (any five) with examples. :id=q090

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Relational (==, !=, <, >, <=, >=) compare operands; Logical (&&, ||, !) combine boolean conditions.

> **🗓️ Asked In Papers:** `2024-06 4(c), 2024-12 1(e)`

### Q091: Explain any five relational operators in C++ with examples. :id=q091

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

<, <=, >, >=, ==, != returning bool (true/false, i.e., 1/0).

> **🗓️ Asked In Papers:** `2019-06 1(h), 2022-12 5(v)`

### Q092: Write a C++ program that prints numbers and their cubes from 1 to 10 using if-then-else and for loop. :id=q092

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

for(int i=1; i<=10; i++) checking boundary/parity via if-else and printing i and i*i*i.

> **🗓️ Asked In Papers:** `2014-06 3(a)`

### Q093: Write an interactive C++ program reading two integers x, y and an operator (+, -, *, /), printing an error for any other operator. :id=q093

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

switch(op) handling +, -, *, / (with y==0 guard) and default: cout << "Invalid operator";.

> **🗓️ Asked In Papers:** `2016-06 3(b)`

### Q094: Write a C++ program to find the difference between two times in 24-hour format (e.g., 09:00:00 - 13:30:00 = 19:30:00). :id=q094

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Convert hh:mm:ss to total seconds; if t1 < t2, add 86,400 seconds (24h wrap-around); convert back to HH:MM:SS.

> **🗓️ Asked In Papers:** `2016-06 5(b)`

### Q095: How are strings handled in C++? Explain how a string can be reversed with the help of a program. :id=q095

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

C-style char[] (\0-terminated, <cstring>) and std::string; reverse via two-pointer swap (start++, end--).

> **🗓️ Asked In Papers:** `BCAOL S2-12`

### Q096: What are comparison and logical operators? How do they differ from arithmetic and assignment operators? :id=q096

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Comparison/logical produce bool for branching; arithmetic compute numeric values; assignment (=, +=) mutates lvalue memory.

> **🗓️ Asked In Papers:** `2014-06 1(c)`

### Q097: Explain the use of the following operators in C++: (i) &, (ii) ?:, (iii) ::, (iv) &&. :id=q097

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

& (address-of/reference/bitwise AND), ?: (ternary conditional), :: (scope resolution), && (logical AND with short-circuiting).

> **🗓️ Asked In Papers:** `2016-12 4(c)`

### Q098: What is looping in C++? Explain its advantages and list the looping options available in C++. :id=q098

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Avoids code duplication, enables traversal; options: for (entry-controlled), while (entry-controlled), do-while (exit-controlled).

> **🗓️ Asked In Papers:** `2014-06 1(e)`

### Q099: Write a C++ program to find the area of a circle. :id=q099

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read r; compute float area = 3.14159 * r * r; and output area.

> **🗓️ Asked In Papers:** `2014-12 5(c)`

### Q100: How do you input non-graphic characters in C++? What do escape sequences \n, \a, and \v represent? :id=q100

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Entered via backslash escape sequences; \n = newline, \a = alert/bell, \v = vertical tab.

> **🗓️ Asked In Papers:** `2015-12 1(b)`

### Q101: Compare while() and do-while() looping constructs with a suitable example for each. :id=q101

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

while checks condition before body (0 or more runs); do-while checks after body (at least 1 run, ends with semicolon).

> **🗓️ Asked In Papers:** `2019-12 1(e)`

### Q102: Differentiate between C and C++ (give at least five differences). :id=q102

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Procedural vs. OOP; stdio.h vs. iostream; malloc/free vs. new/delete; no overloading/references/classes in C vs. full support in C++.

> **🗓️ Asked In Papers:** `2021-06 2(b)`

### Q103: Explain the use of && and ! operators in C++ with an example. :id=q103

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

&& returns true only if both operands are true; ! negates a boolean operand.

> **🗓️ Asked In Papers:** `2021-06 3(d)`

### Q104: What is the difference between an if statement and a for loop? Explain with an example. :id=q104

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

if is a single-decision conditional branch (executes 0 or 1 time); for is an iterative loop repeating until condition becomes false.

> **🗓️ Asked In Papers:** `2023-06 3(c)`

### Q105: What is operator precedence? Explain the precedence order in arithmetical operators in C++ with an example. :id=q105

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Determines evaluation order: parentheses () highest, then unary ++/--/-, then *, /, % (left-to-right), then +, - (left-to-right).

> **🗓️ Asked In Papers:** `2023-06 3(d)`

### Q106: Explain the working of the goto statement. Does its usage violate the rules of OOP? :id=q106

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Unconditional jump to a labeled statement in same function; discourages structured modularity and risks bypassing object initialization/cleanup.

> **🗓️ Asked In Papers:** `2023-12 1(e)`

### Q107: Write a C++ program to find whether a given number is odd or even. :id=q107

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read n; if (n % 2 == 0) cout << "Even"; else cout << "Odd";

> **🗓️ Asked In Papers:** `2023-12 2(b)`

### Q108: Explain the use of the do-while loop with the help of a C++ program. :id=q108

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Post-tested loop ideal for menu-driven programs requiring at least one execution.

> **🗓️ Asked In Papers:** `2023-12 5(a)`

### Q109: Explain the working of the for loop with the help of an example C++ program. :id=q109

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Three clauses (init; condition; update): initializes once, checks condition before each iteration, updates after body.

> **🗓️ Asked In Papers:** `2024-06 1(e)`

### Q110: What is a Reference Variable, and what is its usage in C++? :id=q110

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Alias to an existing variable (int& ref = x;), must be initialized at declaration, used for pass-by-reference and operator overloading.

> **🗓️ Asked In Papers:** `2017-12 1(b)`

### Q111: What are data modifiers? How do they affect base data types? Give a suitable example. :id=q111

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

signed, unsigned, short, long alter memory width and value range of int/char/double.

> **🗓️ Asked In Papers:** `2017-12S 1(b)`

### Q112: Write a C++ program to find the sum of two given numbers. :id=q112

⚪ **Low Priority** • **1 (4 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Declare int a, b;, read via cin >> a >> b;, output a + b

> **🗓️ Asked In Papers:** `2018-06 1(c)`

### Q113: Explain the use of the nested if statement with an example. :id=q113

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

An if placed inside another if/else block to evaluate hierarchical/dependent conditions.

> **🗓️ Asked In Papers:** `2018-12S 2(c)`

### Q114: List any four keywords in C++ and explain their functions. :id=q114

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

E.g., class (defines type), virtual (enables runtime dispatch), const (read-only), return (exits function with value).

> **🗓️ Asked In Papers:** `BCAOL S1-5`

