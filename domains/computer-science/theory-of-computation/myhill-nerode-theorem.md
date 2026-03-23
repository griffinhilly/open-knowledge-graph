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
status: validated
---

# Myhill-Nerode Theorem

## Core Idea
The Myhill-Nerode theorem characterizes regular languages via equivalence classes over strings: a language is regular if and only if the set of right equivalence classes (where two strings are equivalent if appending any suffix produces the same acceptance result) is finite. This provides a criterion for regularity independent of any automaton, showing that regularity is fundamentally about how many 'distinct behaviors' a language requires. The theorem yields an algorithm for computing minimal DFAs and proves certain languages (like palindromes) cannot be regular by showing infinite equivalence classes.

## How It's Best Learned
Compute equivalence classes for both regular and non-regular languages explicitly. Prove non-regularity using infinite equivalence classes. Construct minimal DFAs from equivalence class partitions.

## Common Misconceptions
Confusing the right-invariant equivalence relation with other string equivalences. Assuming equivalent strings must be identical. Applying the theorem to non-regular language classes.

## Questions

```yaml
- question: "For language L = {w ∈ {0,1}* | w ends in '1'}, are the strings '01' and '111' Myhill-Nerode equivalent?"
  type: multiple-choice
  options:
    - "No, because the strings have different lengths and different content"
    - "Yes, because both strings end in '1', and any suffix appended produces the same accept/reject outcome for both"
    - "No, because '01' has fewer 1s than '111', which affects acceptance of continuations"
    - "Yes, because both strings are accepted by L, so they must be in the same equivalence class"
  answer: 1
  explanation: "Two strings are Myhill-Nerode equivalent if no suffix can distinguish them: for every z, xz ∈ L ↔ yz ∈ L. Both '01' and '111' end in 1. For any suffix z: if z is empty, both are in L; if z ends in 0, neither is in L; if z ends in 1, both are in L. No suffix distinguishes them, so they are equivalent. Option D is wrong — acceptance of the strings themselves does not determine equivalence; equivalence is about identical behavior under *all* extensions, including those that push them outside L."

- question: "To prove that L = {aⁿbⁿ | n ≥ 0} is not regular using the Myhill-Nerode theorem, you would:"
  type: multiple-choice
  options:
    - "Show that the language cannot be expressed as a regular expression"
    - "Exhibit infinitely many strings that are pairwise Myhill-Nerode distinguishable — each pair separated by some suffix — proving the language requires infinitely many equivalence classes"
    - "Show that any DFA for L requires at least n+1 states for inputs of length 2n, so the minimal DFA grows without bound"
    - "Apply the pumping lemma to a string in L and show that any pumping produces a string outside L"
  answer: 1
  explanation: "The Myhill-Nerode approach is direct: for each i ≠ j, strings aⁱ and aʲ are distinguishable by the suffix bⁱ — because aⁱbⁱ ∈ L but aʲbⁱ ∉ L. Since a, a², a³, ... are all pairwise distinguishable, there are infinitely many equivalence classes, so L is not regular. Option C describes a consequence but not the proof technique. Option D (pumping lemma) also works but is typically less direct and less illuminating than identifying concrete distinguishing suffixes."

- question: "If two strings reach the same state in the minimal DFA for language L, they are Myhill-Nerode equivalent."
  type: true-false
  answer: true
  explanation: "The Myhill-Nerode theorem establishes an exact correspondence: each equivalence class under ≡_L corresponds to exactly one state in the minimal DFA. Two strings reach the same state if and only if no suffix can distinguish their futures — precisely the definition of Myhill-Nerode equivalence. In a non-minimal DFA, equivalent strings might land in different (redundant) states; but the *minimal* DFA collapses all equivalent strings into one state. This is why the minimal DFA is unique: its states are determined by the language itself, not by any design choice."

- question: "A regular language can have infinitely many Myhill-Nerode equivalence classes, as long as the DFA recognizing it has finitely many states."
  type: true-false
  answer: false
  explanation: "The Myhill-Nerode theorem states the equivalence in both directions: a language is regular *if and only if* the number of equivalence classes under ≡_L is *finite*. Moreover, that number exactly equals the number of states in the minimal DFA. A regular language recognized by a DFA with n states has exactly n equivalence classes — no more. If a language has infinitely many equivalence classes, it cannot be regular and no finite automaton can recognize it, regardless of construction."

- question: "What does the number of Myhill-Nerode equivalence classes for a language tell you, and why is this significant?"
  type: short-answer
  answer: "The number of equivalence classes equals the number of states in the minimal DFA for the language — if finite. Each class corresponds to one state representing everything the automaton needs to remember about the input seen so far. This is significant because it shows the minimal DFA is uniquely determined by the language itself, not by any particular construction, and reveals the fundamental 'memory requirement' of the language: how many distinct situations the automaton must distinguish to correctly classify all inputs. A language requiring infinitely many classes cannot be regular."
  explanation: "The Myhill-Nerode theorem gives regularity a characterization purely in terms of the language's structure — independent of any machine model. This makes it both a theoretical foundation and a practical tool: computing equivalence classes is the basis for DFA minimization algorithms, and exhibiting infinite classes is often the cleanest proof of non-regularity."
```

## Explainer

From your work with DFA minimization and regular language properties, you know that some languages can be recognized by finite automata and some cannot, and that every regular language has a unique minimal DFA. The **Myhill-Nerode theorem** provides the deepest explanation of *why* this is true — it characterizes regularity purely in terms of the language itself, without reference to any particular machine.

The central concept is an **equivalence relation** on strings. Given a language L over alphabet Σ, we say two strings x and y are **Myhill-Nerode equivalent** (written x ≡_L y) if for every possible suffix z ∈ Σ*, the strings xz and yz are either both in L or both not in L. In other words, x and y are equivalent if no continuation can distinguish them — they behave identically with respect to membership in L. For example, if L is the language of binary strings with an even number of 1s, then the strings "01" and "10" are equivalent because both contain exactly one 1, so appending any suffix produces the same accept/reject outcome for both. But "01" and "00" are *not* equivalent: appending the empty string gives "01" (odd number of 1s, rejected) versus "00" (even number of 1s, accepted).

The theorem states: **a language L is regular if and only if the number of equivalence classes under ≡_L is finite**. Moreover, that number of equivalence classes equals the number of states in the minimal DFA for L. Each equivalence class corresponds to exactly one state — the state represents "everything the machine needs to remember about the input seen so far," and two strings that lead to the same state are precisely those that no suffix can distinguish. This is why the minimal DFA is unique: the equivalence classes are determined by the language, not by any design choice.

The theorem's power as a proof tool comes from its contrapositive: if you can exhibit infinitely many strings that are pairwise distinguishable (each pair separated by some suffix), then the language is not regular. Consider the language {aⁿbⁿ | n ≥ 0}. The strings a, aa, aaa, ... are all pairwise distinguishable: aⁱ and aʲ (with i ≠ j) are separated by the suffix bⁱ, since aⁱbⁱ ∈ L but aʲbⁱ ∉ L. Infinitely many equivalence classes means no finite automaton suffices, so the language is not regular. This argument is often cleaner and more illuminating than the pumping lemma, because it directly identifies what makes the language complex: it requires the machine to remember an unbounded amount of information about the input.
