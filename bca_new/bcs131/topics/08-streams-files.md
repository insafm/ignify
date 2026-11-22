# 08. Streams, Manipulators & File Handling

> **Syllabus Unit:** Block 3 Unit 1 | **Rank:** #8 | **Frequency Score:** 68.0 | **Offered Marks:** 260 | **Papers Present:** 24/30 | **Importance:** Medium-High

---

## 📋 Topic Overview

This module covers **17 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

### Quick Jump to Questions

| ID | Question Summary | Frequency | Marks | Type | Importance |
| :--- | :--- | :---: | :---: | :--- | :---: |
| [Q167](#q167) | What is a stream manipulator? Explain the use of setw() and setprecision() ... | **6x** | 31 marks | Theory / Short Answer | <span class="badge badge-vhigh">Very High</span> |
| [Q168](#q168) | Write a C++ program (with comments) to open an existing file and append "My... | **5x** | 50 marks | Coding / Long Answer | <span class="badge badge-high">High</span> |
| [Q169](#q169) | What are stream manipulators? Briefly discuss the purpose of various stream... | **5x** | 29 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q170](#q170) | What is a stream in C++? Name the stream classes generally used for file I/... | **4x** | 21 marks | Theory / Short Answer & Long Answer | <span class="badge badge-high">High</span> |
| [Q171](#q171) | Explain file pointers (get and put pointers) and operations (seekg(), seekp... | **3x** | 15 marks | Theory / Short Answer | <span class="badge badge-high">High</span> |
| [Q172](#q172) | Write the general form of user-defined stream manipulators and write a prog... | **2x** | 20 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q173](#q173) | What are file stream operations? Write a C++ program demonstrating reading ... | **2x** | 17 marks | Theory + Coding / Long Answer | <span class="badge badge-medium">Medium</span> |
| [Q174](#q174) | Explain input and output streams and stream classes in C++ with an example. | **2x** | 10 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q175](#q175) | Differentiate between: (i) ios::ate vs ios::app, (ii) Binary file vs Text f... | **2x** | 10 marks | Theory / Short Answer | <span class="badge badge-medium">Medium</span> |
| [Q176](#q176) | Explain file pointers and write a C++ program demonstrating put(), get(), r... | **1x** | 10 marks | Theory + Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q177](#q177) | Explain various file open modes (in, out, app, ate, trunc, binary) and the ... | **1x** | 10 marks | Theory / Long Answer | <span class="badge badge-low">Low</span> |
| [Q178](#q178) | Write a C++ program to copy the contents of one file into another file. | **1x** | 10 marks | Coding / Long Answer | <span class="badge badge-low">Low</span> |
| [Q179](#q179) | Explain the use of standard stream objects (cin, cout, cerr, clog) with exa... | **1x** | 8 marks | Theory / Long Answer | <span class="badge badge-low">Low</span> |
| [Q180](#q180) | What is a data stream? Explain the stream class hierarchy in C++. | **1x** | 5 marks | Theory + Diagram / Short Answer | <span class="badge badge-low">Low</span> |
| [Q181](#q181) | Write a C++ program to display a price-list of five vegetables using precis... | **1x** | 5 marks | Coding / Short Answer | <span class="badge badge-low">Low</span> |
| [Q182](#q182) | How is unformatted I/O different from formatted I/O? Explain. | **1x** | 5 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |
| [Q183](#q183) | Write a short note on File Stream Operations. | **1x** | 4 marks | Theory / Short Answer | <span class="badge badge-low">Low</span> |

---

## ❓ Detailed Question Bank & Answers

<div class="question-box" id="q167">

### <span class="badge-qid">Q167</span> What is a stream manipulator? Explain the use of setw() and setprecision() with examples.

<span class="badge badge-vhigh">Very High Priority</span> <span class="badge badge-freq">Frequency: 6 (31 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

<iomanip> functions formatting I/O streams; setw(n) sets minimum field width for next output; setprecision(k) sets significant/decimal digits.

> **🗓️ Asked In Papers:** `2013-06 1(f), 2014-06 3(c), 2019-06 1(e), 2020-06 1(f), 2022-06 1(c), 2025-06 2(a)`

</div>

<div class="question-box" id="q168">

### <span class="badge-qid">Q168</span> Write a C++ program (with comments) to open an existing file and append "My C++ File" / "File program in C++" at the end.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 5 (50 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

ofstream fout("file.txt", ios::app); check if(!fout) error, write string, fout.close();.

> **🗓️ Asked In Papers:** `2013-06 3(a), 2017-12S 5(a), 2020-06 5(a), 2022-06 4(a), 2025-06 4(a)`

</div>

<div class="question-box" id="q169">

### <span class="badge-qid">Q169</span> What are stream manipulators? Briefly discuss the purpose of various stream manipulators (explain any two).

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 5 (29 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Format output/input inline (endl, setw, setprecision, fixed, left, right, setfill).

> **🗓️ Asked In Papers:** `2019-12 5(d), 2020-12 5(iii), 2021-06 5(a), 2023-06 5(d), 2026-06 5(a)`

</div>

<div class="question-box" id="q170">

### <span class="badge-qid">Q170</span> What is a stream in C++? Name the stream classes generally used for file I/O and explain their utility.

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 4 (21 marks)</span> <span class="badge badge-topic">Theory / Short Answer & Long Answer</span>

**💡 Key Answer Points:**

Abstraction of byte flow; <fstream> classes: ifstream (read), ofstream (write), fstream (read+write), filebuf.

> **🗓️ Asked In Papers:** `2017-12S 3(c), 2022-06 5(b), 2024-06 4(d), 2025-12 2(d)`

</div>

<div class="question-box" id="q171">

### <span class="badge-qid">Q171</span> Explain file pointers (get and put pointers) and operations (seekg(), seekp(), tellg(), tellp()).

<span class="badge badge-high">High Priority</span> <span class="badge badge-freq">Frequency: 3 (15 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

seekg/tellg reposition/query input cursor; seekp/tellp reposition/query output cursor using ios::beg, ios::cur, ios::end.

> **🗓️ Asked In Papers:** `2014-06 5(d), 2018-12S 5(d), 2024-06 1(g)`

</div>

<div class="question-box" id="q172">

### <span class="badge-qid">Q172</span> Write the general form of user-defined stream manipulators and write a program implementing one (e.g., width 10, right, precision 2, fill *, trailing zeros).

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (20 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

ostream& manip(ostream& out) { out << setw(10) << right << fixed << setprecision(2) << setfill('*') << showpoint; return out; }

> **🗓️ Asked In Papers:** `2016-06 2(b), 2017-06 3(c)`

</div>

<div class="question-box" id="q173">

### <span class="badge-qid">Q173</span> What are file stream operations? Write a C++ program demonstrating reading from and writing to a disk file.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (17 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

Open file with ofstream, write text, close; open with ifstream, read via getline(), display, close.

> **🗓️ Asked In Papers:** `2014-12 4(b), 2019-12 3(b)`

</div>

<div class="question-box" id="q174">

### <span class="badge-qid">Q174</span> Explain input and output streams and stream classes in C++ with an example.

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (10 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

istream (cin), ostream (cout), iostream handle buffered formatted/unformatted data transfer.

> **🗓️ Asked In Papers:** `2013-12 5(b), 2016-06 1(c)`

</div>

<div class="question-box" id="q175">

### <span class="badge-qid">Q175</span> Differentiate between: (i) ios::ate vs ios::app, (ii) Binary file vs Text file, (iii) get() vs getline().

<span class="badge badge-medium">Medium Priority</span> <span class="badge badge-freq">Frequency: 2 (10 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

app always writes at EOF; ate seeks to EOF on open (can seek elsewhere). Binary stores raw bytes; Text translates newlines/ASCII. get() leaves delimiter in buffer; getline() discards it.

> **🗓️ Asked In Papers:** `2017-12S 3(a), 2022-06 5(a)`

</div>

<div class="question-box" id="q176">

### <span class="badge-qid">Q176</span> Explain file pointers and write a C++ program demonstrating put(), get(), read(), and write().

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory + Coding / Long Answer</span>

**💡 Key Answer Points:**

put()/get() handle single characters; write((char*)&obj, sizeof(obj)) and read(...) handle raw binary records.

> **🗓️ Asked In Papers:** `2016-06 1(e)`

</div>

<div class="question-box" id="q177">

### <span class="badge-qid">Q177</span> Explain various file open modes (in, out, app, ate, trunc, binary) and the working of seekg(), seekp(), tellg(), tellp(), read(), and write().

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

Detail all 6 ios:: flags, random-access cursor functions, and block binary I/O functions.

> **🗓️ Asked In Papers:** `2024-12 5(a)`

</div>

<div class="question-box" id="q178">

### <span class="badge-qid">Q178</span> Write a C++ program to copy the contents of one file into another file.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (10 marks)</span> <span class="badge badge-topic">Coding / Long Answer</span>

**💡 Key Answer Points:**

Open source with ifstream and destination with ofstream; loop while(fin.get(ch)) fout.put(ch);; close both

> **🗓️ Asked In Papers:** `2025-12 4(a)`

</div>

<div class="question-box" id="q179">

### <span class="badge-qid">Q179</span> Explain the use of standard stream objects (cin, cout, cerr, clog) with examples.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (8 marks)</span> <span class="badge badge-topic">Theory / Long Answer</span>

**💡 Key Answer Points:**

cin (stdin), cout (buffered stdout), cerr (unbuffered stderr), clog (buffered stderr).

> **🗓️ Asked In Papers:** `2019-06 4(b)`

</div>

<div class="question-box" id="q180">

### <span class="badge-qid">Q180</span> What is a data stream? Explain the stream class hierarchy in C++.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory + Diagram / Short Answer</span>

**💡 Key Answer Points:**

ios base → istream, ostream → iostream; file derivatives ifstream, ofstream, fstream.

> **🗓️ Asked In Papers:** `2012-12 4(b)`

</div>

<div class="question-box" id="q181">

### <span class="badge-qid">Q181</span> Write a C++ program to display a price-list of five vegetables using precision(2).

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Coding / Short Answer</span>

**💡 Key Answer Points:**

Arrays of 5 names/prices; cout << fixed << setprecision(2) (or cout.precision(2)) formatting tabular output

> **🗓️ Asked In Papers:** `2015-06 4(b)`

</div>

<div class="question-box" id="q182">

### <span class="badge-qid">Q182</span> How is unformatted I/O different from formatted I/O? Explain.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (5 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Unformatted (get, put, read, write) transfers raw bytes without conversion; formatted (>>, <<, manipulators) parses/formats human-readable text.

> **🗓️ Asked In Papers:** `2016-12 4(a)`

</div>

<div class="question-box" id="q183">

### <span class="badge-qid">Q183</span> Write a short note on File Stream Operations.

<span class="badge badge-low">Low Priority</span> <span class="badge badge-freq">Frequency: 1 (4 marks)</span> <span class="badge badge-topic">Theory / Short Answer</span>

**💡 Key Answer Points:**

Opening (open()/constructor), checking state (is_open(), eof()), reading/writing, and closing (close()).

> **🗓️ Asked In Papers:** `2021-12 5(a)`

</div>

