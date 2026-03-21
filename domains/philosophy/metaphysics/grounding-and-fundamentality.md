---
id: grounding-and-fundamentality
title: Grounding and Fundamentality
domain: philosophy
course: metaphysics
prerequisites:
- id: ontological-categories
  type: hard
- id: facts-and-truthmakers
  type: soft
- id: logical-consequence-and-validity
  type: soft
tags:
- grounding
- fundamentality
- Fine
- dependence
- metaphysical explanation
stage: formal-systems
status: draft
---

# Grounding and Fundamentality

## Core Idea
Grounding is a relation of metaphysical determination: when we say the mental is grounded in the physical, or the moral in the natural, we mean that the former holds in virtue of the latter. Kit Fine, Gideon Rosen, and others have argued that grounding is a distinctive relation — irreflexive, asymmetric, transitive — that carves out a hierarchy of metaphysical priority distinct from both causation and supervenience. Fundamentality is the bottom of this hierarchy: the fundamental facts are those not grounded in anything further. The grounding framework promises to unify disparate debates — physicalism, mathematical ontology, normativity — under a single structural question: what is prior to what? Critics question whether grounding is a single unified relation or a grab-bag of heterogeneous dependencies.

## How It's Best Learned
Read Fine's 'Guide to Ground' for the formal framework, then Schaffer's 'On What Grounds What' for the picture of metaphysics as a discipline studying grounding structure rather than existence. Compare grounding with supervenience and ask what explanatory work grounding does that supervenience cannot.

## Common Misconceptions
- Grounding is not causation — it is a synchronic, constitutive relation, not a diachronic productive one.
- Saying one fact grounds another does not mean the grounded fact is unreal; grounded facts are fully real, just non-fundamental.

## Questions

```yaml
- question: "A physicalist claims that mental facts are grounded in physical facts. What does this claim add that 'mental facts supervene on physical facts' does not?"
  type: multiple-choice
  options:
    - "The grounding claim adds that mental facts are identical to physical facts, whereas supervenience allows them to be distinct"
    - "The grounding claim asserts that physical facts are explanatorily prior — mental facts obtain because of physical facts — whereas supervenience only asserts co-variation without explanation or direction"
    - "The grounding claim is weaker than supervenience, applying only to some mental facts while supervenience applies to all"
    - "Grounding and supervenience are equivalent; the distinction is merely terminological"
  answer: 1
  explanation: "Supervenience says mental facts can't differ without physical facts differing — a correlation. But you could have systematic supervenience with no explanatory relation (both might depend on a third thing, or it might be brute coincidence). Grounding asserts asymmetric explanatory priority: the physical facts are why the mental facts hold. This directional, 'in virtue of' content is exactly what supervenience lacks and what physicalists actually mean to claim."

- question: "The grounding relation is irreflexive, asymmetric, and transitive. Which scenario would violate these formal properties?"
  type: multiple-choice
  options:
    - "The fact that a surface is red is grounded in facts about its surface molecules and how they interact with light"
    - "Moral fact F is grounded in natural fact N, and N is grounded in microphysical fact M, so F is also grounded in M (by transitivity)"
    - "The fact that water is liquid is grounded in its molecular arrangement, and the molecular arrangement is partly grounded in the fact that the water is liquid"
    - "Mathematical facts are not grounded in physical facts, forming an independent hierarchy"
  answer: 2
  explanation: "Scenario C creates a grounding circle: if A grounds B and B grounds A, the relation is symmetric — violating asymmetry. By transitivity, if liquidity grounds the arrangement and the arrangement grounds liquidity, then liquidity would ground itself — violating irreflexivity. Grounding must be a strict partial ordering (irreflexive, asymmetric, transitive) to make the concept of a hierarchy of metaphysical priority coherent."

- question: "If a fact is grounded in another fact, the grounded fact is less real or merely apparent — it has diminished ontological status compared to the fundamental fact that grounds it."
  type: true-false
  answer: false
  explanation: "This is a central misconception about grounding. Grounded facts are fully real — grounding is not an ontological demotion. The fact that a surface is red is fully real even if it is grounded in facts about wavelengths and neural responses. Grounding describes priority within reality, not degrees of reality. The physical facts being more fundamental than mental facts doesn't make mental facts illusory — it just tells us which facts depend on which."

- question: "Grounding is distinct from causation because grounding is a synchronic, constitutive relation while causation is a diachronic, productive one."
  type: true-false
  answer: true
  explanation: "Causation is temporal: the cause precedes the effect and produces it over time. Grounding is not temporal: the molecular arrangement of water doesn't cause it to be liquid at some later time — the liquidity obtains simultaneously, constituted by the arrangement. You can ask 'what caused the fire?' but grounding asks 'what is the fire's existence in virtue of?' — a different question entirely. This distinction explains why physicalism is not a causal thesis and why grounding counts as metaphysical, not natural, explanation."

- question: "Why do philosophers introduce the concept of grounding rather than relying on supervenience to capture 'in virtue of' relations like physicalism?"
  type: short-answer
  answer: "Supervenience only captures co-variation: if mental facts supervene on physical facts, the two can't come apart. But supervenience is compatible with the mental and physical co-varying for any reason — both depending on a third thing, or through brute necessity with no explanatory relation. Grounding adds directionality and explanation: the physical facts are prior, and the mental facts hold because of them. This 'because of' is what physicalists actually mean — not just that they co-vary, but that the physical level explains and determines the mental level. Grounding makes this explanatory priority formal and tractable."
  explanation: "The philosophical payoff of grounding over supervenience is exactly this explanatory content. Many debates in philosophy of mind, ethics, and mathematics are really debates about what grounds what — supervenience alone is too weak to capture the claim being made."
```

