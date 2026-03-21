---
id: fundamental-properties-sparse-abundant
title: 'Fundamental and Derivative Properties: Sparse and Abundant Ontologies'
domain: philosophy
course: metaphysics
prerequisites:
- id: properties-intrinsic-extrinsic
  type: hard
- id: grounding-and-fundamentality
  type: hard
- id: substance-and-property
  type: soft
builds-toward:
  - abstract-entities-platonism
tags:
- properties
- fundamentality
- ontology
- sparse
- abundant
stage: formal-systems
status: draft
---
# Fundamental and Derivative Properties: Sparse and Abundant Ontologies

## Core Idea
Abundant theories count as properties any condition expressible by a predicate (redness, being-a-table, being-north-of-Boston); sparse theories restrict properties to fundamental, causally-efficacious ones required to explain all other facts. The choice shapes understanding of causation, laws of nature, and scientific ontology.

## Questions

```yaml
- question: "A sparse theorist is asked whether 'being located within ten miles of the Eiffel Tower' is a genuine property. Which response best reflects the sparse view?"
  type: multiple-choice
  options:
    - "Yes — the predicate is coherent and applies to many objects, so it corresponds to a property"
    - "No — the predicate doesn't track a natural kind with causal efficacy; it's a gerrymandered classification that doesn't carve nature at its joints"
    - "Yes — location is a physical fact, so any location-based predicate picks out a real property"
    - "No — properties must be intrinsic, and this predicate is relational"
  answer: 1
  explanation: "The sparse theorist asks not 'is the predicate coherent?' but 'does it track something with causal power that explains resemblance and supports laws?' A location relative to an arbitrary landmark does none of this — two objects within ten miles of the Eiffel Tower may share nothing physically relevant. Option A is the abundant-theory answer, which accepts any coherent predicate. Option D confuses sparse/abundant with intrinsic/extrinsic — these are separate distinctions."

- question: "Consider the predicate 'being-such-that-2+2=4,' which applies to every object since 2+2=4 is necessarily true. From this, an abundant theorist concludes that every object shares this property. What does this example reveal about the explanatory limits of abundant properties?"
  type: multiple-choice
  options:
    - "It reveals the abundant theory is self-contradictory, because a property shared by everything cannot exist"
    - "Abundant properties can be trivially shared without tracking any real similarity — they therefore cannot explain resemblance, causation, or why some generalizations are laws while others are accidents"
    - "It shows that abundant theory only applies to contingent predicates, and necessary truths generate a different kind of property"
    - "The example proves that abundant theory collapses into nominalism"
  answer: 1
  explanation: "The abundant theory's strength (logical tractability) is also its weakness: properties proliferate without doing explanatory work. Two objects sharing 'being-such-that-2+2=4' tells you nothing about their causal similarity. Sparse theorists argue that genuine properties must explain why similar objects behave similarly in law-governed ways. Option A misunderstands the abundant theory — it doesn't claim a universally shared property is incoherent, just that it exists. That's exactly the problem: it exists but explains nothing."

- question: "On the sparse theory, whether 'redness' is a genuine property depends on whether there is a corresponding fundamental physical property with causal efficacy — not merely on whether 'red' is a coherent, commonly-used predicate."
  type: true-false
  answer: true
  explanation: "This is the core commitment of sparse ontology. The sparse theory asks: does this predicate pick out something that does real causal work, supports laws of nature, and grounds resemblance? If 'redness' turns out to be fully reducible to surface reflectance properties that do the actual causal work, then 'redness' itself may be a useful shorthand rather than a sparse property. Coherence and common use are criteria for abundant properties, not sparse ones."

- question: "The sparse/abundant distinction is primarily a terminological dispute with no real consequences for philosophy of science, since laws of nature can be formulated using any predicates as long as they are consistently applied."
  type: true-false
  answer: false
  explanation: "The distinction has significant stakes for philosophy of science. Laws formulated using non-natural predicates — like Goodman's predicate 'grue' (green before a date, blue after) — fail to support counterfactuals and inductive projection. A sparse theorist explains this: 'grue' doesn't pick out a natural property, so regularities involving it aren't genuine laws. The abundant theorist has no such explanation. The distinction also matters for causation: if only sparse properties can be causes, then ordinary-language predicates that don't track natural kinds are causally otiose."

- question: "Why can't abundant properties explain the difference between laws of nature and accidental generalizations? What does the sparse theory offer that the abundant theory cannot?"
  type: short-answer
  answer: "Abundant properties exist for every coherent predicate, so both 'all electrons repel each other' and 'all things within ten miles of the Eiffel Tower expand when heated' have corresponding properties — abundant theory treats them symmetrically. It cannot explain why the first supports counterfactuals and the second doesn't, or why the first is a law and the second is an accident. The sparse theory resolves this by restricting genuine properties to natural kinds that carry causal efficacy. Laws are regularities among sparse properties, which ground necessity and support inductive projection. The geographic predicate doesn't pick out a sparse property, so the regularity it describes is an accident, not a law."
  explanation: "This is the philosophical payoff of the sparse/abundant distinction. The problem of distinguishing laws from accidents (the 'problem of induction' and 'problem of lawhood') runs through philosophy of science. Sparse ontology provides a principled basis: natural properties ground nomological necessity. Without this restriction, any accidental regularity becomes a candidate law — which is no theory at all."
```

