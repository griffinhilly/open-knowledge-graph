---
id: lexical-semantics
title: Lexical Semantics
domain: language-and-communication
course: linguistics
prerequisites:
- id: morphological-structure
  type: soft
builds-toward:
- compositional-semantics
- linguistic-pragmatics
tags:
- semantics
- word meaning
- sense
- reference
- prototype
- semantic relations
stage: formal-systems
status: validated
---

# Lexical Semantics

## Core Idea
Lexical semantics studies the meaning of words and the systematic relationships between them. Key distinctions include sense (the concept a word expresses) and reference (what the word picks out in the world). Words enter into semantic relations: synonymy (similar meaning), antonymy (opposite meaning), hyponymy (subset/superset), and meronymy (part/whole). Prototype theory proposes that word meanings are organized around central, typical examples rather than necessary and sufficient conditions.

## How It's Best Learned
Map out semantic fields (clusters of related words, like color terms or kinship terms) to see how meaning is organized relationally. Compare how different languages carve up the same conceptual space (e.g., color categories, spatial relations) to reveal how lexicalization varies cross-linguistically.

## Common Misconceptions
- Words do not have single fixed meanings; polysemy (multiple related meanings) is the norm, not the exception.
- Synonyms are rarely perfectly interchangeable — connotation, register, and collocation always differ.
- Dictionary definitions are not semantic representations; they are imperfect, circular approximations.

## Questions

```yaml
- question: "Which of the following best illustrates the distinction between a word's sense and its reference?"
  type: multiple-choice
  options:
    - "'Dog' and 'canine' have the same reference and the same sense."
    - "The expressions 'the morning star' and 'the evening star' have the same reference (Venus) but different senses."
    - "Sense is the physical object a word points to; reference is the mental concept."
    - "Only proper names have reference; common nouns have only sense."
  answer: 1
  explanation: "Frege's classic example: 'the morning star' and 'the evening star' both refer to Venus, but they express different senses (modes of presentation). This shows that reference alone cannot capture meaning — two expressions can pick out the same thing in the world while conveying different information. Sense is the cognitive content; reference is the worldly entity."

- question: "Prototype theory proposes that category membership is most-or-hardly anything: an entity either fully belongs to a category (e.g., 'bird') or does not belong at most."
  type: true-false
  answer: false
  explanation: "This describes the classical, necessary-and-sufficient-conditions view of categories. Prototype theory, developed by Eleanor Rosch, proposes graded membership: categories are organized around central, typical examples (prototypes), and members vary in how well they represent the category. A robin is a more prototypical bird than a penguin, even though both are birds. This is why people rate category members as better or worse examples."

- question: "What is the difference between hyponymy and meronymy? Give an example of each."
  type: short-answer
  answer: "Hyponymy is an 'is a' (subset/superset) relation: 'rose' is a hyponym of 'flower' because a rose IS A flower. Meronymy is a 'part of' relation: 'petal' is a meronym of 'flower' because a petal IS PART OF a flower."
  explanation: "The distinction matters because hyponymy organizes taxonomic hierarchies (biological classifications, for example), while meronymy organizes part-whole structures (anatomy, machine components). Conflating them is a common error when building semantic networks or ontologies."
```

## Explainer

If you have studied morphological structure, you know that words are built from meaningful parts — morphemes combine to form complex words. Lexical semantics operates at the level above morphemes: it asks what words mean as units, and how the meanings of different words in a language relate to each other.

The most fundamental distinction is between sense and reference, introduced by Frege. The reference of an expression is what it picks out in the world — the actual entity or set of entities. The sense is the mode of presentation, the cognitive content associated with the expression. "The morning star" and "the evening star" both refer to Venus, but they are not the same expression semantically — they convey different information and were once believed to refer to different objects. This distinction explains why substituting co-referential expressions into certain contexts (like "John believes that...") can change truth values: what matters is sense, not just reference.

Words do not mean in isolation; they mean in relation to other words. Semantic fields are clusters of words that carve up a conceptual domain together — color terms, kinship terms, verbs of motion. Within a semantic field, words enter into structural relations. Synonymy (near-identical meaning, like "begin" and "commence") is rarer than it appears — truly interchangeable synonyms scarcely exist because words always differ in register, connotation, or collocational range. Antonymy comes in several types: gradable opposites ("hot/cold"), complementary pairs ("alive/dead"), and converses ("buy/sell"). Hyponymy organizes hierarchies ("collie" is a hyponym of "dog"), while meronymy organizes part-whole structures ("wheel" is a meronym of "car").

Prototype theory, developed by Eleanor Rosch in the 1970s, challenged the classical assumption that category membership is determined by necessary and sufficient conditions. The classical view would say that something is a bird if and only if it has the features [+feathers, +wings, +lays eggs, ...]. But people reliably rate robins as better birds than penguins or ostriches, even though all are equally birds by the classical definition. Prototype theory explains this by proposing that categories are organized around typical central members, and membership is graded — objects can be more or less representative of the category.

Finally, polysemy — one word carrying multiple related meanings — is not an exception but the norm. "Bright" means both "emitting light" and "intelligent" through a systematic conceptual metaphor (understanding is seeing). "Mouth" applies to humans and rivers. These extended meanings are not random; they follow patterns of metaphor, metonymy, and semantic shift. Recognizing polysemy helps explain why word-by-word translation across languages so often fails: the semantic boundaries a language draws are language-specific, and the same word form may carve up conceptual space very differently from its apparent translation equivalent.
