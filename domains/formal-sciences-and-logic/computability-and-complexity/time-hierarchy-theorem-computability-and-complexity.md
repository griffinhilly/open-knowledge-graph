---
id: time-hierarchy-theorem-computability-and-complexity
title: Time Hierarchy Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: turing-machines-formal
  type: hard
builds-toward:
- space-hierarchy-theorem
tags:
- separations
- resource-bounded
- computability
stage: advanced
status: validated
---

# Time Hierarchy Theorem

## Core Idea
The time hierarchy theorem states that for reasonable complexity measures, strictly greater time allows a Turing machine to decide strictly more languages. Formally, if f and g are time-constructible functions with f·log(f) = o(g), then DTIME(f) ⊊ DTIME(g). This unconditionally proves P ⊂ EXPTIME and guarantees unbounded growth of computational power with time resources.

## How It's Best Learned
Understand the proof using diagonalization: a TM with more time can solve the time-bounded halting problem for TMs with less time, constructing a language not in the smaller class.

## Questions

```yaml
- question: "A researcher claims that DTIME(n²) = DTIME(n³) — that cubic time provides no additional computational power over quadratic time. The time hierarchy theorem implies:"
  type: multiple-choice
  options:
    - "This is possible; the theorem only applies when the time bounds differ by an exponential factor"
    - "This is false — the theorem unconditionally guarantees DTIME(n²) ⊊ DTIME(n³), so there are languages requiring cubic time that cannot be solved in quadratic time"
    - "This is an open question, analogous to P vs. NP, requiring new proof techniques to resolve"
    - "This is false only if P ≠ NP; otherwise additional time might not help within polynomial time"
  answer: 1
  explanation: "The time hierarchy theorem provides an unconditional separation: given time-constructible f and g satisfying f(n)·log f(n) = o(g(n)), we have DTIME(f) ⊊ DTIME(g). For n² and n³: (n²)·log(n²) = 2n²log n = o(n³), so the condition is met and DTIME(n²) ⊊ DTIME(n³) holds without any assumptions. This is a proven theorem, not a conjecture. The claim DTIME(n²) = DTIME(n³) is simply false, as a matter of proven mathematics — no appeal to P vs. NP is needed."

- question: "The time hierarchy theorem's proof constructs a language not in DTIME(f) by building a TM D that operates in time g(n). The key mechanism is:"
  type: multiple-choice
  options:
    - "Reducing DTIME(f) to the halting problem and showing the halting problem is not in DTIME(g)"
    - "Showing that the complement of any language in DTIME(f) lies in DTIME(g) by a padding argument"
    - "Diagonalizing: D simulates each time-f TM Mᵢ on input ⟨i⟩ and does the opposite, ensuring D's language differs from every time-f machine on at least one input"
    - "Using a counting argument to show DTIME(g) must contain more languages than DTIME(f)"
  answer: 2
  explanation: "Diagonalization is Cantor's trick applied to computability. The TM D has budget g(n). On input ⟨i⟩, it simulates Mᵢ on ⟨i⟩ for f(|⟨i⟩|)·log f(|⟨i⟩|) steps — affordable because g grows faster. If Mᵢ accepts, D rejects; if Mᵢ doesn't accept in time, D accepts. By construction, D's language differs from every time-f machine on the input ⟨i⟩ corresponding to that machine. So D's language is not in DTIME(f), but D itself runs in time g(n), placing the language in DTIME(g). The log f overhead accounts for the simulation slowdown."

- question: "The time hierarchy theorem proves P ⊊ EXPTIME unconditionally — no unproven conjectures are required."
  type: true-false
  answer: true
  explanation: "P = DTIME(n^k for all k), and EXPTIME = DTIME(2^{n^k} for all k). Taking f = n^k and g = 2^n, we have f(n)·log f(n) = n^k · k·log n = o(2^n), so the hierarchy theorem applies and gives DTIME(n^k) ⊊ DTIME(2^n). Since this holds for every polynomial k, P ⊊ EXPTIME is proven as a theorem. This is one of the few unconditional separations in complexity theory — most other separations (like P vs. NP or P vs. PSPACE) remain open conjectures."

- question: "Because the time hierarchy theorem proves separations between deterministic time classes using diagonalization, the same technique can be applied to prove P ≠ NP."
  type: true-false
  answer: false
  explanation: "The diagonalization argument works cleanly for DTIME(f) vs. DTIME(g) because both sides are deterministic: D can simulate any deterministic TM Mᵢ in a predictable way. The argument breaks down for deterministic vs. nondeterministic comparisons (P vs. NP) because nondeterministic TMs can produce exponentially many computation paths — a deterministic simulator cannot enumerate and 'do the opposite of' all of them within a polynomial time budget. This barrier is formalized by the relativization result: there exist oracles relative to which P=NP and oracles relative to which P≠NP, meaning diagonalization-based proofs cannot resolve P vs. NP."

- question: "Explain why the time hierarchy theorem is an unconditional result, and contrast this with the open status of P vs. NP."
  type: short-answer
  answer: "The time hierarchy theorem is unconditional because its proof — diagonalization over deterministic TMs — is entirely constructive and makes no unverified assumptions. We explicitly build a TM D that runs in time g(n) and decides a language provably not in DTIME(f(n)). Every step of the argument is verified mathematics. P vs. NP asks whether nondeterministic polynomial time adds power over deterministic polynomial time. Here the diagonalization technique fails: a deterministic simulator of an NTM may not fit within polynomial time, and no other proof technique has succeeded. The separation might be true (P≠NP) or false (P=NP), but proving either direction requires fundamentally new ideas that bypass the known barriers to diagonalization-style proofs."
  explanation: "The contrast highlights why unconditional separations are rare in complexity theory. Within deterministic time, we have a clean simulation relationship: a DTM can simulate another DTM with a known overhead, making diagonalization work. The moment nondeterminism enters, or we ask about space vs. time, the simulation relationships become unclear and diagonalization fails to give a clean separation. This is the heart of why P vs. NP is hard — not that the answer is unknown, but that our current proof tools are provably insufficient to decide it."
```

