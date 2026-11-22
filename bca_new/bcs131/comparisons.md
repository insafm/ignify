# ⚖️ Most Repeated Comparison Questions

> Comparison questions form IGNOU's most predictable **5- to 10-mark structural template**. In almost every term-end examination, examiners ask at least two direct comparison questions.

---

## 📊 Comparison Frequency Leaderboard

| Comparison Pair | Related Canonical Question | Frequency | Total Marks | Most Recent Appearance |
| :--- | :---: | :---: | :---: | :---: |
| Structured / Procedural Programming vs. OOP | [Q134](/bca_new/bcs131/questions.md#q134) | **16** | 103 | `Jun 2026 Q4(a)` |
| Function Overloading vs. Function Overriding | [Q041](/bca_new/bcs131/questions.md#q041) | **7** | 60 | `Jun 2024 Q2(b)` |
| Virtual Function vs. Pure Virtual Function | [Q043](/bca_new/bcs131/questions.md#q043) | **6** | 36 | `Jun 2026 Q1(b)` |
| Encapsulation vs. Information Hiding | [Q136](/bca_new/bcs131/questions.md#q136) | **6** | 29 | `Jun 2023 Q2(c)` |
| Compile-Time vs. Run-Time Polymorphism | [Q047](/bca_new/bcs131/questions.md#q047) | **4** | 33 | `Jun 2021 Q4(d)` |
| Class Template vs. Function Template | [Q117](/bca_new/bcs131/questions.md#q117) | **4** | 31 | `Jun 2021 Q5(b)` |
| Default Constructor vs. Parameterized Constructor | [Q061](/bca_new/bcs131/questions.md#q061) | **4** | 26 | `Jun 2021 Q5(c-i)` |
| Multiple vs. Multilevel Inheritance | [Q147](/bca_new/bcs131/questions.md#q147) | **4** | 24 | `Jun 2026 Q1(c)` |
| Structure vs. Class in C++ | [Q006](/bca_new/bcs131/questions.md#q006) | **4** | 20 | `Dec 2025 Q1(a)` |
| Call-by-Value vs. Call-by-Reference | [Q187](/bca_new/bcs131/questions.md#q187) | **3** | 28 | `Dec 2022 Q4(b)` |
| Copy Constructor vs. Default Constructor | [Q065](/bca_new/bcs131/questions.md#q065) | **3** | 22 | `Jun 2026 Q4(b)` |
| Early Binding vs. Late Binding | [Q053](/bca_new/bcs131/questions.md#q053) | **3** | 15 | `Jun 2025 Q4(c)` |
| Global vs. Local Variable Scope | [Q082](/bca_new/bcs131/questions.md#q082) | **3** | 15 | `Jun 2025 Q1(b)` |
| Keyword vs. Identifier | [Q084](/bca_new/bcs131/questions.md#q084) | **3** | 13 | `Dec 2025 Q2(c)` |

---

## 📝 Detailed Comparison Guides & Answer Templates

### ⚖️ Structured / Procedural Programming vs. OOP

**Q134** **Asked 16 times (103 marks)** **Recent: Jun 2026 Q4(a)**

**Key Differentiating Points:**

Procedural focuses on step-by-step algorithms and functions (top-down), data moves freely and is vulnerable. OOP models real-world entities with classes and objects (bottom-up), binding data and methods together with access control (data hiding).

### ⚖️ Function Overloading vs. Function Overriding

**Q041** **Asked 7 times (60 marks)** **Recent: Jun 2024 Q2(b)**

**Key Differentiating Points:**

Overloading occurs in the same class/scope with identical function name but differing parameter lists (resolved at compile-time). Overriding occurs in base-derived inheritance where derived redefines base's virtual function with identical signature and return type (resolved at run-time).

### ⚖️ Virtual Function vs. Pure Virtual Function

**Q043** **Asked 6 times (36 marks)** **Recent: Jun 2026 Q1(b)**

**Key Differentiating Points:**

Virtual function has a definition in the base class and provides default behavior (base class can be instantiated). Pure virtual function has `= 0` syntax, usually no body in base, forces derived classes to override it, and makes the class abstract (cannot be instantiated).

### ⚖️ Encapsulation vs. Information Hiding

**Q136** **Asked 6 times (29 marks)** **Recent: Jun 2023 Q2(c)**

**Key Differentiating Points:**

Encapsulation is the mechanism of packaging data and the methods operating on that data into a single unit (class). Information Hiding is the design principle of concealing internal object state and implementation details from outside code (achieved using private/protected access specifiers).

### ⚖️ Compile-Time vs. Run-Time Polymorphism

**Q047** **Asked 4 times (33 marks)** **Recent: Jun 2021 Q4(d)**

**Key Differentiating Points:**

Compile-time (Early/Static binding) resolves function calls at compile-time via function overloading, operator overloading, and templates (faster execution, less memory). Run-time (Late/Dynamic binding) resolves function calls during execution via virtual functions and base class pointers/references (flexible and extensible).

### ⚖️ Class Template vs. Function Template

**Q117** **Asked 4 times (31 marks)** **Recent: Jun 2021 Q5(b)**

**Key Differentiating Points:**

Function template defines a generic algorithm where data types are passed as parameters (type deduction is automatic from function arguments). Class template defines a generic class/data-structure (e.g. Stack<T>, Vector<T>) where explicit type specification like `<int>` is required at instantiation.

### ⚖️ Default Constructor vs. Parameterized Constructor

**Q061** **Asked 4 times (26 marks)** **Recent: Jun 2021 Q5(c-i)**

**Key Differentiating Points:**

Default constructor takes zero arguments (or all arguments have default values) and initializes objects with default states. Parameterized constructor accepts one or more arguments to initialize distinct objects with specific caller-provided values upon instantiation.

### ⚖️ Multiple vs. Multilevel Inheritance

**Q147** **Asked 4 times (24 marks)** **Recent: Jun 2026 Q1(c)**

**Key Differentiating Points:**

Multiple inheritance allows one derived class to inherit directly from two or more distinct base classes (class C : public A, public B), potentially causing diamond ambiguity. Multilevel inheritance is a chain of single derivations where class B inherits from A, and class C inherits from B (transitive inheritance).

### ⚖️ Structure vs. Class in C++

**Q006** **Asked 4 times (20 marks)** **Recent: Dec 2025 Q1(a)**

**Key Differentiating Points:**

In a C++ `struct`, members and base classes are `public` by default. In a `class`, members and base classes are `private` by default. Both support constructors, member functions, access specifiers, and inheritance.

### ⚖️ Call-by-Value vs. Call-by-Reference

**Q187** **Asked 3 times (28 marks)** **Recent: Dec 2022 Q4(b)**

**Key Differentiating Points:**

Call-by-Value copies the argument value into function parameters (modifications inside the function do not affect caller's original variable; extra memory for copy). Call-by-Reference passes an alias (&) to the original variable (modifications directly mutate caller's variable; zero copy overhead).

### ⚖️ Copy Constructor vs. Default Constructor

**Q065** **Asked 3 times (22 marks)** **Recent: Jun 2026 Q4(b)**

**Key Differentiating Points:**

Default constructor initializes an object from scratch with default values. Copy constructor (`ClassName(const ClassName& obj)`) initializes a newly created object as an exact replica of an existing object of the same class (prevents shallow-copy pointer aliasing).

### ⚖️ Early Binding vs. Late Binding

**Q053** **Asked 3 times (15 marks)** **Recent: Jun 2025 Q4(c)**

**Key Differentiating Points:**

Early Binding associates function call with code address at compile time based on pointer type (default in C++, faster). Late Binding defers association until runtime using the object's vptr and vtable (enabled by `virtual` keyword, allows polymorphic dispatch).

### ⚖️ Global vs. Local Variable Scope

**Q082** **Asked 3 times (15 marks)** **Recent: Jun 2025 Q1(b)**

**Key Differentiating Points:**

Local variables are declared inside a function or block, stored on stack, and accessible only within that block lifetime. Global variables are declared outside all functions, stored in data segment, exist for entire program execution, and can be accessed anywhere (or disambiguated with `::` operator).

### ⚖️ Keyword vs. Identifier

**Q084** **Asked 3 times (13 marks)** **Recent: Dec 2025 Q2(c)**

**Key Differentiating Points:**

Keywords are reserved words predefined by the C++ compiler with fixed syntactic meaning (e.g., `class`, `virtual`, `return`) and cannot be used as names. Identifiers are user-defined names given to variables, functions, arrays, and classes following naming rules.

