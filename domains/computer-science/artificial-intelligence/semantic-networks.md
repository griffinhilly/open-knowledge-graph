---
id: semantic-networks
title: Semantic Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: first-order-logic-ai
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward: []
tags:
- knowledge-representation
- conceptual-networks
- inference
stage: advanced
status: draft
---
# Semantic Networks

## Core Idea
Semantic networks represent knowledge as labeled directed graphs where nodes are concepts and edges represent relationships such as "is-a", "part-of", or "has-property". They enable inheritance (properties of a parent class apply to children) and path-based reasoning, though they are less expressive than first-order logic and can lead to ambiguity in reasoning.

## Questions

```yaml
- question: "A semantic network encodes that 'Bird can-fly' and 'Penguin is-a Bird.' A student adds a 'Penguin cannot-fly' property directly to the Penguin node. Which statement best describes how the network handles this exception?"
  type: multiple-choice
  options:
    - "The network raises a logical contradiction and cannot represent both facts simultaneously"
    - "The more specific (closer) property on Penguin overrides the inherited property from Bird, so Penguin cannot fly"
    - "The network ignores the exception because inherited properties always take precedence"
    - "The network requires the student to delete the 'Bird can-fly' edge before adding the exception"
  answer: 1
  explanation: "Semantic networks handle exceptions through specificity: more specific (closer in the inheritance hierarchy) properties override general inherited ones. The Penguin node's direct 'cannot-fly' property takes precedence over the 'can-fly' property inherited via the Bird is-a path. This is what makes semantic networks useful for default reasoning with exceptions — you can state the general rule once and add local overrides. Unlike FOL, there is no formal contradiction; specificity is the resolution principle. This approach breaks down, however, when two equally specific parents assign conflicting values."

- question: "In a semantic network with nodes for Animal, Dog, Fido, and edges 'Dog is-a Animal,' 'Animal has-property Has-Heart,' and 'Fido is-a Dog,' how does the network establish that Fido has a heart?"
  type: multiple-choice
  options:
    - "The network cannot establish this without an explicit 'Fido has-property Has-Heart' edge"
    - "By traversing the is-a edges upward from Fido → Dog → Animal and collecting has-property edges encountered along the path"
    - "By searching the entire graph for any node labeled 'Has-Heart' and connecting Fido to it directly"
    - "Fido inherits properties only from Dog, not from Animal, so it cannot inherit Has-Heart"
  answer: 1
  explanation: "Inheritance is the central mechanism of semantic networks. To find Fido's properties, traverse is-a edges upward: Fido is-a Dog, Dog is-a Animal, Animal has-property Has-Heart. Following this path, Fido inherits Has-Heart without needing an explicit edge. Inheritance propagates transitively through is-a chains of any length. This is more efficient than explicitly stating every property of every individual node, and it mirrors how humans organize taxonomic knowledge."

- question: "Semantic networks are equally expressive as first-order logic for representing knowledge — they simply use a graph notation instead of symbolic predicates and quantifiers."
  type: true-false
  answer: false
  explanation: "Semantic networks are significantly less expressive than first-order logic. FOL can express quantified statements ('All birds can fly except those that are penguins or ostriches'), negation, logical connectives, and explicit exception handling. Semantic networks cannot represent quantifiers or logical connectives directly — they rely on inheritance conventions rather than formal rules. Additionally, multiple inheritance conflicts (two parent classes assigning different values to the same property) have no principled resolution in semantic networks, whereas FOL can represent the same situation with explicit conditions. The tradeoff is that semantic networks are more intuitive and easier to traverse for simple hierarchical queries."

- question: "In a semantic network, a more specific node (lower in the is-a hierarchy) takes precedence over a more general ancestor when they assign conflicting property values."
  type: true-false
  answer: true
  explanation: "This specificity convention is how semantic networks handle exceptions in default reasoning. If 'Bird can-fly' and 'Penguin cannot-fly' are both encoded, the Penguin node's more specific (directly attached) property wins. The assumption is that exceptions are stated at the most specific applicable level, and the closer (more specific) value should reflect reality better than the inherited general rule. This works well for single-inheritance hierarchies but becomes unprincipled when multiple inheritance paths assign different values — the network has no formal way to decide which parent is 'more specific.'"

- question: "Why does multiple inheritance create a problem for semantic networks that does not arise in the same way in first-order logic, and what is the underlying reason?"
  type: short-answer
  answer: "In a semantic network, when a node inherits from two parent nodes that assign conflicting values to the same property, the specificity convention (closer wins) fails to resolve the conflict — both parents are equally close. The network has no principled mechanism to choose between them, creating ambiguity in any inference that depends on the disputed property. First-order logic handles this cleanly because it represents knowledge as explicit propositions with logical connectives; exceptions and conditions can be stated precisely with if-then rules and negation-as-failure or explicit exceptions. FOL can say 'X has property P unless Q holds,' whereas a semantic network has no syntax for such conditional overrides."
  explanation: "This limitation was a major motivation for developing more expressive knowledge representation formalisms like description logics and ontology languages (OWL), which have formal semantics and well-defined inference procedures that handle inheritance, exceptions, and disjunctions without ambiguity."
```

## Explainer

From your study of first-order logic, you know how to represent knowledge using predicates, quantifiers, and logical connectives — statements like ∀x(Bird(x) → CanFly(x)). This is precise and powerful, but it can be unwieldy for representing the kind of everyday knowledge that humans navigate effortlessly: "a robin is a bird," "birds have wings," "wings enable flight." **Semantic networks** represent this same knowledge as a labeled directed graph, where each concept is a node and each relationship is a labeled edge. The statement "a robin is a bird" becomes a node for Robin, a node for Bird, and a directed edge labeled "is-a" connecting them.

The most important feature of semantic networks is **inheritance through the is-a hierarchy**. If Bird has a "has-property" edge to Wings, and Robin has an "is-a" edge to Bird, then Robin automatically inherits the property Wings without needing to state it explicitly. This mirrors how humans organize knowledge taxonomically — you do not need to separately learn that every individual robin has wings, a beak, and feathers. You learn these facts about birds once, and every subclass inherits them. The graph structure from graph theory that you already understand makes this traversal natural: to find what properties a robin has, simply follow "is-a" edges upward and collect "has-property" edges along the way.

Semantic networks excel at representing **default reasoning** with exceptions. The general network might encode that birds can fly, but a specific "is-a" link from Penguin to Bird can override this with an explicit "cannot-fly" property. The convention is that more specific (closer) properties take precedence over inherited ones. This works intuitively for simple hierarchies but becomes problematic with **multiple inheritance** — if an object inherits from two parent classes that assign conflicting values to the same property, the network provides no principled way to resolve the conflict. This ambiguity is one reason semantic networks are considered less expressive than first-order logic, which can represent the same knowledge with explicit quantifiers and exception clauses.

Despite these limitations, semantic networks were foundational to AI knowledge representation and remain influential today. Their direct descendants include modern **knowledge graphs** like those powering search engines and recommendation systems, where billions of entity-relationship-entity triples (essentially semantic network edges) encode facts about the world. The intuitive visual structure makes semantic networks an excellent tool for organizing domain knowledge, even when the formal reasoning tasks require translation into a more rigorous representation.
