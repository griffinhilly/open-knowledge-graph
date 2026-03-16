---
id: peephole-optimization
title: Peephole Optimization
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: basic-block-analysis
  type: hard
builds-toward:
- assembly-code-generation
tags:
- optimization
- code-generation
- local
stage: advanced
status: draft
---

# Peephole Optimization

## Core Idea
Peephole optimization examines small windows of code to replace inefficient instruction sequences with faster equivalents. For example, a load-then-store becomes a move, and consecutive jumps are collapsed. It's language and platform independent, making it a final polish pass in code generation.

## Explainer

After a compiler generates code — whether intermediate representation or actual machine instructions — the result is often locally wasteful. Earlier compilation phases focus on correctness and handle one construct at a time, which means they produce sequences that are correct but clumsy when viewed together. **Peephole optimization** is the clean-up crew: it slides a small window (the "peephole," typically 2–5 instructions wide) across the generated code and applies pattern-matching rules to replace inefficient sequences with better ones. You already know about basic blocks from your prerequisite work — peephole optimization typically operates within a single basic block, making it a purely local transformation.

The classic example is **redundant load-store elimination**. Suppose the code generator produces `STORE R1, [addr]` followed immediately by `LOAD R2, [addr]`. The peephole optimizer recognizes that the value just stored is still in R1, so it replaces the pair with `MOV R2, R1` — eliminating an unnecessary memory access. Another common pattern is **jump chaining**: if instruction A jumps to label L1, and L1 contains nothing but a jump to L2, the optimizer rewrites A to jump directly to L2. Other patterns include replacing `x = x + 0` with nothing, replacing `x = x * 1` with nothing, and strength-reducing `x * 2` to `x << 1`.

What makes peephole optimization elegant is its simplicity. Each rule is a small, self-contained pattern match: "if you see this sequence, replace it with that sequence." The rules don't need to understand the program's overall structure, data flow, or control flow — they just match local instruction patterns. This means peephole optimizers are easy to implement, easy to verify for correctness, and easy to extend with new rules. They compose well with other optimization passes too: running peephole optimization after other transformations often catches inefficiencies that those transformations introduced.

Despite its simplicity, peephole optimization can be surprisingly effective. It typically runs as one of the last passes in the compilation pipeline, after instruction selection and register allocation. Those earlier phases sometimes introduce awkward instruction sequences — a register allocator might insert a spill and reload that turns out to be unnecessary, or instruction selection might produce a two-instruction sequence where a single specialized instruction exists. The peephole pass catches these cases cheaply. In practice, compilers often run peephole optimization iteratively, since replacing one pattern can expose new opportunities — collapsing a jump chain might place two redundant loads adjacent, which the next pass eliminates.
