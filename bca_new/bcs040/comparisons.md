# ⚖️ High-Frequency Statistical Comparisons (BCS-040)

> **Exam Relevance:** Direct comparative analysis is one of IGNOU's most consistent question formats. Examiners systematically award 5 to 10 marks for well-structured difference tables featuring clear comparison parameters, mathematical formulas, underlying assumptions, and practical examples.

---

## 🧭 Master Comparison Index

| Pair # | Comparison Subject | Primary Syllabus Module | Key Distinction | Question Link |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **Parametric Tests vs. Non-Parametric Tests** | [04. Parametric Hypothesis Testing](/bca_new/bcs040/topics/04-parametric-hypothesis-testing.md) | Distributional assumptions & data scale | [**Q046**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q046) |
| **02** | **Correlation vs. Regression** | [05. Correlation & Regression Analysis](/bca_new/bcs040/topics/05-correlation-regression.md) | Degree of association vs. causal prediction | [**Q058**](/bca_new/bcs040/topics/05-correlation-regression?id=q058) |
| **03** | **Binomial Distribution vs. Poisson Distribution** | [02. Probability Distributions](/bca_new/bcs040/topics/02-probability-distributions.md) | Fixed finite trials vs. continuous-interval rare events | [**Q016**](/bca_new/bcs040/topics/02-probability-distributions?id=q016) |
| **04** | **One-Way ANOVA vs. Two-Way ANOVA** | [08. Analysis of Variance (ANOVA)](/bca_new/bcs040/topics/08-anova.md) | Single factor vs. two simultaneous factors | [**Q084**](/bca_new/bcs040/topics/08-anova?id=q084) |
| **05** | **Stratified Sampling vs. Cluster Sampling** | [01. Sampling Distributions](/bca_new/bcs040/topics/01-sampling-distributions.md) | Homogeneous strata vs. heterogeneous clusters | [**Q006**](/bca_new/bcs040/topics/01-sampling-distributions?id=q006) |
| **06** | **Point Estimation vs. Interval Estimation** | [09. Estimation & Confidence Intervals](/bca_new/bcs040/topics/09-estimation-confidence-intervals.md) | Single best value vs. range with confidence level | [**Q089**](/bca_new/bcs040/topics/09-estimation-confidence-intervals?id=q089) |
| **07** | **Chance Causes vs. Assignable Causes in SQC** | [10. Statistical Quality Control](/bca_new/bcs040/topics/10-statistical-quality-control.md) | Inherent natural noise vs. identifiable defects | [**Q096**](/bca_new/bcs040/topics/10-statistical-quality-control?id=q096) |
| **08** | **Type I Error ($\alpha$) vs. Type II Error ($\beta$)** | [04. Parametric Hypothesis Testing](/bca_new/bcs040/topics/04-parametric-hypothesis-testing.md) | False positive (reject true $H_0$) vs. false negative | [**Q048**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q048) |
| **09** | **Mean vs. Median** | [06. Descriptive Statistics](/bca_new/bcs040/topics/06-descriptive-statistics.md) | Algebraic center (outlier-sensitive) vs. positional center | [**Q068**](/bca_new/bcs040/topics/06-descriptive-statistics?id=q068) |
| **10** | **Additive vs. Multiplicative Time Series Models** | [07. Time Series Forecasting](/bca_new/bcs040/topics/07-time-series-forecasting.md) | Absolute component sum vs. percentage proportions | [**Q077**](/bca_new/bcs040/topics/07-time-series-forecasting?id=q077) |
| **11** | **Variables Control Charts vs. Attributes Control Charts** | [10. Statistical Quality Control](/bca_new/bcs040/topics/10-statistical-quality-control.md) | Continuous dimensions ($\bar{X}, R$) vs. defect counts ($p, np$) | [**Q095**](/bca_new/bcs040/topics/10-statistical-quality-control?id=q095) |
| **12** | **Linear Systematic Sampling vs. Circular Systematic** | [01. Sampling Distributions](/bca_new/bcs040/topics/01-sampling-distributions.md) | $N = nk$ integer requirement vs. cyclic rounding | [**Q007**](/bca_new/bcs040/topics/01-sampling-distributions?id=q007) |
| **13** | **Sampling with Replacement (SWR) vs. Without (SWOR)** | [01. Sampling Distributions](/bca_new/bcs040/topics/01-sampling-distributions.md) | Independence maintained vs. variance reduced by FPC | [**Q004**](/bca_new/bcs040/topics/01-sampling-distributions?id=q004) |
| **14** | **Null Hypothesis ($H_0$) vs. Alternative Hypothesis ($H_1$)** | [04. Parametric Hypothesis Testing](/bca_new/bcs040/topics/04-parametric-hypothesis-testing.md) | Claim of no effect / equality vs. research assertion | [**Q047**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q047) |

