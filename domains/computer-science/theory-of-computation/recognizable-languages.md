---
id: recognizable-languages
title: Recognizable Languages and Turing Recognizability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: decidable-languages
  type: hard
builds-toward:
- undecidable-problems
tags:
- recognizable
- semi-decidable
- turing-recognizable
stage: abstract-reasoning
status: draft
---

# Recognizable Languages and Turing Recognizability

## Core Idea
A language is recognizable (or recursively enumerable) if there exists a Turing machine that halts and accepts all strings in the language, but may loop indefinitely on strings outside the language. Not all recognizable languages are decidable; the halting problem is recognizable but not decidable.

## Questions

```yaml
- question: "A Turing machine M runs on input w for 10,000 steps without halting. What can you conclude?"
  type: multiple-choice
  options:
    - "w is not in the language that M recognizes"
    - "M has an infinite loop and will never halt on w"
    - "Nothing — M might halt on step 10,001, or it might loop forever; non-halting for any finite number of steps is not conclusive"
    - "w is in the language, because a recognizer must accept all members within a bounded number of steps"
  answer: 2
  explanation: "This is the core asymmetry of recognizable vs. decidable languages. A recognizer guarantees that it will halt and accept if the input is in the language, but makes no guarantee about when (or whether) it will halt on non-members. Observing 10,000 steps of non-halting tells you nothing: the machine might accept on step 10,001, or loop forever. You can never conclude non-membership by watching a recognizer run — this is exactly why recognizable languages are not decidable."

- question: "The halting problem is recognizable but not decidable. Which statement correctly captures what this means?"
  type: multiple-choice
  options:
    - "There exists a Turing machine that always correctly determines in finite time whether any given machine halts on any given input"
    - "There exists a Turing machine that accepts all ⟨M, w⟩ pairs where M halts on w, but may loop forever on pairs where M does not halt"
    - "No Turing machine can accept any instance of the halting problem"
    - "The halting problem can be solved by a more powerful model of computation than a standard Turing machine"
  answer: 1
  explanation: "Recognizability means there exists a machine that correctly accepts all members of the language (all halting computations), which we can build by simulating M on w and accepting if M halts. But this recognizer loops forever when M doesn't halt — it never outputs 'no.' Decidability would require a machine that always halts with a definitive answer, which is impossible for the halting problem. The distinction is between 'can reliably say yes' and 'can reliably say both yes and no.'"

- question: "Every decidable language is also recognizable, because a decider is automatically a recognizer that simply never loops."
  type: true-false
  answer: true
  explanation: "A decider always halts and outputs accept or reject. This means it satisfies the recognizability condition (halts and accepts all members of the language) plus an additional guarantee (also halts and rejects all non-members). Decidability is a strictly stronger condition than recognizability: the class of decidable languages is a proper subset of recognizable languages."

- question: "If a language L is recognizable, its complement L̄ must also be recognizable, since you can just reverse the accept/reject logic of the recognizer."
  type: true-false
  answer: false
  explanation: "This works for deciders (which always halt), but not for recognizers (which may loop). Flipping a recognizer's accept and reject states does not help when the machine loops forever — looping remains looping regardless of what you do to the halting states. For the halting problem, the complement (non-halting computations) is not recognizable. The correct theorem goes the other direction: L is decidable if and only if *both* L and L̄ are recognizable — recognizability of both is required, not guaranteed."

- question: "Explain why a language is decidable if and only if both it and its complement are recognizable, and what running two recognizers in parallel achieves."
  type: short-answer
  answer: "If L is decidable, a decider for L is also a recognizer for both L and L̄ (since it halts and rejects non-members, it recognizes L̄ too). Conversely, if you have a recognizer R₁ for L and a recognizer R₂ for L̄, you can decide L by running both in parallel: for any input w, exactly one of R₁ or R₂ will eventually accept (since w is either in L or in L̄, never both). The first to accept gives the definitive answer — accept if R₁ wins, reject if R₂ wins. This parallel simulation turns two one-sided 'yes' guarantees into a complete decider. The halting problem's complement is not recognizable, which is why this trick cannot be applied to make the halting problem decidable."
  explanation: "This theorem is the bridge between recognizability and decidability. It also explains why showing that a language's complement is not recognizable is a powerful way to prove undecidability — if you can show that no recognizer exists for L̄, you've shown that L cannot be decidable either."
```

## Explainer

You already understand decidable languages — those for which a Turing machine always halts and gives a definitive yes-or-no answer. **Recognizable languages** (also called **recursively enumerable** or **Turing-recognizable** languages) relax this guarantee in a specific way: a recognizer must still halt and accept every string that *is* in the language, but it is allowed to loop forever on strings that are *not* in the language. In other words, a recognizer can reliably say "yes" but might never get around to saying "no."

Think of it like a search process. Suppose you want to know whether a particular mathematical theorem has a proof. You could systematically enumerate all possible proofs, checking each one. If a proof exists, you will eventually find it and halt with "yes." But if no proof exists, you will search forever without ever being certain that you've exhausted all possibilities. This asymmetry — certainty of membership but not of non-membership — is exactly what separates recognizable from decidable. Every decidable language is recognizable (a decider is automatically a recognizer that just never loops), but not every recognizable language is decidable.

The canonical example is the **halting problem**: the language of all ⟨M, w⟩ pairs where Turing machine M halts on input w. You can recognize this language by simply simulating M on w — if M halts, you accept. But if M runs forever, your simulation also runs forever, and you never produce a "no" answer. This is why the halting problem is recognizable but not decidable: there is no machine that can always correctly determine in finite time whether an arbitrary computation will halt.

A useful theorem connects recognizability to decidability: a language is decidable if and only if both it and its complement are recognizable. If you have a recognizer for L and a recognizer for its complement L̄, you can run both in parallel — on any input, exactly one of them will eventually accept, giving you a definitive answer either way. This means that for undecidable but recognizable languages like the halting problem, the complement (the set of non-halting computations) is not even recognizable. There exist languages so far beyond computation that no Turing machine can even partially identify their members.
