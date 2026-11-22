# 🗂️ Master Question Bank by Topic Modules (MCS-203)

> **Curriculum & Exam Coverage:** Across 10 previous-year IGNOU Term-End Examination papers (December 2021 – June 2026), 125 raw question items deduplicate into **80 unique canonical questions**. All 80 questions are organized, priority-tagged, and answered with canonical notes inside the **9 topic modules** below.

---

## 🏆 Topic Modules by Priority & Exam Weightage

### 🔴 Tier 1: Mandatory Mastery (Very High Priority • 53% of Total Exam Marks)

Mastering these three modules covers the vast majority of compulsory Question 1 and high-scoring 10-mark questions across all 10 exam sessions:

#### [Module 01: Case Study – Mobile Operating Systems (Android & iOS)](/bca_new/mcs203/topics/01-mobile-os.md)
* **Syllabus Units:** Block 3 Unit 3 & Block 4 Units 3–4
* **Historical Weight:** **235 Marks** (Offered in 10 of 10 papers) • **Rank #1** • Frequency Score: **13.2**
* **Canonical Questions:** **17 Unique Questions** (Q001 – Q017)
* **Core Themes Covered:**
  * iOS 4-layer architecture stack (Cocoa Touch, Media, Core Services, Core OS)
  * iOS sandboxed directory structure (`Documents/`, `Library/`, `tmp/`, `AppName.app`, iCloud Container)
  * Android layered architecture (Linux Kernel, HAL, ART/Libraries, Framework, Applications)
  * Android Process Lifecycle (Foreground, Visible, Service, Background, Empty) & Low Memory Killer (LMK)
  * Mobile communication (Binder IPC, Intents, Infrared, Bluetooth, NFC 2-unit communications)
  * Comparative analysis: Symbian vs. Android, KaiOS architecture, Qualcomm Snapdragon vs. Intel Atom
  * General design issues and hardware constraints in mobile operating systems

#### [Module 02: Memory Management & Virtual Memory](/bca_new/mcs203/topics/02-memory-management.md)
* **Syllabus Units:** Block 2 Units 1–2
* **Historical Weight:** **220 Marks** (Offered in 10 of 10 papers) • **Rank #2** • Frequency Score: **12.0**
* **Canonical Questions:** **14 Unique Questions** (Q018 – Q030A)
* **Core Themes Covered:**
  * Segmentation address translation hardware diagram ($\langle s, d \rangle$, Segment Table, Base/Limit)
  * Paging hardware, PTBR, and Translation Lookaside Buffer (TLB) acceleration
  * Contiguous partition allocation algorithms: First-Fit, Best-Fit, Worst-Fit simulations
  * Virtual memory model, protection, sharing, and Valid/Invalid bit
  * Demand paging and the step-by-step 8-stage page fault handling sequence
  * Thrashing causes, detection, Working Set Model, and Page Fault Frequency (PFF) strategy
  * Dynamic page replacement numerical simulations (FIFO, LRU, OPT, LFU) with frame trace tables

#### [Module 03: Advanced OS – Multiprocessor & Distributed Systems](/bca_new/mcs203/topics/03-multiprocessor-distributed.md)
* **Syllabus Units:** Block 3 Units 1–2
* **Historical Weight:** **180 Marks** (Offered in 9 of 10 papers) • **Rank #3** • Frequency Score: **8.6**
* **Canonical Questions:** **10 Unique Questions** (Q031 – Q039, Q032A)
* **Core Themes Covered:**
  * Distributed system design challenges (heterogeneity, openness, security, scalability, failure handling)
  * Lamport's Logical Clocks scheme and the happens-before ($\rightarrow$) relation
  * Distributed mutual exclusion algorithms: Ricart-Agrawala ($2(N-1)$ messages) and Lamport DME ($3(N-1)$ messages)
  * Distributed Shared Memory (DSM) application model, page replication, and coherence
  * Multiprocessor OS functions and configurations (Master-Slave, Separate Supervisor, SMP)
  * Low-level hardware synchronization primitives (Test-and-Set, Compare-and-Swap, Fetch-and-Add)
  * Remote Procedure Call (RPC) architecture, stubs, data marshaling, and limitations

---

### 🟠 Tier 2: High Scoring Core Modules (High Priority • Regular 10-Mark Anchors)

#### [Module 04: Process Synchronization & Mutual Exclusion](/bca_new/mcs203/topics/04-process-synchronization.md)
* **Syllabus Unit:** Block 1 Unit 3
* **Historical Weight:** **135 Marks** (Offered in 8 of 10 papers) • **Rank #4** • Frequency Score: **7.6**
* **Canonical Questions:** **7 Unique Questions** (Q040 – Q046)
* **Core Themes Covered:**
  * Semaphores and atomic primitives (`wait()` and `signal()`)
  * Bounded-Buffer Producer-Consumer complete algorithmic implementation
  * Software-based mutual exclusion: Dekker's algorithm (2 processes) and Lamport's Bakery algorithm ($n$ processes)
  * Classical coordination problems: Readers-Writers database problem and Dining Philosophers
  * Sleeping Barber synchronization algorithm
  * Spinlocks vs. Sleep Mutexes and thread-level locking mechanisms

