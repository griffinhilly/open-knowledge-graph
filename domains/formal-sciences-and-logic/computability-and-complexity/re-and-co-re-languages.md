---
id: re-and-co-re-languages
title: Recursively Enumerable and Co-RE Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: computability-reductions
  type: hard
- id: cardinality-and-countability
  type: soft
- id: rices-theorem
  type: soft
- id: recursively-enumerable-languages-computability-and-complexity
  type: soft
builds-toward:
- arithmetical-hierarchy
- kolmogorov-complexity
tags:
- computability
- language-classes
- recognizability
- decidability
stage: formal-systems
status: validated
---
# Recursively Enumerable and Co-RE Languages

## Core Idea
A language is recursively enumerable (RE) if some Turing machine accepts every string in it, though it may loop forever on strings not in it. A language is decidable (recursive) if some TM both accepts strings in it and rejects strings not in it, always halting. Co-RE languages are complements of RE languages. A language is decidable if and only if it is both RE and co-RE. The halting problem is RE but not decidable; its complement is co-RE but not RE. These classes form the base of the arithmetical hierarchy.

## How It's Best Learned
Contrast 'recognizing' (may loop on negatives) versus 'deciding' (always halts). Prove that the class of decidable languages is closed under complement, while RE is not. Use diagonalization to show the existence of languages outside RE entirely — most languages over any alphabet are not even RE.

## Common Misconceptions
- 'Recursively enumerable' does not imply the language is infinite — every finite language is RE (and in fact decidable).
- A TM that loops forever on some inputs still recognizes a language; recognition requires only that all positives are eventually accepted.

## Questions

```yaml
- question: "You build a Turing machine M that, given ⟨P, x⟩, simulates P on x and accepts if P halts — but loops forever if P does not halt. What can you conclude about the halting problem?"
  type: multiple-choice
  options:
    - "M decides the halting problem, since it correctly identifies all halting instances"
    - "M only recognizes the halting problem — it is a recognizer, not a decider, because it loops on non-halting instances rather than rejecting them"
    - "M is impossible to build, since the halting problem is undecidable"
    - "M proves the halting problem is in co-RE but not in RE"
  answer: 1
  explanation: "A recognizer only needs to accept all strings in the language — it makes no promise about non-members, which may cause it to loop. M is a valid recognizer: it accepts every ⟨P, x⟩ where P halts on x, so the halting problem is RE. But M is not a decider, because it loops forever on non-halting instances instead of halting with a 'reject.' A decider must halt on all inputs. The halting problem is RE-but-undecidable: we can recognize it (simulate and accept if halting) but cannot decide it (we cannot reliably detect non-halting). Undecidability and non-RE-membership are different things."

- question: "A computer scientist has M₁ (recognizes language L, may loop on strings not in L) and M₂ (recognizes L̄, may loop on strings in L). She claims this is sufficient to decide L. Is she correct?"
  type: multiple-choice
  options:
    - "No — a recognizer for L̄ only provides information about strings outside L and cannot help decide membership in L"
    - "Yes — run M₁ and M₂ in parallel; one of them is guaranteed to eventually accept any input, giving the correct answer and always halting"
    - "Only if both machines halt within polynomial time"
    - "No — having recognizers for both L and L̄ is equivalent to having a single recognizer for L"
  answer: 1
  explanation: "Running M₁ and M₂ in dovetailed parallel creates a decider: for any input w, either w ∈ L (M₁ eventually accepts) or w ∉ L (M₂ eventually accepts). One must accept, so the combined machine always halts — it is a decider. This is the constructive proof of the theorem: L is decidable if and only if both L and its complement are RE. Note that we interleave steps of M₁ and M₂ rather than running M₁ to completion first (which might loop forever if w ∉ L)."

- question: "If language L is recursively enumerable, then its complement L̄ is also recursively enumerable."
  type: true-false
  answer: false
  explanation: "RE is not closed under complementation — this is one of the most important facts in computability theory. The halting problem H is RE (a recognizer exists), but its complement co-H is not RE (no Turing machine can recognize co-H). If both H and co-H were RE, we could run recognizers for both in parallel to decide H — contradicting undecidability. Only the decidable languages sit at the intersection of RE and co-RE; languages that are RE-but-undecidable have complements that are co-RE-but-not-RE."

- question: "A Turing machine that loops forever on inputs not in L — never halting with a reject — still qualifies as a recognizer for L."
  type: true-false
  answer: true
  explanation: "Recognition only requires that the machine accepts every string in L — eventually, after any finite amount of computation. What the machine does on strings not in L is irrelevant to recognition: it may loop, or it may halt with a reject; both are acceptable behaviors for a recognizer. Only a decider must halt on all inputs (accepting members and explicitly rejecting non-members). Looping on negatives is the normal, expected behavior of a recognizer for an undecidable language — the machine simply has no way to determine that a non-member will never be accepted."

- question: "Why is a language decidable if and only if it is both RE and co-RE? Explain using the definitions of recognition and decision."
  type: short-answer
  answer: "A language L is RE if a Turing machine M₁ accepts every string in L (possibly looping on strings not in L). L is co-RE if a Turing machine M₂ accepts every string not in L (i.e., M₂ recognizes the complement). If L is both RE and co-RE, run M₁ and M₂ in parallel on any input w: either w ∈ L (M₁ eventually accepts) or w ∉ L (M₂ eventually accepts). One must accept, so the combined machine always halts with the correct answer — it is a decider. Conversely, any decidable language is trivially both RE (the decider is itself a recognizer) and co-RE (run the decider and swap accept/reject to get a recognizer for the complement)."
  explanation: "The 'if' direction (RE ∩ co-RE ⊆ decidable) is the constructive argument via parallel simulation. The 'only if' direction (decidable ⊆ RE ∩ co-RE) is immediate from definitions. Together they establish that decidability is exactly the property of being recognizable from both sides — the machine can certify both membership and non-membership. The halting problem fails precisely because its complement is not RE: we can certify halting instances but cannot certify non-halting ones."
```

