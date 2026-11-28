# 05. Correlation & Regression Analysis

> **Syllabus Units:** Block 3 Unit 9 | **Rank:** #5 | **Frequency Score:** 32 | **Coverage:** 21/26 (80.8%) | **Importance:** Very High
> **Coverage:** 9 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q057: Calculate correlation coefficient $r$ (and slope $b_{yx}$) from summary statistics of 20 pairs ($n = 20, \Sigma x = 15, \Sigma xy = 50, \Sigma y^2 = 90$). :id=q057

🔴 **Very High Priority** • **8 (40 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Base (Jun 15, Dec 16, Jun 18, Dec 20, Jun 23, Jun 25; $\Sigma y = -6, \Sigma x^2 = 61$): $r = 0.8227, b_{yx} = 1.0955$. Jun 22 Q3 ($\Sigma Y = +6, \Sigma X^2 = 61$): $r = 0.6869, b_{yx} = 0.9146$. Jun 26 Q4 ($\Sigma Y = +6, \Sigma X^2 = 50$, $r$ only): $r = 0.7783$.

**📝 Example PQP Question (Jun 2026 Q4):**

In order to find the correlation coefficient between two variables $X$ and $Y$ from 20 pairs of observations, the following calculations are made:

$\sum X = 15$, $\sum Y = 6$, $\sum XY = 50$, $\sum X^2 = 50$ and $\sum Y^2 = 90$

Calculate the correlation coefficient. *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2016 (Q2)](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [Jun 2018 (Q5)](/bca_new/bcs040/pqp/BCS-040_June_2018.pdf ':ignore'), [Dec 2020 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore'), [Jun 2022 (Q3)](/bca_new/bcs040/pqp/BCS-040_June_2022.pdf ':ignore'), [Jun 2023 (Q4)](/bca_new/bcs040/pqp/BCS-040_June_2023.pdf ':ignore'), [Jun 2025 (Q5)](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore'), [Jun 2026 (Q4)](/bca_new/bcs040/pqp/BCS-040_June_2026.pdf ':ignore')

---

### Q058: Destroyed laboratory record: Given $\text{Var}(x) = 9$ and regression lines 8x - 10y + 66 = 0 and 40x - 18y - 214 = 0, find means, $r$, and $\text{SD}(y)$. :id=q058

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Intersection gives $\bar{x} = 13, \bar{y} = 17$. Slopes $b_{yx} = 8/10 = 0.80$ and $b_{xy} = 18/40 = 0.45$ give $r = +\sqrt{0.36} = 0.60$ and $\sigma_y = (0.8 \times 3)/0.6 = 4.00$. (In Dec 22 Q7, note 4x is a typo causing $b_{yx}b_{xy} = 3.6 > 1$ and solve using 40x).

**📝 Example PQP Question (Jun 2025 Q10):**

In a partially destroyed laboratory record of an analysis of correlation of data, only the following results are legible:

Variance of $x = 9$,

Regression equations:
(i) $8x - 10y + 66 = 0$
(ii) $40x - 18y - 214 = 0$

What were (a) the means of $x$ and $y$, (b) the coefficient of correlation between $x$ and $y$, and (c) the standard deviation of $y$? *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2015 (Q7)](/bca_new/bcs040/pqp/BCS-040_Dec_2015.pdf ':ignore'), [June 2020 (Q7)](/bca_new/bcs040/pqp/BCS-040_June_2020.pdf ':ignore'), [Dec 2022 (Q7)](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore'), [Jun 2025 (Q10)](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore')

---

### Q059: Fit linear regression lines (+ scatter diagram / prediction) for unique paired datasets. :id=q059

🟠 **High Priority** • **4 (40 marks)** • *Numerical, Diagram, Long Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (June 2024, Q8 — 10 Marks)
Given data on Advertising Cost ($X$, in ₹ '000) and Sales Volume ($Y$, in ₹ '000) for 6 regions:
| Region | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Adv. Cost ($X$)** | 2 | 4 | 5 | 6 | 8 | 11 |
| **Sales ($Y$)** | 3 | 5 | 6 | 8 | 10 | 14 |

*Task:* Fit linear regression equation $\hat{Y} = a + bX$ and estimate sales for an advertising expenditure of ₹ 15,000 ($X = 15$).

#### 🧮 Step-by-Step Computational Table:
| Point | $X$ | $Y$ | $X^2$ | $XY$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 2 | 3 | 4 | 6 |
| 2 | 4 | 5 | 16 | 20 |
| 3 | 5 | 6 | 25 | 30 |
| 4 | 6 | 8 | 36 | 48 |
| 5 | 8 | 10 | 64 | 80 |
| 6 | 11 | 14 | 121 | 154 |
| **Total ($n=6$)** | **36** | **46** | **266** | **338** |

