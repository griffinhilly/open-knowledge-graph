---
id: quadruple-intermediate-representation
title: Quadruple Intermediate Representation
domain: computer-science
course: compilers
prerequisites:
- id: three-address-intermediate-code
  type: hard
builds-toward:
- basic-block-analysis
tags:
- ir
- intermediate-representation
stage: advanced
status: validated
---

# Quadruple Intermediate Representation

## Core Idea
A quadruple explicitly represents a three-address instruction as a 4-tuple: (op, arg1, arg2, result). Quadruples are more explicit than textual 3AC and support easier manipulation during optimization. Triples (omitting the result field) are more compact but harder to optimize.

## How It's Best Learned
Implement both quadruple and triple representations. Compare them on a real optimization task to understand trade-offs.

## Questions

```yaml
- question: "A compiler performs dead-code elimination on a triple-based IR and removes instruction at position 3. What problem does this create?"
  type: multiple-choice
  options:
    - "The removed instruction cannot be recovered because triples have no result field"
    - "All subsequent triple position numbers shift down by one, invalidating every positional reference to instructions that were at positions 4 and beyond"
    - "The optimization is illegal because dead-code elimination requires a quadruple representation"
    - "Removing a triple creates a type mismatch between the operator and its arguments"
  answer: 1
  explanation: "Triples identify results by their position number in the instruction list. When you delete instruction 3, the old instruction 4 becomes instruction 3, instruction 5 becomes instruction 4, and so on. Every triple that referenced a result by its old position number now points to the wrong instruction. Fixing this requires updating every positional reference in the entire program — an O(n²) bookkeeping burden. Quadruples avoid this entirely because results are stored in named temporaries (t1, t2, …) that remain valid regardless of instruction order."

- question: "Which of the following correctly represents the expression 'x = a + b * c' as a sequence of quadruples?"
  type: multiple-choice
  options:
    - "(+, a, b*c, x) — one quadruple captures the full expression"
    - "(*, b, c, t1) followed by (+, a, t1, x) — two quadruples, one per operation"
    - "(*, b, c, +, a, x) — a single quadruple with five fields"
    - "(b, c, *, t1) followed by (a, t1, +, x) — with operands before the operator"
  answer: 1
  explanation: "Each quadruple represents exactly one operation with the format (operator, arg1, arg2, result). Complex expressions must be broken into a sequence of simple operations. 'b * c' becomes the first quadruple (*, b, c, t1), storing the result in a temporary t1. Then 'a + t1' becomes (+, a, t1, x). This mirrors three-address code: at most one operator per instruction. The named temporary t1 is the key — it makes the connection between the two instructions explicit and independent of their position."

- question: "In triple representation, referring to the result of instruction 5 as '(5)' is equivalent to using a named temporary in quadruples — both approaches are equally robust when instructions are reordered."
  type: true-false
  answer: false
  explanation: "This is the central weakness of triples. A positional reference like '(5)' is fragile: it only remains correct as long as instruction 5 stays at position 5. Any optimization that inserts, deletes, or reorders instructions invalidates the reference. Named temporaries in quadruples (e.g., t3) are stable identifiers — they refer to the same result regardless of where the producing quadruple ends up after optimization. This is why quadruples are preferred for optimizing compilers despite using one extra field per instruction."

- question: "A quadruple for a unary operation like 'x = -y' will leave one of its four fields empty or unused."
  type: true-false
  answer: true
  explanation: "The quadruple format (op, arg1, arg2, result) allocates four fields for every instruction, but not all instructions need all four. A unary negation uses only arg1 and result: (negate, y, _, x), where the second argument field is empty. Similarly, an unconditional jump (goto, _, _, L3) uses only the result field for the label. This fixed-size format is slightly wasteful in space but makes the data structure uniform and simple to manipulate — every instruction occupies the same size record."

- question: "Explain why quadruples are more suitable than triples for optimization passes that reorder or delete instructions. What specific property makes this possible?"
  type: short-answer
  answer: "Quadruples store the result of each instruction in a named temporary (e.g., t1, t2). These names are stable identifiers that remain valid regardless of instruction order. When an optimizer reorders, deletes, or inserts instructions, the named temporaries continue to refer to the correct results. Triples, by contrast, refer to results by position number — so any structural change to the instruction sequence breaks positional references and requires an expensive global update. The specific property is named vs. positional result storage."
  explanation: "The key insight is that optimization passes constantly transform the instruction sequence — constant folding, dead-code elimination, instruction scheduling, and common subexpression elimination all involve moving or removing instructions. Named temporaries decouple the identity of a result from its location in the instruction stream. A triple's positional reference is essentially a pointer into a sorted array; shift the array and the pointer breaks. A quadruple's named temporary is like a pointer to a labeled object; you can move the object and the label follows it."
```

## Explainer

You already understand three-address code as an intermediate representation where each instruction has at most one operator and up to two source operands producing one result. Quadruples make this structure explicit by storing every instruction as a fixed-size record with four fields: **(operator, argument1, argument2, result)**. This is not a new language — it is a concrete data structure for representing the same three-address instructions you have already seen, in a form that is easy to store in arrays and manipulate programmatically.

Consider the expression `a = b * c + d`. A three-address code listing might write `t1 = b * c` followed by `a = t1 + d`. As quadruples, these become two records: `(*, b, c, t1)` and `(+, t1, d, a)`. Each record is self-contained — you can look at any quadruple and immediately know the operation, its inputs, and where the result goes. Not every field is always used: a unary operation like `t1 = -b` becomes `(negate, b, _, t1)`, and an unconditional jump becomes `(goto, _, _, L3)`. The unused fields are simply left empty.

The main alternative is the **triple** representation, which saves space by eliminating the result field entirely. Instead of naming a temporary for each result, triples refer to the result of an instruction by its position number in the instruction list. So instruction 0 might be `(*, b, c)` and instruction 1 might be `(+, (0), d)`, where `(0)` means "the result of instruction 0." This is more compact, but it creates a fragile dependency on instruction ordering — if you reorder, delete, or insert instructions during optimization, every positional reference must be updated. Quadruples avoid this problem because results are stored in named temporaries that remain valid regardless of instruction order, making them significantly easier to optimize.

In practice, most compiler implementations use quadruples (or a closely related structure) for their intermediate representation because optimization passes constantly rearrange, delete, and insert instructions. The small overhead of an extra field per instruction is a worthwhile trade for the freedom to transform code without maintaining a web of positional back-references. When you move on to basic block analysis and optimization, you will find that quadruples make operations like dead code elimination and common subexpression elimination straightforward — you simply mark a quadruple as dead or redirect its result, without renumbering the entire instruction sequence.
