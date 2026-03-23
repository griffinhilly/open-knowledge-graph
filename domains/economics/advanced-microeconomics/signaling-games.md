---
id: signaling-games
title: Signaling Games
domain: economics
course: advanced-microeconomics
prerequisites:
- id: perfect-bayesian-equilibrium
  type: hard
- id: adverse-selection
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: bayesian-games-strategy
  type: hard
tags:
- contract-theory
- signaling
- information-revelation
stage: expert
status: validated
---

# Signaling Games

## Core Idea
In a signaling game, the informed player (agent) moves first by choosing an action (signal) that reveals or conceals type. The uninformed player (principal) observes the signal and chooses a response. Separating equilibrium: different types send different signals. Pooling equilibrium: all types send the same signal. Example: education as a signal of ability in the job market.

## How It's Best Learned
Analyze Spence's education signaling model. Draw payoff matrices and solve for equilibria. Identify when separating vs. pooling equilibria arise.

## Questions

```yaml
- question: "Suppose the cost of obtaining a college degree is identical for high-ability and low-ability workers. What happens to the separating equilibrium in Spence's signaling model?"
  type: multiple-choice
  options:
    - "The separating equilibrium is stronger — equal costs mean neither type has an incentive to deviate"
    - "The separating equilibrium collapses — low-ability workers would mimic high-ability workers since signaling costs no longer deter them"
    - "A pooling equilibrium becomes impossible — only separating equilibria can survive when costs are equal"
    - "Employers simply offer wages equal to the average ability, and both types attend college"
  answer: 1
  explanation: "The differential cost condition is the foundation of signaling equilibria. If low-ability workers face the same cost as high-ability workers, the signal is no longer differentially costly — low types would always mimic high types to collect the wage premium. The separating equilibrium dissolves into a pooling equilibrium (or no equilibrium at all), because no signal can credibly distinguish the types. Equal costs destroy the information content of the signal."

- question: "In a pooling equilibrium of a signaling game, what information does the receiver gain from observing the signal?"
  type: multiple-choice
  options:
    - "The receiver learns the sender's exact type because the signal uniquely identifies who sends it"
    - "The receiver gains no new information — the signal is sent by all types, so the posterior equals the prior"
    - "The receiver infers only that the sender is not the lowest type, since weak types cannot afford any signal"
    - "The receiver updates beliefs toward high types because signaling is inherently associated with quality"
  answer: 1
  explanation: "In a pooling equilibrium, every type sends the same signal. Bayes' rule updates the receiver's beliefs using observed signal frequencies, but since all types send the same signal with equal frequency, the posterior is identical to the prior — no updating occurs. The signal transmits zero information about the sender's type. This is why pooling equilibria can feel 'uninformative' compared to separating ones, and why refinements like the Intuitive Criterion often favor separating equilibria."

- question: "In a separating equilibrium, the receiver's beliefs after observing each signal are fully pinned down by Bayes' rule, because each signal is sent by exactly one type."
  type: true-false
  answer: true
  explanation: "This is the defining property of separation. If each type sends a distinct signal, observing any on-path signal tells the receiver exactly which type sent it — Bayes' rule assigns probability one to that type. This is why separating equilibria are 'fully revealing': the sender's private information is perfectly communicated through the signal choice, even though the sender may have preferred to conceal it."

- question: "A signal credibly separates types as long as it is costly for the sender to send."
  type: true-false
  answer: false
  explanation: "Cost alone is not sufficient — the key condition is *differential* cost. If the signal is costly but equally costly for all types, low types will still mimic high types whenever the benefit (a higher wage or price) exceeds the cost. The signal only separates types when the cost is lower for high types, so that high types find signaling worthwhile but low types find mimicking prohibitively expensive. A uniformly costly signal is merely a barrier, not a credible separator."

- question: "Why is differential cost — not just cost alone — the essential requirement for a credible separating signal in a signaling game?"
  type: short-answer
  answer: "A separating equilibrium requires that low types choose not to mimic high types. If the signal cost is the same for all types, any low type would rationally mimic the high type to collect the higher payoff — the signal conveys no information and the separation collapses. Differential cost creates a self-enforcing wedge: the high type signals because the payoff justifies the cost, and the low type does not signal because the same cost is prohibitively expensive relative to the expected benefit. The signal's credibility comes entirely from this asymmetry in cost, not from the cost level itself."
  explanation: "This is the mechanism behind all real-world credible signals: warranties (costly for low-quality producers who expect many claims), dividends (costly for firms without real cash flow), and retained equity (costly for entrepreneurs who can't afford to hold illiquid assets). In each case, the signal deters mimicry specifically because it is cheap for the genuine type and expensive for an imitator."
```

## Explainer

From your work on adverse selection, you know that private information can destroy markets: if buyers cannot distinguish high-quality sellers from low-quality ones, good sellers exit and the market unravels. Signaling games ask the next question — what if the informed party can *do something* to credibly reveal their type before the uninformed party acts? The key insight is that not just any action works as a signal. For a signal to separate types, it must be **differentially costly**: expensive enough for low types that they would not want to mimic, but cheap enough for high types that sending it is worthwhile given the reward.

The canonical example is **Spence's job market signaling model**. Suppose workers are either high-ability or low-ability, and employers cannot observe ability directly. Workers can choose to get a college degree before entering the job market. The critical assumption is that education is *less costly* for high-ability workers — not necessarily in tuition, but in effort, time, or opportunity cost. If this differential cost condition holds, a **separating equilibrium** can emerge: high-ability workers get degrees, low-ability workers do not, and employers rationally offer high wages to degree-holders and low wages to non-degree-holders. Crucially, in this pure signaling model, education need not increase productivity at all — it works purely as a sorting device.

The structure of the game follows directly from your knowledge of Bayesian games and perfect Bayesian equilibrium. Nature moves first, assigning a type to the sender (the informed player). The sender observes their type and chooses a signal. The receiver (the uninformed player) observes the signal, updates beliefs using Bayes' rule, and chooses an action. In a **separating equilibrium**, the receiver's beliefs are pinned down by Bayes' rule because each signal is sent by exactly one type. In a **pooling equilibrium**, all types send the same signal, so the receiver's posterior equals the prior — no information is transmitted. Semi-separating equilibria, where some types randomize, also exist.

The hardest part of solving signaling games is handling **off-equilibrium beliefs** — what the receiver believes when observing a signal that no type is supposed to send. Perfect Bayesian equilibrium alone does not restrict these beliefs, which means many pooling equilibria can be sustained by pessimistic off-path beliefs. Refinements like the **Intuitive Criterion** (Cho and Kreps) eliminate implausible equilibria by asking: if only one type could possibly benefit from deviating to the off-path signal, the receiver should assign probability one to that type. This refinement typically selects the most efficient separating equilibrium and rules out pooling equilibria where the high type would want to deviate.

Signaling games appear throughout economics beyond education: firms issue dividends to signal profitability, entrepreneurs retain equity to signal project quality, nations build military capacity to signal resolve, and warranties signal product durability. The unifying logic is always the same — credible communication requires costly action, and the cost must fall differently on different types. Without differential cost, signals are cheap talk and cannot credibly separate.
