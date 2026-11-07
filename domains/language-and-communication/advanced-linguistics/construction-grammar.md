---
id: construction-grammar
title: Construction Grammar
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: argument-structure-thematic-roles
  type: hard
- id: syntactic-structure
  type: hard
- id: lexical-semantics
  type: soft
- id: head-driven-phrase-structure-grammar
  type: soft
- id: fixed-idioms-and-expressions
  type: soft
builds-toward: []
tags:
- syntax
- construction-grammar
- argument-structure
- usage-based
- idioms
- cognitive-linguistics
stage: expert
status: validated
---
# Construction Grammar

## Core Idea
Construction Grammar is a family of theories holding that grammar consists of constructions: learned pairings of form and meaning at every level of size and abstraction, from words and idioms to abstract sentence patterns. In this view there is no sharp division between the lexicon and the rules; "kick the bucket," "the X-er, the Y-er," and the English ditransitive pattern are all stored constructions. Adele Goldberg's 1995 book argued that argument-structure patterns themselves carry meaning, which explains sentences like "She sneezed the napkin off the table," where the verb alone does not license the extra arguments. The approach is closely tied to usage-based accounts of acquisition and to cognitive linguistics.

## How It's Best Learned
Start with partly fixed idioms that standard phrase-structure rules handle awkwardly, such as "let alone" or "What's this fly doing in my soup?", and ask what a speaker must know to use them. Then compare a lexicalist account, which lists argument frames in each verb's entry, with a constructional account, which attaches meaning to the sentence pattern. Test both on novel verb uses, such as "He texted me the address." Read the foundational papers alongside a usage-based acquisition study to see how the theory links grammar to learning.

## Common Misconceptions
- Construction Grammar is only a theory of idioms. (It began with idioms but claims that all of grammar, including the most general patterns like the transitive clause, consists of constructions.)
- Construction Grammar is a single formal framework. (It is a family that includes Berkeley Construction Grammar, Goldberg's cognitive version, Radical Construction Grammar, and Sign-Based Construction Grammar, with different degrees of formalization.)
- If constructions carry meaning, verbs carry none. (Verb meaning and construction meaning combine; the construction supplies an event frame, and the verb must be compatible with it.)

## Questions

```yaml
- question: "In 'Pat sneezed the foam off the cappuccino,' the verb 'sneeze' is usually intransitive. How does Construction Grammar explain the direct object and path phrase?"
  type: multiple-choice
  options:
    - "The verb 'sneeze' has a separate transitive lexical entry meaning 'move by sneezing'"
    - "The caused-motion construction, a form-meaning pairing meaning 'X causes Y to move along path Z,' supplies the extra arguments"
    - "The sentence is ungrammatical and only appears in jokes"
    - "A transformation inserts a hidden verb 'cause'"
  answer: 1
  explanation: "Goldberg argued that the caused-motion pattern [Subj V Obj Oblique-path] carries its own meaning. The verb contributes the manner (sneezing), and the construction contributes the caused-motion frame and argument slots. This avoids positing a new sense of 'sneeze' for every such use."

- question: "Which expression is a classic example of a partially schematic construction studied in early Construction Grammar?"
  type: multiple-choice
  options:
    - "The cat sat on the mat"
    - "The more you practice, the better you get"
    - "Colorless green ideas sleep furiously"
    - "John is easy to please"
  answer: 1
  explanation: "The comparative correlative 'the X-er, the Y-er' has fixed parts ('the,' comparative forms) and open slots. Its form and meaning cannot be predicted from general English phrase-structure rules, which made it a central example for arguing that such patterns must be stored as constructions."

- question: "Construction Grammar maintains a strict separation between a lexicon of words and a separate set of grammatical rules."
  type: true-false
  answer: false
  explanation: "A core claim of Construction Grammar is that words, idioms, and abstract patterns lie on a continuum of constructions differing in size and schematicity. The full inventory is sometimes called the 'constructicon.'"

- question: "How does Construction Grammar fit with usage-based theories of language acquisition?"
  type: short-answer
  answer: "Both treat grammar as learned from input. Usage-based researchers such as Michael Tomasello argue that children start with item-specific constructions tied to particular words and gradually generalize them into abstract patterns. Construction Grammar supplies the units, form-meaning pairings at many levels, that such learning would produce."
  explanation: "This pairing contrasts with accounts in which children set parameters of an innate universal grammar. The debate centers on how much abstract structure must be built in versus extracted from experience."
```

## Explainer

Mainstream generative syntax has often divided linguistic knowledge into two parts: a lexicon of words with their properties, and a general system of rules that combine them. Idioms such as "kick the bucket" were treated as exceptions stored in the lexicon. Construction Grammar challenges that division.

The starting point was a set of patterns that are neither fully fixed nor fully general. In a 1988 paper, Charles Fillmore, Paul Kay, and Mary Catherine O'Connor analyzed "let alone," as in "I can't afford a bicycle, let alone a car." Its use depends on special conditions of meaning and context that no general rule predicts. Similar cases include the comparative correlative ("The more you read, the more you know") and the "What's X doing Y?" pattern ("What's this fly doing in my soup?"), which expresses surprise or disapproval, not a literal question about activity. Speakers must learn each of these as a unit with its own form and meaning.

Construction Grammar generalizes this point. A **construction** is any conventional pairing of form and meaning. Constructions range from fully specific (the word "avocado") through partly open ("the X-er, the Y-er") to fully abstract (a subject-verb-object clause). The whole inventory is sometimes called the **constructicon**.

Adele Goldberg's *Constructions* (1995) extended the idea to argument structure. Compare:

- "She sneezed." (intransitive)
- "She sneezed the napkin off the table." (caused motion)
- "He baked her a cake." (ditransitive: intended transfer)

A lexicalist approach needs a new sense of "sneeze" or "bake" for each frame. Goldberg proposed instead that the **caused-motion** and **ditransitive** constructions carry meaning themselves. The verb fills in manner, and the construction supplies the event structure and argument slots. When a verb's meaning conflicts with a construction, the construction can **coerce** a new interpretation, or the sentence becomes odd.

Construction Grammar is a family of approaches. Berkeley Construction Grammar and Sign-Based Construction Grammar use formal feature structures similar to HPSG. Goldberg's version and William Croft's Radical Construction Grammar are closer to cognitive linguistics.

The theory connects closely to **usage-based** acquisition research. Michael Tomasello and others argue that children first learn item-specific patterns, such as "more ___" or "Where's the ___?", and gradually abstract general constructions. On this view, grammar is learned from experience with constructions rather than derived from innate parameters, a point of continuing debate with generative approaches.
