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

## Explainer

From your work on game theory basics, you know that strategic situations involve players whose outcomes depend on each other's choices. The **strategic form** (also called normal form) is the most compact way to write down a game: list every player, list every strategy available to each player, and assign a payoff to every possible combination of strategies. For a two-player game, this produces the familiar payoff matrix — rows for Player 1's strategies, columns for Player 2's, and a pair of numbers in each cell representing what each player receives. But strategic form is not limited to two players or finite strategies; it generalizes to any number of players with potentially continuous strategy spaces, like firms choosing prices on a real number line.

The power of this representation is that it makes **Nash equilibrium** visually and analytically tractable. A Nash equilibrium is a combination of strategies — one per player — where no single player can improve their payoff by switching to a different strategy while everyone else holds fixed. Think of it as a state of mutual best response: each player is already doing the best they can given what everyone else is doing. In the Prisoner's Dilemma, both players confessing is a Nash equilibrium because neither gains by unilaterally switching to silence, even though both would prefer mutual silence. The equilibrium concept captures strategic stability, not optimality.

To find Nash equilibria systematically, you construct each player's **best-response function** (or correspondence): for every possible strategy profile of the other players, what is this player's optimal reply? In a two-player matrix game, you can underline the best payoff in each column for the row player and the best payoff in each row for the column player — cells where both payoffs are underlined are Nash equilibria. For continuous games, best-response functions are curves or sets, and equilibria occur at their intersections. This geometric view connects game theory to fixed-point mathematics.

Nash's existence theorem guarantees that every finite game has at least one Nash equilibrium, possibly in **mixed strategies** — probability distributions over pure strategies rather than deterministic choices. This is a profound result: no matter how complex the strategic interaction, as long as there are finitely many players and strategies, equilibrium exists. The theorem relies on fixed-point theorems (Kakutani's, generalizing Brouwer's) and requires only that payoff functions are continuous and strategy sets are compact and convex. When you cannot find a pure-strategy equilibrium in a game, the existence theorem tells you to look for mixed-strategy equilibria — players randomizing in a way that makes their opponents indifferent, which you will formalize next.
