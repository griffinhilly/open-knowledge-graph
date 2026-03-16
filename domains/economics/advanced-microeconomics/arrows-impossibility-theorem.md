---
id: arrows-impossibility-theorem
title: Arrow's Impossibility Theorem
domain: economics
course: advanced-microeconomics
prerequisites:
- id: welfare-analysis-microeconomics
  type: soft
- id: game-theory-basics-microeconomics
  type: soft
tags:
- social-choice
- voting
- impossibility
stage: advanced
status: draft
---

# Arrow's Impossibility Theorem

## Core Idea
Arrow's impossibility theorem proves that no voting rule can simultaneously satisfy four desirable properties: universal domain (handle any preference profile), Pareto efficiency (if all prefer A to B, society ranks A above B), independence of irrelevant alternatives (social ranking of A and B depends only on voters' pairwise preferences), and non-dictatorship (no single voter determines social ranking).

## Explainer

Suppose a group must rank three candidates — call them A, B, and C. Each voter has a complete, transitive preference ordering. The question Arrow posed is deceptively simple: can we design a rule that aggregates individual rankings into a social ranking while satisfying a few basic fairness conditions? From welfare economics, you already know that comparing outcomes across individuals is fraught with difficulty. Arrow formalized this intuition and proved something striking: the answer is no, not even with the mildest requirements.

The four conditions seem almost too reasonable to be controversial. **Universal domain** says the rule must work for any possible combination of voter preferences — you cannot design a system that only works when voters happen to agree. **Pareto efficiency** says if every single voter prefers A to B, the social ranking must place A above B — unanimous preferences should be respected. **Independence of irrelevant alternatives** (IIA) says that society's ranking of A versus B should depend only on how voters rank A versus B, not on how they feel about C. If you preferred chocolate to vanilla yesterday and nothing about those two options changed, the introduction of strawberry as an option should not flip the social ranking of chocolate and vanilla. **Non-dictatorship** says no single voter's preference automatically becomes the social ranking regardless of everyone else.

The theorem's power lies in showing that these conditions are jointly inconsistent when there are three or more alternatives. Any rule satisfying universal domain, Pareto efficiency, and IIA must be dictatorial — one person's ranking is the group ranking. The proof works by showing that the ability to be "pivotal" (decisive between two options) concentrates: if a voter is decisive over one pair, IIA and the Pareto condition force that voter to be decisive over all pairs, making them a dictator. This is not a matter of finding a cleverer voting system. Majority rule fails IIA because of the **Condorcet paradox** — cyclical majorities where A beats B, B beats C, but C beats A. Borda counts fail IIA because adding or removing a candidate can reshuffle the point totals. Every conceivable ranked-choice system falls to the theorem.

Arrow's result does not mean democracy is hopeless — it means that every real voting system involves tradeoffs among desirable properties. Majority rule sacrifices transitivity (and thus potentially IIA). Score voting relaxes the ordinal framework entirely by allowing cardinal information. Restricting the domain of preferences (for example, to single-peaked preferences, where voters agree on a left-right dimension) can restore possibility — this is Black's median voter theorem. The impossibility theorem is a foundational negative result: it sets the boundaries of what social choice theory can achieve and forces explicit discussion of which fairness condition a society is willing to relax.
