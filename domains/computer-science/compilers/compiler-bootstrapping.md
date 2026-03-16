---
id: compiler-bootstrapping
title: Compiler Bootstrapping and Self-Hosting
domain: computer-science
course: compilers
prerequisites:
- id: compiler-phases-and-organization
  type: hard
- id: assembly-language-basics
  type: hard
tags:
- bootstrapping
- compilation
- self-hosting
stage: advanced
status: draft
---

# Compiler Bootstrapping and Self-Hosting

## Core Idea
A bootstrap compiler is a compiler written in its own language. Building one requires an initial compiler in another language to compile the bootstrapping version; the bootstrapped compiler then compiles itself, enabling improvements with each iteration and providing a reference implementation.

## Explainer

There is a seemingly paradoxical question at the heart of compiler design: if you want to write a compiler for language X in language X, what compiles the compiler? This is the **bootstrapping problem**, and understanding it requires thinking carefully about the distinction between the language a compiler is *written in* and the language it *compiles*. From your study of compiler phases, you know a compiler is just a program — it reads source code, transforms it through a pipeline of phases, and emits target code. The language it is written in is independent of the language it processes.

The classic solution involves three stages, sometimes called a **bootstrap chain**. First, you write a minimal compiler for language X in some existing language Y — say, you write a C compiler for a subset of X. This compiler does not need to be fast, elegant, or complete; it just needs to correctly compile enough of X to be useful. Second, you rewrite the compiler in X itself, using only the subset that your stage-one compiler supports. Third, you compile this X-written compiler using the stage-one compiler. The result is a binary — produced by Y's toolchain — that can compile X source code. Now you feed the X-written compiler source to *itself* (the binary you just produced), and out comes a new binary that was compiled by an X compiler. This new binary is the **self-hosting** compiler.

The process can be repeated iteratively. Each time you improve the compiler's source code (adding optimizations, fixing bugs, supporting new language features), you compile the new source with the previous version of the compiler. The improvements compound: a compiler that generates better code will, when used to compile itself, produce a faster compiler binary, which in turn compiles the next version faster. This **iterative self-improvement** is one of the elegant properties of bootstrapping. In practice, compiler developers often maintain a "known good" binary of the previous compiler version specifically for this purpose.

Bootstrapping also provides a powerful **correctness check**. If you compile the compiler source with version N to produce binary N+1, and then compile the same source with binary N+1 to produce binary N+2, then binaries N+1 and N+2 should be identical — a property called **fixed-point reproducibility**. If they differ, something is wrong: either the compiler has a bug that manifests differently depending on which binary compiled it, or there is nondeterminism in the compilation process. This technique was used historically to validate early C compilers and remains a standard practice. Real-world examples include GCC (originally bootstrapped from a Pastel compiler), Rust (bootstrapped from an OCaml implementation), and Go (which was rewritten from C to Go and bootstrapped through a translation tool).
