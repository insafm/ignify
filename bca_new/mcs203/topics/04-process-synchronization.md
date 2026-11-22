# 04. Process Synchronization & Mutual Exclusion

> **Syllabus Unit:** Block 1 Unit 3 | **Rank:** #4 | **Frequency Score:** 7.6 | **Offered Marks:** 135 | **Papers Present:** 8/9 | **Importance:** High  
> **Coverage:** 7 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q042: Define a Semaphore. Explain its atomic operations wait() and signal(), and provide the complete solution to the Bounded-Buffer Producer-Consumer problem. :id=q042

🔴 **Very High Priority** • **3 (30 marks)** • *Theory & Code Implementation*

**💡 Key Answer Points:**
- **Definition:** A Semaphore $S$ is a protected integer synchronization variable accessed exclusively through two atomic, indivisible operations: `wait()` (also known as $P$ or `down()`) and `signal()` (also known as $V$ or `up()`).
- **Atomic Operations Specification:**
```c
// Decrements S. If S becomes negative, the calling process blocks
void wait(semaphore S) {
    S.value--;
    if (S.value < 0) {
        // add this process to S.queue;
        block();
    }
}

// Increments S. If there are waiting processes, wakes one up
void signal(semaphore S) {
    S.value++;
    if (S.value <= 0) {
        // remove a process P from S.queue;
        wakeup(P);
    }
}
```
- **Bounded-Buffer Producer-Consumer Implementation:**
  - `mutex`: Binary semaphore initialized to `1` (guarantees mutual exclusion when accessing buffer array).
  - `empty`: Counting semaphore initialized to buffer size `N` (tracks available empty slots).
  - `full`: Counting semaphore initialized to `0` (tracks currently filled items).

```c
#define BUFFER_SIZE 10
typedef int item;
item buffer[BUFFER_SIZE];
int in = 0, out = 0;

semaphore mutex = 1;
semaphore empty = BUFFER_SIZE;
semaphore full = 0;

void Producer() {
    item next_produced;
    while (1) {
        // produce an item in next_produced
        wait(empty);    // wait for an empty buffer slot
        wait(mutex);    // acquire exclusive lock on buffer

        buffer[in] = next_produced;
        in = (in + 1) % BUFFER_SIZE;

        signal(mutex);  // release lock
        signal(full);   // increment full slot count
    }
}

void Consumer() {
    item next_consumed;
    while (1) {
        wait(full);     // wait for at least one filled slot
        wait(mutex);    // acquire exclusive lock on buffer

        next_consumed = buffer[out];
        out = (out + 1) % BUFFER_SIZE;

        signal(mutex);  // release lock
        signal(empty);  // signal availability of empty slot
        // consume the item in next_consumed
    }
}
```

> **🗓️ Asked In Papers:** `Dec 2021 Q3(b), June 2023 Q1(a), Dec 2024 Q3(b)`

---

---

### Q043: Present Lamport's Bakery Algorithm for mutual exclusion among n processes. :id=q043

🟠 **High Priority** • **2 (20 marks)** • *Theory & Algorithm*

**💡 Key Answer Points:**
- **Analogy:** Mirrors a traditional bakery where each customer entering the shop receives a numbered ticket. The customer holding the smallest number is served first. If two processes receive the same ticket number, the process with the smaller process identifier (PID) is given priority: $(a, b) < (c, d) \iff (a < c) \lor (a == c \land b < d)$.
- **Shared Data Structures:**
```c
bool choosing[n] = {false}; // choosing[i] = true while Pi is picking a number
int number[n] = {0};        // number[i] is the ticket assigned to process Pi
```
- **Algorithm for Process $P_i$:**
```c
do {
    choosing[i] = true;
    // Pick ticket number strictly greater than all existing numbers
    number[i] = 1 + max(number[0], number[1], ..., number[n-1]);
    choosing[i] = false;

    // Wait for all other processes to finish choosing and have lower priority
    for (int j = 0; j < n; j++) {
        while (choosing[j]); // Wait if Pj is currently choosing a ticket
        
        while (number[j] != 0 && 
              (number[j] < number[i] || (number[j] == number[i] && j < i)));
    }

    // CRITICAL SECTION
    /* Access shared resource */

    number[i] = 0; // Release ticket upon exit

    // REMAINDER SECTION
} while (true);
```

