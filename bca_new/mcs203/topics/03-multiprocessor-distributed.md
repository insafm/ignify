# 03. Advanced OS: Multiprocessor and Distributed Systems

> **Syllabus Units:** Block 3 Units 1 & 2 | **Rank:** #3 | **Frequency Score:** 8.0 | **Offered Marks:** 160 | **Papers Present:** 8/9 | **Importance:** Very High  
> **Coverage:** 9 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q031: Explain Lamport's Logical Clocks scheme and the happens-before relation for distributed event ordering. :id=q031

🟠 **High Priority** • **Asked in: June 2022 Q5(a) (10 Marks)** • *Theory / Algorithm*

**💡 Key Answer Points:**
- **The Challenge:** Distributed nodes lack physical shared memory and a synchronized global clock.
- **Happens-Before Relation ($
ightarrow$):**
  1. If events $a$ and $b$ occur within the same process, and $a$ occurs before $b$, then $a \rightarrow b$.
  2. If $a$ is the sending of a message by one process, and $b$ is the receipt of the same message by another process, then $a \rightarrow b$.
  3. If $a \rightarrow b$ and $b \rightarrow c$, then $a \rightarrow c$ (Transitivity).
- **Lamport's Clock Algorithm Rules:**
  - Each process $P_i$ maintains a scalar integer clock $C_i$.
  - **Rule 1 (Internal Event):** Before executing an event, $P_i$ increments its clock: $C_i = C_i + 1$.
  - **Rule 2 (Message Passing):** When sending message $m$, $P_i$ attaches timestamp $ts(m) = C_i$.
  - **Rule 3 (Message Receipt):** When process $P_j$ receives message $m$ with timestamp $ts(m)$, it updates its local clock:
    $$C_j = \max(C_j, ts(m)) + 1$$

> **🗓️ Asked In Papers:** `June 2022 Q5(a)`

---

### Q032: Write and explain Ricart and Agrawala's distributed mutual exclusion algorithm. :id=q032

🔴 **Very High Priority** • **Asked in: Dec 2021 Q3(a), June 2025 Q4(a) (10 Marks)** • *Theory / Algorithm & Protocols*

**💡 Key Answer Points:**
- **Algorithm Nature:** A permission-based, non-token algorithm optimizing Lamport's algorithm. It requires no central coordinator and reduces communication overhead to exactly **$2(N-1)$ messages** per Critical Section (CS) execution.
- **Data Structures at Each Node $S_i$:**
  - `our_sequence_number`: Timestamp of local request.
  - `highest_sequence_number`: Highest sequence number seen so far.
  - `requesting_CS`: Boolean flag indicating if node is seeking entry.
  - `deferred_reply_queue`: Array of node IDs to which replies are temporarily deferred.
- **Four Operational Protocols:**
  1. **Requesting Protocol:**
     - Node $S_i$ sets `requesting_CS = true`, increments its clock, sets `our_sequence_number = clock`, and broadcasts a `REQUEST(our_sequence_number, i)` message to all other $N-1$ nodes.
  2. **Receiving Protocol:**
     - When node $S_j$ receives `REQUEST(k, i)` from $S_i$:
     - $S_j$ updates `highest_sequence_number = max(highest_sequence_number, k)`.
     - Node $S_j$ immediately grants permission by returning a `REPLY` message to $S_i$ **UNLESS**:
       - $S_j$ is currently executing the CS, OR
       - $S_j$ is also requesting the CS and has higher priority ($(\text{our\_seq\_num}_j, j) < (k, i)$).
     - If permission is denied, $S_j$ places node ID $i$ on its `deferred_reply_queue`.
  3. **Execution Protocol:**
     - Node $S_i$ enters its Critical Section only after receiving explicit `REPLY` messages from **all other $N-1$ nodes**.
  4. **Release Protocol:**
     - Upon exiting the CS, $S_i$ sets `requesting_CS = false` and sends a `REPLY` message to every node waiting in its `deferred_reply_queue`, emptying the queue.

> **🗓️ Asked In Papers:** `Dec 2021 Q3(a), June 2025 Q4(a)`

---

### Q033: Enumerate and explain the core design challenges and issues in building Distributed Systems. :id=q033

🔴 **Very High Priority** • **Asked in: Dec 2021 Q1(c), June 2024 Q1(b), Dec 2025 Q1(c) (10 Marks)** • *Theory / Short & Long Answer*

**💡 Key Answer Points:**
1. **Heterogeneity:** Managing diverse hardware architectures (ARM, x86), operating systems (Linux, Windows), networks, and programming languages using standardized middleware.
2. **Openness:** Designing systems with standardized public interfaces (e.g., POSIX, REST) so new services can be added without disrupting existing operations.
3. **Security:** Protecting data confidentiality and integrity across open network channels through encryption, authentication (Kerberos), and non-repudiation.
4. **Scalability:** Ensuring performance does not degrade as users, data volumes, and geographically distributed nodes increase.
5. **Independent Failure Handling:** Detecting and recovering from partial failures without halting the entire system (fault tolerance, data replication, consensus algorithms).
6. **Transparency:** Concealing distributed complexity from users across 8 dimensions: Access, Location, Migration, Relocation, Replication, Concurrency, Failure, and Persistence transparency.