## Explainer

From your study of the halting problem, you know that some problems are simply undecidable—no Turing machine can solve them for all inputs. But undecidability comes in degrees. The RE/co-RE distinction gives you a fine-grained picture of what is just barely undecidable versus what is fully decidable, and it explains precisely where the halting problem sits in the landscape of computation.

**Recognition** is weaker than **decision**. A Turing machine *recognizes* a language L if it accepts every string in L (eventually, even if slowly), but may loop forever on strings outside L. A Turing machine *decides* L if it both accepts strings in L and *rejects*—halts and says "no"—all strings outside L. The gap is the fate of negative inputs: a recognizer makes no promise about them. You might wait arbitrarily long and never know whether the machine will accept or loop forever. A language is **recursively enumerable (RE)** if it has a recognizer, and **decidable (recursive)** if it has a decider.

The halting problem H = {⟨M,x⟩ : M halts on x} is the canonical RE-but-undecidable language. A recognizer is straightforward: simulate M on x; if M halts, accept. But rejecting non-halting instances would require *detecting* that M loops forever—which is undecidable. Its complement co-H is co-RE: the class of complements of RE languages. A language is in co-RE when you can recognize its *complement*. A fundamental theorem ties everything together: a language is **decidable if and only if it is both RE and co-RE**. If you can recognize L and recognize its complement, run both recognizers in parallel—whichever accepts first gives the correct answer, guaranteeing the computation terminates on every input.

This equivalence makes co-RE membership a hardness certificate. If you can show a language is RE but prove (by reduction from the halting problem) that its complement is not RE, the language is not decidable. Your prerequisite on computability reductions is the key tool: reduce from a known undecidable language to show a new problem is also undecidable, and use the structure of the reduction to place it correctly in RE versus co-RE. Rice's theorem is a sweeping corollary: every non-trivial semantic property of Turing machines defines an RE-undecidable language, because recognizing such properties is exactly as hard as the halting problem. The RE/co-RE classes also form the base of the **arithmetical hierarchy**: RE corresponds to Σ₁ and co-RE to Π₁ in the hierarchy of definability by quantifier alternation, connecting computability theory to logic in a precise structural way.
