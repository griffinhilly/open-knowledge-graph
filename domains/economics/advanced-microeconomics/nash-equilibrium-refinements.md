---
id: nash-equilibrium-refinements
title: Nash Equilibrium Refinements
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
builds-toward:
- subgame-perfect-equilibrium
- perfect-bayesian-equilibrium
tags:
- game-theory
- equilibrium
- solution-concepts
stage: expert
status: draft
---

# Nash Equilibrium Refinements

## Core Idea
A Nash equilibrium refinement is a criterion that eliminates some Nash equilibria as implausible or unreasonable. Common refinements include subgame perfection (no implausible threats), perfect Bayesian equilibrium (consistent beliefs), and trembling-hand perfection (robustness to small errors). Refinements help pin down equilibrium when multiple equilibria exist.

## How It's Best Learned
Start with games that have multiple Nash equilibria. Show why some seem unreasonable. Apply different refinements and see which equilibria survive.

## Questions

```yaml
- question: "In a market entry game, an incumbent threatens to start a price war if a challenger enters — a war that would hurt both firms. This threat sustains an equilibrium where the challenger stays out. Which statement correctly describes this situation?"
  type: multiple-choice
  options:
    - "This is not a Nash equilibrium because the incumbent's threat is not credible"
    - "This is a Nash equilibrium, but it fails subgame perfection because the incumbent would not rationally carry out the threat if entry actually occurred"
    - "This is both a Nash equilibrium and a subgame perfect equilibrium, since no player deviates from their strategy on the equilibrium path"
    - "Subgame perfection does not apply to market entry games — it is only relevant to repeated games"
  answer: 1
  explanation: "Nash equilibrium only requires that no player wants to deviate *given the current strategies*. Because the challenger stays out, the incumbent's threat is never actually tested — so the threat can sustain the equilibrium even if carrying it out would be irrational. This is the key flaw that refinements address. Subgame perfection applies backward induction: it asks whether the incumbent's strategy is a Nash equilibrium in every subgame, including the subgame that starts *after* entry occurs. Since a price war hurts the incumbent, the credible response to entry is accommodation — so the price-war threat fails subgame perfection, and the only subgame perfect equilibrium is for the challenger to enter and the incumbent to accommodate."

- question: "Perfect Bayesian Equilibrium requires that beliefs be updated using Bayes' rule. Why might beliefs still be underdetermined even when all Bayes' rule conditions are met?"
  type: multiple-choice
  options:
    - "Bayes' rule requires prior probabilities that are never well-defined in game-theoretic settings"
    - "Beliefs at information sets that are never reached on the equilibrium path are not constrained by Bayes' rule, leaving them free to be specified arbitrarily"
    - "PBE only pins down beliefs when there are exactly two player types; more types leave the system underdetermined"
    - "Bayes' rule only applies to complete-information games where all types are observable"
  answer: 1
  explanation: "Bayes' rule updates probabilities based on observed events: P(type | signal) ∝ P(signal | type) × P(type). But Bayes' rule only applies when the conditioning event (the signal or action observed) has positive probability under the equilibrium. If an off-equilibrium action is never taken in equilibrium, Bayes' rule places no constraint on what the receiver should believe upon observing it — the conditioning event has probability zero and the formula is undefined. Different off-equilibrium beliefs can support different equilibria, which is why PBE is often further refined by criteria like the Intuitive Criterion that restrict what off-equilibrium beliefs are 'reasonable.'"

- question: "Subgame perfection eliminates Nash equilibria that rely on threats that would be irrational to actually carry out if the moment to act arrived."
  type: true-false
  answer: true
  explanation: "This is precisely the point of subgame perfection. It requires that strategies form a Nash equilibrium in every subgame of the original game — including subgames that are never reached in the equilibrium play. A threat that would hurt the threatening party if executed fails this test: in the subgame that begins when the threat must be carried out, following through is not the optimal action, so the strategy cannot be part of a subgame perfect equilibrium. Backward induction systematically removes such threats by determining optimal play at each final decision node and working backwards."

- question: "Every subgame perfect equilibrium is also a trembling-hand perfect equilibrium."
  type: true-false
  answer: false
  explanation: "Subgame perfection and trembling-hand perfection impose different requirements and neither is a subset of the other in general. Trembling-hand perfection requires that a strategy remain a best response when opponents occasionally make small random errors ('trembles'). This can eliminate equilibria that survive subgame perfection — for example, equilibria where a player is indifferent between two strategies and the equilibrium relies on choosing the one that would be suboptimal under any perturbation. Conversely, trembling-hand perfection is defined for strategic form games and can select equilibria that would be eliminated by subgame perfection in the extensive form. The two refinements capture different kinds of implausibility."

- question: "Why does Nash equilibrium alone permit 'non-credible threats' to sustain equilibria, and how does subgame perfection address this problem?"
  type: short-answer
  answer: "Nash equilibrium only requires that no player wants to deviate given what the other players are currently doing. A threat can sustain an equilibrium even if executing the threat would be irrational — as long as the threat deters the opponent from acting in a way that would trigger it, the threat is never tested. Because Nash equilibrium only checks optimality along the equilibrium path, it cannot rule out strategies that specify irrational behavior off the path. Subgame perfection fixes this by requiring strategies to be a Nash equilibrium in every subgame, including those reached only if a threat is called. This forces each player's strategy to be optimal at every decision node regardless of history, eliminating any strategy that relies on a commitment that rational players would abandon if tested."
  explanation: "The key distinction is on-path vs. off-path optimality. Nash equilibrium only enforces optimality on the path that is actually played; subgame perfection enforces it everywhere. This is why backward induction is the tool for finding subgame perfect equilibria — it starts from the end of the game tree, where there is no future strategy to hide behind, and works backwards, enforcing rationality at every node."
```

