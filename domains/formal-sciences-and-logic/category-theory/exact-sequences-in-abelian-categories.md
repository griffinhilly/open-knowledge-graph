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
stage: advanced
status: draft
---

# Exact Sequences in Abelian Categories

## Core Idea
In an abelian category, a sequence of morphisms is exact at an object if the image of one morphism equals the kernel of the next, generalizing the notion of exactness from module categories. Exactness is the central concept of homological algebra and allows systematic study of how information flows through categorical constructions.

## How It's Best Learned
Start with short exact sequences in the category of abelian groups, then extend to modules and general abelian categories. Verify exactness by computing images and kernels. Construct examples of exact and non-exact sequences.

## Common Misconceptions
Exactness at an object depends on both the morphism going in and going out, not either alone. Students sometimes forget that exactness is a local condition—it must hold at every object in the sequence.

## Questions

```yaml
- question: "Consider the sequence of abelian groups 0 → ℤ →^(×2) ℤ →^(mod 2) ℤ/2ℤ → 0. To verify exactness at the middle ℤ, which condition must be checked?"
  type: multiple-choice
  options:
    - "That the map ×2 is surjective onto ℤ"
    - "That ℤ has no zero divisors"
    - "That the image of ×2 (which is 2ℤ) equals the kernel of (mod 2) (which is also 2ℤ)"
    - "That the sequence is exact at 0 first, since exactness propagates from left to right"
  answer: 2
  explanation: "Exactness at the middle ℤ means: im(×2) = ker(mod 2). The image of multiplication by 2 is 2ℤ — all even integers. The kernel of reduction mod 2 is also all even integers. Since these subgroups are equal, the sequence is exact at the middle ℤ. Exactness is a local condition: you check it at each object independently using only the maps immediately entering and leaving that object. Option D reflects a common misunderstanding — exactness at one position does not imply or enable checking at another; each position is verified independently."

- question: "A student is given the sequence A →^f B →^g C →^h D and checks that im(f) = ker(g). They conclude the sequence is exact. Why is this conclusion premature?"
  type: multiple-choice
  options:
    - "Exactness requires f to be a monomorphism, which the student has not verified"
    - "Exactness is a local condition: the student has only verified it at B; they must also verify im(g) = ker(h) at C (and any other intermediate objects) separately"
    - "Exactness requires both f and g to be epimorphisms, which is a stronger condition than image-kernel equality"
    - "The check is complete if A, B, C, D are all finitely generated abelian groups"
  answer: 1
  explanation: "This is the central misconception the topic's Common Misconceptions section flags: exactness is a local condition that must be verified at every intermediate object independently. Checking im(f) = ker(g) tells you about the 'flow' at B, but says nothing about whether im(g) = ker(h) at C. A sequence can be exact at some objects and fail at others. The student must check each position: exactness at B, exactness at C, and so on for every intermediate object in the sequence."

- question: "In a short exact sequence 0 → A →^f B →^g C → 0, the map g: B → C is necessarily an epimorphism (surjective, in the case of modules and abelian groups)."
  type: true-false
  answer: true
  explanation: "Exactness at C means im(g) = ker(C → 0). The kernel of the zero map C → 0 is all of C (every element maps to 0). So im(g) = C — meaning g surjects onto C. This is automatic from the definition: the '0' on the right of a short exact sequence is not decorative; it forces the last non-trivial map to be surjective. Similarly, exactness at A forces f to be injective. The short exact sequence encodes precisely: A embeds into B as a subobject, and C is the quotient B/A."

- question: "A sequence of morphisms with im(f) ⊆ ker(g) at every position (i.e., the composition of any two consecutive morphisms is zero) is an exact sequence."
  type: true-false
  answer: false
  explanation: "A sequence where every consecutive composition is zero is called a chain complex — it satisfies g ∘ f = 0, which means im(f) ⊆ ker(g). But exactness requires the stronger condition im(f) = ker(g): the image must equal the kernel, not merely be contained in it. The gap between a chain complex and an exact sequence is precisely what homology measures: the homology at B is ker(g)/im(f), which is trivial if and only if the sequence is exact at B. Exact sequences are chain complexes with zero homology. The distinction is fundamental — much of algebraic topology is the study of how far chain complexes deviate from exactness."

- question: "What does a short exact sequence 0 → A →^f B →^g C → 0 say about the relationship between A, B, and C?"
  type: short-answer
  answer: "It says that A embeds into B as a subobject (f is a monomorphism), B maps onto C (g is an epimorphism), and C is isomorphic to the quotient B/im(A). Equivalently, B is an 'extension' of C by A — it contains a copy of A, and the remainder is C."
  explanation: "Unpacking the four exactness conditions: exactness at A (with 0 entering) forces f to be injective — A sits inside B. Exactness at C (with 0 following) forces g to be surjective — every element of C has a preimage. Exactness at B says ker(g) = im(f) — everything that maps to 0 in C is exactly the image of A. Together these say B is 'built from' A and C in the sense that A is a subobject and C is the quotient. The short exact sequence is the categorical language for 'B is an extension of C by A,' and it recurs throughout algebra, topology, and geometry wherever objects are constructed by gluing simpler pieces together."
```

## Explainer

You've studied chain complexes and exact sequences in the concrete settings of abelian groups and modules, where kernels and images are specific subgroups you can compute by hand. Abelian categories abstract precisely the structure needed to make this machinery work — kernels, cokernels, images, and the factorization properties that connect them — without fixing what the objects actually are. The notion of an **exact sequence** in an abelian category is not a new definition: it is exactly the definition you already know, now valid in any abelian category at once.

Recall the definition: a sequence of morphisms ··· → A → B → C → ··· is **exact at B** if the image of the incoming morphism (A → B) equals the kernel of the outgoing morphism (B → C). In an abelian category, both kernel and image are defined as subobjects — objects equipped with monomorphisms into B — and "equal" means these subobjects are isomorphic over B. Exactness is a strictly **local condition**: you check it one object at a time. A long sequence can be exact at some objects and fail at others. When you say a sequence is exact, you mean it is exact at every intermediate object; exact at the endpoints requires specifying what the sequence continues with (typically 0).

The most fundamental case is the **short exact sequence** 0 → A → B → C → 0. This says four things simultaneously: the map A → B is a monomorphism (A injects into B); the map B → C is an epimorphism (B surjects onto C); the image of A in B equals the kernel of B → C; and every element of C has a preimage in B. Intuitively, C is obtained from B by "quotienting out" the copy of A inside it. In abelian groups: 0 → ℤ →^×2 ℤ → ℤ/2ℤ → 0 says that doubling injects ℤ into itself, and the cokernel of this injection is ℤ/2ℤ. In module theory this is the language of submodules and quotient modules. In topology it describes how spaces are constructed by attaching pieces. The short exact sequence is the single most reusable sentence in homological algebra.

Why extend exactness to a general abelian category rather than working always in modules? Because the same algebraic structure appears in categories of sheaves, cochain complexes, representations of algebras, and many other settings that don't have a clean element-level description. By proving theorems about exact sequences axiomatically — using only the properties of an abelian category — you obtain results that apply simultaneously to all of these. The **snake lemma**, **five lemma**, and **long exact sequence of a pair** all become theorems in any abelian category, proved once and applied everywhere. Exact sequences in abelian categories are the common scaffolding on which all of homological algebra is built, and the exactness condition is the thread that holds that scaffold together.
