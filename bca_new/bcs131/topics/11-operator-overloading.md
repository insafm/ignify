# 11. Operator Overloading

> **Syllabus Unit:** Block 2 Unit 2 | **Rank:** #11 | **Frequency Score:** 43.5 | **Offered Marks:** 163 | **Papers Present:** 20/30 | **Importance:** Medium-Low
> **Coverage:** 9 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q203: What is operator overloading? Explain its advantages and general rules. :id=q203

🔴 **Very High Priority** • **7 (42 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Redefines existing C++ operators for user-defined types (operator@); rules: cannot create new tokens, cannot change arity/precedence, at least one operand must be user-defined.

**📝 Example PQP Question (2019-06 1(d)):**

What is operator overloading ? Briefly explain general rules of operator overloading. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2013-12 5(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2015-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2019-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2023-12 1(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [2023-12 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q204: Write a C++ program (with comments) to overload the binary + operator to add two complex numbers. :id=q204

🟠 **High Priority** • **3 (25 marks)** • *Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Complex operator+(const Complex& c) { return Complex(real + c.real, imag + c.imag); }

**📝 Example PQP Question (2025-06 1(f)):**

What is operator overloading ? Write a program in C++ to overload '+' operator to add two complex numbers. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2022-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2025-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q205: List the C++ operators that cannot be overloaded, and give reasons for why they cannot be overloaded. :id=q205

🟠 **High Priority** • **3 (16 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

:: (scope resolution), . (member access), .* (pointer-to-member), ?: (ternary), sizeof (and typeid); operate on names/types at compile time rather than runtime values.

**📝 Example PQP Question (2017-12 2(b)):**

What is Operator Overloading ? List the operators which cannot be overloaded. Give reasons behind it. *(7 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(d)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2017-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [BCAOL S1-4](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q206: What is operator overloading? List operators that cannot be overloaded and write a C++ program to overload unary minus (-). :id=q206

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

void operator-() { x = -x; y = -y; } (or returns negated copy) + list of 5 non-overloadable operators.

**📝 Example PQP Question (2019-06 3(a)):**

What do you mean by operator-overloading in C++ ? List the operators which cannot be overloaded. Write a program in C++, to overload unary minus (-) operator. *(10 marks)*

> **🗓️ Asked In Papers:** [2015-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2019-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

### Q207: Write a C++ program to overload stream insertion (<<) and extraction (>>) operators (e.g., for a Date class dd, mm, yy). :id=q207

🔵 **Medium Priority** • **2 (20 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Must be non-member friend functions: friend ostream& operator<<(ostream& out, const Date& d) and friend istream& operator>>(istream& in, Date& d).

**📝 Example PQP Question (2024-12 4(a)):**

Write a program to overload input and output operators for data class having data members as dd,mm,yy. *(10 marks)*

> **🗓️ Asked In Papers:** [2017-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2024-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q208: Explain the need for operator overloading, why some operators cannot be overloaded, and write a program overloading + to add two complex numbers. :id=q208

🔵 **Medium Priority** • **2 (15 marks)** • *Theory + Coding / Short Answer & Long Answer*

**💡 Key Answer Points:**

Combines rules/non-overloadable list (::, ., .*, ?:, sizeof) with Complex::operator+ code.

**📝 Example PQP Question (2021-12 1(f)):**

What is operator overloading ? Why some operators can't be overloaded ? Write a program to overload '+' operator to add two complex numbers. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-12 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2021-12 1(f)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

### Q209: Explain the need for operator overloading, why some operators cannot be overloaded, and write a C++ program overloading + to concatenate two character strings. :id=q209

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

String class holding char str[100]; operator+ uses strcpy/strcat to concatenate and return new String.

**📝 Example PQP Question (2012-12 4(a)):**

Explain need of operator overloading. Also explain why some operators can not be overloaded ? Write a C++ program to overload '+' operator to add two character strings. *(10 marks)*

> **🗓️ Asked In Papers:** [2012-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore')

### Q210: Write a C++ program to overload += and *= operators for a Complex number class (real, imaginary). :id=q210

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Complex& operator+=(const Complex& c) updates real += c.real; imag += c.imag; return *this;; *= computes (ac - bd) + (ad + bc)i and returns *this.

**📝 Example PQP Question (2024-06 5(b)):**

Write a program to overload += and *= operator for complex number class (data members are real and imaginary for the class). *(10 marks)*

> **🗓️ Asked In Papers:** [2024-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q211: What are the limitations of Operator Overloading and Function Overloading? :id=q211

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Operator: fixed arity/precedence, 5 operators barred, cannot alter built-in type behavior; Function: cannot overload by return type alone, ambiguity with default args.

**📝 Example PQP Question (2021-06 4(c)):**

What are the limitations of Operator overloading and Function overloading. *(5 marks)*

> **🗓️ Asked In Papers:** [2021-06 4(c)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore')