---

## 📝 Canonical Comparison Guides

### ⚖️ 1. Parametric Tests vs. Non-Parametric Tests

[**Q046**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q046) • **Asked 4 times (20 marks)** • *Recent: Dec 2024 Q5(a), June 2022 Q5(a)*

| Parameter | Parametric Tests | Non-Parametric (Distribution-Free) Tests |
| :--- | :--- | :--- |
| **Distributional Assumption** | Assumes the underlying population follows a specific distribution (usually Normal). | Makes no assumptions regarding population distribution shape. |
| **Measurement Scale** | Quantitative interval or ratio scale data (continuous metrics). | Nominal (categorical) or ordinal (ranked) scale data. |
| **Parameters Tested** | Tests specific population parameters (Mean $\mu$, Variance $\sigma^2$, Proportion $p$). | Tests medians, distributions, independence, or rankings. |
| **Statistical Power** | Higher statistical power when distributional assumptions are satisfied. | Slightly lower statistical power; requires larger sample sizes. |
| **Sample Size Dependency** | Large samples preferred, or small samples strictly requiring normality. | Robust and reliable even for very small samples ($n < 30$). |
| **Standard Examples** | $Z$-test, Student's $t$-test, Paired $t$-test, $F$-test, ANOVA. | Chi-Square ($\chi^2$) test, Mann-Whitney $U$, Wilcoxon Signed-Rank. |

---

### ⚖️ 2. Correlation vs. Regression

[**Q058**](/bca_new/bcs040/topics/05-correlation-regression?id=q058) • **Asked 4 times (20 marks)** • *Recent: Dec 2024 Q4(a), June 2023 Q3(a)*

| Comparison Parameter | Correlation Analysis ($r$) | Regression Analysis ($Y = a + bX$) |
| :--- | :--- | :--- |
| **Fundamental Objective** | Measures the strength and direction of linear association between two variables. | Models the functional/mathematical relationship to predict one variable from another. |
| **Variable Symmetry** | Completely symmetric: $r_{xy} = r_{yx}$. Neither variable is dependent or independent. | Asymmetric: $Y$ on $X$ is distinct from $X$ on $Y$ ($b_{yx} \ne b_{xy}$ in general). |
| **Cause and Effect** | Does not imply causation (correlation does not mean causation). | Assumes a directional cause-and-effect relationship (independent $\to$ dependent). |
| **Units of Measurement** | Dimensionless pure number bounded strictly in $[-1, +1]$. | Expressed in physical measurement units of the dependent variable. |
| **Mathematical Property** | $r = \pm \sqrt{b_{yx} \cdot b_{xy}}$. Shares the same sign as regression slopes. | Regression lines intersect at the point of means $(\bar{x}, \bar{y})$. |

---

### ⚖️ 3. Binomial Distribution vs. Poisson Distribution

[**Q016**](/bca_new/bcs040/topics/02-probability-distributions?id=q016) • **Asked 4 times (20 marks)** • *Recent: Dec 2025 Q1, June 2025 Q1*

