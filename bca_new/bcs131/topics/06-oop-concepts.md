# 06. OOP Concepts & Paradigms

> **Syllabus Unit:** Block 1 Unit 1 | **Rank:** #6 | **Frequency Score:** 81.5 | **Offered Marks:** 283 | **Papers Present:** 29/30 | **Importance:** High
> **Coverage:** 11 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q134: What is the Object-Oriented Programming (OOP) paradigm? Explain its basic characteristics and advantages over structured/procedural programming. :id=q134

🔴 **Very High Priority** • **16 (103 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Models real-world entities combining data + behavior (Encapsulation, Abstraction, Inheritance, Polymorphism); improves security, modularity, reusability, and scalability over top-down procedural C.

**📝 Example PQP Question (2026-06 4(a)):**

What is Object Oriented Programming? How does it differ from Procedural Programming? Give examples. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2013-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2014-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2014-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2015-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore'), [2016-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore'), [2017-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore'), [2019-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2021-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2021-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore'), [2022-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2023-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2024-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2025-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore'), [2026-06 4(a)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q135: What is message passing? Explain how it is used in C++ (and supports interfaces) with an example. :id=q135

🔴 **Very High Priority** • **12 (76 marks)** • *Theory (+ Coding) / Short Answer & Long Answer*

**💡 Key Answer Points:**

Objects communicate by invoking each other's public member functions (obj.method(args)); decouples internal implementation from public interface.

**📝 Example PQP Question (2025-12 2(a)):**

Explain message passing in C++ with the help of an example. 5 A–24/BCS–031/BCS–131

> **🗓️ Asked In Papers:** [2012-12 2(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2014-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2017-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2018-12S 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2019-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2020-12 5(iv)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2022-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2022-12 5(ii)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [BCAOL S2-14](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore'), [2025-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q136: What is encapsulation? Are encapsulation and information hiding the same? Differentiate with an example. :id=q136

🔴 **Very High Priority** • **6 (29 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Not identical: encapsulation bundles data + methods into a single unit (class), while information hiding restricts access (private) so internals are shielded.

**📝 Example PQP Question (2023-06 2(c)):**

Explain the difference between information hiding and encapsulation with the help of an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2018-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore'), [2018-12S 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2020-06 1(b)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2022-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2022.pdf ':ignore'), [2023-06 2(c)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q137: Explain the features, advantages, and disadvantages of the structured programming paradigm with respect to OOP. :id=q137

🟠 **High Priority** • **3 (19 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Features: sequence/selection/iteration, top-down functions; Pros: simple for small tasks; Cons: global data exposure, poor real-world modeling, hard to scale.

**📝 Example PQP Question (2018-12S 1(a)):**

Write four advantages and four disadvantages of structured programming. *(8 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore'), [2015-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2015.pdf ':ignore'), [2018-12S 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore')

### Q138: What do you mean by Abstraction and Encapsulation? How are the two terms interrelated? :id=q138

🟠 **High Priority** • **3 (13 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Abstraction exposes essential interface hiding complexity ("what"); Encapsulation binds and protects implementation ("how"); encapsulation implements abstraction.

**📝 Example PQP Question (BCAOL S1-1):**

Explain the term ‘Abstraction’ with an example. *(4 marks)*

> **🗓️ Asked In Papers:** [2017-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-1.pdf ':ignore'), [2023-12 2(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore'), [BCAOL S1-1](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-2.pdf ':ignore')

### Q139: Write a short note on Encapsulation with an example. :id=q139

🔵 **Medium Priority** • **2 (10 marks)** • *Theory (+ Coding) / Short Answer*

**💡 Key Answer Points:**

Wrapping data members and member functions inside a class with controlled public accessors/mutators.

**📝 Example PQP Question (2019-06 5(c)):**

Write a short note on: Encapsulation *(5 marks)*

> **🗓️ Asked In Papers:** [2014-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2019-06 5(c)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

### Q140: Explain any four benefits of Object-Oriented Programming. :id=q140

🔵 **Medium Priority** • **2 (9 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Reusability (inheritance), Data Security (encapsulation), Extensibility (polymorphism), and Real-world modeling/Maintainability.

**📝 Example PQP Question (2023-06 2(a)):**

What is object oriented programming? Explain the benefits of object oriented programming. *(5 marks)*

> **🗓️ Asked In Papers:** [2017-12S 1(h)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2023-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore')

### Q141: What is encapsulation? Explain how it differs from information hiding using a Library Books issue/return program. :id=q141

⚪ **Low Priority** • **1 (8 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

LibraryBook class bundles bookID, isIssued (private = info hiding) with issueBook()/returnBook() (public methods = encapsulation).

**📝 Example PQP Question (2012-12 1(b)):**

What is encapsulation? Explain how it is different from information hiding with the help of an example program to manage Books issue and return in a Library. *(8 marks)*

> **🗓️ Asked In Papers:** [2012-12 1(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore')

### Q142: Define Abstraction and Encapsulation, and explain class and object with an example. :id=q142

⚪ **Low Priority** • **1 (6 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Combine definitions of both OOP pillars with a concrete Car/Account class and object instantiation.

**📝 Example PQP Question (2018-06 1(a)):**

Define Abstraction and Encapsulation in object oriented programming. Explain class and object with the help of an example. *(6 marks)*

> **🗓️ Asked In Papers:** [2018-06 1(a)](/bca_new/bcs131/pqp/BCS-031_June_2018.pdf ':ignore')

### Q143: What design concepts would you keep in mind while designing an object-oriented application? Explain with an example. :id=q143

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Identify domain classes/nouns, assign single responsibilities, favor composition/inheritance carefully, program to interfaces, and enforce encapsulation.

**📝 Example PQP Question (2023-12 5(d)):**

What design concepts you would keep in mind while designing an object oriented application? Explain with an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2023-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2023.pdf ':ignore')

### Q144: "A class is a way to accomplish data hiding." Comment with a suitable example. :id=q144

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Default private access prevents external direct corruption of member state, allowing mutation only through validated public methods.

**📝 Example PQP Question (2024-12 1(a)):**

“A class is a way to accomplish data hiding.” Comment with a suitable example. *(5 marks)*

> **🗓️ Asked In Papers:** [2024-12 1(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

