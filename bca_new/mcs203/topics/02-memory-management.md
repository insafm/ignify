# 02. Memory Management & Virtual Memory

> **Syllabus Units:** Block 2 Units 1 & 2 | **Rank:** #2 | **Frequency Score:** 9.6 | **Offered Marks:** 190 | **Papers Present:** 9/9 | **Importance:** Very High  
> **Coverage:** 13 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q018: Define Segmentation. With the help of an architectural diagram, explain the address translation hardware and protection mechanisms. :id=q018

🔴 **Very High Priority** • **4 (40 marks)** • *Theory / Diagram & Architecture*

**💡 Key Answer Points:**
- **Definition:** Segmentation is a variable-length memory management scheme that mirrors the programmer's view of a program. A logical address space is a collection of named/numbered segments (code, stack, heap, symbol table).
- **Logical Address Tuple:** Represented as $\langle s, d \rangle$, where:
  - $s$ is the **Segment Number** (used as an index into the Segment Table).
  - $d$ is the **Offset** within the segment.
- **Segment Table:** Each entry contains:
  - **Base:** Starting physical memory address of the segment in RAM.
  - **Limit:** Total length/size of the segment.

```
       Logical Address: < s, d >
                         |  |
            +------------+  |
            |               |
            v               |
     +--------------+       |
     | Segment Table|       |
  s: | Limit | Base |       |
     +-------+------+       |
         |      |           |
         |      v           v
         |     [Base] ----> (+) ====> Physical Address
         |                   ^
         v                   |
     [Limit] <---- ( d ) ----+
        |           |
     d < Limit?     |
        |           |
     No | Yes ------+
        v
      TRAP: Addressing Violation
```

- **Hardware Translation Sequence:**
  1. Segment number $s$ indexes the Segment Table to fetch `Limit` and `Base`.
  2. The hardware checks whether offset $d < \text{Limit}$.
  3. If $d \ge \text{Limit}$, an addressing violation trap is generated.
  4. If valid, the physical address is calculated as: $\text{Physical Address} = \text{Base} + d$.

> **🗓️ Asked In Papers:** `June 2022 Q3(a), June 2023 Q1(c), Dec 2024 Q5(b), June 2026 Q1(c)`

---

---

### Q019: Explain Virtual Memory principles, logical-to-physical address translation, memory protection, and page sharing. :id=q019

🔴 **Very High Priority** • **3 (30 marks)** • *Theory / Architecture*

**💡 Key Answer Points:**
- **Principle of Virtual Memory:** Abstracts physical RAM into a massive, contiguous logical address space, allowing processes to execute without being completely loaded in physical RAM.
- **Translation Mechanism:**
  - A logical address is divided into **Page Number ($p$)** and **Page Offset ($d$)**.
  - $p$ indexes into the process's **Page Table** to retrieve **Frame Number ($f$)**.
  - $\text{Physical Address} = (f \times \text{Page Size}) + d$.
- **Protection Bits:** Each Page Table Entry (PTE) contains status bits:
  - `Valid / Invalid (V/I) Bit`: Indicates whether the page is currently in physical RAM.
  - `Read / Write / Execute (R/W/X) Bits`: Enforces memory access permissions.
  - `Dirty / Modified Bit`: Indicates whether the page has been written to, avoiding unnecessary disk writes during page replacement.
- **Page Sharing:** Two or more processes share identical physical frames by mapping entries in their respective page tables to the same frame number $f$ (e.g., shared C standard libraries).

> **🗓️ Asked In Papers:** `Dec 2022 Q1(c), June 2024 Q4(a), Dec 2024 Q4(b)`

---

---

### Q020: Detail the step-by-step sequence of handling a Page Fault in a Demand-Paging system. :id=q020

🔴 **Very High Priority** • **2 (20 marks)** • *Theory / Algorithmic Flow*

**💡 Key Answer Points:**
When a CPU executes an instruction that accesses a page whose Valid/Invalid bit is set to `Invalid` (0), the hardware initiates an 8-step sequence:

