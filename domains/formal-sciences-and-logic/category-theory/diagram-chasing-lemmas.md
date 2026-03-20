---
id: diagram-chasing-lemmas
title: Diagram Chasing Methods and Lemmas
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: commutative-diagrams-and-composition
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
builds-toward:
- the-snake-lemma
- the-five-lemma
tags:
- diagram-chasing
- element-chasing
- homological-algebra
- proof-methods
stage: advanced
status: draft
---

# Diagram Chasing Methods and Lemmas

## Core Idea
Diagram chasing is the art of proving categorical theorems by carefully tracking elements and morphisms through commutative diagrams, particularly effective in abelian categories where kernels and cokernels provide element-like access. Core techniques include the element method (treating elements as if morphisms from terminal objects), the spine-chasing method, and the abstract 'no-element' proofs that work in any abelian category. Mastery of diagram chasing is essential for understanding homological algebra.

## How It's Best Learned
Practice proving small lemmas via diagram chasing: show that a certain morphism is zero, that two paths commute, or that a morphism is injective. Work both in concrete categories (modules, abelian groups) and abstractly. Compare element-based and element-free approaches.

## Common Misconceptions
Diagram chasing can be done elementwise (treating objects as having elements) or abstractly without choosing elements; both approaches are valid but require different care. The abstract approach applies more generally but is often harder to visualize.

## Explainer

From your study of commutative diagrams, you know that commutativity means different paths between the same two objects always yield the same morphism. From exact sequences, you know that images and kernels interlock — the image of one map is exactly the kernel of the next. Diagram chasing is the proof technique that turns these structural facts into logical arguments: given that certain parts of a diagram commute and certain sequences are exact, what can you conclude about other parts?

The **element-chasing** method is the natural place to start, especially in concrete categories like abelian groups or R-modules. You begin with an arbitrary element x in some object, trace it through morphisms according to the commutativity conditions, and use exactness to deduce membership or zero conditions at each step. For example, to show a morphism is injective, you take an arbitrary x in its kernel (f(x) = 0) and trace through the commuting diagram, using exactness at adjacent objects to conclude x = 0. The argument is a chain of implications: "x maps to 0 under f, so x is in the kernel of f, so by exactness x is in the image of the previous map, so x = g(y) for some y, and by commutativity..." Each step is forced by the structure; you're not choosing — you're following the only possible path.

A concrete illustration is the **four lemma**: given a commutative diagram of two exact rows and vertical morphisms α, β, γ, δ where α is surjective and δ is injective, you can conclude β is injective or γ is surjective (depending on which version you need). The proof is a diagram chase: start with an element in the kernel of β, lift it back through surjectivity of α, push it forward through commutativity, use exactness to conclude it's zero somewhere, then trace back. Every step is a logical necessity from the local structure. The Snake Lemma, which you'll encounter next, is a longer version of the same pattern, connecting kernels and cokernels across rows.

The **abstract approach** to diagram chasing avoids elements entirely, working instead with morphisms and universal properties. An element x can be replaced by a morphism from a terminal object or a projective generator; kernels and cokernels replace membership conditions. This approach works in any abelian category — including categories of sheaves or chain complexes where objects have no actual elements — making the proofs more general. The Freyd-Mitchell embedding theorem guarantees that any small abelian category embeds into a category of modules, which is one way to justify using element-based arguments even in abstract settings. But it is cleaner, when possible, to learn both styles and choose based on context.

The practical skill is recognizing diagram-chasing problems when you see them and having a systematic strategy. Start by identifying what you want to prove (some morphism is zero, injective, or surjective). Choose an arbitrary element (or morphism) witnessing the contrary, if proving by contradiction, or an arbitrary element in the relevant set, if proving directly. Trace it through every available path, applying commutativity and exactness at each step. If you get stuck, look for a zig-zag: go forward one map, use exactness to lift backward through another, then push forward again. Most homological lemmas require at most two or three such zig-zags. Mastering this pattern makes the Snake Lemma, the Five Lemma, and eventually the long exact sequence of a pair feel inevitable rather than magical.
