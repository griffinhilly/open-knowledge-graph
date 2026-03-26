---
id: pipeline-hazards
title: Pipeline Hazards
domain: computer-science
course: computer-architecture
prerequisites:
- id: pipelining-fundamentals
  type: hard
tags:
- data-hazard
- control-hazard
- structural-hazard
- forwarding
- stall
- branch-prediction
stage: formal-systems
status: validated
---

# Pipeline Hazards

## Core Idea
Pipeline hazards are conditions that prevent the next instruction from executing in its scheduled stage, reducing throughput below ideal. Structural hazards arise when two instructions need the same hardware resource simultaneously. Data hazards occur when an instruction depends on a result not yet written back by a prior instruction. Control hazards arise from branches: the next instruction to execute is not known until the branch resolves. Solutions include pipeline stalls (bubbles), data forwarding (routing results earlier in the pipeline), branch prediction, and delayed branching.

## How It's Best Learned
Trace data hazards in a sequence like 'ADD R1,R2,R3; SUB R4,R1,R5' through a pipeline diagram and identify which cycles require stalls or forwarding. Model a branch misprediction and count the penalty cycles. Compare the CPI impact of each hazard type.

## Common Misconceptions
- Data forwarding does not eliminate all stalls — a load-use hazard (load immediately followed by use of the loaded value) still requires one stall even with full forwarding.
- Branch prediction misses are not errors; they are expected events that the pipeline handles by flushing incorrect instructions and restarting from the correct path.

## Questions

```yaml
- question: "A pipeline has full data forwarding (bypassing) implemented. Consider the instruction sequence: LOAD R1, [addr]; ADD R2, R1, R3. How many stall cycles are required between these two instructions?"
  type: multiple-choice
  options:
    - "Zero — data forwarding eliminates all data hazard stalls"
    - "One — a load-use hazard requires one stall even with full forwarding"
    - "Two — the loaded value is not available until write-back, two stages after execute"
    - "Three — the pipeline must wait until LOAD completes all five stages"
  answer: 1
  explanation: "This is the load-use hazard — the one case where data forwarding cannot eliminate the stall. In a standard 5-stage pipeline, data forwarding routes the result from the end of the execute stage directly to the next instruction's execute input. But a LOAD instruction doesn't have the data until the end of the memory access stage (one stage later than execute). Since ADD needs R1 at its execute stage, which begins one cycle after LOAD's memory stage ends, there is exactly one cycle where the data simply is not available yet. One stall is inserted. The misconception that 'forwarding eliminates all stalls' is the most common error in pipeline hazard analysis."

- question: "A branch instruction is in the pipeline and the branch predictor predicts 'not taken.' Three instructions after the branch have already been fetched speculatively. The branch turns out to be taken. What happens?"
  type: multiple-choice
  options:
    - "The processor raises an exception and restarts from the branch"
    - "The three speculatively fetched instructions are flushed, and the pipeline restarts from the branch target"
    - "The processor stalls until the branch condition is evaluated before fetching any further instructions"
    - "The three instructions complete execution but their results are discarded"
  answer: 1
  explanation: "A branch misprediction causes the pipeline to flush the incorrectly fetched instructions (converting them to bubbles/NOPs) and restart fetching from the correct branch target address. This is not an exception — it is a normal, expected event handled by the pipeline's branch misprediction recovery mechanism. The misprediction penalty is typically 2-3 cycles in a simple pipeline (the number of cycles between branch fetch and when the branch resolves). Critically, the speculatively fetched instructions must be flushed before completing — allowing them to execute would compute wrong results."

- question: "Data forwarding (bypassing) eliminates the need for stall cycles in most data hazard cases."
  type: true-false
  answer: false
  explanation: "False. Data forwarding eliminates stalls for most data hazards — for example, the result of an ADD in the execute stage can be forwarded directly to the next instruction's execute stage, eliminating a 2-cycle stall. But the load-use hazard cannot be solved by forwarding alone. A LOAD instruction's result is only available after the memory access stage, which is one cycle too late to forward directly to the immediately following instruction's execute stage. One stall cycle must still be inserted. This is a common misconception: forwarding is powerful but not a complete solution."

- question: "Branch mispredictions are processor errors that indicate a bug in branch prediction logic; a correctly functioning processor should rarely mispredict a branch."
  type: true-false
  answer: false
  explanation: "False. Branch mispredictions are expected, normal events in any processor with speculative execution. A predictor achieving 95%+ accuracy still mispredicts millions of branches per second in a modern processor running at GHz speeds. A misprediction means the predicted outcome was wrong — not that the hardware malfunctioned. The pipeline is designed to handle mispredictions gracefully by flushing incorrect instructions and restarting from the correct path. Mispredictions cause performance penalties (wasted cycles), not incorrect computation, because the incorrect instructions are flushed before they can commit results."

- question: "Why does a load-use hazard require a stall cycle even when the pipeline has full data forwarding, while a RAW (read-after-write) hazard between two arithmetic instructions does not?"
  type: short-answer
  answer: "In a 5-stage pipeline, arithmetic instructions produce their result at the end of the execute (EX) stage. Data forwarding routes this result directly back to the beginning of the next instruction's EX stage, so consecutive arithmetic instructions can run without stalls. A LOAD instruction, however, doesn't have the data until the end of the memory access (MEM) stage — one full stage later than EX. If the instruction immediately after the load needs that value, it enters its EX stage before the load has even completed MEM. There is no way to forward data that hasn't been retrieved yet; the pipeline must insert one bubble to let the load complete MEM before the dependent instruction begins EX."
  explanation: "The root cause is the pipeline stage at which data becomes available: EX for arithmetic, MEM for loads. Forwarding can only move data forward in time within the pipeline — it cannot make data available before it is physically computed or retrieved from memory. This one-cycle gap between when a load produces data and when the next instruction needs it is structurally unavoidable without deeper pipeline restructuring or out-of-order execution."
```

