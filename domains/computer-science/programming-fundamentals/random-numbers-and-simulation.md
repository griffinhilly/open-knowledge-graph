---
id: random-numbers-and-simulation
title: Random Numbers and Simulation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loops
  type: hard
- id: numeric-types
  type: hard
- id: conditional-statements
  type: hard
- id: simple-probability
  type: soft
builds-toward: []
tags:
- random
- pseudorandom
- simulation
- monte-carlo
- modeling
- AP-CSP
stage: formal-systems
status: validated
---
# Random Numbers and Simulation

## Core Idea
Programs get random-looking values from a pseudorandom number generator, a deterministic algorithm whose output passes many statistical tests for randomness. Library calls such as Python's `random.randint(1, 6)` or Java's `Math.random()` let a program roll dice, shuffle cards or pick random points. A simulation uses such values to imitate a real process many times, so the program can estimate outcomes that are hard to compute directly or too slow, costly or dangerous to test in the real world.

## How It's Best Learned
Begin with a dice-rolling program and tally the results of 60 rolls, then 60,000, to see the proportions settle near 1/6. Ask students to predict, then measure, the effect of a simplifying assumption, such as treating every customer as arriving at an even rate. Show that setting a seed makes a "random" run repeat exactly, which links the idea of pseudorandomness to debugging.

## Common Misconceptions
- Computer random numbers are truly random. (Standard library generators are pseudorandom: the same seed always produces the same sequence.)
- A simulation's answer is exact once the code is correct. (A simulation gives an estimate that varies from run to run and depends on the model's simplifying assumptions.)
- `random.randint(1, 6)` in Python can never return 6. (Python's `randint(a, b)` includes both endpoints; it is `range` and `random.random()` that exclude the upper end.)
- After several heads in a row, a simulated coin is "due" for tails. (Each call is designed to be independent of earlier results, so the chance stays the same.)

## Questions

```yaml
- question: "In Java, Math.random() returns a double d with 0.0 <= d < 1.0. Which expression produces a random integer from 1 to 6, each value equally likely?"
  type: multiple-choice
  options:
    - "(int) (Math.random() * 6)"
    - "(int) (Math.random() * 6) + 1"
    - "(int) (Math.random() * 7)"
    - "(int) Math.random() * 6 + 1"
  answer: 1
  explanation: "Math.random() * 6 lies in [0, 6), and casting to int gives 0 through 5. Adding 1 shifts the range to 1 through 6. Option A gives 0 to 5. Option C gives 0 to 6. Option D casts Math.random() to int first, which is always 0, so it always gives 1."

- question: "A program calls random.seed(42) and then prints five calls to random.randint(1, 100). It is run twice on the same Python version. What happens?"
  type: multiple-choice
  options:
    - "The two runs print different numbers, because the values are random"
    - "The two runs print the same five numbers"
    - "The second run raises an error, because a seed can be used only once"
    - "Both runs print 42 five times"
  answer: 1
  explanation: "A pseudorandom generator is deterministic. The same seed starts it in the same internal state, so it produces the same sequence. Programmers use this to make bugs in simulations repeatable."

- question: "Running a simulation with more trials always produces the exact true probability."
  type: true-false
  answer: false
  explanation: "More trials usually bring the estimate closer to the true value, as the law of large numbers predicts, but any finite run still has random error. A simulation also inherits any error built into its model's assumptions."

- question: "A city simulates traffic at a new intersection instead of building it and watching. Give one advantage of the simulation and one limitation."
  type: short-answer
  answer: "Advantage: it can test many designs quickly, cheaply and safely, including rare or dangerous situations. Limitation: it simplifies reality (for example, it assumes drivers behave in fixed ways), so its results can be wrong or biased if those assumptions do not match real behavior."
  explanation: "Simulations trade realism for speed and safety. Their value depends on how well the model's assumptions match the real system, which is why results are checked against real data when possible."
```

## Explainer

Many programs need values that cannot be predicted in advance: a game rolls dice, a quiz shuffles questions, a model guesses where a storm might go. Every major language provides a generator for this. In Python, `import random` gives `random.randint(1, 6)`, which returns an integer from 1 to 6 inclusive, and `random.random()`, which returns a float from 0.0 up to but not including 1.0. In Java, `Math.random()` returns a `double` in the same half-open range, so `(int) (Math.random() * 6) + 1` simulates a die.

These values are **pseudorandom**. The generator is an ordinary algorithm that turns an internal state into the next number and updates the state. Its output looks random and passes many statistical tests, but it is fully determined by its starting state, called the **seed**. Calling `random.seed(42)` before a run makes the program produce the same sequence every time. That is useful for testing. It also means these generators should not be used for passwords or encryption keys; security code uses special cryptographic generators instead.

A **simulation** uses random values to imitate a process. To estimate the chance that two dice sum to 7, roll two simulated dice 100,000 times and count. The fraction will be close to 1/6, about 0.167. A classic example estimates pi: pick random points in a 1-by-1 square and count how many land inside the quarter circle of radius 1. That fraction approaches pi/4. Methods like this are called **Monte Carlo** methods.

Two facts govern every simulation. First, the answer is an **estimate**. Different runs give slightly different results, and more trials usually shrink the spread. Second, a simulation is only as good as its **model**. A traffic simulation must assume how fast cars arrive and how drivers react. Those simplifications make the program possible, but if they are wrong, the output is wrong too, however many trials you run.

Simulations are still widely used because they let people explore situations that are expensive, slow or unsafe to test directly, such as crowd evacuations, disease spread or new road layouts. The skill is to state the assumptions openly, run enough trials, and compare results against real data whenever possible.
