# 01. Sampling Techniques & Sampling Distributions

> **Syllabus Units:** Block 2 Unit 4 & Block 4 Units 12–14 | **Rank:** #1 | **Frequency Score:** 56 | **Coverage:** 23/26 (88.5%) | **Importance:** Very High
> **Coverage:** 13 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q001: List all possible WOR samples of size 2 or 3 from a small population, construct the sampling distribution of means, and verify that sample mean is an unbiased estimator of population mean. :id=q001

🔴 **Very High Priority** • **8 (80 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Verify $\mu_{\bar{x}} = \mu$ across $\binom{N}{n}$ samples: Jun 13 Q3 (N = 6, n = 2, 15 samples, $\mu = 51.00$); Dec 14 Q4 / Dec 25 Q3 (N = 5, n = 3, 10 samples, $\mu = 77.00$); Jun 17 Q5(b) (N = 5, n = 2, 10 samples); Dec 18 Q2 (N = 5, n = 3, 10 samples, $\mu = 6.40$); 2019-I Q4 (N = 5, n = 2, 10 samples, $\mu = 14.80$); Dec 22 Q5 (N = 4, n = 2, 6 samples, $\mu = 78.75$); Jun 24 Q2 (N = 4, n = 2, 6 samples, $\mu = 32.00$).

> **🗓️ Asked In Papers:** `Jun 2013 (Q3), Dec 2014 (Q4), Jun 2017 (Q5(b)), Dec 2018 (Q2), 2019-I (Q4), Dec 2022 (Q5), Jun 2024 (Q2), Dec 2025 (Q3)`

---

### Q002: Explain / Write a short note on Stratified Random Sampling. :id=q002

🔴 **Very High Priority** • **8 (40 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Divide a heterogeneous population into non-overlapping homogeneous strata ($N_1+\dots+N_k=N$) and draw independent SRS from each stratum. Improves representativeness and lowers sampling variance.

> **🗓️ Asked In Papers:** `Jun 2013 (Q9(b)), Jun 2018 (Q10(b)), Dec 2018 (Q4(c)), 2019-I (Q9(a)), Dec June 2019 (Q6(b)), Jun 2023 (Q10(b)), Jun 2024 (Q6(i)), Dec 2024 (Q10(a))`

---

### Q003: Determine stratum sample sizes using (i) Proportional Allocation and (ii) Neyman's Optimum Allocation. :id=q003

🔴 **Very High Priority** • **6 (60 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Apply $n_h = n\frac{N_h}{N}$ and $n_h = n\frac{N_h S_h}{\sum N_h S_h}$. Dec 15 Q10 (n = 100): Prop [20, 30, 30, 20], Neyman [13.33, 32.00, 28.00, 26.67]; Dec 17 Q10(b) / 2019-I Q9(b) / Jun 23 Q7 (n = 500): Prop [208.33, 125, 166.67], Neyman [272.73, 81.82, 145.45]; Dec 21 Q8 (n = 500): Prop [250, 50, 100, 100], Neyman [304.88, 24.39, 73.17, 97.56]; Jun 26 Q5 (n = 50): Prop [25.83, 24.17], Neyman [19.54, 30.46].

> **🗓️ Asked In Papers:** `Dec 2015 (Q10), Dec 2017 (Q10(b)), 2019-I (Q9(b)), Dec 2021 (Q8), Jun 2023 (Q7), Jun 2026 (Q5)`

---

### Q004: Compare and contrast Random Sampling with Non-Random Sampling, and briefly discuss methods for selecting a Simple Random Sample. :id=q004

🔴 **Very High Priority** • **6 (30 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Random sampling gives every unit a known non-zero selection probability (unbiased, allows error quantification), whereas non-random sampling relies on judgment or convenience (unquantifiable bias). SRS selection methods: Lottery method and Random Number Tables.

> **🗓️ Asked In Papers:** `Jun 2014 (Q9(a)), Jun 2016 (Q7(b)), Dec 2016 (Q7(c)), Jun 2017 (Q5(a)), Dec 2017 (Q10(a)), Jun 2025 (Q6)`

---

### Q005: Write a short note on Systematic Sampling (or differentiate SRS from Systematic Sampling). :id=q005

🔴 **Very High Priority** • **6 (30 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Explain interval $k = N/n$ and random start $r$. Contrast SRS (every unit drawn independently via random numbers) with Systematic Sampling (only 1st unit is random, remaining $n-1$ follow fixed interval $k$).

> **🗓️ Asked In Papers:** `Jun 2013 (Q9(c)), Dec 2018 (Q4(b)), Dec June 2019 (Q6(c)), Jun 2022 (Q4), Dec 2024 (Q6(b)), Jun 2026 (Q10(ii))`

---

### Q006: Define Simple Random Sampling (SRS), describe its limitations, and differentiate SRSWR from SRSWOR. :id=q006

🔴 **Very High Priority** • **5 (25 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
SRS assigns equal probability to all samples of size $n$. Limitations: needs an up-to-date frame, ignores stratification, high travel cost when dispersed. SRSWR allows repeat draws ($N^n$ samples, $\text{Var}(\bar{x}) = \sigma^2/n$); SRSWOR prohibits repeats ($\binom{N}{n}$ samples, finite population correction $\frac{N-n}{N-1}$ reduces variance).

> **🗓️ Asked In Papers:** `Dec 2015 (Q4), Jun 2016 (Q7(a)), Dec 2018 (Q4(a)), 2019-I (Q5(c)), Dec 2022 (Q8(a))`

---

### Q007: Discuss Systematic Sampling, differentiate between Linear and Circular systematic sampling, and give two advantages and limitations. :id=q007

🟠 **High Priority** • **4 (40 marks)** • *Theory, Long Answer*

**💡 Key Answer Points:**
Select random start $r$ and every $k$-th unit thereafter. Linear sets $k = \lfloor N/n \rfloor$ and stops at $N$ (unequal sample sizes when $N \ne nk$); Circular selects $r \in [1, N]$, sets $k = \text{round}(N/n)$, and wraps modulo $N$ (guaranteeing exact size $n$ and unbiased mean). Advantages: simple execution, even spread across ordered lists. Limitations: vulnerable to hidden periodicity, single-sample variance cannot be estimated unbiasedly.

> **🗓️ Asked In Papers:** `Jun 2014 (Q8(a)), Dec 2014 (Q7), June 2020 (Q10), Dec 2025 (Q5)`

---

### Q008: Select a systematic random sample of 7 units from 25 districts (or 10 units from 40 villages) and compute the sample mean. :id=q008

🟠 **High Priority** • **3 (30 marks)** • *Theory, Numerical, Long Answer*

**💡 Key Answer Points:**
Jun 21 Q2 / Jun 24 Q9 (N = 25, n = 7, k = 3, starting at r = 1): indices 1,4,7,10,13,16,19 yield [23, 37, 13, 58, 10, 17, 17], mean $= 25.00$. Dec 21 Q5 (N = 40, n = 10, k = 4, r = 1): [20, 55, 28, 24, 29, 16, 29, 31, 27, 26], mean $= 28.50$.

> **🗓️ Asked In Papers:** `Jun 2021 (Q2), Dec 2021 (Q5), Jun 2024 (Q9)`

---

### Q009: List the advantages and disadvantages of using a sampling approach instead of a census approach. :id=q009

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Advantages: lower cost, faster results, greater detail/scope, enables destructive testing, higher precision via trained enumerators. Disadvantages: sampling error, unsuitable if complete population records are required or population is tiny, selection bias if poorly designed.

> **🗓️ Asked In Papers:** `Jun 2013 (Q5), Jun 2022 (Q5), Dec 2024 (Q6(a))`

---

### Q010: Explain / Write a short note on Cluster Sampling. :id=q010

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Partition the population into natural heterogeneous groups (clusters), randomly sample a subset of clusters, and observe all units within selected clusters. Reduces listing/travel costs when no complete unit frame exists, though variance rises if intra-cluster homogeneity is high.

> **🗓️ Asked In Papers:** `Jun 2013 (Q9(a)), Jun 2018 (Q10(a)), Jun 2021 (Q10(ii))`

---

### Q011: A sample of size n = 50 is drawn from N = 200 observations with standard deviation 22. Find the standard error. :id=q011

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
With FPC ($n/N = 0.25 > 0.05$): $SE(\bar{x}) = \frac{22}{\sqrt{50}}\sqrt{\frac{200-50}{200-1}} = 2.7012$ (without FPC: $3.1113$).

> **🗓️ Asked In Papers:** `Jun 2014 (Q3), Jun 2025 (Q3)`

---

### Q012: List all possible samples of size 3 from 10 households using (a) Linear systematic and (b) Circular systematic sampling. :id=q012

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
(a) Linear (k = 3): {1,4,7,10}, {2,5,8}, {3,6,9}. (b) Circular (k = 3, r = 1–10 mod 10): {1,4,7}, {2,5,8}, {3,6,9}, {4,7,10}, {5,8,1}, {6,9,2}, {7,10,3}, {8,1,4}, {9,2,5}, {10,3,6}.

> **🗓️ Asked In Papers:** `Jun 2018 (Q2)`

---

### Q013: Differentiate between Neyman Allocation and Optimum Allocation. :id=q013

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Optimum Allocation accounts for varying per-unit stratum sampling costs $c_h$ ($n_h \propto \frac{N_h S_h}{\sqrt{c_h}}$) to minimize variance at fixed budget. Neyman Allocation assumes equal per-unit costs across strata ($c_h = c$), reducing to $n_h \propto N_h S_h$.

> **🗓️ Asked In Papers:** `Dec 2016 (Q7(a))`