#### [Module 05: Case Study – Linux Architecture & System Security](/bca_new/mcs203/topics/05-linux-case-study.md)
* **Syllabus Unit:** Block 4 Unit 2
* **Historical Weight:** **125 Marks** (Offered in 9 of 10 papers) • **Rank #5** • Frequency Score: **6.8**
* **Canonical Questions:** **5 Unique Questions** (Q047 – Q050A)
* **Core Themes Covered:**
  * Linux monolithic kernel architecture diagram (SCI, VFS, Memory Manager, CFS Scheduler, Drivers)
  * Process management, states, priorities, and `clone()` task creation
  * Linux virtual memory mapping, page tables, swapping, page cache, and buddy system allocator
  * Multi-layered Linux security model (User Accounts, POSIX permissions, SHA-256 integrity, LUKS, SSH)
  * Access Matrix Security Model (domains, objects, rights, ACLs vs. Capability lists)

#### [Module 06: Deadlocks](/bca_new/mcs203/topics/06-deadlocks.md)
* **Syllabus Unit:** Block 1 Unit 4
* **Historical Weight:** **105 Marks** (Offered in 8 of 10 papers) • **Rank #6** • Frequency Score: **6.4**
* **Canonical Questions:** **6 Unique Questions** (Q051 – Q055, Q054A)
* **Core Themes Covered:**
  * Deadlock definition and the 4 Coffman necessary conditions
  * Havender's deadlock prevention rules and elimination protocols
  * Dijkstra's Banker's Algorithm for deadlock avoidance (Safety Algorithm and matrices)
  * Resource Allocation Graphs (RAG), request/assignment edges, and multi-instance cycle evaluation
  * Deadlock detection via Wait-For Graphs and recovery mechanisms (preemption vs. process termination)

---

### 🟡 Tier 3: Specialized & Platform Modules (Medium Priority)

#### [Module 07: File Systems & Disk Management](/bca_new/mcs203/topics/07-file-disk-management.md)
* **Syllabus Unit:** Block 2 Unit 3
* **Historical Weight:** **95 Marks** (Offered in 7 of 10 papers) • **Rank #7** • Frequency Score: **5.8**
* **Canonical Questions:** **7 Unique Questions** (Q056 – Q062)
* **Core Themes Covered:**
  * Disk space allocation methods: Contiguous Allocation vs. Non-Contiguous Allocation (Linked & Indexed)
  * Disk scheduling algorithms: FCFS, SSTF, SCAN (Elevator), and C-SCAN (Circular SCAN)
  * Numerical seek distance simulations and cylinder head motion traces
  * Hierarchical directory structures: Two-Level, Tree, Acyclic-Graph, and General Graph directories

#### [Module 08: Process Management & CPU Scheduling](/bca_new/mcs203/topics/08-process-cpu-scheduling.md)
* **Syllabus Units:** Block 1 Units 1–2
* **Historical Weight:** **95 Marks** (Offered in 7 of 10 papers) • **Rank #8** • Frequency Score: **5.6**
* **Canonical Questions:** **9 Unique Questions** (Q063 – Q070, Q069A)
* **Core Themes Covered:**
  * Process Control Block (PCB) fields and execution contexts
  * Schedulers hierarchy: Long-Term, Medium-Term, and Short-Term schedulers
  * CPU-bound vs. I/O-bound load profiles and OS process management duties
  * Multiprogramming operating systems: Batch, Interactive, Time-Sharing, Real-Time, Distributed
  * CPU scheduling algorithms comparison (FCFS, Round Robin, Priority, Starvation, Aging)
  * Numerical CPU scheduling simulations (Gantt charts, Turnaround Time, Waiting Time, SRTN, RR $q=2$)

#### [Module 09: Case Study – Windows 10 Architecture](/bca_new/mcs203/topics/09-windows10-case-study.md)
* **Syllabus Unit:** Block 4 Unit 1
* **Historical Weight:** **70 Marks** (Offered in 6 of 10 papers) • **Rank #9** • Frequency Score: **5.2**
* **Canonical Questions:** **5 Unique Questions** (Q071 – Q075)
* **Core Themes Covered:**
  * Windows 10 Virtual Memory 64-bit flat logical address space and Demand Paging
  * Windows 10 Memory Compression architecture and compressed memory store in RAM
  * NTFS file system architecture, Master File Table (MFT), and Journaling (Transaction Logging)
  * Windows 10 preemptive, dynamic priority thread scheduling
  * Windows 10 Inter-Process Communication (LPC, Named Pipes, Mailslots, COM, Shared Memory)
  * Windows 10 vs. Linux Operating System comprehensive architectural comparison
