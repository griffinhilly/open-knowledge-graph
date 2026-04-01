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
status: validated
---

# Phrase Structure Rules and Context-Free Grammars

## Core Idea
Phrase structure rules generate well-formed trees by specifying how syntactic nodes expand. Rules like NP → Det + N' formalize the recursive structure of phrases. Context-free grammars capture the vast majority of natural language syntax, though real grammars also require constraints on unbounded dependencies (movement, coordination, ellipsis) that context-free rules alone cannot express.

## Questions

```yaml
- question: "What feature of phrase structure rules allows a finite set of rules to generate an infinite number of grammatical sentences?"
  type: multiple-choice
  options:
    - "Each rule applies in parallel, so multiple derivations run simultaneously"
    - "Recursion: the same category can appear on both sides of a rule, embedding phrases inside phrases without limit"
    - "Context-sensitivity: rules change based on surrounding words, multiplying possible outputs"
    - "Each rule can be applied exactly once, but there are infinitely many rules in the grammar"
  answer: 1
  explanation: "Recursion is the key. A rule like VP → V NP PP allows a VP to contain a PP, and PP → P NP allows that PP to contain another NP, which can itself be expanded further. Because categories can appear on both sides of rules — generating structures that contain themselves — the same finite grammar produces infinitely long well-formed sentences. This is what distinguishes a formal grammar from a finite list of memorized sentences."

- question: "A linguist proposes the rule: 'VP can expand as V NP only when the NP immediately follows the subject noun phrase.' Why does this rule fall outside the class of context-free grammars?"
  type: multiple-choice
  options:
    - "Context-free grammars cannot include NPs in any rule"
    - "The expansion of VP depends on the surrounding context (the adjacent subject NP), violating the context-free requirement that a node expands the same way regardless of what surrounds it"
    - "Context-free grammars require that all rules be recursive, and this rule is not recursive"
    - "Context-free grammars do not allow verbs to precede noun phrases"
  answer: 1
  explanation: "'Context-free' means that a node's expansion is determined solely by the node's own category label — it does not depend on what is next to it in the tree. The proposed rule violates this: the VP can only expand as V NP if it is adjacent to a subject NP. That is a context-sensitive rule. CFGs are powerful precisely because expansions are local and independent of global structure, making them computationally tractable. Rules that require checking neighboring nodes belong to context-sensitive grammar formalisms."

- question: "Context-free grammars (CFGs) cannot adequately describe natural language syntax, because most natural languages require transformational rules to capture basic sentences."
  type: true-false
  answer: false
  explanation: "CFGs capture the vast majority of natural language syntax efficiently and are the foundation of most syntactic theory. The claim that CFGs are wholly inadequate is an overstatement. CFGs do have well-documented limitations — cross-serial dependencies in Swiss German, unbounded movement, certain coordination patterns — but these are edge cases, not the core of sentence structure. The correct position is that CFGs are powerful but not fully sufficient; more expressive formalisms (transformational grammar, Minimalism, HPSG) extend CFGs precisely because they need to handle these specific phenomena."

- question: "A phrase structure rule like S → NP VP is called 'context-free' because the expansion of S (into NP VP) is the same regardless of what other nodes surround S in the sentence structure."
  type: true-false
  answer: true
  explanation: "This is the defining property of context-free grammars. In a context-free rule, the left-hand side is a single non-terminal (here, S), and its expansion (NP VP) does not depend on any surrounding material. If expansion depended on what was adjacent — say, S only expands to NP VP when embedded in a certain clause type — the grammar would be context-sensitive. The 'context-free' label describes a formal property: the rewrite rule fires based solely on the node's own category."

- question: "What is the key limitation of context-free grammars that motivated the development of more powerful syntactic formalisms, and what kind of linguistic phenomenon illustrates this limitation?"
  type: short-answer
  answer: "CFGs cannot represent 'crossed dependencies' — co-reference relationships between words that create intersecting lines in the parse tree. Swiss German subordinate clauses, where subject-verb agreement creates dependencies that cross over each other, are the canonical example. CFGs can only represent nested (non-crossing) dependencies. Movement phenomena (wh-movement, topicalization) where a word appears far from its base position also challenge pure CFGs. These limitations motivated transformational grammar and other more expressive formalisms."
  explanation: "A tree — the output of phrase structure rules — is a planar hierarchical structure where no branches cross. This means CFGs can represent hierarchical nesting (A inside B inside C) but not the kind of interlocking dependencies found in Swiss German verb-argument patterns. Understanding what CFGs cannot do is as important as knowing what they can: every subsequent syntactic theory is a response to specific empirical limitations of context-free rules, and recognizing those limitations explains why syntactic theory evolved from simple phrase structure toward more powerful mechanisms."
```

## Explainer

You've already worked with constituency tests, which let you identify what counts as a phrase — a unit that moves together, can be replaced by a pronoun, and appears in certain structural positions. You've also studied X-bar theory, which proposes a uniform template for phrase-internal structure. **Phrase structure rules** are the formal mechanism that ties these observations together: they are rewrite rules that specify exactly how each syntactic node can expand into its parts.

A phrase structure rule has the form X → Y Z, which means "a node of type X can be rewritten as (i.e., is composed of) a sequence Y followed by Z." For example, S → NP VP says that a sentence can be rewritten as a noun phrase followed by a verb phrase. VP → V NP says a verb phrase can be rewritten as a verb followed by a noun phrase. NP → Det N says a noun phrase can be rewritten as a determiner followed by a noun. Starting from S, applying these rules in sequence generates a tree — a **parse tree** — that shows the hierarchical structure of a sentence. "The cat chased the mouse" gets a tree with S at the root, branching to NP ("the cat") and VP ("chased the mouse"), and so on down to the individual words.

The power of phrase structure rules comes from **recursion**: the same category can appear on both sides of a rule. VP → V NP PP allows a verb phrase to contain a prepositional phrase; PP → P NP allows that prepositional phrase to contain another noun phrase, which could in turn contain another prepositional phrase. This is how "the cat sat on the mat near the house in the village by the river" is grammatical with no theoretical upper limit on length. A finite set of rules generates an infinite number of well-formed sentences — which is exactly what a formal grammar is supposed to do.

**Context-free grammars** (CFGs) are the mathematical class that phrase structure rules belong to. "Context-free" means that the expansion of a node doesn't depend on the surrounding context — VP always expands the same way regardless of what's next to it. CFGs are computationally tractable and capture most of English syntax efficiently. However, they run into trouble with certain constructions: **crossed dependencies** in languages like Swiss German (where verb agreement creates intersecting co-reference lines that a tree cannot represent), **unbounded movement** (where a word seems to originate in one position and appear in another — "Who did you say that she thought he liked?"), and **coordination** of unlike types. These phenomena motivated the move to more powerful formalisms — transformational grammar, Head-Driven Phrase Structure Grammar, Minimalism — but phrase structure rules remain the foundation from which those more complex systems depart. Understanding what context-free rules can and cannot do is the prerequisite for understanding why syntactic theory evolved the way it did.
