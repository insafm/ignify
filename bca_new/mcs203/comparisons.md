# ⚖️ Most Repeated Comparison Questions in MCS-203

> Comparison questions represent IGNOU's most reliable **5- to 10-mark structural template**. In virtually every MCS-203 Term-End Examination, examiners ask between two and four direct differentiation questions. Structuring these answers in tabular form with precise operating system terminology guarantees maximum marks.

---

## 📊 Comparison Frequency Leaderboard

| Comparison Pair | Related Canonical Question | Historical Frequency | Total Marks | Most Recent Appearance |
| :--- | :---: | :---: | :---: | :---: |
| **Segmentation vs. Paging** | [Q018](/bca_new/mcs203/topics/02-memory-management?id=q018) | **4** | 35 | `June 2026 Q1(c)` |
| **Windows 10 vs. Linux Operating System** | [Q075](/bca_new/mcs203/topics/09-windows10-case-study?id=q075) | **3** | 25 | `June 2026 Q4(b)` |
| **Symbian OS vs. Android OS** | [Q005](/bca_new/mcs203/topics/01-mobile-os?id=q005) | **3** | 25 | `Dec 2025 Q5(c)` |
| **Process vs. Thread** | [Q063](/bca_new/mcs203/topics/08-process-cpu-scheduling?id=q063) | **3** | 20 | `Dec 2023 Q3(b)` |
| **Loosely-Coupled vs. Tightly-Coupled Systems** | [Q039](/bca_new/mcs203/topics/03-multiprocessor-distributed?id=q039) | **3** | 20 | `Dec 2024 Q4(c)` |
| **Security Policy vs. Security Model** | [Q050](/bca_new/mcs203/topics/05-linux-case-study?id=q050) | **2** | 15 | `Dec 2022 Q2(a)` |
| **Overlays vs. Swapping** | [Q022](/bca_new/mcs203/topics/02-memory-management?id=q022) | **2** | 15 | `Dec 2022 Q3(a)` |
| **CPU-Bound vs. I/O-Bound Programs** | [Q065](/bca_new/mcs203/topics/08-process-cpu-scheduling?id=q065) | **2** | 15 | `Dec 2025 Q1(a)` |
| **SCAN vs. C-SCAN Disk Scheduling** | [Q057](/bca_new/mcs203/topics/07-file-disk-management?id=q057) | **2** | 15 | `June 2023 Q1(b)` |
| **Master-Slave vs. Separate Supervisor OS** | [Q038](/bca_new/mcs203/topics/03-multiprocessor-distributed?id=q038) | **2** | 15 | `June 2025 Q4(b)` |
| **Test-and-Set vs. Compare-and-Swap (CAS)** | [Q035](/bca_new/mcs203/topics/03-multiprocessor-distributed?id=q035) | **2** | 15 | `Dec 2023 Q2(b)` |
| **Linked Allocation vs. Indexed Allocation** | [Q056](/bca_new/mcs203/topics/07-file-disk-management?id=q056) | **2** | 15 | `June 2022 Q4(a)` |
| **Paged Segmentation vs. Segmented Paging** | [Q020](/bca_new/mcs203/topics/02-memory-management?id=q020) | **1** | 10 | `Dec 2021 Q2(a)` |
| **Qualcomm Snapdragon vs. Intel Atom** | [Q011](/bca_new/mcs203/topics/01-mobile-os?id=q011) | **1** | 10 | `June 2023 Q4(b)` |
| **Rule-Based Access Control vs. Role-Based Access Control** | [Q050](/bca_new/mcs203/topics/05-linux-case-study?id=q050) | **1** | 10 | `June 2025 Q5(d)` |

---

## 📝 Detailed Comparison Guides & Answer Templates

### ⚖️ 1. Segmentation vs. Paging

[**Q018**](/bca_new/mcs203/topics/02-memory-management?id=q018) • **Asked 4 times (35 marks)** • *Recent: Dec 2024 Q5(b), June 2023 Q1(c)*

