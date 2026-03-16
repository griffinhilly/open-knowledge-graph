---
id: myhill-nerode-theorem
title: Myhill-Nerode Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: dfa-state-minimization
  type: hard
- id: regular-language-properties
  type: hard
tags:
- automata
- regular-languages
- minimization
stage: advanced
status: draft
---

# Myhill-Nerode Theorem

## Core Idea
The Myhill-Nerode theorem characterizes regular languages via equivalence classes over strings: a language is regular if and only if the set of right equivalence classes (where two strings are equivalent if appending any suffix produces the same acceptance result) is finite. This provides a criterion for regularity independent of any automaton, showing that regularity is fundamentally about how many 'distinct behaviors' a language requires. The theorem yields an algorithm for computing minimal DFAs and proves certain languages (like palindromes) cannot be regular by showing infinite equivalence classes.

## How It's Best Learned
Compute equivalence classes for both regular and non-regular languages explicitly. Prove non-regularity using infinite equivalence classes. Construct minimal DFAs from equivalence class partitions.

## Common Misconceptions
Confusing the right-invariant equivalence relation with other string equivalences. Assuming equivalent strings must be identical. Applying the theorem to non-regular language classes.

## Explainer

From your work with DFA minimization and regular language properties, you know that some languages can be recognized by finite automata and some cannot, and that every regular language has a unique minimal DFA. The **Myhill-Nerode theorem** provides the deepest explanation of *why* this is true — it characterizes regularity purely in terms of the language itself, without reference to any particular machine.

The central concept is an **equivalence relation** on strings. Given a language L over alphabet Σ, we say two strings x and y are **Myhill-Nerode equivalent** (written x ≡_L y) if for every possible suffix z ∈ Σ*, the strings xz and yz are either both in L or both not in L. In other words, x and y are equivalent if no continuation can distinguish them — they behave identically with respect to membership in L. For example, if L is the language of binary strings with an even number of 1s, then the strings "01" and "10" are equivalent because both contain exactly one 1, so appending any suffix produces the same accept/reject outcome for both. But "01" and "00" are *not* equivalent: appending the empty string gives "01" (odd number of 1s, rejected) versus "00" (even number of 1s, accepted).

The theorem states: **a language L is regular if and only if the number of equivalence classes under ≡_L is finite**. Moreover, that number of equivalence classes equals the number of states in the minimal DFA for L. Each equivalence class corresponds to exactly one state — the state represents "everything the machine needs to remember about the input seen so far," and two strings that lead to the same state are precisely those that no suffix can distinguish. This is why the minimal DFA is unique: the equivalence classes are determined by the language, not by any design choice.

The theorem's power as a proof tool comes from its contrapositive: if you can exhibit infinitely many strings that are pairwise distinguishable (each pair separated by some suffix), then the language is not regular. Consider the language {aⁿbⁿ | n ≥ 0}. The strings a, aa, aaa, ... are all pairwise distinguishable: aⁱ and aʲ (with i ≠ j) are separated by the suffix bⁱ, since aⁱbⁱ ∈ L but aʲbⁱ ∉ L. Infinitely many equivalence classes means no finite automaton suffices, so the language is not regular. This argument is often cleaner and more illuminating than the pumping lemma, because it directly identifies what makes the language complex: it requires the machine to remember an unbounded amount of information about the input.