> **🗓️ Asked In Papers:** `June 2024 Q3(a), Dec 2024 Q3(a)`

---

---

### Q044: Solve the Dining Philosophers Problem using semaphores, discussing deadlock prevention strategies. :id=q044

🟠 **High Priority** • **2 (20 marks)** • *Theory & Concurrency*

**💡 Key Answer Points:**
- **Problem Description:** Five philosophers sit around a circular table with 5 bowls of rice and 5 chopsticks. A philosopher alternates between thinking and eating. To eat, a philosopher must acquire both their left and right chopsticks.
- **Deadlock Condition:** If all five philosophers sit simultaneously and pick up their left chopstick, all chopsticks are held, and each philosopher waits indefinitely for their right chopstick (Circular Wait).
- **Deadlock Prevention Solutions:**
  1. **Asymmetric Protocol:** Odd-numbered philosophers pick up their left chopstick first, then their right; even-numbered philosophers pick up their right chopstick first, then their left.
  2. **Bounded Capacity:** Allow at most 4 philosophers to sit at the table simultaneously using a counting semaphore initialized to 4.
  3. **Atomic Dual Pickup:** Allow a philosopher to pick up chopsticks only if both are currently available.

```c
semaphore chopstick[5] = {1, 1, 1, 1, 1};

void Philosopher(int i) {
    while (1) {
        think();
        if (i % 2 == 0) { // Even philosopher: Right then Left
            wait(chopstick[(i + 1) % 5]);
            wait(chopstick[i]);
        } else {          // Odd philosopher: Left then Right
            wait(chopstick[i]);
            wait(chopstick[(i + 1) % 5]);
        }
        eat();
        signal(chopstick[i]);
        signal(chopstick[(i + 1) % 5]);
    }
}
```

> **🗓️ Asked In Papers:** `June 2025 Q1(c), Dec 2025 Q1(b)`

---

---

### Q045: Define concurrent processes and explain Dekker's Algorithm for mutual exclusion between two processes. :id=q045

🟠 **High Priority** • **1 (10 marks)** • *Theory & Algorithm*

**💡 Key Answer Points:**
- **Concurrent Processes:** Processes executing simultaneously on multiple processor cores, or interleaved on a single CPU via time-slicing, potentially sharing resources and variables.
- **Dekker's Algorithm:** The first mathematically correct software-based mutual exclusion algorithm for two processes ($P_0$ and $P_1$) that avoids busy deadlock and starvation.
- **Shared Variables:**
```c
bool flag[2] = {false, false}; // flag[i] = true indicates Pi wants to enter CS
int turn = 0;                  // Indicates whose turn it is to resolve contention
```
- **Algorithm for Process $P_i$ (with peer $P_j$):**
```c
do {
    flag[i] = true;             // Express intent to enter
    while (flag[j] == true) {   // If peer also wants to enter
        if (turn != i) {        // If it's not Pi's turn
            flag[i] = false;    // Temporarily retract intent
            while (turn != i);  // Busy wait until turn becomes i
            flag[i] = true;     // Re-assert intent
        }
    }

    // CRITICAL SECTION
    /* Access shared data */

    turn = j;                   // Pass priority to peer
    flag[i] = false;            // Exit Critical Section

    // REMAINDER SECTION
} while (true);
```
- **Properties Satisfied:**
  1. *Mutual Exclusion:* Flag check and turn variable guarantee only one process can enter.
  2. *Progress:* If both want to enter, `turn` breaks the tie deterministically.
  3. *Bounded Waiting:* Alternating `turn = j` prevents starvation.

> **🗓️ Asked In Papers:** `Dec 2022 Q1(a)`

---

---

### Q046: Formulate the complete algorithmic solution to the Readers-Writers problem using semaphores. :id=q046

🟠 **High Priority** • **1 (10 marks)** • *Theory & Algorithm*

