# 06. Deadlocks

> **Syllabus Unit:** Block 1 Unit 4 | **Rank:** #6 | **Frequency Score:** 5.4 | **Offered Marks:** 95 | **Papers Present:** 7/9 | **Importance:** High  
> **Coverage:** 5 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q054: Define a Deadlock. List and explain the four necessary Coffman conditions for a deadlock occurrence. :id=q054

🔴 **Very High Priority** • **4 (40 marks)** • *Theory / Core Concepts*

**💡 Key Answer Points:**
- **Definition:** A deadlock is a state where a set of concurrent processes are permanently blocked because each process holds at least one resource and is waiting to acquire another resource held by another process in the same set.
- **The Four Coffman Conditions:** A deadlock can arise if and only if all four conditions hold simultaneously in the system:
  1. **Mutual Exclusion:** At least one resource must be non-shareable. Only one process can hold the resource at any given moment.
  2. **Hold and Wait:** A process must currently hold at least one resource and simultaneously wait to acquire additional resources that are currently held by other processes.
  3. **No Preemption:** Resources cannot be forcibly confiscated from a process; a resource can only be released voluntarily by the holding process after completing its task.
  4. **Circular Wait:** A closed chain of processes $\{P_0, P_1, \dots, P_n\}$ must exist such that $P_0$ is waiting for a resource held by $P_1$, $P_1$ is waiting for $P_2$, $\dots$, and $P_n$ is waiting for a resource held by $P_0$.

**📝 Example PQP Question (Dec 2024 Q1(b)):**

Define a deadlock. List and explain all the four conditions that are must to create the deadlock situation. *(5 marks)*

