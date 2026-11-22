# 08. Analysis of Variance (ANOVA)

> **Syllabus Units:** Block 3 Unit 8 | **Rank:** #8 | **Frequency Score:** 23 | **Coverage:** 22/26 (84.6%) | **Importance:** High
> **Coverage:** 6 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q082: One-way ANOVA on unique datasets (Hospitals, Salesmen, Wheat fertilizers, Schools, Cholesterol Diets, Processes, Glue drying). :id=q082

🔴 **Very High Priority** • **8 (80 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (June 2026, Q8 — 10 Marks)
The three drying techniques for a glue were studied and the following times (in minutes) were observed:

| Observation | Technique A ($X_1$) | Technique B ($X_2$) | Technique C ($X_3$) |
| :---: | :---: | :---: | :---: |
| 1 | 13 | 10 | 5 |
| 2 | 10 | 11 | 4 |
| 3 | 8 | 14 | 4 |
| 4 | 11 | 14 | 5 |
| 5 | 8 | 15 | 6 |
| **Total ($T_j$)** | **$T_1 = 50$** | **$T_2 = 64$** | **$T_3 = 24$** |
| **Mean ($\bar{X}_j$)** | **10.0** | **12.8** | **4.8** |

*Hypothesis:* $H_0: \mu_1 = \mu_2 = \mu_3$ (treatment means are equal) vs. $H_1:$ at least two means differ. Given critical $F_{0.05}(2, 12) = 3.89$.

#### 🧮 Step-by-Step Computations:
1. **Summary Totals & Correction Factor ($CF$):**
   - $k = 3, n_1 = n_2 = n_3 = 5, N = 15$.
   - Grand Total $G = 50 + 64 + 24 = 138$.
   - $CF = \frac{G^2}{N} = \frac{138^2}{15} = \frac{19044}{15} = 1269.60$.
2. **Total Sum of Squares ($TSS$):**
   - $\sum \sum X^2 = (169+100+64+121+64) + (100+121+196+196+225) + (25+16+16+25+36) = 518 + 838 + 118 = 1474$.
   - $TSS = \sum \sum X^2 - CF = 1474 - 1269.60 = 204.40$.
3. **Between Treatments Sum of Squares ($SSB$):**
   - $SSB = \sum \frac{T_j^2}{n_j} - CF = \frac{50^2 + 64^2 + 24^2}{5} - 1269.60 = \frac{2500 + 4096 + 576}{5} - 1269.60 = 1434.40 - 1269.60 = 164.80$.
4. **Within Treatments / Error Sum of Squares ($SSW$):**
   - $SSW = TSS - SSB = 204.40 - 164.80 = 39.60$.

#### 📊 Completed ANOVA Summary Table:
| Source of Variation | Sum of Squares ($SS$) | Degrees of Freedom ($df$) | Mean Square ($MS$) | Variance Ratio ($F$) | Critical $F_{0.05}$ | Decision |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Between Treatments** | 164.80 | $k - 1 = 2$ | $MSB = \frac{164.80}{2} = 82.40$ | $\frac{82.40}{3.30} = \mathbf{24.97}$ | $F(2, 12) = 3.89$ | **Reject $H_0$** ($24.97 > 3.89$) |
| **Within / Error** | 39.60 | $N - k = 12$ | $MSW = \frac{39.60}{12} = 3.30$ | — | — | Average times differ significantly |
| **Total** | 204.40 | $N - 1 = 14$ | — | — | — | — |

#### 🔄 Cross-Session Variations & Decisions:
| Exam Session | Domain / Treatments | Sample Size ($N$) | Calculated $F$ | Critical $F$ | Conclusion |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Jun 2017 (Q8)** | 3 Hospitals | $N = 15$ | $F = 1.882$ | $F(2,12) = 3.89$ | Fail to reject $H_0$ |
| **Jun 2018 (Q9)** | 3 Salesmen | $N = 12$ | $F = 0.133$ | $F(2,9) = 4.26$ | Fail to reject $H_0$ |
| **Dec 2018 (Q10)**| 4 Wheat Fertilizers | $N = 16$ | $F = 5.677$ | $F(3,12) = 3.41$ | **Reject $H_0$** |
| **2019-I (Q6)** | 3 Schools | $N = 12$ | $F = 1.800$ | $F(2,9) = 4.26$ | Fail to reject $H_0$ |
| **Dec 2019 (Q7)** | 3 Salesmen | $N = 12$ | $F = 1.163$ | $F(2,9) = 4.26$ | Fail to reject $H_0$ |
| **Jun 2021 (Q7)** | 3 Diets (Cholesterol)| $N = 15$ | $F = 1.727$ | $F(2,12) = 3.885$ | Fail to reject $H_0$ |
| **Dec 2021 (Q7)** | 3 Industrial Processes | $N = 18$ | $F = 2.658$ | $F(2,15) = 3.24$ | Fail to reject $H_0$ |
| **Jun 2026 (Q8)** | 3 Glue Drying Techniques | $N = 15$ | $F = 24.970$ | $F(2,12) = 3.89$ | **Reject $H_0$** |

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