```
[1. Memory Access] ---> [2. Page Table: Invalid Bit detected]
                                 │
                                 ▼
                     [3. Trap to OS: Page Fault Exception]
                                 │
                                 ▼
                     [4. OS validates reference & checks disk backing store]
                                 │
                                 ▼
                     [5. OS allocates free frame (or executes page replacement)]
                                 │
                                 ▼
                     [6. Disk I/O scheduled to fetch page into frame]
                                 │
                                 ▼
                     [7. Disk read completes -> Page Table updated (Valid=1)]
                                 │
                                 ▼
                     [8. Context restored -> Instruction restarted]
```

1. **Memory Reference:** The CPU attempts to fetch an operand or instruction from logical address $\langle p, d \rangle$.
2. **Invalid Bit Detection:** The Memory Management Unit (MMU) consults the Page Table and finds the valid/invalid bit is set to `0` (Page Fault).
3. **Hardware Trap:** The MMU generates an internal hardware interrupt (trap) to the operating system kernel.
4. **Validation Check:** The OS intercepts the trap, saves the process CPU registers, and checks the internal PCB to ensure the memory address was a legitimate virtual address.
5. **Frame Allocation:** The OS searches the free-frame list. If no frame is free, a page replacement algorithm (e.g., LRU) selects a victim page, writing it to disk if dirty.
6. **Disk I/O Scheduling:** The OS issues an I/O request to the secondary storage controller to read the missing page into the selected physical frame.
7. **Page Table Update:** Once the I/O interrupt signals completion, the OS updates the Page Table entry with the allocated frame number and flips the status bit to `Valid` (1).
8. **Instruction Restart:** The OS restores saved CPU registers and restarts the exact instruction that triggered the page fault.

> **🗓️ Asked In Papers:** `Dec 2022 Q4(a), June 2024 Q5(b)`

---

---

### Q021: Define Paging. With the help of a diagram, explain address translation hardware and the role of the Translation Lookaside Buffer (TLB). :id=q021

🔴 **Very High Priority** • **1 (10 marks)** • *Theory / Diagram & Architecture*

**💡 Key Answer Points:**
- **Definition:** Paging is a physical memory management scheme that permits a process's physical address space to be non-contiguous, completely eliminating external fragmentation.
- **Hardware Architecture with TLB:** Because page tables reside in main memory, every logical memory reference requires two physical memory accesses (one for the page table, one for the actual data). To mitigate this delay, a high-speed associative hardware cache called the **Translation Lookaside Buffer (TLB)** is utilized.

```
                  Logical Address: < p, d >
                                    |  |
                 +------------------+  |
                 |                     |
                 v                     |
          +--------------+             |
          |  TLB (Cache) |             |
          |  Tag | Frame |             |
          +------+-------+             |
           /            \              |
    TLB Hit               TLB Miss      |
     /                      \          |
    v                        v         |
 [Frame f]             [Page Table]    |
    |                   p: [Frame f]   |
    |                        |         |
    +--------+   +-----------+         |
             |   |                     |
             v   v                     v
          Physical Address:   < f  |  d >
```

- **Effective Access Time (EAT) Calculation:**
  $$\text{EAT} = (h \times (t_{\text{TLB}} + t_{\text{RAM}})) + ((1 - h) \times (t_{\text{TLB}} + 2 \times t_{\text{RAM}}))$$
  where $h$ is the TLB hit ratio, $t_{\text{TLB}}$ is the cache lookup time, and $t_{\text{RAM}}$ is physical memory access latency.

> **🗓️ Asked In Papers:** `June 2025 Q1(b)`

---

---

### Q022: Numerical Simulation — LRU and Optimal Page Replacement on 3 Frames. :id=q022

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Reference String: `1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6`  
Number of Frames: **3 (Initially Empty)**. Calculate page faults for: (i) Least Recently Used (LRU), (ii) Optimal (OPT).

**Step-by-Step Simulation:**

#### (i) Least Recently Used (LRU) Algorithm:
Replaces the page that has not been used for the longest period of time.