- $\bar{X} = 6.0, \bar{Y} = 7.667$.
- Slope $b = \frac{6(338) - 36(46)}{6(266) - 36^2} = \frac{2028 - 1656}{1596 - 1296} = \frac{372}{300} = \mathbf{1.24} \approx 1.25$. Intercept $a = 7.667 - 1.24(6.0) = \mathbf{0.227} \approx 0.25$.
- Regression line: $\mathbf{\hat{Y} = 0.25 + 1.25X}$.
- Prediction at $X = 15$: $\hat{Y} = 0.25 + 1.25(15) = \mathbf{19.00}$ (₹ 19,000).

#### 🔄 Cross-Session Variations & Regression Equations:
| Exam Session | Variables ($X \to Y$) | Sample ($n$) | Fitted Line | Prediction Target & Result |
| :--- | :--- | :---: | :--- | :--- |
| **Dec 2017 (Q7)** | Stress ($X$) $\to$ Tensile Strength ($Y$) | $n = 5$ | $\hat{Y} = -3.20 + 0.80X$ | At $X = 5 \text{ kg} \to \hat{Y} = \mathbf{0.80}$ |
| **Jun 2021 (Q9)** | Paired $(X, Y)$ test data | $n = 7$ | $\hat{Y} = 1.751 + 1.372X$ | At $X = 8 \to \hat{Y} = \mathbf{12.72}$ |
| **Dec 2021 (Q10)**| Age ($X$) $\to$ Blood Pressure ($Y$) | $n = 8$ | $\hat{Y} = 22.887 + 1.694X$ | At Age $38 \to \hat{Y} = \mathbf{87.24}\text{ mmHg}$ |
| **Jun 2024 (Q8)** | Adv Cost ($X$) $\to$ Sales ($Y$) | $n = 6$ | $\hat{Y} = 0.25 + 1.25X$ | At $X = 15 \to \hat{Y} = \mathbf{19.00}\text{ (₹19,000)}$ |

**📝 Example PQP Question (Jun 2024 Q8):**

A company has the following cost and sales data:

| Cost (in ₹ '000) | Sales (in ₹ '000) |
| :---: | :---: |
| 10 | 15 |
| 12 | 16 |
| 13 | 16 |
| 11 | 15 |
| 9 | 10 |
| 11 | 14 |
| 12 | 14 |
| 10 | 12 |

