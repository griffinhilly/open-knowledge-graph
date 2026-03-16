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

## Explainer

From your study of substance and property you know that the world contains things that have features — objects and the characteristics they possess. A red ball has the property of redness; a charged particle has the property of charge. **Property exemplification** (or instantiation) names the fundamental relation — or whatever ties objects to their properties — that makes it true that an object "has" a property at all. Understanding exemplification means asking not just *which* properties objects have, but *what kind of fact it is* that they have them.

The simplest picture treats exemplification as a genuine two-place relation: just as "a is taller than b" involves a relation of being-taller-than holding between a and b, "a is red" involves a relation of exemplification holding between a and the property redness. In first-order logic notation, this is usually rendered as *Fa* — the predicate F is satisfied by the object a. But this logical notation is neutral about the metaphysics: does *Fa* represent a genuine relational fact? Or does something like a "non-relational tie" bind object to property without itself being another entity in the inventory? The distinction matters because relations, if they exist, themselves need to be exemplified. This is the seed of **Bradley's regress**: if a exemplifies redness via a relation R, then R must hold between a and redness, which requires another relation R' between a, R, and redness... and so on infinitely. One response is to deny that exemplification is a relation at all, treating it instead as a primitive ontological connector — the way things just are bound to their properties, with no further story to tell.

**Self-exemplification** introduces a different set of puzzles. Some properties seem to exemplify themselves: the property of being abstract is itself abstract. The property of being a property is itself a property. But now consider the property of *not exemplifying itself*. Does it exemplify itself? If it does, it doesn't (by definition). If it doesn't, it does. This is an analogue of Russell's paradox applied to properties rather than sets. The paradox forces property theorists to introduce type-theoretic restrictions (properties of objects, properties of properties-of-objects, etc.) or other constraints that prevent unrestricted self-exemplification. Getting exemplification right — knowing what it is, whether it's a relation, and which exemplification facts are permissible — turns out to be load-bearing for consistency in any systematic theory of properties.

The question also connects to the direction of explanation between predication in language and exemplification in the world. One view: sentences like "The apple is red" are true because of an underlying metaphysical fact — exemplification holding between an apple and redness. Language mirrors ontology. Another view: talk of "exemplification" is just a way of formalizing predication; there is no further fact beyond the apple being red that the notion of exemplification is tracking. On this deflationary reading, exemplification is a quasi-logical device for talking about object-property relationships, not a substantive relation requiring its own metaphysical explanation. Choosing between these positions shapes what you think property theory owes by way of explanation and what work the formal apparatus of logic is actually doing.
