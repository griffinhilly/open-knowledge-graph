---
id: nash-equilibrium-simultaneous-move-games
title: Nash Equilibrium in Simultaneous-Move Games
domain: economics
course: microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
builds-toward:
- cournot-quantity-competition-model
- prisoner-dilemma-cooperation-failure
tags:
- nash-equilibrium
- simultaneous-move
- game-theory
- equilibrium
stage: formal-systems
status: draft
---

# Nash Equilibrium in Simultaneous-Move Games

## Core Idea
A Nash equilibrium in a simultaneous-move game is a strategy profile where no player can improve their payoff by unilaterally changing their strategy, given the strategies of other players. In simultaneous-move games, players choose strategies at the same time without knowledge of others' choices. Nash equilibria can be found by identifying best-response functions and locating their intersection. Some games have unique Nash equilibria, others have multiple, and some have none (in pure strategies).

## Explainer

From your game theory prerequisites, you know that a game specifies players, their available strategies, and the payoffs each receives as a function of everyone's choices. In a **simultaneous-move game**, no player observes another's action before choosing — they all move at once, like choosing Rock, Paper, or Scissors on a count of three. This simultaneity makes the problem genuinely strategic: you must reason about what others will do while they reason about what you will do.

A **Nash equilibrium** is the resolution to this mutual-reasoning problem. It is a combination of strategies — one per player — such that each player's choice is the best they can do given what the other players are doing. More precisely: if you told every player exactly what the others planned to do, no one would want to deviate. This mutual best-response property is what makes Nash equilibrium a stable prediction. It's not that players necessarily cooperate or communicate — it's that each is already playing optimally against the others' strategies, so there is no individual incentive to change.

The practical method for finding Nash equilibria in small games is to search for **best responses**. For each strategy of your opponent, ask: "What is my best reply?" Mark it. Then do the same for your opponent given your strategies. A Nash equilibrium is any cell where both players are simultaneously best-responding to each other — where both markings coincide. In a 2×2 payoff matrix, this amounts to checking four cells; in larger games, you list best-response functions and find where they intersect.

Not all games have a unique Nash equilibrium. Some have multiple — the classic coordination game "which side of the road do we drive on?" has two Nash equilibria (both left, or both right) and neither is inherently superior. Some games have no Nash equilibrium in **pure strategies** (where each player picks one strategy with certainty), though Nash's theorem guarantees that every finite game has at least one equilibrium in **mixed strategies** (where players randomize). Understanding Nash equilibrium is the foundation for nearly everything that follows in game theory: Cournot competition, the prisoner's dilemma, and bargaining models all turn on identifying where best-response functions meet.
