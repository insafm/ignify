# 08. Streams, Manipulators & File Handling

> **Syllabus Unit:** Block 3 Unit 1 | **Rank:** #8 | **Frequency Score:** 68.0 | **Offered Marks:** 260 | **Papers Present:** 24/30 | **Importance:** Medium-High
> **Coverage:** 17 canonical questions from 30 TEE papers (Dec 2012 – Jun 2026), ranked by historical frequency.

---

## ❓ Question Bank & Canonical Answers

### Q167: What is a stream manipulator? Explain the use of setw() and setprecision() with examples. :id=q167

🔴 **Very High Priority** • **6 (31 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

<iomanip> functions formatting I/O streams; setw(n) sets minimum field width for next output; setprecision(k) sets significant/decimal digits.

**📝 Example PQP Question (2025-06 2(a)):**

What are stream manipulators ? Explain the use of setw() and setprecision() as a stream manipulation. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2014-06 3(c)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2019-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore'), [2020-06 1(f)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2022-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-06 2(a)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q168: Write a C++ program (with comments) to open an existing file and append "My C++ File" / "File program in C++" at the end. :id=q168

🟠 **High Priority** • **5 (50 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

ofstream fout("file.txt", ios::app); check if(!fout) error, write string, fout.close();.

**📝 Example PQP Question (2025-06 4(a)):**

Write a program in C++ to open an existing file and insert the text "file program in C++" at the end of the file. *(10 marks)*

> **🗓️ Asked In Papers:** [2013-06 3(a)](/bca_new/bcs131/pqp/BCS-031_June_2013.pdf ':ignore'), [2017-12S 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2020-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2020.pdf ':ignore'), [2022-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2025-06 4(a)](/bca_new/bcs131/pqp/BCS-031_June_2025.pdf ':ignore')

### Q169: What are stream manipulators? Briefly discuss the purpose of various stream manipulators (explain any two). :id=q169

🟠 **High Priority** • **5 (29 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Format output/input inline (endl, setw, setprecision, fixed, left, right, setfill).

**📝 Example PQP Question (2026-06 5(a)):**

What are stream manipulators ? Explain any two stream manipulators in C++. *(10 marks)*

> **🗓️ Asked In Papers:** [2019-12 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore'), [2020-12 5(iii)](/bca_new/bcs131/pqp/BCS-031_Dec_2020.pdf ':ignore'), [2021-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2021.pdf ':ignore'), [2023-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2023_Set-1.pdf ':ignore'), [2026-06 5(a)](/bca_new/bcs131/pqp/BCS-131-BLS-031.pdf ':ignore')

### Q170: What is a stream in C++? Name the stream classes generally used for file I/O and explain their utility. :id=q170

🟠 **High Priority** • **4 (21 marks)** • *Theory / Short Answer & Long Answer*

**💡 Key Answer Points:**

Abstraction of byte flow; <fstream> classes: ifstream (read), ofstream (write), fstream (read+write), filebuf.

**📝 Example PQP Question (2025-12 2(d)):**

What is a stream in C++ ? Name the streams generally used for file I/O. *(5 marks)*

> **🗓️ Asked In Papers:** [2017-12S 3(c)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2022-06 5(b)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore'), [2024-06 4(d)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore'), [2025-12 2(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q171: Explain file pointers (get and put pointers) and operations (seekg(), seekp(), tellg(), tellp()). :id=q171

🟠 **High Priority** • **3 (15 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

seekg/tellg reposition/query input cursor; seekp/tellp reposition/query output cursor using ios::beg, ios::cur, ios::end.

**📝 Example PQP Question (2024-06 1(g)):**

Explain seekg( ), seekp( ), tellg( ), tellp( ) functions of stream classes. *(5 marks)*

> **🗓️ Asked In Papers:** [2014-06 5(d)](/bca_new/bcs131/pqp/BCS-031_June_2014.pdf ':ignore'), [2018-12S 5(d)](/bca_new/bcs131/pqp/BCS-031_Dec_2018.pdf ':ignore'), [2024-06 1(g)](/bca_new/bcs131/pqp/BCS-031_June_2024.pdf ':ignore')

### Q172: Write the general form of user-defined stream manipulators and write a program implementing one (e.g., width 10, right, precision 2, fill *, trailing zeros). :id=q172

🔵 **Medium Priority** • **2 (20 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

ostream& manip(ostream& out) { out << setw(10) << right << fixed << setprecision(2) << setfill('*') << showpoint; return out; }

**📝 Example PQP Question (2017-06 3(c)):**

Write the general form of the user-defined manipulators. Design a single manipulator format to provide the following output specifications for printing float values :
(i) 10 column width
(ii) Right Justified
(iii) Two-digit precision
(iv) Filling of unused places with *
(v) Trailing zeroes shown *(10 marks)*

> **🗓️ Asked In Papers:** [2016-06 2(b)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore'), [2017-06 3(c)](/bca_new/bcs131/pqp/BCS-031_June_2017.pdf ':ignore')

### Q173: What are file stream operations? Write a C++ program demonstrating reading from and writing to a disk file. :id=q173

🔵 **Medium Priority** • **2 (17 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

Open file with ofstream, write text, close; open with ifstream, read via getline(), display, close.

**📝 Example PQP Question (2019-12 3(b)):**

What are File stream operations? Write a program in C++ to demonstrate the file reading and writing operations. *(10 marks)*

> **🗓️ Asked In Papers:** [2014-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2014.pdf ':ignore'), [2019-12 3(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2019.pdf ':ignore')

### Q174: Explain input and output streams and stream classes in C++ with an example. :id=q174

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

istream (cin), ostream (cout), iostream handle buffered formatted/unformatted data transfer.

**📝 Example PQP Question (2016-06 1(c)):**

Explain C++ streams and stream classes with an example. *(5 marks)*

> **🗓️ Asked In Papers:** [2013-12 5(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2013.pdf ':ignore'), [2016-06 1(c)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore')

### Q175: Differentiate between: (i) ios::ate vs ios::app, (ii) Binary file vs Text file, (iii) get() vs getline(). :id=q175

🔵 **Medium Priority** • **2 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

app always writes at EOF; ate seeks to EOF on open (can seek elsewhere). Binary stores raw bytes; Text translates newlines/ASCII. get() leaves delimiter in buffer; getline() discards it.

**📝 Example PQP Question (2022-06 5(a)):**

Differentiate between the following :
(i) Binary file and Text file
(ii) get( ) and getline( ) *(5 marks)*

> **🗓️ Asked In Papers:** [2017-12S 3(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2017_Set-2.pdf ':ignore'), [2022-06 5(a)](/bca_new/bcs131/pqp/BCS-031_June_2022.pdf ':ignore')

### Q176: Explain file pointers and write a C++ program demonstrating put(), get(), read(), and write(). :id=q176

⚪ **Low Priority** • **1 (10 marks)** • *Theory + Coding / Long Answer*

**💡 Key Answer Points:**

put()/get() handle single characters; write((char*)&obj, sizeof(obj)) and read(...) handle raw binary records.

**📝 Example PQP Question (2016-06 1(e)):**

Explain file pointers and operations. Write a C++ program which demonstrates the use of put( ) — get( ) and read( ) — write( ). *(10 marks)*

> **🗓️ Asked In Papers:** [2016-06 1(e)](/bca_new/bcs131/pqp/BCS-031_June_2016.pdf ':ignore')

### Q177: Explain various file open modes (in, out, app, ate, trunc, binary) and the working of seekg(), seekp(), tellg(), tellp(), read(), and write(). :id=q177

⚪ **Low Priority** • **1 (10 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

Detail all 6 ios:: flags, random-access cursor functions, and block binary I/O functions.

**📝 Example PQP Question (2024-12 5(a)):**

Explain various modes in which a file can be opened. Explain the working of seekg( ), seekp( ), tellg( ), tellp( ), read( ), write( ) functions in istream classes. *(10 marks)*

> **🗓️ Asked In Papers:** [2024-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2024.pdf ':ignore')

### Q178: Write a C++ program to copy the contents of one file into another file. :id=q178

⚪ **Low Priority** • **1 (10 marks)** • *Coding / Long Answer*

**💡 Key Answer Points:**

Open source with ifstream and destination with ofstream; loop while(fin.get(ch)) fout.put(ch);; close both

**📝 Example PQP Question (2025-12 4(a)):**

Write a program in C++ to copy the contents of one file into other file. *(10 marks)*

> **🗓️ Asked In Papers:** [2025-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2025.pdf ':ignore')

### Q179: Explain the use of standard stream objects (cin, cout, cerr, clog) with examples. :id=q179

⚪ **Low Priority** • **1 (8 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**

cin (stdin), cout (buffered stdout), cerr (unbuffered stderr), clog (buffered stderr).

**📝 Example PQP Question (2019-06 4(b)):**

Explain the use of the following standard stream objects with the help of examples :
(i) cin
(ii) cout
(iii) cerr
(iv) clog *(8 marks)*

> **🗓️ Asked In Papers:** [2019-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2019.pdf ':ignore')

### Q180: What is a data stream? Explain the stream class hierarchy in C++. :id=q180

⚪ **Low Priority** • **1 (5 marks)** • *Theory + Diagram / Short Answer*

**💡 Key Answer Points:**

ios base → istream, ostream → iostream; file derivatives ifstream, ofstream, fstream.

**📝 Example PQP Question (2012-12 4(b)):**

What is data stream ? Explain stream hierarchy in C++. *(5 marks)*

> **🗓️ Asked In Papers:** [2012-12 4(b)](/bca_new/bcs131/pqp/BCS-031_Dec_2012.pdf ':ignore')

### Q181: Write a C++ program to display a price-list of five vegetables using precision(2). :id=q181

⚪ **Low Priority** • **1 (5 marks)** • *Coding / Short Answer*

**💡 Key Answer Points:**

Arrays of 5 names/prices; cout << fixed << setprecision(2) (or cout.precision(2)) formatting tabular output

**📝 Example PQP Question (2015-06 4(b)):**

Write a C++ program to display the price-list of five vegetables. Use precision( ) function to set precision 2 for display price. *(5 marks)*

> **🗓️ Asked In Papers:** [2015-06 4(b)](/bca_new/bcs131/pqp/BCS-031_June_2015.pdf ':ignore')

### Q182: How is unformatted I/O different from formatted I/O? Explain. :id=q182

⚪ **Low Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Unformatted (get, put, read, write) transfers raw bytes without conversion; formatted (>>, <<, manipulators) parses/formats human-readable text.

**📝 Example PQP Question (2016-12 4(a)):**

How is unformatted I/O different from formatted I/O ? Explain. *(5 marks)*

> **🗓️ Asked In Papers:** [2016-12 4(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2016.pdf ':ignore')

### Q183: Write a short note on File Stream Operations. :id=q183

⚪ **Low Priority** • **1 (4 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**

Opening (open()/constructor), checking state (is_open(), eof()), reading/writing, and closing (close()).

**📝 Example PQP Question (2021-12 5(a)):**

Write short notes on the following: File Stream Operations *(4 marks)*

> **🗓️ Asked In Papers:** [2021-12 5(a)](/bca_new/bcs131/pqp/BCS-031_Dec_2021.pdf ':ignore')

