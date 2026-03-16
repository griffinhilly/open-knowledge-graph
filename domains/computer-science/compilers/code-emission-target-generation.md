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
status: draft
---

# Code Emission and Target Generation

## Core Idea
After instruction selection and register allocation, the compiler must emit target assembly or machine code. Code emission must handle instruction encoding, relocation information for jumps and calls, and proper instruction ordering. Modern emitters also generate debugging information.

## How It's Best Learned
Implement a code emitter producing assembly code from allocated instructions. Generate position-independent code and handle relocations.

## Explainer

By this point in the compilation pipeline, the heavy lifting of optimization and register allocation is done. You have an intermediate representation where virtual registers have been replaced with physical machine registers (from graph coloring register allocation), and instructions have been selected for the target architecture. **Code emission** is the final translation step: converting this internal representation into actual bytes — assembly text or binary machine code — that the target processor can execute.

The process may sound mechanical, but several non-trivial problems arise. First, **instruction encoding**: each target architecture has its own binary format for instructions. An x86 `MOV` instruction, for example, has dozens of encoding variants depending on operand sizes, addressing modes, and whether the operands are registers or memory locations. The emitter must select the correct encoding for each instruction and produce the exact byte sequence the processor expects. RISC architectures like ARM have simpler, fixed-width encodings, but they introduce their own challenges — limited immediate value ranges may require the emitter to split a large constant across multiple instructions.

Second, **relocations** handle addresses that are not yet known. When the emitter encounters a function call or a jump to another code section, it may not know the target address — especially if the code will be linked with other object files or loaded at a runtime-determined address. The emitter inserts a **relocation entry**: a placeholder in the binary plus metadata telling the linker "fill in the actual address here later." For **position-independent code** (PIC), used in shared libraries, the emitter generates instructions that access data and functions relative to the current instruction pointer rather than using absolute addresses, enabling the code to work regardless of where it is loaded in memory.

Third, modern emitters generate far more than just instructions. **Debugging information** (in formats like DWARF) maps machine instructions back to source lines, variable names, and types, enabling debuggers to present a source-level view of execution. **Exception handling tables** describe how to unwind the stack when exceptions occur. **Symbol tables** and **section headers** organize the output into the structured format expected by the operating system's loader (ELF on Linux, PE on Windows, Mach-O on macOS). The emitter must produce all of these correctly — a bug in relocation metadata can cause crashes that only manifest when the linker combines specific object files, making code emission bugs notoriously difficult to diagnose.
