---
id: sample-spaces-and-events
title: Sample Spaces and Events
domain: mathematics
course: probability-and-statistics
prerequisites: []
builds-toward:
- probability-rules-for-events
- law-of-total-probability
tags:
- foundations
- probability
- set-theory
stage: formal-systems
status: draft
---

# Sample Spaces and Events

## Core Idea
A sample space is the set of all possible outcomes of an experiment. An event is any subset of the sample space. Understanding sample spaces and events is essential for assigning probabilities and reasoning about random phenomena.

## How It's Best Learned
Start with concrete experiments like coin flips and dice rolls. Draw Venn diagrams to visualize events and their relationships. Practice identifying sample spaces and events in various real-world scenarios.

## Common Misconceptions
Confusing an event with a single outcome. Thinking the sample space is always numerical. Not recognizing that the same experiment can have different sample spaces depending on what outcomes we care about.

## Explainer

Before you can assign probabilities to anything, you need a precise language for describing what can happen. A **sample space** is simply the set of all possible outcomes of an experiment — exhaustive (every possibility is included) and mutually exclusive (no two outcomes can occur simultaneously). For a coin flip, the sample space is {Heads, Tails}. For rolling a standard die, it is {1, 2, 3, 4, 5, 6}. For measuring tomorrow's temperature, it might be any real number in a continuous range. The sample space is your universe — nothing outside it can be assigned a probability.

An **event** is any subset of the sample space. When you ask "what is the probability of rolling an even number?", you are asking about the event {2, 4, 6} — a subset of the die's sample space. Single outcomes like {3} are called **elementary events** or **simple events**; compound events like "rolling above 4" = {5, 6} are just larger subsets. Even the empty set ∅ is a valid event (the impossible event), and the entire sample space Ω is the certain event.

Because events are sets, all of set theory applies to them. The **union** A ∪ B is the event "A or B occurs"; the **intersection** A ∩ B is "both A and B occur"; the **complement** Aᶜ is "A does not occur." These set operations are how you build complex probability statements from simple ones — and they are exactly what makes the Venn diagram a natural tool for probability reasoning.

The same physical experiment can be described by different sample spaces depending on what you care about. Consider tossing a coin twice: if you care about order, the sample space is {HH, HT, TH, TT}. If you only care about how many heads appear, the sample space collapses to {0, 1, 2}. Both are valid, but they support different questions. Choosing the right sample space — one that is rich enough for your purposes but no richer — is the first modeling decision in any probability problem. The events you can define, and the probabilities you can assign, depend entirely on which sample space you commit to.
