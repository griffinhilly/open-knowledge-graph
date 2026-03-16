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

## Explainer

From your study of superscalar and VLIW design, you know that processors try to execute multiple instructions simultaneously. But a major obstacle is **data dependencies**: if instruction B needs the result of instruction A, B must wait for A to finish. In-order processors stall the entire pipeline when they hit a dependency, even if later independent instructions could execute right now. **Out-of-order execution** (OoO) solves this by allowing instructions to execute as soon as their operands are ready, regardless of their original program order. The processor dynamically reorders execution to fill every functional unit every cycle.

The key mechanism enabling this is a structure called the **reorder buffer** (ROB). Instructions enter the ROB in program order and are dispatched to execution units as their inputs become available — potentially out of order. When an instruction completes, its result is written to the ROB but not yet committed to the architectural state. The ROB ensures that instructions **retire** (commit their results) strictly in program order, so the processor can always recover a consistent state if an exception or branch misprediction occurs. Think of it as a factory where workers tackle tasks in whatever order is most efficient, but the shipping department sends finished products out the door in the original order.

**Register renaming** is the companion technique that unlocks much of OoO's potential. Consider two instructions that both write to the same register but are otherwise independent — this creates a **write-after-write** (WAW) hazard, or a **write-after-read** (WAR) hazard if one reads the register before the other writes it. These are called **false dependencies** because there is no actual data flow between the instructions; they just happen to reuse the same register name. Register renaming eliminates these by maintaining a pool of **physical registers** far larger than the set of **architectural registers** visible to the programmer. Each time an instruction writes to a logical register, the processor assigns a fresh physical register, so the two "conflicting" instructions actually write to different locations. Only true **read-after-write** (RAW) dependencies — where one instruction genuinely needs another's result — remain.

The hardware cost of out-of-order execution is substantial: the reorder buffer, register rename tables, reservation stations (where instructions wait for operands), and the associative logic to wake up waiting instructions all consume significant chip area and power. This is why simpler embedded processors often skip OoO entirely, and why VLIW architectures tried to push this reordering work to the compiler instead. But for general-purpose processors running unpredictable workloads, OoO execution with register renaming remains the dominant approach because it extracts parallelism that compilers cannot always find statically, adapting dynamically to the actual data flow at runtime.
