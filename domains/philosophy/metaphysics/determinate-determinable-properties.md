---
id: determinate-determinable-properties
title: Determinate and Determinable Properties
domain: philosophy
course: metaphysics
prerequisites:
- id: properties-intrinsic-extrinsic
  type: hard
- id: substance-and-property
  type: soft
builds-toward:
- fundamental-properties-sparse-abundant
- first-order-higher-order-properties
tags:
- properties
- determinates
- determinables
stage: formal-systems
status: draft
---

# Determinate and Determinable Properties

## Core Idea
Properties exist at different levels of specificity: determinable properties are general categories (like color) while determinate properties are specific instances (like crimson red). Understanding this distinction proves crucial for metaphysical theories of properties and predication, as causes typically cite determinate rather than determinable properties.

## How It's Best Learned
Compare concrete color examples—analyze how specific hues relate to general color categories—and work through why this distinction matters for causal explanation and property attribution.

## Common Misconceptions
Treating determinables and determinates as entirely separate properties rather than as different levels of generality. Confusing this distinction with the type/token distinction or with the distinction between abstract and concrete properties.

## Questions

```yaml
- question: "A rose is crimson. How does the determinate/determinable framework describe the relationship between 'crimson' and 'colored'?"
  type: multiple-choice
  options:
    - "Crimson and colored are entirely separate, unrelated properties that happen to co-occur"
    - "Crimson is a determinate of the determinable 'colored' — a maximally specific instance of the general property"
    - "Colored is a determinate of crimson — a broader version of a more specific property"
    - "Crimson and colored are the same property, just described at different levels of linguistic abstraction"
  answer: 1
  explanation: "Crimson is a specific shade — a determinate — that instantiates the more general determinable 'colored.' The relationship is hierarchical: being crimson necessarily entails being colored (you can't be crimson without being colored), but being colored does not determine which color (you could be crimson, cerulean, or any other shade). Note that 'red' sits in between: it's a determinable relative to crimson but a determinate relative to colored. The hierarchy runs from most general to most specific."

- question: "A philosopher argues that 'color' is just shorthand for the disjunctive property 'is crimson OR is cerulean OR is scarlet OR …' — that determinables reduce to disjunctions of their determinates. What is the best objection?"
  type: multiple-choice
  options:
    - "This is correct — determinables are just convenient abbreviations for long disjunctions"
    - "Determinables cannot be defined at all since there are infinitely many possible determinates"
    - "The disjunction analysis fails because having 'color' is not merely having one or more options from a list — it means having some fully specific shade, and the determinates under a determinable are mutually exclusive in a way that a bare disjunction does not capture"
    - "The disjunction analysis works, but only for color; other determinables like shape or mass resist it"
  answer: 2
  explanation: "The mutual exclusivity of determinates is the key problem for the disjunction analysis. A thing can instantiate only one determinate per determinable at a time — an object cannot be both crimson and cerulean simultaneously. A bare disjunction (A OR B OR C) doesn't capture this exclusivity; it would allow all three to be true at once. Moreover, determinables carry structure that mere disjunctions lack: the determinates are organized along a dimension of variation (hue, in the case of color) with a specific incompatibility built in. This structure is why 'determinable' is a distinct metaphysical category, not just an abbreviation."

- question: "If an object instantiates the determinate property 'scarlet,' it necessarily also instantiates the determinable property 'colored.'"
  type: true-false
  answer: true
  explanation: "This is the fundamental logical relationship between determinates and determinables: instantiating a determinate entails instantiating the corresponding determinable. Being scarlet is a way of being colored, so any scarlet object is also colored — by necessity, not contingency. The reverse does not hold: being colored does not determine which color. This one-way entailment (determinate → determinable, but not vice versa) defines the determinate/determinable relationship."

- question: "A single object can instantiate two different determinates of the same determinable at the same time — for example, being both crimson and cerulean simultaneously."
  type: true-false
  answer: false
  explanation: "Mutual exclusivity of co-instantiation is a defining feature of determinates under a common determinable. A thing can have exactly one determinate per determinable at any moment. This incompatibility is metaphysically necessary, not just empirically observed: it's built into the structure of the determinable. This is precisely why determinables can't be reduced to disjunctions — a disjunction would permit multiple disjuncts to be true simultaneously, but the determinate/determinable structure forbids it."

- question: "Why do philosophers of causation typically hold that causes must cite determinate rather than determinable properties?"
  type: short-answer
  answer: "Causes must cite the specific properties that actually made the difference — the determinate level of description. A highly determinable description (e.g., 'sound caused the heart attack') underdetermines the causal mechanism: many different sounds with different frequencies, volumes, and timing would satisfy 'sound,' but only the specific determinate properties of this particular sound did the causal work. Citing only the determinable leaves open the question of what specifically caused the effect. Moreover, if causes were determinable, we'd face a problem of causal overdetermination: both the determinable property and its specific determinate property would each cause the same effect, which is metaphysically problematic."
  explanation: "The connection to causal exclusion debates is central here. In philosophy of mind, if mental states are determinable descriptions of more determinate neural states, the worry is that the mental level never actually causes anything — the more determinate physical level always does the real causal work. This is why the determinate/determinable distinction matters beyond abstract metaphysics: it structures debates about whether higher-level properties (psychological, biological, social) can be genuinely causally efficacious."
```

## Explainer

From intrinsic and extrinsic properties, you know that properties can be categorized by their dependence on other things — whether a property belongs to an object in isolation or only in relation to something else. The **determinate/determinable distinction** cuts along a different axis entirely: it organizes properties by their **level of specificity**. Rather than a flat list of properties, properties form hierarchies from the general to the particular, and understanding where a property sits in this hierarchy matters for both metaphysics and the theory of causation.

A **determinable** is a general property that can be realized in multiple, more specific ways. **Color** is a paradigm determinable: it can be realized as red, blue, green, and so on. **Red** is itself a determinable relative to its own determinates — crimson, scarlet, vermilion are all more specific reds. A **determinate** is a fully specific way of instantiating a determinable — a particular shade that cannot be further refined within that dimension of variation. The key logical feature of this relationship: if something instantiates a determinate, it necessarily instantiates the corresponding determinable (being crimson entails being colored), but the reverse does not hold (being colored does not determine which color).

There is a striking constraint on how determinates relate to each other: **a thing can instantiate only one determinate under a given determinable at a time**. An object can be crimson or cerulean but not both simultaneously — those are incompatible determinates of color. This incompatibility is not merely empirical (it happens to be that way) but metaphysically necessary (it's built into the nature of the determinable structure). This is why determinables aren't reducible to disjunctions of their determinates: having "color" doesn't mean having crimson OR cerulean OR scarlet as a disjunctive property; it means having some fully specific color, exactly one.

The determinate/determinable distinction connects directly to questions about **causal explanation**. When something happens — a ball breaks a window — what is the causally relevant description of the event? The window-breaking was caused by impact: but was the cause "physical contact" (a highly determinable description) or "the specific force, angle, and material properties of the ball" (a much more determinate one)? Philosophers of causation generally argue that **causes are determinate events**, not determinable ones. If a doctor's loud shout startled a patient with a heart condition, what caused the heart attack — "sound" (determinable) or the specific decibels, frequency, and shock of that particular shout (determinate)? The distinction structures debates about causal exclusion, mental causation, and the question of whether higher-level properties (like psychological states) can genuinely cause anything when more determinate physical properties are always available.
