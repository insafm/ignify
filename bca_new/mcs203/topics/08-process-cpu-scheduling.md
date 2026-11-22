# 08. Process Management & CPU Scheduling

> **Syllabus Units:** Block 1 Units 1 & 2 | **Rank:** #8 | **Frequency Score:** 5.0 | **Offered Marks:** 75 | **Papers Present:** 6/9 | **Importance:** Medium  
> **Coverage:** 8 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q067: Numerical Simulation — CPU Scheduling for Five Simultaneous Processes. :id=q067

🔴 **Very High Priority** • **2 (20 marks)** • *Numerical / Gantt Chart*

**Problem Statement:**
Processes arriving at $t = 0$: $P_1 = 7, P_2 = 6, P_3 = 9, P_4 = 4, P_5 = 3$ ms.  
Simulate FCFS, SJF, and Round Robin ($q = 2$).

- **SJF Order:** $P_5(3) \rightarrow P_4(4) \rightarrow P_2(6) \rightarrow P_1(7) \rightarrow P_3(9)$
- Completion Times: $P_5 = 3, P_4 = 7, P_2 = 13, P_1 = 20, P_3 = 29$
- Waiting Times: $P_5 = 0, P_4 = 3, P_2 = 7, P_1 = 13, P_3 = 20$
- **Average Waiting Time (SJF):** $(0 + 3 + 7 + 13 + 20) / 5 = 43 / 5 = 8.6 \text{ ms}$.

> **🗓️ Asked In Papers:** `June 2025 Q1(a), June 2026 Q1(a)`

---

---

### Q068: Numerical Simulation — FCFS, SJF, and Round Robin Scheduling (Simultaneous Arrival). :id=q068

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Gantt Chart*

**Problem Statement:**
Processes arriving simultaneously at time $t = 0$:  
$P_1 = 10$ ms, $P_2 = 8$ ms, $P_3 = 4$ ms, $P_4 = 6$ ms.  
Draw Gantt charts and compute average Turnaround Time ($TAT$) and Waiting Time ($WT$) for: (i) SJF, (ii) FCFS, (iii) Round Robin ($q = 2$).

**Formulas:**
- $\text{Turnaround Time (TAT)} = \text{Completion Time} - \text{Arrival Time}$
- $\text{Waiting Time (WT)} = \text{TAT} - \text{Burst Time}$

**Step-by-Step Traces:**

#### (i) Shortest Job First (SJF - Non-Preemptive):
Execution Order: $P_3 (4) \rightarrow P_4 (6) \rightarrow P_2 (8) \rightarrow P_1 (10)$
- Gantt Chart: `[ P3: 0-4 | P4: 4-10 | P2: 10-18 | P1: 18-28 ]`
- Completion Times: $P_3 = 4, P_4 = 10, P_2 = 18, P_1 = 28$
- Waiting Times: $P_3 = 0, P_4 = 4, P_2 = 10, P_1 = 18$
- **Average Waiting Time:** $(0 + 4 + 10 + 18) / 4 = 32 / 4 = 8.0 \text{ ms}$
- **Average Turnaround Time:** $(4 + 10 + 18 + 28) / 4 = 60 / 4 = 15.0 \text{ ms}$

#### (ii) First-Come First-Served (FCFS):
Execution Order: $P_1 (10) \rightarrow P_2 (8) \rightarrow P_3 (4) \rightarrow P_4 (6)$
- Gantt Chart: `[ P1: 0-10 | P2: 10-18 | P3: 18-22 | P4: 22-28 ]`
- Waiting Times: $P_1 = 0, P_2 = 10, P_3 = 18, P_4 = 22$
- **Average Waiting Time:** $(0 + 10 + 18 + 22) / 4 = 50 / 4 = 12.5 \text{ ms}$

#### (iii) Round Robin ($q = 2$ ms):
- Gantt Schedule:
  `P1: 0-2 | P2: 2-4 | P3: 4-6 | P4: 6-8 | P1: 8-10 | P2: 10-12 | P3: 12-14 (done) | P4: 14-16 | P1: 16-18 | P2: 18-20 | P4: 20-22 (done) | P1: 22-24 | P2: 24-26 (done) | P1: 26-28 (done)`
- Completion Times: $P_3 = 14, P_4 = 22, P_2 = 26, P_1 = 28$
- Waiting Times:
  - $P_1 = 28 - 10 = 18$
  - $P_2 = 26 - 8 = 18$
  - $P_3 = 14 - 4 = 10$
  - $P_4 = 22 - 6 = 16$
- **Average Waiting Time:** $(18 + 18 + 10 + 16) / 4 = 62 / 4 = 15.5 \text{ ms}$

> **🗓️ Asked In Papers:** `Dec 2022 Q1(b)`