> **🗓️ Asked In Papers:** `Dec 2021 Q1(c), June 2024 Q1(b), Dec 2025 Q1(c)`

---

### Q034: Explain the Distributed Shared Memory (DSM) application model with an architectural block diagram. :id=q034

🟠 **High Priority** • **Asked in: June 2023 Q3(b) (10 Marks)** • *Theory / Diagram & Architecture*

**💡 Key Answer Points:**
- **Concept:** Distributed Shared Memory provides a virtual shared address space abstraction across physically separate, networked computer nodes. Programmers use standard shared-memory pointers and variables instead of message-passing APIs.

```
+------------------------+      +------------------------+
| Application Threads P1 |      | Application Threads P2 |
+------------------------+      +------------------------+
|    DSM Software Layer  | <--> |    DSM Software Layer  |
+------------------------+      +------------------------+
| Local Physical Memory  |      | Local Physical Memory  |
+------------------------+      +------------------------+
| Network Interface Card |      | Network Interface Card |
+------------------------+      +------------------------+
            ^                               ^
            +====== High-Speed Network =====+
```

- **Operational Coordination:**
  - When thread $P_1$ accesses a page present in local RAM, access is instantaneous.
  - If the page resides on a remote node, the MMU fires a page fault intercepted by the DSM runtime layer.
  - The DSM software requests the page across the network, caches it locally, and uses memory consistency protocols (Strict, Sequential, or Release Consistency) to maintain global coherence.

> **🗓️ Asked In Papers:** `June 2023 Q3(b), June 2026 Q5(e)`

---

### Q035: Detail multiprocessor synchronization hardware primitives: Test-and-Set, Compare-and-Swap, and Fetch-and-Add. :id=q035

🔴 **Very High Priority** • **Asked in: June 2023 Q4(a), Dec 2023 Q2(b) (10 Marks)** • *Theory / Hardware Primitives*

**💡 Key Answer Points:**
Modern multi-core processors enforce mutual exclusion using low-level, atomic (indivisible) hardware bus instructions:

1. **Test-and-Set (`TAS`):** Atomically reads a memory location and sets it to `true` in a single bus lock cycle:
```c
bool TestAndSet(bool *target) {
    bool rv = *target;
    *target = true;
    return rv;
}
```
2. **Compare-and-Swap (`CAS`):** Takes three operands: a memory location $V$, expected old value $A$, and new target value $B$. Atomically updates $V$ to $B$ only if current value equals $A$:
```c
int CompareAndSwap(int *word, int expected, int new_val) {
    int temp = *word;
    if (temp == expected)
        *word = new_val;
    return temp;
}
```
3. **Fetch-and-Add (`FAA`):** Atomically increments a memory counter by a specified increment value and returns the prior value:
```c
int FetchAndAdd(int *variable, int increment) {
    int old_val = *variable;
    *variable += increment;
    return old_val;
}
```

> **🗓️ Asked In Papers:** `June 2023 Q4(a), Dec 2023 Q2(b)`

---

### Q036: Contrast the three primary architectures for distributed applications: Client/Server (RPC), Distributed Objects, and Distributed Shared Memory. :id=q036

🟠 **High Priority** • **Asked in: Dec 2023 Q2(a) (10 Marks)** • *Theory / Comparison & Architecture*

**💡 Key Answer Points:**

| Architecture | Communication Paradigm | State Location | Programming Abstraction |
| :--- | :--- | :--- | :--- |
| **Client/Server (RPC)** | Synchronous Request / Reply message exchange over network sockets. | Server holds centralized state; clients are stateless or session-bound. | Function calls look local via client/server stubs (`stub.invoke()`). |
| **Distributed Objects** | Remote Method Invocation (RMI / CORBA / DCOM). | Encapsulated inside distributed objects across network hosts. | Object-oriented method invocations across address spaces (`remoteObj.method()`). |
| **Distributed Shared Memory (DSM)** | Hardware/software page faulting and virtual memory replication. | Shared virtual address space mapped across nodes' physical memories. | Standard memory load/store operations (`*ptr = value`) with hardware MMU. |

> **🗓️ Asked In Papers:** `Dec 2023 Q2(a)`

---

### Q037: Explain Remote Procedure Call (RPC): Execution steps, data marshaling, and inherent limitations. :id=q037

🟠 **High Priority** • **Asked in: Dec 2023 Q5(d), Dec 2025 Q4(a) (10 Marks)** • *Theory / Architecture*

