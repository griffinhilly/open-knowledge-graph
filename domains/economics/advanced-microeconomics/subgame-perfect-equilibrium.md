---
id: subgame-perfect-equilibrium
title: Subgame Perfect Equilibrium
domain: economics
course: advanced-microeconomics
prerequisites:
- id: extensive-form-games
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- perfect-bayesian-equilibrium
tags:
- game-theory
- sequential-games
- equilibrium-refinement
stage: advanced
status: draft
---

# Subgame Perfect Equilibrium

## Core Idea
Subgame perfect equilibrium requires that strategies form a Nash equilibrium in every subgame, not just the entire game. This eliminates incredible threats: actions that would not actually be chosen if reached. Backward induction finds subgame perfect equilibrium by solving from terminal nodes backward, ensuring strategic consistency throughout the game tree.

## Questions

```yaml
- question: "An incumbent firm publicly announces: 'If any competitor enters our market, we will immediately start a price war that is costly for everyone, including us.' This threat deters entry and constitutes a Nash equilibrium. Why does subgame perfect equilibrium reject this outcome?"
  type: multiple-choice
  options:
    - "The threat was announced publicly, making it legally binding and therefore not a game-theoretic construct"
    - "Nash equilibrium cannot apply to sequential games with more than two players"
    - "If entry actually occurred, the incumbent's optimal action would be accommodation — making the threat incredible and irrational to carry out"
    - "The entrant should simply call the bluff regardless of the threat, so no Nash equilibrium exists"
  answer: 2
  explanation: "SPE requires rational play at every decision node, including nodes never reached in equilibrium. Even though the price war threat deters entry (so the node where the incumbent must choose is never reached), SPE asks: if that node WERE reached, would the incumbent actually fight? Since fighting is mutually costly and accommodation is better for the incumbent once entry has occurred, the threat is incredible — the incumbent wouldn't carry it out. Nash equilibrium allows incredible off-path threats because those nodes are never tested; SPE eliminates them by demanding rationality everywhere in the game tree."

- question: "In a two-stage sequential bargaining game, backward induction is used to find the subgame perfect equilibrium. What does backward induction specifically require?"
  type: multiple-choice
  options:
    - "Solving from the first decision node forward, determining each player's best response in sequence"
    - "Identifying all Nash equilibria first, then eliminating those involving irrational off-path play"
    - "Starting at the final decision nodes and working backward so each earlier choice correctly anticipates what happens downstream"
    - "Assuming both players move simultaneously at each stage and solving the resulting normal-form game"
  answer: 2
  explanation: "Backward induction starts at the LAST decision nodes of the game tree, determines what players would rationally do there, then folds those choices back into the analysis of earlier nodes. This ensures that each player's strategy at every stage is a best response to what would actually happen later — the defining property of SPE. Forward reasoning (option A) cannot guarantee this because you don't yet know downstream outcomes when analyzing early nodes. The technique works by eliminating the last strategic uncertainty first, then propagating backward."

- question: "A Nash equilibrium in a sequential extensive-form game guarantees that every player's strategy is rational at every decision node, including nodes that are not reached during play."
  type: true-false
  answer: false
  explanation: "False — this is precisely the gap that SPE is designed to fill. Nash equilibrium only requires that the overall strategy profile is a mutual best response given the entire game. It says nothing about rationality at off-path nodes (nodes that are never reached in equilibrium play). An incredible threat at an off-path node can sustain a Nash equilibrium because that node is never tested. SPE adds the requirement that behavior within every subgame — including off-path ones — must also constitute a Nash equilibrium. This is why SPE is called a refinement of Nash equilibrium."

- question: "Backward induction can always find a subgame perfect equilibrium for any extensive-form game, regardless of what information players have about prior moves."
  type: true-false
  answer: false
  explanation: "False. Backward induction works cleanly for games of perfect information — where every player observes all prior moves and every decision node is in a singleton information set, making every subtree a well-defined subgame. When players have imperfect information (they don't know exactly where they are in the game tree), many off-path nodes cannot start a properly defined subgame, and backward induction breaks down. SPE alone becomes insufficient; stronger refinements like Perfect Bayesian Equilibrium are needed to handle beliefs at information sets and off-path rationality in imperfect-information games."

- question: "What is an 'incredible threat,' and why does subgame perfect equilibrium eliminate it while Nash equilibrium does not?"
  type: short-answer
  answer: "An incredible threat is a promised action that a player would not rationally execute if the relevant situation actually arose — typically because carrying out the threat would harm the player making it more than the alternative. Nash equilibrium can sustain incredible threats because Nash only requires that strategies are mutual best responses given the full game; if the threat succeeds in deterring the relevant action, the threat node is never reached and its irrationality is never exposed. SPE eliminates incredible threats by requiring Nash equilibrium play within every subgame, including those at off-path nodes — the threatening player's strategy must be optimal at the threat node itself, not just credible as a deterrent."
  explanation: "The entry deterrence game is the canonical example: an incumbent threatens a costly price war to deter entry. This Nash equilibrium logic holds as long as the threat is believed: given the threat, no one enters, so the threat is never called upon. But SPE asks: what would the incumbent do if entry occurred? The optimal response is accommodation, not war. Since the incumbent would not actually fight, the threat cannot rationally deter a forward-looking entrant. SPE forces the analysis to reflect what players would actually do at every stage — not just what they might threaten. This makes SPE essential for analyzing bargaining, market entry, and any sequential interaction where the credibility of commitments is the central strategic question."
```

## Explainer

You already know that a Nash equilibrium is a set of strategies where no player can improve their payoff by unilaterally deviating. And from extensive-form games, you know how to represent sequential decisions as a game tree with nodes, branches, and payoffs at terminal nodes. The problem is that Nash equilibrium alone can sustain outcomes in sequential games that rely on threats no rational player would actually carry out. **Subgame perfect equilibrium** (SPE) is the refinement that eliminates these hollow threats by demanding rational play at every point in the game, not just at the start.

Consider a classic entry-deterrence game. An entrant decides whether to enter a market, and then an incumbent decides whether to fight (price war) or accommodate. Fighting is costly for both players. One Nash equilibrium has the incumbent threatening to fight if entry occurs, which deters the entrant. But this threat is **incredible** — if the entrant actually entered, the incumbent would prefer accommodating to a mutually destructive price war. The threat only works if the entrant believes the incumbent would irrationally hurt itself. Subgame perfect equilibrium rejects this: it requires that the incumbent's strategy be optimal even at the node where entry has already occurred.

The technique for finding SPE is **backward induction**. You start at the terminal nodes of the game tree and work backward. At each decision node, you determine what the player at that node would rationally choose, given what happens downstream. Then you fold that choice back into the analysis of earlier nodes. In the entry game, you first solve the incumbent's problem: fight or accommodate? Accommodation is better, so that is the incumbent's choice at that subgame. Knowing this, the entrant at the first node anticipates accommodation and enters. The subgame perfect equilibrium is (Enter, Accommodate) — the only outcome consistent with rational play at every stage.

A **subgame** is any portion of the game tree that starts at a single decision node (where the player knows exactly where they are), includes all subsequent nodes, and can stand alone as a complete game. SPE requires Nash equilibrium play within every such subgame. In games of perfect information — where every player observes all prior moves — backward induction always yields at least one subgame perfect equilibrium. This makes SPE especially powerful for analyzing bargaining, sequential market entry, and multi-stage strategic interactions where the credibility of threats and promises is the central question.
