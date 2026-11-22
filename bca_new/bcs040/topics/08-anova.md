# 08. Analysis of Variance (ANOVA)

> **Syllabus Units:** Block 3 Unit 8 | **Rank:** #8 | **Frequency Score:** 23 | **Coverage:** 22/26 (84.6%) | **Importance:** High
> **Coverage:** 6 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q082: One-way ANOVA on unique datasets (Hospitals, Salesmen, Wheat fertilizers, Schools, Cholesterol Diets, Processes, Glue drying). :id=q082

🔴 **Very High Priority** • **8 (80 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Jun 17 Q8 Hospitals ($F = 1.8822 < 3.89$, fail to reject); Jun 18 Q9 Salesmen ($F = 0.1327 < 4.26$, fail to reject); Dec 18 Q10 Wheat ($F = 5.6765 > 3.41$, reject $H_0$); 2019-I Q6 Schools ($F = 1.8000 < 4.26$, fail to reject); 2019-II (6384) Q7 Salesmen ($F = 1.1633 < 4.26$, fail to reject); Jun 21 Q7 Diets ($F = 1.7273 < 3.885$, fail to reject); Dec 21 Q7 Processes ($F = 2.6577 < 3.24$, fail to reject); Jun 26 Q8 Glue drying ($F = 24.9697 > 3.89$, reject $H_0$).

> **🗓️ Asked In Papers:** `Jun 2017 (Q8), Jun 2018 (Q9), Dec 2018 (Q10), 2019-I (Q6), Dec June 2019 (Q7), Jun 2021 (Q7), Dec 2021 (Q7), Jun 2026 (Q8)`

---

### Q083: One-way ANOVA: Test equality of means for $X_1, X_2, X_3$ ([13,11,16,22], [16,8,21,11], [15,12,25,10], $F_{2,9}(0.05) = 4.26$). :id=q083

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 12, k = 3, G = 180, CF = 2700, $SSB = 6.00$ ($MSB = 3.00$), $SSW = 300.00$ ($MSW = 33.33$), $F = 0.0900 < 4.26$ (fail to reject $H_0$; means equal).

> **🗓️ Asked In Papers:** `Dec 2015 (Q8), Jun 2016 (Q8), June 2020 (Q8), Dec 2025 (Q7)`

---

### Q084: One-way ANOVA: Compare 3 or 4 job methods A, B, C(, D) by completion times. :id=q084

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Dec 17 Q8 / Jun 23 Q9 (4 methods, N = 16, crit 5.95): $SSB = 70.25, SSW = 29.50, F = 9.5254 > 5.95$ (reject $H_0$). Jun 22 Q9 (3 methods, N = 12, crit 4.26): $SSB = 40.17, SSW = 24.50, F = 7.3776 > 4.26$ (reject $H_0$). Dec 24 Q7 (3 methods, n = 5, crit 3.885): $SSB = 2.533, SSW = 60.40, F = 0.2517 < 3.885$ (fail to reject).

> **🗓️ Asked In Papers:** `Dec 2017 (Q8), Jun 2022 (Q9), Jun 2023 (Q9), Dec 2024 (Q7)`

---

### Q085: Construct a Model ANOVA table for one-way classification. :id=q085

🟠 **High Priority** • **3 (30 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Columns for Source (Between Treatments, Within Treatments/Error, Total), Sum of Squares ($SSB, SSW, TSS$), Degrees of Freedom ($k-1, N-k, N-1$), Mean Square ($MSB = SSB/(k-1)$, $MSW = SSW/(N-k)$), and $F = MSB/MSW$.

> **🗓️ Asked In Papers:** `Jun 2014 (Q4), June 2020 (Q5), Jun 2025 (Q2)`

---

### Q086: Two-way ANOVA: Four catalysts (1–4) tested in three plants (A, B, C). Test catalyst significance at 5% ($F_{3,6} = 4.76$). :id=q086

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
N = 12, G = 26, CF = 56.3333, $TSS = 11.6667$, $SS_{\text{catalyst}} = 1.00$ (df = 3), $SS_{\text{plant}} = 0.1667$ (df = 2), $SS_{\text{error}} = 10.50$ (df = 6, $MS = 1.75$). $F_{\text{catalyst}} = 0.1905 < 4.76$ (not significant).

> **🗓️ Asked In Papers:** `Jun 2015 (Q7), Dec 2020 (Q8), Dec 2023 (Q9)`

---

### Q087: Expand ANOVA and briefly discuss its utility with suitable examples. :id=q087

⚪ **Low Priority** • **1 (10 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Analysis of Variance; compares 3 or more population means simultaneously by partitioning total variability into between-group and within-group components, preventing Type I error inflation from multiple pairwise $t$-tests (e.g., comparing crop yield across 4 fertilizers).

> **🗓️ Asked In Papers:** `Jun 2013 (Q4)`
