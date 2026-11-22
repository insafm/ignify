# 08. Streams, Manipulators & File Handling

> **Syllabus Unit:** Block 3 Unit 1 | **Rank:** #8 | **Frequency Score:** 68.0 | **Offered Marks:** 260 | **Papers Present:** 24/30 | **Importance:** Medium-High

---

## 📋 Topic Overview

This module covers **17 canonical questions** asked across 30 previous-year IGNOU Term-End Examination papers. Questions are prioritized by historical recurrence.

---

## ❓ Detailed Question Bank & Answers

### [Q167] What is a stream manipulator? Explain the use of setw() and setprecision() with examples. :id=q167

🔴 **Very High Priority** • **6 (31 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

<iomanip> functions formatting I/O streams; setw(n) sets minimum field width for next output; setprecision(k) sets significant/decimal digits.

> **🗓️ Asked In Papers:** `2013-06 1(f), 2014-06 3(c), 2019-06 1(e), 2020-06 1(f), 2022-06 1(c), 2025-06 2(a)`

### [Q168] Write a C++ program (with comments) to open an existing file and append "My C++ File" / "File program in C++" at the end. :id=q168

🟠 **High Priority** • **5 (50 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

ofstream fout("file.txt", ios::app); check if(!fout) error, write string, fout.close();.

> **🗓️ Asked In Papers:** `2013-06 3(a), 2017-12S 5(a), 2020-06 5(a), 2022-06 4(a), 2025-06 4(a)`

### [Q169] What are stream manipulators? Briefly discuss the purpose of various stream manipulators (explain any two). :id=q169

🟠 **High Priority** • **5 (29 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Format output/input inline (endl, setw, setprecision, fixed, left, right, setfill).

> **🗓️ Asked In Papers:** `2019-12 5(d), 2020-12 5(iii), 2021-06 5(a), 2023-06 5(d), 2026-06 5(a)`

### [Q170] What is a stream in C++? Name the stream classes generally used for file I/O and explain their utility. :id=q170

🟠 **High Priority** • **4 (21 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Abstraction of byte flow; <fstream> classes: ifstream (read), ofstream (write), fstream (read+write), filebuf.

> **🗓️ Asked In Papers:** `2017-12S 3(c), 2022-06 5(b), 2024-06 4(d), 2025-12 2(d)`

### [Q171] Explain file pointers (get and put pointers) and operations (seekg(), seekp(), tellg(), tellp()). :id=q171

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

seekg/tellg reposition/query input cursor; seekp/tellp reposition/query output cursor using ios::beg, ios::cur, ios::end.

> **🗓️ Asked In Papers:** `2014-06 5(d), 2018-12S 5(d), 2024-06 1(g)`

### [Q172] Write the general form of user-defined stream manipulators and write a program implementing one (e.g., width 10, right, precision 2, fill *, trailing zeros). :id=q172

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

ostream& manip(ostream& out) { out << setw(10) << right << fixed << setprecision(2) << setfill('*') << showpoint; return out; }

> **🗓️ Asked In Papers:** `2016-06 2(b), 2017-06 3(c)`

### [Q173] What are file stream operations? Write a C++ program demonstrating reading from and writing to a disk file. :id=q173

🔵 **Medium Priority** • **2 (17 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Open file with ofstream, write text, close; open with ifstream, read via getline(), display, close.

> **🗓️ Asked In Papers:** `2014-12 4(b), 2019-12 3(b)`

### [Q174] Explain input and output streams and stream classes in C++ with an example. :id=q174

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

istream (cin), ostream (cout), iostream handle buffered formatted/unformatted data transfer.

> **🗓️ Asked In Papers:** `2013-12 5(b), 2016-06 1(c)`

### [Q175] Differentiate between: (i) ios::ate vs ios::app, (ii) Binary file vs Text file, (iii) get() vs getline(). :id=q175

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

app always writes at EOF; ate seeks to EOF on open (can seek elsewhere). Binary stores raw bytes; Text translates newlines/ASCII. get() leaves delimiter in buffer; getline() discards it.

> **🗓️ Asked In Papers:** `2017-12S 3(a), 2022-06 5(a)`

### [Q176] Explain file pointers and write a C++ program demonstrating put(), get(), read(), and write(). :id=q176

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

put()/get() handle single characters; write((char*)&obj, sizeof(obj)) and read(...) handle raw binary records.

> **🗓️ Asked In Papers:** `2016-06 1(e)`

### [Q177] Explain various file open modes (in, out, app, ate, trunc, binary) and the working of seekg(), seekp(), tellg(), tellp(), read(), and write(). :id=q177

⚪ **Low Priority** • **1 (10 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Detail all 6 ios:: flags, random-access cursor functions, and block binary I/O functions.

> **🗓️ Asked In Papers:** `2024-12 5(a)`

### [Q178] Write a C++ program to copy the contents of one file into another file. :id=q178

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Open source with ifstream and destination with ofstream; loop while(fin.get(ch)) fout.put(ch);; close both

> **🗓️ Asked In Papers:** `2025-12 4(a)`

### [Q179] Explain the use of standard stream objects (cin, cout, cerr, clog) with examples. :id=q179

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

cin (stdin), cout (buffered stdout), cerr (unbuffered stderr), clog (buffered stderr).

> **🗓️ Asked In Papers:** `2019-06 4(b)`

### [Q180] What is a data stream? Explain the stream class hierarchy in C++. :id=q180

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Diagram / Short Answer*

**💡 Key Answer Points:**

ios base → istream, ostream → iostream; file derivatives ifstream, ofstream, fstream.

> **🗓️ Asked In Papers:** `2012-12 4(b)`

### [Q181] Write a C++ program to display a price-list of five vegetables using precision(2). :id=q181

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Arrays of 5 names/prices; cout << fixed << setprecision(2) (or cout.precision(2)) formatting tabular output

> **🗓️ Asked In Papers:** `2015-06 4(b)`

### [Q182] How is unformatted I/O different from formatted I/O? Explain. :id=q182

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Unformatted (get, put, read, write) transfers raw bytes without conversion; formatted (>>, <<, manipulators) parses/formats human-readable text.

> **🗓️ Asked In Papers:** `2016-12 4(a)`

### [Q183] Write a short note on File Stream Operations. :id=q183

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Opening (open()/constructor), checking state (is_open(), eof()), reading/writing, and closing (close()).

> **🗓️ Asked In Papers:** `2021-12 5(a)`

