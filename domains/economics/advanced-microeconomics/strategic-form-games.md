---
id: strategic-form-games
title: Strategic Form Games and Nash Equilibrium
domain: economics
course: advanced-microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- mixed-strategy-equilibrium
- nash-refinements-and-trembling-hand
tags:
- game-theory
- strategic-interaction
stage: advanced
status: draft
---

# Strategic Form Games and Nash Equilibrium

## Core Idea
Strategic form specifies players, each player's strategy set, and payoff functions. A Nash equilibrium is a strategy profile where no player wants to unilaterally deviate. Nash's existence theorem guarantees that mixed-strategy equilibria exist under mild continuity conditions, even if pure-strategy equilibria don't. Best-response functions visualize equilibrium as the intersection of best-response correspondences.

## Questions

```yaml
- question: "In the Prisoner's Dilemma, both players confessing is a Nash equilibrium even though both players would receive higher payoffs if they both stayed silent. Why does mutual confession qualify as a Nash equilibrium?"
  type: multiple-choice
  options:
    - "Both players prefer confessing because they anticipate the other will confess, making it a self-fulfilling prophecy"
    - "Neither player can improve their individual payoff by unilaterally switching to silence, given that the other player is confessing"
    - "The Nash equilibrium always selects the strategy that maximizes the sum of all players' payoffs"
    - "Both players are playing dominant strategies, and dominant strategies always produce Nash equilibria"
  answer: 1
  explanation: "A Nash equilibrium requires only that no single player can profitably deviate given the others' strategies — not that the outcome is collectively optimal. If Player 1 is confessing, Player 2's best response is also to confess (silence would give the worst payoff). And if Player 2 is confessing, Player 1's best response is to confess. So neither player wants to deviate unilaterally — mutual confession is stable. Option A hints at a reasoning process, not the formal definition. Option C is wrong — Nash equilibria can be collectively suboptimal (PD is the canonical example). Option D is correct that confessing is a dominant strategy, and dominant strategies are always Nash equilibria — but the reasoning in B is the direct definition."

- question: "A game has three pure strategies for each of two players and no cell in the payoff matrix has both payoffs underlined (i.e., no pure-strategy Nash equilibrium exists). What does Nash's existence theorem guarantee?"
  type: multiple-choice
  options:
    - "The game has no equilibrium and players should use maximin strategies"
    - "The theorem does not apply because not all finite games have equilibria"
    - "The game must have at least one Nash equilibrium in mixed strategies"
    - "Players must coordinate on a correlated equilibrium instead"
  answer: 2
  explanation: "Nash's existence theorem guarantees that every finite game — any game with a finite number of players and finite strategy sets — has at least one Nash equilibrium, possibly in mixed strategies. When no pure-strategy equilibrium exists, the theorem guarantees a mixed-strategy equilibrium exists: probability distributions over pure strategies such that each player is indifferent among the strategies they mix over (and therefore willing to randomize). The theorem rests on Kakutani's fixed-point theorem applied to the best-response correspondence."

- question: "A Nash equilibrium is a strategy profile in which every player is playing a best response to the strategies of all other players."
  type: true-false
  answer: true
  explanation: "This is the precise definition of Nash equilibrium: mutual best response. If every player is already responding optimally to what everyone else is doing, no single player has an incentive to unilaterally change their strategy — the profile is stable. The best-response interpretation also suggests the systematic way to find Nash equilibria: for each player, underline their best payoff given each strategy of the opponent; cells where all players have their best payoffs underlined are Nash equilibria."

- question: "A Nash equilibrium always produces the outcome that maximizes the total combined payoffs for all players in the game."
  type: true-false
  answer: false
  explanation: "The Prisoner's Dilemma is the classic counterexample. Both players confessing is the unique Nash equilibrium, but mutual silence gives each player a higher payoff — total surplus is maximized at mutual silence, not at the equilibrium. Nash equilibrium is about strategic stability (no individual incentive to deviate), not social optimality. This gap between individual rationality and collective welfare is one of the central lessons of game theory and underlies problems ranging from arms races to climate agreements."

- question: "Why is a Nash equilibrium described as 'stable' rather than 'optimal,' and what classic game illustrates the difference most clearly?"
  type: short-answer
  answer: "A Nash equilibrium is stable in the sense that no player has a unilateral incentive to deviate — each is already doing the best they can given others' choices. But stability has nothing to do with producing the best collective outcome. The Prisoner's Dilemma illustrates this: the unique Nash equilibrium (both confess) is worse for both players than the alternative (both cooperate/stay silent), which is not an equilibrium because each player individually wants to deviate from it. The equilibrium is 'trapped' at a suboptimal outcome because individual incentives undermine the collectively better choice."
  explanation: "This distinction — between individual strategic rationality and collective optimality — is foundational to applied game theory, mechanism design, and policy analysis. It explains why markets can fail (equilibria exist but are inefficient), why arms races persist (mutual disarmament is not a Nash equilibrium), and why achieving cooperation often requires changing the payoff structure (e.g., through contracts, regulations, or repeated interaction) rather than appealing to rationality alone."
```

## Explainer

From your work on game theory basics, you know that strategic situations involve players whose outcomes depend on each other's choices. The **strategic form** (also called normal form) is the most compact way to write down a game: list every player, list every strategy available to each player, and assign a payoff to every possible combination of strategies. For a two-player game, this produces the familiar payoff matrix — rows for Player 1's strategies, columns for Player 2's, and a pair of numbers in each cell representing what each player receives. But strategic form is not limited to two players or finite strategies; it generalizes to any number of players with potentially continuous strategy spaces, like firms choosing prices on a real number line.

The power of this representation is that it makes **Nash equilibrium** visually and analytically tractable. A Nash equilibrium is a combination of strategies — one per player — where no single player can improve their payoff by switching to a different strategy while everyone else holds fixed. Think of it as a state of mutual best response: each player is already doing the best they can given what everyone else is doing. In the Prisoner's Dilemma, both players confessing is a Nash equilibrium because neither gains by unilaterally switching to silence, even though both would prefer mutual silence. The equilibrium concept captures strategic stability, not optimality.

To find Nash equilibria systematically, you construct each player's **best-response function** (or correspondence): for every possible strategy profile of the other players, what is this player's optimal reply? In a two-player matrix game, you can underline the best payoff in each column for the row player and the best payoff in each row for the column player — cells where both payoffs are underlined are Nash equilibria. For continuous games, best-response functions are curves or sets, and equilibria occur at their intersections. This geometric view connects game theory to fixed-point mathematics.

Nash's existence theorem guarantees that every finite game has at least one Nash equilibrium, possibly in **mixed strategies** — probability distributions over pure strategies rather than deterministic choices. This is a profound result: no matter how complex the strategic interaction, as long as there are finitely many players and strategies, equilibrium exists. The theorem relies on fixed-point theorems (Kakutani's, generalizing Brouwer's) and requires only that payoff functions are continuous and strategy sets are compact and convex. When you cannot find a pure-strategy equilibrium in a game, the existence theorem tells you to look for mixed-strategy equilibria — players randomizing in a way that makes their opponents indifferent, which you will formalize next.