| Reference | Frame 1 | Frame 2 | Frame 3 | Fault? | Explanation / Victim Evicted |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **1** | - | - | **Fault (1)** | Empty frame filled |
| **2** | 1 | **2** | - | **Fault (2)** | Empty frame filled |
| **3** | 1 | 2 | **3** | **Fault (3)** | Empty frame filled |
| **4** | **4** | 2 | 3 | **Fault (4)** | Page 1 least recently used -> Evicted |
| **2** | 4 | 2 | 3 | **Hit** | Page 2 already in frame |
| **1** | 4 | 2 | **1** | **Fault (5)** | Page 3 least recently used -> Evicted |
| **5** | **5** | 2 | 1 | **Fault (6)** | Page 4 least recently used -> Evicted |
| **6** | 5 | **6** | 1 | **Fault (7)** | Page 2 least recently used -> Evicted |
| **2** | 5 | 6 | **2** | **Fault (8)** | Page 1 least recently used -> Evicted |
| **1** | **1** | 6 | 2 | **Fault (9)** | Page 5 least recently used -> Evicted |
| **2** | 1 | 6 | 2 | **Hit** | Page 2 already in frame |
| **3** | 1 | **3** | 2 | **Fault (10)** | Page 6 least recently used -> Evicted |
| **7** | **7** | 3 | 2 | **Fault (11)** | Page 1 least recently used -> Evicted |
| **6** | 7 | 3 | **6** | **Fault (12)** | Page 2 least recently used -> Evicted |

- **Total LRU Page Faults:** **12 Faults** (2 Hits out of 14 accesses).

#### (ii) Optimal (OPT) Replacement Algorithm:
Replaces the page that will not be used for the longest period in the future.

| Reference | Frame 1 | Frame 2 | Frame 3 | Fault? | Explanation / Future Horizon |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **1** | - | - | **Fault (1)** | Empty frame |
| **2** | 1 | **2** | - | **Fault (2)** | Empty frame |
| **3** | 1 | 2 | **3** | **Fault (3)** | Empty frame |
| **4** | 1 | 2 | **4** | **Fault (4)** | 1 used at t=6, 2 at t=5, 3 at t=12 -> 3 replaced |
| **2** | 1 | 2 | 4 | **Hit** | Present |
| **1** | 1 | 2 | 4 | **Hit** | Present |
| **5** | 1 | 2 | **5** | **Fault (5)** | 4 never used again -> 4 replaced |
| **6** | 1 | 2 | **6** | **Fault (6)** | 5 never used again -> 5 replaced |
| **2** | 1 | 2 | 6 | **Hit** | Present |
| **1** | 1 | 2 | 6 | **Hit** | Present |
| **2** | 1 | 2 | 6 | **Hit** | Present |
| **3** | **3** | 2 | 6 | **Fault (7)** | 1 never used again -> 1 replaced |
| **7** | 3 | **7** | 6 | **Fault (8)** | 2 never used again -> 2 replaced |
| **6** | 3 | 7 | 6 | **Hit** | Present |

- **Total Optimal Page Faults:** **8 Faults** (6 Hits out of 14 accesses).

> **🗓️ Asked In Papers:** `Dec 2021 Q1(b)`

---

---

### Q023: Numerical Simulation — Optimal and FIFO Page Replacement on 3 Frames. :id=q023

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Reference String: `0, 1, 3, 4, 6, 4, 3, 9, 6, 4`  
Number of Frames: **3 (Initially Empty)**. Calculate page faults for: (i) Optimal Replacement, (ii) First-In First-Out (FIFO).

**Step-by-Step Simulation:**

#### (i) Optimal Replacement (OPT):
- Pages: `0, 1, 3` -> **3 Faults** (Frames: `[0, 1, 3]`).
- Page `4`: Future needs: 0 (never), 1 (never), 3 (at t=7). Replace 0 (or 1) -> Frame: `[4, 1, 3]` -> **Fault (4)**.
- Page `6`: Future needs: 4 (at t=6), 1 (never), 3 (at t=7). Replace 1 -> Frame: `[4, 6, 3]` -> **Fault (5)**.
- Page `4`: Hit (`[4, 6, 3]`).
- Page `3`: Hit (`[4, 6, 3]`).
- Page `9`: Future needs: 4 (at t=10), 6 (at t=9), 3 (never). Replace 3 -> Frame: `[4, 6, 9]` -> **Fault (6)**.
- Page `6`: Hit (`[4, 6, 9]`).
- Page `4`: Hit (`[4, 6, 9]`).
- **Total OPT Faults:** **6 Page Faults** (4 Hits).

