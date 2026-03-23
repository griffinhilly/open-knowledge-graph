---
id: procedure-inlining-optimization
title: Procedure Inlining Optimization
domain: computer-science
course: compilers
prerequisites:
- id: global-optimization-techniques
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- instruction-selection-techniques
tags:
- optimization
- inlining
- procedure-calls
stage: advanced
status: validated
---

# Procedure Inlining Optimization

## Core Idea
Procedure inlining replaces a function call with a copy of the function body, eliminating call overhead and enabling further optimizations. Inlining trades code size for speed and must be controlled via heuristics to avoid code bloat.

## How It's Best Learned
Implement function inlining with a simple heuristic (inline if function is small). Measure code size and speed impacts.

## Questions

```yaml
- question: "A compiler inlines the call `square(5)`, replacing it with `5 * 5` in the caller. What optimization is most likely to follow immediately?"
  type: multiple-choice
  options:
    - "Dead code elimination removes the now-unreachable square function definition"
    - "Constant folding reduces `5 * 5` to `25` at compile time"
    - "Register allocation improves because one fewer function call means fewer callee-saved registers"
    - "Loop unrolling becomes possible because the inlined body reveals a hidden iteration"
  answer: 1
  explanation: "Once the function is inlined and the constant argument 5 is propagated into the function body, constant folding can evaluate `5 * 5 = 25` at compile time — producing a constant result with no runtime computation at all. This chain of optimizations (inline → constant propagation → constant folding) is impossible across a call boundary because the compiler cannot see inside the called function to propagate values through it. Option A (dead code elimination of the function definition) may occur as a secondary effect, but the immediate downstream win is constant folding on the inlined body."

- question: "A function called from 50 different sites is aggressively inlined everywhere. What is the primary risk that could make this slower than not inlining?"
  type: multiple-choice
  options:
    - "The program stack grows too large because inlined code has no stack frame discipline"
    - "Inlined code cannot be shared across call sites, leading to subtle behavioral differences"
    - "Code size grows 50x, increasing instruction cache pressure and potentially causing more cache misses"
    - "Register allocation becomes impossible when the inlined function has more than 4 local variables"
  answer: 2
  explanation: "Every inlining decision copies the function body, so inlining a function at 50 call sites creates 50 copies in the binary. Larger code means the instruction cache must hold more distinct instructions. If the working set exceeds the cache size, the CPU must fetch instructions from main memory more frequently — a severe performance penalty that can dwarf the savings from eliminating call overhead. This is the fundamental tension in inlining heuristics: the benefit (enabling downstream optimizations, eliminating call cost) must be weighed against the risk of cache thrashing from code bloat."

- question: "The primary benefit of procedure inlining is often not the elimination of call overhead itself, but enabling subsequent optimizations like constant propagation and dead code elimination that become visible only after inlining."
  type: true-false
  answer: true
  explanation: "Call overhead (stack manipulation, register saves, jumps) is typically a small cost — a few nanoseconds. The larger win is that inlining expands the optimizer's view: constant arguments can be propagated into the function body, dead branches conditional on those constants can be eliminated, and common subexpressions between caller and callee become visible. A call to `square(5)` saves very little by avoiding a jump; it saves significantly more when inlining enables `25` to appear directly in the code with no multiplication at runtime."

- question: "Recursive functions are ideal candidates for inlining because their repeated structure creates many opportunities for constant propagation and loop optimization."
  type: true-false
  answer: false
  explanation: "Recursive functions generally cannot be fully inlined because doing so would require infinite copies of the function body. Some compilers inline recursion to a fixed depth (e.g., 2–3 levels), but beyond that the recursion must still be handled with actual calls. Additionally, deeply inlined recursive bodies quickly explode in code size, causing exactly the cache pressure problems that make aggressive inlining counterproductive. Compilers typically exclude recursive functions from standard inlining heuristics or treat them as a special case."

- question: "Why is procedure inlining typically performed early in the compiler's optimization pipeline rather than as one of the last passes?"
  type: short-answer
  answer: "Inlining is performed early because it creates new opportunities for downstream optimization passes. Once a function body is inlined, constant propagation, dead code elimination, common subexpression elimination, and loop optimizations can all operate on the combined caller-callee code — finding redundancies that were invisible across the function boundary. If inlining were done late, after these passes had already run, the compiler would miss all those secondary optimizations. The value of inlining compounds: it doesn't just save call overhead, it sets up a cascade of further improvements that need subsequent passes to exploit."
  explanation: "This sequencing principle — perform transformations that expand the visible code early, then run analysis-and-reduction passes — is a general compiler design pattern. Inlining is a code-expanding transformation that trades code size for optimization opportunity, and that opportunity is only captured if the reducing passes (constant propagation, DCE, CSE) run afterward on the expanded code."
```

## Explainer

From your work on global optimization and control flow graphs, you know that many optimizations operate across basic blocks and depend on seeing enough code to find redundancies. **Procedure inlining** dramatically expands the optimizer's view by replacing a function call with a copy of the called function's body, spliced directly into the caller. Instead of a call instruction that jumps away and returns, the code just continues straight through, as if the function's logic had been written inline at the call site.

The immediate benefit is eliminating call overhead — saving the cost of pushing arguments onto the stack, jumping to the callee, saving and restoring registers, and returning. But this direct saving is often the smaller win. The larger benefit is that inlining exposes the function body to the caller's optimization context. Once inlined, constant arguments can be propagated into the function body, dead branches can be eliminated, and common subexpressions between the caller and the inlined code become visible. Consider a function `square(x)` that returns `x * x`. Called as `square(5)`, inlining produces `5 * 5`, which constant folding reduces to `25` — a chain of optimizations that would be impossible across a function call boundary.

The fundamental tension in inlining is the **code size tradeoff**. Every inlining decision copies the function body, increasing the total code size. If a function is called from 50 different sites and each call is inlined, the compiled binary contains 50 copies of that code. Larger code means more instruction cache pressure, which can actually slow down execution — the opposite of the intended effect. Compilers therefore use heuristics to decide what to inline: small functions (a few statements) are almost always inlined, functions called from a single site are inlined regardless of size (since no duplication occurs), and hot call sites identified by profiling data get priority. Recursive functions generally cannot be inlined (or are inlined only to a fixed depth), and functions with complex control flow may offer diminishing returns.

The implementation mechanics matter too. When inlining into a control flow graph, the compiler must rename local variables to avoid name collisions, map the caller's arguments onto the callee's parameters, and replace return statements with jumps to a continuation point in the caller. If the inlined function has multiple return paths, these must be merged. The compiler also needs to handle interactions with other optimizations — inlining can change loop structures, affect alias analysis, and create new opportunities for constant propagation that require additional optimization passes to exploit. This is why inlining is typically performed early in the optimization pipeline, so that downstream passes can capitalize on the newly exposed code.
