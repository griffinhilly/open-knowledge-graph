---
id: laws-of-nature
title: Laws of Nature
domain: philosophy
course: metaphysics
prerequisites:
- id: causation-and-causal-relations
  type: hard
- id: regularity-theory-of-causation
  type: hard
tags:
- laws of nature
- regularity
- necessitarianism
- Armstrong
- Best Systems
- Humean
stage: formal-systems
status: draft
---

# Laws of Nature

## Core Idea
What are the laws of nature — are they mere descriptions of cosmic regularities, or do they express genuine necessities that govern what happens? The Humean regularity view, refined by Lewis's Best Systems Account, holds that laws are the axioms of the simplest and strongest systematization of all the particular facts — they describe but do not govern. The necessitarian view (Armstrong, Dretske, Tooley) holds that laws are relations of nomic necessitation between universals: it is not just that all copper conducts electricity, but that the universal copper-hood necessitates the universal conductivity. The debate connects to causation (do laws ground causal connections?), counterfactuals (do laws support them because they are necessary or merely because they are robust regularities?), and the metaphysics of science more broadly.

## How It's Best Learned
Read Armstrong's What Is a Law of Nature? chapters 1-5 for the necessitarian account, then Lewis's 'New Work for a Theory of Universals' section on Best Systems for the Humean alternative. Evaluate each against the identification problem: how do we distinguish genuine laws from accidental regularities?

## Common Misconceptions
- Humeans about laws do not deny that laws are important or explanatory; they deny that laws have a governing role over and above the regularities they describe.
- The debate is not about whether science discovers laws — both sides agree it does — but about what laws are in the furniture of the world.

## Questions

```yaml
- question: "Both 'All copper conducts electricity' and 'All coins in the philosopher's pocket today are dimes' are true universal generalizations. What feature most clearly marks the first as a law of nature and the second as a mere accidental regularity?"
  type: multiple-choice
  options:
    - "The first statement has far more instances confirming it than the second"
    - "The first statement supports counterfactuals — if this wire were copper, it would conduct electricity — while the second does not"
    - "The first was discovered through controlled experimentation rather than observation"
    - "The first describes a physical property while the second describes a contingent collection"
  answer: 1
  explanation: "Both statements cover all their actual instances, so breadth of confirmation alone can't distinguish them. The key test is counterfactual support: genuine laws hold not just for what actually exists but for what would be the case in hypothetical scenarios. 'If this iron rod were copper, it would conduct electricity' is true; 'If this quarter were in the philosopher's pocket, it would be a dime' is false. Laws back counterfactuals; accidental regularities don't. This is the core philosophical criterion both Humeans and necessitarians must explain."

- question: "According to Armstrong's necessitarian view, what makes 'all copper conducts electricity' a law of nature rather than a mere regularity?"
  type: multiple-choice
  options:
    - "It appears in the simplest and most powerful systematization of all physical facts"
    - "It has been confirmed by an extremely large number of independent observations"
    - "The universal copper-hood stands in a necessitation relation N(F, G) to the universal conductivity"
    - "Scientists have reached consensus that it is a fundamental principle of nature"
  answer: 2
  explanation: "Armstrong's necessitarian account posits that laws are second-order relations between universals. It is not merely that every copper instance happens to be conductive — rather, the property copper-hood necessitates the property conductivity at the level of universals. This necessitation relation N(F, G) is what explains why the regularity holds necessarily rather than accidentally and why it supports counterfactuals. Option A describes Lewis's Best Systems Account (the Humean alternative), not Armstrong's view."

- question: "On the Humean view, laws of nature describe regularities in the world but do not govern or necessitate what happens — there is no enforcement mechanism above the regularities themselves."
  type: true-false
  answer: true
  explanation: "True. Humeans about laws — including Lewis's Best Systems Account — hold that the world consists of a mosaic of particular facts, and laws are just the axioms of the best systematization of those facts. They are summaries, not governors. The idea that laws 'make' events happen or 'enforce' regularities adds metaphysical machinery the Humean regards as unnecessary and explanatorily inert. Laws describe what is and was and will be; they do not stand behind events as their cause."

- question: "Humeans about laws of nature deny that laws are genuinely explanatory or important to scientific understanding."
  type: true-false
  answer: false
  explanation: "False — this is the most common misconception about the Humean position. Humeans fully accept that laws explain, predict, and unify phenomena; they are central to scientific practice. What Humeans deny is a specific metaphysical claim: that laws have a governing role over and above the regularities they describe. The debate is about what laws are in the furniture of the world, not about whether science successfully discovers them or uses them to explain. Both Humeans and necessitarians agree that laws matter; they disagree about their ultimate metaphysical nature."

- question: "What is the 'identification problem' for theories of laws of nature, and why does it challenge both Humean and necessitarian accounts?"
  type: short-answer
  answer: "The identification problem asks: how do we distinguish genuine laws from merely accidental regularities? Both describe true universal generalizations, so the distinction can't come from truth or generality alone. For the Humean (Best Systems Account), the answer is holistic — only by assessing the entire system of facts can you determine which generalizations earn a place in the optimal systematization, making the criterion potentially circular or indeterminate. For the necessitarian, the answer requires identifying which universals stand in the necessitation relation N(F,G) — but there is no clear empirical method for detecting this second-order relation distinct from simply observing the regularity itself."
  explanation: "The identification problem is a live challenge for both camps. Lewis acknowledges that the Best Systems Account may give multiple tied systems, leaving laws underdetermined. Armstrong acknowledges we cannot directly observe nomic necessitation — we infer it from regularities, which risks making the necessitarian account empirically indistinguishable from the Humean one. The problem drives the central literature because any theory of laws must explain both what laws ARE and how we KNOW which regularities are lawful."
```

