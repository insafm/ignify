# 🖥️ MCS-203: Operating Systems

> **Programme:** IGNOU BCA_NEW (Semester 2) / PGDCA-NEW | **Course Code:** MCS-203 | **Credits:** 4 Credits  
> **Evaluation Pattern:** 30% Continuous Assessment (Assignments) + 70% Term-End Examination (TEE) • Separate minimum 40% passing standard required.

---

## 🎯 Course Curriculum & Syllabus Structure

As established in the official IGNOU eGyanKosh curriculum for **MCS-203: Operating Systems**, the course comprises **4 Blocks and 15 Units**:

### 📦 Block 1: Introduction to Operating Systems and Process Management
- **Unit 1: Operating System: An Overview** — Goals, functions, generations, structures, batch, interactive, time-sharing, real-time, distributed systems ([Module 8: Process & CPU Scheduling](/bca_new/mcs203/topics/08-process-cpu-scheduling.md)).
- **Unit 2: Processes** — Process concepts, states, PCB, context switching, CPU scheduling algorithms (FCFS, SJF, SRTN, RR, Priority) ([Module 8: Process & CPU Scheduling](/bca_new/mcs203/topics/08-process-cpu-scheduling.md)).
- **Unit 3: Interprocess Communication and Synchronization** — Concurrency, race conditions, critical sections, semaphores, Dekker's, Bakery, Producer-Consumer, Readers-Writers, Dining Philosophers ([Module 4: Process Synchronization](/bca_new/mcs203/topics/04-process-synchronization.md)).
- **Unit 4: Deadlocks** — System model, Coffman conditions, RAG, prevention (Havender's rules), avoidance (Banker's algorithm), detection and recovery ([Module 6: Deadlocks](/bca_new/mcs203/topics/06-deadlocks.md)).

### 📦 Block 2: Memory Management, File Management and Security
- **Unit 1: Memory Management** — Contiguous partition allocation (First-Fit, Best-Fit, Worst-Fit), swapping, overlays, paging hardware, segmentation, address translation, TLB ([Module 2: Memory Management](/bca_new/mcs203/topics/02-memory-management.md)).
- **Unit 2: Virtual Memory** — Demand paging, page fault handling, page replacement (FIFO, LRU, OPT, LFU), thrashing, working set model ([Module 2: Memory Management](/bca_new/mcs203/topics/02-memory-management.md)).
- **Unit 3: I/O and File Management** — File directory structures (two-level, acyclic graph, general graph), allocation methods (continuous, linked, indexed), disk scheduling (FCFS, SSTF, SCAN, C-SCAN) ([Module 7: File & Disk Management](/bca_new/mcs203/topics/07-file-disk-management.md)).
- **Unit 4: Security and Protection** — Security goals, threats, Access Control Matrix (ACM), DAC/MAC, rule-based vs. role-based access control ([Module 5: Linux Case Study](/bca_new/mcs203/topics/05-linux-case-study.md)).

### 📦 Block 3: Advanced Topics in Operating Systems
- **Unit 1: Multiprocessor Systems** — Multiprocessor OS configurations (Master-Slave, Separate Supervisor, SMP), hardware synchronization primitives (Test-and-Set, Compare-and-Swap, Fetch-and-Add) ([Module 3: Multiprocessor & Distributed](/bca_new/mcs203/topics/03-multiprocessor-distributed.md)).
- **Unit 2: Distributed Operating Systems** — Design issues, Lamport logical clocks, happens-before relation, distributed mutual exclusion (Ricart-Agrawala, Lamport DME), RPC, Distributed Shared Memory (DSM) ([Module 3: Multiprocessor & Distributed](/bca_new/mcs203/topics/03-multiprocessor-distributed.md)).
- **Unit 3: Mobile Operating Systems** — Mobile constraints, wireless communication (IR, Bluetooth, NFC), Symbian, KaiOS, Qualcomm Snapdragon vs. Intel Atom architectures ([Module 1: Mobile OS](/bca_new/mcs203/topics/01-mobile-os.md)).

