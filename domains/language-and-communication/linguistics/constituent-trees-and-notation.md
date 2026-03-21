---
id: constituent-trees-and-notation
title: Constituent Trees and Formal Notation
domain: language-and-communication
course: linguistics
prerequisites:
- id: symbolic-representation-linguistics
  type: hard
- id: constituency-and-phrases
  type: soft
builds-toward:
- derivation-vs-generation
- x-bar-theory
tags:
- syntax
- representation
- tree-structures
stage: formal-systems
status: draft
---

# Constituent Trees and Formal Notation

## Core Idea
Constituent structure is formally represented as labeled trees where nodes represent phrases and edges represent dominance relations. Notational systems (brackets, indented lists, line diagrams) make trees explicit and computationally processable.

## Questions

```yaml
- question: "The sentence 'I saw the man with the telescope' has two distinct interpretations. In constituent tree notation, how is this structural ambiguity represented?"
  type: multiple-choice
  options:
    - "One tree, with the word 'with' marked as lexically ambiguous"
    - "Two trees with identical structures but different word labels at the PP node"
    - "Two trees in which the PP 'with the telescope' attaches to different nodes — either inside the VP or inside the NP"
    - "One tree with a dotted edge showing the optional attachment of 'with the telescope'"
  answer: 2
  explanation: "Structural ambiguity arises from different constituency structures, not from ambiguous words. In reading 1 (you used the telescope to see), the PP 'with the telescope' attaches inside the VP as a modifier of the verb 'saw.' In reading 2 (the man had the telescope), the PP attaches inside the NP 'the man with the telescope.' These are two different trees with different dominance relations — the same string of words, two distinct hierarchical structures. This is exactly why formal notation is useful: it makes the source of the ambiguity explicit and unambiguous."

- question: "A student argues: 'Bracket notation like [S [NP the cat] [VP sat]] is just shorthand for the tree diagram; the tree diagram shows more information because you can see the hierarchy visually.' This claim is:"
  type: multiple-choice
  options:
    - "Correct — tree diagrams encode dominance relations that linear brackets cannot express"
    - "Incorrect — both representations encode exactly the same structural information; visual clarity differs but information content is identical"
    - "Correct — bracket notation cannot represent non-binary branching structures"
    - "Incorrect — bracket notation is actually more expressive because it specifies word order more precisely"
  answer: 1
  explanation: "Tree diagrams and bracket notation are equivalent representations — they are two different notations for the same formal object. Every dominance relation visible in the tree is encoded in the nesting structure of the brackets, and vice versa. The labels on nodes appear as labels inside brackets. The branching structure appears as nesting depth. A skilled linguist reads structural information from bracket notation just as efficiently as from a tree. The student confuses visual ease of reading with information content."

- question: "Structural ambiguity in a sentence occurs when one or more of the words in the sentence has multiple meanings."
  type: true-false
  answer: false
  explanation: "That describes lexical ambiguity, not structural ambiguity. Structural ambiguity arises when a single string of words — with all words having fixed, unambiguous meanings — can be assigned two distinct constituent structures (trees). 'I saw the man with the telescope' is structurally ambiguous because the PP can attach in two different places in the hierarchy; neither 'saw,' 'man,' nor 'telescope' is ambiguous as a word. The two readings come from different tree structures, not from different word meanings."

- question: "In a constituent tree, if node A dominates node B, then the phrase represented by A contains the phrase represented by B as a part."
  type: true-false
  answer: true
  explanation: "Dominance is the formal representation of structural containment. If NP dominates Det and N, then the noun phrase contains the determiner and noun. If S dominates NP and VP, then the sentence contains the noun phrase and the verb phrase. This is what makes trees useful: the hierarchy of domination relationships directly encodes which phrases are parts of which larger phrases, something that a flat sequence of words cannot capture."

- question: "Why is formal tree notation particularly useful for analyzing structural ambiguity, compared to describing the ambiguity in prose?"
  type: short-answer
  answer: "Formal trees make ambiguity precise and visible. A prose description can gesture at two readings ('he used the telescope' vs. 'the man had the telescope'), but it cannot pinpoint the structural source of the difference. Two trees with different attachment sites for the PP show exactly which grouping differs — and make it clear that the ambiguity is structural, not lexical. Trees also enable systematic comparison: any two readings of an ambiguous sentence are represented as two distinct formal objects that can be analyzed, compared, and used computationally."
  explanation: "Prose explanations are circular: 'it can mean X or Y' just restates the ambiguity without explaining it. Trees explain it by showing the two different structures that give rise to the two meanings. This is why formal notation is not just convenient but epistemically superior for syntactic analysis — it forces precision about what the structural options actually are and excludes hand-waving."
```

## Explainer

You already know from symbolic representation that linguistic structures can be expressed formally rather than just intuitively, and from constituency and phrases that a sentence is not a flat string of words — it is a **hierarchical structure** in which words group into phrases, and phrases group into larger phrases. Constituent trees are the primary formal tool for making that hierarchy explicit. A tree diagram takes the implicit groupings that a fluent speaker feels and renders them visible, precise, and manipulable.

In a constituent tree, each **node** represents a unit — either a terminal (an individual word) or a non-terminal (a phrase). Non-terminal nodes are **labeled** with their syntactic category: NP for noun phrase, VP for verb phrase, PP for prepositional phrase, S for sentence. The **edges** connecting nodes represent the **dominance relation**: a higher node immediately dominates the nodes directly below it. Domination means containment — the VP node dominates the verb and every element inside the verb phrase. This is structural containment made visible and formal.

Consider "The old man saw the cat." The tree has an S node at the top, which branches into two daughters: an NP ("The old man") and a VP ("saw the cat"). The NP branches further into a determiner, an adjective, and a noun; the VP branches into a verb and another NP. **Bracket notation** encodes the identical structure linearly: [S [NP The old man] [VP saw [NP the cat]]]. Trees are visually clearer for human reading; brackets are easier to type and process computationally. Both representations carry exactly the same structural information — learning to move fluently between them is a core skill.

The power of formal notation becomes clear when you encounter **structural ambiguity**. "I saw the man with the telescope" can have two distinct structures: either "with the telescope" attaches inside the VP (you used the telescope to see him) or inside the NP (he had the telescope). Two different trees, one string of words. The ambiguity that native speakers feel intuitively maps precisely onto two distinct structural descriptions, and drawing both trees makes the source of the ambiguity transparent in a way that prose explanation cannot. Formal notation thus enables systematic reasoning about structure — and provides the foundation for computational parsing and for formal syntactic theories like X-bar theory.