| Feature | Binomial Distribution | Poisson Distribution |
| :--- | :--- | :--- |
| **Nature of Trials** | Fixed finite number of trials $n$. | Infinite/unbounded trials over a continuous interval of time or space. |
| **Probability of Success ($p$)** | Constant and non-negligible ($p$ is moderate, e.g., $0.1$ to $0.9$). | Very small / rare event ($p \to 0$ as $n \to \infty$). |
| **Parameters** | Two parameters: $n$ (trials) and $p$ (success probability). | Single parameter: $\lambda = np$ (mean arrival / occurrence rate). |
| **Mean vs. Variance** | $\text{Mean} = np$, $\text{Variance} = npq$. Mean is strictly greater than variance (since $q < 1$). | $\text{Mean} = \lambda$, $\text{Variance} = \lambda$. Mean and variance are strictly equal. |
| **PMF Equation** | $P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$ for $x = 0, 1, \dots, n$. | $P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}$ for $x = 0, 1, 2, \dots$. |
| **Typical Use Case** | Tossing coins, quality control defectives in fixed batches of 10 items. | Incoming phone calls per hour, typographical errors per page, rare diseases. |

---

### ⚖️ 4. One-Way ANOVA vs. Two-Way ANOVA

[**Q084**](/bca_new/bcs040/topics/08-anova?id=q084) • **Asked 3 times (15 marks)** • *Recent: Dec 2023 Q3, June 2021 Q4*

| Dimension | One-Way ANOVA | Two-Way ANOVA |
| :--- | :--- | :--- |
| **Independent Variables** | Examines the effect of a **single factor** (e.g., 3 machine types or 3 diets). | Examines the simultaneous effect of **two factors** (e.g., 4 catalysts across 3 plants). |
| **Partitioning of Variance** | $TSS = SSB + SSW$ (Between-groups and Within-groups/Error). | $TSS = SSA + SSB + SSE$ (Factor A, Factor B, and Residual Error). |
| **Hypotheses Tested** | Single null hypothesis: $H_0: \mu_1 = \mu_2 = \dots = \mu_k$. | Two separate hypotheses: $H_{0A}$ (Factor A equality) and $H_{0B}$ (Factor B equality). |
| **Degrees of Freedom** | $df_{\text{Between}} = k - 1$, $df_{\text{Error}} = N - k$. | $df_A = r - 1$, $df_B = c - 1$, $df_{\text{Error}} = (r - 1)(c - 1)$. |
| **Experimental Design** | Completely Randomized Design (CRD). | Randomized Block Design (RBD) or Two-Factor Factorial Design. |

---

### ⚖️ 5. Stratified Sampling vs. Cluster Sampling

[**Q006**](/bca_new/bcs040/topics/01-sampling-distributions?id=q006) • **Asked 4 times (20 marks)** • *Recent: June 2024 Q2, June 2017 Q2*

| Criterion | Stratified Random Sampling | Cluster Sampling |
| :--- | :--- | :--- |
| **Subdivision Basis** | Population is divided into non-overlapping groups called **strata**. | Population is divided into naturally occurring groups called **clusters**. |
| **Internal Composition** | **Homogeneous within** each stratum; **heterogeneous between** strata. | **Heterogeneous within** each cluster; **homogeneous between** clusters. |
| **Sampling Mechanism** | A random sample is selected from **every single stratum**. | A random sample of **clusters is chosen**, and all units in selected clusters are studied. |
| **Primary Objective** | Increases precision and reduces standard error of the estimate. | Minimizes administrative survey costs, travel time, and logistical overhead. |
| **Sampling Frame** | Complete sampling frame required for every single sub-population stratum. | Sampling frame required only for clusters, not for all individual elements. |

---

### ⚖️ 6. Point Estimation vs. Interval Estimation