---

---

### Q069: Numerical Simulation — CPU Scheduling with Distinct Arrival Times. :id=q069

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Distinct Arrivals*

**Problem Statement:**
Process Table:  
$P_1: (\text{Arr} = 1, \text{Burst} = 6)$  
$P_2: (\text{Arr} = 2, \text{Burst} = 4)$  
$P_3: (\text{Arr} = 4, \text{Burst} = 1)$  
$P_4: (\text{Arr} = 3, \text{Burst} = 2)$  
$P_5: (\text{Arr} = 5, \text{Burst} = 3)$  
Calculate TAT, WT, and CPU Utilization under FCFS, SJF, and Round Robin ($q = 2$).

- **CPU Idle Period:** Note that at $t = 0$ to $t = 1$, the CPU is IDLE because $P_1$ arrives at $t = 1$.
- **FCFS Trace:**
  - Idle: $0–1$
  - $P_1: 1–7 \implies TAT = 7 - 1 = 6, WT = 0$
  - $P_2: 7–11 \implies TAT = 11 - 2 = 9, WT = 5$
  - $P_4: 11–13 \implies TAT = 13 - 3 = 10, WT = 8$
  - $P_3: 13–14 \implies TAT = 14 - 4 = 10, WT = 9$
  - $P_5: 14–17 \implies TAT = 17 - 5 = 12, WT = 9$
- **Total CPU Utilization:** $(16 / 17) \times 100 = 94.12\%$.

> **🗓️ Asked In Papers:** `Dec 2023 Q1(a)`

---

---

### Q070: Numerical Simulation — CPU Scheduling with FCFS, SRTN, and Round Robin (q = 2). :id=q070

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Gantt Chart & Performance Metrics*

**Problem Statement:**
Consider processes arriving with distinct arrival times:
- $P_1$: Arrival = 1, Burst = 4 ms
- $P_2$: Arrival = 2, Burst = 6 ms
- $P_3$: Arrival = 3, Burst = 2 ms
- $P_4$: Arrival = 4, Burst = 5 ms
- $P_5$: Arrival = 5, Burst = 3 ms

Draw Gantt charts and compute average Turnaround Time ($TAT$), Waiting Time ($WT$), Processor Utilization, and Throughput under: (i) FCFS, (ii) SRTN (Shortest Remaining Time Next), and (iii) Round Robin ($q = 2$).

**Formulas:**
- $TAT = \text{Completion Time} - \text{Arrival Time}$
- $WT = TAT - \text{Burst Time}$
- $\text{Processor Utilization} = \frac{\text{Total Busy Time}}{\text{Total Elapsed Time}} \times 100\%$
- $\text{Throughput} = \frac{\text{Total Completed Processes}}{\text{Total Elapsed Time}}$

**Step-by-Step Simulation:**

#### (i) First-Come First-Served (FCFS):
- $0–1$: CPU IDLE (no process has arrived yet).
- $P_1$: executes $1–5 \implies \text{Completion} = 5, TAT = 5 - 1 = 4, WT = 4 - 4 = 0$
- $P_2$: executes $5–11 \implies \text{Completion} = 11, TAT = 11 - 2 = 9, WT = 9 - 6 = 3$
- $P_3$: executes $11–13 \implies \text{Completion} = 13, TAT = 13 - 3 = 10, WT = 10 - 2 = 8$
- $P_4$: executes $13–18 \implies \text{Completion} = 18, TAT = 18 - 4 = 14, WT = 14 - 5 = 9$
- $P_5$: executes $18–21 \implies \text{Completion} = 21, TAT = 21 - 5 = 16, WT = 16 - 3 = 13$
- **Total TAT:** $4 + 9 + 10 + 14 + 16 = 53 \implies \text{Average } TAT = 53 / 5 = \mathbf{10.6 \text{ ms}}$
- **Total WT:** $0 + 3 + 8 + 9 + 13 = 33 \implies \text{Average } WT = 33 / 5 = \mathbf{6.6 \text{ ms}}$
- **Processor Utilization:** $(20 / 21) \times 100 = \mathbf{95.24\%}$
- **Throughput:** $5 / 21 = \mathbf{0.238 \text{ processes/ms}}$

