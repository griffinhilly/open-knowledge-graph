---
id: cross-world-identity-principles
title: Cross-World Identity and Counterpart Theory
domain: philosophy
course: metaphysics
prerequisites:
- id: modal-realism
  type: hard
- id: possible-worlds-semantics
  type: hard
- id: identity-of-indiscernibles
  type: soft
builds-toward:
- modal-status-identity-statements
- rigid-designators-modal-reference
tags:
- modality
- identity
- possible-worlds
stage: advanced
status: draft
---

# Cross-World Identity and Counterpart Theory

## Core Idea
Cross-world identity principles specify which objects in different possible worlds are the same object. Approaches include essentialist principles (identity preserves essential properties), counterpart theory (objects related by similarity without strict identity), and direct identity (identity is primitive across worlds). These choices fundamentally affect modal semantics and metaphysics.

## How It's Best Learned
Compare theories' handling of modal intuitions about identity: must an object have all its actual properties in every world where it exists? Can an object be different in essential ways across worlds while remaining identical?

## Common Misconceptions
Assuming direct identity across worlds is obviously correct without argument. Thinking the debate is purely semantic rather than substantive for modal metaphysics and the metaphysics of modality.

## Questions

```yaml
- question: "On Lewis's counterpart theory, when we say 'Aristotle could have been a carpenter,' what are we actually saying?"
  type: multiple-choice
  options:
    - "Aristotle himself exists in some possible world where he chose to become a carpenter instead of a philosopher"
    - "There is a possible world containing an individual sufficiently similar to Aristotle who is a carpenter"
    - "In all possible worlds, Aristotle has the potential to have been a carpenter"
    - "The actual Aristotle has the hidden dispositional property of being a possible carpenter"
  answer: 1
  explanation: "On Lewis's counterpart theory, all objects are world-bound — no individual exists in more than one world. When we say Aristotle could have been a carpenter, we are not saying Aristotle himself exists elsewhere as a carpenter. Instead, we are saying some other-world individual who resembles Aristotle sufficiently closely (in the relevant respects) is a carpenter. The 'could have been' is not about Aristotle-in-another-world but about Aristotle's counterpart in another world. This is a substantive metaphysical difference: what is possible for Aristotle depends on the facts about how similar other-world individuals are to him."

- question: "Direct identity theory faces a challenge from Leibniz's Law. What is that challenge?"
  type: multiple-choice
  options:
    - "If Nixon is identical across worlds, he must share all properties in all worlds — but he has 'winning in the actual world' and 'losing in some other world,' which seem to conflict"
    - "Leibniz's Law implies that any two possible worlds containing 'Nixon' must contain numerically identical objects, making counterpart theory impossible"
    - "Two objects can only be identical if they exist at the same spatiotemporal location, so trans-world identity is geometrically impossible"
    - "Leibniz's Law implies all identical objects are indiscernible, but possible worlds clearly differ from each other, so nothing can be shared"
  answer: 0
  explanation: "Leibniz's Law states that if A = B, then A and B share all properties. If Nixon is the same individual across worlds, he seems to have both 'winning the 1968 election' (true at the actual world) and 'losing the 1968 election' (true at some other world) — which look contradictory. The standard response is to relativize properties to worlds: Nixon has 'winning at α' and 'losing at w,' which don't conflict. But counterpart theorists see this relativization as problematic, and prefer to simply deny that Nixon exists at multiple worlds at all."

- question: "On Lewis's counterpart theory, the same individual object can exist in multiple possible worlds simultaneously."
  type: true-false
  answer: false
  explanation: "Counterpart theory holds precisely the opposite: all objects are world-bound, existing in exactly one possible world. This is a defining feature that distinguishes counterpart theory from direct identity theory. When we make modal claims about an individual, counterpart theory analyzes them in terms of other-world individuals who resemble the actual individual sufficiently closely. No individual 'travels' between worlds — only counterpart relations hold between world-bound individuals."

- question: "The choice between direct identity and counterpart theory has substantive consequences for what essential properties an object has."
  type: true-false
  answer: true
  explanation: "On direct identity theory, an object's essential properties are those it has in every world where it exists. On counterpart theory, essence is defined in terms of what all counterparts share. These analyses can diverge: whether you could have had different parents, or been made of different matter, may receive different verdicts depending on which framework is used, because the counterpart relation is context-sensitive and can be defined in terms of different respects of similarity. The theories are not merely terminological variants."

- question: "Why does counterpart theory make modal claims 'covertly relational,' and what does this mean for the objectivity of claims like 'I could have been taller'?"
  type: short-answer
  answer: "On counterpart theory, 'I could have been taller' means there exists a world containing an individual sufficiently similar to me who is taller. What counts as 'sufficiently similar' depends on context — which respects of similarity are salient. In a context emphasizing physical constitution, physical similarity dominates; in one emphasizing psychological continuity, mental properties dominate. The modal claim is therefore relational: true relative to one contextually specified counterpart relation, potentially false relative to another. This makes de re modal claims partly context-dependent rather than objective facts about the individual simpliciter."
  explanation: "This is one of the main costs of counterpart theory that critics press. Direct identity theory makes 'I could have been taller' simply a claim about whether I myself exist at some world where I am taller — a fact about me and the worlds. Counterpart theory replaces this with a claim about other-world individuals and a context-sensitive similarity relation. Whether a given modal claim is true can shift with conversational context, which some find implausible. Lewis accepted this consequence; he argued that the context-sensitivity is a feature of our modal talk, not a defect of the theory."
```

