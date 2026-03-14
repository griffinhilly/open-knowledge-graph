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
