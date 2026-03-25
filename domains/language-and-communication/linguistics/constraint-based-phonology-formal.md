---
id: constraint-based-phonology-formal
title: 'Constraint-Based Phonology: Formal Foundations'
domain: language-and-communication
course: linguistics
prerequisites:
- id: formal-phonotactics
  type: hard
- id: optimality-theory-introduction
  type: soft
- id: morpheme-structure-constraints
  type: soft
tags:
- phonology
- constraints
- OT
stage: advanced
status: validated
---
# Constraint-Based Phonology: Formal Foundations

## Core Idea
Constraint-based phonology, especially Optimality Theory, formalizes phonology as the interaction of violable constraints ranked by language. Outputs are optimal (minimal-cost) structures satisfying the ranking; this replaces ordered rules with ranked principles.

## Questions

```yaml
- question: "In a language, the markedness constraint *Complex (no complex onsets) is ranked above the faithfulness constraint Dep-IO (don't insert segments). The underlying form /bla/ is the input. What does EVAL select as the optimal output?"
  type: multiple-choice
  options:
    - "/bla/ — because the input form should always be preserved when possible"
    - "/əbla/ — because inserting a vowel before the cluster avoids the complex onset at no deletion cost"
    - "/la/ — because deleting the /b/ avoids the complex onset"
    - "/bəla/ — because inserting a vowel between consonants satisfies *Complex while violating only the lower-ranked Dep-IO"
  answer: 3
  explanation: "When *Complex outranks Dep-IO, the grammar tolerates faithfulness violations (insertions) to avoid complex onsets. The output /bəla/ violates only Dep-IO (one insertion), which is the lower-ranked constraint. The faithful output /bla/ violates the higher-ranked *Complex and is therefore suboptimal. This demonstrates the core OT insight: the winning form is not the one that satisfies all constraints, but the one that only violates lower-ranked ones. Different languages with different rankings produce different optimal outputs from the same input."

- question: "A language ranks *NoCoda (no coda consonants) above Max-IO (don't delete input segments). Given the underlying form /kant/ as input, what output does OT predict?"
  type: multiple-choice
  options:
    - "/kant/ — because faithfulness constraints should always be satisfied in the optimal output"
    - "/kan/ — because deleting the coda /t/ satisfies the higher-ranked constraint at the cost of the lower-ranked one"
    - "/kanto/ — because epenthesis satisfies both constraints simultaneously"
    - "/ant/ — because onset consonants are less marked than coda consonants"
  answer: 1
  explanation: "/kan/ is optimal because *NoCoda outranks Max-IO: the language tolerates deletion (violating Max-IO) to avoid a coda consonant (satisfying *NoCoda). The faithful output /kant/ would violate the higher-ranked constraint. This is the OT architecture in action: ranked constraints compete, the higher-ranked one wins, and the output is the candidate that minimizes violations starting from the top. A language with the opposite ranking (Max-IO >> *NoCoda) would preserve /kant/ intact."

- question: "In Optimality Theory, every candidate output violates at least one constraint — the 'optimal' output is optimal not because it's perfect, but because it violates only lower-ranked constraints."
  type: true-false
  answer: true
  explanation: "True. This is the most important conceptual shift from rule-based phonology. There is no candidate in OT that satisfies every constraint, because markedness constraints and faithfulness constraints are in permanent tension: satisfying markedness (simplify the output) necessarily violates faithfulness (preserve the input), and vice versa. The optimal candidate is the one that loses to no other candidate in the constraint hierarchy — not the one that violates nothing. A candidate wins by violating fewer highly-ranked constraints than any competitor, even if it violates lower-ranked constraints freely."

- question: "In Optimality Theory, the set of constraints (CON) varies across languages — different languages have different constraints, which is what produces surface differences in pronunciation."
  type: true-false
  answer: false
  explanation: "False. This is the opposite of OT's central claim. CON is universal — the same set of constraints is shared across all human languages. What varies between languages is the *ranking* of those constraints. This universality is theoretically significant: it means cross-linguistic variation is constrained — you can only produce a language by ranking the universal constraints differently, not by inventing new constraints. This predicts that language types will cluster around the possible rankings rather than vary arbitrarily."

- question: "How does Optimality Theory explain why languages differ from each other in phonology, but only in constrained, predictable ways — not arbitrarily?"
  type: short-answer
  answer: "OT explains cross-linguistic variation through ranking permutation over a universal constraint set. All languages have the same constraints (CON); they differ only in how those constraints are ordered relative to one another. The space of possible human language grammars is bounded by the possible rankings of the universal constraints — large but structured. Languages cannot differ arbitrarily because they cannot invent new constraints; they can only reorder existing ones. Typological patterns — the clustering of features across languages — directly reflect constraint interaction properties."
  explanation: "This is OT's main theoretical advantage over rule-based accounts. Rule-based phonology stipulates different rules for each language with no principled reason why language A has certain rules and language B others. OT provides a unified explanation: the same constraints, differently ranked, generate both A and B as predicted outcomes. When a typological generalization holds — 'no language has voiced obstruents only in coda position' — OT explains it as a consequence of constraint interaction, not a coincidence requiring separate stipulation in each language's grammar."
```

## Explainer

From your study of formal phonotactics, you know that every language permits some sound sequences and prohibits others — English allows *str-* onsets but not *tl-*, for example. Rule-based phonology explained these patterns through ordered derivational rules: the underlying form is the input, rules apply in a specified sequence, and the surface form is the output. This works, but it has a significant limitation: when languages differ, you must posit different rules for each one, and explaining why certain patterns cluster together across unrelated languages requires separate stipulation for each case. **Optimality Theory (OT)** offers a different architecture that addresses this directly.

In OT, the grammar has three components. **GEN** generates a large (in principle infinite) set of candidate output forms from any given input — every conceivable way of pronouncing the underlying representation. **CON** is a universal set of constraints, shared across all human languages. **EVAL** applies the ranked constraint hierarchy to filter the candidates, selecting the one that best satisfies the ranking as the grammatical output. The key insight is that constraints are **violable**: the winning candidate is not the one that violates no constraints, but the one that violates the fewest highly ranked ones. Every candidate violates something; the optimal one violates only lower-ranked constraints.

The constraints in CON fall into two fundamental families. **Markedness constraints** penalize phonologically marked structures — complex onsets, closed syllables, nasal vowels, voiced obstruents in coda position, and so on. These constraints push outputs toward simple, typologically common forms. **Faithfulness constraints** require outputs to match the input — preserve the input's segments, maintain their features, keep their order. These constraints resist the simplifying pressure of markedness. The grammar of any language is essentially a ranking of these two families against each other: when markedness outranks faithfulness, the language sacrifices input fidelity to produce simpler structures; when faithfulness outranks markedness, the language preserves input contrasts even at the cost of phonological complexity.

Cross-linguistic variation falls out naturally from ranking differences. Consider syllable-final consonant clusters: a language that ranks *NoCoda* (no coda consonants) above *Max-IO* (don't delete input segments) will delete coda consonants — the output is simpler, at the cost of faithfulness. A language with the opposite ranking will preserve coda clusters. The same two constraints, different ranking, different typological outcome. This is OT's central theoretical achievement: universal constraints plus language-specific rankings generates the space of possible human language grammars, explaining why languages differ in constrained, predictable ways rather than arbitrarily. Where your earlier work in phonotactics described which sequences are legal, OT explains *why* — as the result of constraint interaction rather than stipulated rules.
