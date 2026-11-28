# 05. Case Study: Linux Architecture & System Security

> **Syllabus Unit:** Block 4 Unit 2 | **Rank:** #5 | **Frequency Score:** 5.8 | **Offered Marks:** 105 | **Papers Present:** 8/9 | **Importance:** High  
> **Coverage:** 4 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q049: Detail the multi-layered security model of the Linux Operating System across its five core pillars. :id=q049

🔴 **Very High Priority** • **5 (50 marks)** • *Theory / Multi-Tier Security*

**💡 Key Answer Points:**
Linux enforces a multi-tier defense-in-depth model across five standard security layers:

```
+-----------------------------------------------------------------+
| 1. USER ACCOUNTS & ISOLATION (UID / GID, Root Superuser vs Non-Root) |
+-----------------------------------------------------------------+
| 2. POSIX DISCRETIONARY ACCESS CONTROL (rwx on Owner/Group/Other) |
+-----------------------------------------------------------------+
| 3. DATA INTEGRITY VERIFICATION (GPG Package Signatures, SHA-256) |
+-----------------------------------------------------------------+
| 4. ENCRYPTED STORAGE AT REST (LUKS Volume Encryption / dm-crypt) |
+-----------------------------------------------------------------+
| 5. SECURE REMOTE ADMINISTRATION (OpenSSH, Public Key Crypto)     |
+-----------------------------------------------------------------+
```

1. **User Accounts & Identity Isolation:**
   - Every user has a unique numeric User ID (`UID`) and Group ID (`GID`).
   - The `root` user (`UID = 0`) has unrestricted kernel access; all normal services run under unprivileged accounts (e.g., `www-data`, `nobody`) to enforce principle of least privilege.
2. **POSIX File Permissions (Discretionary Access Control):**
   - Every file and directory is assigned 9 permission bits divided into three triads: **Owner (u)**, **Group (g)**, and **Others (o)**.
   - Permissions enforce **Read (r = 4)**, **Write (w = 2)**, and **Execute (x = 1)**, alongside special bits (`SUID`, `SGID`, Sticky bit).
3. **Data Verification & Cryptographic Integrity:**
   - Linux package management (APT / YUM) verifies downloaded binaries using **GPG public key signatures**.
   - System file integrity tools utilize cryptographic hashes (**SHA-256 / SHA-512**) to detect unauthorized tampering of system executables.
4. **Encrypted Storage at Rest (LUKS):**
   - Implements block-level volume encryption using **LUKS (Linux Unified Key Setup)** and the kernel `dm-crypt` subsystem.
   - Entire disk partitions, including swap space and root filesystems, are encrypted with AES-256, protecting against physical disk extraction.
5. **Secure Remote Administration (SSH):**
   - Eliminates insecure cleartext protocols (Telnet, RSH) in favor of **OpenSSH**.
   - Employs asymmetric public-key cryptography (Ed25519 / RSA), disablement of root password logins, and port-knocking/fail2ban defense.

**📝 Example PQP Question (Dec 2023 Q1(d)):**

Discuss the security features in LINUX with respect to the following :

(i) User Accounts
(ii) File Permissions
(iii) Encrypted Storage
(iv) Remote Access *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2021 Q4(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2021.pdf ':ignore'), [Dec 2022 Q5(c)](/bca_new/mcs203/pqp/MCS-203_Dec_2022.pdf ':ignore'), [June 2023 Q5(c)](/bca_new/mcs203/pqp/MCS-203_June_2023.pdf ':ignore'), [Dec 2023 Q1(d)](/bca_new/mcs203/pqp/MCS-203_Dec_2023.pdf ':ignore'), [June 2025 Q5(c)](/bca_new/mcs203/pqp/MCS-203_June_2025.pdf ':ignore')

---

---

### Q050: Draw and explain the core architecture diagram of the Linux Operating System. :id=q050

🔴 **Very High Priority** • **3 (30 marks)** • *Theory / Diagram & Architecture*

**💡 Key Answer Points:**
Linux employs a modular, monolithic kernel architecture where all core OS subsystems execute within a single privileged memory address space.