#### (ii) Shortest Remaining Time Next (SRTN - Preemptive SJF):
- $0–1$: IDLE.
- $t = 1$: $P_1$ arrives (remaining: 4). Executes $1–2$.
- $t = 2$: $P_2$ arrives (rem: 6). $P_1$ rem: 3 $< 6$. $P_1$ continues $2–3$.
- $t = 3$: $P_3$ arrives (rem: 2). $P_1$ rem: 2. Tie goes to current ($P_1$). $P_1$ executes $3–5$ and **completes at 5**.
- $t = 5$: Ready queue: $P_3 (2), P_5 (3), P_4 (5), P_2 (6)$.
- $P_3$ executes $5–7$ and **completes at 7**.
- $P_5$ executes $7–10$ and **completes at 10**.
- $P_4$ executes $10–15$ and **completes at 15**.
- $P_2$ executes $15–21$ and **completes at 21**.
- **Completions:** $P_1 = 5, P_2 = 21, P_3 = 7, P_4 = 15, P_5 = 10$
- **TAT:** $P_1 = 4, P_2 = 19, P_3 = 4, P_4 = 11, P_5 = 5 \implies \text{Average } TAT = 43 / 5 = \mathbf{8.6 \text{ ms}}$
- **WT:** $P_1 = 0, P_2 = 13, P_3 = 2, P_4 = 6, P_5 = 2 \implies \text{Average } WT = 23 / 5 = \mathbf{4.6 \text{ ms}}$

#### (iii) Round Robin ($q = 2$ ms):
- $0–1$: IDLE.
- $1–3: P_1$ runs (rem: 2). ($P_2, P_3$ arrive). Queue: $P_2, P_3, P_1$.
- $3–5: P_2$ runs (rem: 4). ($P_4, P_5$ arrive). Queue: $P_3, P_1, P_4, P_5, P_2$.
- $5–7: P_3$ runs (rem: 0) $\implies \mathbf{P_3 \text{ completes at } 7}$.
- $7–9: P_1$ runs (rem: 0) $\implies \mathbf{P_1 \text{ completes at } 9}$.
- $9–11: P_4$ runs (rem: 3). Queue: $P_5, P_2, P_4$.
- $11–13: P_5$ runs (rem: 1). Queue: $P_2, P_4, P_5$.
- $13–15: P_2$ runs (rem: 2). Queue: $P_4, P_5, P_2$.
- $15–17: P_4$ runs (rem: 1). Queue: $P_5, P_2, P_4$.
- $17–18: P_5$ runs (rem: 0) $\implies \mathbf{P_5 \text{ completes at } 18}$.
- $18–20: P_2$ runs (rem: 0) $\implies \mathbf{P_2 \text{ completes at } 20}$.
- $20–21: P_4$ runs (rem: 0) $\implies \mathbf{P_4 \text{ completes at } 21}$.
- **Completions:** $P_1 = 9, P_2 = 20, P_3 = 7, P_4 = 21, P_5 = 18$
- **TAT:** $P_1 = 8, P_2 = 18, P_3 = 4, P_4 = 17, P_5 = 13 \implies \text{Average } TAT = 60 / 5 = \mathbf{12.0 \text{ ms}}$
- **WT:** $P_1 = 4, P_2 = 12, P_3 = 2, P_4 = 12, P_5 = 10 \implies \text{Average } WT = 40 / 5 = \mathbf{8.0 \text{ ms}}$

> **🗓️ Asked In Papers:** `June 2026 Q1(b)`

---

### Q071: Define the Process Control Block (PCB) and detail all of its essential fields. :id=q071

🟠 **High Priority** • **1 (10 marks)** • *Theory / Data Structures*

**💡 Key Answer Points:**
- **Definition:** The Process Control Block (PCB, also known as Task Control Block) is the primary kernel data structure that stores all execution state and hardware context for an active process.
- **Essential PCB Fields:**
  1. **Process Identifier (PID):** Unique numeric identifier assigned to the process.
  2. **Process State:** Current state of the process (`New`, `Ready`, `Running`, `Waiting`, `Terminated`).
  3. **Program Counter (PC):** Hardware register pointing to the address of the next instruction to be fetched.
  4. **CPU Registers:** Accumulators, index registers, stack pointers, and condition codes saved during a context switch.
  5. **CPU Scheduling Information:** Process priority value, pointers to scheduling queues, and CPU burst counters.
  6. **Memory Management Information:** Page table pointers, segment tables, and base/limit registers defining the process address space.
  7. **Accounting Statistics:** Cumulative CPU execution time, real time elapsed, clock ticks, and account numbers.
  8. **I/O Status Information:** List of open file descriptors, allocated I/O devices, and pending disk requests.

> **🗓️ Asked In Papers:** `June 2022 Q1(d)`

---

---

### Q072: Differentiate the execution roles and frequencies of Long-Term, Medium-Term, and Short-Term Schedulers. :id=q072

🟠 **High Priority** • **1 (10 marks)** • *Theory / Schedulers*

**💡 Key Answer Points:**

