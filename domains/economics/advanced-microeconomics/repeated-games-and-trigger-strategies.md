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
- id: mixed-strategies-probability
  type: soft
builds-toward:
- cartel-and-collusion
tags:
- game-theory
- repeated-interaction
stage: expert
status: validated
---
# Repeated Games and Trigger Strategies

## Core Idea
In infinitely repeated games, players can sustain cooperation via trigger strategies that punish deviations. The Folk Theorem shows that any outcome achieving each player's maximin payoff can be sustained as subgame-perfect equilibrium with low enough discount rates. Triggers create accountability: deviating gains short-term but triggers permanent punishment, making cooperation attractive if players are patient enough.

## Questions

```yaml
- question: "Two oligopolists play a prisoner's dilemma and know they will interact exactly 20 times. A consultant recommends implementing a grim trigger strategy to sustain cooperation throughout all 20 rounds. What is the fundamental flaw in this advice?"
  type: multiple-choice
  options:
    - "The grim trigger is too lenient — tit-for-tat would be necessary to deter defection over 20 rounds"
    - "In a finitely repeated game with a known endpoint, backward induction unravels cooperation: both firms defect in round 20 (no future threat exists), then in round 19, and so on, leaving no cooperative equilibrium regardless of the trigger strategy used"
    - "The grim trigger fails because the discount factors in oligopoly settings are too high to make punishment credible"
    - "Twenty rounds is too short for trigger strategies to establish a cooperation norm"
  answer: 1
  explanation: "The logic of backward induction destroys cooperation in any finitely repeated prisoner's dilemma with a known endpoint. In the final round, no future interaction exists to threaten, so the dominant strategy is to defect. Both players know this, so in round 19 the future threat is already worthless, and defection dominates there too. This logic propagates all the way back to round 1. The grim trigger (or any trigger strategy) requires a credible future threat, and knowing the game ends in round 20 removes that credibility entirely. Indefinite repetition — not just long repetition — is the essential ingredient."

- question: "A business relationship becomes more long-term, raising a firm's discount factor δ from 0.6 to 0.95. Under a grim trigger strategy in an infinitely repeated prisoner's dilemma, how does this change affect the sustainability of cooperation?"
  type: multiple-choice
  options:
    - "Higher δ reduces the present value of future payoffs relative to current payoffs, making defection more tempting"
    - "Higher δ makes cooperation more sustainable because the long-run cost of triggering permanent punishment (the lost stream of cooperative surplus) now outweighs the short-run gain from defecting"
    - "The discount factor is irrelevant in infinitely repeated games because the game has no terminal period"
    - "Higher δ reduces the credibility of the grim trigger by making punishment more costly for both parties"
  answer: 1
  explanation: "A higher δ means the firm places more weight on future payoffs. Cooperation is sustained when the present value of remaining cooperative forever exceeds the one-time defection gain plus the discounted stream of punishment-phase payoffs. When δ rises, the future cooperative stream (worth 3/(1−δ) in the classic prisoner's dilemma) grows much larger, while the defection gain (worth 5 once) stays constant. Above the critical threshold δ*, the future cooperation value dominates and defection is irrational. Patient players — those who care about the future — cooperate."

- question: "Trigger strategies can sustain cooperation in a finitely repeated prisoner's dilemma as effectively as in an infinitely repeated one, provided players choose a sufficiently severe punishment."
  type: true-false
  answer: false
  explanation: "Severity of punishment does not matter when the game has a known endpoint. In the final period, no future threat of any severity exists, so both players defect. Backward induction then unravels cooperation in every preceding period, regardless of the punishment that would apply in a period that never triggers. Only in indefinitely repeated games (where each period has positive probability of continuation) does the threat of future punishment remain credible in every period."

- question: "The Folk Theorem implies that infinitely repeated games with sufficiently patient players have many possible equilibrium outcomes — not a single cooperative equilibrium."
  type: true-false
  answer: true
  explanation: "The Folk Theorem shows that any payoff vector giving each player at least their minmax payoff can be sustained as a subgame-perfect equilibrium when δ is close enough to 1. This creates a vast set of sustainable outcomes — from barely better than mutual defection all the way to the cooperative ideal, and many points in between. Which equilibrium actually emerges depends on which strategies players coordinate on. The Folk Theorem explains cooperation but also why predicting the specific cooperative outcome is difficult: repetition opens up a large equilibrium space rather than selecting a unique outcome."

- question: "Explain why a player's discount factor δ is crucial to whether cooperation can be sustained under a grim trigger strategy in an infinitely repeated prisoner's dilemma."
  type: short-answer
  answer: "The discount factor δ determines how much a player values future payoffs relative to present ones. Under the grim trigger, a player contemplating defection compares a one-time gain (defecting while the opponent cooperates) against the permanent loss of the cooperative surplus (triggering mutual defection forever). If δ is low, future payoffs are heavily discounted and the short-term defection gain dominates — cooperation breaks down. If δ is high (close to 1), future payoffs are nearly as valuable as today's, and the long stream of foregone cooperative surplus makes defection unprofitable. There is a critical threshold δ* above which cooperation is individually rational for every player in every period."
  explanation: "The formal condition is: cooperation payoff stream ≥ defection payoff, or V_coop/(1−δ) ≥ V_defect + δ·V_punish/(1−δ). Rearranging gives δ ≥ (V_defect − V_coop)/(V_defect − V_punish). The intuition is that patience — valuing the future — is what makes threats credible and cooperation self-enforcing."
```

