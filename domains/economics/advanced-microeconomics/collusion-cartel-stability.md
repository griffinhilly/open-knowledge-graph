---
id: collusion-cartel-stability
title: Collusion, Cartels, and Stability
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cournot-competition
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
tags:
- industrial-organization
- collusion
- repeated-games
stage: expert
status: validated
---

# Collusion, Cartels, and Stability

## Core Idea
Cartels are agreements among competitors to restrict output and elevate price toward monopoly levels, sharing monopoly profit. Collusion is unstable because each firm has incentive to cheat by undercutting the agreed price. Sustainability requires credible punishment (grim trigger: permanent reversion to Cournot) and sufficient future profit weight, with higher discount rates destabilizing collusion.

## Questions

```yaml
- question: "Two firms have agreed to collude at monopoly output levels. One firm is considering secretly expanding its output. Why is cheating individually rational, even though it harms the cartel?"
  type: multiple-choice
  options:
    - "The cheating firm earns extra revenue by undercutting the agreed price while the rival still restricts output, capturing more sales at a still-high price"
    - "Cheating is only rational if the rival can be permanently driven out of the market"
    - "Cheating is rational only in industries with low fixed costs because margins are thin"
    - "The cheating firm benefits because its rival will retaliate by also raising output, pushing price back to competitive levels"
  answer: 0
  explanation: "If one firm secretly expands output while the rival adheres to the agreement, the cheater sells more units at a price that is still elevated (because the rival is still restricting). This is the prisoner's dilemma structure: taking the other's cooperation as given, defecting is privately optimal. The cheater captures more than its agreed share of a still-inflated price. This is exactly why collusion is unstable without credible enforcement — the incentive to defect exists even when cooperation is jointly superior."

- question: "A cartel has been stable for several years. Interest rates in the economy rise sharply, increasing firms' discount rates. What does this do to cartel stability?"
  type: multiple-choice
  options:
    - "It strengthens the cartel because higher rates increase the cost of building new production capacity, protecting members' market shares"
    - "It has no effect because cartel stability depends only on market concentration, not on interest rates"
    - "It destabilizes the cartel because a higher discount rate reduces the present value of future collusive profits relative to the one-time cheating gain"
    - "It stabilizes the cartel because firms become more risk-averse and prefer the certainty of collusive profits"
  answer: 2
  explanation: "The sustainability condition requires that the present value of continuing to collude (future stream of collusive profits) exceeds the one-time windfall from cheating plus the discounted stream of Cournot punishment profits. A higher discount rate reduces the present value of all future payoffs — the collusive profit stream shrinks relative to the immediate gain from defection. This is the critical economic logic: patient firms (high δ, low discount rates) can sustain collusion; impatient firms cannot. Rising interest rates are thus a genuine destabilizing force for cartels."

- question: "In a one-shot (single-period) prisoner's dilemma game, cheating on a collusive agreement is the dominant strategy for each firm."
  type: true-false
  answer: true
  explanation: "In a one-shot game, each firm's best response is to cheat regardless of what the other does. If the rival restricts output, cheating yields more profit. If the rival also cheats, cheating prevents being the sucker. There is no future relationship to protect, so the one-time gain from defection is unambiguously optimal. This is precisely why indefinite repetition is necessary for collusion — only the threat of future punishment creates an incentive to cooperate today."

- question: "Cartels with more member firms are more stable than two-firm cartels because more members means better mutual monitoring of each other's output."
  type: true-false
  answer: false
  explanation: "More firms actually destabilizes collusion, for two reasons. First, each firm's share of monopoly profits shrinks as n increases, while the temptation to cheat (proportional to the market price gap) remains large — the gain from defection is less diluted than the cooperative reward. Second, monitoring becomes harder with more participants because detecting who cheated among many firms is more difficult. The Green-Porter model formalizes this: imperfect monitoring creates uncertainty about whether a price decline reflects cheating or just demand variation, and more firms compound this problem."

- question: "What is the grim trigger strategy, and why must the threatened punishment be credible for it to sustain collusion?"
  type: short-answer
  answer: "The grim trigger strategy is: cooperate (restrict output to the agreed level) as long as all firms have cooperated in every past period; if anyone ever cheats, revert permanently to the Cournot-Nash equilibrium forever. For this to deter cheating, the threat must be credible — firms must actually follow through on the punishment. If the threatened reversion to Cournot is itself optimal once cheating occurs (it is, since Cournot is a Nash equilibrium), the threat is credible even without an external enforcer."
  explanation: "The credibility requirement is non-trivial. A threat to do something that would not be in your interest to actually carry out is not credible. Crucially, reverting to Cournot after cheating IS individually rational — Cournot is the static Nash equilibrium, and each firm's best response to the other playing Cournot is to play Cournot. So the punishment enforces itself. This is why grim trigger works while, say, threatening to exit the market would not — exit is too extreme and therefore not credible."
```

## Explainer

From Cournot competition, you know that oligopolists who independently choose quantities end up at a Nash equilibrium where industry profits are lower than monopoly profits — competition dissipates some of the surplus. This creates an obvious temptation: what if firms agree to collectively restrict output to the monopoly level and split the larger pie? This is the logic behind **cartels**, and it immediately raises the central question of this topic: why don't all oligopolists collude, and why do cartels so often fall apart?

The instability comes directly from the structure of the Cournot game. Suppose two firms agree to each produce half the monopoly quantity. At this restricted output, the market price is high. But each firm, taking the other's restricted output as given, finds it profitable to **cheat** — to secretly produce more than its agreed share. The cheating firm captures extra sales at a still-high price (since the other firm is still restricting output), earning more than its share of monopoly profits. This is the same logic as the prisoner's dilemma: mutual cooperation (collusion) is jointly optimal, but individual defection is privately optimal. In a one-shot game, cheating is the dominant strategy and collusion unravels.

The resolution lies in **repeated interaction**. If firms compete period after period indefinitely, they can sustain collusion using **trigger strategies**: cooperate as long as everyone cooperates, but if anyone cheats, revert permanently to the Cournot-Nash equilibrium (the **grim trigger**). The cheater gains a one-period windfall from extra output but loses the stream of future collusive profits, receiving only Cournot profits forever after. Whether collusion holds depends on the **discount factor** (δ). The critical condition is that the present value of continued collusive profits must exceed the one-time cheating gain plus the discounted stream of punishment profits. This yields a minimum discount factor below which collusion is unsustainable — impatient firms (high discount rates, low δ) cannot maintain cartels because the immediate temptation outweighs distant future losses.

Several real-world factors map onto this framework. More firms make collusion harder — each firm's share of monopoly profit shrinks while the temptation to cheat remains large. Demand fluctuations create problems because firms cannot easily distinguish a rival's cheating from a genuine demand decline (the **Green-Porter** model of imperfect monitoring). Asymmetric costs make agreement on output shares contentious. Antitrust enforcement raises the cost of collusion by adding legal penalties. OPEC illustrates every element: members periodically agree to output quotas, individual members regularly exceed them, and the cartel's effectiveness varies with how patient members are and how well they can monitor each other's production.
