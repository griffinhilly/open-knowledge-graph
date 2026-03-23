---
id: philosophy-of-biology
title: Philosophy of Biology
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: philosophy-of-science-intro
  type: hard
- id: natural-kinds-classification
  type: soft
builds-toward:
- philosophy-of-neuroscience
tags:
- biology
- evolution
- species
- natural-selection
stage: expert
status: draft
---

# Philosophy of Biology

## Core Idea
Philosophy of biology examines conceptual foundations of biological science: the nature of species (natural kinds or historical lineages?), the status of evolutionary theory (is it testable?), the logic of natural selection, the definition of life, and relationships between molecular and organismal biology. Evolution raises distinctive philosophical puzzles: how can selection explain design without a designer? What makes a trait an adaptation? Is evolution progressive?

## Questions

```yaml
- question: "The 'tautology objection' to natural selection claims that 'survival of the fittest' is circular because fitness just means reproductive success. How do modern evolutionary theorists respond?"
  type: multiple-choice
  options:
    - "They abandon the concept of fitness and explain selection purely through genetic mechanisms"
    - "They define fitness as expected reproductive success given an organism's traits and environment — a probabilistic prediction, not simply the observed outcome"
    - "They accept the circularity but argue that circular explanations can still be scientifically useful"
    - "They restrict 'fitness' to organisms that survive — organisms that die young have zero fitness by definition"
  answer: 1
  explanation: "The tautology objection bites when fitness is identified with actual reproductive success — then 'the fittest survive' means 'those who reproduce most, reproduce most.' The modern response defines fitness as a probabilistic disposition: the expected number of offspring given an organism's phenotype in a particular environment, independent of what actually occurs. This makes natural selection a genuine causal explanation — high expected fitness causes (probabilistically) higher actual reproduction — rather than a definitional truth. Options A and C misstate the actual theoretical response; option D makes fitness even more tautological, not less."

- question: "Hull and Ghiselin argued that species are 'historical individuals' rather than natural kinds. What is the most important implication of this view for biological explanation?"
  type: multiple-choice
  options:
    - "Species cannot be studied scientifically because individuals are too variable"
    - "There can be no exceptionless biological laws quantifying over species the way physical laws quantify over electrons"
    - "Taxonomy should be based entirely on morphological similarity, not evolutionary lineage"
    - "The species concept should be abandoned in favor of population genetics"
  answer: 1
  explanation: "If species are historical individuals — particular lineages with a spatial and temporal location — then 'all tigers are carnivores' is not a law of nature but a contingent generalization about members of a specific lineage that could have been otherwise. Laws of physics hold universally across all instances of a kind (all electrons everywhere behave identically). But biological generalizations about species are historically contingent: they depend on the particular evolutionary path that lineage has taken. This is why philosophy of biology cannot simply import the explanatory models of physics — the objects are fundamentally different in kind."

- question: "Gould and Lewontin's 'spandrels' argument implies that not every biological trait needs an adaptationist explanation."
  type: true-false
  answer: true
  explanation: "True. Gould and Lewontin argued that biologists too readily construct 'just-so stories' — plausible narratives about why a trait would have been selected for — without independent evidence. Some traits are structural byproducts (spandrels in their cathedral analogy): they arise because of other selected traits, not because selection directly favored them. Others result from genetic drift, developmental constraints, or historical contingency. A proper adaptationist explanation must show both that selection could have produced the trait and that alternative explanations are less parsimonious. The default assumption that every trait has an adaptive explanation is not warranted."

- question: "'Survival of the fittest' is a tautology because fitness is defined as reproductive success, making the claim that the fittest survive logically empty."
  type: true-false
  answer: false
  explanation: "False — this was a genuine early criticism, but modern evolutionary theory resolves it. Fitness is not simply the observed reproductive outcome; it is defined as the *expected* reproductive success given an organism's heritable traits in a given environment. This makes fitness a causal disposition measurable (in principle) independently of the actual reproductive outcome. The fittest organism in a particular environment may, by chance, leave fewer offspring than a less fit one — that is a stochastic deviation from expected fitness, not a refutation of selection. The probabilistic definition transforms natural selection from a definition into an empirically testable causal mechanism."

- question: "What does 'multiple realizability' mean in biology, and why does it create a problem for reducing biology to molecular chemistry?"
  type: short-answer
  answer: "Multiple realizability is the fact that the same biological function (e.g., a particular adaptation) can be implemented by many different molecular mechanisms across different organisms. If that is true, then a complete description at the molecular level would not capture what the biological concept explains — you could enumerate every molecular mechanism without stating the generalizing principle that unites them. Reduction loses explanatory content by trading a higher-level generalization for a heterogeneous list of physical realizations."
  explanation: "For example, camera eyes and compound eyes are both 'eyes' in a functional sense — both detect light and produce images — but their molecular and anatomical implementations are completely different. A molecular description of each would give no indication that they serve the same function. This is why selection, fitness, and adaptation operate at the organismal and population level: the explanatory concepts pick out functional patterns that cut across many possible molecular realizations, and that cross-cutting generality is precisely what gets lost in a full reduction."
```