[**Q089**](/bca_new/bcs040/topics/09-estimation-confidence-intervals?id=q089) • **Asked 3 times (15 marks)** • *Recent: Dec 2024 Q2, June 2022 Q3*

| Characteristic | Point Estimation | Interval Estimation |
| :--- | :--- | :--- |
| **Definition** | A single numerical value calculated from sample data used to estimate a population parameter. | A range of values (confidence interval) within which the true parameter is expected to lie. |
| **Standard Formula** | $\hat{\mu} = \bar{x} = \frac{\sum x}{n}$. | $\bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$ or $\bar{x} \pm t_{\alpha/2} \cdot \frac{s}{\sqrt{n}}$. |
| **Confidence Level** | Does not provide a confidence level or probability of capturing the true parameter. | Directly tied to a prescribed confidence coefficient (e.g., $95\%$ or $99\%$). |
| **Error Quantification** | Does not reflect sample variability or margin of error. | Explicitly incorporates margin of error ($E = Z_{\alpha/2} \sigma / \sqrt{n}$) and sample size $n$. |
| **Information Provided** | Simple but incomplete statement about the parameter. | Comprehensive statement incorporating precision and reliability. |

---

### ⚖️ 7. Chance Causes vs. Assignable Causes in SQC

[**Q096**](/bca_new/bcs040/topics/10-statistical-quality-control?id=q096) • **Asked 2 times (10 marks)** • *Recent: Dec 2024 Q6, June 2021 Q5*

| Feature | Chance (Common) Causes of Variation | Assignable (Special) Causes of Variation |
| :--- | :--- | :--- |
| **Origin & Nature** | Inherent, natural fluctuations built into any stable operating process. | External, abnormal disruptions introduced into the operating process. |
| **Predictability** | Follows statistical laws of probability and remains stable over time. | Unpredictable, erratic, and causes process instability. |
| **Examples** | Slight voltage variations, minute machine vibration, atmospheric humidity. | Tool wear, defective raw materials, operator fatigue, improper machine setting. |
| **Elimination Strategy** | Cannot be eliminated economically without completely re-engineering the process. | Can be identified, tracked, and eliminated through corrective operating actions. |
| **Process State** | When only chance causes exist, the process is in **Statistical Quality Control**. | When assignable causes exist, the process is **Out of Control**. |

---

### ⚖️ 8. Type I Error ($\alpha$) vs. Type II Error ($\beta$)

[**Q048**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q048) • **Asked 3 times (15 marks)** • *Recent: Dec 2023 Q2, June 2022 Q4*

| Dimension | Type I Error (Producer's Risk - $\alpha$) | Type II Error (Consumer's Risk - $\beta$) |
| :--- | :--- | :--- |
| **Statistical Definition** | Rejecting the null hypothesis $H_0$ when it is actually **true**. | Failing to reject (accepting) $H_0$ when it is actually **false**. |
| **Probability Denotation** | $P(\text{Reject } H_0 \mid H_0 \text{ is true}) = \alpha$ (Level of Significance). | $P(\text{Fail to reject } H_0 \mid H_0 \text{ is false}) = \beta$. |
| **Analogy in Judicial System** | Convicting an innocent person (False Positive). | Acquitting a guilty criminal (False Negative). |
| **Control Mechanism** | Directly set by the researcher prior to the test (typically $0.05$ or $0.01$). | Controlled indirectly by increasing sample size $n$ or choosing a more powerful test. |
| **Power of the Test** | Complement is the Confidence Level ($1 - \alpha$). | Complement is the **Power of the Test** ($1 - \beta$). |

---

### ⚖️ 9. Mean vs. Median

[**Q068**](/bca_new/bcs040/topics/06-descriptive-statistics?id=q068) • **Asked 3 times (15 marks)** • *Recent: June 2024 Q6, Dec 2020 Q1*

