---
id: arrow-impossibility-theorem
title: Arrow's Impossibility Theorem and Social Choice
domain: economics
course: advanced-microeconomics
prerequisites:
- id: information-asymmetry
  type: soft
tags:
- social-choice
- voting
stage: advanced
status: draft
---
# Arrow's Impossibility Theorem and Social Choice

## Core Idea
Arrow's Impossibility Theorem shows that no voting rule simultaneously satisfies: unrestricted domain (any preference profile), unanimity (if all prefer A to B, society does), independence of irrelevant alternatives (society's A vs. B ranking depends only on voters' relative preferences), and non-dictatorship (no single voter dictates). This fundamental result reveals unavoidable tradeoffs in aggregating preferences into collective decisions.

## Explainer

Suppose a group of friends needs to rank three restaurants for dinner. Each person has their own preference ordering. You want a rule that takes everyone's individual rankings and produces a single group ranking. This sounds straightforward — majority rule works fine with two options. But Arrow's theorem says that with three or more alternatives, no rule can satisfy a small set of seemingly reasonable fairness conditions simultaneously. The result is not about any particular voting system being flawed; it is about all possible systems being flawed in at least one way.

The four conditions Arrow requires each seem individually uncontroversial. **Unrestricted domain** means the rule must work for any combination of individual preferences — you cannot assume people's tastes are conveniently aligned. **Unanimity** (also called the Pareto condition) says that if literally every voter prefers A to B, the group ranking should place A above B. **Independence of irrelevant alternatives** (IIA) says that the group's ranking of A versus B should depend only on how individuals rank A versus B — not on how they feel about some third option C. **Non-dictatorship** says no single individual always gets their way regardless of what everyone else wants. Each condition seems like a minimal requirement for a fair system, yet Arrow proved they are collectively incompatible.

The proof works by showing that the conditions, taken together, force an escalating concentration of power. Start with any group of voters that is "decisive" over some pair of alternatives — meaning their preferences determine the group ranking for that pair. IIA and unanimity together imply that this decisive group must also be decisive over every other pair. Then you can show that any decisive group can be split into smaller decisive subgroups, and this process continues until you reach a single individual who is decisive over all pairs — a dictator. The logic is inescapable: the axioms themselves generate the dictatorship.

The practical impact is profound for institutional design. Every real voting system — plurality rule, ranked-choice voting, Borda counts, approval voting — violates at least one of Arrow's conditions. Plurality and ranked-choice violate IIA: adding a third candidate can change the relative ranking of the original two (this is the "spoiler effect" familiar from elections). Borda counts also violate IIA. Dictatorship satisfies the other three conditions trivially but violates non-dictatorship. Understanding which condition each system sacrifices is essential for evaluating democratic institutions, committee decision-making, and any setting where individual preferences must be aggregated into a collective choice. Arrow's theorem does not say democracy is impossible — it says that every democratic system involves an unavoidable compromise, and the question is which compromise you are willing to accept.
