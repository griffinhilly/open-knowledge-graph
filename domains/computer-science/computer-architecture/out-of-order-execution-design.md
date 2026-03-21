---
id: out-of-order-execution-design
title: Out-of-Order Execution and Register Renaming
domain: computer-science
course: computer-architecture
prerequisites:
- id: superscalar-and-vliw-design
  type: hard
builds-toward:
- power-thermal-performance-metrics
tags:
- ooo
- execution
- register-renaming
- performance
stage: formal-systems
status: draft
---

# Out-of-Order Execution and Register Renaming

## Core Idea
Out-of-order execution allows instructions to complete before earlier instructions, maximizing hardware utilization. Register renaming removes false data dependencies by mapping logical registers to physical registers, enabling more parallelism.

## Questions

```yaml
- question: "Two instructions both write to register R1 but neither reads the result of the other. A classic in-order pipeline would stall on this hazard. What does register renaming do to resolve it?"
  type: multiple-choice
  options:
    - "It detects that R1 is shared and forces both instructions to wait for a lock on the register"
    - "It assigns each instruction a distinct physical register, eliminating the false dependency entirely"
    - "It reorders the instructions so the second write happens first, preventing the naming conflict"
    - "It routes both writes through the reorder buffer, which serializes them at commit time"
  answer: 1
  explanation: "The WAW (write-after-write) hazard here is a *false dependency* — no actual data flows between the two instructions; they just happen to target the same architectural register name. Register renaming resolves this by mapping each write to a fresh physical register from a pool. The two instructions now write to different physical locations and can execute simultaneously. Only true RAW (read-after-write) dependencies — where one instruction genuinely needs another's result — remain after renaming. Options A and D describe serialization, not elimination; option C describes reordering, which does not resolve the underlying naming conflict."

- question: "Why does out-of-order execution still require instructions to *retire* (commit to architectural state) in program order?"
  type: multiple-choice
  options:
    - "To ensure that each instruction occupies a functional unit for the same number of cycles"
    - "Because register renaming cannot correctly track results committed out of order"
    - "So the processor can recover a consistent architectural state after exceptions or branch mispredictions"
    - "To prevent the reorder buffer from overflowing when many instructions are in flight"
  answer: 2
  explanation: "If instructions committed their results to the visible architectural state as soon as they finished executing, an exception in an early instruction would find that later instructions had already modified registers and memory — making precise recovery impossible. The reorder buffer (ROB) holds completed results and releases them to architectural state strictly in program order, so the committed state always reflects what in-order execution would have produced up to that point. This invariant enables precise exception handling and recovery from branch mispredictions."

- question: "Register renaming in out-of-order processors eliminates all data dependencies between instructions."
  type: true-false
  answer: false
  explanation: "Register renaming eliminates only *false dependencies* — WAW (write-after-write) and WAR (write-after-read) hazards that arise purely from reuse of the same register name. It cannot eliminate true RAW (read-after-write) dependencies, where one instruction genuinely needs the result produced by an earlier instruction. Those real dependencies still enforce ordering constraints. The power of renaming is removing the artificial constraints introduced by the ISA's limited number of architectural registers, revealing the true data-flow graph."

- question: "Instructions in an out-of-order processor may execute in a different order than they were issued, and they also retire (commit to the architectural register file) in a different order than they were issued."
  type: true-false
  answer: false
  explanation: "Out-of-order *execution* is the entire point: instructions execute as soon as their inputs are ready, regardless of program order. But *retirement* (committing results to the visible architectural state) always happens in program order, enforced by the reorder buffer (ROB). This in-order retirement is essential for precise exception handling — the processor can always roll back to a consistent state. Conflating execution order with retirement order is a common confusion about OoO processors."

- question: "What is the role of the reorder buffer (ROB) in an out-of-order processor, and why is it necessary?"
  type: short-answer
  answer: "The ROB holds results of instructions that have finished executing but have not yet been committed to the architectural state. It ensures that despite out-of-order execution, instructions retire strictly in program order. This is necessary for precise exceptions: if an instruction causes an exception, all instructions before it in program order can be committed and all after it can be squashed, leaving a consistent state for recovery. Without the ROB, out-of-order commits would make recovery from exceptions or branch mispredictions impossible."
  explanation: "The ROB reconciles the performance goal (execute out of order) with the correctness requirement (maintain sequential semantics). It also enables branch misprediction recovery: the ROB can flush all instructions after the mispredicted branch, restoring the last known-good committed state. The ROB, reservation stations, and rename tables together are the core microarchitectural structures that make OoO execution work."
```

## Explainer

From your study of superscalar and VLIW design, you know that processors try to execute multiple instructions simultaneously. But a major obstacle is **data dependencies**: if instruction B needs the result of instruction A, B must wait for A to finish. In-order processors stall the entire pipeline when they hit a dependency, even if later independent instructions could execute right now. **Out-of-order execution** (OoO) solves this by allowing instructions to execute as soon as their operands are ready, regardless of their original program order. The processor dynamically reorders execution to fill every functional unit every cycle.

The key mechanism enabling this is a structure called the **reorder buffer** (ROB). Instructions enter the ROB in program order and are dispatched to execution units as their inputs become available — potentially out of order. When an instruction completes, its result is written to the ROB but not yet committed to the architectural state. The ROB ensures that instructions **retire** (commit their results) strictly in program order, so the processor can always recover a consistent state if an exception or branch misprediction occurs. Think of it as a factory where workers tackle tasks in whatever order is most efficient, but the shipping department sends finished products out the door in the original order.

**Register renaming** is the companion technique that unlocks much of OoO's potential. Consider two instructions that both write to the same register but are otherwise independent — this creates a **write-after-write** (WAW) hazard, or a **write-after-read** (WAR) hazard if one reads the register before the other writes it. These are called **false dependencies** because there is no actual data flow between the instructions; they just happen to reuse the same register name. Register renaming eliminates these by maintaining a pool of **physical registers** far larger than the set of **architectural registers** visible to the programmer. Each time an instruction writes to a logical register, the processor assigns a fresh physical register, so the two "conflicting" instructions actually write to different locations. Only true **read-after-write** (RAW) dependencies — where one instruction genuinely needs another's result — remain.

The hardware cost of out-of-order execution is substantial: the reorder buffer, register rename tables, reservation stations (where instructions wait for operands), and the associative logic to wake up waiting instructions all consume significant chip area and power. This is why simpler embedded processors often skip OoO entirely, and why VLIW architectures tried to push this reordering work to the compiler instead. But for general-purpose processors running unpredictable workloads, OoO execution with register renaming remains the dominant approach because it extracts parallelism that compilers cannot always find statically, adapting dynamically to the actual data flow at runtime.
