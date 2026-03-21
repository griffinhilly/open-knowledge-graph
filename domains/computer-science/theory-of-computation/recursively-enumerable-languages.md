---
id: recursively-enumerable-languages
title: Recursively Enumerable Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: decidability
  type: hard
builds-toward:
- recognizability-vs-decidability
- halting-problem
tags:
- computability
- formal-languages
- turing-completeness
stage: advanced
status: draft
---

# Recursively Enumerable Languages

## Core Idea
A language is recursively enumerable (RE) if a Turing machine exists that halts-and-accepts every string in the language; for strings outside the language, the machine may never halt. RE languages equal Type 0 languages in the Chomsky hierarchy. They represent the boundary of mechanical computation: problems whose solutions can be systematically generated (enumerated) but not necessarily verified in finite time characterize this class.

## Questions

```yaml
- question: "A Turing machine M runs on input w. If w ∈ L, M eventually halts and accepts. If w ∉ L, M runs forever without halting. Which statement best describes L?"
  type: multiple-choice
  options:
    - "L is decidable because M correctly handles every string that belongs to L"
    - "L is recursively enumerable but not necessarily decidable, because M accepts members but never halts on non-members"
    - "L is not recursively enumerable because no Turing machine halts on all inputs of L"
    - "L is context-sensitive because the machine always terminates on strings it accepts"
  answer: 1
  explanation: "L is RE by definition: a TM exists that accepts every string in L (and for strings outside L, may loop). L is not necessarily decidable because a decider must halt on ALL inputs — both members and non-members — giving an explicit yes or no. The machine described never provides a 'no' answer; it simply runs forever on non-members. This asymmetry is the defining feature of RE languages that are not recursive."

- question: "Which condition is both necessary and sufficient for a language L to be decidable (recursive)?"
  type: multiple-choice
  options:
    - "L is recognized by some Turing machine that accepts all strings in L"
    - "L and its complement are both recursively enumerable"
    - "L can be enumerated by a Turing machine that lists all its members in finite time"
    - "L is recognized by a Turing machine that halts within polynomial time on every input"
  answer: 1
  explanation: "A language is decidable if and only if both it and its complement are RE. If both have recognizers, you can run them in parallel: whichever halts first gives the answer. If only L has a recognizer (its complement has none), you can confirm membership but never confirm non-membership — so L is RE but not decidable. Option A is only the definition of RE, not decidability. Option D is a stronger condition (polynomial time) that implies decidability but is not equivalent to it."

- question: "If you run a Turing machine on a string for one million steps without seeing it accept, you can safely conclude the string is not in the language (for an RE language that is not decidable)."
  type: true-false
  answer: false
  explanation: "False. For an RE language with no decider, you can never conclude non-membership from silence. The machine might accept after one million and one steps, or after a trillion steps — any finite upper bound is meaningless. This is the fundamental asymmetry of RE languages: you can confirm 'yes' by waiting for acceptance, but you cannot confirm 'no' by waiting any fixed amount of time. That inability to certify non-membership is exactly what distinguishes RE from decidable."

- question: "The halting problem — the language of (M, w) pairs where Turing machine M halts on input w — is recursively enumerable."
  type: true-false
  answer: true
  explanation: "True. A recognizer for the halting problem exists: simulate M on w, and if M ever halts, accept. If M truly halts on w, this simulation eventually terminates and accepts — so every member of the halting language is accepted. For pairs where M loops forever on w, the simulation also loops forever (no rejection). This confirms the halting language is RE. It is the canonical example of a language that is RE but not decidable, since no machine can always determine whether an arbitrary TM halts."

- question: "Why is it impossible to convert an arbitrary RE recognizer into a decider for the same language — why can't you simply add a step-counter that halts the machine and outputs 'reject' after N steps?"
  type: short-answer
  answer: "You cannot choose a fixed N because accepting computations can take arbitrarily many steps. For any bound N you pick, there exists a string in the language whose accepting computation requires more than N steps — your time-limited machine would incorrectly reject it. There is no computable function that maps each input to the maximum steps needed for acceptance, because computing such a bound would itself solve the halting problem. The inability to find a finite cutoff is precisely why the RE-but-not-decidable languages cannot be decided: you can never rule out a later acceptance."
  explanation: "This gets at the heart of undecidability. If you knew, for each input, the maximum number of steps any accepting computation could take, you could build a decider. But computing that bound is equivalent to solving the halting problem, which is undecidable. The RE class captures exactly those languages where membership can be confirmed but non-membership cannot — and no engineering trick can bridge that gap without additional information about the language structure."
```

## Explainer

From your study of Turing machines and decidability, you know that a **decidable** (recursive) language has a Turing machine that always halts — it says "yes" for strings in the language and "no" for strings outside it. A **recursively enumerable** language relaxes this guarantee in a crucial way: the machine must still halt and accept every string that belongs to the language, but for strings that do not belong, it is allowed to run forever. You get a definitive "yes" but never a guaranteed "no."

Think of it like a search process. Imagine you are looking for a proof that a mathematical statement is true. If a proof exists, a systematic search will eventually find it — you can enumerate all possible proof strings in order of length and check each one. If the statement is provable, your search halts with the proof. But if the statement is not provable, your search continues indefinitely; you never reach a point where you can confidently declare "no proof exists," because there is always a longer candidate you haven't tried yet. This asymmetry between confirmation and refutation is the defining feature of recursively enumerable languages.

The name "recursively enumerable" comes from an equivalent characterization: a language is RE if and only if there exists a Turing machine that **enumerates** (lists) all strings in the language, one by one, possibly with repetitions and in no particular order. If you wait long enough, every member of the language will eventually appear on the list. But if a string is not in the language, it simply never shows up — and you can never be sure it won't appear later. This enumeration perspective connects to the idea of a **semi-decision procedure**: a process that can confirm membership but cannot confirm non-membership.

The gap between RE and decidable languages has profound consequences. The **halting problem** — does a given Turing machine halt on a given input? — is the classic example of a language that is RE but not decidable. You can confirm halting by simply running the machine and waiting for it to stop, but you cannot confirm non-halting because the machine might halt after any number of steps. This means the complement of an RE language is not necessarily RE; in fact, a language is decidable if and only if both it and its complement are recursively enumerable. When one side of this pair breaks — when you can enumerate the "yes" instances but not the "no" instances — you have crossed from decidability into the territory of undecidability, and recursively enumerable languages mark exactly that frontier.
