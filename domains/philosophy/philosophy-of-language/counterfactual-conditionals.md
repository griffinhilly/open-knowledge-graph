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

## Explainer

From your study of possible worlds semantics you know that modal claims — claims about what is possible, necessary, or contingent — are analyzed in terms of how things stand across different ways the world could be. A **counterfactual conditional** like "If the match had been struck, it would have lit" is a claim about what would have been true in a situation that did not actually occur. The antecedent ("the match was struck") is false in the actual world. The conditional is asking: in scenarios where that false antecedent was true instead, what else would have been true?

The problem with the **material conditional** analysis familiar from propositional logic is that a material conditional is simply false when its antecedent is false — which means all counterfactuals would be vacuously true (since their antecedents are false). But "If the match had been struck, it would have turned into a fish" is not true. We need an account that distinguishes good counterfactuals from bad ones. Robert Stalnaker and David Lewis independently developed the **closest-worlds** analysis: a counterfactual "If P had been the case, Q would have been the case" is true just in case Q holds in the closest possible worlds to the actual world where P is true. The match-would-light counterfactual is true because in the nearest worlds where the match is struck (dry conditions, oxygen present, not on Pluto) it lights. The match-would-become-a-fish counterfactual is false because even in nearby worlds where it is struck, fish don't appear.

The notion of **world-similarity** — what makes one possible world "closer" to actuality than another — does the main work and is the main source of debate. Lewis argued for a set of priorities: large-scale violations of actual laws of nature make a world less similar than small "miracles" confined to the antecedent event; then comes overall match of particular fact across history; then exact match of laws. This gives counterfactuals an asymmetry of time: "If Nixon had pressed the button, there would have been nuclear war" is evaluated by looking forward from the moment of pressing, not backward. The past remains as it was; the counterfactual consequence unfolds into the future. A **backtracking** reading — "If Nixon had pressed the button, something in his past must have been different to make him do so" — is non-standard, and Lewis's similarity ordering explains why.

Counterfactuals are not merely a semantic curiosity. They underpin the analysis of **causation**: on counterfactual theories, C caused E just in case if C had not occurred, E would not have occurred. They also figure centrally in scientific and practical reasoning: a law of nature supports counterfactuals in a way that an accidental regularity does not. "All copper conducts electricity" supports "If this penny were copper, it would conduct electricity"; "All coins in my pocket are copper" does not support the same form of reasoning about coins generally. The distinction between laws and accidents, between causal and non-causal regularities, and between robust and fragile generalizations all cash out, in part, in terms of which counterfactuals are supported.