#### (ii) First-In First-Out (FIFO):
- `0, 1, 3`: Initial **3 Faults** (`[0, 1, 3]`).
- `4`: Evict oldest (0) -> `[4, 1, 3]` -> **Fault (4)**.
- `6`: Evict oldest (1) -> `[4, 6, 3]` -> **Fault (5)**.
- `4`: Hit (`[4, 6, 3]`).
- `3`: Hit (`[4, 6, 3]`).
- `9`: Evict oldest (3) -> `[4, 6, 9]` -> **Fault (6)**.
- `6`: Hit (`[4, 6, 9]`).
- `4`: Hit (`[4, 6, 9]`).
- **Total FIFO Faults:** **6 Page Faults** (4 Hits).

> **🗓️ Asked In Papers:** `June 2023 Q2(a)`

---

---

### Q024: Numerical Simulation — LRU and FIFO Page Replacement on 3 Frames. :id=q024

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Reference String: `1, 3, 2, 4, 3, 1, 4, 5, 2, 1, 3`  
Number of Frames: **3**. Calculate page faults for: (i) LRU, (ii) FIFO.

**Results Summary:**
- **LRU Simulation:**
  - `1, 3, 2`: 3 Faults (`[1, 3, 2]`)
  - `4`: Evicts 1 -> `[4, 3, 2]` -> Fault (4)
  - `3`: Hit
  - `1`: Evicts 2 -> `[4, 3, 1]` -> Fault (5)
  - `4`: Hit
  - `5`: Evicts 3 -> `[4, 5, 1]` -> Fault (6)
  - `2`: Evicts 1 -> `[4, 5, 2]` -> Fault (7)
  - `1`: Evicts 4 -> `[1, 5, 2]` -> Fault (8)
  - `3`: Evicts 5 -> `[1, 3, 2]` -> Fault (9)
  - **LRU Total:** **9 Page Faults** (2 Hits).
- **FIFO Simulation:**
  - `1, 3, 2`: 3 Faults (`[1, 3, 2]`)
  - `4`: Evicts 1 -> `[4, 3, 2]` -> Fault (4)
  - `3`: Hit
  - `1`: Evicts 3 -> `[4, 1, 2]` -> Fault (5)
  - `4`: Hit
  - `5`: Evicts 2 -> `[4, 1, 5]` -> Fault (6)
  - `2`: Evicts 4 -> `[2, 1, 5]` -> Fault (7)
  - `1`: Hit
  - `3`: Evicts 1 -> `[2, 3, 5]` -> Fault (8)
  - **FIFO Total:** **8 Page Faults** (3 Hits).

> **🗓️ Asked In Papers:** `Dec 2023 Q1(b)`

---

---

### Q025: Numerical Simulation — FIFO, LRU, and LFU Page Replacement on 4 Frames. :id=q025

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Reference String: `1, 2, 5, 4, 2, 1, 3, 2, 6, 4`  
Number of Frames: **4 (Initially Empty)**. Calculate page faults for: (i) FIFO, (ii) LRU, (iii) Least Frequently Used (LFU).

**Simulation Details:**
- **FIFO (4 Frames):**
  - Initial 4 loads: `1, 2, 5, 4` -> **4 Faults** (Queue order: 1, 2, 5, 4).
  - Next accesses: `2` (Hit), `1` (Hit).
  - `3`: Oldest page (1) evicted -> `[3, 2, 5, 4]` -> **Fault (5)**.
  - `2`: Hit.
  - `6`: Oldest page (2) evicted -> `[3, 6, 5, 4]` -> **Fault (6)**.
  - `4`: Hit.
  - **Total FIFO Faults:** **6 Faults**.
- **LRU (4 Frames):**
  - `1, 2, 5, 4` -> **4 Faults** (`[1, 2, 5, 4]`).
  - `2`: Hit. (Recency order: 2, 4, 5, 1).
  - `1`: Hit. (Recency order: 1, 2, 4, 5).
  - `3`: Evicts 5 (least recently used) -> `[1, 2, 3, 4]` -> **Fault (5)**.
  - `2`: Hit.
  - `6`: Evicts 4 -> `[1, 2, 3, 6]` -> **Fault (6)**.
  - `4`: Evicts 1 -> `[4, 2, 3, 6]` -> **Fault (7)**.
  - **Total LRU Faults:** **7 Faults**.
