# 06. Descriptive Statistics & Data Visualization

> **Syllabus Units:** Block 1 Unit 1 | **Rank:** #6 | **Frequency Score:** 31 | **Coverage:** 26/26 (100.0%) | **Importance:** Very High
> **Coverage:** 11 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q066: Calculate Mean and Standard Deviation (or Mean and Median) for a grouped marks/wages frequency distribution. :id=q066

🔴 **Very High Priority** • **6 (30 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (June 2026, Q1 — 5 Marks)
The daily wages (in rupees) of 50 workers of a factory are given as follows:

| Daily Wages (₹) | No. of Workers ($f_i$) |
| :---: | :---: |
| 250–350 | 10 |
| 350–450 | 12 |
| 450–550 | 20 |
| 550–650 | 5 |
| 650–750 | 3 |

*Task:* Calculate the Mean and Standard Deviation of the wages of the workers.

#### 🧮 Step-by-Step Computational Table (Step-Deviation Method):
Let assumed mean $A = 500$ (midpoint of central class $450-550$) and class width $h = 100$.
Step deviation $d_i = \frac{x_i - A}{h} = \frac{x_i - 500}{100}$.

| Class Interval | Frequency ($f_i$) | Midpoint ($x_i$) | $d_i$ | $f_i d_i$ | $f_i d_i^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 250–350 | 10 | 300 | -2 | -20 | 40 |
| 350–450 | 12 | 400 | -1 | -12 | 12 |
| 450–550 | 20 | 500 | 0 | 0 | 0 |
| 550–650 | 5 | 600 | +1 | +5 | 5 |
| 650–750 | 3 | 700 | +2 | +6 | 12 |
| **Total** | **$N = 50$** | — | — | **$\sum f_i d_i = -21$** | **$\sum f_i d_i^2 = 69$** |

#### 📐 Formulas & Solutions:
1. **Arithmetic Mean ($\bar{x}$):**
   $$\bar{x} = A + \left(\frac{\sum f_i d_i}{N}\right) \times h = 500 + \left(\frac{-21}{50}\right) \times 100 = 500 - 42.00 = \mathbf{458.00 \text{ rupees}}$$
2. **Population Standard Deviation ($\sigma$):**
   $$\sigma = h \times \sqrt{\frac{\sum f_i d_i^2}{N} - \left(\frac{\sum f_i d_i}{N}\right)^2} = 100 \times \sqrt{\frac{69}{50} - (-0.42)^2} = 100 \times \sqrt{1.38 - 0.1764} = 100 \times \sqrt{1.2036} = \mathbf{109.71 \text{ rupees}}$$
   *(Sample standard deviation $s = \sigma \sqrt{\frac{N}{N-1}} = 109.71 \times \sqrt{\frac{50}{49}} = \mathbf{110.82 \text{ rupees}}$).*

#### 🔄 Cross-Session Variations & Results:
| Exam Session | Class Range & Variable | Sample ($N$) | Calculated Mean ($\bar{x}$) | Standard Deviation / Median |
| :--- | :--- | :---: | :---: | :--- |
| **Dec 2016 (Q1)** | 0–70 marks | $N = 100$ | $\bar{x} = 37.90$ | $\sigma = 16.33$ ($s = 16.41$) |
| **2019-I (Q1)** | 200–600 wages | $N = 20$ | $\bar{x} = 360.00$ | $\sigma = 88.88$ ($s = 91.19$) |
| **Jun 2022 (Q2)** | 0–60 marks | $N = 100$ | $\bar{x} = 31.30$ | $\sigma = 13.90$ ($s = 13.97$) |
| **Dec 2022 (Q3)** | 0–60 marks | $N = 100$ | $\bar{x} = 31.30$ | $\text{Median} = \mathbf{32.00}$ |
| **Dec 2024 (Q5)** | 0–50 marks | $N = 50$ | $\bar{x} = 24.00$ | $\sigma = 12.21$ ($s = 12.33$) |
| **Jun 2026 (Q1)** | 250–750 daily wages | $N = 50$ | $\bar{x} = 458.00$ | $\sigma = \mathbf{109.71}$ |

**📝 Example PQP Question (Jun 2026 Q1):**

The daily wages (in rupees) of 50 workers of a factory are given as follows:

| Daily wages | No. of workers |
| :---: | :---: |
| 250–350 | 10 |
| 350–450 | 12 |
| 450–550 | 20 |
| 550–650 | 5 |
| 650–750 | 3 |

Calculate mean and standard deviation of the wages of the workers. *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2016 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2016.pdf ':ignore'), [2019-I (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2019.pdf ':ignore'), [Jun 2022 (Q2)](/bca_new/bcs040/pqp/BCS-040_June_2022.pdf ':ignore'), [Dec 2022 (Q3)](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore'), [Dec 2024 (Q5)](/bca_new/bcs040/pqp/BCS-040_Dec_2024.pdf ':ignore'), [Jun 2026 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2026.pdf ':ignore')

---

### Q067: Draw a Histogram (and/or Frequency Polygon on the same scale) and calculate the Mean/average (and comment on shape). :id=q067

🔴 **Very High Priority** • **5 (25 marks)** • *Numerical, Diagram, Short Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (Dec 2023, Q4 / Dec 2017, Q1 — 5 Marks)
The number of road accidents occurring in a city across 50 weeks was recorded as:

| Number of Accidents (Class) | Number of Weeks ($f_i$) | Midpoint ($x_i$) | $f_i x_i$ |
| :---: | :---: | :---: | :---: |
| 0–4 | 8 | 2 | 16 |
| 5–9 | 22 | 7 | 154 |
| 10–14 | 10 | 12 | 120 |
| 15–19 | 8 | 17 | 136 |
| 20–24 | 2 | 22 | 44 |
| **Total** | **$N = 50$** | — | **$\sum f_i x_i = 470$** |

*Tasks:*
1. Calculate the mean number of accidents per week:
   $$\bar{x} = \frac{\sum f_i x_i}{N} = \frac{470}{50} = \mathbf{9.40 \text{ accidents/week}}$$
   *(Or with boundary adjustments $[0-5, 5-10, \dots]$ giving midpoint sequence $[2.5, 7.5, 12.5, 17.5, 22.5]$, $\sum f_i x_i = 495 \implies \mathbf{9.90}$).*
2. **Histogram Construction:** Draw rectangular bars whose widths correspond to the class intervals on the $X$-axis and heights correspond to frequencies on the $Y$-axis.
3. **Frequency Polygon:** Join the midpoints of the top of each histogram bar using straight line segments, and tie off at both ends to the horizontal axis at the midpoints of the preceding and succeeding imaginary classes.
4. **Distribution Shape:** The distribution exhibits positive (right) skewness with a distinct modal peak in the $5-9$ range and a tapering tail toward higher accident counts.

#### 🔄 Cross-Session Variations & Means:
| Exam Session | Domain / Variable | Sample ($N$) | Mean Value | Graphical Note |
| :--- | :--- | :---: | :---: | :--- |
| **Dec 2017 (Q1)** | 50 weeks accidents ([8, 22, 10, 8, 2]) | $N = 50$ | **$9.90$** | Histogram + Frequency polygon |
| **Jun 2018 (Q1)** | Machine production time 20–50 min | $N = 36$ | **$34.03$ min** | Unimodal, slightly right-skewed peaking at 30–35 |
| **Dec 2022 (Q1)** | Weekly income ₹14k–₹20k ([5, 10, 20, 9, 6, 2]) | $N = 52$ | **₹ 16.71k** | Bars + polygon closed at 13.5k & 20.5k |
| **Dec 2023 (Q4)** | 50 weeks accidents ([8, 22, 10, 8, 2]) | $N = 50$ | **$9.90$** | Histogram & mean |
| **Dec 2024 (Q1)** | 50 weeks accidents ([8, 20, 12, 8, 2]) | $N = 50$ | **$10.10$** | Histogram & mean |

**📝 Example PQP Question (Dec 2024 Q1):**

The Government has conducted a survey of road accidents. In this study the data of accidents of a particular road for the last 50 weeks were compiled. This data is grouped into a frequency distribution as follows:

| No. of Accidents | No. of Weeks |
| :---: | :---: |
| 0–5 | 8 |
| 5–10 | 20 |
| 10–15 | 12 |
| 15–20 | 8 |
| 20–25 | 2 |

Draw a histogram and calculate average number of accidents per week. *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2017 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2017.pdf ':ignore'), [Jun 2018 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2018.pdf ':ignore'), [Dec 2022 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2022.pdf ':ignore'), [Dec 2023 (Q4)](/bca_new/bcs040/pqp/BCS-040_Dec_2023.pdf ':ignore'), [Dec 2024 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2024.pdf ':ignore')

---

### Q068: Write two merits and two demerits of Median (and/or median formula). Given the 10–80 distribution ($f$: 12, 30, ?, 65, ?, 25, 18) with N = 200 and Median = 46, find the missing frequencies (or find Median when frequencies 34 and 46 are given). :id=q068

🟠 **High Priority** • **4 (20 marks)** • *Theory, Numerical, Short Answer*

**💡 Key Answer Points:**
Merits: unaffected by extreme values, works for open-end intervals. Demerits: ignores exact magnitudes, lacks algebraic properties. Formula: $M = L + \frac{N/2 - cf}{f_m}\times h$. Missing-frequency version (Jun 15, Dec 20, Jun 23): $f_1 + f_2 = 50$, median class 40–50 gives $46 = 40 + \frac{100-(42+f_1)}{65}\times 10 \Rightarrow f_1 = 19, f_2 = 31$. Dec 25 Q4 (f1 = 34, f2 = 46, N = 230): $M = 40 + \frac{115-76}{65}\times 10 = 46.00$.

**📝 Example PQP Question (Dec 2025 Q4):**

Write two merits and two demerits of median. Given the frequency distribution as follows:

| C. I. | Frequency |
| :---: | :---: |
| 10–20 | 12 |
| 20–30 | 30 |
| 30–40 | 34 |
| 40–50 | 65 |
| 50–60 | 46 |
| 60–70 | 25 |
| 70–80 | 18 |

Find the median value. *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2015 (Q6)](/bca_new/bcs040/pqp/BCS-040_June_2015.pdf ':ignore'), [Dec 2020 (Q6)](/bca_new/bcs040/pqp/BCS-040_Dec_2020.pdf ':ignore'), [Jun 2023 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2023.pdf ':ignore'), [Dec 2025 (Q4)](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q069: Construct a continuous frequency distribution from raw observations and draw a Histogram. :id=q069

🟠 **High Priority** • **4 (20 marks)** • *Numerical, Diagram, Short Answer*

**💡 Key Answer Points:**
Tally values into continuous intervals $[L, U)$ and plot touching vertical bars. Jun 17 Q1 (50 rainfall readings, 150–160 to 220–230): [4, 5, 3, 9, 6, 8, 7, 8]; 2019-II (6384) Q1 (25 marks, 0–10 to 40–50): [2, 4, 9, 6, 4]; Jun 21 Q1 (30 car services): width 5 (10–15 to 40–45) gives [3, 6, 5, 7, 4, 3, 2] or width 10 (10–20 to 40–50) gives [9, 12, 7, 2]; Jun 24 Q1 (20 bulb lives, width 10, 100–110 to 170–180): [2, 1, 2, 2, 3, 4, 4, 2].

**📝 Example PQP Question (Jun 2024 Q1):**

The life of 20 electric bulbs (in hours) are given as follows:

`125, 160, 175, 170, 111, 101, 165, 150, 140, 130, 120, 135, 145, 155, 165, 145, 105, 157, 167, 153`

(a) Construct a continuous frequency distribution of the data by taking class width 10. *(3 marks)*
(b) Draw the histogram of the distribution in given above. *(2 marks)*

> **🗓️ Asked In Papers:** [Jun 2017 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2017.pdf ':ignore'), [Dec June 2019 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2019.pdf ':ignore'), [Jun 2021 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2021.pdf ':ignore'), [Jun 2024 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')

---

### Q070: Given a sample of 20 (or 10) raw numbers, (a) compute Mean, Variance, and Standard Deviation; (b) if the largest value is changed to 500, analyze and justify how mean and variance are affected. :id=q070

🟠 **High Priority** • **3 (15 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
For Dec 14 / Undated Q1 (n = 20, largest 79 $\to$ 500): $\bar{x} = 46.35$, Sample Var $s^2 = 384.56$ ($s = 19.61$), Pop Var $= 365.33$; after change, $\bar{x}' = 67.40$ (+21.05), $s'^2 = 10,693.52$ ($s' = 103.41$), Pop Var $= 10,158.84$. For Dec 25 Q2 (n = 10, largest 59 $\to$ 500): $\bar{x} = 38.50$, $s^2 = 327.39$ ($s = 18.09$), Pop Var $= 294.65$; after change, $\bar{x}' = 82.60$ (+44.10), $s'^2 = 21,784.49$, Pop Var $= 19,606.04$. Justification: mean shifts linearly by $\Delta/n$, whereas variance surges because deviations are squared.

**📝 Example PQP Question (Dec 2025 Q2):**

Given the following sample of 10 numbers:

`12, 41, 48, 58, 14, 43, 50, 59, 15, 45`

(a) Compute Mean, Variance and Standard Deviation. *(3 marks)*
(b) If the largest value in the above set of numbers is changed to 500, to what extent are the mean and variance affected by the change? Justify your answer. *(2 marks)*

> **🗓️ Asked In Papers:** [Dec 2014 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2014.pdf ':ignore'), [June 2020 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2020.pdf ':ignore'), [Dec 2025 (Q2)](/bca_new/bcs040/pqp/BCS-040_Dec_2025.pdf ':ignore')

---

### Q071: Calculate an estimate of Median for grouped data (inclusive classes 0–24.9 to 125–149.9 or 200–700 wages). :id=q071

🟠 **High Priority** • **3 (15 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Jun 14 Q9(b) / Jun 25 Q4 (N = 70, N/2 = 35, class 75–99.9, cf = 31, f = 16): using true boundaries ($L = 74.95, h = 25$), Median $= 81.20$ (nominal limits: $81.225$). 2019-II (6384) Q2 (200–700, N = 50, N/2 = 25, class 400–500, cf = 22, f = 20): Median $= 400 + \frac{25-22}{20}\times 100 = 415.00$.

**📝 Example PQP Question (Jun 2025 Q4):**

Calculate an estimate of median for the following data:

| Class | Frequency |
| :---: | :---: |
| 0–24.9 | 6 |
| 25–49.9 | 11 |
| 50–74.9 | 14 |
| 75–99.9 | 16 |
| 100–124.9 | 13 |
| 125–149.9 | 10 |

*(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2014 (Q9(b))](/bca_new/bcs040/pqp/BCS-040_June_2014.pdf ':ignore'), [Dec June 2019 (Q2)](/bca_new/bcs040/pqp/BCS-040_Dec_2019.pdf ':ignore'), [Jun 2025 (Q4)](/bca_new/bcs040/pqp/BCS-040_June_2025.pdf ':ignore')

---

### Q072: The mean and standard deviation of 20 items are 10 and 2. One incorrect item of value 8 is deleted/omitted. Recalculate the mean and standard deviation. :id=q072

🟡 **Medium Priority** • **2 (10 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
Corrected $\sum x = 200 - 8 = 192 \Rightarrow$ New Mean $= 192/19 = 10.1053$. If given SD = 2 is population SD, $\sum x^2 = 20(4+100)=2080 \Rightarrow$ New $\sum x^2 = 2016 \Rightarrow$ New SD $= \sqrt{2016/19 - 10.1053^2} = 1.9972$ (if sample SD: $1.9971$).

**📝 Example PQP Question (Dec 2018 Q1):**

The mean and standard deviation of 20 items is found to be 10 and 2, respectively. At the time of checking it was found that one item with value 8 was incorrect. Calculate the mean and standard deviation if the wrong item is omitted. *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2016 (Q1)](/bca_new/bcs040/pqp/BCS-040_June_2016.pdf ':ignore'), [Dec 2018 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2018.pdf ':ignore')

---

### Q073: Compute Mean Deviation and Standard Deviation for 10 numbers (12, 41, 48, 58, 14, 43, 50, 59, 15, 79). :id=q073

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\bar{x} = 41.90$; Mean Deviation about Mean $MD = \frac{\sum |x_i - \bar{x}|}{10} = 17.12$; Sample SD $s = 22.18$ (Pop SD $\sigma = 21.05$).

**📝 Example PQP Question (Jun 2013 Q6):**

Given the following sample of 10 numbers: `12, 41, 48, 58, 14, 43, 50, 59, 15, 79`. Compute Mean deviation and Standard deviation for the data given above. *(5 marks)*

> **🗓️ Asked In Papers:** [Jun 2013 (Q6)](/bca_new/bcs040/pqp/BCS-040_June_2013.pdf ':ignore')

---

### Q074: Compute Mean, Standard Deviation, and Coefficient of Variation (CV) for dopamine levels in 10 rats (6.8, 7.0, 5.3, 6.0, 5.9, 5.6, 6.8, 7.4, 6.2, 7.0). :id=q074

⚪ **Low Priority** • **1 (5 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\bar{x} = 6.40$; Sample SD $s = 0.6944 \Rightarrow CV = (s/\bar{x})\times 100 = 10.85\%$ (Pop SD $\sigma = 0.6588 \Rightarrow CV = 10.29\%$).

**📝 Example PQP Question (Dec 2021 Q1):**

A pharmacologist measured the amount of dopamine (no. of moles/gm) in the brains of each of 10 rats. The observed data is given below:

`6.8, 7.0, 5.3, 6.0, 5.9, 5.6, 6.8, 7.4, 6.2, 7.0`

Calculate:
(i) The mean and standard deviation
(ii) Coefficient of variation *(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2021 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2021.pdf ':ignore')

---

### Q075: Write two merits and two demerits of Arithmetic Mean, and find the variance for the number of seeds in a pod ($x$: 1–6; $f$: 8, 14, 7, 12, 3, 1). :id=q075

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Numerical, Short Answer*

**💡 Key Answer Points:**
Merits: rigidly defined, uses every observation, algebraically tractable. Demerits: distorted by extreme outliers, unsuited to open-ended classes or qualitative data. Numerical (N = 45): $\bar{x} = 126/45 = 2.80$; Pop Variance $\sigma^2 = 1.7156$ (Sample Var $s^2 = 1.7545$).

**📝 Example PQP Question (Dec 2015 Q1):**

Write any two merits and demerits of Arithmetic Mean. Given below is the data about the number of seeds in a pod of a certain plant. Find the variance:

| No. of Seeds | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Frequency | 8 | 14 | 7 | 12 | 3 | 1 |

*(5 marks)*

> **🗓️ Asked In Papers:** [Dec 2015 (Q1)](/bca_new/bcs040/pqp/BCS-040_Dec_2015.pdf ':ignore')

---

### Q076: Write a short note on Median and Standard Deviation. :id=q076

⚪ **Low Priority** • **1 (5 marks)** • *Theory, Short Answer*

**💡 Key Answer Points:**
Median is the middle positional value dividing sorted data into two equal halves (outlier-resistant); Standard Deviation ($\sigma = \sqrt{\frac{\sum (x_i-\bar{x})^2}{n}}$) is the positive square root of variance quantifying dispersion around the mean in original units.

**📝 Example PQP Question (Jun 2024 Q6(iii)):**

Write short notes on any two of the following:
(iii) Median and Standard deviation *(2.5 marks)*

> **🗓️ Asked In Papers:** [Jun 2024 (Q6(iii))](/bca_new/bcs040/pqp/BCS-040_June_2024.pdf ':ignore')
