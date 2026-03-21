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

## Questions

```yaml
- question: "A program declares a global variable `count` and then declares a local variable also named `count` inside a function. When the compiler resolves the use of `count` inside the function body, how does it determine which declaration to use?"
  type: multiple-choice
  options:
    - "It reports an ambiguity error because two declarations with the same name exist"
    - "It uses the global `count` because global scope takes precedence over local scope"
    - "It finds the local `count` first because the function's scope table sits higher on the scope stack and is searched before outer scopes"
    - "It uses whichever declaration was entered into the symbol table most recently, regardless of scope level"
  answer: 2
  explanation: "Scope resolution uses a stack of symbol tables. The current (innermost) scope sits at the top of the stack; the global scope sits at the bottom. When a name is looked up, the compiler searches from top to bottom, returning the first match found. Because the local `count` is in the function's scope table (near the top), it is found before the global `count`. This is shadowing: a local declaration hides an outer one with the same name. The global declaration is not deleted — it is simply unreachable from inside the function because the local one intercepts the search."

- question: "What happens to the symbol table entries for variables declared inside a function when the compiler finishes processing the function body?"
  type: multiple-choice
  options:
    - "They are moved to the global symbol table so other functions can reference them"
    - "The function's scope table is popped from the stack, making those names inaccessible to the surrounding scope"
    - "They remain in the table but are marked as 'inactive' for future reference"
    - "They are archived in a separate table used only for error reporting and debugging"
  answer: 1
  explanation: "When the compiler exits a block, it pops the scope table for that block from the stack. The names that were declared in that block simply cease to be visible — they cannot be referenced by any code outside the block. This is the compiler implementation of lexical scope: a variable's lifetime in the symbol table mirrors its lexical extent in the source code. Popping the table is also what enables the same local variable name to be reused in a different function without conflict — each function gets its own fresh scope table pushed and popped independently."

- question: "When the compiler encounters a name reference (not a declaration), it searches starting from the current innermost scope and works outward through enclosing scopes until it either finds a matching declaration or exhausts all scopes."
  type: true-false
  answer: true
  explanation: "This outward search — from the innermost scope to progressively outer scopes — is the core of scope chain resolution. It correctly handles shadowing (inner declarations found first) and closures (inner scopes can access outer declarations). If no declaration is found after searching all the way to the global scope, the compiler reports an 'undeclared identifier' error. A new symbol table entry is only created at declaration points, not at use sites."

- question: "A new entry is added to the symbol table each time a variable name is *used* in the program source code."
  type: true-false
  answer: false
  explanation: "Symbol table entries are created at *declaration* points — where a variable, function, or type is introduced into the program. Uses of a name trigger a *lookup* in the symbol table, not an insertion. If a use-site lookup fails (no matching declaration found in any enclosing scope), the compiler reports an undeclared identifier error. Inserting entries at every use would make the symbol table enormous and would destroy the scoping semantics — you would no longer know which declaration a name refers to."

- question: "Why is a stack the natural data structure for implementing scope resolution, and what do pushing and popping correspond to in the program's structure?"
  type: short-answer
  answer: "A stack naturally models nested block structure: scopes are nested inside one another, and the innermost scope is always the one currently being processed — exactly what a stack's top represents. Pushing a new scope table corresponds to entering a new block (a function body, an if-statement, a loop body); popping corresponds to exiting that block. Name lookup searches from the top of the stack downward, finding the innermost matching declaration first and naturally implementing shadowing. Because blocks nest but never partially overlap, the LIFO discipline of a stack exactly matches the enter/exit pattern of block scoping."
  explanation: "This is a case where the data structure perfectly mirrors the logical structure. The scope nesting in source code is a tree; a depth-first traversal of that tree during compilation follows a path from root to current node — exactly what a stack tracks. Alternative structures (like a single flat table) would require complex bookkeeping to achieve the same semantics."
```

## Explainer

When a compiler processes `x = y + 1`, it needs to answer concrete questions: What type is `y`? Where is it stored? Was it even declared? The **symbol table** is the data structure that holds these answers. It maps each identifier (variable name, function name, type name) to a record containing everything the compiler knows about it — its type, memory location, whether it is a constant, its parameter list if it is a function, and so on. From your study of hash tables, you know how to build a dictionary with fast lookup by key. The symbol table is exactly that dictionary, specialized for compiler use.

The complication is **scope**. Most languages allow the same name to mean different things in different parts of the program. A variable `x` declared inside a function is different from an `x` declared at the global level, and a new `x` declared inside an inner block shadows the outer one. The compiler must resolve each use of a name to the correct declaration, which means the symbol table must understand the nesting structure of scopes. This is where the connection to abstract syntax trees becomes essential: the AST encodes the block structure of the program, and the compiler uses it to determine which scope each name reference belongs to.

The standard implementation uses a **stack of symbol tables**, one per scope level. When the compiler enters a new block (a function body, an if-statement block, a loop body), it pushes a new empty table onto the stack. Declarations within that block are inserted into the top table. When a name is looked up, the compiler searches from the top of the stack downward — first the current scope, then the enclosing scope, then the next enclosing scope, all the way to the global scope. This **scope chain** naturally implements the shadowing rule: a local declaration is found before the global one because it sits higher on the stack. When the compiler exits a block, it pops the top table, and those local names become inaccessible.

This design also enables **separate compilation**. When compiling one module, the compiler doesn't have access to the source code of other modules — but it needs to know the types and signatures of their exported symbols. The symbol table for the current module is populated with declarations imported from headers or module interfaces, allowing the compiler to type-check and generate code without seeing the full program. At link time, the linker resolves the actual memory addresses. The symbol table thus serves as the compiler's memory throughout the entire compilation pipeline, from parsing through code generation.
