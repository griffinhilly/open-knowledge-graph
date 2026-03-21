---
id: perfect-bayesian-equilibrium
title: Perfect Bayesian Equilibrium
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games-incomplete-info
  type: hard
- id: subgame-perfect-equilibrium
  type: hard
builds-toward:
- pooling-separating-equilibrium
tags:
- game-theory
- equilibrium-refinement
- beliefs
stage: advanced
status: draft
---

# Perfect Bayesian Equilibrium

## Core Idea
Perfect Bayesian equilibrium refines Bayesian Nash equilibrium by imposing consistency requirements on beliefs at information sets reached with positive probability (via Bayes' rule) and requiring sequential rationality at every information set. It eliminates implausible equilibria sustained by unreasonable beliefs off the equilibrium path.

## Questions

```yaml
- question: "In a signaling game, all worker types choose not to pursue an MBA in equilibrium (a pooling equilibrium). A firm claims this is supported by the belief that any applicant who does get an MBA is low-ability. Is this a valid Perfect Bayesian Equilibrium?"
  type: multiple-choice
  options:
    - "No — Bayes' rule requires the firm to update toward high-ability upon observing an MBA, making this belief inadmissible"
    - "Yes — getting an MBA is an off-path action (probability zero in equilibrium), so Bayes' rule provides no constraint on beliefs there, and pessimistic off-path beliefs can sustain the equilibrium"
    - "No — in a PBE, all information sets must be reached with positive probability, otherwise the equilibrium is undefined"
    - "Yes — but only if the probability of low-ability types matches the unconditional prior distribution of types"
  answer: 1
  explanation: "PBE requires that beliefs follow Bayes' rule at information sets reached with positive probability on the equilibrium path. In a pooling equilibrium where nobody gets an MBA, the information set reached by observing an MBA has probability zero — it is off-path. At off-path information sets, Bayes' rule cannot be applied (it requires dividing by zero), so PBE leaves beliefs there relatively unconstrained. Pessimistic off-path beliefs (any MBA applicant is low-ability) are thus admissible under PBE, even though they might seem implausible. Further refinements like the Intuitive Criterion specifically address this weakness."

- question: "What is the key difference between a Perfect Bayesian Equilibrium and a Bayesian Nash Equilibrium?"
  type: multiple-choice
  options:
    - "PBE requires mixed strategies; BNE only allows pure strategies in games with complete information"
    - "PBE adds sequential rationality at every information set and requires beliefs to be updated via Bayes' rule on the equilibrium path, ruling out non-credible threats in dynamic games"
    - "PBE applies to static games with private information; BNE applies to sequential games where players move one at a time"
    - "PBE requires complete information about payoffs; BNE is the appropriate concept when payoffs are private"
  answer: 1
  explanation: "BNE specifies strategies and prior beliefs but does not require that strategies remain optimal at every sequential decision point — it can sustain equilibria where players make non-credible threats that are never tested. PBE adds two requirements: (1) sequential rationality — strategies must be optimal at every information set, given beliefs — and (2) belief consistency via Bayes' rule on the equilibrium path. These requirements eliminate equilibria sustained by implausible off-path threats. PBE is essentially the combination of subgame perfect equilibrium's sequential rationality idea with Bayesian updating in games of incomplete information."

- question: "In a Perfect Bayesian Equilibrium, Bayes' rule must be applied to update beliefs at every information set, including those that are never reached in equilibrium."
  type: true-false
  answer: false
  explanation: "Bayes' rule can only be applied at information sets reached with positive probability — this is a mathematical requirement, not a design choice. Bayes' rule involves conditioning on an event, and conditioning on a probability-zero event is undefined. PBE therefore only requires Bayes' rule at on-path information sets. At off-path information sets (probability zero in equilibrium), beliefs are required to support sequentially rational play, but PBE leaves the actual belief values relatively unconstrained. This is a genuine limitation of PBE, which is why stronger refinements exist."

- question: "A Perfect Bayesian Equilibrium requires players' strategies to be sequentially rational — optimal given their beliefs — at every information set, including those that occur with probability zero in equilibrium."
  type: true-false
  answer: true
  explanation: "Sequential rationality is a requirement at every information set in a PBE, not just those reached in equilibrium. This is what rules out non-credible threats: even if a player's information set is never reached (because the equilibrium path avoids it), the strategy at that information set must still be optimal given whatever beliefs the player holds there. If it weren't, the equilibrium would be sustained by a threat the player would not actually carry out. Sequential rationality at every information set is the key requirement that PBE inherits from the subgame perfect equilibrium concept."

- question: "Why does defining a Perfect Bayesian Equilibrium require specifying both a strategy profile AND a belief system, rather than just strategies as in a standard Nash equilibrium?"
  type: short-answer
  answer: "In dynamic games with incomplete information, players make decisions at information sets where they are uncertain about which node they are at — they don't know which type the other player is or which prior moves were made. Without an explicit belief system, we cannot evaluate whether a strategy is rational: 'maximize expected payoff' requires knowing the probabilities over the nodes in the information set. A strategy that looks rational under one belief might be irrational under another. The belief system specifies exactly what each player believes at each information set, making the rationality criterion well-defined. Bayes' rule then ensures these beliefs are not arbitrary — they must be coherent with the equilibrium strategies wherever possible."
  explanation: "This is why PBE is technically a solution concept for a pair (strategy profile, belief system), not just for a strategy profile. The two components are jointly required to satisfy sequential rationality and belief consistency."
```

## Explainer

From Bayesian games, you know how to model strategic situations where players have private information (types) and form beliefs about each other using probability distributions. From subgame perfect equilibrium, you know that credible strategies must be optimal at every decision point, not just at the start of the game — this eliminates Nash equilibria sustained by non-credible threats. **Perfect Bayesian equilibrium (PBE)** combines both ideas: it requires that players' strategies are sequentially rational given their beliefs, and that beliefs are updated using Bayes' rule wherever possible.

The need for PBE arises in games with **incomplete information and sequential moves**. Consider a signaling game: a job applicant (the sender) has private information about their ability (high or low) and chooses whether to get an MBA. An employer (the receiver) observes the education choice but not the ability, and decides whether to offer a high or low salary. Subgame perfection alone cannot handle this because the employer's decision node is not a proper subgame — it is inside an information set where the employer is uncertain about the applicant's type. We need a concept that specifies both what players *do* and what they *believe* at these information sets.

A PBE consists of two components: a **strategy profile** (what each player does at each information set) and a **belief system** (probability distributions over nodes within each information set). Two requirements bind them together. First, **sequential rationality**: at every information set, the player's strategy must maximize expected payoff given their beliefs about where they are in the game and given other players' strategies going forward. Second, **belief consistency**: at information sets reached with positive probability on the equilibrium path, beliefs must follow from Bayes' rule — if the employer sees an MBA, they must update their beliefs about the applicant's type using the prior probability of each type and the probability that each type gets an MBA according to the equilibrium strategies.

The power of PBE is in what it *rules out*. Consider a Bayesian Nash equilibrium where the employer believes, off the equilibrium path, that anyone who gets an MBA is low-ability — and this pessimistic belief supports the equilibrium because it deters education. If no one gets an MBA in equilibrium, Bayes' rule provides no guidance for beliefs at that information set (it is reached with probability zero). PBE requires sequential rationality even here, which constrains behavior, but it does not fully pin down off-path beliefs. This is both a strength and a limitation — PBE eliminates the most egregious equilibria (those involving non-credible threats) while leaving some off-path flexibility. Further refinements like the Intuitive Criterion or D1 impose additional structure on off-path beliefs to select among remaining PBEs.

PBE is the workhorse equilibrium concept for dynamic games with private information. It structures the analysis of signaling games (education, warranties, advertising), screening problems (insurance menus, price discrimination), bargaining with incomplete information, and reputation models. When you encounter **pooling equilibria** (all types take the same action) and **separating equilibria** (different types take different actions), you are analyzing the PBE of a signaling game. In each case, the discipline is the same: specify strategies, specify beliefs, verify that strategies are rational given beliefs, and verify that beliefs follow Bayes' rule on the equilibrium path.