## Explainer

From strategic-form games and Nash equilibrium, you know that the prisoner's dilemma has a unique Nash equilibrium: both players defect, even though mutual cooperation would make both better off. This is frustrating but logically airtight — in a one-shot interaction. But most real interactions are not one-shot. Firms compete quarter after quarter, countries negotiate trade policy year after year, and neighbors interact daily. **Repeated games** formalize this by playing the same "stage game" over and over, and the central insight is dramatic: repetition can sustain cooperation that is impossible in a single play.

The mechanism is a **trigger strategy**. The simplest version, the **grim trigger**, works as follows: cooperate in every period as long as all players have cooperated in every past period; if anyone ever defects, switch to the Nash equilibrium of the stage game forever. Consider two firms in a repeated prisoner's dilemma. Under mutual cooperation, each earns a payoff of 3 per period. Defecting while the other cooperates yields 5 in that period but triggers permanent reversion to mutual defection, earning only 1 per period thereafter. A firm contemplating defection compares the one-time gain (5 - 3 = 2) against the perpetual loss of future cooperative surplus. With a discount factor δ (the weight placed on next period's payoff), cooperation is sustained when the present value of continued cooperation exceeds the defection payoff: 3/(1-δ) ≥ 5 + δ·1/(1-δ). Rearranging yields a critical discount factor — above this threshold, patient players cooperate; below it, the future is not valuable enough to deter cheating.

The **Folk Theorem** generalizes this logic far beyond the grim trigger. It states that for sufficiently patient players (δ close to 1), *any* payoff vector that gives each player at least their **minmax payoff** (the worst they can guarantee themselves regardless of others' actions) can be sustained as a subgame-perfect equilibrium of the infinitely repeated game. The implication is startling: repetition does not select a single cooperative outcome — it opens up a vast set of sustainable outcomes, from barely better than mutual defection to the cooperative ideal. The specific equilibrium that emerges depends on which strategies players coordinate on, making equilibrium selection a central challenge.

The grim trigger is powerful but extreme — permanent punishment for a single deviation seems disproportionate and fragile in practice. More realistic strategies include **tit-for-tat** (cooperate initially, then copy the opponent's last action) and **forgiving triggers** that revert to cooperation after a finite punishment phase. These are more robust to errors and trembles — if a player accidentally defects, grim trigger locks in permanent mutual destruction, while tit-for-tat recovers after one round of mutual retaliation. The framework explains why cooperation often emerges in ongoing relationships (business partnerships, international trade) but breaks down when the end is in sight: in a finitely repeated prisoner's dilemma with a known endpoint, backward induction unravels cooperation entirely, since there is no future to threaten in the last period. Indefinite repetition — where players always believe there is a positive probability of future interaction — is the essential ingredient that makes cooperation self-enforcing.