## Explainer

From pipelining fundamentals, you know the core idea: break instruction execution into stages (fetch, decode, execute, memory access, write-back) and overlap them so multiple instructions are in flight simultaneously. In an ideal 5-stage pipeline, you complete one instruction per clock cycle after the pipeline fills. But this ideal throughput assumes every instruction can enter the pipeline on schedule — **pipeline hazards** are the situations where that assumption breaks down.

**Structural hazards** are the simplest to understand: two instructions need the same hardware at the same time. Imagine a pipeline where instruction fetch and data memory access both use a single shared memory port. If instruction 3 is fetching while instruction 1 is reading data from memory, they collide. The fix is usually to duplicate the resource — separate instruction and data caches (a Harvard-style memory) eliminate this particular structural hazard entirely. Where duplication is too expensive, the pipeline inserts a **stall** (also called a bubble): one instruction waits a cycle while the other uses the resource.

**Data hazards** are more subtle and more common. Consider two instructions in sequence: `ADD R1, R2, R3` followed by `SUB R4, R1, R5`. The SUB needs the value of R1, but ADD won't write its result to the register file until the write-back stage — three cycles after it produces the result in the execute stage. If SUB tries to read R1 during its decode stage, it gets the old, stale value. The simplest fix is stalling: freeze SUB for two cycles until R1 is updated. But a much better solution is **data forwarding** (also called bypassing): since the ADD's result is actually computed at the end of the execute stage, the hardware can route it directly back to the SUB's execute input, bypassing the register file entirely. Forwarding eliminates most data hazard stalls, but not all — a **load-use hazard** (where a load instruction is immediately followed by an instruction using the loaded value) still requires one stall cycle because the data isn't available until the memory access stage.

**Control hazards** arise from branches. When the pipeline fetches a conditional branch instruction, it doesn't know which instruction comes next until the branch condition is evaluated — potentially several stages later. Every cycle spent waiting is a wasted slot. **Branch prediction** addresses this by guessing the branch outcome and speculatively fetching instructions along the predicted path. If the guess is correct, the pipeline runs at full speed. If the guess is wrong, the speculatively fetched instructions must be **flushed** (discarded), and the pipeline restarts from the correct address — this penalty is typically 2-3 cycles in a simple pipeline, but can be much more in deeper pipelines. Modern processors use sophisticated predictors that achieve over 95% accuracy, making branch mispredictions relatively rare but still one of the most significant sources of lost performance.
