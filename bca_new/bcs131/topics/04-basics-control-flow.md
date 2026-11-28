# 04. C++ Basics, Operators & Control Flow

> **Syllabus Unit:** Block 1 Unit 2 | **Rank:** #4 | **Frequency Score:** 91.0 | **Offered Marks:** 321 | **Papers Present:** 27/30 | **Importance:** High
> **Coverage:** 36 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q079: Explain the use of break and continue statements in C++ with an example program. :id=q079

🟠 **High Priority** • **4 (25 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

break terminates the enclosing loop/switch immediately; continue skips remaining statements in current iteration and jumps to next iteration.

**📝 Example PQP Question (2021-06 2(d)):**

Compare Break and Continue statement. Exhibit the usage of break and continue statement with suitable code in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2016-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2019-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2021-06 2(d)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q080: What is the scope resolution operator (::)? Explain its uses with a C++ program. :id=q080

🟠 **High Priority** • **4 (19 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Accesses hidden global variables (::x), defines class member functions outside class (Class::f()), and resolves multiple inheritance ambiguity.

**📝 Example PQP Question (2020-06 1(h)):**

What is scope resolution operator? Explain its use with the help of a C++ program. 4 I3 BCS-031

> **🗓️ Asked In Papers:** [2013-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2019-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2020-12 5(v)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore')

### Q081: What is an operator? List and explain the various types of operators available in C++. :id=q081

🟠 **High Priority** • **3 (26 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Arithmetic, Relational, Logical, Bitwise, Assignment, Increment/Decrement, Ternary (?:), Scope resolution (::), sizeof, and new/delete.

**📝 Example PQP Question (2018-12S 1(c)):**

What are the operators in C++? Explain with an example. *(8 marks)*

> **🗓️ Asked In Papers:** [2013-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2018-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2018-12S 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q082: What is the scope of a variable? Compare global variables and local variables in C++ with example code. :id=q082

🟠 **High Priority** • **3 (15 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Local: declared inside block/function, stack-allocated, limited visibility; Global: declared outside functions, data-segment lifetime, file-wide access.

**📝 Example PQP Question (2025-06 1(b)):**

What do you understand by scope of a variable? Compare global variable and local variable in C++, with suitable example code. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2021-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2025-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q083: What is type conversion? Differentiate between automatic (implicit) type conversion and explicit type casting with examples. :id=q083

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Implicit: compiler promotes smaller to larger types (int to double); Explicit casting: programmer forces conversion ((int)x or static_cast<int>(x)).

**📝 Example PQP Question (2023-06 2(b)):**

Differentiate between automatic and typecasting with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2018-12S 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2021-06 2(c)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2023-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q084: What is the difference between a keyword and an identifier? Explain with a simple C++ program. :id=q084

🟠 **High Priority** • **3 (13 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Keywords are compiler-reserved words with fixed meaning (int, class, return); identifiers are programmer-defined names for variables/functions/classes.

**📝 Example PQP Question (2025-12 2(c)):**

What is the difference between a keyword and an identifier? Explain with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2022-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q085: What is a data type? List built-in data types (and sizes) with examples, and explain the need for derived data types. :id=q085

🔵 **Medium Priority** • **2 (11 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Built-in: char (1B), int (4B), float (4B), double (8B), bool (1B), void; Derived (arrays, pointers, references) model collections/indirection.

**📝 Example PQP Question (2025-12 1(d)):**

List any five data types of C++ with an example of each. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2025-12 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q086: Write a C++ program to demonstrate the use of the switch statement. :id=q086

🔵 **Medium Priority** • **2 (11 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

switch(choice) with case labels, break; after each case, and default: fallback (e.g., day-of-week or menu).

**📝 Example PQP Question (2018-12S 1(d)):**

Write a program in C++ to demonstrate the use of Switch statement. *(6 marks)*

> **🗓️ Asked In Papers:** [2015-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2018-12S 1(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q087: Discuss and draw the taxonomy/hierarchy of data types in C++. :id=q087

🔵 **Medium Priority** • **2 (10 marks)** • *Theory + Diagram / Short Answer*

**💡 Key Answer Points:**

Three branches: Built-in (int, char, float, double, void), Derived (array, function, pointer, reference), User-defined (class, struct, union, enum).

**📝 Example PQP Question (2021-12 2(c)):**

Discuss the taxonomy of C++ data types with the help of a suitable block diagram. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2021-12 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q088: Write a program in C++ to calculate the factorial of a given number. :id=q088

🔵 **Medium Priority** • **2 (10 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read n; initialize long long fact = 1; loop i = 1..n multiplying fact *= i; handle n=0 -> 1.

**📝 Example PQP Question (2018-12S 3(c)):**

Write a program in C++ to find the factorial of a given number. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2018-12S 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q089: What are breaking statements? Give the syntax of break, continue, goto, and exit. :id=q089

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

break;, continue;, goto label; ... label:, and exit(status); (from <cstdlib>, terminates entire process).

**📝 Example PQP Question (2025-12 1(f)):**

Write the syntax of the following statements: *(5 marks)*

> **🗓️ Asked In Papers:** [2021-12 2(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2025-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q090: Explain relational and logical operators in C++ (any five) with examples. :id=q090

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Relational (==, !=, <, >, <=, >=) compare operands; Logical (&&, ||, !) combine boolean conditions.

**📝 Example PQP Question (2024-12 1(e)):**

Explain any five operators among relational and logical operators used in C++ along with an example for each. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2024-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q091: Explain any five relational operators in C++ with examples. :id=q091

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

<, <=, >, >=, ==, != returning bool (true/false, i.e., 1/0).

**📝 Example PQP Question (2019-06 1(h)):**

Explain any five relational operators in C++ with the help of examples. *(5 marks)*

> **🗓️ Asked In Papers:** [2019-06 1(h)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2022-12 5(v)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore')

### Q092: Write a C++ program that prints numbers and their cubes from 1 to 10 using if-then-else and for loop. :id=q092

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

for(int i=1; i<=10; i++) checking boundary/parity via if-else and printing i and i*i*i.

**📝 Example PQP Question (2014-06 3(a)):**

Write a program in C++ that prints numbers and its cubes from 1 to 10 by using if-then-else and for loop. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore')

### Q093: Write an interactive C++ program reading two integers x, y and an operator (+, -, *, /), printing an error for any other operator. :id=q093

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

switch(op) handling +, -, *, / (with y==0 guard) and default: cout << "Invalid operator";.

**📝 Example PQP Question (2016-06 3(b)):**

Write an interactive C++ program which reads two integer numbers x and y, and an operator. It then performs the following operations:

> **🗓️ Asked In Papers:** [2016-06 3(b)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore')

### Q094: Write a C++ program to find the difference between two times in 24-hour format (e.g., 09:00:00 - 13:30:00 = 19:30:00). :id=q094

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Convert hh:mm:ss to total seconds; if t1 < t2, add 86,400 seconds (24h wrap-around); convert back to HH:MM:SS.

**📝 Example PQP Question (2016-06 5(b)):**

Write a C++ program for finding the difference between two times that are given in 24 hour format. So "19:00:00" — "3:30:00" = 15:30:00, while "09:00:00" — "13:30:00" = "19:30:00". *(10 marks)*

> **🗓️ Asked In Papers:** [2016-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore')

### Q095: How are strings handled in C++? Explain how a string can be reversed with the help of a program. :id=q095

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

C-style char[] (\0-terminated, <cstring>) and std::string; reverse via two-pointer swap (start++, end--).

**📝 Example PQP Question (BCAOL S2-12):**

How are Strings handled in C++? Explain how a string can be revised with the help of a program. *(10 marks)*

> **🗓️ Asked In Papers:** [BCAOL S2-12](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q096: What are comparison and logical operators? How do they differ from arithmetic and assignment operators? :id=q096

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Comparison/logical produce bool for branching; arithmetic compute numeric values; assignment (=, +=) mutates lvalue memory.

**📝 Example PQP Question (2014-06 1(c)):**

What is meant by comparison and logical operators? How are they different from the arithmetic and assignment operators, explain with the help of an example. *(8 marks)*

> **🗓️ Asked In Papers:** [2014-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore')

### Q097: Explain the use of the following operators in C++: (i) &, (ii) ?:, (iii) ::, (iv) &&. :id=q097

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

& (address-of/reference/bitwise AND), ?: (ternary conditional), :: (scope resolution), && (logical AND with short-circuiting).

**📝 Example PQP Question (2016-12 4(c)):**

Explain the use of the following operators in C++:

> **🗓️ Asked In Papers:** [2016-12 4(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore')

### Q098: What is looping in C++? Explain its advantages and list the looping options available in C++. :id=q098

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Avoids code duplication, enables traversal; options: for (entry-controlled), while (entry-controlled), do-while (exit-controlled).

**📝 Example PQP Question (2014-06 1(e)):**

What is looping in C++? What are the advantages of using loops in C++? Also list the various looping options available in C++. *(6 marks)*

> **🗓️ Asked In Papers:** [2014-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore')

### Q099: Write a C++ program to find the area of a circle. :id=q099

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read r; compute float area = 3.14159 * r * r; and output area.

**📝 Example PQP Question (2014-12 5(c)):**

Write a C++ program to find the area of a circle.

> **🗓️ Asked In Papers:** [2014-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore')

### Q100: How do you input non-graphic characters in C++? What do escape sequences \n, \a, and \v represent? :id=q100

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Entered via backslash escape sequences; \n = newline, \a = alert/bell, \v = vertical tab.

**📝 Example PQP Question (2015-12 1(b)):**

How do you input non-graphic characters in the C++ programming language? What do these escape sequences represent? 5

> **🗓️ Asked In Papers:** [2015-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore')

### Q101: Compare while() and do-while() looping constructs with a suitable example for each. :id=q101

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

while checks condition before body (0 or more runs); do-while checks after body (at least 1 run, ends with semicolon).

**📝 Example PQP Question (2019-12 1(e)):**

Compare while ( ) and do-while( ) looping constructs with the help of suitable example for each. *(5 marks)*

> **🗓️ Asked In Papers:** [2019-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore')

### Q102: Differentiate between C and C++ (give at least five differences). :id=q102

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Procedural vs. OOP; stdio.h vs. iostream; malloc/free vs. new/delete; no overloading/references/classes in C vs. full support in C++.

**📝 Example PQP Question (2021-06 2(b)):**

Differentiate between C and C++, give at least five differences. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q103: Explain the use of && and ! operators in C++ with an example. :id=q103

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

&& returns true only if both operands are true; ! negates a boolean operand.

**📝 Example PQP Question (2021-06 3(d)):**

Explain the use of ‘&&’ and ‘!’ operators in C++ with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 3(d)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

### Q104: What is the difference between an if statement and a for loop? Explain with an example. :id=q104

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

if is a single-decision conditional branch (executes 0 or 1 time); for is an iterative loop repeating until condition becomes false.

**📝 Example PQP Question (2023-06 3(c)):**

What is the difference between If statement and For loop? Explain with example. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 3(c)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q105: What is operator precedence? Explain the precedence order in arithmetical operators in C++ with an example. :id=q105

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Determines evaluation order: parentheses () highest, then unary ++/--/-, then *, /, % (left-to-right), then +, - (left-to-right).

**📝 Example PQP Question (2023-06 3(d)):**

What is operator precedence? Explain the order of operator precedence in arithmetical operators in C++ with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-06 3(d)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q106: Explain the working of the goto statement. Does its usage violate the rules of OOP? :id=q106

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Unconditional jump to a labeled statement in same function; discourages structured modularity and risks bypassing object initialization/cleanup.

**📝 Example PQP Question (2023-12 1(e)):**

Explain the working of GOTO statement. Does its usage violate the rules of OOP? Explain. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-12 1(e)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q107: Write a C++ program to find whether a given number is odd or even. :id=q107

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Read n; if (n % 2 == 0) cout << "Even"; else cout << "Odd";

**📝 Example PQP Question (2023-12 2(b)):**

Write a C++ program to find whether a given number is odd or even. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q108: Explain the use of the do-while loop with the help of a C++ program. :id=q108

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Post-tested loop ideal for menu-driven programs requiring at least one execution.

**📝 Example PQP Question (2023-12 5(a)):**

Explain use of do---while loop with the help of a program. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q109: Explain the working of the for loop with the help of an example C++ program. :id=q109

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Coding / Short Answer*

**💡 Key Answer Points:**

Three clauses (init; condition; update): initializes once, checks condition before each iteration, updates after body.

**📝 Example PQP Question (2024-06 1(e)):**

Explain the working of for loop with the help of an example C++ program. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q110: What is a Reference Variable, and what is its usage in C++? :id=q110

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Alias to an existing variable (int& ref = x;), must be initialized at declaration, used for pass-by-reference and operator overloading.

**📝 Example PQP Question (2017-12 1(b)):**

What is a Reference Variable? What is its usage?

> **🗓️ Asked In Papers:** [2017-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore')

### Q111: What are data modifiers? How do they affect base data types? Give a suitable example. :id=q111

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

signed, unsigned, short, long alter memory width and value range of int/char/double.

**📝 Example PQP Question (2017-12S 1(b)):**

What are data modifiers? How do they affect the base data type? Give suitable example. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore')

### Q112: Write a C++ program to find the sum of two given numbers. :id=q112

⚪ **Low Priority** • **1 (4 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Declare int a, b;, read via cin >> a >> b;, output a + b

**📝 Example PQP Question (2018-06 1(c)):**

Write a C++ program to find the sum of two given numbers. *(4 marks)*

> **🗓️ Asked In Papers:** [2018-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore')

### Q113: Explain the use of the nested if statement with an example. :id=q113

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

An if placed inside another if/else block to evaluate hierarchical/dependent conditions.

**📝 Example PQP Question (2018-12S 2(c)):**

Explain the use of nested if statement with the help of an example. *(4 marks)*

> **🗓️ Asked In Papers:** [2018-12S 2(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q114: List any four keywords in C++ and explain their functions. :id=q114

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

E.g., class (defines type), virtual (enables runtime dispatch), const (read-only), return (exits function with value).

**📝 Example PQP Question (BCAOL S1-5):**

List any four keywords in C++. Also, explain their functions. *(4 marks)*

> **🗓️ Asked In Papers:** [BCAOL S1-5](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

