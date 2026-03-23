---
id: coordination-games-equilibrium
title: Coordination Games and Multiple Equilibria
domain: social-sciences
course: international-relations-theory
prerequisites:
- id: multilateralism-coordination-games
  type: hard
- id: optimization-multivariable-basics
  type: hard
- id: fixed-point-iteration
  type: soft
- id: prisoner-dilemma-cooperation
  type: soft
builds-toward:
- signaling-and-resolve
- international-norms-diffusion
tags:
- game-theory
- coordination
- equilibrium
stage: expert
status: validated
---

# Coordination Games and Multiple Equilibria

## Core Idea
Coordination games differ from prisoner's dilemmas: players want to coordinate, but there may be multiple equilibrium outcomes. For example, states want to avoid war but must choose military postures. If one chooses high readiness and the other matches it, both might be at a costly military equilibrium rather than a peaceful one. Communication and trust help states reach better (lower-cost) equilibria.

## How It's Best Learned
Model a driving game: both benefit from driving on the same side of the road, but which side? Without communication or precedent, states may end up at an inferior coordination point.

## Common Misconceptions
In coordination games, states want to cooperate—the problem is not mutual incentive to defect but uncertainty about which equilibrium others will choose.

## Explainer

From your study of the prisoner's dilemma, you learned the defining feature of that game: each player has a dominant strategy to defect, and if both follow it, both end up worse than if both had cooperated. Coordination games pose a structurally different problem. In a coordination game, both players *want* to coordinate — they just don't know how. There is no dominant defection incentive. Instead, there are **multiple Nash equilibria**, and the problem is selecting among them. Understanding this distinction unlocks a large class of international political phenomena that prisoner's dilemma logic cannot explain.

The classic example is the driving game. Everyone benefits from all cars driving on the same side of the road — it doesn't matter which side, just that everyone chooses consistently. Left-side coordination (UK standard) and right-side coordination (US standard) are both Nash equilibria: given that everyone else drives on the right, your best response is also to drive on the right. No player has an incentive to deviate unilaterally once coordination is achieved. But before a standard is established, or when actors with different conventions interact (think of international drivers at borders), the game presents a genuine coordination problem: which equilibrium will emerge?

Your prerequisite work in **multivariable optimization** and **fixed-point iteration** gives you the mathematical intuition here. A Nash equilibrium is a fixed point: a strategy profile where no player can improve their outcome by changing their strategy while others hold theirs fixed. In games with multiple Nash equilibria, the mathematical tools alone cannot select which equilibrium will be reached — additional information is needed. **Thomas Schelling** introduced the concept of **focal points** (or Schelling points) to explain how real actors resolve this indeterminacy: certain equilibria are salient by virtue of convention, history, precedent, or shared cultural knowledge. When two people must meet in New York City without any communication, most Americans historically converged on Grand Central Station at noon — not because it is mathematically privileged, but because it is culturally salient.

In international relations, this logic explains how **international regimes and institutions** gain their power. Once a convention is established — a particular form for treaties, a standard unit of measurement, a maritime navigation rule — deviating from it is costly not because others will punish you (as in the prisoner's dilemma with its enforcement problem) but because coordination around a different standard is difficult to achieve. The stability of the dollar as the global reserve currency, the QWERTY keyboard, and the norm of diplomatic immunity all exhibit coordination game structure: they persist because everyone coordinates on them, and no single actor has incentive to deviate while others maintain the convention.

The deeper insight for international relations theory is that **coordination problems are self-enforcing once solved, but getting to the equilibrium requires trust, communication, and often historical accident**. States do not always end up at the *best* available equilibrium — they may become locked in costly military postures, trade wars with mutually damaging tariffs, or suboptimal technical standards — not because of defection but because of historical path dependence and coordination failure during a critical period when conventions were being established.

## Questions

```yaml
- question: "How does a coordination game differ from a prisoner's dilemma, and why does this distinction matter for explaining international cooperation?"
  type: short-answer
  answer: "In a prisoner's dilemma, each player has a dominant incentive to defect, making cooperation hard to sustain without external enforcement. In a coordination game, players want to coordinate but face multiple equilibria — once coordination is achieved, it is self-enforcing. This matters because it explains why some forms of international cooperation (driving conventions, treaty formats, reserve currencies) are stable without enforcement mechanisms."
  explanation: "The prisoner's dilemma logic dominates IR theory but cannot explain self-enforcing conventions. Coordination game theory fills this gap by explaining why some norms persist without punishment mechanisms and why path dependence matters: whichever equilibrium was established historically tends to persist because deviating unilaterally is costly."

- question: "What is a 'focal point' (Schelling point), and why does it help explain which equilibrium actors select when multiple Nash equilibria exist?"
  type: short-answer
  answer: "A focal point is an equilibrium that stands out as culturally or contextually salient, making it the natural 'landing point' for actors who cannot communicate directly. It is not mathematically privileged but socially privileged — actors converge on it because they expect others to converge on it."
  explanation: "Schelling's insight was that rationality alone cannot select among multiple equilibria — actors need some shared basis for expectation. Focal points are that basis: they emerge from history, convention, salience, or precedent. This is why institutions matter even when they have no enforcement power: they create the shared expectation that anchors coordination."
```