## Explainer

You know from possible-worlds semantics that modal claims—claims about what could or must be the case—are analyzed in terms of possible worlds: "possibly P" is true if P holds at some possible world, "necessarily P" if P holds at every world. And from modal realism you know that David Lewis treats possible worlds as genuine, concrete spatiotemporal realities comparable to our own. Once you accept a plurality of concrete worlds, a new question immediately arises: when we say "this very chair could have been red instead of green," are we saying something about *this exact chair* existing in another world with different properties, or about a *different but similar* chair in that world? This is the problem of **cross-world identity**.

The most intuitive view is **direct identity**: objects literally exist in multiple possible worlds, and when we say Nixon could have lost the election, we are talking about Nixon himself—the very same individual—in a world where the election went differently. This view requires that objects be **trans-world individuals**, numerically identical across distinct worlds. The problem is that Leibniz's Law (if A and B are identical, they share all properties) seems to threaten this: Nixon has the property *actually winning the 1968 election* and also the property *possibly losing the 1968 election*. These look like contradictory properties unless we are very careful about how to characterize them (typically by relativizing properties to worlds: Nixon has *winning at the actual world* and *losing at some other world*, which don't conflict).

David Lewis rejected direct identity in favor of **counterpart theory**. On his view, no individual exists in more than one possible world; all objects are world-bound. When we say Nixon could have lost, we are not saying Nixon himself exists in another world and loses there—we are saying that Nixon has a **counterpart** in some other world who loses. A counterpart is an individual in another world who resembles the actual individual sufficiently closely in the relevant respects. What counts as "relevant respects" is context-sensitive: in a modal context about political careers, political similarity matters; in a context about physical constitution, physical similarity matters. Counterpart theory has the advantage of keeping objects metaphysically tidy (each exists only once, in one world) at the cost of treating modal claims as covertly relational—what is possible for you depends on the facts about your counterparts elsewhere.

The choice between direct identity and counterpart theory has downstream effects on how you analyze **de re** modal claims—claims about what a specific individual could or must be. "Aristotle could have been a carpenter" means different things on the two theories: for direct identity, Aristotle-himself exists in some world as a carpenter; for counterpart theory, some sufficiently similar individual is a carpenter in some world. The theories also differ on **essential properties**: if direct identity is right, the essential properties of an object are those it has in every world where it exists. Counterpart theory redefines essence in terms of what all counterparts share. This matters for debates about whether material constitution or origin is essential to an object—the question of whether you could have had different parents, or been made of different matter, gets different traction depending on which framework you use.
