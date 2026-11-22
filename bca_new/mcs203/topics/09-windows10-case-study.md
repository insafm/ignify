# 09. Case Study: Windows 10 Architecture

> **Syllabus Unit:** Block 4 Unit 1 | **Rank:** #9 | **Frequency Score:** 4.2 | **Offered Marks:** 60 | **Papers Present:** 5/9 | **Importance:** Medium  
> **Coverage:** 5 canonical questions across all 9 TEE papers (Dec 2021 – Dec 2025), ranked by historical repetition and examiner emphasis.

---

## ❓ Question Bank & Canonical Answers

### Q071: Describe the Virtual Memory architecture, demand paging, and page files in Windows 10. :id=q071

🟠 **High Priority** • **Asked in: June 2022 Q1(c), June 2024 Q1(d) (10 Marks)** • *Theory / Windows Architecture*

**💡 Key Answer Points:**
- **Flat 64-Bit Address Space:** Each 64-bit user-mode process in Windows 10 is allocated a private, flat logical address space of up to **128 TB**, with the operating system reserving the remaining high-order virtual address space.
- **Demand Paging Implementation:** Pages are mapped via two-level or four-level page table trees and brought into physical RAM only upon reference (demand paging).
- **Working Set Management:**
  - Every process is assigned a **Working Set** (the collection of pages currently resident in physical memory).
  - The Windows Memory Manager dynamically trims working sets of idle background apps when free system RAM drops below threshold watermarks.
- **Page Files (`pagefile.sys`):** Windows 10 supports multiple concurrent paging files on disk to back private, modified virtual pages that cannot be recreated from executable binaries.

> **🗓️ Asked In Papers:** `June 2022 Q1(c), June 2024 Q1(d)`

---

### Q072: Explain Memory Compression in Windows 10 and how it improves system responsiveness. :id=q072

🟠 **High Priority** • **Asked in: Dec 2021 Q1(d) (10 Marks)** • *Theory / Memory Optimization*

**💡 Key Answer Points:**
- **The Classical Bottleneck:** In traditional operating systems, when physical memory fills up, modified pages are written directly to secondary disk storage (`pagefile.sys`). Disk I/O latencies (even on SSDs) cause noticeable application stutter.
- **Memory Compression Mechanism:**
  - Instead of immediately flushing least-recently-used pages to disk, Windows 10 compresses the pages using an in-memory compression algorithm.
  - The compressed pages are stored inside a dedicated in-memory pool called the **Compressed Memory Store** (visible as the "System and compressed memory" process in Task Manager).
- **Performance Benefits:**
  - Reduces disk I/O operations by up to 50–70%.
  - Increases the effective capacity of physical RAM without hardware upgrades.
  - Retrieving a compressed page from RAM requires microsecond CPU decompression, which is thousands of times faster than waiting for secondary disk retrieval.

> **🗓️ Asked In Papers:** `Dec 2021 Q1(d)`

---

### Q073: Detail the file management system of Windows 10, highlighting NTFS features and Journaling (Transaction Logging). :id=q073

🔴 **Very High Priority** • **Asked in: Dec 2021 Q4(a), June 2023 Q5(b) (10 Marks)** • *Theory / NTFS File System*

**💡 Key Answer Points:**
- **NTFS (New Technology File System) Architecture:** The default filesystem for Windows 10, designed for massive volume capacities, reliability, and security.
- **The Master File Table (MFT):**
  - The heart of an NTFS volume. Every file and directory is represented by at least one 1 KB record in the MFT.
  - Small files (< 700 bytes) are stored directly inside the MFT record itself (Resident Attributes), eliminating separate disk data seeks.
- **NTFS Journaling (Transaction Logging):**
  - NTFS implements a **Metadata Journal** via the `$LogFile` system service.
  - Before any structural filesystem change is executed on disk (e.g., file creation, directory rename), the transaction is written to the circular journal on disk.
  - If a power outage or crash occurs mid-write, the NTFS recovery engine parses the `$LogFile` during reboot, rolling back uncommitted transactions and rolling forward committed ones. This completely eliminates the need for slow `chkdsk` sweeps.
- **Advanced Features:** Encrypting File System (EFS), native file compression, volume shadow copy, and POSIX hard links.

> **🗓️ Asked In Papers:** `Dec 2021 Q4(a), June 2023 Q5(b)`

---

### Q074: Explain Process Management and Thread Scheduling in Windows 10. :id=q074

🟡 **Medium Priority** • **Asked in: Dec 2023 Q3(b) (10 Marks)** • *Theory / Scheduling*

**💡 Key Answer Points:**
- **Thread-Based Execution:** Windows 10 schedules **threads**, not processes. A process is simply a container holding an address space, security tokens, and handles.
- **Priority Structure (32 Priority Levels, 0 to 31):**
  - **Real-Time Class (Levels 16–31):** Fixed-priority threads that do not change dynamically (e.g., audio drivers).
  - **Variable Class (Levels 1–15):** Dynamic priorities for normal user applications.
  - **Zero-Page Thread (Level 0):** System thread that zeros out free memory frames when the CPU is otherwise idle.
- **Dynamic Priority Boosting:** The Windows scheduler dynamically boosts the priority of a thread in the variable class when:
  - An I/O operation completes (boosts interactive responsiveness).
  - The thread's GUI window receives user keyboard or mouse input.
  - A thread suffers starvation in the ready queue for over 4 seconds (Balance Set Manager boost).

> **🗓️ Asked In Papers:** `Dec 2023 Q3(b)`

---

### Q075: Detail Inter-Process Communication (IPC) mechanisms in Windows 10. :id=q075

🟡 **Medium Priority** • **Asked in: Dec 2024 Q2(a) (10 Marks)** • *Theory / IPC Mechanisms*

**💡 Key Answer Points:**
Windows 10 provides a versatile suite of IPC mechanisms:
1. **Advanced Local Procedure Calls (ALPC):** High-speed, message-passing mechanism used for communication between user-mode processes and kernel executive subsystems (e.g., Win32 subsystem).
2. **Named Pipes:** Byte-stream communication channels supporting two-way communication between processes on the same machine or across a local area network.
3. **Mailslots:** Lightweight one-way broadcast mechanism across a local network subnet.
4. **Shared Memory (Section Objects):** Allows two processes to map the same physical memory frames into their respective virtual address spaces for instantaneous data transfer.
5. **Component Object Model (COM / DCOM):** Object-oriented IPC framework allowing software components to interact across process boundaries.

> **🗓️ Asked In Papers:** `Dec 2024 Q2(a)`
