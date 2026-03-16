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
builds-toward:
- arithmetical-hierarchy
- kolmogorov-complexity
tags:
- computability
- language-classes
- recognizability
- decidability
stage: advanced
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

## Explainer

From your study of the halting problem, you know that some problems are simply undecidable—no Turing machine can solve them for all inputs. But undecidability comes in degrees. The RE/co-RE distinction gives you a fine-grained picture of what is just barely undecidable versus what is fully decidable, and it explains precisely where the halting problem sits in the landscape of computation.

**Recognition** is weaker than **decision**. A Turing machine *recognizes* a language L if it accepts every string in L (eventually, even if slowly), but may loop forever on strings outside L. A Turing machine *decides* L if it both accepts strings in L and *rejects*—halts and says "no"—all strings outside L. The gap is the fate of negative inputs: a recognizer makes no promise about them. You might wait arbitrarily long and never know whether the machine will accept or loop forever. A language is **recursively enumerable (RE)** if it has a recognizer, and **decidable (recursive)** if it has a decider.

The halting problem H = {⟨M,x⟩ : M halts on x} is the canonical RE-but-undecidable language. A recognizer is straightforward: simulate M on x; if M halts, accept. But rejecting non-halting instances would require *detecting* that M loops forever—which is undecidable. Its complement co-H is co-RE: the class of complements of RE languages. A language is in co-RE when you can recognize its *complement*. A fundamental theorem ties everything together: a language is **decidable if and only if it is both RE and co-RE**. If you can recognize L and recognize its complement, run both recognizers in parallel—whichever accepts first gives the correct answer, guaranteeing the computation terminates on every input.

This equivalence makes co-RE membership a hardness certificate. If you can show a language is RE but prove (by reduction from the halting problem) that its complement is not RE, the language is not decidable. Your prerequisite on computability reductions is the key tool: reduce from a known undecidable language to show a new problem is also undecidable, and use the structure of the reduction to place it correctly in RE versus co-RE. Rice's theorem is a sweeping corollary: every non-trivial semantic property of Turing machines defines an RE-undecidable language, because recognizing such properties is exactly as hard as the halting problem. The RE/co-RE classes also form the base of the **arithmetical hierarchy**: RE corresponds to Σ₁ and co-RE to Π₁ in the hierarchy of definability by quantifier alternation, connecting computability theory to logic in a precise structural way.
