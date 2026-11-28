# 07. File and Disk Management

> **Syllabus Unit:** Block 2 Unit 3 | **Rank:** #7 | **Frequency Score:** 5.4 | **Offered Marks:** 85 | **Papers Present:** 6/9 | **Importance:** Medium-High  
> **Coverage:** 7 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q060: Explain file disk space allocation methods: Contiguous Allocation vs. Non-Contiguous Allocation (Linked and Indexed) for effective disk utilization and quick access. :id=q060

🔴 **Very High Priority** • **2 (20 marks)** • *Theory / Storage Allocation*

**💡 Key Answer Points:**
- **Contiguous Allocation:**
  - Requires each file to occupy a set of contiguous blocks on disk. Directory entry stores `Starting Block` and `Length`.
  - *Effective Access:* Best performance for sequential and direct/random access (read head doesn't move between blocks).
  - *Disk Space Utilization:* Very poor; suffers from severe **external fragmentation** and dynamic storage allocation problems (requires disk compaction).
- **Non-Contiguous Allocation — Linked Allocation:**
  - Each file is a linked list of scattered disk blocks. Directory entry stores pointers to the `First Block` and `Last Block`. Each block holds a pointer to the next block.
  - *Disk Space Utilization:* Excellent; zero external fragmentation, any free block can be allocated.
  - *Access Speed:* Inefficient for random access (to read block $i$, must traverse first $i-1$ blocks sequentially).
- **Non-Contiguous Allocation — Indexed Allocation:**
  - Brings all block pointers together into a single dedicated block called the **Index Block**.
  - *Disk Space Utilization:* Eliminates external fragmentation; incurs index block overhead.
  - *Access Speed:* Excellent direct/random access through the index array without sequential pointer chasing.

```
Linked Allocation:
Directory Entry [FileA | Start: 9 | End: 25]
Block 9 [ Data | Ptr: 16 ] -> Block 16 [ Data | Ptr: 25 ] -> Block 25 [ Data | Ptr: -1 ]

Indexed Allocation:
Directory Entry [FileB | Index Block: 19]
Block 19 (Index Block): [ 71 | 14 | 88 | 32 | -1 | -1 ... ]
   │    │    │    │
   ▼    ▼    ▼    ▼
 [Data Data Data Data]
```

**📝 Example PQP Question (June 2026 Q3(b)):**

How to allocate space to files for effective disk space utilization and quick access using the following methods.

(i) Continuous allocation
(ii) Non-continuous allocation *(10 marks)*

> **🗓️ Asked In Papers:** [June 2022 Q4(a)](/bca_new/mcs203/pqp/MCS-203_June_2022.pdf ':ignore'), [June 2026 Q3(b)](/bca_new/mcs203/pqp/MCS-203_June_2026.pdf ':ignore')

---

---

### Q061: Numerical Simulation — SSTF and C-SCAN Disk Scheduling. :id=q061

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Request Sequence: `61, 141, 40, 160, 15, 63, 60, 125`  
Initial Head Position: Cylinder `0`. Assume disk cylinders range from `0 to 199`. Calculate total head movement (in cylinders) for: (i) SSTF, (ii) C-SCAN.

**Step-by-Step Solution:**

#### (i) SSTF Simulation (Starting at 0):
Queue: `15, 40, 60, 61, 63, 125, 141, 160`
1. From 0 $\rightarrow$ closest is **15**: $|15 - 0| = 15$
2. From 15 $\rightarrow$ closest is **40**: $|40 - 15| = 25$
3. From 40 $\rightarrow$ closest is **60**: $|60 - 40| = 20$
4. From 60 $\rightarrow$ closest is **61**: $|61 - 60| = 1$
5. From 61 $\rightarrow$ closest is **63**: $|63 - 61| = 2$
6. From 63 $\rightarrow$ closest is **125**: $|125 - 63| = 62$
7. From 125 $\rightarrow$ closest is **141**: $|141 - 125| = 16$
8. From 141 $\rightarrow$ closest is **160**: $|160 - 141| = 19$

$$\text{Total Head Movement (SSTF)} = 15 + 25 + 20 + 1 + 2 + 62 + 16 + 19 = 160 \text{ cylinders}$$

#### (ii) C-SCAN Simulation (Starting at 0, moving right):
Queue: `15, 40, 60, 61, 63, 125, 141, 160`. Moves right toward 199:
1. Services `15, 40, 60, 61, 63, 125, 141, 160` and moves to disk boundary `199`:
   $$\text{Distance} = 199 - 0 = 199$$
2. Returns from 199 to beginning cylinder `0` (without servicing):
   $$\text{Distance} = 199 - 0 = 199$$
3. (All requests were already serviced in the initial rightward sweep from 0).

$$\text{Total Head Movement (C-SCAN)} = 199 + 199 = 398 \text{ cylinders} \quad (\text{or } 199 \text{ if non-servicing return jump is ignored})$$

**📝 Example PQP Question (June 2023 Q1(b)):**

Using SSTF and C-SCAN disk scheduling algorithms, calculate the total head movement for the following block sequence :

`61, 141, 40, 160, 15, 63, 60, 125`

Note : Initially the head is at cylinder numbered 0. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2023 Q1(b)](/bca_new/mcs203/pqp/MCS-203_June_2023.pdf ':ignore')

