---
id: single-cycle-processor-design
title: Single-Cycle Processor Architecture
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: instruction-fetch-decode-execute
  type: hard
- id: finite-state-machine-processor-design
  type: soft
builds-toward:
- multi-cycle-processor-design
- instruction-level-parallelism
tags:
- processor-design
- single-cycle
- architecture
stage: formal-systems
status: draft
---

# Single-Cycle Processor Architecture

## Core Idea
A single-cycle processor completes one instruction per clock cycle: fetch, decode, execute, memory access, and writeback all happen in a single clock period. The clock period must accommodate the longest critical path through all stages. This design is simple and has no pipeline hazards, but the slow clock limits performance.

## Questions

```yaml
- question: "A single-cycle processor supports three instruction types with these critical path delays: R-type = 600ps, branch = 500ps, load word = 800ps. What must the clock period be, and what is the CPI?"
  type: multiple-choice
  options:
    - "633ps clock period, CPI = 1 (weighted average of the three)"
    - "800ps clock period, CPI = 1"
    - "600ps clock period, CPI varies by instruction type"
    - "800ps clock period, CPI = 1.3 (averaged over instruction types)"
  answer: 1
  explanation: "In a single-cycle design, the clock period must accommodate the longest critical path so that every instruction can complete in one cycle. That means 800ps — set by the load word instruction. Every instruction, including the 500ps branch, must wait this full period. CPI is always exactly 1 for single-cycle: by definition, each instruction completes in one clock cycle. Option A is wrong because clock period cannot be averaged — the slowest instruction dictates the period. Option D is wrong because CPI is not averaged; it is structurally 1."

- question: "Why is the single-cycle processor rarely used in real systems despite its simplicity?"
  type: multiple-choice
  options:
    - "Its CPI is too high — many instructions require 3–5 cycles"
    - "It requires complex pipeline hazard detection logic that adds overhead"
    - "The clock must run at the speed of the slowest instruction, so faster instructions waste most of their clock period"
    - "It cannot support load and store instructions because they require two memory accesses"
  answer: 2
  explanation: "The fundamental problem is that the clock period is forced to match the critical path of the slowest instruction (typically load word, traversing 5 datapath stages). An ADD instruction that could finish in 600ps must wait the full 800ps clock period. This wasted time multiplies across every simple instruction. Multi-cycle designs and pipelining both exist specifically to reclaim this wasted time. Options A and B describe problems with *other* designs (pipelined processors have CPI > 1 due to hazards; single-cycle has no pipeline). Option D is false — single-cycle processors handle load/store in one clock cycle."

- question: "In a single-cycle processor, an ADD instruction and a LOAD instruction both take exactly one clock cycle to complete, even though ADD uses fewer datapath stages."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of a single-cycle processor — CPI = 1 for every instruction, regardless of complexity. ADD may use fewer stages (no data memory access), but the clock period is set by the slowest instruction (LOAD). ADD finishes its work early and then 'idles' until the clock ticks. This is the waste that motivates multi-cycle and pipelined designs, where ADD would get a shorter cycle or where multiple instructions overlap."

- question: "In a single-cycle processor, reducing the number of instructions in a program directly reduces execution time, regardless of which instruction types are used."
  type: true-false
  answer: false
  explanation: "While fewer instructions generally help, the relationship is not that simple. Execution time = instruction count × CPI × clock period. In a single-cycle processor, CPI = 1 and the clock period is fixed at the critical path delay (e.g., 800ps). If you reduce the count but replace simple instructions with complex ones (e.g., more load words), the clock period doesn't change — the 800ps is already set by load. However, if a redesign could eliminate the slowest instruction type entirely, the critical path would shorten and the clock could run faster, reducing execution time beyond the instruction count reduction."

- question: "Why is CPI always exactly 1 in a single-cycle processor, and what is the fundamental performance cost of this design choice?"
  type: short-answer
  answer: "CPI = 1 because the entire datapath is combinational — signals propagate from instruction fetch through register write-back in one continuous path, and the clock triggers exactly once per instruction. The performance cost is that the clock period must equal the delay of the slowest instruction (typically load word). Every simpler instruction, no matter how fast it could finish, must wait for this long clock period. The processor spends most of its time on simple instructions that do not need data memory access, yet all are penalized equally by the slow clock required by the rare load/store instructions."
  explanation: "This is why multi-cycle designs split instructions into variable-length phases (each taking one short cycle) and why pipelines overlap multiple instructions. Both approaches reclaim the time wasted by the single-cycle design's uniformly long clock period. CPI = 1 is conceptually simple but operationally wasteful."
```

## Explainer

You know from studying the CPU datapath that executing an instruction requires several operations: fetching the instruction from memory, decoding which operation to perform and which registers to use, executing the computation in the ALU, potentially accessing data memory, and writing the result back to a register. A **single-cycle processor** performs all of these operations in one clock cycle — signals ripple through the entire datapath from instruction memory to register write-back before the clock ticks again.

To see how this works concretely, trace an R-type instruction like `add $t0, $t1, $t2`. The **program counter** feeds an address to instruction memory, which outputs the 32-bit instruction. The decode logic extracts register specifiers and sends them to the **register file**, which outputs the values in $t1 and $t2. These values flow into the **ALU**, which computes their sum. The result travels past the data memory (unused for this instruction — controlled by MUXes you studied earlier) and arrives at the register file's write port, where it is stored in $t0. All of this — memory read, register read, ALU computation, register write — must complete within a single clock period. No intermediate values are stored; every signal propagates combinationally from input to output.

The fatal weakness of this design is the **critical path** problem. Different instructions use different parts of the datapath: an `add` never touches data memory, but a `lw` (load word) must read from data memory after the ALU computes the address. The clock period must be long enough for the *slowest* instruction to complete — typically `lw`, which traverses instruction memory, register file, ALU, data memory, and register write-back in sequence. Every other instruction, no matter how simple, must wait for this same long clock period. An `add` that could finish in 600 picoseconds is forced to wait 800 picoseconds because `lw` needs the extra time. This means the processor's clock frequency is dictated by its most complex instruction, wasting time on every simpler one.

Despite this inefficiency, the single-cycle design is valuable as a conceptual foundation. It is the simplest complete processor architecture: no pipeline registers, no hazards, no forwarding logic, no stall control. Every instruction takes exactly one cycle, so CPI (cycles per instruction) is always 1 — performance depends entirely on clock speed. Understanding its limitations motivates the multi-cycle design (which breaks execution into variable-length steps to avoid the critical-path penalty) and pipelining (which overlaps multiple instructions to reclaim the wasted time). The single-cycle processor is rarely built in practice, but it is the baseline against which all more sophisticated designs are measured.
