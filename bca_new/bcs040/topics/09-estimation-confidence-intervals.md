# 09. Estimation & Confidence Intervals

> **Syllabus Units:** Block 2 Unit 5 | **Rank:** #9 | **Frequency Score:** 15 | **Coverage:** 11/26 (42.3%) | **Importance:** Medium
> **Coverage:** 6 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q088: Find 95% or 99% Confidence Interval for a single population mean (and analyze sample size effect or population variance). :id=q088

🔴 **Very High Priority** • **5 (25 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Use $\bar{x} \pm Z_{\alpha/2}\cdot SE$. Jun 17 Q4(b) (n = 100, 99%): [287.10, 312.90]; Jun 18 Q6 (n = 10, $\bar{x} = 67$, SE = 0.8, 95%): [65.432, 68.568], $\sigma^2 = 10 \times 0.64 = 6.4$; Dec 18 Q5 (n = 64 vs. 256, 95%): [75.1, 84.9] (width 9.8 halves to 4.9 at n = 256); Dec 21 Q4 (n = 80, $\bar{x} = 50$, SD omitted in paper): state symbolic formula $50 \pm 1.96(s/\sqrt{80})$; Jun 22 Q1 (N = 200, n = 50, 95%): [72.228, 77.772] without FPC or [72.593, 77.407] with FPC.

> **🗓️ Asked In Papers:** `Jun 2017 (Q4(b)), Jun 2018 (Q6), Dec 2018 (Q5), Dec 2021 (Q4), Jun 2022 (Q1)`

---

### Q089: Explain the criteria / properties of a Good Estimator with examples. :id=q089

🟠 **High Priority** • **4 (20 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Unbiasedness ($E(\hat{\theta}) = \theta$, e.g., sample mean for $\mu$), Consistency ($\hat{\theta}_n \to \theta$ as $n \to \infty$), Efficiency (smallest variance among unbiased estimators, e.g., mean vs. median in normal populations), and Sufficiency (captures all sample information about $\theta$).

> **🗓️ Asked In Papers:** `Jun 2013 (Q7(c)), Dec June 2019 (Q6(a)), Dec 2022 (Q8(c)(ii)), Jun 2026 (Q10(iii))`

---

### Q090: Compute a point estimate of the mean length of life of 10 motors / bulbs (4.5, 5.0, 4.2, 4.8, 4.2, 5.1, 4.0, 4.2, 4.2, 4.5). :id=q090

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Point estimate $\hat{\mu} = \bar{x} = 44.7/10 = 4.47$ thousand hours (sample SD $s = 0.3802$).

> **🗓️ Asked In Papers:** `Dec 2017 (Q6(b)), Dec 2023 (Q1(a))`

---

### Q091: Obtain a 99% Confidence Interval for the difference of average life of two types of bulbs/machines ($n_A = 50, \bar{x}_A = 1300, s_A = 50$; $n_B = 60, \bar{x}_B = 1200, s_B = 60$; $Z_{0.005} = 2.58$). :id=q091

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$SE = \sqrt{50^2/50 + 60^2/60} = \sqrt{110} = 10.4881$; $99\% \text{ CI} = 100 \pm 2.58(10.4881) = [72.94, 127.06]$.

> **🗓️ Asked In Papers:** `Dec 2017 (Q5), Dec 2023 (Q6)`

---

### Q092: Differentiate between Estimator and Estimate with examples. :id=q092

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
An estimator is the general rule/formula (a random variable, e.g., $\bar{X} = \frac{1}{n}\sum X_i$); an estimate is the specific number calculated from an observed sample (e.g., $\bar{x} = 4.47$).

> **🗓️ Asked In Papers:** `Jun 2017 (Q4(a))`

---

### Q093: From 500 addresses, 100 are selected WOR and 25 wrong addresses are found. Identify the population, estimate total wrong addresses, and find standard error. :id=q093

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Population: all 500 addresses. Sample $p = 0.25 \Rightarrow$ Estimated total $\hat{Y} = 500 \times 0.25 = 125$; $SE(\hat{Y}) = 500\sqrt{0.8 \times \frac{0.25(0.75)}{99}} = 19.46$ (or $19.38$ using $N-1$ and $n$).

> **🗓️ Asked In Papers:** `Jun 2018 (Q4)`
