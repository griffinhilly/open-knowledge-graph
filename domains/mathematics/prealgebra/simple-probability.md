---
id: simple-probability
title: Simple Probability
domain: mathematics
course: prealgebra
prerequisites:
- id: ratios
  type: hard
- id: multiplying-fractions
  type: hard
builds-toward:
- compound-probability
- probability-axioms
tags:
- probability
- fractions
- ratios
- statistics
stage: abstract-reasoning
status: validated
---
# Simple Probability

## Core Idea
Probability measures how likely an event is to occur, expressed as a number from 0 (impossible) to 1 (certain). The probability of an event is the number of favorable outcomes divided by the total number of equally likely outcomes: P(event) = favorable / total. For example, the probability of rolling a 3 on a fair six-sided die is 1/6. Probability can be expressed as a fraction, decimal, or percent. This topic introduces students to reasoning under uncertainty, which is essential for statistics, data science, game theory, and everyday decision-making.

## How It's Best Learned
Use physical experiments: dice, coins, spinners, colored marbles in a bag. Have students predict probabilities, then run experiments and compare theoretical to experimental results. Emphasize listing all possible outcomes (sample space) before computing the probability. Practice expressing probabilities in all three forms (fraction, decimal, percent).

## Common Misconceptions
- Thinking probability of 1/6 means the event will happen exactly once in six tries (that is the long-run average, not a guarantee).
- Confusing "unlikely" with "impossible" or "likely" with "certain."
- Not listing all outcomes in the sample space, leading to incorrect counts.

## Questions

```yaml
- question: "A bag contains 4 red, 3 blue, and 3 green marbles. You pick one at random. What is the probability of picking a red marble?"
  type: multiple-choice
  options: ["4/3", "3/10", "4/10", "1/4"]
  answer: 2
  explanation: "There are 4 + 3 + 3 = 10 total equally likely outcomes and 4 favorable ones (the red marbles), so P(red) = 4/10 = 2/5. The option 1/4 is wrong because it ignores the green marbles; 3/10 is the probability for blue, not red."

- question: "If you flip a fair coin 5 times and get heads most time, the probability of getting tails on the 6th flip is greater than 1/2."
  type: true-false
  answer: false
  explanation: "Each coin flip is an independent event — the coin has no memory of past results. The probability of tails on any fair flip is always exactly 1/2, regardless of what came before. The belief that past results influence future independent outcomes is called the gambler's fallacy."

- question: "A fair six-sided die is rolled. What is the sample space, and what is the probability of rolling an even number?"
  type: short-answer
  answer: "Sample space: {1, 2, 3, 4, 5, 6}. P(even) = 3/6 = 1/2."
  explanation: "Listing all possible outcomes first — the sample space — is the essential first step. There are 6 equally likely outcomes. Three of them are even (2, 4, 6), so the probability is 3/6, which simplifies to 1/2. Expressing this as a decimal (0.5) or percent (50%) are equally valid."
```

## Explainer

Probability is the mathematics of uncertainty. It gives you a precise, numerical way to answer the question: "How likely is this to happen?" The answer is always a number between 0 and 1. A probability of 0 means impossible — the event cannot occur. A probability of 1 means certain — the event always occurs. Everything in between represents varying degrees of likelihood.

The formula for simple probability is P(event) = (number of favorable outcomes) / (total number of equally likely outcomes). The critical phrase is "equally likely" — the formula only works cleanly when every outcome in the sample space has the same chance. Rolling a fair die satisfies this: each face (1 through 6) is equally likely, so the sample space is {1, 2, 3, 4, 5, 6} and each outcome has probability 1/6. If the die were weighted, this formula would not apply directly. Always ask: are these outcomes truly equally likely?

The sample space — the complete list of all possible outcomes — is worth constructing explicitly before computing anything. It is easy to miscount outcomes by guessing rather than listing. For a coin flip, the sample space is {H, T}. For two coin flips, it is {HH, HT, TH, TT} — four outcomes, not three, because HT and TH are distinct. Students who list "both same" and "one of each" have collapsed two distinct outcomes into one and will get the wrong probability for "at least one head."

Probability connects directly to ratios, which you studied as a prerequisite. A probability of 4/10 is a ratio of favorable to total, exactly like any other part-to-whole ratio. You can simplify it (2/5), convert it to a decimal (0.4), or express it as a percent (40%) — the three forms are interchangeable. The ratio framing also makes it clear why probabilities of all outcomes in a sample space must add to 1: the favorable counts for all outcomes together equal the total, so their probabilities sum to total/total = 1.
