---
id: counterfactual-conditionals
title: Counterfactual Conditionals and Similarity
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-logic-intro
  type: soft
builds-toward:
- temporal-semantics-and-tense
tags:
- conditionals
- modality
- counterfactuals
stage: advanced
status: draft
---

# Counterfactual Conditionals and Similarity

## Core Idea
Counterfactual conditionals are analyzed using possible worlds ordered by similarity to the actual world. A counterfactual is false when its consequent is false in the closest worlds where the antecedent is true, distinguishing them from material conditionals and strict conditionals.

## Questions

```yaml
- question: "Why does treating 'If the match had been struck, it would have turned into a fish' as a material conditional fail to capture its falsity?"
  type: multiple-choice
  options:
    - "Because material conditionals require both parts to be empirically verifiable"
    - "Because the antecedent 'the match was struck' is false in the actual world, which makes a material conditional vacuously true — so the fish conditional would come out true, which is absurd"
    - "Because material conditionals do not allow modal language"
    - "Because the consequent describes a physically impossible event"
  answer: 1
  explanation: "A material conditional is false only when its antecedent is true and its consequent is false. When the antecedent is false, the material conditional is vacuously true — regardless of the consequent. Since counterfactuals have false antecedents by definition (they describe what didn't happen), every counterfactual would be vacuously true under the material conditional analysis. This gives us 'If the match had been struck, it would have turned into a fish' as true, which is clearly wrong. The Lewis-Stalnaker closest-worlds analysis is designed precisely to avoid this vacuity, by asking what holds in nearby worlds where the antecedent is true."

- question: "Historians debate: 'If Napoleon had won at Waterloo, France would have dominated Europe for another generation.' According to the Lewis-Stalnaker analysis, how should this counterfactual be evaluated?"
  type: multiple-choice
  options:
    - "By asking whether Napoleon's character, had it been different in relevant ways, would have led to such dominance"
    - "By finding the closest possible worlds to actuality where Napoleon wins at Waterloo, and checking whether France dominates Europe in those worlds"
    - "By consulting historical experts about what the most probable outcome of a Napoleon victory would have been"
    - "By treating the conditional as equivalent to the material conditional and noting that the antecedent is false"
  answer: 1
  explanation: "The closest-worlds analysis evaluates a counterfactual by fixing the actual world as the reference point, identifying worlds where the antecedent holds (Napoleon wins at Waterloo), ordered by similarity to actuality, and checking whether the consequent holds in the nearest such worlds. The similarity ordering keeps past history largely fixed and allows the counterfactual consequence to unfold into the future from the point of divergence. Option A describes the backtracking reading — tracing back in time to what must have been different — which Lewis's account treats as non-standard."

- question: "On Lewis's account of counterfactuals, the standard reading of 'If Nixon had pressed the button, something in his past must have been different' is the preferred interpretation."
  type: true-false
  answer: false
  explanation: "This is the non-standard 'backtracking' reading of counterfactuals. Lewis's similarity ordering explicitly privileges the forward-looking reading: the closest worlds where Nixon presses the button are those where a small divergence from actual history (a 'local miracle') causes him to press it, but the past remains as it actually was. The counterfactual consequence then unfolds forward from that moment of divergence. The backtracking reading — in which we infer that something in the past must have been different to cause the pressing — is non-standard and requires special context to become the intended interpretation."

- question: "Counterfactual conditionals play a central role in the philosophical analysis of causation, not just in the semantics of modal language."
  type: true-false
  answer: true
  explanation: "Counterfactual theories of causation analyze 'C caused E' as 'if C had not occurred, E would not have occurred.' This makes the semantics of counterfactuals directly relevant to the metaphysics of causation. The same analysis underlies the distinction between laws of nature and accidental regularities: a genuine law supports counterfactuals (if this were copper, it would conduct electricity) in a way that an accidental generalization does not. So the machinery of possible-worlds semantics for counterfactuals is not a philosophical curiosity — it underpins fundamental questions in metaphysics and the philosophy of science."

- question: "What work does the notion of 'world similarity' do in the Lewis-Stalnaker analysis of counterfactuals, and why is it philosophically controversial?"
  type: short-answer
  answer: "World similarity is the ordering relation that determines which possible worlds are 'closest' to actuality when evaluating a counterfactual. A counterfactual 'If P, then Q' is true if Q holds in the closest worlds where P is true. Similarity does the work of distinguishing good counterfactuals from bad ones — it explains why 'the match would have lit' is true but 'the match would have become a fish' is false, even though both have false antecedents. It is controversial because 'similarity' between possible worlds is not a natural or unambiguous notion: Lewis had to impose a complex priority ordering (match of laws, then match of particular facts) to avoid counterintuitive results, and critics argue this ordering is ad hoc or itself depends on causal intuitions, making the analysis partly circular."
  explanation: "The core philosophical worry is that world-similarity is doing enormous theoretical work but is not independently well-defined. Lewis tried to formalize it using a hierarchy: large violations of actual laws make a world farther; matching particular facts matters but less than matching laws; small 'miracles' confined to the antecedent event are tolerated. But why should this ordering reflect genuine metaphysical closeness? And why does it produce the right temporal asymmetry (forward, not backtracking)? Critics argue that Lewis's similarity ordering was reverse-engineered to match our pre-theoretical judgments about counterfactuals, rather than providing an independent analysis. This is a live dispute in the semantics and metaphysics of modality."
```

