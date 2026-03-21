---
id: dead-code-elimination
title: Dead Code Elimination
domain: computer-science
course: compilers
prerequisites:
- id: live-variable-analysis
  type: hard
tags:
- optimization
- code-quality
- dead-code
stage: advanced
status: draft
---

# Dead Code Elimination

## Core Idea
Dead code elimination removes statements whose results are never used. An assignment to a non-live variable is dead: the value is computed but never observed. Unreachable code (after return, throw, or unconditional jump) is also dead. This optimization reduces code size and can expose further optimization opportunities. Aggressive dead-code elimination requires interprocedural analysis.

## Questions

```yaml
- question: "A compiler sees: `x = a * b + c` on line 5. Variable x is overwritten on line 12 without being read between lines 5 and 12. Variables a, b, and c are each used only in this expression. What does dead code elimination do?"
  type: multiple-choice
  options:
    - "It removes only line 5, since x is dead after that assignment, but a, b, and c remain because they were 'used' on line 5"
    - "It removes line 5 and also removes any assignments that produced a, b, and c, since those values are now also dead"
    - "It cannot remove line 5 because a, b, and c might have side effects from their definitions"
    - "It marks line 5 as unreachable code and uses control flow analysis to eliminate it"
  answer: 1
  explanation: "Dead code elimination cascades. Removing the dead assignment `x = a * b + c` makes the prior computations of a, b, and c dead as well — if their only use was on line 5, they are no longer live anywhere. A second pass (or aggressive DCE in a single pass) removes those assignments too. This cascading effect is why compilers run DCE iteratively or use the aggressive approach that starts by assuming everything dead and marks live only what contributes to observable effects."

- question: "What is the fundamental difference between dead assignment elimination and unreachable code elimination?"
  type: multiple-choice
  options:
    - "Dead assignment elimination is safe; unreachable code elimination might change program behavior"
    - "Dead assignment elimination relies on live variable analysis to identify values that are computed but never read; unreachable code elimination relies on control flow analysis to find basic blocks with no reachable predecessors"
    - "Dead assignment elimination only works on scalars; unreachable code elimination works on any code block"
    - "Unreachable code elimination is a subset of dead assignment elimination — all unreachable code contains dead assignments"
  answer: 1
  explanation: "The two are distinct optimizations that use different analyses. Dead assignments exist in reachable code — the code runs, but the computed value is never subsequently read. This requires live variable analysis: is this variable live after this definition? Unreachable code cannot execute at all — it lies on no path from the entry block in the control flow graph. This requires control flow analysis, not liveness. Both are called 'dead code' colloquially, but a compiler handles them through different mechanisms."

- question: "Dead code elimination can reveal additional dead code, because removing a dead assignment may make the computations that produced the assigned value dead as well."
  type: true-false
  answer: true
  explanation: "True — this cascading property is one of the defining characteristics of DCE and why compilers run it iteratively or use the aggressive (mark-from-observable-effects) approach. If x is dead, its definition `x = a * b + c` is removed. If a, b, and c were defined only to be used in that expression, their definitions are now dead. Removing those may make further upstream computations dead. The chain can propagate arbitrarily deep through the program's def-use graph."

- question: "If a code block is never executed during any test run, a compiler can determine it is unreachable and safely eliminate it."
  type: true-false
  answer: false
  explanation: "False. Unreachable code is a *static* (compile-time) property determined by control flow graph analysis — a block is unreachable if it has no predecessors other than itself in the CFG. Test execution is a *dynamic* property; code that was never executed during testing might be reachable under different inputs. A compiler cannot use test coverage data to decide what to eliminate — it would change the program's semantics for those untested inputs. Only static analysis proves unreachability."

- question: "What makes 'aggressive' dead code elimination different from the naive approach, and why is it particularly effective after function inlining?"
  type: short-answer
  answer: "The naive approach finds statements that are dead (value never read) and removes them. Aggressive DCE works in the opposite direction: it starts by assuming everything is dead, then marks statements as live only if they contribute to observable effects (return values, memory writes visible outside the function, I/O). Everything not marked live is deleted in a single pass, naturally handling chains of dead code. After inlining, large sections of the inlined function's code may be irrelevant in the caller's context — variables never read, branches never taken — and aggressive DCE eliminates all of it in one pass without needing to iterate."
  explanation: "The key conceptual difference is the starting assumption. Naive DCE asks 'is this specific statement dead?' and must iterate to catch cascades. Aggressive DCE asks 'does this statement contribute to any observable program effect?' and propagates liveness backward from observable effects, naturally handling arbitrarily long chains of dead code in one traversal. Inlining amplifies this benefit because it often creates large regions of code that are locally correct but globally irrelevant to the caller's purpose."
```

## Explainer

Your prerequisite, live variable analysis, answers a precise question for every point in a program: which variables might still be read before being overwritten? A variable is **live** at a point if there exists some execution path from that point to a use of the variable without an intervening definition. **Dead code elimination** (DCE) is the optimization that exploits this information directly — if a statement computes a value that is not live after the statement, the computation is wasted work and can be removed.

Consider a concrete example. Suppose a function computes `x = a * b + c` on line 10, but x is reassigned on line 15 without being read in between, and line 10's value of x is never used on any path. Live variable analysis marks x as not live after line 10, which means the assignment is **dead**. The compiler deletes line 10 entirely. This is not just tidying up — it eliminates the multiplication and addition, freeing the execution unit and potentially freeing a register that was holding x. In real compilers, dead code often arises not from sloppy programming but from earlier optimization passes: constant propagation might replace all uses of a variable with a constant, leaving the original assignment dead; inlining might duplicate code where one branch becomes unreachable; and loop transformations might render intermediate computations unnecessary.

There are two distinct kinds of dead code. The first, described above, is **dead assignments**: statements that compute values nobody reads. The second is **unreachable code**: statements that no execution path can ever reach. Code after an unconditional return, code in an `if (false)` branch after constant folding, or code following an infinite loop is unreachable. Unreachable code detection uses **control flow analysis** rather than live variable analysis — it identifies basic blocks with no predecessors in the control flow graph (other than the entry block). Both kinds should be eliminated, but they rely on different analyses.

Dead code elimination is a cascading optimization, meaning that removing dead code can create more dead code. Deleting a dead assignment to x might make the computations of a, b, and c dead as well, if they were only used to compute x. This is why compilers typically run DCE iteratively or interleave it with other passes. **Aggressive dead code elimination** works in the opposite direction from the naive approach: instead of finding dead statements to delete, it starts by assuming *everything* is dead and then marks statements as live only if they contribute to observable effects — function return values, writes to memory visible outside the function, I/O operations, or stores to volatile variables. Everything not marked live is deleted. This aggressive approach naturally handles chains of dead code in a single pass and is particularly effective after inlining, where large sections of inlined code may turn out to be irrelevant in the caller's context.
