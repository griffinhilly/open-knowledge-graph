---
id: processor-affinity-and-cpu-binding
title: Processor Affinity and CPU Binding
domain: computer-science
course: operating-systems
prerequisites:
- id: context-switching-and-cpu-dispatch
  type: hard
- id: cpu-scheduling-basics
  type: soft
tags:
- scheduling
- multiprocessor
- optimization
stage: formal-systems
status: draft
---

# Processor Affinity and CPU Binding

## Core Idea
Processor affinity controls which CPUs a process or thread can execute on, enabling cache optimization and NUMA-aware scheduling. Hard affinity strictly restricts execution to specific CPUs; soft affinity expresses a preference while allowing migration if necessary. Binding processes to CPUs can improve cache hit rates and memory locality on multiprocessor and NUMA systems.

## Questions

```yaml
- question: "A web server process runs for 10ms on Core 2, gets preempted, and the scheduler migrates it to Core 5. What is the primary performance cost of this migration?"
  type: multiple-choice
  options:
    - "Core 5 runs at a lower clock speed than Core 2"
    - "The process must rebuild its working set in Core 5's cache, fetching data from slower shared cache or main memory"
    - "Migrating a process requires copying its memory to Core 5's local memory bank"
    - "The scheduler takes longer to dispatch on Core 5 because it must load new CPU state"
  answer: 1
  explanation: "When a process runs on Core 2, Core 2's L1 and L2 caches fill with the process's recently accessed data — its cache is 'warm.' When the process migrates to Core 5, Core 5's cache has no knowledge of this process and is 'cold.' The process must re-fetch all its working data from the shared L3 cache or DRAM, which is orders of magnitude slower than L1/L2. The migration itself (saving and restoring register state) is fast; the cache cold-start penalty is the real cost."

- question: "On a 2-socket NUMA server, a database process is pinned to cores on socket 0 but its data buffers were allocated in socket 1's memory. What is the consequence?"
  type: multiple-choice
  options:
    - "The process cannot access socket 1's memory and will crash"
    - "Every memory access must cross the inter-socket interconnect, incurring 2–3x the latency of local memory access"
    - "The OS will automatically migrate the data to socket 0's memory over time"
    - "Performance is identical because modern NUMA systems use cache coherence to hide the difference"
  answer: 1
  explanation: "On NUMA systems, each socket has its own memory bank. Memory accesses to local memory are fast; accesses to a remote socket's memory must cross the interconnect (QPI, Infinity Fabric, etc.), which adds significant latency — typically 2–3x slower than local access. Cache coherence ensures *correctness* across sockets but does not eliminate the latency penalty. This is why NUMA-aware memory allocation (ensuring threads and their data live on the same socket) is as important as CPU binding."

- question: "Processor affinity improves performance by preventing the OS scheduler from migrating a process to a CPU whose cache does not contain the process's working set."
  type: true-false
  answer: true
  explanation: "This is precisely the mechanism: the CPU's hardware cache builds up a warm working set for a process over time. If the scheduler migrates the process to a different core, that cache warmth is lost and must be rebuilt from scratch. Processor affinity — whether soft (preference) or hard (restriction) — keeps the process on the core whose cache is already warm, reducing expensive cache misses. The hardware built the locality; affinity prevents the scheduler from discarding it."

- question: "Hard affinity is always preferable to soft affinity because it guarantees the process always runs on a warm cache."
  type: true-false
  answer: false
  explanation: "Hard affinity trades scheduling flexibility for cache locality. If pinned cores are busy and other cores sit idle, the scheduler cannot use those idle cores even when the pinned threads are waiting. This can cause load imbalance and hurt overall throughput. Soft affinity achieves most of the cache benefit — it tries to keep processes on their home core — while preserving the freedom to migrate when load balancing requires it. Hard affinity is the right choice for latency-sensitive applications (real-time audio, HFT) but often the wrong default for general workloads."

- question: "Why is processor affinity described as preventing the scheduler from 'undoing' something the hardware has already built up? What has the hardware built up, and how does migration undo it?"
  type: short-answer
  answer: "The hardware — specifically the CPU's L1 and L2 caches — builds up a warm working set for a running process over time. As the process accesses memory, the cache hierarchy loads frequently used data into fast local cache. When the OS migrates the process to a different core, that core's cache contains no data relevant to the process; the process must re-fetch everything from the slower shared L3 cache or DRAM. The work the cache hierarchy did — anticipating the process's memory needs — is discarded. Processor affinity prevents this by keeping the process on the same core whose cache already contains its working set."
  explanation: "This framing clarifies that processor affinity is a cache management strategy, not a CPU speed-up or priority mechanism. The processor itself isn't faster; you're simply avoiding the penalty of cold-cache restarts. It also explains why soft affinity captures most of the benefit: rare migrations don't eliminate the advantage, only frequent ones do."
```

## Explainer

From your study of context switching and CPU dispatch, you know that when the OS switches a process off a CPU, it saves the process's register state and loads another process's state onto that core. What you may not have considered is what happens to the data that process left behind in the CPU's cache. Each core maintains its own L1 and L2 caches filled with the recently accessed memory of whatever was running on it. When a process is dispatched back to the *same* core, those cache lines may still be warm — the data the process needs is already sitting in fast local memory. If the scheduler moves the process to a *different* core, the new core's cache is cold for that process, and it must re-fetch everything from slower shared cache or main memory. This is the performance problem that **processor affinity** addresses.

**Soft affinity** is the default behavior in most modern schedulers: the OS *prefers* to schedule a process back onto the core it last ran on, but will migrate it to another core if that core is idle and the home core is busy. This is a best-effort optimization — it improves cache hit rates on average without creating load imbalance. **Hard affinity**, by contrast, is an explicit constraint set by the programmer or administrator. It restricts a process or thread to a specific set of CPUs and the scheduler will never move it outside that set, even if those cores are overloaded and others sit idle.

Hard affinity becomes critical on **NUMA (Non-Uniform Memory Access)** systems, where each CPU socket has its own local memory bank. Accessing local memory is fast; accessing a remote socket's memory can take two to three times as long. If a process's data lives in socket 0's memory but the scheduler moves the process to socket 1, every memory access crosses the interconnect. By binding the process to the cores on socket 0, you guarantee that memory accesses stay local. Database servers, real-time audio processing, and high-frequency trading systems routinely use CPU binding for this reason.

The tradeoff is straightforward: affinity improves cache and memory locality at the cost of scheduling flexibility. If you pin four threads to four cores and a fifth thread needs CPU time, it cannot use those pinned cores even if the pinned threads are sleeping. On Linux, the `taskset` command and `sched_setaffinity()` system call control hard affinity; on Windows, `SetProcessAffinityMask()` and `SetThreadAffinityMask()` serve the same purpose. The key insight is that processor affinity is not about making the CPU faster — it is about preventing the scheduler from undoing the locality that the hardware cache hierarchy has already built up.
