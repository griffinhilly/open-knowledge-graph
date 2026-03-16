---
id: strategic-form-game-theory
title: Strategic Form Games and Normal Form
domain: economics
course: advanced-microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- extensive-form-games
- mixed-strategies-probability
tags:
- game-theory
- strategic-interaction
stage: advanced
status: draft
---

# Strategic Form Games and Normal Form

## Core Idea
Strategic form (normal form) games specify players, strategy sets for each player, and payoff functions for every strategy profile. Each player chooses simultaneously or independently without knowledge of others' choices. Nash equilibrium is the primary solution concept: no player can improve payoff by unilateral strategy change given others' choices.

## Explainer

A **strategic form game** (also called **normal form**) is the most compact way to represent a strategic interaction. You already know from game theory basics that games involve players making choices that affect each other's outcomes, and from Nash equilibrium that a stable outcome is one where no player wants to deviate alone. The strategic form takes these ideas and organizes them into a precise structure: a list of players, the complete set of strategies available to each player, and a payoff function that assigns a numerical outcome to every possible combination of strategies.

The classic representation is a **payoff matrix**. Consider two firms deciding whether to set high or low prices. Each firm has two strategies, so the matrix is 2×2. Each cell contains a pair of payoffs — one for each firm — corresponding to that combination of choices. The key modeling assumption is **simultaneity**: players choose without observing what others do. This does not literally require choices at the same instant — it means each player must decide without knowing the other's decision, as if moves were simultaneous. This is what distinguishes strategic form games from extensive form games, where players move in sequence and can observe earlier actions.

Finding Nash equilibria in a strategic form game follows a systematic procedure. For each cell in the matrix, ask: given what the other player chose, could this player do better by switching? If neither player can improve by switching, that cell is a **Nash equilibrium**. In the classic Prisoner's Dilemma, both players defecting is the unique Nash equilibrium — not because it is the best joint outcome, but because neither player can unilaterally improve by cooperating when the other defects. Some games have multiple Nash equilibria (like the Battle of the Sexes), which raises coordination problems. Others have no pure-strategy equilibrium at all, requiring the mixed strategies you will encounter next.

The power of strategic form representation is its generality. Any finite simultaneous-move game — pricing competition, political campaigning, auction bidding, arms races — can be written as a payoff matrix and analyzed with the same equilibrium tools. The limitation is that it becomes unwieldy as the number of players or strategies grows, and it cannot represent sequential structure or information revelation. That is where extensive form games pick up. But for analyzing the core logic of strategic interdependence — "what should I do given what I think you will do?" — the strategic form is the essential starting framework.