## Explainer

From Nash equilibrium, you know that an equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. This is a powerful concept, but in many games it is too permissive — it admits equilibria that rely on threats no rational player would actually carry out, beliefs that make no sense given the structure of the game, or strategies that would collapse if players made even tiny mistakes. **Equilibrium refinements** are additional criteria designed to eliminate these implausible equilibria and sharpen predictions.

The most intuitive refinement is **subgame perfection**, which requires that strategies form a Nash equilibrium in every subgame of the original game — not just the game as a whole. Consider a market entry game: an incumbent threatens to start a price war if a challenger enters. This threat can sustain an equilibrium where the challenger stays out. But if entry actually occurred, would the incumbent really follow through? A price war hurts the incumbent too. Subgame perfection requires that the incumbent's strategy be optimal even after entry happens, eliminating threats that are not credible when actually tested. You find subgame perfect equilibria through **backward induction**: start at the end of the game tree, determine optimal play at each final decision node, then work backwards. Any equilibrium that relies on a player acting against their own interest at some decision point is eliminated.

When games involve **incomplete information** — players are uncertain about others' types or previous actions — subgame perfection alone is insufficient because there may not be well-defined subgames to analyze. **Perfect Bayesian equilibrium** (PBE) addresses this by requiring two things simultaneously: strategies must be sequentially rational (optimal at every information set given beliefs), and beliefs must be consistent with strategies via **Bayes' rule** wherever possible. In a signaling game, for example, PBE pins down not just what the sender does and how the receiver responds, but what the receiver believes about the sender's type after observing each possible signal. Beliefs cannot be arbitrary — they must be updated rationally from prior probabilities and observed actions.

A third important refinement is **trembling-hand perfection**, which tests whether an equilibrium is robust to small mistakes. The idea is that every player has a tiny probability of "trembling" and playing any available strategy by accident. A trembling-hand perfect equilibrium must remain a best response even when opponents occasionally err. This eliminates equilibria that survive only because a player is indifferent between strategies and the equilibrium relies on them choosing a specific one that would be suboptimal if opponents ever deviated. Each refinement captures a different aspect of strategic plausibility — credibility of threats (subgame perfection), consistency of beliefs (PBE), or robustness to errors (trembling hand) — and the choice of which refinement to apply depends on the game's structure and what kind of implausibility you are trying to rule out.
