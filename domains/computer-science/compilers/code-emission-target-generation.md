---
id: code-emission-target-generation
title: Code Emission and Target Generation
domain: computer-science
course: compilers
prerequisites:
- id: graph-coloring-register-allocation
  type: hard
builds-toward:
- calling-conventions-abi
tags:
- code-generation
- backend
- assembly
stage: advanced
status: validated
---

# Code Emission and Target Generation

## Core Idea
After instruction selection and register allocation, the compiler must emit target assembly or machine code. Code emission must handle instruction encoding, relocation information for jumps and calls, and proper instruction ordering. Modern emitters also generate debugging information.

## How It's Best Learned
Implement a code emitter producing assembly code from allocated instructions. Generate position-independent code and handle relocations.

## Questions

```yaml
- question: "A compiler emits code for a shared library. One function calls another that may reside in a different library loaded at an unknown address. How does the emitter handle the unknown call target?"
  type: multiple-choice
  options:
    - "It hard-codes the function's expected virtual address from the linker map"
    - "It inserts a relocation entry — a placeholder plus metadata telling the linker to fill in the real address later"
    - "It leaves the address field as zero and relies on the OS loader to zero-extend it at runtime"
    - "It duplicates the called function's body inline to avoid the address problem"
  answer: 1
  explanation: "Relocations are the standard mechanism for addresses that cannot be resolved at compile time. The emitter writes a placeholder and records metadata (symbol name, relocation type, offset) so the linker or dynamic loader can patch the correct address in. For position-independent code in shared libraries, the emitter generates PC-relative instructions so the code works regardless of where it is loaded — absolute addresses would break when the library is mapped to a different base address."

- question: "An emitter targeting ARM encounters a 32-bit constant that must be loaded into a register. ARM uses fixed-width 32-bit instructions with limited immediate fields. What must the emitter do?"
  type: multiple-choice
  options:
    - "Reject the compilation with an error — the constant exceeds what the architecture supports"
    - "Split the constant across multiple instructions, loading it in pieces"
    - "Switch to a variable-width encoding mode for this instruction only"
    - "Store the constant in a floating-point register, which supports larger immediates"
  answer: 1
  explanation: "Fixed-width RISC architectures like ARM encode immediates in a limited number of bits within the instruction word. A full 32-bit constant cannot fit in one instruction. The emitter must emit an instruction sequence — for example, loading the upper 16 bits then ORing in the lower 16. This is a non-trivial emitter responsibility that doesn't arise with variable-length encodings like x86, illustrating that code emission involves architecture-specific problem solving."

- question: "Code emission bugs that corrupt relocation metadata can be especially difficult to diagnose because they may only manifest when the linker combines specific object files."
  type: true-false
  answer: true
  explanation: "Relocation bugs do not crash the emitter or even the individual compilation — the object file looks syntactically valid. The error only surfaces when the linker tries to resolve the broken relocation, and only for certain link combinations. This makes them hard to reproduce in isolation and explains why the topic states code emission bugs are 'notoriously difficult to diagnose.'"

- question: "Code emission is essentially a mechanical transcription step — once instruction selection and register allocation are complete, the emitter simply writes out the instructions with no further decision-making."
  type: true-false
  answer: false
  explanation: "Code emission involves several non-trivial decisions: selecting the correct binary encoding for each instruction (x86 MOV alone has dozens of variants), inserting relocation entries for unresolved addresses, generating position-independent addressing for shared libraries, and producing debugging information (DWARF), exception tables, symbol tables, and section headers in the correct object file format. A bug in any of these produces incorrect or non-functional output."

- question: "A compiler engineer calls code emission 'the easy final step' after optimization and register allocation. What non-trivial problems must code emission actually solve, and why can bugs at this stage be especially hard to diagnose?"
  type: short-answer
  answer: "Code emission must handle: (1) correct binary instruction encoding — each architecture has many encoding variants per instruction; (2) relocations — placeholders for addresses unknown at compile time, with metadata for the linker to resolve later; (3) position-independent code for shared libraries; and (4) generation of debug info, exception tables, and object-file structure. Bugs are hard to diagnose because relocation errors only appear when the linker combines specific object files, not during compilation itself."
  explanation: "The 'easy' label misses how much architecture-specific knowledge and careful bookkeeping code emission requires. Instruction encoding alone demands understanding every operand variant for the target ISA. Relocation bugs are silent until link time or even runtime, making them exceptionally hard to trace back to the emitter."
```

## Explainer

By this point in the compilation pipeline, the heavy lifting of optimization and register allocation is done. You have an intermediate representation where virtual registers have been replaced with physical machine registers (from graph coloring register allocation), and instructions have been selected for the target architecture. **Code emission** is the final translation step: converting this internal representation into actual bytes — assembly text or binary machine code — that the target processor can execute.

The process may sound mechanical, but several non-trivial problems arise. First, **instruction encoding**: each target architecture has its own binary format for instructions. An x86 `MOV` instruction, for example, has dozens of encoding variants depending on operand sizes, addressing modes, and whether the operands are registers or memory locations. The emitter must select the correct encoding for each instruction and produce the exact byte sequence the processor expects. RISC architectures like ARM have simpler, fixed-width encodings, but they introduce their own challenges — limited immediate value ranges may require the emitter to split a large constant across multiple instructions.

Second, **relocations** handle addresses that are not yet known. When the emitter encounters a function call or a jump to another code section, it may not know the target address — especially if the code will be linked with other object files or loaded at a runtime-determined address. The emitter inserts a **relocation entry**: a placeholder in the binary plus metadata telling the linker "fill in the actual address here later." For **position-independent code** (PIC), used in shared libraries, the emitter generates instructions that access data and functions relative to the current instruction pointer rather than using absolute addresses, enabling the code to work regardless of where it is loaded in memory.

Third, modern emitters generate far more than just instructions. **Debugging information** (in formats like DWARF) maps machine instructions back to source lines, variable names, and types, enabling debuggers to present a source-level view of execution. **Exception handling tables** describe how to unwind the stack when exceptions occur. **Symbol tables** and **section headers** organize the output into the structured format expected by the operating system's loader (ELF on Linux, PE on Windows, Mach-O on macOS). The emitter must produce all of these correctly — a bug in relocation metadata can cause crashes that only manifest when the linker combines specific object files, making code emission bugs notoriously difficult to diagnose.
