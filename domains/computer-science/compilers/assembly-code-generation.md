---
id: assembly-code-generation
title: Assembly Code Generation from IR
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: assembly-language-basics
  type: hard
- id: instruction-selection-techniques
  type: hard
builds-toward:
- target-specific-code-generation
tags:
- code-generation
- assembly
- lowering
stage: advanced
status: draft
---

# Assembly Code Generation from IR

## Core Idea
Assembly code generation translates target-independent intermediate code into assembly language for the host CPU. It selects registers, chooses addressing modes, and generates instruction sequences respecting CPU constraints while preserving IR semantics—the bridge between high-level optimization and machine execution.

## Questions

```yaml
- question: "An instruction selector encounters the IR sequence 't1 = a * b; t2 = t1 + c'. On a target that supports fused multiply-add (FMA), what is the best outcome?"
  type: multiple-choice
  options:
    - "The selector must emit two instructions: one for the multiply and one for the add"
    - "The selector can recognize the pattern and emit a single FMA instruction, reducing instruction count and latency"
    - "The selector passes this to the register allocator to decide how many instructions are needed"
    - "The selector rewrites the IR to simplify it before selecting instructions"
  answer: 1
  explanation: "Instruction selection operates by pattern-matching IR trees against a catalog of machine instruction patterns. A multiply followed by an add is a classic FMA pattern — many modern CPUs (x86 with AVX, ARM with NEON) have a single instruction for a*b+c. A selector that recognizes this emits one instruction rather than two, improving performance. Option A is the naive, non-optimal approach. Option C is wrong: register allocation is a separate phase that happens after (or interleaved with) instruction selection. Getting this right is exactly why instruction selection is a covering/optimization problem, not a simple translation."

- question: "What is 'spill code' in the context of assembly code generation?"
  type: multiple-choice
  options:
    - "Assembly instructions that handle arithmetic overflow by spilling to an error routine"
    - "Stack alignment instructions inserted before function calls"
    - "Store and load instructions inserted when a value cannot fit in a physical register and must be moved to/from the stack"
    - "Padding bytes inserted to align the code section to cache-line boundaries"
  answer: 2
  explanation: "IR uses unlimited virtual registers, but the target CPU has a fixed, small set of physical registers. When register allocation cannot assign every live variable to a register, it 'spills' some values — storing them to a designated stack slot and reloading them before use. The stores and loads inserted for spilled values are called spill code. Spill code is correct but costly (memory traffic); minimizing spills is a key optimization goal in register allocation."

- question: "In assembly code generation, instruction selection always produces a one-to-one mapping: each IR operation becomes exactly one machine instruction."
  type: true-false
  answer: false
  explanation: "One-to-one mapping is the exception, not the rule. A single IR operation like 'load and add' often requires multiple instructions: a memory load, then the arithmetic operation. Conversely, an instruction selector that recognizes patterns can collapse multiple IR operations into a single powerful instruction (e.g., FMA, LEA for address arithmetic, or vector instructions for loops). The point of instruction selection as an optimization problem is precisely to find the most efficient coverage of the IR tree with machine instruction patterns — cost-minimization over a range of covering options."

- question: "Violating the target architecture's calling convention — for example, by placing function arguments in the wrong registers — will produce machine code that is syntactically valid but causes incorrect behavior at runtime."
  type: true-false
  answer: true
  explanation: "Calling conventions are contracts between caller and callee about register usage, argument passing, return values, and which registers must be preserved. If a code generator places an argument in the wrong register (e.g., the second integer argument in rdi instead of rsi on x86-64 System V), the assembly will assemble without error, but the called function reads a garbage value. These bugs are notoriously hard to diagnose because the source code looks correct — the error lives at the machine-code level. Correctly implementing calling conventions is non-negotiable for interoperability with system libraries and other compiled code."

- question: "Why is instruction selection described as a 'covering' problem, and what does the code generator typically try to minimize?"
  type: short-answer
  answer: "The IR for a computation forms a tree of operations. The code generator must 'cover' every node in this tree with machine instruction patterns — sequences of IR nodes that map to a single machine instruction. Each pattern has a cost (in instruction count, code size, or estimated latency). The goal is to find the lowest-cost complete cover, where every IR node is handled by exactly one pattern with no gaps. Dynamic programming over the tree is the classic algorithm for finding the optimal cover."
  explanation: "This framing (due to Aho, Ganapathi, and Tjiang) clarifies why instruction selection is non-trivial: the space of possible coverings grows exponentially in the number of IR nodes, but dynamic programming reduces it to a polynomial-time problem by computing the optimal cost bottom-up through the tree. Different targets have different instruction catalogs and costs, which is why the code generator is target-specific even when the optimizer is target-independent."
```

## Explainer

By this point in the compiler pipeline, the source program has been parsed, type-checked, and lowered into an intermediate representation — a clean, target-independent form like three-address code or SSA. Assembly code generation is where the rubber meets the road: you must take those abstract operations and express them using the specific instructions, registers, and addressing modes of a real CPU. The IR instruction `t3 = t1 + t2` might become `mov eax, [rbp-8]; add eax, [rbp-12]` on x86, or `add x3, x1, x2` on ARM. Every target architecture has its own instruction set, calling conventions, and constraints that shape this translation.

The first major task is **instruction selection** — mapping each IR operation to one or more machine instructions. This is rarely one-to-one. A single IR operation might require multiple assembly instructions (loading values from memory, performing the operation, storing the result), or conversely, a clever instruction selector might recognize patterns that map to single specialized instructions (like x86's `lea` for address arithmetic or fused multiply-add). From your study of instruction selection techniques, you know that tree-pattern matching and dynamic programming are common approaches. The goal is to **cover** every IR node with machine instruction patterns while minimizing cost (instruction count, latency, or code size).

The second task is mapping the IR's unlimited virtual registers to the CPU's finite physical registers — a problem handled by register allocation, which typically runs as a separate pass. During code generation, the emitter must respect the allocator's decisions, inserting **spill code** (stores to and loads from the stack) wherever a value could not be kept in a register. It must also obey the target's **calling convention**: which registers are caller-saved versus callee-saved, where arguments and return values go, and how the stack frame is laid out. For example, on x86-64 System V, the first six integer arguments go in `rdi, rsi, rdx, rcx, r8, r9`, and the callee must preserve `rbx, rbp, r12–r15`.

Finally, the code generator must handle **addressing modes** — the different ways the CPU can reference operands. A variable might be at a fixed offset from the frame pointer (`[rbp-16]`), at an address computed from a base register plus an index register times a scale (`[rax + rcx*4]`), or an immediate constant embedded in the instruction. Choosing the right addressing mode can eliminate explicit load instructions and reduce code size. The output of this phase is a complete assembly listing that an assembler can translate to machine code — the last step before the program becomes executable. Getting this phase right means every optimization performed earlier in the pipeline actually pays off in faster machine code.
