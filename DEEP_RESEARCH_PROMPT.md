# Gemini Deep Research Prompt Template (Subject Dump Generator)

> Use this prompt with **Gemini Deep Research** alongside your uploaded IGNOU Previous-Year Question Papers (PQPs) to generate the structured `dump/*.md` file for any subject on **IGNify**.
> Replace `[PROGRAMME / COURSE_CODE - SUBJECT_NAME]` (and the PDF naming pattern if different) before running.

---

```markdown
I have uploaded multiple previous-year IGNOU **[PROGRAMME, e.g., BCA_NEW] — [COURSE_CODE - SUBJECT_NAME, e.g., BCS-131 - Programming in C++]** Term-End Examination (TEE) question papers.

Your task is to perform a deep, exhaustive exam analysis focused on maximizing marks for the upcoming exam, and output the complete report in clean **Markdown** so it can be used directly to generate the subject's learning portal (`README.md`, `analysis.md`, `comparisons.md`, `predictions.md`, `questions.md`, and `topics/*.md`).

---

### 1. Extraction & Deduplication Rules
- Extract **every single question and sub-part** from all uploaded papers (do not skip any question, short note, numerical, code snippet, or diagram).
- Group questions into logical **syllabus/topic modules**, sorted from **highest to lowest importance**.
- Deduplicate equivalent questions into **canonical questions**, preserving every session and question number where each canonical question appeared.
- Standardize **Session + Question Number** tags consistently across the entire output (e.g., `Jun 2013 (Q3)`, `Dec 2024 (Q5(a))`, `June 2026 (Q1(b))` — or `YYYY-MM Q#(part)`), matching the exact exam sessions of the uploaded PDFs so every tag can be linked directly to its PQP PDF.
- **Formatting Rule:** Do **NOT** use Markdown blockquotes (`>`) inside question bodies, answer points, or verbatim example questions. Reserve `> **🗓️ Asked In Papers:**` strictly for the final metadata line of each question.

---

### 2. Exam Blueprint & Structural Trends
Provide a concise overview of:
- Total papers analyzed, session range (e.g., June 2013 – June 2026), and total raw question items vs. deduplicated canonical questions.
- Marking scheme & section structure (compulsory vs. optional sections, marks per question, calculator/aid rules, and any major format shifts across eras).
- Practical caveats and paper anomalies (e.g., printing typos, missing data, dual-coded papers).

---

### 3. Topic Frequency & Importance Table
Create a summary table sorted from **highest to lowest importance** based on Frequency Score, Paper Coverage, and Recent Trend:

| Topic | Total Questions | Repeated Questions | Frequency Score | Paper Coverage | Importance |
| :--- | :---: | :---: | :---: | :---: | :--- |

*(Importance tiers: `Very High`, `High`, `Medium`, `Low`.)*

---

### 4. Repetition Pattern Analysis
Analyze and list:
1. **Most Repeated Questions** (top canonical questions with exact appearance counts and marks).
2. **Most Repeated Concepts** (core procedures, theorems, algorithms, or mechanisms).
3. **Most Repeated Definitions** (high-frequency short notes and glossary prompts).
4. **Most Repeated Diagrams / Code / Numericals** (exact diagram types, coding patterns, or numerical workhorses).
5. **Most Repeated Comparisons** as a structured table:
   | Comparison Pair | Canonical ID | Frequency | Asked In |
6. **Most Repeated Short-Answer vs. Long-Answer Questions** (section placement divide).
7. **Questions Repeated with Minor Modifications & Paper Anomalies** as a structured table:
   | Template | Canonical ID | Exact Modification or Paper Anomaly | Impact on Solution |

---

### 5. High-Probability Exam Areas by Topic
For each topic module, provide:
- **Frequency of Appearance** (appearances across N papers and %)
- **Important Subtopics**
- **Frequently Tested Concepts**
- **Frequently Tested Problem Types**

---

### 6. Consolidated Topic-Wise Question Bank (Primary Portal Dataset)
List **every unique canonical question** from all uploaded papers without duplication, grouped under its topic heading (`TOPIC: [Topic Name]`), and sorted within each topic by **highest to lowest historical frequency/marks**.

Use this **exact format** for every canonical question:

```markdown
### Q001: [Clear canonical question statement summarizing the core ask]

**[Very High / High / Medium / Low] Priority** • **[Frequency] ([Total Marks] marks)** • *[Question Type: Theory / Numerical / Coding / Diagram / Short Answer / Long Answer]*

**💡 Key Answer Points:**
[Concise, high-scoring exam takeaways: key definitions, formulas in LaTeX `$...$`, step-by-step algorithm/points, comparison tables, or compact code/ASCII architecture.]

**📝 Example PQP Question ([Session] [Q#]):**

[Full verbatim question text from one of the uploaded PQP papers—preferably the most recent clear appearance—including exact wording, numerical data/tables formatted in Markdown, code snippets in fenced code blocks, sub-parts, and marks like `*(5 marks)*` or `*(10 marks)*`. Do NOT use `>` blockquotes here.]

> **🗓️ Asked In Papers:** [Session 1 (Q#)], [Session 2 (Q#)], ...
```

---

### 7. Master Question List & Next-Exam Predictions
1. **Master Question List:** Compact index of all canonical questions (`Q001` – `Qnnn`) mapped to Topic, Frequency, Marks, and Importance (`Very High`, `High`, `Medium`, `Low`).
2. **Next-Exam Predictions:** High-probability questions and topics likely to appear in the upcoming TEE session, justified by:
   - Historical repetition rate and cycle/gap analysis
   - Recent-era topic density and format shifts
   - Recurring templates and likely parameter-modified variants
```
