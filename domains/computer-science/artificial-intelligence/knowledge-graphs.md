---
id: knowledge-graphs
title: Knowledge Graphs
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: first-order-logic-ai
  type: hard
- id: relational-model-basics
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- semantic-networks
tags:
- knowledge-representation
- semantic-web
- entities
- relations
stage: advanced
status: draft
---

# Knowledge Graphs

## Core Idea
Knowledge graphs represent facts as triples (subject, relation, object) forming a semantic network where entities and relationships form a queryable graph structure. They enable structured knowledge representation for semantic search, question answering, and recommendation systems; subgraph matching and embedding methods enable reasoning over incomplete graphs. Knowledge graphs power modern AI systems from search engines to virtual assistants.

## How It's Best Learned
Work with a knowledge graph library (RDF/SPARQL) to store and query facts, then implement basic inference rules to derive new facts.

## Explainer

You already know from first-order logic that knowledge can be expressed as predicates over objects — `Teaches(Socrates, Plato)` or `CapitalOf(France, Paris)`. A **knowledge graph** takes this idea and makes it concrete: every fact becomes a **triple** of the form (subject, relation, object), and the collection of all such triples forms a directed graph. Entities are nodes, relations are labeled edges. If you have worked with relational databases, think of it as a single universal table with three columns — subject, predicate, object — where every row is one fact about the world.

The power of this representation comes from its graph structure. From graph theory, you know that graphs support traversal, path-finding, and pattern matching. In a knowledge graph, these operations become semantic queries. To answer "Who were Socrates' intellectual grandchildren?" you traverse two `Teaches` edges. To find indirect connections between two drugs, you look for paths through shared molecular targets. The query language **SPARQL** lets you express these graph patterns declaratively, much like SQL does for relational tables but with the flexibility to follow arbitrary relationship chains without predefined joins.

What makes knowledge graphs more than just databases of triples is **inference** — deriving new facts from existing ones. If the graph contains `BornIn(Einstein, Ulm)` and `LocatedIn(Ulm, Germany)`, a rule can infer `BornIn(Einstein, Germany)` through transitivity. This is where your first-order logic background pays off directly: inference rules in knowledge graphs are essentially Horn clauses applied to the triple store. Ontologies like **RDF Schema** and **OWL** formalize these rules, defining class hierarchies (`Scientist subClassOf Person`) and property constraints (`hasMother` is functional — each person has exactly one) that let the system reason about types and relationships automatically.

Modern knowledge graphs also handle the messiness of real-world data. Entities from different sources may refer to the same thing under different names — a process called **entity resolution**. Facts may be uncertain or contradictory. **Knowledge graph embeddings** address this by learning continuous vector representations of entities and relations, enabling link prediction: given `(Einstein, ?)` and a trained model, you can predict missing relations with probability scores. This bridges symbolic reasoning (your logic background) with statistical learning, which is why knowledge graphs sit at the intersection of classical AI and modern machine learning. Google's Knowledge Graph, Wikidata, and biomedical ontologies like SNOMED CT are all large-scale examples powering search, drug discovery, and question answering today.
