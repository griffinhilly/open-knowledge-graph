---
id: morphology-syntax-interface
title: The Morphology-Syntax Interface
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: morphological-structure
  type: hard
- id: movement-and-transformations
  type: soft
- id: agreement-and-feature-checking
  type: soft
- id: case-theory-and-abstract-case
  type: soft
- id: templatic-morphology
  type: soft
builds-toward:
- distributed-morphology
tags:
- morphology
- syntax
- interface
stage: expert
status: validated
---
# The Morphology-Syntax Interface

## Core Idea
The morphology-syntax interface concerns how morphological and syntactic processes interact. Is morphology derived from syntax (words built by phrase-building operations), or separate? Modern approaches like Distributed Morphology argue morphosyntactic features are assigned syntactically, but actual word forms are determined at the phonological interface, unifying morphology and syntax under one derivational system.

## Questions

```yaml
- question: "Spanish verbs inflect for the person and number of their subject: habla (she speaks) vs. hablamos (we speak). A non-lexicalist theorist would say this pattern is evidence that..."
  type: multiple-choice
  options:
    - "The lexicon stores all conjugated verb forms as separate entries, each linked to syntactic contexts"
    - "Agreement features are assigned during syntactic derivation, driving the morphological realization of verb forms"
    - "Verb forms are morphologically autonomous and only coincidentally reflect syntactic relationships"
    - "Spanish syntax and morphology operate in entirely separate cognitive modules with no interaction"
  answer: 1
  explanation: "Non-lexicalist approaches (like Distributed Morphology) argue that agreement morphology is not a coincidence but a direct product of syntactic feature assignment: the syntactic relationship between verb and subject generates the agreement features that are then phonologically realized as inflectional endings. If morphology were truly separate and pre-syntactic (Strong Lexicalist view), agreement would have to be stipulated as an accidental mapping, not explained by grammar architecture. The non-lexicalist account makes agreement systematic rather than stipulated."

- question: "The Strong Lexicalist Hypothesis claims that..."
  type: multiple-choice
  options:
    - "Inflectional morphology is handled by syntax, but derivational morphology occurs in the pre-syntactic lexicon"
    - "Both inflectional and derivational morphology are assembled in a pre-syntactic lexicon; syntax only sees completed words"
    - "The lexicon and syntax are the same module operating at different scales"
    - "Morphological complexity is determined entirely by the phonological interface, not by underlying syntax"
  answer: 1
  explanation: "The Strong Lexicalist Hypothesis holds that all morphology — both inflectional (walked, walks) and derivational (unhappiness, re-read) — occurs in a pre-syntactic lexicon. Syntax then receives these completed words without any access to their internal morphological structure. This contrasts with the Weak Lexicalist Hypothesis (inflection is syntactic, derivation is lexical) and non-lexicalist approaches (all morphology is syntactic in origin). Knowing these positions is essential for evaluating which phenomena are problematic for each theory."

- question: "In non-lexicalist approaches, agreement morphology on verbs is derived from the same computational system that builds syntactic phrases."
  type: true-false
  answer: true
  explanation: "This is the core non-lexicalist claim: morphology is not a separate pre-syntactic module but the phonological realization of features already present in the syntactic derivation. Agreement, case marking, and inflectional endings are the surface reflex of syntactic feature configurations. The 'interface' problem then becomes one of mapping between syntactic feature structures and phonological forms — which is what Distributed Morphology's Vocabulary Insertion operation handles."

- question: "The Lexicalist and non-lexicalist frameworks make identical predictions about inflectional morphology; they differ only in how they treat derivational word formation."
  type: true-false
  answer: false
  explanation: "The frameworks diverge sharply on inflectional morphology. The Strong Lexicalist Hypothesis holds that inflectional forms are pre-syntactically assembled in the lexicon; non-lexicalist approaches like Distributed Morphology hold that inflection is directly derived by syntactic operations. These produce different predictions about mismatches between morphological form and syntactic structure, the behavior of portmanteau morphemes, and patterns of syncretism — which is why these phenomena are central battlegrounds in the debate."

- question: "What is the central empirical question that decides between lexicalist and non-lexicalist accounts of morphology, and why can't it be resolved by looking at agreement in regular cases alone?"
  type: short-answer
  answer: "The central question is whether morphological form tracks syntactic structure systematically enough that morphology must be derived from syntax, or whether the correlations can be treated as coincidental lexical specification. Regular agreement looks the same under both accounts — the Lexicalist can stipulate forms that happen to match syntax, while the non-lexicalist derives them. The decisive evidence comes from edge cases: morphological mismatches with syntax, the behavior of clitics (which seem syntactically active but morphologically word-like), phrasal idioms with non-compositional meaning, and the scope and productivity of different morphological operations."
  explanation: "This is why the debate has lasted decades: both frameworks can describe the core cases. The methodological lesson is that theoretical linguistics advances by identifying phenomena that one framework handles naturally and the other must stipulate — those are the revealing data points. Agreement in simple verb-subject pairs is not one of them."
```

## Explainer

Your prerequisite in morphological structure gave you the tools to analyze how morphemes combine within words — affixes, roots, inflectional versus derivational morphology, paradigm structure. Your acquaintance with syntactic movement introduced hierarchical phrase-building and displacement operations. The **morphology-syntax interface** asks the question that bridges these two areas: are word-building and phrase-building fundamentally the same kind of operation, or are they separate cognitive modules that merely interact at their boundaries? The answer has consequences for the entire architecture of the grammar.

The strongest evidence for tight interaction between morphology and syntax comes from **agreement**: the morphological form of a verb reflects its syntactic relationship to a subject. In Latin or Spanish, verbal endings change according to the person and number of the subject — morphological realization that tracks syntactic structure transparently. If morphology were truly separate from syntax, this correspondence would have to be stipulated, not explained. **Head movement** provides another piece of evidence: in many languages, a verb moves from its base position in the verb phrase to a higher functional position (Tense, Agreement), and this movement is reflected morphologically — V2 in Germanic languages, V-to-T movement in French. The movement and the morphology are two sides of the same coin.

The dominant theoretical divide concerns where complex words are built. **Lexicalism** holds that morphologically complex words are assembled in a pre-syntactic module — the lexicon — and syntax sees only the completed words it inserts. The **Weak Lexicalist Hypothesis** restricts this to derivational morphology (word-formation like *un-happi-ness*), allowing syntax to handle inflection. The **Strong Lexicalist Hypothesis** extends it to all morphology. Against this, **non-lexicalist** approaches argue that the apparent distinction between word-building and sentence-building dissolves under scrutiny — both involve hierarchical feature-structure building, differing in scale but not in kind. Distributed Morphology, your next topic, is the most fully developed version of this position.

The interface problem resists easy resolution because the same surface patterns can be described in multiple theoretical vocabularies. A language where verbs agree with subjects can be analyzed as syntax driving agreement (non-lexicalist) or as the lexicon inserting agreement-marked forms after syntactic derivation (Lexicalist). The choice between these analyses depends on subtle empirical differences: mismatches between morphological and syntactic structure, the behavior of clitics, the distribution of phrasal idioms, the properties of incorporation. Mastering the interface means learning to see what each theory predicts that the other cannot handle — which is the method of theoretical linguistics at its core.
