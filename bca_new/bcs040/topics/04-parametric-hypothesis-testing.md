# 04. Parametric Hypothesis Testing

> **Syllabus Units:** Block 2 Unit 6 | **Rank:** #4 | **Frequency Score:** 32 | **Coverage:** 23/26 (88.5%) | **Importance:** Very High
> **Coverage:** 12 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q045: One-sample $t$-test for Mean (advertisement campaign sales, tyre life, male height). :id=q045

🔴 **Very High Priority** • **6 (30 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Jun 15 Q5 / Dec 20 Q4 / Jun 23 Q5 (n = 22): $t = \frac{153.7 - 146.3}{17.2/\sqrt{22}} = 2.0180$ ($< 2.08$ two-tailed supplied, $> 1.721$ one-tailed). Jun 24 Q4 (n = 16): $t = 1.6000 < 1.753$ (fail to reject). Jun 22 Q7(b) (tyres, n = 16): $t = 1.6000 < 1.75$ (fail to reject). Dec 18 Q3 (height, n = 10, s = 3.1623): $t = 2.0000$ ($< 2.26$ supplied two-tailed).

**📝 Example PQP Question (Jun 2024 Q4):**

The mean weekly sales of chocolate packets in different departmental stores was 146 packets per store. After an advertisement campaign the mean weekly sales of 16 stores for a typical week was 150 and showed a standard deviation of 10. Was the advertisement campaign successful at 5% level of significance? (Given $t(15), 0.05 = 1.753$). *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q5)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2018 (Q3)](/bca_new/bcs040/pqp/BCS-040_Dec_2018.pdf ':ignore'), [Dec 2020 (Q4)](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore'), [Jun 2022 (Q7(b))](/bca_new/bcs040/pqp/BCS-040_June_2022.pdf ':ignore'), [Jun 2023 (Q5)](/bca_new/bcs040/pqp/BCS-040_June_2023.pdf ':ignore'), [Jun 2024 (Q4)](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')

---

### Q046: Explain / Write a short note on the $t$-test for Mean. :id=q046