| Parameter | Long-Term Scheduler (Job Scheduler) | Medium-Term Scheduler (Swapper) | Short-Term Scheduler (CPU Scheduler) |
| :--- | :--- | :--- | :--- |
| **Execution Frequency** | Infrequent (seconds to minutes); executes only when a job enters or leaves. | Intermediate (seconds); runs when memory becomes overcommitted. | Highly frequent (milliseconds); executes on every clock tick or interrupt. |
| **Primary Responsibility** | Selects jobs from disk job pool and admits them into the ready queue in RAM. | Temporarily removes processes from RAM to disk swap space (swapping out/in). | Selects a process from the ready queue and allocates the physical CPU to it. |
| **Core Goal** | Regulates the **Degree of Multiprogramming**; balances CPU- and I/O-bound jobs. | Mitigates memory over-allocation, reduces thrashing, and frees physical RAM. | Optimizes CPU utilization, maximizes throughput, and minimizes turnaround time. |
| **State Transition** | `New` $\rightarrow$ `Ready` | `Ready` $\leftrightarrow$ `Suspended Ready`, `Blocked` $\leftrightarrow$ `Suspended Blocked` | `Ready` $\rightarrow$ `Running` |

> **🗓️ Asked In Papers:** `June 2024 Q3(b)`

---

---

### Q073: Contrast CPU-bound programs with I/O-bound programs and enumerate primary OS process management duties. :id=q073

🟠 **High Priority** • **1 (10 marks)** • *Theory / Workloads*

**💡 Key Answer Points:**
- **CPU-Bound vs. I/O-Bound Programs:**
  - **CPU-Bound Programs:** Spend the vast majority of their runtime performing complex mathematical calculations and logic loops on the processor (e.g., scientific matrix multiplication, video encoding). They have very long CPU bursts and rare I/O requests.
  - **I/O-Bound Programs:** Spend the vast majority of their execution time waiting for input/output operations to complete (e.g., database query engines, text editors, web browsers). They feature numerous very short CPU bursts separated by long I/O waits.
- **Primary OS Process Management Duties:**
  1. *Process Creation & Termination:* Spawning processes via `fork()`/`exec()` and reclaiming resources via `exit()`.
  2. *Process Scheduling:* Allocating CPU cores across ready processes to ensure fairness and maximize throughput.
  3. *Process Synchronization:* Coordinating concurrent access to shared memory buffers to prevent race conditions.
  4. *Inter-Process Communication (IPC):* Supplying message queues, pipes, and shared memory abstractions.
  5. *Deadlock Handling:* Detecting, avoiding, and recovering from resource deadlocks.

> **🗓️ Asked In Papers:** `Dec 2025 Q1(a)`

---

---

### Q074: Analyze CPU Scheduling algorithms: FCFS, Round Robin, and Priority Scheduling, discussing discrimination against short processes and starvation. :id=q074

🟠 **High Priority** • **1 (10 marks)** • *Theory / Comparative Evaluation*

**💡 Key Answer Points:**
1. **FCFS Evaluation:** Simple, non-preemptive. Severe discrimination against short processes due to the **Convoy Effect**, where short I/O-bound jobs wait behind a single CPU-heavy job.
2. **Round Robin (RR) Evaluation:** Preemptive, fair, responsive. Solves the convoy effect by imposing a fixed time slice $q$. However, if $q$ is too small, context-switching overhead dominates CPU runtime.
3. **Priority Scheduling Evaluation:** Allocates CPU to highest-priority tasks. Suffers from **Starvation (Indefinite Blocking)** for low-priority processes. Solved via **Aging** (gradually increasing a waiting process's priority over time).

> **🗓️ Asked In Papers:** `June 2022 Q2(a)`

---

---

### Q075: Define Batch, Time-Sharing, Real-Time, and Distributed Operating Systems. :id=q075

🟡 **Medium Priority** • **2 (20 marks)** • *Theory / OS Classification*

**💡 Key Answer Points:**
1. **Batch Operating Systems:** Jobs with similar requirements are bundled into batches by an operator and processed sequentially without direct user interaction. Maximizes CPU utilization for heavy corporate reporting.
2. **Time-Sharing Systems:** Uses rapid CPU scheduling (timer interrupts and round-robin quantum) to provide multiple concurrent interactive users with the illusion of dedicated system ownership. Focuses on minimizing response time.
3. **Real-Time Systems (RTOS):** Systems where the correctness of an operation depends strictly on the logical result and the exact time envelope in which it is delivered:
   - *Hard Real-Time:* Missing a deadline results in catastrophic system failure (e.g., pacemaker, flight flight-control).
   - *Soft Real-Time:* Missing a deadline degrades service quality but does not cause system collapse (e.g., video streaming).
4. **Distributed Operating Systems:** Manages a collection of autonomous computers connected via high-speed networks, presenting them to the user as a single, coherent, transparent system.

> **🗓️ Asked In Papers:** `June 2025 Q1(a), June 2026 Q1(a)`

---
