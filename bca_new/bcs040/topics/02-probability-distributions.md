# 02. Probability & Probability Distributions

> **Syllabus Units:** Block 1 Units 2–3 | **Rank:** #2 | **Frequency Score:** 48 | **Coverage:** 25/26 (96.2%) | **Importance:** Very High
> **Coverage:** 21 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q014: Describe "Probability Distribution" with a suitable example. How does the Binomial distribution differ from the Poisson distribution? :id=q014

🟠 **High Priority** • **4 (20 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
A probability distribution specifies all possible values of an RV and their probabilities ($\sum p(x)=1$ or $\int f(x)dx=1$; e.g., heads in two coin tosses). Binomial vs. Poisson: Binomial uses fixed finite trials $n$ and non-negligible $p$ with $\text{mean } np > \text{variance } npq$; Poisson models rare events ($n \to \infty, p \to 0, \lambda = np$ finite) with single parameter $\lambda$ where $\text{mean} = \text{variance} = \lambda$.

> **🗓️ Asked In Papers:** `Jun 2014 (Q1), Dec 2020 (Q5(ii)), Jun 2025 (Q1), Dec 2025 (Q1)`

---

### Q015: Suppose 2% of factory items are defective. Find the probability of (i) 3 defectives in a sample of 100, and (ii) no defectives in a sample of 50. :id=q015

🟠 **High Priority** • **4 (20 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Poisson approximation ($p = 0.02, n \ge 50$): (i) $\lambda = 2 \Rightarrow P(X=3) = \frac{e^{-2}2^3}{6} = 0.1804$ (exact Binomial: $0.1823$); (ii) $\lambda = 1 \Rightarrow P(X=0) = e^{-1} = 0.3679$ (exact Binomial: $0.3642$).

> **🗓️ Asked In Papers:** `Jun 2015 (Q2), Dec 2016 (Q4), Dec 2020 (Q3), Jun 2023 (Q3)`

---

### Q016: Binomial distribution word problems (Meena late, ice factory cold, oil drilling holes, occupational disease). :id=q016

🟠 **High Priority** • **4 (20 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Apply $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$. Dec 15 Q6 (Meena late, n = 6, p = 0.2): $P(X=2) = 0.2458, P(X \ge 1) = 1 - 0.8^6 = 0.7379$; Jun 17 Q2 (cold, n = 5, p = 0.25): $P(X \ge 4) = 1/64 = 0.0156$; 2019-I Q3 (oil holes, n = 4, p = 0.2): $P(X \ge 2) = 113/625 = 0.1808$; Jun 21 Q4 (disease, n = 6, p = 0.2): $P(X \ge 4) = 0.0170, P(X=3) = 0.0819$.

> **🗓️ Asked In Papers:** `Dec 2015 (Q6), Jun 2017 (Q2), 2019-I (Q3), Jun 2021 (Q4)`

---

### Q017: Bayes' Theorem (Police radar traps): Traps at $L_1, L_2, L_3, L_4$ operate 40%, 30%, 20%, and 30% (10% in Jun 18) of the time; passing probabilities are 0.2, 0.1, 0.5, 0.2. Find $P(\text{ticket})$ and $P(L_i \mid \text{ticket})$. :id=q017

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Jun 15 Q10 & Dec 23 Q7 (L4 = 30%): $P(T) = 0.08 + 0.03 + 0.10 + 0.06 = 0.27$; posteriors $L_1 = 8/27 (0.2963), L_2 = 3/27 (0.1111), L_3 = 10/27 (0.3704), L_4 = 6/27 (0.2222)$. Jun 18 Q7(a) (L4 = 10%): $P(T) = 0.23$; $P(L_1 \mid T) = 0.08/0.23 = 0.3478$.

> **🗓️ Asked In Papers:** `Jun 2015 (Q10), Jun 2018 (Q7(a)), Dec 2023 (Q7)`

---

### Q018: Write a short note on Binomial distribution / Write its PMF and find the probability of hitting a target twice in 5 independent shots ($p = 1/5$). :id=q018

🟠 **High Priority** • **3 (15 marks)** • *Theory, Numerical, Short Answer*

**💡 Key Answer Points:**
PMF $P(X=x) = \binom{n}{x}p^x(1-p)^{n-x}$ ($x = 0,1,\dots,n$); Mean $= np$, Var $= npq$. Numerical (n = 5, p = 0.2, x = 2): $P(X=2) = \binom{5}{2}(0.2)^2(0.8)^3 = 10(0.04)(0.512) = 0.2048$.

> **🗓️ Asked In Papers:** `June 2020 (Q6(ii)), Dec 2024 (Q3), Jun 2026 (Q6(ii))`

---

### Q019: Suppose $A$ and $B$ are two independent events. Given $P(A \cup B)$ and either $P(A \cap B')$ or $P(A)$, determine $P(B)$. :id=q019

🟠 **High Priority** • **3 (15 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Jun 14 Q2 / Dec 20 Q2 ($P(A \cup B) = 0.6, P(A \cap B') = 0.4$): $P(B) = 0.6 - 0.4 = 0.2$ (yielding $P(A) = 0.5, P(A \cap B) = 0.1$). Jun 16 Q3(b) ($P(A \cup B) = 0.8, P(A) = 0.5$): $0.8 = 0.5 + P(B) - 0.5P(B) \Rightarrow P(B) = 0.6$.

> **🗓️ Asked In Papers:** `Jun 2014 (Q2), Jun 2016 (Q3(b)), Dec 2020 (Q2)`

---

### Q020: State (and prove) the Addition Theorem / Additive Law of Probability, and solve a union numerical (300 hospital patients or Rahul/Meena passing BCS-040). :id=q020

🟠 **High Priority** • **3 (15 marks)** • *Theory, Numerical, Short Answer*

**💡 Key Answer Points:**
Law: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, proven by partitioning $A \cup B$ into disjoint events $A$ and $B \cap A'$. Jun 24 Q3 (300 patients: 15 COVID, 13 typhoid, 3 both): $(15+13-3)/300 = 25/300 = 1/12 \approx 0.0833$. Dec 24 Q2 (Rahul 2/5, Meena 1/3, independent): $2/5 + 1/3 - 2/15 = 9/15 = 3/5 = 0.60$.

> **🗓️ Asked In Papers:** `Jun 2016 (Q3(a)), Jun 2024 (Q3), Dec 2024 (Q2)`

---

### Q021: Box A (or X) contains 5 red and 4 blue balls; Box B (or Y) contains 2 red and 5 blue balls. One ball is drawn from each box; find the probability that one is red and one is blue. :id=q021

🟠 **High Priority** • **3 (15 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$P(R_A B_B) + P(B_A R_B) = (5/9)(5/7) + (4/9)(2/7) = 33/63 = 11/21 \approx 0.5238$.

> **🗓️ Asked In Papers:** `Dec 2016 (Q3), Dec 2018 (Q6), Dec 2022 (Q4)`

---

### Q022: Independent attempts to hit a target or solve a statistics problem by 2 or 3 individuals. :id=q022

🟠 **High Priority** • **3 (15 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Use complement $1 - P(\text{none succeeds})$. 2019-I Q2 (4/5, 2/3): $1 - (1/5)(1/3) = 14/15 \approx 0.9333$. 2019-II (6384) Q3 (0.3, 0.5, 0.6): $1 - (0.7)(0.5)(0.4) = 0.86$. Dec 22 Q2 (1/2, 1/3, 1/4): (i) $P(\text{solved}) = 1 - (1/2)(2/3)(3/4) = 3/4 = 0.75$; (ii) $P(\text{only one}) = (1/2)(2/3)(3/4) + (1/2)(1/3)(3/4) + (1/2)(2/3)(1/4) = 11/24 \approx 0.4583$.

> **🗓️ Asked In Papers:** `2019-I (Q2), Dec June 2019 (Q3), Dec 2022 (Q2)`

---

### Q023: Define Random Experiment and Random Variable. Briefly discuss the types of Random Variables with suitable examples. :id=q023

🟡 **Medium Priority** • **2 (10 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
A random experiment has well-defined outcomes whose exact result on any trial is uncertain (e.g., rolling a die). A random variable (RV) maps sample space outcomes to real numbers: Discrete RVs take countable values (e.g., defective items in a batch), whereas Continuous RVs take uncountable values over intervals (e.g., waiting time or bulb lifetime).

> **🗓️ Asked In Papers:** `Jun 2013 (Q1), Jun 2016 (Q4(a))`

---

### Q024: The probability that at least one of two independent events occurs is 0.5; $P(\text{only } A) = 3/25$; $P(\text{only } B) = 8/25$. Find the probability that none occurs. :id=q024

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$P(\text{none}) = 1 - P(A \cup B) = 1 - 0.5 = 0.5$ (and $P(A \cap B) = 0.5 - 0.12 - 0.32 = 0.06$).

> **🗓️ Asked In Papers:** `Jun 2013 (Q2), Dec 2014 (Q2)`

---

### Q025: Compute simple union probability $P(A \cup B)$ from given percentages (breast cancer/smokers or defective keyboard/mouse). :id=q025

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Dec 21 Q2 (5% cancer, 15% smoker, 3% both): $0.05 + 0.15 - 0.03 = 0.17$. Jun 26 Q2 (5% keyboard, 12% mouse, 4% both): $0.05 + 0.12 - 0.04 = 0.13$.

> **🗓️ Asked In Papers:** `Dec 2021 (Q2), Jun 2026 (Q2)`

---

### Q026: A bag contains 10 white and 3 black balls. Balls are drawn one by one without replacement until all black balls are drawn. Find the probability the procedure ends at the 6th draw. :id=q026

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
First 5 draws must yield 3 white and 2 black balls, and the 6th draw must be the 3rd black ball: $\frac{\binom{10}{3}\binom{3}{2}}{\binom{13}{5}} \times \frac{1}{8} = \frac{5}{143} \approx 0.0350$.

> **🗓️ Asked In Papers:** `Jun 2016 (Q4(b)), Jun 2018 (Q3)`

---

### Q027: Bayes' Theorem (Insured drivers): 1000 scooter (or truck), 3000 car, 6000 truck (or scooter) drivers insured; accident probabilities 0.2, 0.04, 0.25. Given an accident, find probability the driver is a car driver. :id=q027

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Priors $0.1, 0.3, 0.6$; total accident probability $= 0.1(0.2) + 0.3(0.04) + 0.6(0.25) = 0.182$; $P(\text{Car} \mid \text{Acc}) = 0.012/0.182 = 6/91 \approx 0.0659$.

> **🗓️ Asked In Papers:** `Dec 2017 (Q3), Dec 2023 (Q2)`

---

### Q028: Switchboard calls occur at an average rate of 6 calls per 10 minutes. Find the probability of exactly 2 calls during a 5-minute break. :id=q028

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Poisson with $\lambda = 6 \times (5/10) = 3$ calls per 5 min; $P(X=2) = \frac{e^{-3}3^2}{2!} = 0.2240$.

> **🗓️ Asked In Papers:** `Dec 2014 (Q3), June 2020 (Q3)`

---

### Q029: Write a short note on Poisson distribution. :id=q029

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Discrete distribution for rare-event counts over fixed time/space intervals; PMF $P(X=x) = \frac{e^{-\lambda}\lambda^x}{x!}$ ($x = 0,1,2,\dots$); Mean = Variance = $\lambda$; limiting case of Binomial when $n \to \infty, p \to 0, np = \lambda$.

> **🗓️ Asked In Papers:** `Jun 2024 (Q10(iii))`

---

### Q030: Divisions A and B have 20 students each; one student is selected from each (or 2 out of 40). Find the probability that Rahul in Division A is selected. :id=q030

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$P(\text{Rahul}) = 1/20 = 0.05$ (likewise, selecting 2 out of 40 gives $2/40 = 0.05$).

> **🗓️ Asked In Papers:** `Dec 2015 (Q2)`

---

### Q031: Bayes' Theorem (Clinical test): Cancer is present in 22% of a population; test is positive with probability 0.70 if present and 0.05 if absent. Given a positive test, find probability the person has cancer. :id=q031

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$P(C \mid +) = \frac{0.22 \times 0.70}{(0.22 \times 0.70) + (0.78 \times 0.05)} = \frac{0.154}{0.193} \approx 0.7979$.

> **🗓️ Asked In Papers:** `Dec 2015 (Q5)`

---

### Q032: Given a discrete PMF table ($X$: 0–5; $p(x)$: $0, C, C, 2C, 3C, C$), find $C$ and $P(X \le 3)$. :id=q032

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\sum p(x) = 8C = 1 \Rightarrow C = 1/8 = 0.125$; $P(X \le 3) = 4C = 0.50$.

> **🗓️ Asked In Papers:** `Dec June 2019 (Q4)`

---

### Q033: Oil filling machine follows $N(\mu = 952, \sigma = 4)$. Find $P(952 \le X \le 956)$ given $P(0 \le Z \le 1) = 0.3413$. :id=q033

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Standardize $Z_1 = (952-952)/4 = 0$ and $Z_2 = (956-952)/4 = 1$, giving $P(0 \le Z \le 1) = 0.3413$.

> **🗓️ Asked In Papers:** `Dec June 2019 (Q5)`

---

### Q034: Let $x_1, x_2$ be independent RVs with $\text{Var}(x_1) = k$ and $\text{Var}(x_2) = 2$. If $\text{Var}(3x_2 - x_1) = 25$, find $k$. :id=q034

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\text{Var}(3x_2 - x_1) = 9\text{Var}(x_2) + \text{Var}(x_1) = 18 + k = 25 \Rightarrow k = 7$.

> **🗓️ Asked In Papers:** `Jun 2016 (Q2)`
