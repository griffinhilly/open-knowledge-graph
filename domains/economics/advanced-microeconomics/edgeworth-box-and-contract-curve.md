---
id: edgeworth-box-and-contract-curve
title: The Edgeworth Box and Contract Curve
domain: economics
course: advanced-microeconomics
prerequisites:
- id: indifference-curves
  type: hard
- id: pareto-efficiency-and-optimality
  type: soft
builds-toward:
- walrasian-equilibrium
tags:
- general-equilibrium
- exchange-economy
stage: expert
status: draft
---

# The Edgeworth Box and Contract Curve

## Core Idea
The Edgeworth box represents all feasible allocations in a 2-good, 2-consumer exchange economy as a rectangle. The contract curve—where indifference curves are tangent—contains all Pareto-efficient allocations. The competitive equilibrium lies on the contract curve at a point where the price line passes through the initial endowment and is tangent to both indifference curves.

## Questions

```yaml
- question: "In an Edgeworth box, Person A and Person B are at an allocation where their indifference curves cross each other. What does this crossing tell us about the allocation?"
  type: multiple-choice
  options:
    - "The allocation is Pareto efficient — both consumers are on their highest feasible indifference curves"
    - "The allocation is on the contract curve because indifference curves intersect"
    - "There exist mutually beneficial trades that have not yet been made"
    - "The competitive equilibrium has been reached at this allocation"
  answer: 2
  explanation: "Crossing indifference curves create a lens-shaped region between them. Every point inside that lens makes both consumers better off than the current allocation — these are unexploited mutual gains from trade. The allocation is therefore not Pareto efficient. The contract curve contains only tangency points (not crossings); at tangency, no lens exists and no further mutual improvements are possible. A competitive equilibrium is a specific point on the contract curve, not just any crossing."

- question: "What geometric condition do all points on the contract curve share?"
  type: multiple-choice
  options:
    - "The relative price line passes through both consumers' indifference curves at the allocation"
    - "Both consumers' marginal rates of substitution are equal — their indifference curves are tangent"
    - "One consumer has reached the highest indifference curve possible given total endowments"
    - "The allocation divides both goods in equal proportions between the two consumers"
  answer: 1
  explanation: "The contract curve is precisely the locus of Pareto-efficient allocations, which occur where indifference curves are tangent rather than crossing. At tangency, both consumers have the same MRS — they value the next unit of each good at the same rate. If MRS values differed, one person would value fish more than the other, and a mutually beneficial swap would exist. Equal division (option D) is one point on the contract curve only if preferences are symmetric; it is not a defining feature."

- question: "A competitive equilibrium always divides the gains from trade equally between the two consumers, landing at the midpoint of the contract curve."
  type: true-false
  answer: false
  explanation: "The competitive equilibrium lands at a specific point on the contract curve determined by the initial endowment and the price ratio, not at the midpoint. The price line passes through the initial endowment and is tangent to both indifference curves at the equilibrium allocation — but where that tangency occurs depends entirely on the shape of preferences and the location of the endowment. Consumers with very strong bargaining positions or favorable endowments may capture most of the gains from trade. The First Welfare Theorem guarantees efficiency (on the contract curve), not equity."

- question: "Every allocation inside the lens-shaped region formed by the two indifference curves passing through the initial endowment makes both consumers better off than the endowment."
  type: true-false
  answer: true
  explanation: "The lens is bounded by the indifference curves that each consumer achieves at the initial endowment. By definition, any point strictly inside the lens lies above A's endowment indifference curve (A prefers it) and above B's endowment indifference curve (B prefers it) — both prefer any point in the interior to the endowment itself. This is why rational agents will trade away from the endowment into the lens, and why the endowment is typically not Pareto efficient unless it happens to already lie on the contract curve."

- question: "Why does trading stop at the contract curve rather than at some arbitrary allocation inside the lens of mutual gains?"
  type: short-answer
  answer: "Trading stops at the contract curve because that is where all mutual gains from trade are exhausted. At any point off the contract curve where indifference curves cross, a lens of further beneficial trades exists — so rational agents will continue trading. Trading stops only when no remaining allocation makes both parties better off, which requires indifference curves to be tangent (equal MRS). At tangency, no further exchange improves both parties, so trade halts. The contract curve is the set of all such tangency points."
  explanation: "The underlying logic is Pareto efficiency: if an allocation is not on the contract curve, it is Pareto dominated by some nearby allocation — meaning we can find a trade that benefits at least one party without harming the other. Rational agents will always accept Pareto-improving trades. Only when the allocation is on the contract curve — where no such improvements exist — does voluntary exchange cease. This is the connection to the First Welfare Theorem: competitive markets drive the economy to the contract curve."
```

## Explainer

Picture two people stranded on an island with fixed quantities of two goods — say, fish and coconuts. Person A has lots of fish but few coconuts; Person B has the reverse. The **Edgeworth box** represents every possible way to divide these goods between them. The box is a rectangle whose width equals the total fish and whose height equals the total coconuts. Person A's origin is the bottom-left corner; Person B's origin is the top-right corner, flipped so that B's quantities increase leftward and downward. Any point inside the box is a feasible allocation — it tells you exactly how much of each good each person has, and the totals always add up.

Now overlay both consumers' indifference curves onto this box. Person A's curves radiate outward from the bottom-left (higher utility curves are further from A's origin). Person B's curves radiate outward from the top-right. At the initial endowment point, the two sets of indifference curves will typically cross, forming a lens-shaped region between them. Every point inside that lens makes *both* people better off than the endowment — these are the **mutually beneficial trades**. Rational agents will trade into this lens. But they will not stop just anywhere; they will keep trading until no further mutual gains exist.

Trading possibilities are exhausted when the indifference curves are **tangent** — touching but not crossing. At tangency, the marginal rates of substitution (MRS) are equal: both consumers value the next unit of fish relative to coconuts at the same rate. If the MRS values differed, one person would value fish more than the other, and a mutually beneficial swap would still exist. The set of all tangency points traces out the **contract curve**, which runs from A's origin to B's origin. Every point on the contract curve is **Pareto efficient** — you cannot make one person better off without making the other worse off. Points off the contract curve always leave gains from trade on the table.

Where on the contract curve do the agents end up? That depends on their starting point and the mechanism of exchange. In a **competitive equilibrium**, a price ratio (the relative price of fish to coconuts) determines a budget line passing through the initial endowment. Each person maximizes utility along this line. The equilibrium price is the one where both consumers' optimal choices coincide — their Marshallian demands add up to the total supply of each good. Geometrically, this is the point on the contract curve where the price line through the endowment is tangent to both indifference curves simultaneously. The First Welfare Theorem guarantees this outcome is Pareto efficient, confirming that competitive markets — even in this stripped-down two-person economy — exhaust all gains from trade.
