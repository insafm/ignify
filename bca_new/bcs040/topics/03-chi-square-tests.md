# 03. Chi-Square Tests

> **Syllabus Units:** Block 2 Unit 7 | **Rank:** #3 | **Frequency Score:** 37 | **Coverage:** 26/26 (100.0%) | **Importance:** Very High
> **Coverage:** 10 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q035: Explain / Describe the Chi-square test for Goodness of Fit with an example. :id=q035

🔴 **Very High Priority** • **6 (60 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests whether observed counts $O_i$ follow a theoretical expected distribution $E_i$ (e.g., fair die) using $\chi^2 = \sum \frac{(O_i-E_i)^2}{E_i}$ with $df = k - 1 - m$.

> **🗓️ Asked In Papers:** `Jun 2013 (Q7(a)), Dec 2014 (Q5(a)), Dec 2016 (Q6(a)), Jun 2018 (Q10(d)), June 2020 (Q6(i)), Jun 2024 (Q10(ii))`

---

### Q036: Chi-square Independence ($3 \times 3$): Hair colour vs. Eye colour of 300 persons ([30,10,40], [40,20,40], [50,30,40]). :id=q036

🔴 **Very High Priority** • **6 (60 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 300, df = 4, $\chi^2 = 7.2917 < 9.49$ (5%) and $< 13.28$ (1% in 2019-I); fail to reject $H_0$ (no significant association).

> **🗓️ Asked In Papers:** `Dec 2017 (Q9), 2019-I (Q8), Jun 2021 (Q8), Jun 2022 (Q8), Jun 2023 (Q8), Dec 2024 (Q9)`

---

### Q037: Explain / Describe the Chi-square test for Independence of Attributes with an example. :id=q037

🔴 **Very High Priority** • **6 (30 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests independence of two categorical attributes in an $r \times c$ table using $E_{ij} = \frac{R_i \times C_j}{N}$, $\chi^2 = \sum \frac{(O_{ij}-E_{ij})^2}{E_{ij}}$, and $df = (r-1)(c-1)$.

> **🗓️ Asked In Papers:** `Jun 2013 (Q7(b)), Jun 2014 (Q5(c)), Jun 2016 (Q6(b)), Jun 2022 (Q6(b)), Jun 2025 (Q7(b)), Dec 2025 (Q6(b))`

---

### Q038: Chi-square Independence on unique contingency tables (School/Economic $4 \times 4$, Music/Age $3 \times 3$, City Smoke/Health $2 \times 3$, Home/Child $3 \times 2$). :id=q038

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Dec 14 Q8 (N = 1650, df = 9): $\chi^2 = 118.0511 > 16.918$; Jun 18 Q8 (N = 900, df = 4): $\chi^2 = 36.1227 > 9.488$; Jun 24 Q7 (N = 165, df = 2): $\chi^2 = 14.1138 > 5.99$; Jun 26 Q9 (N = 300, df = 2): $\chi^2 = 33.6806 > 5.99$. All four reject $H_0$.

> **🗓️ Asked In Papers:** `Dec 2014 (Q8), Jun 2018 (Q8), Jun 2024 (Q7), Jun 2026 (Q9)`

---

### Q039: Chi-square Goodness of Fit: Die rolled 1200 times (195, 289, 202, 242, 163, 109). Test if unbiased at 5% ($\chi^2_{0.05}(5) = 11.07$). :id=q039

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
$E_i = 200$ per face; $\chi^2 = 96.82 > 11.07$ (reject $H_0$; die is biased).

> **🗓️ Asked In Papers:** `Dec 2015 (Q3), Dec 2016 (Q9), June 2020 (Q2)`

---

### Q040: Chi-square Goodness of Fit: Digits 0–9 frequencies (99, 100, 82, 65, 50, 77, 88, 57, 82, 30). Test uniform occurrence at 5% ($\chi^2_9(0.05) = 16.918$). :id=q040

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Total N = 730, $E_i = 73$ per digit; $\chi^2 = 61.7260 > 16.918$ (reject $H_0$; frequencies are not uniform).

> **🗓️ Asked In Papers:** `Jun 2015 (Q3), Dec 2020 (Q10), Jun 2023 (Q6)`

---

### Q041: Chi-square Independence ($3 \times 3$): Education level vs. Marriage adjustment score ([25,5,10], [50,30,40], [120,60,60], $\chi^2_{4,0.05} = 9.488$). :id=q041

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 400, df = 4, $\chi^2 = 7.3529 < 9.488$; fail to reject $H_0$ (cannot conclude higher education implies greater marriage adjustment).

> **🗓️ Asked In Papers:** `Dec 2015 (Q9), Dec 2018 (Q7), Jun 2025 (Q8)`

---

### Q042: Chi-square Independence ($2 \times 2$): Air pollution bother in two communities ([43,157], [81,119], $\chi^2_{1,0.05} = 3.841$). :id=q042

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 400, df = 1, $\chi^2 = 16.8770 > 3.841$ (reject $H_0$; communities are bothered differently).

> **🗓️ Asked In Papers:** `Jun 2015 (Q9), Dec 2023 (Q10)`

---

### Q043: Chi-square Independence ($3 \times 3$): Performance in Statistics vs. Computer Sciences ([36,72,42], [34,122,44], [50,56,44], $\chi^2_{0.05,4} = 9.49$). :id=q043

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 500, df = 4, $\chi^2 = 21.4037 > 9.49$ (reject $H_0$; performances are dependent).

> **🗓️ Asked In Papers:** `Jun 2017 (Q10), Dec 2022 (Q9)`

---

### Q044: Chi-square Independence ($2 \times 2$): College students' IQ vs. Parents' economic condition (N = 1000, $\chi^2_{1,0.01} = 6.63$). :id=q044

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
2019-II (6384) Q8 ([240,160],[460,140]): $\chi^2 = 31.7460 > 6.63$. Dec 21 Q9 ([230,170],[470,130]): $\chi^2 = 49.6032 > 6.63$. Both reject $H_0$.

> **🗓️ Asked In Papers:** `Dec June 2019 (Q8), Dec 2021 (Q9)`