| Feature / Dimension | Paging | Segmentation |
| :--- | :--- | :--- |
| **Basic Concept** | Divides physical memory into fixed-sized blocks (frames) and logical memory into same-sized blocks (pages). | Divides memory into variable-sized, logically cohesive modules (segments) based on user view. |
| **Unit Size** | Fixed block size (typically 4 KB or 8 KB), determined by hardware architecture. | Variable block size, determined by program segment length (code, data, stack, heap). |
| **Programmer Visibility** | **Invisible** to the programmer; handled transparently by the operating system and MMU. | **Visible** to the programmer; logical addresses are explicitly structured as $\langle \text{segment}, \text{offset} \rangle$. |
| **Hardware Mapping Table** | **Page Table** maps page number $p$ to frame number $f$. | **Segment Table** maps segment number $s$ to $\langle \text{Base}, \text{Limit} \rangle$. |
| **Internal Fragmentation** | **Suffers from internal fragmentation** in the final page of a process (average half page size). | **No internal fragmentation** because segment allocations match requested sizes exactly. |
| **External Fragmentation** | **Zero external fragmentation**; any free frame can be allocated to any process page. | **Suffers from external fragmentation** as segments are loaded/removed, requiring compaction. |
| **Protection & Sharing** | Protection bits applied per page; sharing code requires shared page table entries. | Natural protection and sharing: an entire procedure, function, or array forms a single segment. |

---

### ⚖️ 2. Symbian OS vs. Android OS

[**Q005**](/bca_new/mcs203/topics/01-mobile-os?id=q005) • **Asked 3 times (25 marks)** • *Recent: Dec 2025 Q5(c), Dec 2021 Q5(c)*

| Evaluation Criteria | Symbian OS | Android OS |
| :--- | :--- | :--- |
| **Kernel Architecture** | Built on a **Microkernel** architecture (EPOC/EKA1 and EKA2). | Built on a modified **Monolithic Linux Kernel** (v4.x/v5.x). |
| **User Interface Paradigm** | Static, physical keypad/stylus oriented, low screen resolution. | Modern capacitive multi-touch interface with gesture navigation. |
| **Runtime Environment** | Native Symbian C++ compiled directly to target ARM machine code. | Virtual Machine runtime: originally **Dalvik VM**, now **Android Runtime (ART)** with AOT/JIT compilation. |
| **Application Ecosystem** | Fragmented, non-standardized distribution; carrier-dependent signing. | Centralized **Google Play Store** with APK/AAB package signing. |
| **Licensing Policy** | Closed-source proprietary; later open-sourced under EPL before deprecation. | **Open Source** (Android Open Source Project - AOSP) under Apache 2.0 and GPL. |
| **Security Architecture** | Capability-based security model tied to manufacturer developer certificates. | Multi-tier security: Linux UID isolation, App Sandboxing, runtime user permissions, SELinux. |
| **Power Management** | Aggressive hardware sleeping designed for 100–200 MHz CPUs and small batteries. | Advanced software wakelocks, Doze Mode, and App Standby buckets on multi-core SoCs. |

---

### ⚖️ 3. Process vs. Thread

[**Q063**](/bca_new/mcs203/topics/08-process-cpu-scheduling?id=q063) • **Asked 3 times (20 marks)** • *Recent: Dec 2023 Q3(b), Dec 2022 Q1(a)*

| Characteristic | Process | Thread (Lightweight Process) |
| :--- | :--- | :--- |
| **Definition** | An independent executing instance of a program with its own private address space. | A basic unit of CPU execution within a process, sharing memory with sibling threads. |
| **Memory Space** | Has its own independent virtual address space, data segment, code segment, and heap. | Shares code segment, data segment, open file descriptors, and heap with the parent process. |
| **Private State** | PCB, page table, open files, registers, stack pointer, signals. | Unique Thread ID, Program Counter (PC), CPU registers, and private stack. |
| **Creation Overhead** | High overhead: allocating address space, copying page tables (`fork()` system call). | Low overhead: shares existing parent memory structures (`clone()` or `pthread_create()`). |
| **Context Switching Overhead** | Expensive: invalidates MMU translation lookaside buffer (TLB), reloads page tables. | Inexpensive: address space remains unchanged; only registers and stack pointers are swapped. |
| **Communication Mechanism** | Requires Inter-Process Communication (IPC): pipes, message queues, shared memory, sockets. | Direct inter-thread communication via shared variables, mutexes, and condition variables. |
| **Fault Isolation** | High: crash of one process does not affect other processes. | Low: an unhandled exception or memory corruption in one thread can crash the entire process. |

