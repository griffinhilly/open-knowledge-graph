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

## Explainer

From your study of control hazards, you know the core problem: when a pipelined processor encounters a conditional branch, it does not know whether to fetch the next sequential instruction or the branch target until the branch condition is evaluated, which happens several stages into the pipeline. Waiting for the result means stalling — inserting bubbles that waste cycles. In a 5-stage pipeline, this costs 1-2 cycles per branch. In a deep 15-stage pipeline, it could cost 10 or more. Since branches occur roughly every 5-7 instructions in typical code, the performance penalty of always stalling would be catastrophic. **Branch prediction** solves this by guessing the branch outcome and fetching instructions along the predicted path speculatively.

The simplest prediction strategy is **static prediction**: always predict that branches are not taken (continue to the next sequential instruction), or always predict backward branches as taken (since they are usually loop-back edges) and forward branches as not taken. This is cheap to implement and captures common loop behavior, achieving roughly 60-70% accuracy. **Dynamic prediction** does much better by learning from the branch's runtime history. A **1-bit predictor** remembers whether the branch was taken last time and predicts it will do the same thing. This works well for branches that are consistently taken or not taken, but it mispredicts twice for every loop — once when entering (if the branch was not taken last time the loop ended) and once when exiting. A **2-bit saturating counter** fixes this by requiring two consecutive mispredictions before flipping the prediction, achieving 85-90% accuracy on typical workloads.

Modern processors use **two-level adaptive prediction**, which tracks not just a single branch's history but the pattern of recent branch outcomes. A **branch history register** (BHR) records the last *n* outcomes (taken/not taken) as a bit string, and this pattern indexes into a **pattern history table** (PHT) of 2-bit counters. This allows the predictor to learn correlations — for example, that after the pattern taken-taken-not-taken, this branch is usually taken. **Tournament predictors** go further by maintaining multiple prediction mechanisms and a meta-predictor that selects whichever mechanism has been more accurate for each branch recently.

When a prediction turns out to be wrong, the processor must **flush** all speculatively executed instructions from the pipeline, discard any register or memory changes they made, and restart fetching from the correct path. This **misprediction penalty** equals the number of pipeline stages between fetch and branch resolution — wasted work that grows with pipeline depth. This is why prediction accuracy matters enormously: even going from 95% to 97% accuracy can yield measurable performance gains, because the remaining mispredictions each cost 10-20 cycles in a modern out-of-order processor. The branch predictor is, paradoxically, one of the most performance-critical components in a processor despite performing no actual computation.
