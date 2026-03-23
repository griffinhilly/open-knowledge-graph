---
id: conjectures-and-testing
title: Conjectures and Testing
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: deductive-vs-inductive-reasoning
    type: hard
  - id: counterexamples-in-reasoning
    type: hard
  - id: number-sequences-patterns
    type: soft
builds-toward:
  - direct-proof-introduction
  - when-is-something-proven
tags: [conjectures, testing, hypothesis, mathematical-reasoning]
stage: abstract-reasoning
status: draft
---

# Conjectures and Testing

## Core Idea
A conjecture is an educated guess — a statement believed to be true based on observation or reasoning but not yet proven. The process of mathematical discovery follows a cycle: observe patterns, form a conjecture, test it against examples, and then either find a counterexample (which disproves it) or attempt a proof (which confirms it). Testing a conjecture means deliberately trying to break it by checking diverse and extreme cases. A conjecture that survives rigorous testing is worth trying to prove; one that fails gets refined or discarded.

## How It's Best Learned
Give students numerical data and ask them to form conjectures. For example: compute 1+3, 1+3+5, 1+3+5+7 (getting 4, 9, 16) and conjecture a pattern. Then test with more cases. Discuss: "When have you tested enough?" Introduce famous conjectures (Goldbach's, Collatz) to show that even simple-looking conjectures can remain unproven for centuries. Emphasize the testing strategy: try small cases, boundary cases, and "weird" cases before attempting a proof.

## Common Misconceptions
- Thinking a conjecture is just a random guess. A good conjecture is based on evidence and patterns, not pulled from thin air.
- Believing that many confirming examples prove a conjecture. They increase confidence but do not constitute proof.
- Assuming a conjecture must be true or false. Some conjectures are undecidable within standard mathematical systems, though this is an advanced topic.

## Questions

```yaml
- question: "A student computes 1² = 1, 11² = 121, 111² = 12321, and 1111² = 1234321. What conjecture might the student form?"
  type: multiple-choice
  options:
    - "Squaring any number gives a palindrome"
    - "The square of a repunit (number with all 1s) produces a palindrome that counts up and then back down"
    - "All palindromes are perfect squares"
    - "Squaring always produces a number with more digits"
  answer: 1
  explanation: "The pattern shows 1, 121, 12321, 1234321 — each is a palindrome that counts up to the number of digits in the repunit, then counts back down. This is a specific, testable conjecture about repunit squares. Option A is too broad (2² = 4 is not a palindrome). Option C reverses the relationship. Option D is true but not the interesting pattern here."

- question: "Testing 100 cases that all support a conjecture proves the conjecture is true."
  type: true-false
  answer: false
  explanation: "No number of confirming cases constitutes a proof. The conjecture 'n² + n + 41 is prime for all positive integers n' holds for n = 1 through n = 39, which is impressive — but it fails at n = 40 (40² + 40 + 41 = 41² = 1681, which is not prime in the relevant sense) and obviously at n = 41. Testing builds confidence and is essential for discovering counterexamples, but only a deductive proof establishes truth for all cases."

- question: "Describe the conjecture-test-refine cycle using an example of a conjecture that needs refinement."
  type: short-answer
  answer: "Start with the conjecture 'the sum of two prime numbers is always even.' Test: 2 + 3 = 5, which is odd — counterexample found. Refine: 'the sum of two odd prime numbers is always even.' Test: 3 + 5 = 8 (even), 7 + 11 = 18 (even), 13 + 19 = 32 (even). No counterexample found. The refined conjecture is ready for a proof attempt."
  explanation: "The cycle shows how counterexamples drive progress. The original conjecture was too broad — it forgot about 2, the only even prime. The counterexample pointed directly at the problem (one prime was even), which led to the fix (restrict to odd primes). The refined conjecture can then be proven deductively: odd + odd = even."
```

## Explainer

Mathematics does not spring fully formed from axioms. It grows through a messy, creative, very human process: you look at examples, notice a pattern, guess that the pattern always holds, and then try to figure out whether you are right. That guess is a conjecture, and learning to form and test conjectures is how you start thinking like a mathematician.

The process has a natural rhythm. First, you compute examples and look for patterns. Computing 1 + 3 = 4, 1 + 3 + 5 = 9, 1 + 3 + 5 + 7 = 16, you notice the sums are perfect squares: 4, 9, 16. The conjecture writes itself: the sum of the first n odd numbers equals n². But noticing a pattern is only the beginning — you need to test it.

Testing means trying to break your conjecture, not just confirming it. It is tempting to check a few more cases (1+3+5+7+9 = 25 = 5², yes!), declare victory, and move on. Resist that temptation. Instead, ask: does it work for n = 1? (1 = 1², yes.) Does it work for large n? (Sum of first 10 odd numbers = 100 = 10², yes.) Does it work for n = 0? (The empty sum is 0 = 0², yes.) You are stress-testing the conjecture by deliberately choosing cases that might be tricky — small numbers, large numbers, boundary cases.

The reason testing cannot replace proof is the gap between "every case I checked" and "every case that exists." One of the most instructive examples is the polynomial n² + n + 41. Plug in n = 1, 2, 3, ..., 39, and every single result is prime. Forty consecutive prime outputs — surely this always works? But at n = 40, you get 40² + 40 + 41 = 1681 = 41², which is not prime. Forty confirming cases meant nothing against that forty-first failure. This is why mathematicians do not call something a theorem until there is a proof.

When a counterexample does surface, the productive response is refinement, not abandonment. The conjecture "the sum of two primes is always even" fails because of 2 + 3 = 5. But the counterexample reveals exactly what went wrong: the number 2 is the only even prime, and adding it to an odd prime gives an odd sum. The fix is simple — restrict to odd primes — and the refined conjecture ("the sum of two odd primes is even") is provable in one line. Counterexamples are not enemies of conjectures; they are editors that make conjectures sharper.