## Explainer

From your study of **Turing machines** and **time complexity classes**, you know that DTIME(f(n)) is the set of languages decidable by a deterministic TM in O(f(n)) steps. A natural question follows immediately: does more time actually buy you more computational power? Could DTIME(n²) and DTIME(n³) be the same class — where the extra time is just wasted? The time hierarchy theorem answers definitively: no. More time strictly expands what can be decided.

The formal statement requires a technical condition: f and g must be **time-constructible** (a TM can compute f(n) in O(f(n)) steps, so the function is "usable" as a resource bound), and the gap between them must satisfy f(n)·log f(n) = o(g(n)). Under these conditions, DTIME(f) is a *strict subset* of DTIME(g) — there are languages in the larger class that provably cannot be decided in the smaller time bound. The log f factor is a minor technical artifact of simulating one TM on another; in practice the theorem says things like DTIME(n) ⊊ DTIME(n²) ⊊ DTIME(n³) ⊊ ··· and P ⊊ EXPTIME.

The proof uses **diagonalization** — the same technique Cantor used to prove uncountability, adapted by Turing to prove undecidability, and now applied to complexity. The idea: a TM D with time bound g(n) enumerates all TMs Mᵢ in order, simulates Mᵢ on input ⟨i⟩ for at most f(|i|)·log f(|i|) steps, and does the opposite of what Mᵢ does. D has enough time to run this simulation (because g grows faster than f·log f) and enough time to *not* be fooled by any time-f(n) machine. The language D decides — "all inputs ⟨i⟩ where Mᵢ doesn't accept within the time limit" — cannot be decided in time f(n), because D's own construction ensures it differs from every such machine on at least one input.

The theorem has immediate structural consequences. It guarantees the polynomial hierarchy is infinite *if* the classes are all distinct: P is strictly inside EXP, which is strictly inside doubly-exponential time, and so on without bound. More subtly, it shows that computational power grows continuously with time — there is no "plateau" where extra time stops helping. This is the unconditional separation in complexity theory, requiring no assumption about P vs. NP or any open conjecture.

One important contrast with NP: the time hierarchy theorem gives a separation between *deterministic* time classes. We know DTIME(n) ⊊ DTIME(n²) unconditionally. But the question of whether P ⊊ NP — a separation between deterministic and nondeterministic time — remains open. Diagonalization works cleanly when both sides of the comparison are deterministic; the nondeterministic case resists the same technique, which is part of why P vs. NP is so hard.
