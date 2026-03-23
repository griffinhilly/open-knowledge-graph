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
stage: expert
status: draft
---

# Strategic Form Games and Normal Form

## Core Idea
Strategic form (normal form) games specify players, strategy sets for each player, and payoff functions for every strategy profile. Each player chooses simultaneously or independently without knowledge of others' choices. Nash equilibrium is the primary solution concept: no player can improve payoff by unilateral strategy change given others' choices.

## Questions

```yaml
- question: "In the Prisoner's Dilemma, both players defecting is the unique Nash equilibrium, even though both cooperating gives higher payoffs to both players. A student argues: 'Both cooperating must also be a Nash equilibrium because it maximizes total welfare.' Why is the student wrong?"
  type: multiple-choice
  options:
    - "The student is correct — any outcome that maximizes total payoffs is a Nash equilibrium by definition"
    - "Both cooperating is not a Nash equilibrium because if one player cooperates, the other player can unilaterally switch to defecting and do better — so cooperation is always a tempting deviation"
    - "Nash equilibrium requires mutual defection by definition in any Prisoner's Dilemma"
    - "Both cooperating is not a Nash equilibrium because it requires communication, which is excluded from strategic form games"
  answer: 1
  explanation: "Nash equilibrium is defined by unilateral deviations: a strategy profile is a Nash equilibrium if and only if no single player can improve their payoff by changing their own strategy while all others hold theirs fixed. In the Prisoner's Dilemma, if one player cooperates, the other's best response is to defect (getting the highest individual payoff). So 'both cooperate' fails the Nash test — either player wants to deviate. 'Both defect' is Nash because defecting is the best response to defection. The Nash concept has nothing to do with maximizing joint welfare; it captures individual stability."

- question: "Two firms set prices 'simultaneously.' In practice, Firm A announces its price on Monday and Firm B announces on Tuesday, and neither knows the other's choice when deciding. Does the simultaneity assumption of strategic form games apply here?"
  type: multiple-choice
  options:
    - "No — the firms move at different times, so this must be represented as an extensive form game with sequential moves"
    - "Yes — 'simultaneous' in strategic form means each player decides without observing the other's choice, not that choices are made at the same physical instant"
    - "No — strategic form games require perfect information, meaning each player must know all prior moves"
    - "Yes — but only if both firms happen to choose the same price by coincidence"
  answer: 1
  explanation: "The simultaneity assumption in strategic form games is about *information*, not timing. It means each player makes their decision without knowing what the other has chosen — they are strategically 'blind' to each other's move. Whether the actual choices happen on the same day or different days is irrelevant, as long as neither player can observe the other's choice before committing. This is what distinguishes strategic form (simultaneous-move, no observation) from extensive form (sequential, observed moves). Many real strategic interactions — sealed-bid auctions, simultaneous price-setting — are simultaneous in this sense even if the literal timing differs."

- question: "A Nash equilibrium is a strategy profile where no individual player can increase their payoff by changing only their own strategy, given that all other players keep their strategies fixed."
  type: true-false
  answer: true
  explanation: "This is the precise definition of Nash equilibrium. The critical element is 'unilateral deviation': the stability condition checks each player in isolation, holding all others fixed. It does not require that the outcome is socially optimal, that players communicate, or that they act cooperatively. The Prisoner's Dilemma illustrates that Nash equilibria can be collectively suboptimal — both players could do better together, but neither can improve alone without the other's cooperation."

- question: "In any strategic form game with a finite number of players and strategies, there exists exactly one Nash equilibrium in pure strategies."
  type: true-false
  answer: false
  explanation: "This is false in both directions: some games have multiple pure-strategy Nash equilibria (e.g., Battle of the Sexes has two), and some games have no pure-strategy Nash equilibrium (e.g., Matching Pennies). Nash's theorem guarantees that every finite game has at least one Nash equilibrium if mixed strategies (probability distributions over pure strategies) are allowed — but pure-strategy equilibria can be zero, one, or many. Uniqueness is a special property of particular game structures, not a general guarantee."

- question: "Why is the Nash equilibrium in the Prisoner's Dilemma not the outcome that maximizes joint payoffs, and what does this reveal about the Nash equilibrium concept?"
  type: short-answer
  answer: "In the Prisoner's Dilemma, mutual cooperation yields the highest combined payoff, but it is not a Nash equilibrium because each player has an incentive to defect given the other's cooperation — defection dominates cooperation regardless of what the other player does. Both defecting is Nash because defection is the best response to defection. This reveals that Nash equilibrium captures *individual stability* (no incentive for unilateral deviation), not *collective optimality*. An equilibrium can be stable in the Nash sense while being Pareto-dominated — everyone could do better if they could credibly commit to cooperate. This tension between individual rationality and collective welfare is the central insight of the Prisoner's Dilemma and much of game theory."
  explanation: "The gap between Nash equilibria and socially optimal outcomes is not a flaw in the concept but a feature: Nash equilibrium models what self-interested agents will actually do in the absence of binding agreements. Understanding why individually rational behavior can produce collectively poor outcomes motivates the study of mechanism design, contracts, and repeated games — all of which try to align individual incentives with collective welfare."
```

## Explainer

A **strategic form game** (also called **normal form**) is the most compact way to represent a strategic interaction. You already know from game theory basics that games involve players making choices that affect each other's outcomes, and from Nash equilibrium that a stable outcome is one where no player wants to deviate alone. The strategic form takes these ideas and organizes them into a precise structure: a list of players, the complete set of strategies available to each player, and a payoff function that assigns a numerical outcome to every possible combination of strategies.

The classic representation is a **payoff matrix**. Consider two firms deciding whether to set high or low prices. Each firm has two strategies, so the matrix is 2×2. Each cell contains a pair of payoffs — one for each firm — corresponding to that combination of choices. The key modeling assumption is **simultaneity**: players choose without observing what others do. This does not literally require choices at the same instant — it means each player must decide without knowing the other's decision, as if moves were simultaneous. This is what distinguishes strategic form games from extensive form games, where players move in sequence and can observe earlier actions.

Finding Nash equilibria in a strategic form game follows a systematic procedure. For each cell in the matrix, ask: given what the other player chose, could this player do better by switching? If neither player can improve by switching, that cell is a **Nash equilibrium**. In the classic Prisoner's Dilemma, both players defecting is the unique Nash equilibrium — not because it is the best joint outcome, but because neither player can unilaterally improve by cooperating when the other defects. Some games have multiple Nash equilibria (like the Battle of the Sexes), which raises coordination problems. Others have no pure-strategy equilibrium at all, requiring the mixed strategies you will encounter next.

The power of strategic form representation is its generality. Any finite simultaneous-move game — pricing competition, political campaigning, auction bidding, arms races — can be written as a payoff matrix and analyzed with the same equilibrium tools. The limitation is that it becomes unwieldy as the number of players or strategies grows, and it cannot represent sequential structure or information revelation. That is where extensive form games pick up. But for analyzing the core logic of strategic interdependence — "what should I do given what I think you will do?" — the strategic form is the essential starting framework.