- **LFU (Least Frequently Used):**
  - Maintains reference counts. Pages with the lowest execution frequencies are evicted first, using FIFO as a tie-breaker.
  - **Total LFU Faults:** **6 Faults**.

> **🗓️ Asked In Papers:** `Dec 2024 Q1(d)`

---

---

### Q026: Numerical Simulation — LRU and FIFO on Extended Reference String with 4 Frames. :id=q026

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Step-by-Step Trace*

**Problem Statement:**
Reference String: `1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6` (20 references)  
Number of Frames: **4**. Calculate page faults for: (i) LRU, (ii) FIFO.

- **FIFO Simulation:** Yields **14 Page Faults** (6 hits).
- **LRU Simulation:** Yields **11 Page Faults** (9 hits), demonstrating the efficiency of temporal locality tracking over long access sequences.

> **🗓️ Asked In Papers:** `Dec 2025 Q2(a)`

---

---

### Q027: Numerical Simulation — Contiguous Memory Allocation (First-Fit, Best-Fit, Worst-Fit). :id=q027

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Memory Partitioning*

**Problem Statement:**
Consider six memory partitions of size: $200\text{ kB}, 400\text{ kB}, 600\text{ kB}, 500\text{ kB}, 300\text{ kB}, 250\text{ kB}$ (in that order).  
Four processes arrive with sizes: $357\text{ kB}, 210\text{ kB}, 468\text{ kB}, 491\text{ kB}$ (in that order).  
Perform allocation using: (i) First-fit, (ii) Best-fit, and (iii) Worst-fit.

**Step-by-Step Allocation Traces:**

#### (i) First-Fit Algorithm (Allocates the first hole that is big enough):
- $P_1$ ($357\text{ kB}$): Searches from start: $200$ (no) $\rightarrow$ **$400\text{ kB}$ allocated**. Leftover: $400 - 357 = 43\text{ kB}$.
- $P_2$ ($210\text{ kB}$): Searches from start: $200$ (no) $\rightarrow 43$ (no) $\rightarrow$ **$600\text{ kB}$ allocated**. Leftover: $600 - 210 = 390\text{ kB}$.
- $P_3$ ($468\text{ kB}$): Searches from start: $200$ (no) $\rightarrow 43$ (no) $\rightarrow 390$ (no) $\rightarrow$ **$500\text{ kB}$ allocated**. Leftover: $500 - 468 = 32\text{ kB}$.
- $P_4$ ($491\text{ kB}$): Searches from start: $200, 43, 390, 32, 300, 250$ — **Cannot be allocated** (must wait).

#### (ii) Best-Fit Algorithm (Allocates the smallest hole that is big enough):
Holes available initially: $200, 400, 600, 500, 300, 250\text{ kB}$.
- $P_1$ ($357\text{ kB}$): Best fits in **$400\text{ kB}$**. Leftover: $400 - 357 = 43\text{ kB}$.
- $P_2$ ($210\text{ kB}$): Best fits in **$250\text{ kB}$**. Leftover: $250 - 210 = 40\text{ kB}$.
- $P_3$ ($468\text{ kB}$): Best fits in **$500\text{ kB}$**. Leftover: $500 - 468 = 32\text{ kB}$.
- $P_4$ ($491\text{ kB}$): Best fits in **$600\text{ kB}$**. Leftover: $600 - 491 = 109\text{ kB}$.
- **Outcome:** **All four processes successfully allocated!**

#### (iii) Worst-Fit Algorithm (Allocates the largest available hole):
- $P_1$ ($357\text{ kB}$): Allocated in largest hole (**$600\text{ kB}$**). Leftover: $600 - 357 = 243\text{ kB}$.
- $P_2$ ($210\text{ kB}$): Largest remaining is **$500\text{ kB}$**. Leftover: $500 - 210 = 290\text{ kB}$.
- $P_3$ ($468\text{ kB}$): Largest remaining is $400\text{ kB} \implies$ **Cannot be allocated** (must wait).
- $P_4$ ($491\text{ kB}$): Cannot be allocated (must wait).

**Conclusion:** Best-Fit achieves 100% allocation efficiency, whereas First-Fit and Worst-Fit leave processes waiting.

> **🗓️ Asked In Papers:** `June 2026 Q2(b)`

---