## Explainer

From your introduction to philosophy of science you know that philosophy interrogates the conceptual foundations of scientific disciplines — what counts as a law, an explanation, a natural kind. Biology forces each of these questions into a distinctive shape, because the objects of biology (organisms, species, traits) have properties that resist the models borrowed from physics.

The **species problem** is the entry point. Your study of natural kinds prepared you to ask: is "tiger" a natural kind the way "gold" is? If species were natural kinds defined by essential properties, we'd expect a sharp boundary and a definition. But species are defined by reproductive isolation, evolutionary lineage, and morphological similarity — criteria that conflict with each other in practice and that generate borderline cases at every speciation event. David Hull and Michael Ghiselin argued that species are better understood as **historical individuals** — particular lineages with a spatial and temporal location — rather than as kinds whose members share essential properties. This means there can be no laws of biology that quantify over species the way laws of physics quantify over electrons: "all humans are rational" is not a law but a contingent generalization about the members of a particular lineage.

The logic of **natural selection** is biology's most philosophically scrutinized structure. The mechanism seems simple — heritable variation in fitness leads to differential reproduction — but the **tautology objection** deserves serious attention. If fitness just means "reproductive success," then "the fittest survive" is circular: it means "those who reproduce most, reproduce most." Modern evolutionary theory sidesteps this by defining fitness as *expected* reproductive success given an organism's traits and environment — a counterfactual probability, not simply the observed outcome. This makes natural selection a genuine explanatory mechanism rather than a tautology, but it imports a probabilistic interpretation that requires philosophical defense.

**Adaptationism** — the program of explaining biological traits as adaptations produced by selection — was famously attacked by Gould and Lewontin in their "spandrels of San Marco" paper. They argued that biologists too readily construct **adaptationist just-so stories**: plausible narratives about why a trait would be selected for, with little independent evidence. Not every feature is an adaptation; some are structural byproducts (spandrels), developmental constraints, or neutral drift results. The debate refined what it means to explain a biological trait: a proper adaptationist explanation requires showing both that selection could have produced the trait and that alternative explanations (drift, constraint, historical contingency) are less parsimonious.

Finally, the question of **reduction** in biology bears on your broader study of science. Molecular biology seemed to promise a reduction of all biology to chemistry — gene sequences to proteins to phenotypes. But selection, fitness, and species concepts operate at the organism and population level, not the molecular level. Multiple realizability (many different molecular mechanisms can realize the same functional adaptation) makes a full reduction look impossible without losing explanatory content. This is the biological version of the debates about reduction you encountered in general philosophy of science, and it remains one of biology's most active conceptual frontiers.
