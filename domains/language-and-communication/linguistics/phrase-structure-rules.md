---
id: phrase-structure-rules
title: Phrase Structure Rules and Context-Free Grammars
domain: language-and-communication
course: linguistics
prerequisites:
- id: constituency-test-methods
  type: hard
- id: x-bar-theory
  type: hard
builds-toward:
- syntax-semantics-interface-formal
tags:
- syntax
- grammar-formalism
- context-free
- phrase-structure
stage: advanced
status: draft
---

# Phrase Structure Rules and Context-Free Grammars

## Core Idea
Phrase structure rules generate well-formed trees by specifying how syntactic nodes expand. Rules like NP → Det + N' formalize the recursive structure of phrases. Context-free grammars capture the vast majority of natural language syntax, though real grammars also require constraints on unbounded dependencies (movement, coordination, ellipsis) that context-free rules alone cannot express.

## Explainer

You've already worked with constituency tests, which let you identify what counts as a phrase — a unit that moves together, can be replaced by a pronoun, and appears in certain structural positions. You've also studied X-bar theory, which proposes a uniform template for phrase-internal structure. **Phrase structure rules** are the formal mechanism that ties these observations together: they are rewrite rules that specify exactly how each syntactic node can expand into its parts.

A phrase structure rule has the form X → Y Z, which means "a node of type X can be rewritten as (i.e., is composed of) a sequence Y followed by Z." For example, S → NP VP says that a sentence can be rewritten as a noun phrase followed by a verb phrase. VP → V NP says a verb phrase can be rewritten as a verb followed by a noun phrase. NP → Det N says a noun phrase can be rewritten as a determiner followed by a noun. Starting from S, applying these rules in sequence generates a tree — a **parse tree** — that shows the hierarchical structure of a sentence. "The cat chased the mouse" gets a tree with S at the root, branching to NP ("the cat") and VP ("chased the mouse"), and so on down to the individual words.

The power of phrase structure rules comes from **recursion**: the same category can appear on both sides of a rule. VP → V NP PP allows a verb phrase to contain a prepositional phrase; PP → P NP allows that prepositional phrase to contain another noun phrase, which could in turn contain another prepositional phrase. This is how "the cat sat on the mat near the house in the village by the river" is grammatical with no theoretical upper limit on length. A finite set of rules generates an infinite number of well-formed sentences — which is exactly what a formal grammar is supposed to do.

**Context-free grammars** (CFGs) are the mathematical class that phrase structure rules belong to. "Context-free" means that the expansion of a node doesn't depend on the surrounding context — VP always expands the same way regardless of what's next to it. CFGs are computationally tractable and capture most of English syntax efficiently. However, they run into trouble with certain constructions: **crossed dependencies** in languages like Swiss German (where verb agreement creates intersecting co-reference lines that a tree cannot represent), **unbounded movement** (where a word seems to originate in one position and appear in another — "Who did you say that she thought he liked?"), and **coordination** of unlike types. These phenomena motivated the move to more powerful formalisms — transformational grammar, Head-Driven Phrase Structure Grammar, Minimalism — but phrase structure rules remain the foundation from which those more complex systems depart. Understanding what context-free rules can and cannot do is the prerequisite for understanding why syntactic theory evolved the way it did.