| Property | Arithmetic Mean ($\bar{x}$) | Median ($M$) |
| :--- | :--- | :--- |
| **Mathematical Nature** | Strictly algebraic center: sum of observations divided by total count. | Positional center: the middle observation dividing sorted data into two halves. |
| **Outlier Sensitivity** | **Highly sensitive to extreme values**; a single large outlier heavily inflates the mean. | **Highly resistant to outliers**; extreme values at ends do not shift the median value. |
| **Mathematical Treatment** | Well-suited for further algebraic manipulation (e.g., combined mean $\bar{x}_{12}$). | Not readily amenable to further algebraic treatment. |
| **Open-Ended Classes** | Cannot be calculated for grouped data with open-ended class intervals (e.g., "$> 500$"). | Can be easily calculated for open-ended classes as long as median falls in closed class. |
| **Graphic Determination** | Cannot be determined directly from cumulative frequency curves (ogives). | Determined directly from the intersection of less-than and more-than ogives. |

---

### ⚖️ 10. Additive vs. Multiplicative Time Series Models

[**Q077**](/bca_new/bcs040/topics/07-time-series-forecasting?id=q077) • **Asked 10 times (50 marks)** • *Recent: June 2026 Q7, Dec 2025 Q7, Dec 2023 Q4*

| Factor | Additive Model ($Y = T + S + C + I$) | Multiplicative Model ($Y = T \times S \times C \times I$) |
| :--- | :--- | :--- |
| **Basic Assumption** | The four components operate **independently** in absolute numerical terms. | The four components are **interdependent**; seasonal/cyclical fluctuations scale with trend. |
| **Seasonal Amplitude** | Seasonal variation remains **constant in magnitude** regardless of trend level. | Seasonal variation **increases or decreases proportionally** with trend level. |
| **Component Units** | All four components are expressed in the original physical units of measurement. | Trend $T$ is in original units; $S, C, I$ are dimensionless percentage ratios ($0.8$ to $1.2$). |
| **Practical Application** | Used when economic series displays uniform seasonal swings over time. | Predominantly used in business and economic time series (sales, profits, retail turnover). |

---

### ⚖️ 11. Variables Control Charts vs. Attributes Control Charts

[**Q095**](/bca_new/bcs040/topics/10-statistical-quality-control?id=q095) • **Asked 2 times (10 marks)** • *Recent: June 2025 Q5, Dec 2021 Q5*

| Feature | Control Charts for Variables | Control Charts for Attributes |
| :--- | :--- | :--- |
| **Data Nature** | Continuous measurable physical characteristics (length, weight, diameter, temperature). | Discrete qualitative count data (defective vs. non-defective, defect counts). |
| **Standard Charts** | $\bar{X}$-chart (process average) and $R$-chart / $S$-chart (process dispersion). | $p$-chart (fraction defective), $np$-chart (number of defectives), $c$-chart, $u$-chart. |
| **Sample Size Required** | Small sample subgroups ($n = 4$ or $5$) provide high statistical sensitivity. | Large sample sizes required ($n = 50$ to $200$) to detect rare attribute defects. |
| **Cost & Inspection** | More expensive per unit due to precise laboratory measuring instruments. | Economical and fast: uses Go/No-Go gauges or visual inspection. |
| **Diagnostic Power** | Provides exact warning of impending process drift before parts become defective. | Indicates that defective parts exist but does not pinpoint the degree of deviation. |

---

### ⚖️ 12. Linear Systematic Sampling vs. Circular Systematic Sampling

[**Q007**](/bca_new/bcs040/topics/01-sampling-distributions?id=q007) • **Asked 3 times (15 marks)** • *Recent: Dec 2024 Q2, June 2023 Q2*

