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
status: validated
---

# Nash Equilibrium in Simultaneous-Move Games

## Core Idea
A Nash equilibrium in a simultaneous-move game is a strategy profile where no player can improve their payoff by unilaterally changing their strategy, given the strategies of other players. In simultaneous-move games, players choose strategies at the same time without knowledge of others' choices. Nash equilibria can be found by identifying best-response functions and locating their intersection. Some games have unique Nash equilibria, others have multiple, and some have none (in pure strategies).

## Questions

```yaml
- question: "In a simultaneous-move game, two firms are currently playing their Nash equilibrium strategies. Firm A's economist points out that if Firm B switched to a different strategy, Firm A could earn a higher profit. What should Firm A do?"
  type: multiple-choice
  options:
    - "Switch its own strategy to try to force Firm B into the better outcome"
    - "Nothing — Firm A's current strategy is already its best response to Firm B's current strategy; Firm A cannot compel Firm B to change"
    - "Communicate with Firm B to coordinate a switch to the higher-payoff outcome"
    - "The situation described is impossible — at Nash equilibrium, no player can benefit from any change by any player"
  answer: 1
  explanation: "Nash equilibrium stability is about *unilateral* deviation: no player can improve by changing their own strategy alone, given what others are doing. The scenario correctly describes Nash equilibrium — Firm A would benefit if *Firm B* changed, but that's a different matter. Option D misreads the definition: Nash equilibrium says no player benefits from changing *their own* strategy, not that no player could benefit from a joint change. Option C describes communication-based coordination, which is not part of Nash equilibrium and may not be available."

- question: "Which of the following best describes what it means for a strategy profile to be a Nash equilibrium?"
  type: multiple-choice
  options:
    - "It is the outcome that maximizes the total payoff for all players combined"
    - "Each player's strategy is their best response to the strategies chosen by all other players"
    - "Players have communicated and agreed to cooperate on the outcome most beneficial for everyone"
    - "Each player is indifferent between all available strategies at the equilibrium"
  answer: 1
  explanation: "Nash equilibrium is defined by mutual best-response: each player is doing as well as they can given what everyone else is doing. It is not about joint welfare maximization (option A) — the prisoner's dilemma is a famous case where the Nash equilibrium is worse for both players than another outcome. It requires no communication (option C). Option D describes mixed-strategy equilibrium indifference, not the general definition."

- question: "A Nash equilibrium can produce an outcome that is worse for every player than some other feasible outcome."
  type: true-false
  answer: true
  explanation: "Yes — the prisoner's dilemma is the textbook example. Mutual defection is a Nash equilibrium (each player's best response to the other defecting is also to defect), but mutual cooperation would be better for both. Nash equilibrium reflects the stability of *individual* incentives, not collective optimality. Players may be 'stuck' in an equilibrium that is inferior for everyone because any single player who deviates unilaterally makes themselves worse off, even if joint deviation would help all."

- question: "In a simultaneous-move game, Nash equilibrium requires that players communicate and agree on their strategies before making their choices."
  type: true-false
  answer: false
  explanation: "False — Nash equilibrium is defined purely in terms of incentives, not communication. Two firms independently setting prices can end up at Nash equilibrium without ever consulting each other, simply because each is responding optimally to what they expect the other to do. The definition only requires that each player's strategy be a best response to the others'. Communication, if anything, would describe correlated equilibrium or cooperative game theory — a different framework."

- question: "What makes a Nash equilibrium 'stable,' and how does this differ from stability in the sense of producing the best possible outcome for the players?"
  type: short-answer
  answer: "Nash equilibrium stability means no individual player has an incentive to unilaterally deviate — each is already playing their best response given what others are doing, so there is no individual gain from switching. This is stability in the sense of no individual pressure to change. It is entirely separate from producing the best possible outcome: the equilibrium may be collectively suboptimal (like mutual defection in the prisoner's dilemma) but still stable because any single player who tries to improve the situation by deviating makes themselves worse off in the process."
  explanation: "The distinction between individual incentive stability and collective optimality is the central tension in game theory. It explains why markets can get stuck in bad equilibria (arms races, pollution, overuse of commons) even when everyone knows a better outcome exists — knowing isn't enough if the individual incentive points in the wrong direction."
```

## Explainer

From your game theory prerequisites, you know that a game specifies players, their available strategies, and the payoffs each receives as a function of everyone's choices. In a **simultaneous-move game**, no player observes another's action before choosing — they all move at once, like choosing Rock, Paper, or Scissors on a count of three. This simultaneity makes the problem genuinely strategic: you must reason about what others will do while they reason about what you will do.

A **Nash equilibrium** is the resolution to this mutual-reasoning problem. It is a combination of strategies — one per player — such that each player's choice is the best they can do given what the other players are doing. More precisely: if you told every player exactly what the others planned to do, no one would want to deviate. This mutual best-response property is what makes Nash equilibrium a stable prediction. It's not that players necessarily cooperate or communicate — it's that each is already playing optimally against the others' strategies, so there is no individual incentive to change.

The practical method for finding Nash equilibria in small games is to search for **best responses**. For each strategy of your opponent, ask: "What is my best reply?" Mark it. Then do the same for your opponent given your strategies. A Nash equilibrium is any cell where both players are simultaneously best-responding to each other — where both markings coincide. In a 2×2 payoff matrix, this amounts to checking four cells; in larger games, you list best-response functions and find where they intersect.

Not all games have a unique Nash equilibrium. Some have multiple — the classic coordination game "which side of the road do we drive on?" has two Nash equilibria (both left, or both right) and neither is inherently superior. Some games have no Nash equilibrium in **pure strategies** (where each player picks one strategy with certainty), though Nash's theorem guarantees that every finite game has at least one equilibrium in **mixed strategies** (where players randomize). Understanding Nash equilibrium is the foundation for nearly everything that follows in game theory: Cournot competition, the prisoner's dilemma, and bargaining models all turn on identifying where best-response functions meet.
