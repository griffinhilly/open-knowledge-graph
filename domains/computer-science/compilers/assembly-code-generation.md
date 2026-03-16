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

## Explainer

By this point in the compiler pipeline, the source program has been parsed, type-checked, and lowered into an intermediate representation — a clean, target-independent form like three-address code or SSA. Assembly code generation is where the rubber meets the road: you must take those abstract operations and express them using the specific instructions, registers, and addressing modes of a real CPU. The IR instruction `t3 = t1 + t2` might become `mov eax, [rbp-8]; add eax, [rbp-12]` on x86, or `add x3, x1, x2` on ARM. Every target architecture has its own instruction set, calling conventions, and constraints that shape this translation.

The first major task is **instruction selection** — mapping each IR operation to one or more machine instructions. This is rarely one-to-one. A single IR operation might require multiple assembly instructions (loading values from memory, performing the operation, storing the result), or conversely, a clever instruction selector might recognize patterns that map to single specialized instructions (like x86's `lea` for address arithmetic or fused multiply-add). From your study of instruction selection techniques, you know that tree-pattern matching and dynamic programming are common approaches. The goal is to **cover** every IR node with machine instruction patterns while minimizing cost (instruction count, latency, or code size).

The second task is mapping the IR's unlimited virtual registers to the CPU's finite physical registers — a problem handled by register allocation, which typically runs as a separate pass. During code generation, the emitter must respect the allocator's decisions, inserting **spill code** (stores to and loads from the stack) wherever a value could not be kept in a register. It must also obey the target's **calling convention**: which registers are caller-saved versus callee-saved, where arguments and return values go, and how the stack frame is laid out. For example, on x86-64 System V, the first six integer arguments go in `rdi, rsi, rdx, rcx, r8, r9`, and the callee must preserve `rbx, rbp, r12–r15`.

Finally, the code generator must handle **addressing modes** — the different ways the CPU can reference operands. A variable might be at a fixed offset from the frame pointer (`[rbp-16]`), at an address computed from a base register plus an index register times a scale (`[rax + rcx*4]`), or an immediate constant embedded in the instruction. Choosing the right addressing mode can eliminate explicit load instructions and reduce code size. The output of this phase is a complete assembly listing that an assembler can translate to machine code — the last step before the program becomes executable. Getting this phase right means every optimization performed earlier in the pipeline actually pays off in faster machine code.