**💡 Key Answer Points:**
- **Problem Statement:** A database is shared among multiple concurrent processes. Multiple readers may access the database simultaneously without conflict, but writers must have exclusive access (no other reader or writer allowed).
- **Semaphores & Shared State:**
```c
semaphore mutex = 1; // Mutual exclusion for modifying readcount
semaphore wrt = 1;   // Exclusive access lock for writer / first reader
int readcount = 0;   // Number of active reader processes
```
- **Reader Process:**
```c
void Reader() {
    while (1) {
        wait(mutex);
        readcount++;
        if (readcount == 1) // First reader locks out all writers
            wait(wrt);
        signal(mutex);

        // READING DATABASE EXECUTED HERE

        wait(mutex);
        readcount--;
        if (readcount == 0) // Last reader releases lock for writers
            signal(wrt);
        signal(mutex);
    }
}
```
- **Writer Process:**
```c
void Writer() {
    while (1) {
        wait(wrt); // Request exclusive access to the database

        // WRITING TO DATABASE EXECUTED HERE

        signal(wrt); // Release database access
    }
}
```

> **🗓️ Asked In Papers:** `Dec 2023 Q1(c)`

---

---

### Q047: Formulate the semaphore-based coordination solution to the Sleeping Barber problem. :id=q047

🟡 **Medium Priority** • **1 (10 marks)** • *Theory & Algorithm*

**💡 Key Answer Points:**
- **Scenario:** A barbershop has one barber, one barber chair, and $N$ waiting chairs. If there are no customers, the barber sleeps. When a customer arrives:
  - If all $N$ waiting chairs are full, the customer leaves (balks).
  - If chairs are available, the customer sits down and wakes up the sleeping barber.
- **Synchronization Variables:**
```c
#define CHAIRS 5
semaphore customers = 0; // Tracks waiting customers; wakes barber
semaphore barber = 0;    // Tracks barber availability
semaphore mutex = 1;     // Guards shared variable 'waiting'
int waiting = 0;         // Number of customers currently waiting
```
- **Algorithmic Tracing:**
```c
void Barber() {
    while (1) {
        wait(customers); // Sleep until a customer arrives
        wait(mutex);     // Lock waiting variable
        waiting--;       // One customer leaves waiting chair to enter barber chair
        signal(barber);  // Notify customer that barber is ready
        signal(mutex);   // Unlock waiting
        cut_hair();
    }
}

void Customer() {
    wait(mutex);
    if (waiting < CHAIRS) {
        waiting++;
        signal(customers); // Wake up barber if sleeping
        signal(mutex);
        wait(barber);      // Wait until barber is ready
        get_haircut();
    } else {
        signal(mutex);     // Shop full; customer balks
    }
}
```

> **🗓️ Asked In Papers:** `June 2022 Q2(b)`

---

---

### Q048: Define Locks in concurrent programming and contrast Spinlocks with Sleep Mutexes. :id=q048

🟡 **Medium Priority** • **1 (5 marks)** • *Theory / Short Answer*

**💡 Key Answer Points:**
- **Lock Definition:** A mutual exclusion synchronization mechanism designed to enforce exclusive access to a shared resource among concurrent threads.
- **Spinlocks vs. Sleep Mutexes:**
  - **Spinlock:** A thread seeking to acquire an unavailable lock continuously loops (spins) in a busy-waiting while loop, testing the lock variable.
    - *Advantages:* Zero context-switching overhead; ideal for multi-core environments where critical sections are extremely short (< few microseconds).
    - *Disadvantages:* Consumes 100% CPU cycles while spinning; useless on uniprocessor systems.
  - **Sleep Mutex:** When a thread finds the lock busy, the OS kernel suspends the thread, moves it to a wait queue, and schedules another process on the CPU.
    - *Advantages:* Does not waste CPU cycles; ideal for long-running critical sections or disk I/O operations.
    - *Disadvantages:* High context-switch latency when sleeping and waking threads.

> **🗓️ Asked In Papers:** `Dec 2024 Q5(c)`