```
+-----------------------------------------------------------------+
|                          USER SPACE                             |
|    User Applications, Shells (Bash), Compilers, Daemons, GUI    |
+-----------------------------------------------------------------+
|                 SYSTEM CALL INTERFACE (SCI)                     |
|           fork(), read(), write(), open(), mmap(), clone()      |
+=================================================================+
|                         KERNEL SPACE                            |
|  +-------------------+  +-----------------+  +---------------+  |
|  | PROCESS SCHEDULER |  | MEMORY MANAGER  |  | VIRTUAL FILE  |  |
|  |  (CFS, Real-Time) |  | (Buddy, Paging) |  | SYSTEM (VFS)  |  |
|  +-------------------+  +-----------------+  +---------------+  |
|  +-------------------+  +-----------------+  +---------------+  |
|  |   NETWORK STACK   |  |   IPC SUBSYSTEM |  | DEVICE        |  |
|  |  (TCP/IP, Sockets)|  |  (Pipes, Shm)   |  | DRIVERS       |  |
|  +-------------------+  +-----------------+  +---------------+  |
+=================================================================+
|                     PHYSICAL HARDWARE                           |
|       CPU, Physical RAM, Hard Disks/SSD, Network Cards, Buses   |
+-----------------------------------------------------------------+
```

- **Core Subsystems:**
  1. **System Call Interface (SCI):** The gateway between unprivileged user-space programs and privileged kernel services via software interrupts (`int 0x80` or `syscall`).
  2. **Process Scheduler:** Manages CPU allocation using the Completely Fair Scheduler (CFS) for interactive/batch tasks and POSIX priority queues for real-time threads.
  3. **Memory Manager:** Handles virtual-to-physical address mapping, demand paging, buddy system physical allocations, and swapping.
  4. **Virtual File System (VFS):** Provides a uniform, object-oriented filesystem interface (`open`, `read`, `write`) that abstracts concrete filesystems (`ext4`, `xfs`, `NFS`, `FAT32`).
  5. **Network Stack:** Implements standard communication protocols (TCP/IP, UDP, IPv6) and BSD socket interfaces.
  6. **Device Drivers:** Modules dynamically loaded into the running kernel to communicate with physical hardware peripherals.

**📝 Example PQP Question (June 2024 Q4(b)):**

With the help of a diagram, explain LINUX architecture with a special focus on ‘Kernel’ and its components. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2023 Q1(d)](/bca_new/mcs203/pqp/MCS-203_June_2023.pdf ':ignore'), [June 2024 Q4(b)](/bca_new/mcs203/pqp/MCS-203_June_2024.pdf ':ignore'), [June 2026 Q5(d)](/bca_new/mcs203/pqp/MCS-203_June_2026.pdf ':ignore')

---

---

### Q051: Explain Virtual Memory mapping and physical memory management in Linux, including page cache and the Buddy System allocator. :id=q051

🟠 **High Priority** • **4 (40 marks)** • *Theory / Long Answer*

**💡 Key Answer Points:**
- **Memory Architecture:** Linux divides memory into two primary zones:
  - **Kernel Space (Top 1 GB on 32-bit / Upper half on 64-bit):** Directly mapped physical RAM containing kernel code and page tables.
  - **User Space (Lower 3 GB on 32-bit):** Private address space per process containing code, data, heap, and stack.
- **Four-Level Paging Hardware:** Linux employs a 4-level paging hierarchy (PGD $\rightarrow$ P4D $\rightarrow$ PUD $\rightarrow$ PMD $\rightarrow$ PTE) to translate virtual addresses across multi-terabyte address spaces.
- **Buddy System Allocator:**
  - Manages contiguous physical page frames to prevent external memory fragmentation.
  - Memory blocks are maintained in size-powers of two ($2^0, 2^1, \dots, 2^{10}$ pages).
  - When a block is freed, the kernel checks if its "buddy" block of identical size is also free; if so, they merge into a larger block.
- **Slab Allocator:** Sits on top of the Buddy System to allocate small kernel objects (e.g., `task_struct`, `mm_struct`) without wasting full 4 KB page frames.
- **Page Cache & Swapping:** Frequently read disk blocks are cached in physical RAM (Page Cache). When free RAM drops, modified dirty pages are flushed to swap partitions via `kswapd`.

**📝 Example PQP Question (June 2025 Q3(b)):**

Explain memory management in LINUX with the help of a diagram. *(10 marks)*

