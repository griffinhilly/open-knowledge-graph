---
id: exact-sequences-in-abelian-categories
title: Exact Sequences in Abelian Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: chain-complexes-exact-sequences
  type: hard
builds-toward:
- the-snake-lemma
- the-five-lemma
- long-exact-sequences
tags:
- exactness
- kernels
- images
- homology
stage: abstract-reasoning
status: draft
---

# Exact Sequences in Abelian Categories

## Core Idea
In an abelian category, a sequence of morphisms is exact at an object if the image of one morphism equals the kernel of the next, generalizing the notion of exactness from module categories. Exactness is the central concept of homological algebra and allows systematic study of how information flows through categorical constructions.

## How It's Best Learned
Start with short exact sequences in the category of abelian groups, then extend to modules and general abelian categories. Verify exactness by computing images and kernels. Construct examples of exact and non-exact sequences.

## Common Misconceptions
Exactness at an object depends on both the morphism going in and going out, not either alone. Students sometimes forget that exactness is a local condition—it must hold at every object in the sequence.

## Explainer

You've studied chain complexes and exact sequences in the concrete settings of abelian groups and modules, where kernels and images are specific subgroups you can compute by hand. Abelian categories abstract precisely the structure needed to make this machinery work — kernels, cokernels, images, and the factorization properties that connect them — without fixing what the objects actually are. The notion of an **exact sequence** in an abelian category is not a new definition: it is exactly the definition you already know, now valid in any abelian category at once.

Recall the definition: a sequence of morphisms ··· → A → B → C → ··· is **exact at B** if the image of the incoming morphism (A → B) equals the kernel of the outgoing morphism (B → C). In an abelian category, both kernel and image are defined as subobjects — objects equipped with monomorphisms into B — and "equal" means these subobjects are isomorphic over B. Exactness is a strictly **local condition**: you check it one object at a time. A long sequence can be exact at some objects and fail at others. When you say a sequence is exact, you mean it is exact at every intermediate object; exact at the endpoints requires specifying what the sequence continues with (typically 0).

The most fundamental case is the **short exact sequence** 0 → A → B → C → 0. This says four things simultaneously: the map A → B is a monomorphism (A injects into B); the map B → C is an epimorphism (B surjects onto C); the image of A in B equals the kernel of B → C; and every element of C has a preimage in B. Intuitively, C is obtained from B by "quotienting out" the copy of A inside it. In abelian groups: 0 → ℤ →^×2 ℤ → ℤ/2ℤ → 0 says that doubling injects ℤ into itself, and the cokernel of this injection is ℤ/2ℤ. In module theory this is the language of submodules and quotient modules. In topology it describes how spaces are constructed by attaching pieces. The short exact sequence is the single most reusable sentence in homological algebra.

Why extend exactness to a general abelian category rather than working always in modules? Because the same algebraic structure appears in categories of sheaves, cochain complexes, representations of algebras, and many other settings that don't have a clean element-level description. By proving theorems about exact sequences axiomatically — using only the properties of an abelian category — you obtain results that apply simultaneously to all of these. The **snake lemma**, **five lemma**, and **long exact sequence of a pair** all become theorems in any abelian category, proved once and applied everywhere. Exact sequences in abelian categories are the common scaffolding on which all of homological algebra is built, and the exactness condition is the thread that holds that scaffold together.