(i) Construct a scatter plot for the given data.
(ii) Find the best linear regression line assuming that cost is an independent variable and sales is a dependent variable.
(iii) Predict sale when cost is ₹ 15,000. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2017 (Q7)](/bca_new/bcs040/pqp/BCS-040_Dec_2017.pdf ':ignore'), [Jun 2021 (Q9)](/bca_new/bcs040/pqp/BCS-040_June_2021.pdf ':ignore'), [Dec 2021 (Q10)](/bca_new/bcs040/pqp/BCS-040_Dec_2021.pdf ':ignore'), [Jun 2024 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')

---

### Q060: Fit best linear regression line for 9-month Output (1,2,4,8,6,5,8,9,7) and Cost (2,3,4,7,6,5,8,8,6) data, and predict cost for 4 tons output. :id=q060

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
Dec 14 Q9 / Dec 25 Q9 (Cost on Output): $y = 1.2679 + 0.7518x \Rightarrow 4.2750$ thousand dollars at $x = 4$. Jun 13 Q10 (explicitly Output dependent, Cost independent): $\text{Output} = -1.4755 + 1.2914(\text{Cost}) \Rightarrow$ Cost $= 4.2399$ lakhs at Output = 4.

**📝 Example PQP Question (Dec 2025 Q9):**

An IT company wants to estimate how its monthly costs are related to its monthly output rate? For that the firm collects a data regarding its costs and outputs for a sample of nine months as given below:

| Output (tons) | Production Cost (in thousands of dollars) |
| :---: | :---: |
| 1 | 2 |
| 2 | 3 |
| 4 | 4 |
| 8 | 7 |
| 6 | 6 |
| 5 | 5 |
| 8 | 8 |
| 9 | 8 |
| 7 | 6 |

(a) Calculate the best linear regression line.
(b) Use this regression line to predict the firm's monthly costs if they decide to produce 4 tons per month. *(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2013 (Q10)](/bca_new/bcs040/pqp/BCS-040_June_2013.pdf ':ignore'), [Dec 2014 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [Dec 2025 (Q9)](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q061: Find and plot the regression line of $y$ (stopping distance) on $x$ (speed: 30, 40, 50, 60; $y$: 160, 240, 330, 435) on a scatter diagram. :id=q061

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Diagram, Long Answer*

**💡 Key Answer Points:**
$\hat{y} = -120.50 + 9.15x$ ($r = 0.9981$); plot the 4 points and draw the line through $(30, 154)$ and $(60, 428.5)$.

**📝 Example PQP Question (Dec 2023 Q8):**

Find and plot the regression line of $y$ on $x$, for the data given below:

| Speed (km/hr.) | 30 | 40 | 50 | 60 |
| :--- | :---: | :---: | :---: | :---: |
| Stopping distance (in feet) | 160 | 240 | 330 | 435 |

*(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q8)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2022 (Q6)](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore'), [Dec 2023 (Q8)](/bca_new/bcs040/pqp/BCS-040_Dec_2023.pdf ':ignore')

---

### Q062: Differentiate between Correlation and Regression. :id=q062

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Correlation quantifies linear strength/direction ($-1 \le r \le 1$, symmetric $r_{xy}=r_{yx}$, unitless); Regression models functional prediction ($y = a + bx$, asymmetric $b_{yx} \ne b_{xy}$, unit-dependent, distinguishes dependent vs. independent variables).

**📝 Example PQP Question (Dec 2025 Q10(b)):**

Differentiate between the following:
(b) Correlation and Regression *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q8(c))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Dec 2016 (Q7(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [Dec 2025 (Q10(b))](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q063: Write short notes on Correlation, Rank-Correlation, and/or Regression. :id=q063

🟠 **High Priority** • **3 (15 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Define Pearson's $r$, Spearman's rank correlation $\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}$ for ordinal rankings, and least-squares regression $y = a + bx$.

**📝 Example PQP Question (Jun 2024 Q6(ii)):**

Write short notes on any two of the following:
(ii) Correlation *(2.5 marks)*

> **🗓️ Asked In Papers:** [Dec 2014 (Q5(c))](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [Jun 2021 (Q10(iii))](/bca_new/bcs040/pqp/BCS-040_June_2021.pdf ':ignore'), [Jun 2024 (Q6(ii))](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')

---

### Q064: Using $\hat{y} = 90 + 50x$, complete $\hat{y}_i$ and $e_i$ for 5 points ($x$: 0.96, 1.28, 1.65, 1.84, 2.35; $y$: 138, 160, 178, 190, 210), compute $R$ and $R^2$, and interpret. :id=q064

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Long Answer*

**💡 Key Answer Points:**
$\hat{y}_i = [138, 154, 172.5, 182, 207.5]$, $e_i = [0, 6, 5.5, 8, 2.5]$; $SSE = 136.50, SST = 3052.80$; $R^2 = 1 - SSE/SST = 0.9553, R = 0.9774$ (Pearson $r = 0.9939, r^2 = 0.9879$), indicating very strong positive correlation.

**📝 Example PQP Question (Dec 2020 Q7):**

Using the regression line: $\hat{y} = 90 + 50x$, fill up the values in the table below:

| Sample No. ($i$) | 12 | 21 | 15 | 1 | 24 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $x_i$ | 0.96 | 1.28 | 1.65 | 1.84 | 2.35 |
| $y_i$ | 138 | 160 | 178 | 190 | 210 |
| $\hat{y}_i$ | 138 | — | — | — | — |
| $e_i = y_i - \hat{y}_i$ | 0 | — | — | — | — |

After filling the table, compute the parameters $R$ and $R^2$. Interpret the correlation between $X$ and $Y$. *(10 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q6)](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Dec 2020 (Q7)](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore')

---

### Q065: Car age (1–6 years) vs. Annual maintenance cost: draw scatter diagram, fit regression line (and predict for 8 years). :id=q065

🟡 **Medium Priority** • **2 (20 marks)** • *Numerical, Diagram, Long Answer*

**💡 Key Answer Points:**
2019-I Q7 ($y = [10,15,18,20,25,35]$): $\hat{y} = 4.80 + 4.4857x \Rightarrow 40.69$ hundred rupees at $x = 8$. Jun 26 Q7 ($y = [10,12,15,15,18,20]$): $\hat{y} = 8.20 + 1.9429x$.

**📝 Example PQP Question (Jun 2026 Q7):**

A manager of a car company wants to find the relationship between age of cars and annual maintenance cost. The following data from the cars of same model are obtained:

| Age of Car (in years) | Maintenance Cost (in thousand rupees) |
| :---: | :---: |
| 1 | 10 |
| 2 | 12 |
| 3 | 15 |
| 4 | 15 |
| 5 | 18 |
| 6 | 20 |

(i) Construct a scatter diagram for the above data.
(ii) Fit a best linear regression line, by taking annual maintenance cost as dependent variable and the age of the car as the independent variable. *(10 marks)*

> **🗓️ Asked In Papers:** [2019-I (Q7)](/bca_new/bcs040/pqp/BCS-040_June_2019.pdf ':ignore'), [Jun 2026 (Q7)](/bca_new/bcs040/pqp/BCS-040_June_2026.pdf ':ignore')
