---
id: assembly-language-basics
title: Assembly Language Basics
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: hexadecimal-number-system
  type: soft
- id: variables-and-assignment
  type: soft
builds-toward:
- cpu-datapath
- memory-organization
tags:
- assembly
- machine-code
- mnemonics
- addressing-modes
stage: formal-systems
status: validated
---

# Assembly Language Basics

## Core Idea
Assembly language is a human-readable representation of machine code, where each instruction mnemonic (like ADD, LOAD, BRANCH) maps directly to a binary opcode. Programmers work with registers by name, specify memory addresses, and use labels for branch targets. Addressing modes — immediate, register, direct, indirect, base+offset — determine how operands are located. Assembly is compiled by an assembler into machine code, and understanding assembly is essential for reverse engineering, performance tuning, and interpreting compiler output.

## How It's Best Learned
Write and run short MIPS or RISC-V assembly programs in a simulator such as MARS or Ripes. Trace register and memory values through each instruction. Examine compiler output at the assembly level using gcc -S or an online tool like Godbolt.

## Common Misconceptions
- Assembly language is not machine code — it is a text-based representation that an assembler translates into binary.
- Writing assembly is not always faster than compiled code; modern optimizing compilers often produce more efficient code than hand-written assembly.

## Questions

```yaml
- question: "In a RISC assembly program, a programmer wants to add two values stored in memory. What must happen before the addition can occur?"
  type: multiple-choice
  options:
    - "The ADD instruction can directly reference memory addresses as its operands"
    - "The values must be loaded into registers first, because arithmetic operations work only on register contents"
    - "The values must be converted to hexadecimal before the processor can handle them"
    - "The programmer must declare the memory addresses as variables at the start of the program"
  answer: 1
  explanation: "In RISC architectures, arithmetic instructions only operate on register contents — this is the load-store model. To add two values in memory, you must first use LOAD instructions to bring them into registers, then ADD the registers, then optionally STORE the result back. The ADD instruction cannot directly reference memory addresses (option A) in a load-store architecture. This constraint keeps the instruction set simple and the hardware fast."

- question: "A student writes `lw $t0, 8($sp)`. Which addressing mode is this, and what does it do?"
  type: multiple-choice
  options:
    - "Immediate addressing — it loads the constant 8 into register $t0"
    - "Register addressing — it copies the value of $sp into $t0, offset by 8 bits"
    - "Base-plus-offset addressing — it loads the word in memory at address (sp + 8) into $t0"
    - "Indirect addressing — it loads the word at the address stored in memory location 8"
  answer: 2
  explanation: "Base-plus-offset addressing computes a memory address by adding a constant offset to a register value. `lw $t0, 8($sp)` means: compute sp+8, read the word at that memory location, and put it in $t0. This mode is essential for accessing stack variables, array elements, and struct fields. Immediate addressing (option A) embeds a constant directly as an operand, not as an address offset."

- question: "Assembly language and machine code are equivalent terms — both refer to the binary instructions a CPU executes."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic addresses. Assembly language is a human-readable text representation of machine instructions — it uses mnemonics like ADD, LOAD, and BRANCH. Machine code is the binary encoding the CPU actually executes. An assembler translates assembly into machine code. They represent the same operations, but assembly is text; machine code is binary."

- question: "In a RISC assembly program, all control flow — if-else, loops, and function calls — ultimately reduces to conditional and unconditional jump instructions."
  type: true-false
  answer: true
  explanation: "Assembly has no structured control flow constructs — no if-else blocks, no for loops, no built-in function call syntax. All control flow is implemented through branch (conditional jump) and jump (unconditional jump) instructions combined with labels. `beq $t0, $zero, loop` is equivalent to 'if $t0 == 0, go to loop.' Everything else — loops, conditionals, function calls, returns — is built from this primitive."

- question: "Why does the load-store model — where arithmetic happens only in registers and memory is accessed only through explicit load/store instructions — make hardware design simpler and faster?"
  type: short-answer
  answer: "By restricting arithmetic to register contents, the CPU's execution units only need to handle a small, fixed set of fast storage locations rather than the vastly larger and slower memory space. Load and store instructions are explicitly sequenced, making memory access predictable. This separation allows the processor to execute arithmetic at register speed — orders of magnitude faster than memory access — while treating memory operations as their own distinct pipeline stage."
  explanation: "The load-store model is the defining characteristic of RISC architectures. It simplifies instruction decoding (every arithmetic instruction has the same format), enables pipelining (arithmetic and memory stages are separate), and allows the CPU to optimize register usage aggressively. The cost is that programmers must explicitly manage data movement — which is exactly why reading assembly reveals what a program is actually doing at the hardware level."
```

## Explainer

You already understand from instruction set architecture that a processor executes binary-encoded instructions, each specifying an operation and its operands. Assembly language is the human-readable face of these binary instructions: instead of writing `0000 0000 1010 0000 0010 0000 0010 0000` you write `add $a0, $a1, $zero`. Every assembly instruction maps to exactly one machine instruction (or, in some assemblers, a small fixed expansion called a **pseudo-instruction**). This one-to-one correspondence is what distinguishes assembly from higher-level languages — there is no abstraction layer, no optimization step, and no hidden behavior.

An assembly program operates on a small, fixed set of **registers** — fast storage locations built directly into the CPU. A typical RISC architecture provides 32 general-purpose registers, each holding one word (32 or 64 bits). Instructions move data between registers, perform arithmetic on register contents, and transfer data between registers and memory. The key insight is that almost all computation happens in registers; memory is only accessed through explicit **load** and **store** instructions. This load-store model keeps the instruction set simple and the hardware fast.

**Addressing modes** determine how an instruction specifies where its data comes from. **Immediate** addressing embeds a small constant directly in the instruction (`addi $t0, $t0, 5` — add 5 to register t0). **Register** addressing names a register (`add $t0, $t1, $t2` — add the contents of t1 and t2). **Base-plus-offset** addressing computes a memory address by adding a constant offset to a register value (`lw $t0, 8($sp)` — load the word at address sp+8). This mode is essential for accessing stack variables, array elements, and struct fields. Understanding addressing modes is critical because they determine what data access patterns the hardware can support efficiently.

Assembly also introduces **labels** and **branch instructions** for control flow. A label like `loop:` marks a position in the code, and a branch instruction like `beq $t0, $zero, loop` jumps to that position if a condition is met. There are no if-else blocks, no for loops, no function call syntax — all control flow reduces to conditional and unconditional jumps. Function calls follow a **calling convention**: arguments go in designated registers, the return address is saved, the callee preserves certain registers, and the result comes back in a specific register. Learning to read and write assembly gives you direct insight into what your compiled code actually does, which is invaluable for debugging, performance analysis, and understanding how abstractions map to hardware.
