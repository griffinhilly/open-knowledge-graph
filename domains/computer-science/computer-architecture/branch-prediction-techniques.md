---
id: branch-prediction-techniques
title: Branch Prediction and Speculative Execution
domain: computer-science
course: computer-architecture
prerequisites:
- id: data-hazards-control-hazards
  type: hard
builds-toward:
- superscalar-and-vliw-design
- out-of-order-execution-design
tags:
- branch
- prediction
- speculation
- performance
stage: formal-systems
status: draft
---

# Branch Prediction and Speculative Execution

## Core Idea
Branch prediction guesses the outcome of conditional branches and speculatively fetches the predicted path, minimizing pipeline stalls from control hazards. Prediction tables track branch history; incorrect predictions require rollback and re-execution.

## Questions

```yaml
- question: "A loop executes exactly 100 times. A 1-bit branch predictor is used for the loop-back branch. How many times does the predictor mispredict across all 100 iterations?"
  type: multiple-choice
  options:
    - "0 times — the predictor quickly learns the branch is always taken"
    - "2 times — once when the loop first executes and once when it finally exits"
    - "100 times — the predictor mispredicts every iteration"
    - "50 times — the 1-bit predictor alternates predictions"
  answer: 1
  explanation: "A 1-bit predictor remembers the last outcome and predicts the same thing will happen again. For a loop running 100 times: the branch is taken 99 times (looping back) and not-taken once (exiting). The predictor mispredicts once on entry (if it last saw a 'not-taken' from the previous loop execution) and once on exit (when it predicts 'taken' but the loop ends). This 2-mispredictions-per-loop pattern is the classic weakness of 1-bit prediction, which the 2-bit saturating counter fixes."

- question: "Why does branch misprediction penalty grow with pipeline depth?"
  type: multiple-choice
  options:
    - "Deeper pipelines encounter branches more frequently because they execute more instructions per cycle"
    - "Each misprediction requires flushing all instructions that were speculatively fetched after the branch, and deeper pipelines have fetched more of them"
    - "Deeper pipelines use more complex prediction algorithms that introduce more errors"
    - "Branch resolution happens earlier in deeper pipelines, giving the predictor less time to decide"
  answer: 1
  explanation: "The misprediction penalty equals the number of pipeline stages between instruction fetch and branch resolution — that is, how many speculative instructions must be discarded. In a 5-stage pipeline, the penalty is 1-2 cycles. In a 15-stage pipeline, it might be 10-15 cycles. Each of those discarded instructions represents wasted computation: fetch, decode, and possibly partial execution occurred for instructions on the wrong path. This is why prediction accuracy is so critical in modern deep-pipeline processors — even improving from 95% to 97% accuracy yields substantial performance gains."

- question: "Static branch prediction can achieve 85–90% accuracy by always predicting branches as not taken."
  type: true-false
  answer: false
  explanation: "Static prediction achieves roughly 60-70% accuracy, not 85-90%. The 85-90% figure is achieved by dynamic 2-bit saturating counter predictors, which learn from runtime history. Static 'always not-taken' performs poorly on loop-back branches (which are taken the majority of the time) and on other frequently-taken conditional branches. The improvement to 85-90% is specifically due to dynamic adaptation based on observed branch behavior."

- question: "When a branch prediction is incorrect, the processor must flush the speculatively executed instructions from the pipeline and restart fetching from the correct path."
  type: true-false
  answer: true
  explanation: "This is the fundamental cost of misprediction. Speculative instructions that were fetched, decoded, and executed along the wrong path must be squashed — their results discarded and any state changes reversed — before the processor can restart from the correct branch target. This pipeline flush is called the misprediction penalty, measured in cycles. Modern out-of-order processors use techniques like precise exceptions and reorder buffers to enable clean rollback without corrupting architectural state."

- question: "Explain why branch prediction is described as 'one of the most performance-critical components in a processor despite performing no actual computation.' What cost does a misprediction incur?"
  type: short-answer
  answer: "Branch prediction is critical because branches occur roughly every 5-7 instructions in typical code, and each misprediction in a modern deep-pipeline processor costs 10-20 wasted cycles — time spent fetching, decoding, and beginning execution of the wrong instruction stream. At a 3 GHz clock with a 15-stage pipeline, a misprediction wastes about 5 nanoseconds. Even at 95% accuracy, with branches every 6 instructions, ~8% of cycles are wasted on mispredictions. Going from 95% to 97% accuracy meaningfully reduces this overhead. The predictor performs no ALU work, but its decisions gate whether all the ALU work ahead of it was useful or wasted."
  explanation: "This counterintuitive importance arises from the interaction between two processor design trends: deeper pipelines (more stages between fetch and branch resolution) and higher instruction throughput (more work in flight). Both trends increase the cost of flushing. A predictor that was 'good enough' for a 5-stage pipeline becomes a bottleneck in a 20-stage one, which is why processor vendors invest heavily in increasingly sophisticated prediction schemes like tournament predictors and neural network-based predictors."
```

## Explainer

From your study of control hazards, you know the core problem: when a pipelined processor encounters a conditional branch, it does not know whether to fetch the next sequential instruction or the branch target until the branch condition is evaluated, which happens several stages into the pipeline. Waiting for the result means stalling — inserting bubbles that waste cycles. In a 5-stage pipeline, this costs 1-2 cycles per branch. In a deep 15-stage pipeline, it could cost 10 or more. Since branches occur roughly every 5-7 instructions in typical code, the performance penalty of always stalling would be catastrophic. **Branch prediction** solves this by guessing the branch outcome and fetching instructions along the predicted path speculatively.

The simplest prediction strategy is **static prediction**: always predict that branches are not taken (continue to the next sequential instruction), or always predict backward branches as taken (since they are usually loop-back edges) and forward branches as not taken. This is cheap to implement and captures common loop behavior, achieving roughly 60-70% accuracy. **Dynamic prediction** does much better by learning from the branch's runtime history. A **1-bit predictor** remembers whether the branch was taken last time and predicts it will do the same thing. This works well for branches that are consistently taken or not taken, but it mispredicts twice for every loop — once when entering (if the branch was not taken last time the loop ended) and once when exiting. A **2-bit saturating counter** fixes this by requiring two consecutive mispredictions before flipping the prediction, achieving 85-90% accuracy on typical workloads.

Modern processors use **two-level adaptive prediction**, which tracks not just a single branch's history but the pattern of recent branch outcomes. A **branch history register** (BHR) records the last *n* outcomes (taken/not taken) as a bit string, and this pattern indexes into a **pattern history table** (PHT) of 2-bit counters. This allows the predictor to learn correlations — for example, that after the pattern taken-taken-not-taken, this branch is usually taken. **Tournament predictors** go further by maintaining multiple prediction mechanisms and a meta-predictor that selects whichever mechanism has been more accurate for each branch recently.

When a prediction turns out to be wrong, the processor must **flush** all speculatively executed instructions from the pipeline, discard any register or memory changes they made, and restart fetching from the correct path. This **misprediction penalty** equals the number of pipeline stages between fetch and branch resolution — wasted work that grows with pipeline depth. This is why prediction accuracy matters enormously: even going from 95% to 97% accuracy can yield measurable performance gains, because the remaining mispredictions each cost 10-20 cycles in a modern out-of-order processor. The branch predictor is, paradoxically, one of the most performance-critical components in a processor despite performing no actual computation.
