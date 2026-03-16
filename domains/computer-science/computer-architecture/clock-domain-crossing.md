---
id: clock-domain-crossing
title: Clock Domain Crossing and Synchronization
domain: computer-science
course: computer-architecture
prerequisites:
- id: synchronous-logic-and-clocks
  type: hard
- id: flip-flops-and-latches
  type: soft
builds-toward:
- multi-core-system-design
tags:
- asynchronous
- synchronization
- metastability
stage: formal-systems
status: draft
---

# Clock Domain Crossing and Synchronization

## Core Idea
When signals cross between clock domains running at different speeds, metastability—where a flip-flop output is neither 0 nor 1—can occur. Synchronizers using cascaded flip-flops (or special synchronization circuits) reduce metastability probability to acceptable levels. This is critical in multi-core and peripheral integration.

## Explainer

From your study of synchronous logic, you know that a flip-flop samples its input at the clock edge and holds a stable output until the next edge. This works perfectly when everything runs on the same clock — the setup and hold time requirements are met, and data flows predictably through the pipeline. But modern systems rarely have a single clock. A CPU core might run at 3 GHz, its memory interface at 800 MHz, a USB controller at 48 MHz, and a network interface at its own frequency. Whenever a signal generated in one clock domain needs to be read in another, you face the **clock domain crossing** problem.

The core issue is **metastability**. A flip-flop needs its input to be stable for a brief window around the clock edge (the setup and hold times you learned about with flip-flops and latches). When a signal arrives from a different clock domain, there is no guarantee about *when* it transitions relative to the receiving clock. If the signal changes right at the clock edge — within the setup/hold window — the flip-flop enters a metastable state where its output voltage hovers between 0 and 1, neither a valid logic high nor a valid logic low. It will eventually resolve to one or the other, but how long that takes is probabilistic. If downstream logic reads the output before it resolves, the ambiguous value can propagate through the circuit, causing unpredictable and catastrophic failures.

The standard solution is a **synchronizer**, typically built from two (or more) flip-flops in series, both clocked by the receiving domain's clock. The first flip-flop may go metastable, but it has an entire clock period to resolve before the second flip-flop samples its output. This dramatically reduces the probability of metastability reaching the rest of the circuit — with each additional flip-flop stage, the failure probability drops exponentially. A two-flip-flop synchronizer is sufficient for most designs, bringing the mean time between failures (MTBF) to thousands of years or more. The tradeoff is **latency**: the synchronized signal arrives two clock cycles late in the receiving domain.

For multi-bit signals (like a data bus), simple flip-flop synchronizers are not enough — each bit could resolve independently, producing a corrupted value that was never actually sent. The solution is to use structures like **asynchronous FIFOs** with Gray-coded pointers, where only one bit changes at a time when the pointer advances, making single-bit synchronization safe. Alternatively, handshake protocols ensure the sender holds data stable until the receiver acknowledges receipt. These techniques become essential when designing the multi-core systems and peripheral interfaces that define modern computer architecture — any time two independently clocked subsystems must communicate, clock domain crossing is the problem you must solve first.
