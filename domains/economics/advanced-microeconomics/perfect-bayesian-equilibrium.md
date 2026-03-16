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

## Explainer

From Bayesian games, you know how to model strategic situations where players have private information (types) and form beliefs about each other using probability distributions. From subgame perfect equilibrium, you know that credible strategies must be optimal at every decision point, not just at the start of the game — this eliminates Nash equilibria sustained by non-credible threats. **Perfect Bayesian equilibrium (PBE)** combines both ideas: it requires that players' strategies are sequentially rational given their beliefs, and that beliefs are updated using Bayes' rule wherever possible.

The need for PBE arises in games with **incomplete information and sequential moves**. Consider a signaling game: a job applicant (the sender) has private information about their ability (high or low) and chooses whether to get an MBA. An employer (the receiver) observes the education choice but not the ability, and decides whether to offer a high or low salary. Subgame perfection alone cannot handle this because the employer's decision node is not a proper subgame — it is inside an information set where the employer is uncertain about the applicant's type. We need a concept that specifies both what players *do* and what they *believe* at these information sets.

A PBE consists of two components: a **strategy profile** (what each player does at each information set) and a **belief system** (probability distributions over nodes within each information set). Two requirements bind them together. First, **sequential rationality**: at every information set, the player's strategy must maximize expected payoff given their beliefs about where they are in the game and given other players' strategies going forward. Second, **belief consistency**: at information sets reached with positive probability on the equilibrium path, beliefs must follow from Bayes' rule — if the employer sees an MBA, they must update their beliefs about the applicant's type using the prior probability of each type and the probability that each type gets an MBA according to the equilibrium strategies.

The power of PBE is in what it *rules out*. Consider a Bayesian Nash equilibrium where the employer believes, off the equilibrium path, that anyone who gets an MBA is low-ability — and this pessimistic belief supports the equilibrium because it deters education. If no one gets an MBA in equilibrium, Bayes' rule provides no guidance for beliefs at that information set (it is reached with probability zero). PBE requires sequential rationality even here, which constrains behavior, but it does not fully pin down off-path beliefs. This is both a strength and a limitation — PBE eliminates the most egregious equilibria (those involving non-credible threats) while leaving some off-path flexibility. Further refinements like the Intuitive Criterion or D1 impose additional structure on off-path beliefs to select among remaining PBEs.

PBE is the workhorse equilibrium concept for dynamic games with private information. It structures the analysis of signaling games (education, warranties, advertising), screening problems (insurance menus, price discrimination), bargaining with incomplete information, and reputation models. When you encounter **pooling equilibria** (all types take the same action) and **separating equilibria** (different types take different actions), you are analyzing the PBE of a signaling game. In each case, the discipline is the same: specify strategies, specify beliefs, verify that strategies are rational given beliefs, and verify that beliefs follow Bayes' rule on the equilibrium path.
