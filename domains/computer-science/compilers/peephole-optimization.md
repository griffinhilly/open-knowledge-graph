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

## Questions

```yaml
- question: "A compiler's code generator produces the instruction sequence: STORE R1, [addr] followed immediately by LOAD R2, [addr]. What does a peephole optimizer do with this, and why?"
  type: multiple-choice
  options:
    - "It removes both instructions because the value in R1 must still be needed later and the load is forward-looking"
    - "It replaces the pair with MOV R2, R1, because the value just stored to [addr] is already in R1, eliminating the redundant memory access"
    - "It reorders the instructions so the LOAD precedes the STORE to improve cache performance"
    - "It does nothing because peephole optimization only handles jump instructions, not memory operations"
  answer: 1
  explanation: "This is the classic 'redundant load-store elimination' pattern. The peephole optimizer sees that immediately after storing R1 to [addr], the code loads from [addr] into R2. Since the value just written is still in R1, the load is unnecessary — R2 can simply receive the value directly from R1. The pair is replaced with MOV R2, R1, eliminating a memory round-trip. This pattern arises naturally when a compiler generates code for each construct independently: the store comes from one context (writing a variable) and the load comes from another (reading it for the next use), and only local inspection reveals the redundancy."

- question: "Why do compilers often run peephole optimization iteratively (multiple passes) rather than just once?"
  type: multiple-choice
  options:
    - "Each pass reduces instruction count, which shrinks the code and requires re-running the pass to handle the now-smaller windows correctly"
    - "Applying one peephole rule can bring two previously non-adjacent instructions into adjacency, exposing new pattern-match opportunities that the first pass could not have seen"
    - "Iterative passes compensate for missed patterns caused by the fixed window size being too small on the first pass"
    - "Peephole optimization is non-deterministic; multiple passes increase the probability of finding the globally optimal sequence"
  answer: 1
  explanation: "Peephole rules compose: applying one substitution can create new opportunities for other rules. For example, collapsing a jump chain (A jumps to L1, L1 jumps to L2 → A jumps directly to L2) might now place two formerly non-adjacent loads to the same address next to each other, which a redundant-load rule can then eliminate. The second pass sees patterns that the first pass could not, because the first pass changed the instruction arrangement. Running until no further changes occur (a fixpoint) guarantees that all discoverable patterns are caught. This composability is one of peephole optimization's practical strengths."

- question: "Peephole optimization is a purely local transformation: it can improve instruction sequences within a small window without needing to analyze the program's data flow, control flow, or overall structure."
  type: true-false
  answer: true
  explanation: "This is what makes peephole optimization both simple and broadly applicable. Each rule is a self-contained pattern match over 2–5 adjacent instructions — 'if you see this sequence, replace it with that sequence.' No global program analysis is needed, no data-flow equations are solved, no call graphs are inspected. The optimizer does not need to understand what the program computes. This simplicity means the optimizer is easy to implement and verify, easy to extend with new rules, and easy to apply across different source languages, target architectures, and earlier optimization phases. It is the quintessential 'local polish' pass."

- question: "Peephole optimization is designed to run early in the compilation pipeline, before register allocation, because it needs to work on high-level intermediate representations."
  type: true-false
  answer: false
  explanation: "Peephole optimization typically runs late in the compilation pipeline, after instruction selection and register allocation. The reason is that earlier phases sometimes introduce awkward instruction sequences — a register allocator might insert a spill (store to memory) and reload (load back from memory) that turns out to be unnecessary, or instruction selection might produce a two-instruction idiom where a single specialized machine instruction exists. The peephole pass is positioned to catch exactly these late-stage inefficiencies. Running it earlier (on high-level IR) would miss the target-specific patterns that instruction selection and register allocation introduce."

- question: "What properties of peephole optimization make it well-suited as a 'final polish' pass in a compiler, as opposed to an earlier, more global optimization phase?"
  type: short-answer
  answer: "Peephole optimization is suited for a final pass because: (1) it is purely local — it only needs to examine 2–5 adjacent instructions, requiring no global analysis that might be expensive or invalidated by later passes; (2) it operates on the final instruction representation (machine code or near-machine IR), where it can apply target-specific rules like strength reduction (multiply → shift) or specialized instruction folding; (3) it catches inefficiencies introduced by earlier phases — register allocation spills, instruction selection idioms — that only become visible at the instruction level; (4) it is safe to apply after all other optimizations since it only makes local substitutions that preserve semantics by construction."
  explanation: "Earlier optimization phases like inlining, loop optimizations, or register allocation make large structural changes to the program and benefit from global program information. Peephole optimization makes tiny local substitutions and needs no such information. This separation of concerns is intentional: global passes do the heavy lifting, and peephole optimization mops up the local inefficiencies they leave behind. Its simplicity also means it can be extended easily — adding a new target architecture pattern is just adding a new rule to the pattern-match table."
```

## Explainer

After a compiler generates code — whether intermediate representation or actual machine instructions — the result is often locally wasteful. Earlier compilation phases focus on correctness and handle one construct at a time, which means they produce sequences that are correct but clumsy when viewed together. **Peephole optimization** is the clean-up crew: it slides a small window (the "peephole," typically 2–5 instructions wide) across the generated code and applies pattern-matching rules to replace inefficient sequences with better ones. You already know about basic blocks from your prerequisite work — peephole optimization typically operates within a single basic block, making it a purely local transformation.

The classic example is **redundant load-store elimination**. Suppose the code generator produces `STORE R1, [addr]` followed immediately by `LOAD R2, [addr]`. The peephole optimizer recognizes that the value just stored is still in R1, so it replaces the pair with `MOV R2, R1` — eliminating an unnecessary memory access. Another common pattern is **jump chaining**: if instruction A jumps to label L1, and L1 contains nothing but a jump to L2, the optimizer rewrites A to jump directly to L2. Other patterns include replacing `x = x + 0` with nothing, replacing `x = x * 1` with nothing, and strength-reducing `x * 2` to `x << 1`.

What makes peephole optimization elegant is its simplicity. Each rule is a small, self-contained pattern match: "if you see this sequence, replace it with that sequence." The rules don't need to understand the program's overall structure, data flow, or control flow — they just match local instruction patterns. This means peephole optimizers are easy to implement, easy to verify for correctness, and easy to extend with new rules. They compose well with other optimization passes too: running peephole optimization after other transformations often catches inefficiencies that those transformations introduced.

Despite its simplicity, peephole optimization can be surprisingly effective. It typically runs as one of the last passes in the compilation pipeline, after instruction selection and register allocation. Those earlier phases sometimes introduce awkward instruction sequences — a register allocator might insert a spill and reload that turns out to be unnecessary, or instruction selection might produce a two-instruction sequence where a single specialized instruction exists. The peephole pass catches these cases cheaply. In practice, compilers often run peephole optimization iteratively, since replacing one pattern can expose new opportunities — collapsing a jump chain might place two redundant loads adjacent, which the next pass eliminates.
