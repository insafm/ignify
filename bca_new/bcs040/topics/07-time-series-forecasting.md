# 07. Time Series Analysis & Forecasting

> **Syllabus Units:** Block 3 Unit 10 | **Rank:** #7 | **Frequency Score:** 29 | **Coverage:** 20/26 (76.9%) | **Importance:** High
> **Coverage:** 5 canonical questions from 26 TEE papers (June 2013 – June 2026), strictly sorted by exam frequency.

---

## ❓ Question Bank & Canonical Answers

### Q077: Define "Time Series" and explain its four components / categories with examples. :id=q077

🔴 **Very High Priority** • **10 (100 marks)** • *Theory, Long Answer*

**💡 Key Answer Points:**
A chronological sequence of observations recorded over equal time intervals. Components: Secular Trend (long-term direction, e.g., steady population growth), Seasonal Variation (intra-year periodic swings, e.g., winter heater sales), Cyclical Variation (multi-year boom/recession cycles), and Irregular Variation (unpredictable shocks like strikes or floods).

> **🗓️ Asked In Papers:** `Jun 2013 (Q8), Dec 2014 (Q6), Dec 2016 (Q5), Jun 2017 (Q7(a)), June 2020 (Q9), Jun 2022 (Q6(a)), Dec 2022 (Q8(b)), Jun 2024 (Q5), Jun 2025 (Q9), Jun 2026 (Q10(i))`

---

### Q078: Compute Moving Averages (3-period, 4-period centered, or 2-period) and plot the trend alongside original data (and forecast). :id=q078

🔴 **Very High Priority** • **9 (90 marks)** • *Numerical, Diagram, Short Answer*

**💡 Key Answer Points:**

#### 📋 Representative Exam Problem (June 2026, Q3 — 5 Marks)
Consider the following data of sales of milk by a dairy in a week:

| Day | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sales (in litres)** | 500 | 400 | 450 | 500 | 600 | 700 | 800 |

*Task:* Find the moving average of length 3. Also plot these moving averages.

#### 🧮 Step-by-Step Computational Table (3-Day Moving Average):
| Day ($t$) | Sales ($Y_t$) | 3-Day Moving Total | 3-Day Moving Average ($\bar{Y}_t$) | Trend Pattern |
| :--- | :---: | :---: | :---: | :--- |
| Monday | 500 | — | — | Initial boundary (no prior days) |
| Tuesday | 400 | $500 + 400 + 450 = 1350$ | $\frac{1350}{3} = \mathbf{450.0}$ | Local dip |
| Wednesday | 450 | $400 + 450 + 500 = 1350$ | $\frac{1350}{3} = \mathbf{450.0}$ | Stabilization |
| Thursday | 500 | $450 + 500 + 600 = 1550$ | $\frac{1550}{3} = \mathbf{516.67}$ | Rising upward |
| Friday | 600 | $500 + 600 + 700 = 1800$ | $\frac{1800}{3} = \mathbf{600.0}$ | Strong upward trend |
| Saturday | 700 | $600 + 700 + 800 = 2100$ | $\frac{2100}{3} = \mathbf{700.0}$ | Peak weekend demand |
| Sunday | 800 | — | — | Terminal boundary (no next day) |

*Plotting Instructions:* Plot Day on horizontal $X$-axis and Sales (litres) on vertical $Y$-axis. Plot raw data as solid line with dots; plot moving averages centered at Tuesday through Saturday as a dashed smoothed line clearly showing the upward secular trend.