| Evaluation Criteria | Linear Systematic Sampling | Circular Systematic Sampling |
| :--- | :--- | :--- |
| **Population Size Requirement** | Strictly requires population size $N$ to be an exact integer multiple of sample size $n$ ($N = nk$). | Applicable whether $N$ is an exact integer multiple of $n$ or not ($N \ne nk$). |
| **Random Start Range** | Random start $r$ is chosen strictly between $1$ and sampling interval $k$ ($1 \le r \le k$). | Random start $r$ is chosen from the entire population range $1$ to $N$ ($1 \le r \le N$). |
| **Sampling Selection Sequence** | Elements selected: $r, r+k, r+2k, \dots, r+(n-1)k$. Stops at end of list. | Elements selected by wrapping cyclically around the list modulo $N$. |
| **Sample Size Stability** | Sample size can fluctuate between $n$ and $n-1$ if $N \ne nk$. | Sample size is always **strictly equal to $n$** for any integer $N$. |
| **Sample Inclusion Probability** | Inclusion probabilities may vary slightly across units if $N$ is not divisible by $n$. | Every unit in the population has a strictly equal inclusion probability ($n/N$). |

---

### ⚖️ 13. Sampling with Replacement (SWR) vs. Without Replacement (SWOR)

[**Q004**](/bca_new/bcs040/topics/01-sampling-distributions?id=q004) • **Asked 5 times (25 marks)** • *Recent: June 2025 Q2, Dec 2022 Q2*

| Dimension | Sampling with Replacement (SWR) | Sampling without Replacement (SWOR) |
| :--- | :--- | :--- |
| **Selection Procedure** | Each selected unit is returned to the population before drawing the next unit. | Selected units are not returned to the population and cannot appear twice. |
| **Total Possible Samples** | $N^n$ possible ordered samples of size $n$ from population $N$. | $\binom{N}{n}$ possible unordered samples (or $N! / (N-n)!$ ordered samples). |
| **Trial Independence** | Successive selections are completely independent; probabilities remain constant ($1/N$). | Selections are dependent; probabilities change at each draw ($1/N, 1/(N-1), \dots$). |
| **Variance of Sample Mean** | $\text{Var}(\bar{x})_{\text{SWR}} = \frac{\sigma^2}{n}$. | $\text{Var}(\bar{x})_{\text{SWOR}} = \frac{\sigma^2}{n} \cdot \left(\frac{N - n}{N - 1}\right)$ (Finite Population Correction). |
| **Statistical Efficiency** | Lower efficiency: same unit can be surveyed repeatedly without new information. | Higher efficiency: strictly smaller sampling variance for the same sample size $n$. |

---

### ⚖️ 14. Null Hypothesis ($H_0$) vs. Alternative Hypothesis ($H_1$)

[**Q047**](/bca_new/bcs040/topics/04-parametric-hypothesis-testing?id=q047) • **Asked 4 times (20 marks)** • *Recent: June 2024 Q3, Dec 2021 Q3*

| Parameter | Null Hypothesis ($H_0$) | Alternative Hypothesis ($H_1$ or $H_a$) |
| :--- | :--- | :--- |
| **Core Assertion** | Statement of **no difference**, no effect, or no relationship between populations. | Statement that a **real difference**, effect, or association exists. |
| **Mathematical Formulation** | Formulated using equality signs: $\mu = \mu_0$, $\mu_1 = \mu_2$, or $\sigma_1^2 = \sigma_2^2$. | Formulated using inequality signs: $\mu \ne \mu_0$ (two-tailed) or $\mu > \mu_0$ (one-tailed). |
| **Role in Statistical Testing** | The hypothesis that is **directly tested and either rejected or not rejected**. | The hypothesis accepted implicitly when $H_0$ is rejected. |
| **Burden of Proof** | Assumed true until empirical evidence provides overwhelming proof to the contrary. | Represents the researcher's substantive claim or research assertion. |
| **Error Association** | Rejecting true $H_0$ constitutes a **Type I Error** (probability $\alpha$). | Failing to reject false $H_0$ constitutes a **Type II Error** (probability $\beta$). |
