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

## Questions

```yaml
- question: "To prove that a morphism f: A → B is injective via diagram chasing, a student begins by taking an arbitrary element x with f(x) = 0. What must happen next to complete the proof?"
  type: multiple-choice
  options:
    - "Trace x through every available commuting path, using exactness conditions to force x = 0 — each step is logically necessitated by the local diagram structure"
    - "Show that f is also surjective, because injective and surjective morphisms in abelian categories coincide"
    - "Find a map g where g ∘ f is the identity, constructing an explicit left inverse for f"
    - "Appeal to the universal property of the kernel of f to show f must be an isomorphism"
  answer: 0
  explanation: "The diagram chase begins with an element in the kernel of f (i.e., x such that f(x) = 0) and must derive a contradiction or conclude x = 0. The only tools available are commutativity (different paths give the same morphism) and exactness (image of one map equals kernel of the next). The student traces x — possibly lifting it back through a surjective map using exactness, pushing it forward through a commuting square, and using exactness at an adjacent node to conclude membership in a kernel. Every step is forced; there is no freedom to choose. The chain of implications terminates when x must equal 0. This is the essence of diagram chasing: logical necessity at each node."

- question: "In one version of the four lemma, surjectivity of α is a hypothesis. Why is this condition needed — what does it make possible in the chase?"
  type: multiple-choice
  options:
    - "Surjectivity of α ensures its kernel is trivial, which directly constrains the behavior of β"
    - "Surjectivity of α lets you lift elements backward: given an element in β's domain, you can express it as the image of something in α's domain, then track that preimage through the commuting square into adjacent sequences"
    - "Surjectivity of α is needed to guarantee the diagram commutes, which is not automatic"
    - "Without surjectivity of α, the sequence would fail to be exact at the adjacent node"
  answer: 1
  explanation: "Surjectivity is precisely the property that lets you 'lift' — given an element b in B, surjectivity of α: A → B guarantees there exists an a in A with α(a) = b. In a diagram chase, this lifting is how you introduce a new element in a domain where you have more structural information (more exactness conditions, more commuting maps) to work with. Without lifting, the chase can get stuck: you have an element in one place but cannot connect it to the rest of the diagram. Surjectivity (and dually, injectivity) are the 'handles' that let the argument reach across the diagram."

- question: "In a diagram chase, each step follows necessarily from the commutativity and exactness conditions — you are not free to choose where an element goes."
  type: true-false
  answer: true
  explanation: "This logical inevitability is the defining feature of diagram chasing as a proof method. Commutativity means every path between two objects gives the same morphism — you cannot choose a path; they all agree. Exactness means membership in a kernel is equivalent to membership in the corresponding image — if f(x) = 0, then x is in the image of the previous map, which means there exists a unique (up to the relevant structure) preimage. The argument is algorithmic: follow the only available path, apply exactness at each node, and the conclusion is forced. This is what makes diagram chasing reliable and teachable — there is a systematic procedure, not creative inspiration."

- question: "Diagram chasing only works in concrete categories like abelian groups or modules where objects have actual elements. Abstract abelian categories require completely different proof techniques."
  type: true-false
  answer: false
  explanation: "Diagram chasing can be done in two ways. The element-based approach works directly in concrete categories (abelian groups, R-modules) and is often more intuitive. The abstract approach replaces elements with morphisms from projective objects (or uses universal properties of kernels and cokernels) and works in any abelian category, including categories of sheaves or chain complexes where objects have no literal elements. Additionally, the Freyd-Mitchell embedding theorem guarantees that any small abelian category embeds fully faithfully into a category of R-modules, which justifies using element-based arguments even in abstract settings (though this requires care about size issues)."

- question: "What are the two structural properties that diagram chasing relies on, and how does each contribute? Describe the 'zig-zag' pattern that characterizes most diagram chase proofs."
  type: short-answer
  answer: "Diagram chasing relies on (1) commutativity — different paths between the same objects compose to the same morphism — and (2) exactness — the image of each map in an exact sequence equals the kernel of the next. Commutativity lets you reroute an element along an alternative path to reach a node with more information. Exactness lets you perform two key moves: if an element maps to zero under some f, exactness says it came from the previous map (lifting backward); if you have two composable maps with exact sequence, the composite is zero (pushing forward). The zig-zag pattern is: start with an element x; push it forward one map; use exactness to lift backward through a different map to get a new element y; push y forward through yet another map; use exactness again to conclude something about x. Most homological lemmas require two or three such zig-zags."
  explanation: "The zig-zag metaphor captures why diagram chases look complicated at first — they aren't following a single path through the diagram, but alternating between forward and backward moves, using exactness as the mechanism to change direction. Once this pattern is internalized, the Snake Lemma, Five Lemma, and nine lemma all feel like variations on the same basic algorithm."
```

## Explainer

From your study of commutative diagrams, you know that commutativity means different paths between the same two objects always yield the same morphism. From exact sequences, you know that images and kernels interlock — the image of one map is exactly the kernel of the next. Diagram chasing is the proof technique that turns these structural facts into logical arguments: given that certain parts of a diagram commute and certain sequences are exact, what can you conclude about other parts?

The **element-chasing** method is the natural place to start, especially in concrete categories like abelian groups or R-modules. You begin with an arbitrary element x in some object, trace it through morphisms according to the commutativity conditions, and use exactness to deduce membership or zero conditions at each step. For example, to show a morphism is injective, you take an arbitrary x in its kernel (f(x) = 0) and trace through the commuting diagram, using exactness at adjacent objects to conclude x = 0. The argument is a chain of implications: "x maps to 0 under f, so x is in the kernel of f, so by exactness x is in the image of the previous map, so x = g(y) for some y, and by commutativity..." Each step is forced by the structure; you're not choosing — you're following the only possible path.

A concrete illustration is the **four lemma**: given a commutative diagram of two exact rows and vertical morphisms α, β, γ, δ where α is surjective and δ is injective, you can conclude β is injective or γ is surjective (depending on which version you need). The proof is a diagram chase: start with an element in the kernel of β, lift it back through surjectivity of α, push it forward through commutativity, use exactness to conclude it's zero somewhere, then trace back. Every step is a logical necessity from the local structure. The Snake Lemma, which you'll encounter next, is a longer version of the same pattern, connecting kernels and cokernels across rows.

The **abstract approach** to diagram chasing avoids elements entirely, working instead with morphisms and universal properties. An element x can be replaced by a morphism from a terminal object or a projective generator; kernels and cokernels replace membership conditions. This approach works in any abelian category — including categories of sheaves or chain complexes where objects have no actual elements — making the proofs more general. The Freyd-Mitchell embedding theorem guarantees that any small abelian category embeds into a category of modules, which is one way to justify using element-based arguments even in abstract settings. But it is cleaner, when possible, to learn both styles and choose based on context.

The practical skill is recognizing diagram-chasing problems when you see them and having a systematic strategy. Start by identifying what you want to prove (some morphism is zero, injective, or surjective). Choose an arbitrary element (or morphism) witnessing the contrary, if proving by contradiction, or an arbitrary element in the relevant set, if proving directly. Trace it through every available path, applying commutativity and exactness at each step. If you get stuck, look for a zig-zag: go forward one map, use exactness to lift backward through another, then push forward again. Most homological lemmas require at most two or three such zig-zags. Mastering this pattern makes the Snake Lemma, the Five Lemma, and eventually the long exact sequence of a pair feel inevitable rather than magical.