---

### ⚖️ 4. Loosely-Coupled vs. Tightly-Coupled Systems

[**Q039**](/bca_new/mcs203/topics/03-multiprocessor-distributed?id=q039) • **Asked 3 times (20 marks)** • *Recent: Dec 2024 Q4(c), June 2024 Q1(b)*

| Feature | Tightly-Coupled Systems (Multiprocessors) | Loosely-Coupled Systems (Distributed Systems) |
| :--- | :--- | :--- |
| **Physical Architecture** | Multiple processors connected to a **single shared physical RAM** via a high-speed bus/crossbar switch. | Multiple independent autonomous computers connected via a **local or wide area network**. |
| **Memory Access** | Shared Memory: any processor can access any memory location directly using standard load/store instructions. | Distributed Memory: each node possesses its own private physical RAM; no direct remote physical addressing. |
| **Operating System** | Managed by a **single unified operating system instance** coordinating all CPUs. | Each node runs its own independent operating system instance (coordinated via middleware or network protocols). |
| **Inter-node Communication** | Fast shared memory read/writes (nanosecond latencies). | Message passing over network links (millisecond latencies). |
| **Scalability** | Limited scalability (typically 2 to 64 cores before memory bus contention saturates bandwidth). | Highly scalable: can expand to thousands of nodes across data centers without physical bus bottlenecks. |
| **Failure Tolerance** | Low: memory failure or kernel crash usually halts the entire system. | High: independent failure isolation; failure of one node does not crash other nodes. |

---

### ⚖️ 5. Overlays vs. Swapping

[**Q022**](/bca_new/mcs203/topics/02-memory-management?id=q022) • **Asked 2 times (15 marks)** • *Recent: Dec 2022 Q3(a)*