🔴 **Very High Priority** • **5 (25 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests $H_0: \mu = \mu_0$ for small normal samples ($n < 30$, unknown $\sigma$) via $t = \frac{\bar{x}-\mu_0}{s/\sqrt{n}} \sim t_{n-1}$, rejecting $H_0$ when $|t| > t_{\alpha/2, n-1}$ (two-tailed) or $t > t_{\alpha, n-1}$ (one-tailed).

**📝 Example PQP Question (Jun 2026 Q6(i)):**

Write short notes on the following:
(i) $t$-test *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q5(a))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [June 2020 (Q6(iii))](/bca_new/bcs040/pqp/BCS-040_June_2020.pdf ':ignore'), [Dec 2022 (Q8(c)(i))](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore'), [Dec 2024 (Q10(c))](/bca_new/bcs040/pqp/BCS-040_Dec_2024.pdf ':ignore'), [Jun 2026 (Q6(i))](/bca_new/bcs040/pqp/BCS-040_June_2026.pdf ':ignore')

---

### Q047: Describe the Paired $t$-test (test about the mean for paired values). :id=q047

🟠 **High Priority** • **4 (20 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Evaluates before/after measurements on the same subjects using differences $d_i = y_i - x_i$. Test $H_0: \mu_d = 0$ via $t = \frac{\bar{d}}{s_d/\sqrt{n}} \sim t_{n-1}$.

**📝 Example PQP Question (Jun 2025 Q7(a)):**

Describe the following tests in detail:
(a) Paired $t$-test *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2014 (Q5(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [Jun 2016 (Q6(a))](/bca_new/bcs040/pqp/BCS-040_June_2016.pdf ':ignore'), [2019-I (Q5(b))](/bca_new/bcs040/pqp/BCS-040_June_2019.pdf ':ignore'), [Jun 2025 (Q7(a))](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore')

---

### Q048: Differentiate between Parametric and Non-Parametric tests. :id=q048

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Parametric tests ($Z, t, F$, ANOVA) assume specific population distributions (normality), require metric data, and test parameters with higher power. Non-parametric tests (Chi-square, Sign, Mann-Whitney) are distribution-free, handle categorical/ordinal data, and resist outliers.

**📝 Example PQP Question (Dec 2023 Q1(b)):**

Compare parametric and non-parametric tests. *(2 marks)*

> **🗓️ Asked In Papers:** [Dec 2017 (Q6(a))](/bca_new/bcs040/pqp/BCS-040_Dec_2017.pdf ':ignore'), [Dec 2020 (Q5(i))](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore'), [Dec 2023 (Q1(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2023.pdf ':ignore')

---

### Q049: Write a short note on / Describe the $F$-test for equality of two variances. :id=q049

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Tests $H_0: \sigma_1^2 = \sigma_2^2$ across two independent normal samples using $F = s_1^2 / s_2^2$ (larger variance in numerator) with $df = (n_1-1, n_2-1)$.

**📝 Example PQP Question (Dec 2025 Q6(a)):**

Write short notes on the following:
(a) $F$-test for equality of two variances *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q5(b))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Dec 2016 (Q6(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [Dec 2025 (Q6(a))](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q050: Paired $t$-test numerical: Pulse rates of 6 people before and after taking a new drug. :id=q050

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
2019-II (6384) Q9 (After 3rd = 81): $d = [3,-1,-3,4,6,6], \bar{d} = 2.50, s_d = 3.7283, t = 1.6425 < 2.015$ (fail to reject at 5%). Dec 21 Q3 (After 3rd = 82): $d = [3,-1,-2,4,6,6], \bar{d} = 2.6667, s_d = 3.4448, t = 1.8962 < 4.032$ (fail to reject at 1%).

**📝 Example PQP Question (Dec 2021 Q3):**

The pulse rate of 6 people was recorded before and after taking a new drug, which are given below:

| Pulse Rate | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Before Drug | 68 | 71 | 84 | 93 | 67 | 74 |
| After Drug | 71 | 70 | 82 | 97 | 73 | 80 |

On the basis of the above information, can you conclude that there is a significant effect of the new drug to increase the pulse rate at 1% level of significance? [Given that $t_5(0.01) = 4.032$] *(5 marks)*

> **🗓️ Asked In Papers:** [Dec June 2019 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2019.pdf ':ignore'), [Dec 2021 (Q3)](/bca_new/bcs040/pqp/BCS-040_Dec_2021.pdf ':ignore')

---

### Q051: Differentiate between Z-test and t-test. :id=q051

🟡 **Medium Priority** • **2 (10 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Z-test uses the standard normal distribution when $\sigma$ is known or $n \ge 30$; t-test uses Student's $t$-distribution ($df = n - 1$) when $n < 30$ and $\sigma$ is unknown (estimated via $s$), featuring heavier tails.

**📝 Example PQP Question (Dec 2025 Q10(a)):**

Differentiate between the following:
(a) $Z$-test and $t$-test *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q8(b))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Dec 2025 (Q10(a))](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q052: One-sample $Z$-test for Mean (medical labs price > 100, n = 64; CFL bulb life = 1600, n = 100). :id=q052

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Jun 16 Q5: $Z = (120-100)/(60/8) = 2.6667 > 1.645$ (reject $H_0$). Jun 21 Q3: $Z = (1570-1600)/(120/10) = -2.5000$, $|Z| = 2.50 > 1.96$ (reject $H_0$).

**📝 Example PQP Question (Jun 2021 Q3):**

A shopkeeper claims that the average life of a CFL Bulb is 1600 hours. To check this claim, a researcher takes a sample of 100 CFL bulbs of the same make randomly and finds mean lifetime of 1570 hours with standard deviation of 120 hours. Is the claim acceptable at 5% level of significance? [Given that $Z = \pm 1.96$] *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2016 (Q5)](/bca_new/bcs040/pqp/BCS-040_June_2016.pdf ':ignore'), [Jun 2021 (Q3)](/bca_new/bcs040/pqp/BCS-040_June_2021.pdf ':ignore')

---

### Q053: Two-sample $Z$-test for proportions: 130 of 300 men and 90 of 300 women use seat belts. Test for significant difference at 5% ($Z_{0.025} = 1.96$). :id=q053

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$p_1 = 0.4333, p_2 = 0.3000$, pooled $\hat{p} = 0.3667, SE = 0.03935, Z = 3.3887 > 1.96$ (reject $H_0$; significant difference exists).

**📝 Example PQP Question (Dec 2023 Q5):**

In order to test whether there is any significant difference between the proportion of safety consciousness of men and women, while driving a car, a study was conducted. The study includes a sample of 300 men and 300 women. Out of 300 men, 130 said that they used seat belts, and out of 300 women, 90 said that they used seat belts. Based on the given data, test the claim that there is no significant difference between the proportion of safety consciousness of men and women, while driving a car at 5% level of significance. (Given that $Z_{0.025} = 1.96$). *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2017 (Q4)](/bca_new/bcs040/pqp/BCS-040_Dec_2017.pdf ':ignore'), [Dec 2023 (Q5)](/bca_new/bcs040/pqp/BCS-040_Dec_2023.pdf ':ignore')

---

### Q054: Differentiate between One-Sample Test and Two-Sample Test. :id=q054

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
A one-sample test compares one sample statistic against a known/hypothesized constant ($\mu_0$ or $p_0$); a two-sample test compares two samples (independent or paired) to evaluate parameter differences ($\mu_1 - \mu_2$ or $p_1 - p_2$).

**📝 Example PQP Question (Jun 2016 Q7(c)):**

Differentiate between any two of the following:
(c) One-Sample Test and Two-Sample Test *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2016 (Q7(c))](/bca_new/bcs040/pqp/BCS-040_June_2016.pdf ':ignore')

---

### Q055: Explain Z-test for Mean. :id=q055

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Large-sample ($n \ge 30$) or known-$\sigma$ test for $H_0: \mu = \mu_0$ using $Z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$, comparing against $\pm 1.96$ (two-tailed 5%) or $1.645$ (one-tailed 5%).

**📝 Example PQP Question (2019-I Q5(a)):**

Write short notes on any two of the following:
(a) $z$-test for mean *(5 marks)*

> **🗓️ Asked In Papers:** [2019-I (Q5(a))](/bca_new/bcs040/pqp/BCS-040_June_2019.pdf ':ignore')

---

### Q056: One-sample $Z$-test for Proportion: Chip manufacturer claims at most 2% defectives; 8 defectives in n = 250 ($Z_{0.05} = 1.645$). :id=q056

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\hat{p} = 0.032, SE = \sqrt{0.02(0.98)/250} = 0.008854, Z = (0.032-0.02)/0.008854 = 1.3553 < 1.645$ (fail to reject $H_0$; claim not disproved).

**📝 Example PQP Question (Jun 2017 Q6):**

A computer chip manufacturer claims that at most 2% of the chips it produces are defective. To check the claim of the manufacturer, a researcher selects a sample of 250 of these chips. If there are eight defective chips among these 250, test the null hypothesis that more than 2% of the chips are defective at 5% level of significance. Does this disprove the manufacturer's claim? (Given that $Z_{0.05} = 1.645$) *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2017 (Q6)](/bca_new/bcs040/pqp/BCS-040_June_2017.pdf ':ignore')