## Explainer

You come to this topic with a grasp of ontological categories — what kinds of things exist — and likely some exposure to truthmakers and logical consequence. Grounding asks a different question from any of these: not "what exists?" but "what is prior to what?" or "what explains what, in a non-causal, constitutive sense?" This is the relation Kit Fine called **metaphysical determination**: the fact that a whole is composed of parts doesn't cause the whole to exist in a temporal sense, but the parts' arrangement *grounds* the whole's existence — it's in virtue of the parts being arranged this way that the whole is what it is.

The formal features of grounding help clarify what it is. The relation is **irreflexive** (nothing grounds itself), **asymmetric** (if A grounds B, then B does not ground A), and **transitive** (if A grounds B and B grounds C, then A grounds C). This gives us a strict partial ordering — a hierarchy running from grounded facts up to fundamental ones. These features distinguish grounding sharply from causation, which can be symmetric (mutual causation) and certainly doesn't ground — the fire that causes the smoke doesn't constitute the smoke in the way that the molecular arrangement of water constitutes its liquidity. Grounding is always synchronic and constitutive; causation is diachronic and productive.

Why introduce grounding at all? Consider the physicalist claim that mental facts hold "in virtue of" physical facts. **Supervenience** captures a correlation — mental facts can't differ without physical facts differing — but it says nothing about explanation or priority. You could have systematic supervenience without any explanatory relation: maybe mental and physical facts co-vary because both depend on something third. **Grounding** asserts the stronger claim: the physical facts are explanatorily prior; the mental facts obtain because of them. Similarly for moral facts and natural facts: the Humean might say that an act being wrong is grounded in its causing unnecessary suffering, not merely that the two co-vary. Grounding gives structure to these "in virtue of" claims that supervenience alone cannot provide.

**Fundamentality** is the limiting case: a fact is fundamental if it is not grounded in anything further. Most metaphysicians locate fundamentality in physics, though this is contested — perhaps mathematical or logical facts are fundamental in a different sense, or perhaps there are multiple independent grounding hierarchies. The framework promises to unify disparate philosophical debates under one structural question: whatever you think is real, how is it ordered? What rests on what? The main challenge critics raise is whether "grounding" names a single unified relation or a family of loosely related explanatory relations — metaphysical, causal, logical, conceptual — that don't really share the formal properties claimed. Engaging with this challenge requires knowing the formal framework well enough to test it against cases.