---

---

### Q062: Numerical Simulation — SCAN Disk Scheduling. :id=q062

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Request Queue: `47, 38, 121, 191, 87, 11, 92, 10`  
Initial Head Position: Cylinder `63`, moving toward **larger cylinder numbers**. Cylinders numbered `0 to 199`. Calculate total head movement using SCAN.

**Step-by-Step Solution:**
1. Requests larger than 63 in sorted order: `87, 92, 121, 191`
2. Requests smaller than 63 in reverse order: `47, 38, 11, 10`
3. Head starts at 63, moves right servicing:
   $63 \rightarrow 87 \rightarrow 92 \rightarrow 121 \rightarrow 191 \rightarrow 199$ (Disk End)
   $$\text{Seek Distance Right} = 199 - 63 = 136 \text{ cylinders}$$
4. Reverses direction at 199 and moves left servicing:
   $199 \rightarrow 47 \rightarrow 38 \rightarrow 11 \rightarrow 10$
   $$\text{Seek Distance Left} = 199 - 10 = 189 \text{ cylinders}$$

$$\text{Total Head Movement} = (199 - 63) + (199 - 10) = 136 + 189 = 325 \text{ cylinders}$$

**📝 Example PQP Question (Dec 2025 Q3(b)):**

Consider a disk queue with requests for I/O to blocks on cylinders 47, 38, 121, 191, 87, 11, 92, 10. The SCAN scheduling algorithm is used. The head is initially at cylinder number 63, moving towards larger cylinder numbers on its servicing pass. The cylinders are numbered from 0 to 199. Find the total head movement (in number of cylinders) incurred while servicing these requests. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2025 Q3(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2025.pdf ':ignore')

---

---

### Q063: Numerical Simulation — SSTF and SCAN Disk Scheduling. :id=q063

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Request Queue: `49, 90, 149, 41, 129, 17, 139, 69, 60`  
Initial Head Position: Cylinder `49`, moving toward larger cylinders on disk $0–199$.

**Results:**
- **SSTF Trace:** $49 \rightarrow 41 (8) \rightarrow 60 (19) \rightarrow 69 (9) \rightarrow 90 (21) \rightarrow 129 (39) \rightarrow 139 (10) \rightarrow 149 (10) \rightarrow 17 (132) = 248 \text{ cylinders}$.
- **SCAN Trace:** $49 \rightarrow 60 \rightarrow 69 \rightarrow 90 \rightarrow 129 \rightarrow 139 \rightarrow 149 \rightarrow 199 (150) \rightarrow 41 \rightarrow 17 (182) = 332 \text{ cylinders}$.

**📝 Example PQP Question (Dec 2024 Q1(a)):**

Explain the significance of disk scheduling. Discuss the Shortest Seek Time First (SSTF) and SCAN scheduling algorithms. Trace the total head movement with SSTF and SCAN scheduling by representing them through a diagram for the following disk queue :

`49, 90, 149, 41, 129, 17, 139, 69, 60`

Assume that the disk head is initially at 49. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2024 Q1(a)](/bca_new/mcs203/pqp/MCS-203_Dec_2024.pdf ':ignore')

