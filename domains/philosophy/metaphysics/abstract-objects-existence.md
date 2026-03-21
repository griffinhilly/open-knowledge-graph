---
id: abstract-objects-existence
title: Abstract Objects and Existence
domain: philosophy
course: metaphysics
prerequisites:
- id: abstract-objects-platonism
  type: hard
- id: nominalism-about-universals
  type: soft
- id: zfc-axioms-overview
  type: soft
builds-toward:
- tropes-vs-universals
tags:
- abstract-objects
- ontology
- platonism
- nominalism
stage: formal-systems
status: draft
---

# Abstract Objects and Existence

## Core Idea
Do abstract objects like numbers, properties, and propositions genuinely exist? Platonists affirm abstract objects' existence; nominalists deny it. This debate has profound implications for metaphysics: what objects must our theory acknowledge, and how do abstract objects relate to the physical world?

## Questions

```yaml
- question: "A student argues that numbers must exist because '7 is prime even if no one had ever thought about it.' A nominalist responds that this doesn't require an object called 'seven' to exist robustly. Which nominalist strategy does this response exemplify?"
  type: multiple-choice
  options:
    - "The indispensability argument — accepting that mathematics is indispensable to science and therefore abstract objects exist"
    - "Fictionalism — mathematical statements can be systematically true within a useful fiction without requiring that the entities they mention actually exist"
    - "Modal structuralism — rephrasing mathematical claims as claims about what structures would exist if certain axioms held"
    - "Trope theory — replacing abstract universal numbers with concrete particular instances of numerosity"
  answer: 1
  explanation: "Fictionalism holds that mathematical statements are 'true within a fiction' — like 'Sherlock Holmes lives at 221B Baker Street,' which is true within Doyle's fiction without implying a real detective. Similarly, '7 is prime' is systematically true within the mathematical fiction without requiring a Platonic object 'seven' to exist. This preserves the utility and inferential structure of mathematics while rejecting its face-value ontological commitment."

- question: "The 'epistemological problem' for Platonism about abstract objects is that:"
  type: multiple-choice
  options:
    - "Abstract objects are too vaguely defined to distinguish them precisely from physical objects"
    - "If abstract objects are non-spatial, non-temporal, and causally inert, it is unclear how cognitive faculties that evolved to track physical environments through causal contact could yield knowledge about them"
    - "Accepting abstract objects conflicts with modern physics, which leaves no room for non-physical entities"
    - "Abstract objects would make mathematical truths too certain, eliminating the possibility of genuine mathematical discovery"
  answer: 1
  explanation: "Our knowledge-forming faculties work through causal chains: perception, memory, and inference are all causally mediated. But abstract objects — non-spatial, non-temporal, and causally inert — cannot enter any causal chain. The Platonist must explain how finite, physical minds come to know a realm that by definition cannot affect them. The standard responses — positing special rational intuition, or revising the causal theory of knowledge — each carry significant philosophical costs."

- question: "The Quine-Putnam indispensability argument concludes that we have reason to believe abstract objects exist because our best scientific theories quantify over mathematical entities and we believe those theories are true."
  type: true-false
  answer: true
  explanation: "The argument runs: (1) we are committed to the existence of entities our best theories quantify over; (2) our best scientific theories quantify over mathematical objects (sets, functions, numbers); (3) therefore we are committed to the existence of mathematical objects. This grounds abstract objects empirically by tying them to theoretical commitments we already accept when we accept physics, rather than grounding them in pure a priori Platonic intuition."

- question: "Nominalists must deny that mathematical statements like '7 is prime' are true, since on their view there is no object '7' for the statement to be about."
  type: true-false
  answer: false
  explanation: "This is a common mischaracterization. Most nominalist strategies preserve mathematical truth without ontological commitment to abstract objects. Fictionalists accept that '7 is prime' is true within a mathematical fiction. Modal structuralists paraphrase it as a claim about what would hold in any Peano-satisfying structure. Neither strategy declares mathematics false — they provide alternative analyses of what mathematical truth amounts to. Nominalism is a position about ontology, not about mathematical correctness."

- question: "What is the epistemological problem for Platonism, and why does it represent a genuine philosophical challenge rather than a merely verbal puzzle?"
  type: short-answer
  answer: "Platonism holds that abstract objects exist in a non-spatial, non-temporal realm, causally isolated from the physical world. Our cognitive faculties — perception, memory, inference — evolved to track physical environments through causal interaction, and knowledge through perception requires that information causally reach us. Since abstract objects are causally inert, no such contact is possible. Every proposed solution has costs: positing 'rational intuition' is mysterious; revising the causal theory of knowledge undermines broader epistemology; fictionalism preserves utility but gives up the view that mathematics is about anything real."
  explanation: "The problem sits at the intersection of metaphysics and epistemology. You can't assess abstract-objects ontology by asking only what makes mathematical discourse true — you must also ask whether proposed entities are epistemically accessible in a way compatible with how minds work. Platonism's strength is explaining mathematical necessity, objectivity, and applicability; its weakness is explaining cognition. This trade-off drives the ongoing debate between Platonist and nominalist positions in philosophy of mathematics."
```

## Explainer

From your study of Platonism about abstract objects, you already know the core Platonic picture: numbers, geometric forms, and properties exist independently of minds and matter, in a non-spatiotemporal realm that we access through reason rather than perception. Now the question deepens: what kind of existence do these objects have, and is that existence compatible with what we know about the physical world? The debate between **Platonism** and **nominalism** is at its heart a debate about the ontological commitments we must accept to make sense of mathematics, language, and thought.

The standard argument for abstract objects comes from mathematics and logic. When we say "the number seven is prime," we appear to be saying something true — and true in a way that doesn't depend on anyone's beliefs, on any physical object, or on any linguistic convention. The number seven would be prime even if no one had ever thought about it. This suggests that mathematical objects have **mind-independent existence**. The **indispensability argument** (Quine and Putnam) sharpens this: our best scientific theories quantify over mathematical objects, and if we believe our best theories are true, we must believe in the entities they quantify over. Abstract objects come in with mathematics.

The nominalist pushes back on multiple fronts. First, she questions whether we need to take mathematical quantification literally — perhaps "the number seven is prime" is true in a way that doesn't require an entity called "seven" to exist in any robust sense. **Fictionalism** treats mathematical statements as true within a fiction, like statements about Sherlock Holmes. **Modal structuralism** rephrases mathematical claims as claims about what structures would exist if certain axioms held. **Nominalism via tropes** replaces abstract universal properties with concrete particular property-instances, eliminating one class of abstract objects. Each strategy tries to preserve the utility of mathematical and logical vocabulary without the ontological overhead.

The most pointed challenge for Platonism is the **epistemological problem**: if abstract objects are non-spatial, non-temporal, and causally inert, how do we come to know anything about them? Our cognitive faculties evolved to track physical environments — perception, memory, and inference are all causally mediated. But causal mediation requires causal contact, which abstract objects by definition cannot provide. The Platonist must either posit a special faculty of rational intuition, explain mathematical knowledge as non-perceptual but still reliable, or revise the standard causal theory of knowledge. Each option has costs.

From your optional prerequisite on ZFC set theory, you can see this debate playing out in foundations of mathematics: ZFC's axioms assert the existence of sets that are paradigmatically abstract — yet every working mathematician relies on them. Whether those sets are real objects, useful fictions, or structural posits is a question your foundations training makes precise. The abstract objects debate is not mere wordplay; it determines what kind of things our best theories are actually claiming the world contains, and whether that picture is coherent.