> **🗓️ Asked In Papers:** [June 2022 Q1(a)](/bca_new/mcs203/pqp/MCS-203_June_2022.pdf ':ignore'), [Dec 2022 Q3(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2022.pdf ':ignore'), [Dec 2024 Q1(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2024.pdf ':ignore'), [Dec 2025 Q1(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2025.pdf ':ignore')

---

---

### Q055: Explain Deadlock Prevention and detail Havender's Algorithm (rules) for eliminating Coffman conditions. :id=q055

🔴 **Very High Priority** • **2 (20 marks)** • *Theory / Prevention Rules*

**💡 Key Answer Points:**
- **Deadlock Prevention Philosophy:** Employs static structural constraints on process resource requests to guarantee that at least one of the four necessary Coffman conditions cannot hold.
- **Havender's Rules:**
  1. **Rule 1 (Eliminate Hold and Wait - Conservative Allocation):**
     - A process must request and be allocated all its required resources at once before commencing execution. If even a single resource is unavailable, none are granted, and the process waits.
     - *Alternative Formulation:* A process may request resources only when it holds zero resources; it must release all current allocations before requesting a new set.
  2. **Rule 2 (Eliminate No Preemption - Resource Revocation):**
     - If a process holding resources requests an additional resource that is currently allocated to another waiting process, all resources held by the requesting process are preempted and returned to the free pool.
  3. **Rule 3 (Eliminate Circular Wait - Global Linear Ordering):**
     - Impose a strict, 1-to-1 linear ordering on all resource classes using a mapping function:
       $$F: R \rightarrow \mathbb{N} \quad (\text{e.g., Disk} = 1, \text{Printer} = 2, \text{Tape} = 3)$$
     - A process can only request a resource $R_j$ if $F(R_j) > F(R_i)$, where $R_i$ is any resource already held by that process. This strictly prevents the formation of cycles.

**📝 Example PQP Question (Dec 2025 Q2(b)):**

Define a deadlock. How can the deadlock be prevented using Havender’s algorithm ? *(10 marks)*

> **🗓️ Asked In Papers:** [June 2022 Q1(a)](/bca_new/mcs203/pqp/MCS-203_June_2022.pdf ':ignore'), [Dec 2025 Q1(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2025.pdf ':ignore')

---

---

### Q056: Numerical Problem — Resource Allocation Graph with Multi-Instance Resources and Deadlock Evaluation. :id=q056

🔴 **Very High Priority** • **1 (10 marks)** • *Numerical / Graph Theory & Deadlock*

**Problem Statement:**
Consider a system with four processes ($P_1, P_2, P_3, P_4$) and two resources ($R_1, R_2$), each with two instances.
- $P_1$ acquires an instance of $R_2$, and requests an instance of $R_1$.
- $P_2$ acquires an instance of $R_1$, and doesn't need any other resource.
- $P_3$ acquires an instance of $R_1$, and requires an instance of $R_2$.
- $P_4$ acquires an instance of $R_2$, and doesn't need any other resource.

**(I) Draw the Resource Allocation Graph (RAG):**
```
      [ R1: 2 instances ]
         /           \
   Allocation     Allocation
       /               \
      v                 v
   ( P2 )             ( P3 )
     |                  |
   [Done]            Request
                        |
                        v
      [ R2: 2 instances ]
         /           \
   Allocation     Allocation
       /               \
      v                 v
   ( P4 )             ( P1 )
     |                  |
   [Done]            Request
                        |
                        +----> [ R1 ]
```

**(II) Is there any cycle in the graph?**
- Cycle 1: $P_1 \rightarrow R_1 \rightarrow P_3 \rightarrow R_2 \rightarrow P_1$.
- **Yes**, there is a directed cycle between $P_1, R_1, P_3,$ and $R_2$.

**(III) Is the system in Deadlock?**
- **NO, the system is NOT in deadlock.**
- **Reason:** Even though a cycle exists, both $R_1$ and $R_2$ possess **multiple instances (2 each)**.
- **Valid Execution Sequence:**
  1. $P_2$ holds 1 instance of $R_1$ and needs no other resources. $P_2$ executes to completion and releases its instance of $R_1$.
  2. Free instances of $R_1$ becomes 1. This free instance can now be allocated to $P_1$.
  3. Meanwhile, $P_4$ holds 1 instance of $R_2$ and needs no other resources. $P_4$ finishes and releases its instance of $R_2$.
  4. Free instances of $R_2$ becomes 1. This free instance can now be allocated to $P_3$.
  5. Both $P_1$ and $P_3$ can now complete execution.
- **Safe Execution Sequence:** $\langle P_2, P_4, P_1, P_3 \rangle$ (or $\langle P_4, P_2, P_3, P_1 \rangle$).

**📝 Example PQP Question (June 2026 Q3(a)):**

There are four processes and two resources in the system. Each resource has two instances. Furthermore :

(i) P1 acquires an instance of R2, and requests an instance of R1.
(ii) P2 acquires an instance of R1, and doesn’t need any other resource.
(iii) P3 acquires an instance of R1, and requires an instance of R2.
(iv) P4 acquires an instance of R2, and doesn’t need any other resource.

(I) Draw the resource allocation graph.
(II) Is there any cycle in the graph ? If yes, name it.
(III) Whether the system is in deadlock ? If yes, explain why; if not, provide sequence of execution of processes. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2026 Q3(a)](/bca_new/mcs203/pqp/MCS-203_June_2026.pdf ':ignore')

---

### Q057: Explain Dijkstra's Banker's Algorithm for deadlock avoidance, detailing the Safety Algorithm. :id=q057

🟠 **High Priority** • **2 (20 marks)** • *Theory & Algorithm*

**💡 Key Answer Points:**
- **Deadlock Avoidance Concept:** Unlike prevention (which restricts static requests), avoidance dynamically inspects each resource allocation request to verify that granting it keeps the system in a **Safe State**.
- **Data Structures (for $n$ processes and $m$ resource types):**
  - `Available[m]`: Number of free instances for each resource type.
  - `Max[n][m]`: Maximum claim matrix declared by each process.
  - `Allocation[n][m]`: Resources currently allocated to each process.
  - `Need[n][m]`: Remaining resource need: $\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$.
- **The Safety Algorithm Steps:**
  1. Initialize `Work = Available` (vector of length $m$) and `Finish[i] = false` for all $i = 0, \dots, n-1$.
  2. Search for an index $i$ such that:
     $$\text{Finish}[i] == \text{false} \quad \text{and} \quad \text{Need}[i] \le \text{Work}$$
  3. If found:
     $$\text{Work} = \text{Work} + \text{Allocation}[i]$$
     $$\text{Finish}[i] = \text{true}$$
     Repeat Step 2.
  4. If `Finish[i] == true` for all $i$, the system is in a **Safe State** (a valid execution order $\langle P_0, P_1, \dots, P_{n-1} \rangle$ exists). If not, the system is unsafe and the request is deferred.

**📝 Example PQP Question (June 2023 Q2(b)):**

Write and explain “Banker’s algorithm” for Deadlock Avoidance proposed by Dijkstra. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2023 Q2(b)](/bca_new/mcs203/pqp/MCS-203_June_2023.pdf ':ignore'), [Dec 2023 Q5(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2023.pdf ':ignore')

---

---

### Q058: Characterize deadlock using a Resource Allocation Graph (RAG) and explain cycle detection. :id=q058

🟠 **High Priority** • **1 (10 marks)** • *Theory / Graph Theory*

**💡 Key Answer Points:**
- **Resource Allocation Graph (RAG):** A directed bipartite graph $G = (V, E)$ where vertices are partitioned into processes $P = \{P_1, \dots, P_n\}$ (circles) and resource types $R = \{R_1, \dots, R_m\}$ (rectangles containing dots for instances).
- **Edge Types:**
  - **Request Edge ($P_i \rightarrow R_j$):** Process $P_i$ has requested an instance of $R_j$ and is currently waiting.
  - **Assignment Edge ($R_j \rightarrow P_i$):** An instance of resource $R_j$ is allocated to process $P_i$.
- **Cycle Theorem for Deadlocks:**
  - **Single Instance per Resource Type:** A directed cycle in the RAG is both a **necessary and sufficient** condition for deadlock.
  - **Multiple Instances per Resource Type:** A cycle is a **necessary condition but NOT sufficient**; processes outside the cycle may finish and release resources, resolving the cycle.

```
Single Instance Deadlock Example:
    ( P1 ) ---- Request ----> [ R1 ]
      ^                         |
      |                     Assignment
  Assignment                    |
      |                         v
    [ R2 ] <--- Request ----- ( P2 )
    [Cycle P1 -> R1 -> P2 -> R2 -> P1 indicates Deadlock]
```

**📝 Example PQP Question (June 2024 Q1(a)):**

Characterize a deadlock in a system. Using a resource allocation graph, illustrate a deadlock. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2024 Q1(a)](/bca_new/mcs203/pqp/MCS-203_June_2024.pdf ':ignore')

---

---

### Q059: Explain Deadlock Detection algorithms and recovery mechanisms (process termination vs. resource preemption). :id=q059

🟡 **Medium Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**
- **Deadlock Detection:**
  - If resources have single instances, the OS collapses the RAG into a **Wait-For Graph** (removing resource nodes) and periodically runs depth-first cycle detection ($O(n^2)$).
  - If resources have multiple instances, an algorithm similar to Banker's Safety algorithm is executed.
- **Recovery Strategies:**
  1. **Process Termination:**
     - *Abort all deadlocked processes:* Guarantees recovery but discards completed work.
     - *Abort processes one at a time:* Terminate the process with lowest priority, re-run detection, and repeat until the cycle breaks.
  2. **Resource Preemption:**
     - *Victim Selection:* Determine which process has incurred minimal runtime or consumed minimal resources.
     - *Rollback:* Roll the selected victim process back to a safe checkpoint state.
     - *Starvation Avoidance:* Ensure the same process is not repeatedly chosen as a preemption victim.

**📝 Example PQP Question (June 2025 Q5(b)):**

Write short notes on: Deadlock detection and Recovery *(5 marks)*

> **🗓️ Asked In Papers:** [June 2025 Q5(b)](/bca_new/mcs203/pqp/MCS-203_June_2025.pdf ':ignore')

---
