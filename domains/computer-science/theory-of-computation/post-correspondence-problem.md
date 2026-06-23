---
id: post-correspondence-problem
title: Post Correspondence Problem and Applications
domain: computer-science
course: theory-of-computation
prerequisites:
- id: reduction-techniques-undecidability
  type: hard
- id: undecidability-proof-by-reduction
  type: soft
tags:
- pcp
- undecidability
- tiling
- string-matching
- canonical
stage: advanced
status: validated
---

# Post Correspondence Problem and Applications

## Core Idea
The Post Correspondence Problem (PCP) asks: given domino pairs (u₁, v₁), ..., (uₙ, vₙ) of strings, can you arrange them to form identical strings? PCP is undecidable without direct reference to TMs—undecidability arises from combinatorial structure. PCP reductions elegantly prove undecidability of grammar problems (CFG equivalence, ambiguity of unrestricted grammars).

## Questions

```yaml
- question: "Why is the Post Correspondence Problem (PCP) particularly valuable as an intermediate step when proving undecidability of formal language problems?"
  type: multiple-choice
  options:
    - "Because PCP is decidable for small domino sets, making it easier to use in reductions"
    - "Because PCP can be solved in polynomial time, making reductions from it efficient"
    - "Because PCP involves only string concatenation and matching — not Turing machine states or tapes — making reductions to grammar and language problems natural"
    - "Because PCP is the only undecidable problem that does not involve the halting problem"
  answer: 2
  explanation: "PCP's power as a reduction tool comes from its surface structure. It is entirely about strings: can you arrange domino pairs so top and bottom concatenations match? This is conceptually close to formal language problems (which also concern string generation and matching), making PCP reductions to those problems natural and clean. Contrast this with reducing directly from the halting problem, which requires encoding Turing machine configurations — a more complex encoding when the target problem is about grammars. PCP is undecidable but looks nothing like a TM, which is precisely what makes it a useful bridge."

- question: "You are given three domino pairs: (ab/a), (b/ba), (a/ab). Which of the following constitutes a valid PCP solution?"
  type: multiple-choice
  options:
    - "Any arrangement where the total number of characters on top equals the total on the bottom"
    - "The sequence domino 1, domino 2, domino 3 chosen exactly once — giving top='abba', bottom='abaab'"
    - "A sequence (possibly with repetition) of dominoes where the concatenation of all top strings equals the concatenation of all bottom strings"
    - "A sequence where each domino's top string is longer than its bottom string"
  answer: 2
  explanation: "A valid PCP solution is a sequence of domino indices (repetition allowed) such that the joined top strings equal the joined bottom strings. Using dominoes 1, 2, 3 once: top = 'ab'+'b'+'a' = 'abba', bottom = 'a'+'ba'+'ab' = 'abaab' — not a match. Crucially, there is no length requirement: the top and bottom concatenations simply must be identical strings. Dominoes may be used in any order and any number of times. The decision problem asks whether any such sequence exists — and no algorithm can answer this for arbitrary domino sets."

- question: "The Post Correspondence Problem can be decided for any finite set of dominoes by exhaustively testing most sequences up to a sufficiently large length bound."
  type: true-false
  answer: false
  explanation: "This is the key misconception. If a PCP solution exists, there is no computable upper bound on how long it might be. A matching sequence might require thousands of domino repetitions before the top and bottom concatenations align. Since you cannot determine when to stop searching, exhaustive bounded search does not work as a decision procedure. This unboundedness is precisely why PCP is undecidable: the acceptance problem for a Turing machine is encoded into domino matching, and the length of the matching sequence corresponds to the length of the TM's computation — which can be arbitrarily long."

- question: "Undecidability of context-free grammar equivalence can be proved by reducing PCP to it, because the string concatenations in PCP correspond naturally to language generation by CFGs."
  type: true-false
  answer: true
  explanation: "This is one of PCP's most important applications. To show CFG equivalence is undecidable, one constructs two context-free grammars whose generated languages encode the top and bottom concatenations of PCP domino sequences. The two grammars generate the same language if and only if some matching sequence exists — i.e., PCP has a solution. Since PCP is undecidable, CFG equivalence must be undecidable too. The reduction is clean because CFG string generation and PCP string concatenation share the same string-based structure — no TM encoding needed."

- question: "Describe how the domino encoding in the PCP undecidability proof simulates a Turing machine computation, and what guarantees that a matching sequence exists if and only if the TM accepts."
  type: short-answer
  answer: "The construction encodes the TM's sequence of configurations (computation history) into domino pairs. Top strings lag one configuration step behind bottom strings — the bottom starts with the initial configuration while the top starts blank. The dominoes are designed so that each step of the TM's computation produces a domino that advances the top by one configuration, closing the lag. The top and bottom concatenations can only become equal if the TM reaches an accepting configuration, at which point special 'accepting' dominoes close the gap. A match exists iff the TM accepts."
  explanation: "The genius of this encoding is that it converts an infinite computational process (does this TM halt and accept?) into a finite combinatorial question (does this domino collection have a matching sequence?). The computation history framing — each domino corresponds to one transition step — ensures that any matching sequence must be a valid TM computation path ending in acceptance. This is why the proof works: solving PCP would solve the acceptance problem, which is undecidable."
```

## Explainer

From your work on reduction techniques, you know that proving a problem undecidable typically involves showing that a known undecidable problem (like the halting problem) can be reduced to it. The **Post Correspondence Problem (PCP)** is valuable because it provides an undecidable problem that looks nothing like Turing machines — it is purely about string manipulation — yet carries the same computational power, making it an ideal intermediate step for proving other problems undecidable.

Here is the setup. You are given a finite collection of **dominoes**, each with a string on top and a string on bottom. For example: domino 1 has "ab" on top and "a" on bottom; domino 2 has "b" on top and "ba" on bottom; domino 3 has "a" on top and "ab" on bottom. You may use any domino as many times as you like, in any order. The question is: can you arrange a sequence of dominoes so that the concatenation of all the top strings exactly equals the concatenation of all the bottom strings? In this example, choosing dominoes 1, 2, 3 gives top = "ab" + "b" + "a" = "abba" and bottom = "a" + "ba" + "ab" = "abba" — a match. Finding such a sequence, or determining that none exists, is the PCP.

The undecidability of PCP is established by reducing the acceptance problem for Turing machines to it. The construction encodes a TM's computation history — its sequence of configurations — into domino pairs, so that a matching sequence of dominoes exists if and only if the TM accepts its input. The top strings always "lag behind" the bottom strings by one configuration step, and the dominoes are designed so the only way to close this gap and achieve a match is if the TM reaches an accepting state. This encoding is intricate but the key insight is that the combinatorial freedom of choosing and repeating dominoes can simulate arbitrary computation.

PCP's real power is as a **reduction tool**. Because it involves only string concatenation and matching — no tapes, heads, or states — it connects naturally to problems about formal languages and grammars. For instance, proving that equivalence of context-free grammars is undecidable becomes straightforward by reducing PCP to it: construct two CFGs whose generated languages correspond to the top and bottom concatenations of domino sequences, so the grammars generate the same language if and only if PCP has a solution. Similarly, PCP reductions prove undecidability of ambiguity for context-free grammars and various properties of unrestricted grammars. PCP thus serves as a bridge between the Turing machine world and the formal language world, making many undecidability proofs cleaner and more direct than going through the halting problem itself.