### 📦 Block 4: Case Studies
- **Unit 1: Case Study 1 – Windows 10** — Virtual memory, demand paging, memory compression, NTFS file system, MFT, journaling, IPC, Windows 10 vs. Linux comparison ([Module 9: Windows 10 Case Study](/bca_new/mcs203/topics/09-windows10-case-study.md)).
- **Unit 2: Case Study 2 – Linux** — Monolithic kernel, CFS scheduler, process states, clone(), virtual memory mapping, buddy system, multi-layered security model ([Module 5: Linux Case Study](/bca_new/mcs203/topics/05-linux-case-study.md)).
- **Unit 3: Case Study 3 – Android** — Layered architecture (Linux kernel, HAL, ART/libraries, framework, apps), process lifecycle states, Binder IPC, security sandbox ([Module 1: Mobile OS](/bca_new/mcs203/topics/01-mobile-os.md)).
- **Unit 4: Case Study 4 – iOS** — Layered SDK architecture (Cocoa Touch, Media, Core Services, Core OS), sandboxed directory layout, Secure Enclave ([Module 1: Mobile OS](/bca_new/mcs203/topics/01-mobile-os.md)).

---

## 🚨 Examination Pattern & Scoring Strategy

> **Examination Blueprint:**
> - **Time Allowed:** 3 Hours | **Maximum Marks:** 100 | **Weightage:** 70%
> - **Structure:** **Question 1 is COMPULSORY (40 Marks)**, consisting of four 10-mark multi-part questions covering CPU scheduling, memory management, deadlocks, and OS case studies.
> - **Elective Section:** Attempt any **3 out of Questions 2 to 5 (20 Marks each = 60 Marks)**.
> - **Total Marks Offered in Question Paper:** 120 Marks.

### 💡 The 70-Mark Rule for Scoring Distinction
Historical analysis across all 10 TEE papers (Dec 2021 – Jun 2026) reveals that scoring 70%+ in MCS-203 requires mastering three high-yield zones:
1. **Algorithmic Numericals (30 Marks):** Disk scheduling (SSTF/SCAN/C-SCAN), Page Replacement (LRU/OPT/FIFO), Memory Partition Allocation (First-Fit, Best-Fit, Worst-Fit), Resource Allocation Graphs, and CPU Scheduling (FCFS/SJF/SRTN/RR).
2. **Platform Case Studies (30 Marks):** Linux security model, iOS layered architecture, Android runtime/stack, and Windows 10 virtual memory/NTFS journaling.
3. **Core Synchronization & Deadlocks (25 Marks):** Coffman conditions, Havender's rules, Banker's algorithm, and semaphore algorithms (Producer-Consumer, Dining Philosophers).

---

## 🧭 Analytical Resources

| Resource | Scope | Focus |
| :--- | :--- | :--- |
| **[📑 Question Papers Archive (10 PDFs)](/bca_new/mcs203/papers.md)** | All 10 TEE papers | Original question paper PDFs (Dec 2021 – Jun 2026) in `/pqp/` |
| **[📊 10-Paper Comprehensive Analysis](/bca_new/mcs203/analysis.md)** | All 10 TEE papers | Mathematical topic rankings, frequency score formula & macro trends |
| **[🎯 High-Probability Predictions](/bca_new/mcs203/predictions.md)** | Top 12 Target questions | Gap analysis, 10-mark expected questions & high-yield topics |
| **[⚖️ Most Repeated Comparison Questions](/bca_new/mcs203/comparisons.md)** | 14 Repeated pairs | Comprehensive difference tables (Segmentation vs. Paging, Windows 10 vs. Linux, etc.) |
| **[🗂️ Master Question Bank (Q001–Q075)](/bca_new/mcs203/questions.md)** | All 75 Questions | Deduplicated canonical question repository organized into 3 priority tiers |