> **🗓️ Asked In Papers:** [Dec 2021 Q2(b)](/bca_new/mcs203/pqp/MCS-203_Dec_2021.pdf ':ignore'), [Dec 2024 Q5(a)](/bca_new/mcs203/pqp/MCS-203_Dec_2024.pdf ':ignore'), [June 2025 Q5(c)](/bca_new/mcs203/pqp/MCS-203_June_2025.pdf ':ignore'), [Dec 2025 Q5(d)](/bca_new/mcs203/pqp/MCS-203_Dec_2025.pdf ':ignore')

---

---

### Q052: Describe Process Management in Linux, including process hierarchy, process states, the CFS scheduler, and the clone() system call. :id=q052

🟠 **High Priority** • **1 (10 marks)** • *Theory / Architecture*

**💡 Key Answer Points:**
- **Process Hierarchy:** Linux maintains a strict parent-child process tree rooted at PID 1 (`init` or `systemd`). Every process is spawned via `fork()` and tracks parent PID (`ppid`).
- **Process States in Linux:**
  - `TASK_RUNNING`: Process is either executing on a CPU or waiting in the runqueue.
  - `TASK_INTERRUPTIBLE`: Process is suspended waiting for an event/resource; can be awakened early by signals.
  - `TASK_UNINTERRUPTIBLE`: Process is waiting directly on hardware I/O; will not wake up for signals.
  - `TASK_STOPPED`: Execution suspended (via SIGSTOP or debugger breakpoint).
  - `TASK_ZOMBIE`: Process terminated, but parent has not yet called `wait()` to collect exit status.
- **Completely Fair Scheduler (CFS):**
  - Manages normal non-real-time processes using a balanced **Red-Black Tree** ordered by `vruntime` (virtual runtime).
  - The process with the smallest `vruntime` is positioned at the leftmost leaf of the tree and scheduled next.
- **The `clone()` System Call:** Linux does not distinguish between threads and processes at the kernel level; both are represented by `task_struct`. The `clone()` system call creates lightweight tasks by passing sharing flags (`CLONE_VM`, `CLONE_FS`, `CLONE_FILES`, `CLONE_SIGHAND`).

**📝 Example PQP Question (June 2022 Q3(a)):**

Describe the process management in LINUX which includes process priorities, process hierarchy, process states and threads management. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2022 Q1(b)](/bca_new/mcs203/pqp/MCS-203_June_2022.pdf ':ignore')

---

---

### Q053: Explain the Access Matrix Security Model implemented in operating systems with an example. :id=q053

🟠 **High Priority** • **1 (10 marks)** • *Theory / Security Architecture*

**💡 Key Answer Points:**
- **Access Matrix Concept:** A formal conceptual model representing the protection state of a computer system. It models access rights as a 2D matrix where:
  - **Rows:** Represent **Domains** / Subjects (Users, Processes executing under a specific user context).
  - **Columns:** Represent **Objects** (Files, Memory Segments, Printers, System Calls).
  - **Matrix Entry $A[\text{Domain } i, \text{Object } j]$:** The set of access rights (e.g., `read`, `write`, `execute`, `owner`) that a process executing in domain $i$ possesses on object $j$.

**Illustrative Example Matrix:**

| Domain / User | File 1 (`/etc/passwd`) | File 2 (`payroll.dat`) | File 3 (`code.c`) | Laser Printer |
| :--- | :--- | :--- | :--- | :--- |
| **Domain 1 (Root Admin)** | `read`, `write`, `owner` | `read`, `write`, `owner` | `read`, `write`, `execute` | `print` |
| **Domain 2 (Finance User)** | `read` | `read`, `write` | `none` | `print` |
| **Domain 3 (Software Dev)** | `read` | `none` | `read`, `write`, `execute` | `none` |

- **Kernel Implementation Mechanisms:** Because a full matrix is sparsely populated, operating systems implement the access matrix in practice using two structures:
  1. **Access Control Lists (ACLs):** Stored column-wise with the object (e.g., File 2 tracks ACL: `[Domain 1: rw, Domain 2: rw]`). Used in modern filesystems (NTFS, ext4).
  2. **Capability Lists:** Stored row-wise with the domain/process (e.g., Domain 2 holds capability tickets for File 1 [r], File 2 [rw], Printer [print]).

**📝 Example PQP Question (June 2026 Q4(a)):**

Briefly explain the Access Matrix Security Model that can possibly be implemented in operating systems with the help of an example. *(10 marks)*

> **🗓️ Asked In Papers:** [June 2026 Q4(a)](/bca_new/mcs203/pqp/MCS-203_June_2026.pdf ':ignore')
