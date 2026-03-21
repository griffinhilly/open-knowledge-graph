---
id: property-exemplification
title: Property Exemplification and Instantiation
domain: philosophy
course: metaphysics
prerequisites:
- id: substance-and-property
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- abstract-objects
- logical-form
tags:
- properties
- exemplification
- instantiation
stage: formal-systems
status: draft
---

# Property Exemplification and Instantiation

## Core Idea
Property exemplification is the fundamental relation by which objects instantiate or possess properties. Clarifying exemplification requires understanding whether it is a primitive relation or reducible to something simpler, and whether exemplification itself counts as a property or represents a special non-relational tie.

## How It's Best Learned
Study how property attribution appears in formal logic notation, then examine self-exemplification paradoxes that arise when properties exemplify themselves and their implications for property theory.

## Common Misconceptions
Treating exemplification as merely a linguistic convention or notational device rather than a real metaphysical relation. Assuming exemplification is always asymmetric in all logical and metaphysical contexts.

## Questions

```yaml
- question: "Suppose exemplification is treated as a genuine two-place relation E that holds between object a and property F whenever a has F. What problem immediately arises?"
  type: multiple-choice
  options:
    - "It makes predication a purely linguistic matter with no metaphysical implications"
    - "It requires a further relation to connect a, F, and E — which in turn requires another relation, and so on without end (Bradley's regress)"
    - "It prevents properties from being abstract objects distinct from their instances"
    - "It makes the distinction between particulars and universals collapse"
  answer: 1
  explanation: "If exemplification is a relation, then for a to exemplify F, the relation E must hold between a and F. But relations themselves must be exemplified — so E must hold between a, F, and E via a further relation E', which requires E'' to connect E' to its relata, and so on infinitely. This is Bradley's regress. It motivates treating exemplification as a primitive non-relational tie — something that just binds object to property, with no further story to tell — rather than as a standard relation that generates new regress problems."

- question: "Consider the property P* = 'the property of not exemplifying itself.' If P* does exemplify itself, then by definition it doesn't; if it doesn't, then by definition it does. This puzzle is most closely analogous to:"
  type: multiple-choice
  options:
    - "Zeno's paradox of motion, which requires mathematical limits to resolve"
    - "Russell's paradox about the set of all sets that do not contain themselves"
    - "The sorites paradox about vague predicates and borderline cases"
    - "Hume's problem of induction about generalizing from finite observations"
  answer: 1
  explanation: "The self-exemplification paradox is a direct analogue of Russell's paradox, applied to properties rather than sets. Just as the set R = {x : x ∉ x} is contradictory (R ∈ R ↔ R ∉ R), the property P* leads to P* ∈ P* ↔ P* ∉ P*. Both paradoxes are resolved by similar means — type-theoretic restrictions that prevent unrestricted self-reference. In property theory, this means preventing properties from ranging freely over all properties, including themselves."

- question: "On a deflationary account of exemplification, the truth of 'The apple is red' is fully accounted for by the apple being red — there is no additional metaphysical relation of exemplification that further explains or grounds this fact."
  type: true-false
  answer: true
  explanation: "Deflationists hold that talk of 'exemplification' is a logical device for formal representation of predication, not a substantive metaphysical relation. On this view, asking 'what makes it the case that the apple exemplifies redness?' is a pseudo-question — the apple's being red is the basic fact, and nothing further grounds it. This contrasts with the realist view that exemplification is a genuine relation or tie that must be posited to explain object-property connections."

- question: "Because exemplification relates an object to a property, it must itself be a property — and therefore must exemplify itself."
  type: true-false
  answer: false
  explanation: "This inference is invalid on most developed accounts. Many property theorists deny that exemplification is itself a property; instead, they treat it as a primitive ontological connector — a non-relational tie — precisely to avoid regresses and paradoxes. Even those who grant that exemplification is a relation need not accept that it exemplifies itself; type-theoretic frameworks restrict self-exemplification to block the resulting paradoxes. Assuming all relations are properties, and all properties self-exemplify, leads directly to the self-exemplification paradox."

- question: "What is Bradley's regress, and why does it motivate treating exemplification as a primitive 'non-relational tie' rather than as a standard two-place relation?"
  type: short-answer
  answer: "Bradley's regress arises when exemplification is treated as a relation: a having F via relation E requires E to hold between a and F, which requires another relation E' connecting a, F, and E, which requires E'', and so on infinitely. The regress never terminates. Treating exemplification as a primitive non-relational tie — something that simply binds object to property without itself being an additional entity — stops the regress by refusing to ask 'what connects them to this connection?' The tie is not a further item in the ontology; it is just what it is for an object to have a property."
  explanation: "The non-relational tie response says: the question 'what makes a related to F by E?' is malformed — exemplification is not itself the kind of thing that gets exemplified. The cost is accepting a primitive that resists further analysis. The benefit is escaping an infinite regress that would undermine any account of object-property relations. Different metaphysical positions (trope theory, Armstrongian states of affairs, nominalism) offer different ways of resolving this tension."
```

## Explainer

From your study of substance and property you know that the world contains things that have features — objects and the characteristics they possess. A red ball has the property of redness; a charged particle has the property of charge. **Property exemplification** (or instantiation) names the fundamental relation — or whatever ties objects to their properties — that makes it true that an object "has" a property at all. Understanding exemplification means asking not just *which* properties objects have, but *what kind of fact it is* that they have them.

The simplest picture treats exemplification as a genuine two-place relation: just as "a is taller than b" involves a relation of being-taller-than holding between a and b, "a is red" involves a relation of exemplification holding between a and the property redness. In first-order logic notation, this is usually rendered as *Fa* — the predicate F is satisfied by the object a. But this logical notation is neutral about the metaphysics: does *Fa* represent a genuine relational fact? Or does something like a "non-relational tie" bind object to property without itself being another entity in the inventory? The distinction matters because relations, if they exist, themselves need to be exemplified. This is the seed of **Bradley's regress**: if a exemplifies redness via a relation R, then R must hold between a and redness, which requires another relation R' between a, R, and redness... and so on infinitely. One response is to deny that exemplification is a relation at all, treating it instead as a primitive ontological connector — the way things just are bound to their properties, with no further story to tell.

**Self-exemplification** introduces a different set of puzzles. Some properties seem to exemplify themselves: the property of being abstract is itself abstract. The property of being a property is itself a property. But now consider the property of *not exemplifying itself*. Does it exemplify itself? If it does, it doesn't (by definition). If it doesn't, it does. This is an analogue of Russell's paradox applied to properties rather than sets. The paradox forces property theorists to introduce type-theoretic restrictions (properties of objects, properties of properties-of-objects, etc.) or other constraints that prevent unrestricted self-exemplification. Getting exemplification right — knowing what it is, whether it's a relation, and which exemplification facts are permissible — turns out to be load-bearing for consistency in any systematic theory of properties.

The question also connects to the direction of explanation between predication in language and exemplification in the world. One view: sentences like "The apple is red" are true because of an underlying metaphysical fact — exemplification holding between an apple and redness. Language mirrors ontology. Another view: talk of "exemplification" is just a way of formalizing predication; there is no further fact beyond the apple being red that the notion of exemplification is tracking. On this deflationary reading, exemplification is a quasi-logical device for talking about object-property relationships, not a substantive relation requiring its own metaphysical explanation. Choosing between these positions shapes what you think property theory owes by way of explanation and what work the formal apparatus of logic is actually doing.
