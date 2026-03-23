---
id: unificationist-theories-of-explanation
title: Unificationist Theories of Explanation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: scientific-explanation-introduction
  type: soft
builds-toward:
- theoretical-virtues-in-theory-choice
tags:
- explanation
- unification
- understanding
stage: expert
status: draft
---

# Unificationist Theories of Explanation

## Core Idea
Unificationism proposes that explanation consists in reducing the number of independent assumptions needed to understand a body of phenomena. A good explanation unifies disparate phenomena under common principles, making them appear intelligible together rather than as separate, disconnected facts.

## Questions

```yaml
- question: "Newton showed that both terrestrial mechanics (falling apples) and celestial mechanics (planetary orbits) follow from the same inverse-square law. What does this example illustrate about unificationist explanation?"
  type: multiple-choice
  options:
    - "Explanation requires identifying the causal mechanism by which gravity acts at a distance"
    - "Explanation consists in deriving phenomena from initial conditions plus laws, regardless of how many laws are used"
    - "Explanatory value comes from reducing two previously independent explanatory resources to one — showing disparate phenomena follow from a common principle"
    - "The more mathematically complex the derivation, the deeper the explanation"
  answer: 2
  explanation: "The Newtonian case is the paradigm of unificationist explanation: before the Principia, terrestrial and celestial mechanics required separate explanatory resources. Afterward, one law covers both. The phenomena become 'intelligible together' in a way they were not before — that reduction of independent assumptions is the locus of explanatory power. This is different from the DN model (which would count any valid derivation as explanatory) and from causal-mechanical accounts (which require citing mechanisms)."

- question: "How does Kitcher's argument-pattern account differ from Hempel's covering-law (DN) model?"
  type: multiple-choice
  options:
    - "Kitcher denies that laws play any role in explanation; Hempel requires derivation from laws"
    - "For Kitcher, only derivations belonging to the maximally unified system of argument patterns are explanatory; for Hempel, any valid deduction from laws and initial conditions counts"
    - "Hempel's model applies to quantitative sciences; Kitcher's applies only to qualitative ones"
    - "Kitcher requires citing causal mechanisms; Hempel does not"
  answer: 1
  explanation: "Hempel: explanation = valid deduction from laws plus initial conditions. Kitcher: explanation = derivation that belongs to the set of argument patterns that minimizes independent principles needed to cover all phenomena. A valid derivation using an isolated, non-generalizing pattern does not explain on Kitcher's view, even if it's logically correct and uses true laws. Explanatory power comes from system-level unification, not from properties of individual derivations."

- question: "According to unificationism, subsuming an event under a general regularity (e.g., 'humans are mortal, so this person died') provides a fully satisfying explanation of why that particular event occurred."
  type: true-false
  answer: false
  explanation: "This is the standard objection to unificationism: subsumption under a regularity may not answer the actual explanatory question. What we want to know is why this person died this way — the causal mechanism. Unificationists have responses (mechanistic explanation works by showing biological processes are special cases of physics/chemistry, which is itself unification), but they acknowledge that simple mortality-subsumption is the kind of case where the causal-mechanical intuition is strongest."

- question: "Most philosophers of science now hold that unificationist and causal-mechanistic accounts are complementary frameworks, each capturing something real about scientific explanation."
  type: true-false
  answer: true
  explanation: "The debate between unificationism and causal-mechanistic explanation has been productive rather than conclusive. Unificationism captures why Newton's laws and Maxwell's equations feel deeply explanatory; causal-mechanistic accounts capture why citing mechanisms seems to answer 'why' questions more directly. Current consensus is that both frameworks are partial, and that a complete theory of scientific explanation will need to incorporate both dimensions."

- question: "Why does the flagpole/shadow asymmetry problem for the DN model motivate the unificationist approach? Use this example to explain what unificationism adds."
  type: short-answer
  answer: "The DN model counts any valid deduction from laws as an explanation. But you can derive the height of a flagpole from the length of its shadow (given sun angle and laws of optics) just as validly as you can derive the shadow from the pole height — yet only one direction seems explanatory. Unificationism addresses this by grounding explanation in system-level properties: the argument pattern 'derive shadow length from object height and solar geometry' is part of the maximally unified system because it covers a wide range of cases; the reverse is not. Explanatory direction is determined by which argument patterns belong to the best unified systematization of science, not by the logic of individual derivations."
  explanation: "The asymmetry problem shows that valid derivation from laws is not sufficient for explanation. Unificationism locates the additional constraint in the overall system: not all valid derivations are explanatory, only those belonging to the unified core."
```

## Explainer

When you study scientific explanation, the central question is: what makes an explanation genuinely explanatory, rather than a mere redescription of the phenomenon? The **deductive-nomological** model (Hempel) said that an explanation is a valid deduction from laws plus initial conditions. But this faces problems — deriving the length of a shadow from the height of a flagpole "explains" the height just as well as vice versa, yet one direction feels explanatory and the other doesn't. Unificationism offers a different answer: the best explanations are those that reduce the number of independent principles needed to understand a body of phenomena.

The classic illustration is Newton. Before the Principia, terrestrial mechanics (why apples fall) and celestial mechanics (why planets orbit) were two separate bodies of knowledge, explained by different principles. Newton showed that both follow from the same inverse-square law of gravitation. After Newton, you no longer need two independent explanatory resources — one set of principles covers both. This is the **unification** that makes the Newtonian achievement feel like a deep explanation rather than a mere redescription. The phenomena are intelligible together in a way they were not before.

**Kitcher's argument pattern account** is the most developed version of unificationism. On Kitcher's view, science aims to reduce the number of **argument patterns** — schemata for deriving explananda from premises — to the minimum needed to account for all phenomena. A science that uses five argument patterns to cover 1,000 phenomena is doing better than one that uses 100 patterns to cover the same phenomena. The explanatory power comes from the generality of the patterns, not the logical properties of any single derivation. This is importantly different from the covering-law model: for Hempel, any derivation from laws counts as explanation; for Kitcher, only derivations that belong to the system's maximally unified set of argument patterns count.

The most important competitor to unificationism is **causal-mechanistic explanation**: the view that genuine explanation requires citing the causes and mechanisms that produce the explanandum, not merely subsuming it under a unifying pattern. Critics of unificationism point out that there are cases where subsumption under a general pattern does not feel explanatory. The classic case: we can formally "explain" why someone died by deriving their death from general regularities about human mortality — but this does not tell us why *this* person died *this* way. What we want is the causal mechanism. Unificationists respond that mechanical explanations work precisely by revealing that biological processes are special cases of chemical and physical processes — which is itself a form of unification. The debate between unificationism and causal-mechanical accounts has driven much of the philosophy of explanation for the past three decades, with most philosophers now thinking both frameworks capture something real about scientific understanding.
