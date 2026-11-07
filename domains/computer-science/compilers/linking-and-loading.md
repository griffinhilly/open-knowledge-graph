---
id: linking-and-loading
title: Linking and Loading
domain: computer-science
course: compilers
prerequisites:
- id: assembly-language-basics
  type: hard
- id: symbol-tables-and-scope
  type: soft
- id: memory-management-basics
  type: soft
- id: process-creation-fork-exec
  type: soft
builds-toward: []
tags:
- linker
- loader
- object-files
- relocation
- symbol-resolution
- shared-libraries
- dynamic-linking
stage: formal-systems
status: validated
---
# Linking and Loading

## Core Idea
A compiler translates each source file separately into a relocatable object file containing machine code, data and a symbol table, but with some addresses left unfilled. The linker combines object files and libraries into one executable by doing two jobs: symbol resolution, which matches every reference to a function or global variable with exactly one definition, and relocation, which assigns final addresses and patches every reference to use them. The loader then copies the executable into memory and starts it. Shared libraries move part of the linking to load time or run time, so many programs can share one copy of common code.

## How It's Best Learned
Compile two small C files with `gcc -c`, inspect the object files with tools such as `nm` and `objdump` to see undefined symbols and relocation entries, and then link them. Trigger the two classic link errors on purpose: an undefined reference and a duplicate definition. Finally, build the same program statically and dynamically and compare file sizes and the output of `ldd`, following the linking chapter of Bryant and O'Hallaron's *Computer Systems: A Programmer's Perspective*.

## Common Misconceptions
- "Undefined reference" errors come from the compiler. (Each file compiles fine on its own; the error comes from the linker, which cannot find a definition for a symbol used somewhere.)
- Including a header file such as `math.h` adds the library's code to the program. (A header only declares names; the code comes from linking the library, for example with `-lm`.)
- With shared libraries, each program carries its own copy of the library code. (Dynamically linked programs refer to one shared file, which the operating system can map into many processes at once.)

## Questions

```yaml
- question: "A C program that calls sqrt compiles each .c file without errors, but the build fails with \"undefined reference to `sqrt'\". Which stage reported the error, and what is the usual fix on Linux?"
  type: multiple-choice
  options:
    - "The preprocessor; add #include <math.h>"
    - "The compiler's type checker; cast the argument to double"
    - "The linker; link the math library, for example by adding -lm"
    - "The loader; run the program with administrator rights"
  answer: 2
  explanation: "Compilation needs only the declaration from math.h. The linker must then find the actual definition of sqrt. On many Linux systems it lives in the separate math library, libm, which is linked with -lm. An undefined reference means the linker found a use with no matching definition."

- question: "What does relocation do during linking?"
  type: multiple-choice
  options:
    - "It moves source files into the same folder"
    - "It assigns run-time addresses to code and data sections and patches each reference so it points to the correct final address"
    - "It deletes unused functions from the source code"
    - "It moves the program from disk into memory at run time"
  answer: 1
  explanation: "Each object file is generated as if its sections started at address zero. The linker merges sections, picks their final addresses, and uses the relocation entries in each object file to fix every instruction or data word that refers to a symbol. Copying the program into memory is the loader's job."

- question: "When a program is dynamically linked against a shared library, the library's machine code is copied into the program's executable file at link time."
  type: true-false
  answer: false
  explanation: "With dynamic linking, the executable records only which shared libraries it needs and which symbols it uses. The dynamic linker maps the library into the process at load or run time. Static linking is the case where library code is copied into the executable."

- question: "Give two advantages of shared (dynamically linked) libraries over static libraries."
  type: short-answer
  answer: "First, one copy of the library's code can be mapped into the memory of many running programs, saving memory and disk space. Second, the library can be updated, for example with a security fix, and every program that uses it gets the fix without being relinked."
  explanation: "The trade-offs are a small cost at startup or first call to resolve symbols, and the risk that a program breaks if an incompatible library version is installed."
```

## Explainer

Real programs are split across many source files, and they call code nobody in the project wrote, such as `printf`. The compiler handles one file at a time. When it compiles `main.c` and sees a call to `compute()` defined in `util.c`, it cannot know where `compute` will sit in memory. So it emits a **relocatable object file** (on Linux, an ELF `.o` file). That file holds machine code in a `.text` section, initialized globals in `.data`, a **symbol table** listing what the file defines and what it uses, and **relocation entries** marking every spot that needs an address filled in later.

The **linker**, such as `ld`, which `gcc` runs for you, turns a set of object files into an executable in two steps. **Symbol resolution** matches each reference to exactly one definition. If no definition exists anywhere, you get "undefined reference". If two files define the same global function, you get a "multiple definition" error. **Relocation** then merges the sections of all files, for example every `.text` into one code section. It assigns each section and symbol its final address and walks the relocation entries, patching each call and each global access with the right address.

Libraries come in two forms. A **static library** (a `.a` archive on Linux) is a bundle of object files. The linker copies in only the members that resolve some needed symbol, and the result is a self-contained executable. A **shared library** (`.so` on Linux, `.dll` on Windows) is linked differently. At build time the linker records only that the program needs, say, `libc.so.6`. When the program starts, a **dynamic linker** maps the library into the process and connects the program's references to it. Shared libraries are compiled as **position-independent code**, so the same physical pages can be mapped at different addresses in different processes.

The **loader** is the last step. When a shell runs a program, the `execve` system call reads the executable's header and maps its code and data segments into a fresh address space. It sets up the stack with the arguments and environment, and on systems that use shared libraries it hands control to the dynamic linker. Execution finally reaches the program's entry point, typically a startup routine named `_start`, which in turn calls `main`.

Knowing these stages turns confusing build failures into ordinary diagnostics. A compile error points at a line of source. A link error points at a missing or duplicated symbol. A load-time error, such as a missing shared library, points at the environment the program runs in.
