---
id: repeated-games-and-trigger-strategies
title: Repeated Games and Trigger Strategies
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
- id: nash-equilibrium-microeconomics
  type: soft
builds-toward:
- cartel-and-collusion
tags:
- game-theory
- repeated-interaction
stage: advanced
status: draft
---

# Repeated Games and Trigger Strategies

## Core Idea
In infinitely repeated games, players can sustain cooperation via trigger strategies that punish deviations. The Folk Theorem shows that any outcome achieving each player's maximin payoff can be sustained as subgame-perfect equilibrium with low enough discount rates. Triggers create accountability: deviating gains short-term but triggers permanent punishment, making cooperation attractive if players are patient enough.

## Explainer

From strategic-form games and Nash equilibrium, you know that the prisoner's dilemma has a unique Nash equilibrium: both players defect, even though mutual cooperation would make both better off. This is frustrating but logically airtight — in a one-shot interaction. But most real interactions are not one-shot. Firms compete quarter after quarter, countries negotiate trade policy year after year, and neighbors interact daily. **Repeated games** formalize this by playing the same "stage game" over and over, and the central insight is dramatic: repetition can sustain cooperation that is impossible in a single play.

The mechanism is a **trigger strategy**. The simplest version, the **grim trigger**, works as follows: cooperate in every period as long as all players have cooperated in every past period; if anyone ever defects, switch to the Nash equilibrium of the stage game forever. Consider two firms in a repeated prisoner's dilemma. Under mutual cooperation, each earns a payoff of 3 per period. Defecting while the other cooperates yields 5 in that period but triggers permanent reversion to mutual defection, earning only 1 per period thereafter. A firm contemplating defection compares the one-time gain (5 - 3 = 2) against the perpetual loss of future cooperative surplus. With a discount factor δ (the weight placed on next period's payoff), cooperation is sustained when the present value of continued cooperation exceeds the defection payoff: 3/(1-δ) ≥ 5 + δ·1/(1-δ). Rearranging yields a critical discount factor — above this threshold, patient players cooperate; below it, the future is not valuable enough to deter cheating.

The **Folk Theorem** generalizes this logic far beyond the grim trigger. It states that for sufficiently patient players (δ close to 1), *any* payoff vector that gives each player at least their **minmax payoff** (the worst they can guarantee themselves regardless of others' actions) can be sustained as a subgame-perfect equilibrium of the infinitely repeated game. The implication is startling: repetition does not select a single cooperative outcome — it opens up a vast set of sustainable outcomes, from barely better than mutual defection to the cooperative ideal. The specific equilibrium that emerges depends on which strategies players coordinate on, making equilibrium selection a central challenge.

The grim trigger is powerful but extreme — permanent punishment for a single deviation seems disproportionate and fragile in practice. More realistic strategies include **tit-for-tat** (cooperate initially, then copy the opponent's last action) and **forgiving triggers** that revert to cooperation after a finite punishment phase. These are more robust to errors and trembles — if a player accidentally defects, grim trigger locks in permanent mutual destruction, while tit-for-tat recovers after one round of mutual retaliation. The framework explains why cooperation often emerges in ongoing relationships (business partnerships, international trade) but breaks down when the end is in sight: in a finitely repeated prisoner's dilemma with a known endpoint, backward induction unravels cooperation entirely, since there is no future to threaten in the last period. Indefinite repetition — where players always believe there is a positive probability of future interaction — is the essential ingredient that makes cooperation self-enforcing.
