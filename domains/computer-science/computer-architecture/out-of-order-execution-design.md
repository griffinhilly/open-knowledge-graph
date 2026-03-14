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
