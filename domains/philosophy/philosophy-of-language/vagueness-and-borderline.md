---
id: vagueness-and-borderline
title: Vagueness and Borderline Cases
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: vagueness-sorites-paradox
  type: hard
- id: logical-form
  type: soft
builds-toward:
- compositionality-semantic-limits
tags:
- vagueness
- sorites
- semantics
- logic
stage: formal-systems
status: draft
---

# Vagueness and Borderline Cases

## Core Idea
Vagueness is ubiquitous (is someone with 1,000,001 hairs bald?), yet traditional logic assumes precise truth-conditions. Sorites arguments show how innocent-seeming principles lead to paradox. Supervaluationism, degree semantics, and epistemicism offer competing solutions with different implications for meaning and logic.

## Explainer

You already understand the Sorites paradox: take a heap of sand, remove one grain — still a heap. Repeat a thousand times. At no point does a single grain make the difference between heap and non-heap, yet we end with one grain and the argument forces us to call it a heap. The paradox arises because "heap" is **vague**: there is no sharp boundary between heaps and non-heaps, and cases in the middle — a hundred grains, perhaps — are **borderline cases** where it is genuinely unclear whether the term applies. The challenge is to explain what's happening in borderline cases without accepting the paradox.

The simplest response is **epistemicism**, defended by Timothy Williamson. Vague predicates actually have perfectly sharp extensions — there really is a precise number of hairs below which someone is bald — but we cannot know where the boundary falls because our concepts are not precise enough to detect it. On this view, classical logic is fully preserved: every statement is either true or false; it's just that we can't always know which. The counterintuitive implication is that removing a single hair sometimes makes someone bald, we just can't tell when. Epistemicism saves logic at the cost of making meaning radically inaccessible.

**Supervaluationism** takes a different route. A vague predicate like "tall" can be "precisified" — made arbitrarily sharp — in many different ways. Someone 5'10" might count as tall on some precisifications and not tall on others. Supervaluationism says a sentence is **supertrue** if it is true on all precisifications, **superfalse** if false on all, and **indeterminate** (neither true nor false) if it varies. Classical tautologies like "John is tall or not tall" remain supertrue — true on every precisification — even when "John is tall" is indeterminate. This preserves classical logical laws while allowing truth-value gaps at borderline cases. The cost: some instances of classical inference fail; you can have a disjunction that is supertrue even though neither disjunct is true.

**Degree semantics** (developed by Kamp, Fine, and others) assigns sentences involving vague predicates **degrees of truth** between 0 and 1, rather than just true or false. "John is tall" might have a degree of 0.7 if he's 5'11". Logical connectives then operate on degrees: "not" inverts, "and" takes the minimum, "or" takes the maximum. Borderline cases are cases with intermediate degree, not missing truth values. The challenge for degree semantics is explaining what these degrees represent — are they objective features of the world, facts about our dispositions, or something else? — and handling higher-order vagueness: the boundary between "clearly tall" and "borderline tall" is itself vague, threatening an infinite regress of borderlines. Each theory reveals something important: vagueness is not merely a linguistic imprecision to be cleaned up, but a deep feature of how language engages with a continuous world.