---

### Q064: Explain the mechanics of SCAN and C-SCAN disk scheduling algorithms. :id=q064

🟠 **High Priority** • **2 (20 marks)** • *Theory & Mechanics*

**💡 Key Answer Points:**
- **SCAN (Elevator Algorithm):**
  - The disk arm starts at one end of the disk and moves toward the opposite end, servicing requests in cylinder order until it reaches the final cylinder of the disk platter.
  - Upon reaching the end, the direction of head movement reverses, servicing pending requests on the return sweep.
  - *Characteristics:* Prevents starvation, but requests at the far end wait longer if the arm just reversed.
- **C-SCAN (Circular SCAN):**
  - Designed to provide more uniform waiting times.
  - Services requests in one direction only (e.g., from cylinder 0 to cylinder $MAX$).
  - When the arm reaches the end, it immediately reverses and sweeps back to the beginning of the disk without servicing any I/O requests along the return path.
  - *Characteristics:* Treats cylinders as a circular list, eliminating the bias towards edge tracks.

**📝 Example PQP Question (Dec 2021 Q1(a)):**

Discuss SCAN and C-SCAN disk scheduling algorithms. List the advantages of SCAN over C-SCAN algorithm. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2021 Q4(a)](/bca_new/mcs203/pqp/MCS-203_Dec_2021.pdf ':ignore'), [June 2023 Q1(b)](/bca_new/mcs203/pqp/MCS-203_June_2023.pdf ':ignore')

---

---

### Q065: Define Disk Scheduling and explain FCFS and Shortest Seek Time First (SSTF) scheduling. :id=q065

🟠 **High Priority** • **1 (10 marks)** • *Theory / Scheduling*

**💡 Key Answer Points:**
- **Definition:** Disk scheduling algorithms re-order pending disk I/O requests to minimize total disk arm seek time (the time taken for the physical read/write head to position itself over the target cylinder).
- **First-Come First-Served (FCFS):**
  - Services I/O requests in strict arrival order.
  - *Merits:* Fair, starvation-free, simple queue management.
  - *Demerits:* Wildly inefficient; produces erratic head movement across platter tracks.
- **Shortest Seek Time First (SSTF):**
  - Selects the request with the minimum seek distance from the current head position:
    $$\min(|\text{Target Cylinder} - \text{Current Head Position}|)$$
  - *Merits:* Significantly reduces total head movement compared to FCFS.
  - *Demerits:* Can lead to **starvation** of requests on outer or inner tracks if a continuous stream of requests clusters around the current head position.

**📝 Example PQP Question (Dec 2022 Q4(b)):**

What is Disk Scheduling ? With the help of an example for each, explain the following disk scheduling algorithms :

(i) FCFS
(ii) SSTF *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2022 Q4(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2022.pdf ':ignore')

---

---

### Q066: Explain Hierarchical Directory Structures: Two-Level, Tree, Acyclic Graph, and General Graph. :id=q066

🟠 **High Priority** • **1 (10 marks)** • *Theory / File Systems*

**💡 Key Answer Points:**
1. **Two-Level Directory:**
   - Master File Directory (MFD) indexes individual User File Directories (UFD).
   - Solves naming collisions between different users; however, users cannot group files into sub-directories.
2. **Tree-Structured Directory:**
   - Directories can contain both files and sub-directories of arbitrary depth.
   - Provides absolute and relative path names (`/home/user/project/file.c`). Guarantees no cycles.
3. **Acyclic-Graph Directory:**
   - Permits directories to share subdirectories and files using hard/symbolic links.
   - Requires reference counting to prevent dangling pointers when a shared file is deleted.
4. **General Graph Directory:**
   - Allows cycles in the directory graph (e.g., links pointing back to ancestor folders).
   - *Challenge:* Traversing directories can trigger infinite loops. Requires garbage collection (mark-and-sweep) to reclaim unreferenced cyclic storage.

**📝 Example PQP Question (June 2025 Q2(b)):**

Describe the operating system’s view of file management. In this context, explain two-level directory structure, acyclic-graph directory structure and general graph directory structure. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2025 Q2(a)](/bca_new/mcs203/pqp/MCS-203_June_2025.pdf ':ignore')

---
