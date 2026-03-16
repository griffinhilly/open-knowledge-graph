---
id: symbol-tables-and-scope
title: Symbol Tables and Scope Resolution
domain: computer-science
course: compilers
prerequisites:
- id: hash-tables
  type: hard
- id: abstract-syntax-trees
  type: hard
builds-toward:
- semantic-analysis
- type-inference-algorithms
tags:
- symbol-table
- scope
- name-resolution
stage: advanced
status: draft
---

# Symbol Tables and Scope Resolution

## Core Idea
A symbol table is a data structure mapping identifiers to their properties (type, storage location, scope). Scoping rules determine which declaration a name reference refers to. Block scoping creates nested symbol tables; a name lookup searches the current scope, then outer scopes (the scope chain). Proper scope handling prevents name collisions and enables separate compilation of modules.

## Explainer

When a compiler processes `x = y + 1`, it needs to answer concrete questions: What type is `y`? Where is it stored? Was it even declared? The **symbol table** is the data structure that holds these answers. It maps each identifier (variable name, function name, type name) to a record containing everything the compiler knows about it — its type, memory location, whether it is a constant, its parameter list if it is a function, and so on. From your study of hash tables, you know how to build a dictionary with fast lookup by key. The symbol table is exactly that dictionary, specialized for compiler use.

The complication is **scope**. Most languages allow the same name to mean different things in different parts of the program. A variable `x` declared inside a function is different from an `x` declared at the global level, and a new `x` declared inside an inner block shadows the outer one. The compiler must resolve each use of a name to the correct declaration, which means the symbol table must understand the nesting structure of scopes. This is where the connection to abstract syntax trees becomes essential: the AST encodes the block structure of the program, and the compiler uses it to determine which scope each name reference belongs to.

The standard implementation uses a **stack of symbol tables**, one per scope level. When the compiler enters a new block (a function body, an if-statement block, a loop body), it pushes a new empty table onto the stack. Declarations within that block are inserted into the top table. When a name is looked up, the compiler searches from the top of the stack downward — first the current scope, then the enclosing scope, then the next enclosing scope, all the way to the global scope. This **scope chain** naturally implements the shadowing rule: a local declaration is found before the global one because it sits higher on the stack. When the compiler exits a block, it pops the top table, and those local names become inaccessible.

This design also enables **separate compilation**. When compiling one module, the compiler doesn't have access to the source code of other modules — but it needs to know the types and signatures of their exported symbols. The symbol table for the current module is populated with declarations imported from headers or module interfaces, allowing the compiler to type-check and generate code without seeing the full program. At link time, the linker resolves the actual memory addresses. The symbol table thus serves as the compiler's memory throughout the entire compilation pipeline, from parsing through code generation.
