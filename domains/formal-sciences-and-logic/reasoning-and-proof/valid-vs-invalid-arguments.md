---
id: valid-vs-invalid-arguments
title: Valid vs. Invalid Arguments
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: what-is-an-argument
    type: hard
  - id: if-then-thinking
    type: soft
builds-toward:
  - counterexamples-in-reasoning
  - deductive-vs-inductive-reasoning
  - direct-proof-introduction
  - deductive-reasoning-and-formal-proofs
tags: [validity, soundness, arguments, logic]
stage: abstract-reasoning
status: draft
---

# Valid vs. Invalid Arguments

## Core Idea
An argument is valid if the conclusion must be true whenever all the premises are true — there is no possible way for the premises to be true and the conclusion false. Validity is about the structure of the argument, not the truth of its premises. An argument is sound if it is valid and all its premises are actually true. An invalid argument has a logical gap: even if the premises are true, the conclusion might not follow. Distinguishing valid from invalid arguments is the central skill of logical reasoning.

## How It's Best Learned
Present pairs of arguments with the same premises but different conclusions, and ask which conclusions are guaranteed. Use concrete examples first: "All dogs are mammals. Rex is a dog. Therefore Rex is a mammal" (valid) vs. "All dogs are mammals. Rex is a mammal. Therefore Rex is a dog" (invalid — Rex could be a cat). Introduce the concept of counterexample informally: an invalid argument is one where you can imagine a scenario where the premises are true but the conclusion is false.

## Common Misconceptions
- Thinking a valid argument must have a true conclusion. A valid argument with false premises can have a false conclusion — validity only guarantees the conclusion IF the premises are true.
- Confusing validity with truth. "All fish can fly. Salmon are fish. Therefore salmon can fly" is valid (the structure is perfect) but not sound (the first premise is false).
- Believing that a true conclusion proves the argument is valid. The conclusion "2 + 2 = 4" is true, but "The sky is green, therefore 2 + 2 = 4" is not a valid argument.

## Questions

```yaml
- question: "Which of the following arguments is valid?"
  type: multiple-choice
  options:
    - "Some birds can swim. Penguins are birds. Therefore, all penguins can swim."
    - "All cats are animals. Whiskers is a cat. Therefore, Whiskers is an animal."
    - "If it rains, the ground is wet. The ground is wet. Therefore, it rained."
    - "Most students passed. Jamie is a student. Therefore, Jamie passed."
  answer: 1
  explanation: "Option B follows the structure: All A are B; X is A; therefore X is B. This is valid — if both premises are true, the conclusion must be true. Option A jumps from 'some' to 'all.' Option C affirms the consequent (the ground could be wet from a sprinkler). Option D uses 'most,' which does not guarantee the conclusion for any specific individual."

- question: "A valid argument with false premises always produces a false conclusion."
  type: true-false
  answer: false
  explanation: "Validity guarantees that IF the premises are true, the conclusion is true. But when the premises are false, the conclusion can be either true or false — validity makes no promise either way. 'All prime numbers are even. 4 is prime. Therefore 4 is even.' Both premises are false, but the conclusion happens to be true. The argument is valid (the structure is correct) but not sound."

- question: "Explain the difference between validity and soundness, and give an example of a valid but unsound argument."
  type: short-answer
  answer: "A valid argument has a structure where the conclusion must follow from the premises. A sound argument is valid AND has all true premises. Example: 'All reptiles can fly. Snakes are reptiles. Therefore snakes can fly.' The structure is valid (All A are B; X is A; so X is B), but the first premise is false, making the argument unsound."
  explanation: "Soundness is the higher standard — it requires both correct logical structure (validity) and factual accuracy of premises. You can verify validity by checking the argument's form alone, but soundness requires also checking whether the premises are true in the real world."
```

## Explainer

You learned that an argument has premises and a conclusion. Now the key question: does the conclusion actually follow from the premises? If it does — if there is no possible way for all the premises to be true while the conclusion is false — the argument is valid. If the conclusion could be false even with true premises, the argument is invalid.

Think of it like a locked door. In a valid argument, true premises are the key that absolutely guarantees entry to the conclusion. In an invalid argument, the premises might happen to lead to the conclusion, but the lock is broken — sometimes the door opens, sometimes it does not. The question "is this valid?" asks whether the connection between premises and conclusion is airtight, not whether the premises themselves are true.

This distinction trips up almost everyone at first. Consider: "All fish can fly. Salmon are fish. Therefore salmon can fly." The premises are absurd, and the conclusion is false. But the argument is valid. Why? Because IF all fish could fly, and IF salmon were fish (which they are), then salmon would indeed fly. The structure is perfect; only the facts are wrong. Conversely, "Birds have feathers. Eagles are birds. Therefore eagles live in North America" has true premises and a true conclusion, but the argument is invalid — the conclusion does not follow from the premises (nothing about feathers tells you where eagles live).

Logicians created the word "sound" to capture the full package. A sound argument is one that is both valid (the conclusion follows from the premises) and has true premises. Sound arguments are the gold standard: they guarantee a true conclusion. Valid-but-unsound arguments have correct structure but bad inputs. Invalid arguments have structural flaws that no amount of true premises can fix. When you evaluate reasoning — in math, science, or daily life — you are always asking these two questions: is the structure valid, and are the premises true?

The fastest way to show an argument is invalid is to find a counterexample: a scenario where the premises are all true but the conclusion is false. If you can construct even one such scenario, the argument fails. You will study counterexamples in depth next, but the intuition starts here: validity means there are zero counterexamples, and invalidity means at least one exists.
