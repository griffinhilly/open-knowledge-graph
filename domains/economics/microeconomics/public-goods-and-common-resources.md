---
id: public-goods-and-common-resources
title: Public Goods and Common Resources
domain: economics
course: microeconomics
prerequisites:
- id: externalities-and-market-failure
  type: hard
- id: welfare-analysis-microeconomics
  type: soft
- id: natural-monopoly
  type: soft
tags:
- public goods
- common resources
- free rider
- tragedy of the commons
- excludability
- rivalry
stage: advanced
status: validated
---
# Public Goods and Common Resources

## Core Idea
Goods are classified by two properties: excludability (can non-payers be prevented from consuming?) and rivalry (does one person's consumption reduce availability for others?). Public goods are non-excludable and non-rival (e.g., national defense); the free-rider problem causes private markets to underprovide them. Common resources are non-excludable but rival (e.g., fisheries); the tragedy of the commons leads to overuse and depletion. Club goods are excludable but non-rival (e.g., streaming services); private markets generally provide these efficiently.

## How It's Best Learned
Build the 2×2 classification matrix and populate it with examples before analyzing incentive problems. The free-rider problem (public goods) and tragedy of the commons (common resources) should each be analyzed using a simple game-theoretic payoff structure.

## Common Misconceptions
- 'Public good' in economics has a precise technical meaning (non-excludable + non-rival) that does not match its everyday use as 'something beneficial to society.'
- Not all government-provided goods are public goods in the economic sense (e.g., toll roads are excludable).

## Questions

```yaml
- question: "A city provides free fireworks displays visible from any outdoor location in the city. How should this be classified using the excludability-rivalry framework?"
  type: multiple-choice
  options:
    - "A private good — only taxpayers who funded it receive the benefit"
    - "A common resource — only a limited number of viewing spots exist near the launch site"
    - "A public good — non-payers cannot be excluded and one person's enjoyment does not reduce another's"
    - "A club good — the city can exclude people by controlling the launch location"
  answer: 2
  explanation: "Fireworks are the textbook example of a public good: they are non-excludable (you cannot prevent anyone in view from watching, whether or not they paid taxes) and non-rival (one person watching does not reduce how much anyone else can enjoy the display). Option B confuses physical proximity with economic rivalry — rivalry means consumption reduces the available quantity, not that locations near the display are preferred. The fact that taxes fund the fireworks doesn't make them excludable; it's the mechanism of provision, not a property of the good itself."

- question: "A national park is free and open to all visitors. A student claims this is a 'public good' in the economic sense. Under what condition would the park fail to qualify as a public good?"
  type: multiple-choice
  options:
    - "If the park is owned and operated by the government rather than a private company"
    - "If the park becomes sufficiently crowded that additional visitors reduce the quality of experience for others — introducing rivalry"
    - "If the park provides ecological benefits to people who never visit it"
    - "A park always qualifies as a public good because it serves the general public"
  answer: 1
  explanation: "The everyday meaning of 'public good' (beneficial to society, government-provided) and the economic definition (non-excludable AND non-rival) frequently diverge. An uncrowded park may be non-rival — my hike doesn't diminish your hike. But once congestion sets in, additional visitors reduce trail quality, parking availability, and wildlife sightings for others. Rivalry has emerged. At that point the park becomes a common resource (non-excludable but rival), subject to overuse problems rather than free-rider problems. Option D is the classic misconception: 'public' in common usage ≠ 'public good' in economics."

- question: "The tragedy of the commons occurs because resource users are irrational or short-sighted — if they fully understood the consequences of overuse, they would voluntarily restrain themselves."
  type: true-false
  answer: false
  explanation: "The tragedy of the commons is a rational equilibrium outcome, not a failure of rationality or foresight. Each individual fisher faces a dominant strategy to fish as much as possible: if they restrain themselves while others don't, the fish are depleted anyway and they simply caught fewer. The individually rational strategy — fish more — leads to collective depletion even when all parties fully understand and regret the outcome. This is a prisoner's dilemma structure, not a cognitive failure. The tragedy follows directly from non-excludability combined with rivalry in the incentive structure."

- question: "A fishing license system that caps the total number of licenses is an example of addressing the tragedy of the commons by converting the resource from non-excludable to excludable."
  type: true-false
  answer: true
  explanation: "Licensing creates excludability: those without a license can be legally prevented from fishing. By capping the number of licenses, the regulator limits total fishing effort to a sustainable level. This doesn't eliminate rivalry (each fish caught is still gone), but it addresses the overuse problem by removing the non-excludability that produced the tragedy. Tradeable permit systems go further by assigning property rights in the catch itself, giving license holders an incentive to manage sustainably — they now own a share of the resource's future value."

- question: "Why do common resources tend toward overuse even when all parties involved would prefer the resource to be conserved? What does this reveal about the structure of the tragedy of the commons?"
  type: short-answer
  answer: "Each individual faces a prisoner's dilemma: if they restrain their use while others do not, the resource is depleted anyway and they simply consumed less. If they use more, they capture more of the resource before it disappears. The dominant strategy for each individual is to use more, regardless of what others do. This produces a Nash equilibrium of overuse even though all parties would prefer collective restraint. The tragedy reveals that the market failure is structural — caused by non-excludability creating a misalignment between individual incentives and collective welfare — not by ignorance or malice."
  explanation: "The tragedy of the commons is an application of the prisoner's dilemma to a shared resource. The key is the asymmetry between the benefits of restraint (shared across all users) and the costs of restraint (borne entirely by the individual). No single actor's restraint prevents depletion if others continue overusing the resource. This structural problem is why policy solutions require changing the incentive structure — through property rights, regulation, or negotiated agreements — rather than simply educating users about consequences."
```

## Explainer

Building on your study of externalities and market failure, public goods and common resources represent two cases where markets fail not because of spillover costs or benefits to third parties, but because of a structural problem with how the good itself can be consumed. The key classification uses two independent properties: **excludability** (can a seller prevent non-paying consumers from using the good?) and **rivalry** (does one person's consumption reduce what is available to others?). These two binary attributes generate a 2×2 grid that carves up the entire universe of goods.

**Public goods** are non-excludable and non-rival. National defense is the textbook case: the military protects everyone within a country's borders whether or not they paid taxes, and one person's protection doesn't diminish anyone else's. This combination produces the **free-rider problem**: since you cannot be excluded if you don't pay, rational individuals have no incentive to voluntarily contribute. Each person prefers to let others fund the good and enjoy the benefits anyway. The Nash equilibrium of this interaction is underprovision — even when the collective value of the good far exceeds its cost, no one pays. This is why public goods are almost universally provided by governments through mandatory taxation rather than voluntary market exchange.

**Common resources** are non-excludable but rival — anyone can access them, but each unit consumed is gone. An ocean fishery is the canonical example: no one owns it, so no one can exclude others, but each fish caught is no longer available. This combination produces the **tragedy of the commons**. Each individual fisher has an incentive to catch as many fish as possible before others do. Even though all fishers collectively would benefit from restraint, each individually is better off fishing more. The equilibrium is overuse and eventual depletion of the resource. The tragedy is not caused by malice or ignorance — it follows directly from the incentive structure created by non-excludability combined with rivalry.

The policy solutions differ accordingly. Public goods problems typically call for government provision funded by taxes, or sometimes subsidies for private provision. Common resource problems typically call for either assigning property rights (privatization, tradeable permits) or direct regulation (catch limits, usage quotas). A fishing permit system that assigns ownership of a share of the total allowable catch converts a common resource into something closer to a private good — now the permit holder has an incentive to manage their allocation sustainably because they own it. Understanding which of the four quadrants a good falls in is the first step in diagnosing what, if anything, needs to be done about it.
