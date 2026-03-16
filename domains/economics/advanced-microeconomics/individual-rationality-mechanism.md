---
id: individual-rationality-mechanism
title: Individual Rationality (Participation Constraint)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-intro
  type: hard
tags:
- mechanism-design
- participation
- voluntary-participation
stage: abstract-reasoning
status: draft
---

# Individual Rationality (Participation Constraint)

## Core Idea
Individual rationality (IR) requires that participation in the mechanism yields at least the agent's reservation utility (outside option). For each type, u_i(outcome | type) ≥ u_i(outside option). The mechanism must leave everyone at least as well off as not participating. IR + IC together characterize feasible mechanisms.

## Explainer

From your introduction to mechanism design, you know that the designer's challenge is to create rules that produce desirable outcomes even when participants have private information and selfish incentives. The **incentive compatibility (IC)** constraint ensures that agents report truthfully. But there is a logically prior question: will agents participate at all? The **individual rationality (IR) constraint**, also called the **participation constraint**, addresses exactly this — it requires that every agent, regardless of their private type, is at least as well off participating in the mechanism as they would be by walking away.

The concept is intuitive through an example. Suppose you are designing an auction to sell a painting. Bidders have private valuations. You want them to bid truthfully (IC) and actually show up to bid (IR). A bidder whose painting valuation is $500 will not participate in a mechanism that charges a $600 entry fee regardless of whether they win. The IR constraint says: for every possible valuation a bidder might hold, their expected payoff from participating must be at least as good as their **outside option** — typically normalized to zero (doing nothing). If you violate IR for some type, agents of that type simply opt out, and your mechanism unravels for those participants.

The bite of the IR constraint depends on *when* it must hold. **Ex post IR** requires that every agent is happy after learning the full outcome — the strongest version, meaning no participant ever regrets joining. **Interim IR** requires that agents are happy to participate given their own type but before learning others' types — this is the standard in Bayesian mechanism design. **Ex ante IR** only requires that agents would participate before knowing their own type, which is the weakest version. The distinction matters because stronger IR constraints limit what the designer can achieve. Ex post IR, for instance, rules out mechanisms where some types sometimes "lose" from participation, even if on average everyone gains.

The real power of IR emerges when combined with IC. Together, they define the **feasible set** of mechanisms — the space of rules the designer can actually implement with voluntary, self-interested participants. A mechanism that achieves the best possible outcome subject to both IC and IR is called a **second-best** mechanism (since the first-best would be achievable with full information and mandatory participation). The classic result in auction theory, for example, shows that the optimal auction must leave **informational rents** to bidders with high valuations: you cannot extract the full surplus because doing so would violate either IC (high types would pretend to be low types) or IR (low types would refuse to participate). The IR constraint for the lowest type, combined with IC for all types, pins down how much surplus the designer must leave on the table.

This framework extends far beyond auctions. Any institution that relies on voluntary participation — labor contracts, insurance markets, public goods provision, trading platforms — faces an IR constraint. A health insurance plan that charges premiums so high that healthy individuals drop out is violating their IR constraint, leading to the adverse selection spiral you may recognize from information economics. The IR constraint is the formal expression of a simple but powerful idea: you cannot design rules for people who refuse to play the game.
