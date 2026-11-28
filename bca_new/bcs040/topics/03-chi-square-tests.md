# 03. Chi-Square Tests

> **Syllabus Units:** Block 2 Unit 7 | **Rank:** #3 | **Frequency Score:** 37 | **Coverage:** 26/26 (100.0%) | **Importance:** Very High
> **Coverage:** 10 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q035: Explain / Describe the Chi-square test for Goodness of Fit with an example. :id=q035

🔴 **Very High Priority** • **6 (60 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests whether observed counts $O_i$ follow a theoretical expected distribution $E_i$ (e.g., fair die) using $\chi^2 = \sum \frac{(O_i-E_i)^2}{E_i}$ with $df = k - 1 - m$.

**📝 Example PQP Question (Jun 2024 Q10(ii)):**

Write short notes on any two of the following:
(ii) Goodness of fit test *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2013 (Q7(a))](/bca_new/bcs040/pqp/BCS-040_June_2013.pdf ':ignore'), [Dec 2014 (Q5(a))](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [Dec 2016 (Q6(a))](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [Jun 2018 (Q10(d))](/bca_new/bcs040/pqp/BCS-040_June_2018.pdf ':ignore'), [June 2020 (Q6(i))](/bca_new/bcs040/pqp/BCS-040_June_2020.pdf ':ignore'), [Jun 2024 (Q10(ii))](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')

---

### Q036: Chi-square Independence ($3 \times 3$): Hair colour vs. Eye colour of 300 persons ([30,10,40], [40,20,40], [50,30,40]). :id=q036

🔴 **Very High Priority** • **6 (60 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 300, df = 4, $\chi^2 = 7.2917 < 9.49$ (5%) and $< 13.28$ (1% in 2019-I); fail to reject $H_0$ (no significant association).

**📝 Example PQP Question (Dec 2024 Q9):**

The following contingency table presents the analysis of 300 persons according to hair colour and eye colour:

| Hair Colour \ Eye Colour | Blue | Gray | Brown |
| :--- | :---: | :---: | :---: |
| Fair | 30 | 10 | 40 |
| Brown | 40 | 20 | 40 |
| Black | 50 | 30 | 40 |

Test the hypothesis that there is no association between hair colour and eye colour at 5% level of significance. (Given $\chi^2_{(4), 0.05} = 9.49$). *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2017 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2017.pdf ':ignore'), [2019-I (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2019.pdf ':ignore'), [Jun 2021 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2021.pdf ':ignore'), [Jun 2022 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2022.pdf ':ignore'), [Jun 2023 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2023.pdf ':ignore'), [Dec 2024 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2024.pdf ':ignore')

---

### Q037: Explain / Describe the Chi-square test for Independence of Attributes with an example. :id=q037

🔴 **Very High Priority** • **6 (30 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests independence of two categorical attributes in an $r \times c$ table using $E_{ij} = \frac{R_i \times C_j}{N}$, $\chi^2 = \sum \frac{(O_{ij}-E_{ij})^2}{E_{ij}}$, and $df = (r-1)(c-1)$.

**📝 Example PQP Question (Dec 2025 Q6(b)):**

Write short notes on the following:
(b) Chi-square test for independence of attributes *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2013 (Q7(b))](/bca_new/bcs040/pqp/BCS-040_June_2013.pdf ':ignore'), [Jun 2014 (Q5(c))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Jun 2016 (Q6(b))](/bca_new/bcs040/pqp/BCS-040_June_2016.pdf ':ignore'), [Jun 2022 (Q6(b))](/bca_new/bcs040/pqp/BCS-040_June_2022.pdf ':ignore'), [Jun 2025 (Q7(b))](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore'), [Dec 2025 (Q6(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q038: Chi-square Independence on unique contingency tables (School/Economic $4 \times 4$, Music/Age $3 \times 3$, City Smoke/Health $2 \times 3$, Home/Child $3 \times 2$). :id=q038

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (June 2026, Q9 — 10 Marks)
The following data give the information about the condition of home and condition of child of 300 families:

| Condition of Home | Child Clean ($C_1$) | Child Dirty ($C_2$) | Total ($R_i$) |
| :--- | :---: | :---: | :---: |
| **Clean ($R_1$)** | 70 | 50 | **120** |
| **Fairly Clean ($R_2$)** | 80 | 20 | **100** |
| **Dirty ($R_3$)** | 30 | 50 | **80** |
| **Total ($C_j$)** | **180** | **120** | **$N = 300$** |

*Hypothesis:* $H_0:$ Condition of home and condition of child are independent vs. $H_1:$ They are not independent. Test at $\alpha = 0.05$ (Given $\chi^2_{0.05}(2) = 5.99$).

#### 🧮 Step-by-Step Expected Frequencies & Chi-Square Calculation:
Formula for expected frequency: $E_{ij} = \frac{R_i \times C_j}{N}$
- $E_{11} = \frac{120 \times 180}{300} = 72$, $E_{12} = \frac{120 \times 120}{300} = 48$
- $E_{21} = \frac{100 \times 180}{300} = 60$, $E_{22} = \frac{100 \times 120}{300} = 40$
- $E_{31} = \frac{80 \times 180}{300} = 48$, $E_{32} = \frac{80 \times 120}{300} = 32$

| Cell ($i, j$) | Observed ($O_{ij}$) | Expected ($E_{ij}$) | Difference ($O - E$) | $(O - E)^2$ | $\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Clean, Clean | 70 | 72 | -2 | 4 | 0.0556 |
| Clean, Dirty | 50 | 48 | +2 | 4 | 0.0833 |
| Fairly Clean, Clean | 80 | 60 | +20 | 400 | 6.6667 |
| Fairly Clean, Dirty | 20 | 40 | -20 | 400 | 10.0000 |
| Dirty, Clean | 30 | 48 | -18 | 324 | 6.7500 |
| Dirty, Dirty | 50 | 32 | +18 | 324 | 10.1250 |
| **Total** | **300** | **300** | **0** | — | $\mathbf{\chi^2 = 33.6806}$ |

- **Degrees of Freedom:** $df = (r - 1)(c - 1) = (3 - 1)(2 - 1) = 2 \times 1 = 2$.
- **Statistical Decision:** Since calculated $\chi^2 = 33.68 > 5.99$, we **reject $H_0$** at the 5% level of significance. Condition of home and condition of child are strongly associated (not independent).

#### 🔄 Cross-Session Variations & Contingency Table Setups:
| Exam Session | Contingency Table Setup | Dimensions | Calculated $\chi^2$ | Critical $\chi^2$ | Statistical Decision |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Dec 2014 (Q8)** | School Types vs. Economic Class | $4 \times 4$ ($N = 1650, df = 9$) | $\chi^2 = 118.05$ | $\chi^2_{0.05}(9) = 16.918$ | **Reject $H_0$** (Dependent) |
| **Jun 2018 (Q8)** | Music Preference vs. Age Group | $3 \times 3$ ($N = 900, df = 4$) | $\chi^2 = 36.12$ | $\chi^2_{0.05}(4) = 9.488$ | **Reject $H_0$** (Dependent) |
| **Jun 2024 (Q7)** | City Smoking vs. Physical Health | $2 \times 3$ ($N = 165, df = 2$) | $\chi^2 = 14.11$ | $\chi^2_{0.05}(2) = 5.99$ | **Reject $H_0$** (Dependent) |
| **Jun 2026 (Q9)** | Condition of Home vs. Condition of Child | $3 \times 2$ ($N = 300, df = 2$) | $\chi^2 = 33.68$ | $\chi^2_{0.05}(2) = 5.99$ | **Reject $H_0$** (Dependent) |

**📝 Example PQP Question (Jun 2026 Q9):**

The following data give the information about the condition of home and condition of child of 300 families:

| Condition of Child \ Condition of Home | Clean | Dirty |
| :--- | :---: | :---: |
| Clean | 70 | 50 |
| Fairly clean | 80 | 20 |
| Dirty | 30 | 50 |

Using the Chi-square test, test whether the condition of home and condition of the child are independent or not at 5% level of significance. (Given $\chi^2_{(2), 0.05} = 5.99$) *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2014 (Q8)](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [Jun 2018 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2018.pdf ':ignore'), [Jun 2024 (Q7)](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore'), [Jun 2026 (Q9)](/bca_new/bcs040/pqp/BCS-040_June_2026.pdf ':ignore')

---

### Q039: Chi-square Goodness of Fit: Die rolled 1200 times (195, 289, 202, 242, 163, 109). Test if unbiased at 5% ($\chi^2_{0.05}(5) = 11.07$). :id=q039

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
$E_i = 200$ per face; $\chi^2 = 96.82 > 11.07$ (reject $H_0$; die is biased).

**📝 Example PQP Question (June 2020 Q2):**

A dice is rolled 1200 times with the following results:

| No. that comes up | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Frequency | 195 | 289 | 202 | 242 | 163 | 109 |

Test the hypothesis, if the dice is unbiased at 5% level of significance (Given that $\chi^2_{0.05}(5) = 11.07$). *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2015 (Q3)](/bca_new/bcs040/pqp/BCS-040_Dec_2015.pdf ':ignore'), [Dec 2016 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [June 2020 (Q2)](/bca_new/bcs040/pqp/BCS-040_June_2020.pdf ':ignore')

---

### Q040: Chi-square Goodness of Fit: Digits 0–9 frequencies (99, 100, 82, 65, 50, 77, 88, 57, 82, 30). Test uniform occurrence at 5% ($\chi^2_9(0.05) = 16.918$). :id=q040

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Total N = 730, $E_i = 73$ per digit; $\chi^2 = 61.7260 > 16.918$ (reject $H_0$; frequencies are not uniform).

**📝 Example PQP Question (Dec 2020 Q10):**

Telephone directories have telephone numbers which are the combinations of ten digits 0 to 9. The observer notes the frequency of occurrence of these digits and wants to test whether the digits occur with same frequency or not ($\alpha = 0.05$). The data is tabulated below:

| Digits | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Frequency | 99 | 100 | 82 | 65 | 50 | 77 | 88 | 57 | 82 | 30 |

(Given that $\chi^2_9(0.05) = 16.918$). *(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q3)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2020 (Q10)](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore'), [Jun 2023 (Q6)](/bca_new/bcs040/pqp/BCS-040_June_2023.pdf ':ignore')

---

### Q041: Chi-square Independence ($3 \times 3$): Education level vs. Marriage adjustment score ([25,5,10], [50,30,40], [120,60,60], $\chi^2_{4,0.05} = 9.488$). :id=q041

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 400, df = 4, $\chi^2 = 7.3529 < 9.488$; fail to reject $H_0$ (cannot conclude higher education implies greater marriage adjustment).

**📝 Example PQP Question (Jun 2025 Q8):**

The following table summarizes a sample showing the level of education and marriage adjustment score for married persons:

| Level of Education \ Marriage Adjustment Score | Low | High | Very High |
| :--- | :---: | :---: | :---: |
| Middle School | 25 | 5 | 10 |
| High School | 50 | 30 | 40 |
| College | 120 | 60 | 60 |

Can you calculate from the above, the higher the level of education, the greater is the degree of adjustment in marriage? (Given: $\chi^2_{(4, 0.05)} = 9.488$). *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2015 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2015.pdf ':ignore'), [Dec 2018 (Q7)](/bca_new/bcs040/pqp/BCS-040_Dec_2018.pdf ':ignore'), [Jun 2025 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore')

---

### Q042: Chi-square Independence ($2 \times 2$): Air pollution bother in two communities ([43,157], [81,119], $\chi^2_{1,0.05} = 3.841$). :id=q042

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 400, df = 1, $\chi^2 = 16.8770 > 3.841$ (reject $H_0$; communities are bothered differently).

**📝 Example PQP Question (Dec 2023 Q10):**

In order to study the impact of air pollution on households, a random sample of 200 households was selected from each of the two communities. The respondent in each house was asked whether or not any one in the house was bothered by air pollution. The responses are tabulated below (Given $\chi^2_1(0.05) = 3.841, \alpha = 0.05$):

| Community | Yes | No | Total |
| :--- | :---: | :---: | :---: |
| I | 43 | 157 | 200 |
| II | 81 | 119 | 200 |
| **Total** | **124** | **276** | **400** |

Can the researcher conclude that the 2 communities are bothered differently by air pollution? *(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q9)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2023 (Q10)](/bca_new/bcs040/pqp/BCS-040_Dec_2023.pdf ':ignore')

---

### Q043: Chi-square Independence ($3 \times 3$): Performance in Statistics vs. Computer Sciences ([36,72,42], [34,122,44], [50,56,44], $\chi^2_{0.05,4} = 9.49$). :id=q043

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 500, df = 4, $\chi^2 = 21.4037 > 9.49$ (reject $H_0$; performances are dependent).

**📝 Example PQP Question (Dec 2022 Q9):**

The table given below shows the relation between the performance of students in Statistics and Computer Sciences. Test the hypothesis that the performance in Statistics is independent of the performance in Computer Sciences using 5% level of significance. (Given that $\chi^2_{0.05, 4} = 9.49$).

| Statistics \ Computer Science | High Grade | Medium Grade | Low Grade |
| :--- | :---: | :---: | :---: |
| High Grade | 36 | 72 | 42 |
| Medium Grade | 34 | 122 | 44 |
| Low Grade | 50 | 56 | 44 |

*(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2017 (Q10)](/bca_new/bcs040/pqp/BCS-040_June_2017.pdf ':ignore'), [Dec 2022 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore')

---

### Q044: Chi-square Independence ($2 \times 2$): College students' IQ vs. Parents' economic condition (N = 1000, $\chi^2_{1,0.01} = 6.63$). :id=q044

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
2019-II (6384) Q8 ([240,160],[460,140]): $\chi^2 = 31.7460 > 6.63$. Dec 21 Q9 ([230,170],[470,130]): $\chi^2 = 49.6032 > 6.63$. Both reject $H_0$.

**📝 Example PQP Question (Dec 2021 Q9):**

1000 students at college level were graded according to their IQ levels and the economic condition of their parents, as follows:

| Economic Condition \ IQ Level | High | Low | Total |
| :--- | :---: | :---: | :---: |
| Rich | 230 | 170 | 400 |
| Poor | 470 | 130 | 600 |
| **Total** | **700** | **300** | **1000** |

Test whether there is any association between IQ level and economic condition of parents at 1% level of significance. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec June 2019 (Q8)](/bca_new/bcs040/pqp/BCS-040_Dec_2019.pdf ':ignore'), [Dec 2021 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2021.pdf ':ignore')
