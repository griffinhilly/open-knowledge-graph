---
id: knowledge-graphs
title: Knowledge Graphs
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: first-order-logic-ai
  type: hard
- id: relational-data-model
  type: soft
- id: graph-adjacency-list-matrix-representations
  type: soft
builds-toward:
- semantic-networks
tags:
- knowledge-representation
- semantic-web
- entities
- relations
stage: advanced
status: validated
---

# Knowledge Graphs

## Core Idea
Knowledge graphs represent facts as triples (subject, relation, object) forming a semantic network where entities and relationships form a queryable graph structure. They enable structured knowledge representation for semantic search, question answering, and recommendation systems; subgraph matching and embedding methods enable reasoning over incomplete graphs. Knowledge graphs power modern AI systems from search engines to virtual assistants.

## How It's Best Learned
Work with a knowledge graph library (RDF/SPARQL) to store and query facts, then implement basic inference rules to derive new facts.

## Questions

```yaml
- question: "A knowledge graph contains the facts (Einstein, bornIn, Ulm) and (Ulm, locatedIn, Germany). A query system returns the fact (Einstein, bornIn, Germany) even though this triple was never explicitly stored. What capability is being demonstrated?"
  type: multiple-choice
  options:
    - "Entity resolution — the system recognized that Ulm and Germany are the same entity"
    - "Inference — the system applied a transitivity rule to derive a new fact from existing ones"
    - "Link prediction — a trained embedding model probabilistically guessed the relationship"
    - "SPARQL querying — the system retrieved a stored triple using pattern matching"
  answer: 1
  explanation: "This is inference: the system applied a rule analogous to transitivity — if X is bornIn Y and Y is locatedIn Z, then X is bornIn Z. The triple was never stored explicitly; it was derived. This distinguishes knowledge graphs from simple databases. Entity resolution would recognize that two different names refer to the same entity. Link prediction uses embeddings to estimate missing relationships probabilistically. SPARQL would retrieve explicit triples but cannot derive new ones without inference rules."

- question: "How does querying a knowledge graph differ most fundamentally from querying a traditional relational database containing the same factual information?"
  type: multiple-choice
  options:
    - "Knowledge graphs store data more efficiently because they avoid redundant columns"
    - "Knowledge graph queries can follow arbitrary chains of relationships without predefined joins, enabling traversal of unknown graph depth"
    - "Knowledge graphs can only answer yes/no questions, while relational databases support aggregation"
    - "Relational databases cannot store relationship data, only entity attributes"
  answer: 1
  explanation: "The key difference is structural flexibility. Relational databases require predefined schema and explicit JOIN operations for each relationship level. A knowledge graph with SPARQL lets you traverse any relationship path dynamically — 'find all intellectual descendants of Aristotle through any number of Taught edges' is natural in SPARQL but requires a recursive CTE or iterative query in SQL. The graph structure enables multi-hop reasoning over paths of arbitrary length."

- question: "A knowledge graph that contains most currently known facts is functionally complete — adding inference rules would mainly produce redundant information already present in the graph."
  type: true-false
  answer: false
  explanation: "Knowledge graphs are almost always incomplete — real-world knowledge graphs like Wikidata and Freebase contain millions of missing relationships. Inference rules are not just redundant shortcuts; they derive facts that are implicitly entailed but not explicitly stored, expanding the effective knowledge of the system. Furthermore, knowledge graph embedding methods are designed precisely to predict these missing links with probabilistic confidence scores, making incompleteness a central problem rather than an edge case."

- question: "Knowledge graph embeddings can assign probability scores to potentially missing (subject, relation, object) triples, even if those triples were never explicitly present in the graph during training."
  type: true-false
  answer: true
  explanation: "This is the core capability of link prediction via embeddings. Methods like TransE, DistMult, and RotatE learn vector representations of entities and relations such that valid triples score higher than invalid ones. Once trained, the model can score any candidate triple — even ones never seen during training — based on the geometric relationship of their learned embeddings. This bridges symbolic knowledge representation with statistical machine learning."

- question: "Why is entity resolution a necessary component of large-scale knowledge graphs that aggregate data from multiple sources?"
  type: short-answer
  answer: "Different sources use different names for the same real-world entity — 'Albert Einstein,' 'A. Einstein,' and 'Einstein' may all refer to the same person. Without entity resolution, the graph treats these as distinct nodes, fragmenting knowledge about the same entity across multiple disconnected representations. Queries about Einstein would miss facts stored under alternate names, and inference rules would fail to connect related facts. Entity resolution maps these surface-level variants to a single canonical identifier, ensuring the graph's connectivity reflects real-world relationships rather than naming accidents."
  explanation: "This problem scales dramatically with graph size. Wikidata and Google's Knowledge Graph invest enormous engineering effort in entity resolution, including techniques from string matching to machine learning classifiers trained on contextual evidence. Without it, the knowledge graph's usefulness for question answering and semantic search degrades substantially."
```

## Questions