| Feature | Overlays | Swapping |
| :--- | :--- | :--- |
| **Basic Concept** | Program modules that are not required simultaneously share the same physical memory space. | Entire processes (or processes' complete memory images) are moved between RAM and backing store. |
| **Management Responsibility** | Managed entirely by the **programmer / compiler**; requires manual overlay drivers. | Managed entirely by the **operating system** (Medium-Term Scheduler) without programmer involvement. |
| **Hardware / OS Support** | Requires no special OS memory management hardware support; works on simple real-mode memory. | Requires OS process state tracking, swap space management on disk, and MMU address translation. |
| **Granularity** | Sub-process granularity: only selected code/data modules within one program are swapped in/out. | Whole-process granularity: the entire memory allocation of a process is suspended to disk. |
| **Primary Goal** | Allows a single large program to execute in a physical memory space smaller than the program binary. | Regulates the **degree of multiprogramming** by swapping out idle/blocked processes to free RAM. |

---

### ⚖️ 6. Security Policy vs. Security Model

[**Q050**](/bca_new/mcs203/topics/05-linux-case-study?id=q050) • **Asked 2 times (15 marks)** • *Recent: Dec 2022 Q2(a), June 2025 Q5(d)*

| Dimension | Security Policy | Security Model |
| :--- | :--- | :--- |
| **Definition** | A high-level, human-readable specification of security rules, rights, and organizational goals. | A formal, mathematical abstraction that translates security policies into concrete system algorithms. |
| **Focus** | Defines **"WHAT"** data assets need protection and who is authorized to perform which actions. | Defines **"HOW"** the operating system enforces access rights and guarantees state consistency. |
| **Examples** | "Medical records can only be viewed by attending physicians", "Financial transactions must be audited". | Bell-LaPadula Model (Confidentiality), Biba Model (Integrity), Access Control Matrix (ACM), RBAC. |
| **Enforcement Mechanism** | Implemented through organizational policies, compliance rules, and legal frameworks. | Implemented inside the OS kernel via reference monitors, file permission bits, and access control lists (ACLs). |
| **Verifiability** | Subjective; verified through external administrative audits and employee compliance checks. | Mathematically provable; states can be formally verified as secure or insecure. |

---

### ⚖️ 7. SCAN vs. C-SCAN Disk Scheduling

[**Q057**](/bca_new/mcs203/topics/07-file-disk-management?id=q057) • **Asked 2 times (15 marks)** • *Recent: June 2023 Q1(b), Dec 2021 Q4(a)*

| Aspect | SCAN (Elevator Algorithm) | C-SCAN (Circular SCAN) |
| :--- | :--- | :--- |
| **Arm Movement Pattern** | Moves back and forth across the disk surface, reversing direction when it reaches the disk boundary. | Moves in only **one direction**, servicing requests until the end, then immediately returns to cylinder 0 without servicing. |
| **Service Uniformity** | **Non-uniform wait times**: requests near the boundary just visited wait longest, while middle tracks get frequent service. | **Uniform wait times**: treats cylinders as a circular list, providing uniform waiting times for all requests across the disk. |
| **Head Travel Distance** | Typically achieves lower total head seek distances under light to medium workloads. | Incurs extra track traversal for the return sweep, but optimizes response time under heavy uniform request loads. |
| **Boundary Handling** | Continues servicing requests as it reverses direction at cylinder 0 or cylinder $MAX$. | Immediately jumps from cylinder $MAX$ back to cylinder 0 without servicing I/O requests on the return journey. |

---

### ⚖️ 8. Windows 10 vs. Linux Operating System

[**Q075**](/bca_new/mcs203/topics/09-windows10-case-study?id=q075) • **Asked 3 times (25 marks)** • *Recent: June 2026 Q4(b), Dec 2023 Q5(c)*

| Evaluation Metric | Microsoft Windows 10 | Linux Operating System (GNU/Linux) |
| :--- | :--- | :--- |
| **Kernel Architecture** | **Hybrid Kernel** (Windows NT Executive with user-mode subsystems and microkernel core). | **Monolithic Kernel** with dynamically loadable kernel modules (LKMs). |
| **Licensing & Source Code** | Proprietary closed-source; commercial licensing fee per installation. | **Open-Source** (GPLv2 / free software); source code is completely auditable and customizable. |
| **File System & Hierarchy** | Drive-letter based (`C:\`, `D:\`) with **NTFS** (features Master File Table and `$LogFile` journaling). | Unified single-rooted hierarchical tree (`/`) with **ext4 / XFS / Btrfs**; everything is treated as a file. |
| **Package Management** | Traditional manual installers (`.exe`, `.msi`) or Windows Store; updates often require system reboots. | Centralized repository package managers (`apt`, `yum`, `pacman`) with non-disruptive live updates. |
| **System Security & Permissions** | Access Control Lists (ACLs), User Account Control (UAC) prompts, and Windows Defender. | Strict POSIX user/group/other permissions (`rwx`), root superuser separation, and kernel **SELinux/AppArmor**. |
| **Resource Efficiency & CLI** | Higher RAM and background resource footprint; heavy graphical overhead. | Highly lightweight, capable of running in headless CLI mode on servers and resource-constrained hardware. |
| **5 Reasons for Choosing Linux (June 2026 Q4(b))** | 1. Superior server stability & zero reboot updates<br>2. Complete customizability and open-source auditability<br>3. Powerful native POSIX shell & development tooling<br>4. High security with granular SELinux isolation<br>5. Zero licensing cost for multi-instance deployments | 1. Unmatched commercial gaming & DirectX support<br>2. Universal consumer hardware driver compatibility<br>3. Dominant enterprise productivity software (MS Office)<br>4. Consistent user-friendly GUI across all machines<br>5. Centralized corporate Active Directory integration |