## Explainer

From your study of intrinsic and extrinsic properties you know that some features of an object belong to it independently of its environment (its mass, its charge) while others depend on relationships (being north of Boston, being the most famous). And from your study of grounding and fundamentality you know that some facts hold in virtue of other facts — derivative truths are grounded in more basic ones. The sparse/abundant debate asks: which of all the things we can truly predicate of an object correspond to genuine, metaphysically substantive properties, and which are merely useful classifications we project onto a world that doesn't carve quite that way?

The **abundant** theory of properties is maximally permissive: for every predicate that can be truly applied to some object, there is a corresponding property. Being-a-prime-number, being-located-within-ten-miles-of-Paris, being-such-that-snow-is-white — all of these correspond to real properties if the predicate is coherent and applicable. The advantage of abundance is logical tractability: properties proliferate as freely as predicates, and no selection problem arises. The disadvantage is that abundant properties cannot do explanatory work. If everything has a property corresponding to every true predicate, you can't use property-sharing to explain causal similarity, natural law, or projectibility. Two things both have the property being-such-that-Plato-existed — that doesn't make them causally alike in any interesting way.

The **sparse** theory holds that only some predicates track genuine, natural properties — the ones that "carve nature at its joints," to use Plato's phrase. David Lewis, the sparse theory's most influential defender, argued that sparse properties are those picked out by physics: mass, charge, spin, and a few others. These are the **perfectly natural properties** that ground resemblance, causal power, and nomological necessity. Everything else is derivative. The predicate "is jade" picks out what turns out to be two natural kinds (jadeite and nephrite) loosely grouped by appearance — it doesn't correspond to a single sparse property. The predicate "is an electron" plausibly does correspond to a sparse property.

The practical stakes are high for philosophy of science. **Laws of nature** are typically understood as regularities among natural properties, not among arbitrary abundant ones. "All electrons repel each other" is a candidate law because "electron" tracks a sparse property; "all things within ten miles of the Eiffel Tower expand when heated" is not, even if accidentally true, because the property is not natural. Similarly, **causation**: only sparse properties can genuinely be causes, on many theories. If the "property" of being red causes nothing (redness just is a certain complex of physical surface reflectance properties that do the causal work), then color language is causally otiose — a useful shorthand, not a report of causal structure. The choice between sparse and abundant theories thus determines whether the predicates of ordinary language and the special sciences carve reality or merely slice a convenient path through it.