```yaml
- question: "A knowledge graph contains (Einstein, bornIn, Ulm) and (Ulm, locatedIn, Germany). Without any inference rules configured, what does a SPARQL query for 'Where was Einstein born?' return?"
  type: multiple-choice
  options:
    - "Germany — the graph automatically applies transitivity to infer the broader location"
    - "Ulm — only explicitly stored triples are returned; inference requires explicitly configured rules or ontologies"
    - "Both Ulm and Germany — knowledge graphs return all logically derivable answers by default"
    - "Nothing — the query requires natural language processing unavailable in SPARQL"
  answer: 1
  explanation: "A knowledge graph is not an inference engine by default — it is a store of explicit triples. Returning 'Germany' requires an explicitly applied transitivity rule (e.g., via OWL reasoning or a SPARQL CONSTRUCT query). This is the key distinction between what is *stored* and what can be *inferred*. Students often assume KGs automatically reason over all implied facts; in practice, inference requires deliberate configuration of ontology rules."

- question: "To find all colleagues of a person who have won a Nobel Prize, a knowledge graph query would:"
  type: multiple-choice
  options:
    - "Perform a two-table JOIN on a 'colleagues' table and an 'awards' table"
    - "Traverse 'colleague' edges from the person node, then check each neighbor for 'wonAward' edges pointing to Nobel Prize nodes"
    - "Search all triples where the person appears as a subject"
    - "Query a single triple (person, nobelPrize, ?) directly"
  answer: 1
  explanation: "The power of the graph representation is multi-hop traversal: follow one type of edge, then follow another. This is natural in a graph (two hops along typed edges) but requires explicit JOINs in a relational model. Option A describes the relational approach; in a knowledge graph, the structure itself enables this pattern without schema-defined join tables. This is why graph queries can express relationship chains that would require multiple JOINs in SQL."

- question: "Knowledge graph embeddings represent entities and relations as continuous vectors, enabling prediction of relationships that were never explicitly stored as triples."
  type: true-false
  answer: true
  explanation: "Embedding methods (TransE, DistMult, ComplEx, etc.) learn vector representations such that the geometric relationship between entity and relation vectors encodes semantic relationships. A trained model can score candidate triples and predict likely missing links — for example, inferring that two drugs probably share a molecular target even if that fact isn't in the graph. This is how knowledge graphs bridge symbolic reasoning with statistical machine learning."

- question: "A knowledge graph and a relational database are equivalent in what they can represent: both use tables of facts and support the same query operations."
  type: true-false
  answer: false
  explanation: "While both can technically encode the same facts, knowledge graphs differ in key ways. The triple store's flexible schema allows adding new relation types without altering a table schema. More importantly, graph queries natively express arbitrary-depth path traversal (multi-hop relationships) without predefined joins, and ontologies (RDF Schema, OWL) enable symbolic inference over class hierarchies and property constraints. These capabilities make knowledge graphs especially suited to heterogeneous, evolving knowledge where relationships are themselves first-class objects."

- question: "What role does entity resolution play in a knowledge graph, and why is it necessary when building large-scale graphs from multiple sources?"
  type: short-answer
  answer: "Entity resolution (also called entity linking or deduplication) is the process of identifying when different names, identifiers, or descriptions in different data sources refer to the same real-world entity. For example, 'Albert Einstein,' 'A. Einstein,' and 'Einstein, Albert' in three different datasets must be recognized as the same node. Without entity resolution, the graph contains duplicate nodes for the same entity, breaking traversal and inference — a query about Einstein's publications would miss results from sources that used a different string. Large KGs like Wikidata solve this by assigning canonical entity IDs and maintaining aliases."
  explanation: "This tests whether students understand the practical engineering challenges of building a knowledge graph, not just its abstract structure. The key insight is that the power of a KG depends on the graph being connected correctly — duplicate nodes for the same entity sever the chains that enable multi-hop queries and inference. Entity resolution is what transforms a collection of independent triples into a coherent semantic network."
```

## Explainer

You already know from first-order logic that knowledge can be expressed as predicates over objects — `Teaches(Socrates, Plato)` or `CapitalOf(France, Paris)`. A **knowledge graph** takes this idea and makes it concrete: every fact becomes a **triple** of the form (subject, relation, object), and the collection of all such triples forms a directed graph. Entities are nodes, relations are labeled edges. If you have worked with relational databases, think of it as a single universal table with three columns — subject, predicate, object — where every row is one fact about the world.

The power of this representation comes from its graph structure. From graph theory, you know that graphs support traversal, path-finding, and pattern matching. In a knowledge graph, these operations become semantic queries. To answer "Who were Socrates' intellectual grandchildren?" you traverse two `Teaches` edges. To find indirect connections between two drugs, you look for paths through shared molecular targets. The query language **SPARQL** lets you express these graph patterns declaratively, much like SQL does for relational tables but with the flexibility to follow arbitrary relationship chains without predefined joins.

What makes knowledge graphs more than just databases of triples is **inference** — deriving new facts from existing ones. If the graph contains `BornIn(Einstein, Ulm)` and `LocatedIn(Ulm, Germany)`, a rule can infer `BornIn(Einstein, Germany)` through transitivity. This is where your first-order logic background pays off directly: inference rules in knowledge graphs are essentially Horn clauses applied to the triple store. Ontologies like **RDF Schema** and **OWL** formalize these rules, defining class hierarchies (`Scientist subClassOf Person`) and property constraints (`hasMother` is functional — each person has exactly one) that let the system reason about types and relationships automatically.

Modern knowledge graphs also handle the messiness of real-world data. Entities from different sources may refer to the same thing under different names — a process called **entity resolution**. Facts may be uncertain or contradictory. **Knowledge graph embeddings** address this by learning continuous vector representations of entities and relations, enabling link prediction: given `(Einstein, ?)` and a trained model, you can predict missing relations with probability scores. This bridges symbolic reasoning (your logic background) with statistical learning, which is why knowledge graphs sit at the intersection of classical AI and modern machine learning. Google's Knowledge Graph, Wikidata, and biomedical ontologies like SNOMED CT are all large-scale examples powering search, drug discovery, and question answering today.