## Explainer

You already know the **regularity theory of causation** from Hume: causation is not a necessary connection we observe directly, but a pattern of constant conjunction — we call A the cause of B because A-events are regularly followed by B-events. Laws of nature are intimately related: the law that copper conducts electricity just *is* the regularity that every instance of copper is followed by electrical conductivity. But this Humean picture faces an immediate challenge — what distinguishes a genuine law from a mere **accidental regularity**?

Consider two true generalizations: "All copper conducts electricity" and "All the coins in Griffin's pocket today are dimes." Both describe universal regularities — everything that satisfies the antecedent satisfies the consequent. But only the first looks like a law. Crucially, the law *supports counterfactuals*: if this piece of iron were copper, it would conduct electricity. The accidental regularity does not: if this quarter were in Griffin's pocket today, it would not thereby become a dime. The challenge for any theory of laws is to explain this difference — why some regularities have the modal force of necessity while others are cosmic coincidences.

David Lewis's **Best Systems Account (BSA)** is the most sophisticated Humean answer. On this view, the laws are the theorems of the axiomatic system that best balances *simplicity* (few axioms) and *strength* (entailing many true facts about the world). A law is not just any regularity — it is one that earns its place in the optimal systematization of all particular facts. "All coins in Griffin's pocket are dimes" adds no strength that a more general truth couldn't subsume, so it does not appear in the best system. The counterfactual support laws provide falls out of their systematic role rather than requiring any metaphysical addition beyond the regularities themselves.

The **necessitarian** alternative, developed by Armstrong, Dretske, and Tooley, holds that laws are real relations of **nomic necessitation** between universals. It is not just that copper-instances are followed by conductive-instances; rather, the universal *copper-hood* necessitates the universal *conductivity*. This second-order relation N(F, G) is what makes the regularity necessary rather than accidental, and what explains why laws support counterfactuals — they could not have been otherwise. The cost is ontological: you must accept universals as real and posit a distinctive necessitation relation over and above their instantiation.

Both accounts struggle with the **identification problem**: how do we tell which regularities in nature are laws and which are accidents? For the Humean, the answer is holistic — only by examining the entire system of facts can you determine which generalizations are law-like. For the necessitarian, the answer requires investigating which universals stand in the necessitation relation — a metaphysically loaded inquiry with no obvious empirical method. The debate is not merely academic; it shapes how we understand the explanatory power of science, whether physical laws could have been different, and what it means for a process to be *governed* by a principle rather than merely conforming to it.
