---
id: supervenience-dependence
title: Supervenience and Dependence Relations
domain: philosophy
course: metaphysics
prerequisites:
- id: necessary-and-sufficient-conditions
  type: hard
- id: logical-equivalence-formulas
  type: soft
builds-toward:
- physicalism-about-mind
- emergence-and-levels
tags:
- supervenience
- dependence
- properties
stage: formal-systems
status: validated
---

# Supervenience and Dependence Relations

## Core Idea
Supervenience is a dependence relation: if A supervenes on B, there cannot be a difference in A without a difference in B. This framework allows dependence without reduction and appears prominently in discussions of mental-physical relations, normativity, and properties at different organizational levels.

## How It's Best Learned
Work through formal definitions of weak and strong supervenience with examples, then examine concrete cases (color properties supervenient on microphysical properties) and identify their logical limits.

## Common Misconceptions
Assuming supervenience entails reduction or strict causal determination. Thinking weak and strong supervenience are logically equivalent or that supervenience is itself a causal relation.

## Questions

```yaml
- question: "A philosopher argues: 'Since mental properties supervene on physical properties, mental facts just are physical facts — psychology reduces to physics.' What is wrong with this inference?"
  type: multiple-choice
  options:
    - "Nothing — supervenience entails reduction by definition"
    - "Supervenience establishes dependence and covariation, but not identity or reduction"
    - "The argument is correct only for strong supervenience, not weak supervenience"
    - "Supervenience applies to properties, not facts, so the inference is a category error"
  answer: 1
  explanation: "Supervenience captures a one-way determination relation: no A-difference without a B-difference. But this falls far short of reduction, which would require A-properties to be identical to or definable in terms of B-properties. The classic example is aesthetic properties supervening on physical ones — any molecular duplicate of the Mona Lisa would be equally beautiful — without 'beautiful' meaning the same thing as any physical description. Supervenience allows non-reductive physicalism: mental properties depend on physical ones without being reducible to them."

- question: "In two different possible worlds, two beings share exactly the same physical properties but differ in their mental states. Which type of supervenience does this violate?"
  type: multiple-choice
  options:
    - "Neither — supervenience only applies within a single world"
    - "Weak supervenience only"
    - "Strong supervenience only"
    - "Both weak and strong supervenience"
  answer: 2
  explanation: "Weak supervenience only requires that within a single possible world, beings with identical B-properties have identical A-properties. It says nothing about what happens across worlds. Strong supervenience is cross-world: if an object has A-property P in virtue of its B-properties, then any object in any possible world with those B-properties also has P. The scenario described — same physical properties, different mental states in different worlds — violates strong but not necessarily weak supervenience."

- question: "If mental properties supervene on physical properties, then two beings with all the same physical properties must have all the same mental properties."
  type: true-false
  answer: true
  explanation: "This is the direct consequence of the supervenience definition: no A-difference without a B-difference. Equivalently (by contrapositive), if two things differ in their A-properties (mental properties), they must differ in their B-properties (physical properties). So fixing all physical facts fixes all mental facts — you cannot have a mental difference while physical properties remain identical."

- question: "If A supervenes on B, then A-properties are causally produced by B-properties."
  type: true-false
  answer: false
  explanation: "Supervenience is a logical/modal relation — a pattern of covariation — not a causal claim. Saying mental properties supervene on physical ones does not say physical events cause mental events (though they may); it says only that the distribution of mental properties is constrained by the distribution of physical properties. Supervenience is compatible with many different metaphysical stories about the relationship (grounding, causation, realization, emergence), but it does not itself assert any of them."

- question: "Why does supervenience allow dependence without reduction, and why is this distinction philosophically important?"
  type: short-answer
  answer: "Supervenience says only that there can be no A-difference without a B-difference — fixing the B-level fixes the A-level. Reduction would further require that A-properties are identical to, or fully definable in terms of, B-properties. These are different claims: supervenience is a constraint on covariation, while reduction is a claim about identity or definability. The distinction is important because it makes non-reductive positions coherent: one can hold that moral or mental properties are fully dependent on physical properties without claiming that moral or mental descriptions are translatable into physical descriptions."
  explanation: "This is why supervenience became central to non-reductive physicalism. Philosophers wanted to avoid substance dualism (which says minds exist separately from bodies) without committing to eliminativism (which says there are no mental facts, only physical ones). Supervenience offers a middle path: mental facts are real but not fundamental — they are fully grounded in physical facts without being identical to them."
```

## Explainer

You know from your study of necessary and sufficient conditions that some facts necessitate others: if X is a necessary condition for Y, you can't have Y without X. Supervenience is a precise way of using this logical relationship to describe how different *levels* or *kinds* of properties depend on each other — without claiming that one level reduces to or is identical with the other.

The core definition: **A-properties supervene on B-properties** if and only if any two things that are indiscernible with respect to their B-properties are also indiscernible with respect to their A-properties. More simply: no A-difference without a B-difference. If mental properties supervene on physical properties, then any two beings with exactly the same physical properties must have exactly the same mental properties — you cannot change someone's beliefs or pains without changing something physical about them. This gives us a **dependence** relation: the A-level is determined by the B-level, in the sense that fixing the B-facts fixes the A-facts.

The distinction between **weak** and **strong** supervenience matters significantly. Weak supervenience holds *within* a single possible world: any two objects in the same world that share all B-properties also share all A-properties. Strong supervenience holds *across* possible worlds: if an object has A-property P in virtue of its B-properties, then any object in *any* possible world with those same B-properties also has P. Strong supervenience is logically stronger — it rules out worlds where the same B-base realizes different A-properties. For physicalism about the mind, strong supervenience is typically what's needed: it's not enough that mental duplicates are physical duplicates in our world; that should be a necessary, world-independent fact.

What makes supervenience philosophically powerful is that it allows dependence without **reduction**. Consider the relationship between aesthetic properties and physical properties. Whether a painting is beautiful arguably supervenes on its physical features — any molecule-for-molecule duplicate of the Mona Lisa would be equally beautiful. But this doesn't mean "beautiful" means the same thing as some specification of physical properties, or that aesthetic facts just are physical facts. Supervenience captures a one-way determination relation that falls short of identity. Similarly, moral properties might supervene on natural properties — no moral difference without some natural difference — without moral facts being reducible to natural facts. This is why supervenience became central to non-reductive physicalism: mental properties depend on physical properties without being identical to them.

The limits of supervenience as a philosophical tool are worth noting. Supervenience describes a *pattern* — the A-level covaries with the B-level — but it doesn't explain *why* or *how*. Saying that mental properties supervene on physical ones doesn't tell us what the metaphysical relationship is: Is it grounding? Causation? Realization? Emergence? Supervenience is compatible with many different metaphysical stories. It is a necessary condition for many forms of dependence but not sufficient to characterize any particular one. This is why philosophers increasingly supplement supervenience claims with grounding claims — "the mental is grounded in the physical" — which aim to capture the explanatory priority and the metaphysical mechanism, not just the covariation pattern.
