---
id: cartel-and-collusion
title: 'Cartels and Collusion: Cooperation in Oligopoly'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cournot-competition
  type: hard
- id: repeated-games-and-trigger-strategies
  type: hard
tags:
- industrial-organization
- collusion
stage: expert
status: draft
---

# Cartels and Collusion: Cooperation in Oligopoly

## Core Idea
Firms can increase joint profit by colluding to reduce output and raise prices. However, each firm has incentive to cheat (produce above quota). In infinitely repeated games, collusion is sustainable via trigger strategies: deviators face permanent retaliation. Stability requires that the present value of cooperation exceeds the one-time deviation gain. Discount rates and market concentration determine collusion sustainability.

## Questions

```yaml
- question: "OPEC member countries have agreed to limit oil production. One member's oil minister privately considers pumping more than its quota. In a one-shot interaction, the individually rational choice is:"
  type: multiple-choice
  options:
    - "Honor the quota — all members benefit from the high cartel price"
    - "Pump more — at the elevated cartel price, extra output is profitable and the deviation is individually rational"
    - "Reduce output below quota to signal loyalty and secure a larger future share"
    - "Pump more only if the oil price is above the long-run competitive equilibrium"
  answer: 1
  explanation: "This is the prisoner's dilemma at the heart of cartel theory. When all other firms are holding output down, the price is high — making it privately rational to increase one's own output and sell more units at that high price. The cheater free-rides on partners' restraint. In a one-shot game, this defection is the Nash equilibrium regardless of how high joint profits would be under cooperation. Cartel stability requires repeated interaction."

- question: "A cartel has been stable for years. An antitrust authority announces it will aggressively prosecute price-fixing, significantly raising the expected penalty for participating firms. The most likely effect on cartel stability is:"
  type: multiple-choice
  options:
    - "Firms cooperate more tightly to avoid individual exposure by staying within the cartel"
    - "The cartel destabilizes because prosecution risk effectively lowers the discount factor, making future collusive profits less valuable relative to the one-time deviation gain"
    - "The cartel becomes more transparent, making it easier to monitor and punish cheating"
    - "Firms reduce output further to hide the cartel agreement from regulators"
  answer: 1
  explanation: "The discount factor δ captures not just time preference but also the probability that the repeated game continues. Antitrust enforcement increases the probability that the game ends (through prosecution), which reduces the effective δ. When δ falls below the threshold needed to sustain collusion, the present value of future cooperative profits no longer exceeds the one-shot deviation gain, and the cartel collapses. This is precisely why antitrust enforcement targets collusion: it makes cartels harder to sustain by altering the game's continuation probability."

- question: "In a one-shot prisoner's dilemma, firms can sustain collusion if the joint profits from cooperation are sufficiently large."
  type: true-false
  answer: false
  explanation: "The size of joint profits is irrelevant in a one-shot game. With no future interaction, there is no threat of punishment for defection. Each firm's dominant strategy is to produce its best-response quantity regardless of what others do, resulting in the Cournot-Nash equilibrium. The cooperative outcome, though jointly superior, is not achievable without the credible threat of future punishment — which requires repeated interaction."

- question: "A grim trigger strategy supports collusion by making defection costly: a single deviation triggers permanent reversion to Cournot-Nash equilibrium, eliminating all future collusive profits."
  type: true-false
  answer: true
  explanation: "The grim trigger is the harshest sustainable punishment: cooperate until anyone defects, then revert to Nash forever. This maximizes the cost of defection (the loss of all future collusive surplus) and therefore minimizes the discount factor needed to sustain cooperation. The key is that the punishment is credible — reverting to Nash is itself a Nash equilibrium, so no firm needs to sacrifice to carry it out."

- question: "Why does the discount factor δ play a central role in determining whether collusion is sustainable, and what factors besides time preference affect its value in practice?"
  type: short-answer
  answer: "The discount factor determines how much a firm values future profits relative to present ones. Collusion requires that the present value of future cooperative profits (a stream discounted by δ) exceeds the one-time gain from defection. A high δ makes the future valuable enough that firms prefer cooperation. Beyond pure time preference, δ is also affected by the probability the game continues: regulatory crackdowns, potential market entry by outsiders, or volatile demand can all end the repeated game, effectively lowering δ and destabilizing the cartel even if firms are individually patient."
  explanation: "This is the key insight: δ is not just about impatience but about the continuation probability of the game. Antitrust enforcement, market entry threats, and volatile demand all reduce the effective δ, making collusion harder to sustain. This explains why antitrust policy focuses on detection and punishment rather than just prohibition."
```

## Explainer

From your study of Cournot competition, you know that oligopolistic firms choosing quantities independently produce more total output and earn lower profits than a monopolist would. Each firm ignores the negative externality its production imposes on rivals' revenues. A **cartel** is an agreement among competitors to restrict output and raise the market price toward the monopoly level, splitting the resulting higher profits among members. OPEC's oil production quotas are the classic real-world example: member countries agree to pump less oil than they individually would, keeping the price elevated.

The fundamental problem with any cartel is the **incentive to cheat**. When all other firms are holding output down, the market price is high — which makes it extremely tempting for any single firm to quietly increase its own production. The cheater sells more units at the high cartel price, earning extra profit at the expense of partners who are faithfully restricting output. In a one-shot Cournot game, this temptation is irresistible: the Nash equilibrium has every firm producing its best-response quantity, and the cartel agreement unravels. This is precisely the structure of a prisoner's dilemma — mutual cooperation is collectively optimal, but individual defection is privately rational.

The resolution comes from **repeated games and trigger strategies**, which you have already studied. If the firms interact repeatedly with no known end date, the future consequences of cheating can deter present defection. In a **grim trigger strategy**, all firms cooperate (restrict output) until someone deviates, after which all firms revert to the Cournot-Nash equilibrium forever. The deviator gets one period of high profit from cheating but loses the stream of future collusive profits. Collusion is sustainable when the present value of continued cooperation exceeds the one-shot deviation gain — formally, when the discount factor δ is high enough. Patient firms (high δ) can sustain collusion; impatient firms cannot.

Several factors determine whether collusion can survive in practice. **Market concentration** matters: with fewer firms, each firm's share of collusive profits is larger relative to the temptation to cheat, and monitoring is easier. **Demand stability** helps because volatile demand makes it hard to distinguish a partner's cheating from a genuine demand shock — firms may trigger punishment by mistake. **Transparency** of prices and quantities facilitates monitoring, which is why antitrust authorities are wary of industry practices that increase price visibility (such as advance price announcements). The discount factor captures not just time preference but also the probability the game continues — regulatory crackdowns or market entry that could end the repeated interaction effectively lower δ and destabilize the cartel. This is why antitrust enforcement focuses heavily on detecting and punishing collusion: by increasing the expected cost of getting caught, it reduces the effective discount factor and makes cartels harder to sustain.