#### 🔄 Cross-Session Variations & Moving Average Types:
| Exam Session | Dataset & Metric | Period / Length | Computed Moving Averages / Forecast |
| :--- | :--- | :--- | :--- |
| **Dec 2016 (Q8)** | Electricity demand (14 days) | 4-day & 2-day centered | 4-day MA: [245.0, 237.5, 243.75, 281.25, 318.75, 372.5, 421.25, 446.25, 408.75, 405.0, 375.0, 328.75] |
| **Jun 2017 (Q7b)**| Production (10 years) | 3-year & 4-year centered | 3-yr MA: [27.0, 28.33, 29.0, 28.67, 28.67, 29.33, 31.0, 31.33]; 4-yr centered: [28.13, 28.50, 28.75, 29.13, 29.63, 30.50] |
| **Dec 2018 (Q9)** | Monthly demand (12 months) | 3-month moving average | [52.0, 51.0, 51.33, 52.0, 60.0, 61.67, 59.67, 56.0, 51.0, 53.0]; Forecast for Month 13 = **53.0 units** |
| **Jun 2021 (Q6)** | Annual sales (12 years) | 3-year moving average | [23.33, 27.67, 42.0, 52.67, 68.33, 78.33, 77.67, 62.67, 46.67, 39.33] |
| **Dec 2021 (Q6)** | Annual rainfall (10 years) | 3-year moving average | [27.0, 28.33, 29.0, 28.67, 28.67, 29.33, 31.0, 31.33] |
| **Jun 2022 (Q7a)**| Quarterly sales (12 quarters)| 3-period moving average | [46.33, 47.0, 51.0, 54.33, 55.67, 53.67, 52.0, 50.0, 49.67, 52.33] |
| **Dec 2024 (Q4)** | Weekly milk sales (7 days) | 3-day moving average | [450.0, 450.0, 516.67, 600.0, 600.0] |
| **Jun 2026 (Q3)** | Weekly milk sales (7 days) | 3-day moving average | [450.0, 450.0, 516.67, 600.0, 700.0] |

> **🗓️ Asked In Papers:** `Dec 2016 (Q8), Jun 2017 (Q7(b)), Jun 2018 (Q10(e)), Dec 2018 (Q9), Jun 2021 (Q6), Dec 2021 (Q6), Jun 2022 (Q7(a)), Dec 2024 (Q4), Jun 2026 (Q3)`

---

### Q079: Explain Forecasting, its relation to future planning (or difference from prediction), and discuss forecasting models. :id=q079

🔴 **Very High Priority** • **5 (50 marks)** • *Theory, Long Answer*

**💡 Key Answer Points:**
Forecasting projects future outcomes systematically from historical data to guide planning (inventory, budgets, staffing); prediction can be qualitative/subjective without statistical extrapolation. Models split into Quantitative (Time Series: Moving Averages, Exponential Smoothing, Trend Projection; Causal: Regression) and Qualitative (Delphi, expert judgment, surveys).

> **🗓️ Asked In Papers:** `Jun 2014 (Q7), Dec 2020 (Q9), Jun 2023 (Q10(c)), Dec 2024 (Q8), Dec 2025 (Q8)`

---

### Q080: Fit a linear trend $y = a + bx$ to 6 months of demand data (Months 1–6; Demand: 46, 56, 54, 43, 57, 56). :id=q080

🟠 **High Priority** • **3 (30 marks)** • *Numerical, Short Answer*

**💡 Key Answer Points:**
$\bar{x} = 3.5, \bar{y} = 52.0$; $b = 1.20, a = 47.80 \Rightarrow y = 47.80 + 1.20x$.

> **🗓️ Asked In Papers:** `Jun 2015 (Q4), June 2020 (Q4), Jun 2023 (Q2)`

---

### Q081: Explain Exponential Smoothing; forecast new colleges (2001–2007: 5, 3, 3, 4, 3, 6, 4) using W = 0.1 and estimate error. :id=q081

🟡 **Medium Priority** • **2 (10 marks)** • *Theory, Numerical, Short Answer*

**💡 Key Answer Points:**
$F_t = W Y_{t-1} + (1-W) F_{t-1}$. Starting with $F_1 = Y_1 = 5$: Forecasts $= [5, 5.0, 4.8, 4.62, 4.558, 4.4022, 4.5620]$; Errors $= [0, -2.0, -1.8, -0.62, -1.558, 1.5978, -0.5620]$; MAD $= 1.3563$.

> **🗓️ Asked In Papers:** `Jun 2018 (Q7(b)), Jun 2021 (Q10(i))`