## Explainer

From your study of possible worlds semantics you know that modal claims — claims about what is possible, necessary, or contingent — are analyzed in terms of how things stand across different ways the world could be. A **counterfactual conditional** like "If the match had been struck, it would have lit" is a claim about what would have been true in a situation that did not actually occur. The antecedent ("the match was struck") is false in the actual world. The conditional is asking: in scenarios where that false antecedent was true instead, what else would have been true?

The problem with the **material conditional** analysis familiar from propositional logic is that a material conditional is simply false when its antecedent is false — which means all counterfactuals would be vacuously true (since their antecedents are false). But "If the match had been struck, it would have turned into a fish" is not true. We need an account that distinguishes good counterfactuals from bad ones. Robert Stalnaker and David Lewis independently developed the **closest-worlds** analysis: a counterfactual "If P had been the case, Q would have been the case" is true just in case Q holds in the closest possible worlds to the actual world where P is true. The match-would-light counterfactual is true because in the nearest worlds where the match is struck (dry conditions, oxygen present, not on Pluto) it lights. The match-would-become-a-fish counterfactual is false because even in nearby worlds where it is struck, fish don't appear.

The notion of **world-similarity** — what makes one possible world "closer" to actuality than another — does the main work and is the main source of debate. Lewis argued for a set of priorities: large-scale violations of actual laws of nature make a world less similar than small "miracles" confined to the antecedent event; then comes overall match of particular fact across history; then exact match of laws. This gives counterfactuals an asymmetry of time: "If Nixon had pressed the button, there would have been nuclear war" is evaluated by looking forward from the moment of pressing, not backward. The past remains as it was; the counterfactual consequence unfolds into the future. A **backtracking** reading — "If Nixon had pressed the button, something in his past must have been different to make him do so" — is non-standard, and Lewis's similarity ordering explains why.

Counterfactuals are not merely a semantic curiosity. They underpin the analysis of **causation**: on counterfactual theories, C caused E just in case if C had not occurred, E would not have occurred. They also figure centrally in scientific and practical reasoning: a law of nature supports counterfactuals in a way that an accidental regularity does not. "All copper conducts electricity" supports "If this penny were copper, it would conduct electricity"; "All coins in my pocket are copper" does not support the same form of reasoning about coins generally. The distinction between laws and accidents, between causal and non-causal regularities, and between robust and fragile generalizations all cash out, in part, in terms of which counterfactuals are supported.