### Q028: Define Thrashing. Explain its causes, consequences, and prevention techniques (Working Set Model and Page Fault Frequency). :id=q028

🟠 **High Priority** • **2 (20 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**
- **Definition:** Thrashing occurs when an operating system spends substantially more time swapping pages in and out of backing store than executing user instructions.
- **Underlying Cause:** Occurs when the sum of the **localities** (working sets) of all active processes exceeds total available physical memory frames:
  $$\sum WSS_i > D > \text{Total Physical Frames}$$
  Processes continuously fault, enter waiting queues for disk I/O, and CPU utilization plummets. In response, a naive OS medium-term scheduler attempts to admit more processes to increase CPU utilization, compounding the catastrophe.
- **Prevention Techniques:**
  1. **Working Set Model:** Introduced by Peter Denning. Monitors the set of pages referenced by a process during the most recent $\Delta$ page references (the Working Set Window). The OS only admits a process if its working set can be completely accommodated in free frames.
  2. **Page Fault Frequency (PFF) Strategy:** Measures the direct rate of page faults. If a process's page-fault rate exceeds an upper threshold, the OS allocates it more frames. If the rate falls below a lower threshold, frames are reclaimed.

> **🗓️ Asked In Papers:** `June 2022 Q4(b), June 2026 Q2(a)`

---

---

### Q029: Define an Overlay with an example and contrast Overlays with Swapping. :id=q029

🟠 **High Priority** • **1 (10 marks)** • *Theory / Comparison*

**💡 Key Answer Points:**
- **Definition of Overlay:** A programming technique that allows a program larger than physical RAM to execute by loading into memory only those instructions and data needed at a given phase. When a new phase is entered, the overlay manager overwrites previous modules in the same memory partition.
- **Classic Example:** A two-pass assembler where Pass 1 (symbol table generation) and Pass 2 (machine code generation) are 80 KB each, running in a 100 KB memory space:
  - Common Driver: 20 KB (Resident in RAM).
  - Overlay Area: 80 KB (Pass 1 loads, executes, terminates; Pass 2 overwrites Pass 1).
- **Contrast with Swapping:**
  - *Overlays:* Managed manually by the programmer / compiler; sub-process granularity; no special OS virtual memory hardware required.
  - *Swapping:* Managed automatically by the operating system kernel; process-level granularity; entire memory spaces are rolled between RAM and swap partition on disk.

> **🗓️ Asked In Papers:** `Dec 2022 Q3(a)`

---

---

### Q030: Define and contrast Segmented Paging and Paged Segmentation. :id=q030

🟡 **Medium Priority** • **1 (10 marks)** • *Theory / Comparison*

**💡 Key Answer Points:**
- **Segmented Paging:** Virtual memory is divided into variable-length logical segments, and each segment is subdivided into fixed-size pages. Address translation uses a two-level indexing hierarchy: Segment Table points to a Page Table, which points to the physical frame.
  - *Advantage:* Combines the logical protection and sharing of segmentation with the elimination of external fragmentation provided by paging.
- **Paged Segmentation:** A massive virtual address space is first partitioned into uniform pages, and these pages are grouped into logical segments.
- **Structural Differences:**
  - *Segmented Paging:* Logical view is primary; segments are paged to simplify memory allocation.
  - *Paged Segmentation:* Hardware paging is primary; segments provide access-control tags over page ranges.

> **🗓️ Asked In Papers:** `Dec 2021 Q2(a)`

---

---

### Q031: Explain the virtual-to-physical address mapping model and the purpose of the Valid/Invalid bit. :id=q031

🟡 **Medium Priority** • **1 (10 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**
- **Mapping Model:** The logical address space is divided into contiguous, equal-sized units called pages. The physical memory is divided into fixed-size frames of the identical size. The Page Table translates the logical page identifier to the physical frame identifier.
- **Valid/Invalid Bit Role:**
  - **Valid (1):** The associated page is legal and currently resident in physical RAM frames. The MMU proceeds with address reconstruction.
  - **Invalid (0):** The page is either not in the process's logical address space (illegal access) or is valid but currently resides on the backing disk storage. Any attempt to access an invalid page immediately fires a page fault exception.

> **🗓️ Asked In Papers:** `Dec 2025 Q3(a)`

---
