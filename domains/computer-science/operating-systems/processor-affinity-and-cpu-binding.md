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

## Explainer

From your study of context switching and CPU dispatch, you know that when the OS switches a process off a CPU, it saves the process's register state and loads another process's state onto that core. What you may not have considered is what happens to the data that process left behind in the CPU's cache. Each core maintains its own L1 and L2 caches filled with the recently accessed memory of whatever was running on it. When a process is dispatched back to the *same* core, those cache lines may still be warm — the data the process needs is already sitting in fast local memory. If the scheduler moves the process to a *different* core, the new core's cache is cold for that process, and it must re-fetch everything from slower shared cache or main memory. This is the performance problem that **processor affinity** addresses.

**Soft affinity** is the default behavior in most modern schedulers: the OS *prefers* to schedule a process back onto the core it last ran on, but will migrate it to another core if that core is idle and the home core is busy. This is a best-effort optimization — it improves cache hit rates on average without creating load imbalance. **Hard affinity**, by contrast, is an explicit constraint set by the programmer or administrator. It restricts a process or thread to a specific set of CPUs and the scheduler will never move it outside that set, even if those cores are overloaded and others sit idle.

Hard affinity becomes critical on **NUMA (Non-Uniform Memory Access)** systems, where each CPU socket has its own local memory bank. Accessing local memory is fast; accessing a remote socket's memory can take two to three times as long. If a process's data lives in socket 0's memory but the scheduler moves the process to socket 1, every memory access crosses the interconnect. By binding the process to the cores on socket 0, you guarantee that memory accesses stay local. Database servers, real-time audio processing, and high-frequency trading systems routinely use CPU binding for this reason.

The tradeoff is straightforward: affinity improves cache and memory locality at the cost of scheduling flexibility. If you pin four threads to four cores and a fifth thread needs CPU time, it cannot use those pinned cores even if the pinned threads are sleeping. On Linux, the `taskset` command and `sched_setaffinity()` system call control hard affinity; on Windows, `SetProcessAffinityMask()` and `SetThreadAffinityMask()` serve the same purpose. The key insight is that processor affinity is not about making the CPU faster — it is about preventing the scheduler from undoing the locality that the hardware cache hierarchy has already built up.