**💡 Key Answer Points:**
- **Concept:** RPC abstracts network message passing so calling a function on a remote machine syntactically mirrors a local function call.
- **Components & Execution Sequence:**
  1. **Client Stub:** Marshals procedure name and arguments into a standardized network packet (Serialization/XDR).
  2. **Communication Module:** Transmits the message over network protocols (UDP/TCP).
  3. **Server Stub:** Unmarshals parameters from the network packet and invokes the actual server procedure.
  4. **Return Path:** Results are marshaled by the server stub, returned via network, and unmarshaled by the client stub to resume client execution.
- **Inherent Limitations:**
  - *Network Latency:* Network traversal is orders of magnitude slower than local register/stack calls.
  - *Failure Modes:* Network partitions, lost packets, and independent server crashes introduce complex failure states.
  - *Pointer Passing:* Memory pointers and references cannot be passed directly across distinct address spaces without deep copying.

> **🗓️ Asked In Papers:** `Dec 2023 Q5(d), Dec 2025 Q4(a), June 2026 Q5(a)`

---

### Q038: Explain Multiprocessor Operating System configurations: Master/Slave vs. Separate Supervisor. :id=q038

🟠 **High Priority** • **Asked in: June 2025 Q4(b) (10 Marks)** • *Theory / Architecture*

**💡 Key Answer Points:**
1. **Master/Slave Configuration:**
   - One designated processor (the Master) executes the operating system kernel, handles interrupts, coordinates memory allocations, and schedules jobs.
   - Remaining processors (Slaves) execute user application tasks only. When a slave requires OS services, it generates a trap to the master.
   - *Limitation:* The master CPU becomes a massive system bottleneck; master failure brings down the entire system.
2. **Separate Supervisor Configuration:**
   - Each processor runs its own private copy of the operating system kernel.
   - Each processor manages its own local memory, interrupts, and ready queues independently.
   - *Limitation:* Resource sharing across processors is difficult; memory tables and process states must be explicitly duplicated.

> **🗓️ Asked In Papers:** `June 2025 Q4(b)`

---

### Q039: Contrast Tightly-Coupled Systems with Loosely-Coupled Systems. :id=q039

🟡 **Medium Priority** • **Asked in: Dec 2024 Q4(c) (5 Marks)** • *Theory / Comparison*

**💡 Key Answer Points:**
- **Tightly-Coupled Systems (Multiprocessors):**
  - Processors share a single central memory (RAM), system bus, clock, and peripherals.
  - Coordinated by a single unified operating system. Communication occurs at memory bus speeds (nanoseconds) via shared variables.
- **Loosely-Coupled Systems (Distributed Systems):**
  - Consists of autonomous independent computers, each possessing its own local CPU, memory, clock, and operating system instance.
  - Nodes communicate strictly via message-passing packets across local or wide area network links (millisecond latency).

> **🗓️ Asked In Papers:** `Dec 2024 Q4(c)`

---

### Q032A: Explain Lamport's Distributed Mutual Exclusion Algorithm and message exchange protocol. :id=q032a

🔴 **Very High Priority** • **Asked in: June 2026 Q1(d) (10 Marks)** • *Theory & Distributed Protocols*

**💡 Key Answer Points:**
- **Foundation:** Lamport's Distributed Mutual Exclusion Algorithm was the first permission-based algorithm designed to achieve mutual exclusion without a central coordinator, relying on Lamport Logical Clocks to establish total event ordering.
- **Data Structures at Each Site $S_i$:**
  - Local logical clock $C_i$.
  - A local request queue `request_queue_i` ordered by timestamp tuple $(T_i, i)$.
- **Protocol Steps:**
  1. **Requesting Critical Section (CS):**
     - Site $S_i$ updates its clock, inserts `REQUEST(T_i, i)` into its own `request_queue_i`, and broadcasts `REQUEST(T_i, i)` to all other $N-1$ sites.
  2. **Receiving a Request:**
     - When site $S_j$ receives `REQUEST(T_i, i)`, it places the request on its local `request_queue_j`, updates its clock, and returns a timestamped `REPLY` message to $S_i$.
  3. **Executing the Critical Section:**
     - Site $S_i$ enters the CS if and only if:
       - $S_i$'s request `REQUEST(T_i, i)` is at the **top of its local request queue** (smallest timestamp), AND
       - $S_i$ has received a message (either a `REPLY` or another message) from **all other $N-1$ sites** with a timestamp greater than $(T_i, i)$.
  4. **Releasing the Critical Section:**
     - Upon exiting, $S_i$ removes its request from the top of its queue and broadcasts a timestamped `RELEASE` message to all $N-1$ sites.
     - When a site receives the `RELEASE`, it removes $S_i$'s request from its queue.
- **Message Complexity:** Requires $3(N-1)$ messages per critical section invocation ($(N-1)$ requests + $(N-1)$ replies + $(N-1)$ releases). *(Note: Ricart-Agrawala later optimized this to $2(N-1)$ messages by eliminating explicit release messages).*

> **🗓️ Asked In Papers:** `June 2026 Q1(d)`
