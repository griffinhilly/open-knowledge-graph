---
id: document-databases
title: Document Databases
domain: computer-science
course: databases
prerequisites:
- id: nosql-concepts
  type: hard
- id: database-schema-design
  type: soft
tags:
- document database
- MongoDB
- JSON
- BSON
- schema-free
- embedded documents
- denormalization
stage: formal-systems
status: validated
---

# Document Databases

## Core Idea
Document databases store data as self-contained, hierarchical documents (typically JSON or BSON) that can contain nested objects and arrays, eliminating the need for joins to access related data. Documents in the same collection may have different fields (schema-flexible), enabling fast iteration during development. Queries match documents by field values and can address nested fields using dot notation. The design philosophy encourages embedding related data within a single document — trading write-time redundancy for fast, join-free reads aligned with specific access patterns.

## How It's Best Learned
Model a blog (posts with embedded comments and tags) in both a relational schema and a document schema. Query for common patterns (get all comments on a post, get all posts by an author) and compare verbosity and execution.

## Common Misconceptions
- Schema-free does not mean schema-less in practice — applications enforce implicit schemas through code, and schema migrations still happen.
- Embedding all related data in one document can cause document bloat and inefficient partial updates; referencing (linking by ID) is sometimes the better choice.
- Document databases handle multi-document transactions poorly compared to relational databases — single-document operations are atomic, but cross-document atomicity requires careful design.

## Questions

```yaml
- question: "An e-commerce platform embeds full customer information (name, address, email) inside every order document. A customer updates their shipping address. What problem does this create?"
  type: multiple-choice
  options:
    - "The update fails because document databases do not support partial document updates"
    - "Every order document containing the old address must be updated, creating write-side redundancy across potentially thousands of records"
    - "The schema-free nature of document databases prevents field-level updates"
    - "Nothing — embedding is always the correct approach for data that is read together"
  answer: 1
  explanation: "This is the classic write-side redundancy problem caused by embedding data that is shared and updated independently. When customer info is embedded in every order, a single address change requires updating every order document — a potentially expensive scatter-update. This is why shared, frequently-updated data is better *referenced* (storing a customer ID and resolving it in application code) rather than embedded. The decision depends on access pattern: if orders always display the address as-of-order-time and never need the current address, embedding might be intentional."

- question: "A developer says their document database application has 'no schema' and therefore requires no schema migrations. Why is this claim misleading?"
  type: multiple-choice
  options:
    - "It is not misleading — document databases truly have no schema requirements"
    - "The database has no schema, but the application code enforces an implicit schema by expecting specific fields and types; evolving that code is effectively a schema migration"
    - "Document databases have schemas stored in a separate metadata collection that must be updated"
    - "Schema migrations are only required when adding new collections, not when modifying fields"
  answer: 1
  explanation: "Schema flexibility means the storage engine doesn't enforce field presence or types — any document can have any fields. But the application code that reads those documents absolutely expects certain fields to exist with certain types. When you add a required field or change a type, every document that doesn't conform will cause application errors. Migrating all existing documents (or handling the missing-field case in code) is functionally a schema migration. Libraries like Mongoose make this implicit schema explicit at the application layer."

- question: "Operations on a single document in a document database are guaranteed to be atomic."
  type: true-false
  answer: true
  explanation: "Atomicity at the document level is a core guarantee of document databases — you will never see a document in a half-updated state. This is intentional: since a document is the unit of data retrieval, it should also be the unit of consistency. The critical consequence is that your document boundaries become your consistency boundaries. If two related pieces of data need to update atomically, they must either be in the same document or you must use the database's multi-document transaction support (with its associated overhead)."

- question: "Embedding all related data in one document is always preferable to referencing because it eliminates joins and makes reads faster."
  type: true-false
  answer: false
  explanation: "Embedding is the right choice when data is always read together, is owned by the parent document, and doesn't grow unboundedly. But it causes problems when the embedded data is shared across many documents (requiring scattered updates), when it changes frequently and independently, or when it grows large (document bloat makes every read fetch more data than needed). The correct principle is to model based on access patterns: embed what is read together, reference what is updated independently or shared. There is no universally correct choice."

- question: "How should you decide whether to embed related data inside a document or reference it by ID, and what are the key tradeoffs?"
  type: short-answer
  answer: "Embed when the related data is always read together with the parent, is owned exclusively by that document, has bounded size, and is updated atomically with the parent. Reference when the related data is shared across many documents, changes frequently and independently, grows without bound, or needs to be updated without touching the parent. The tradeoff: embedding gives fast single-read access but creates write-side redundancy for shared data; referencing avoids redundancy but requires application-level join logic and extra queries."
  explanation: "This decision is the central modeling skill in document databases and has no universal answer. The guiding question is always: which queries does my application run most often, and how does my data change? A comment embedded in a blog post is always read with the post and edited rarely — embed it. A product category shared across thousands of product documents and renamed regularly — reference it. The document boundary is also the atomicity boundary, so consistency requirements also influence the choice."
```

## Explainer

Coming from relational databases and the NoSQL concepts you already know, document databases represent a fundamentally different way of thinking about data modeling. Instead of spreading related data across multiple tables linked by foreign keys and reassembled with JOINs, a document database stores related data together in a single **document** — a self-contained, hierarchical structure typically represented as JSON or BSON (Binary JSON). A blog post document might contain the title, body, author info, an array of tags, and an array of comment objects, all nested inside one structure. To display the post, you fetch one document — no joins required.

This **embedding** strategy directly trades normalization for read performance. In a relational schema, displaying that blog post might require joining four tables (posts, authors, tags, comments). In a document database, it's a single read by document ID. The tradeoff is write-side complexity: if the author changes their display name, you may need to update that name in every document where it's embedded. This is why document modeling requires thinking carefully about **access patterns** — which queries will you run most often? Data that is always read together should be embedded; data that is shared across many documents or updated independently should be **referenced** by storing an ID and resolving it in application code.

Documents within the same **collection** (the document database analog of a table) do not need to share the same structure. One product document might have a "dimensions" field while another has a "download_size" field. This **schema flexibility** accelerates early development — you can evolve your data model without running ALTER TABLE migrations. In practice, however, applications enforce an implicit schema through code: your application expects certain fields to exist and have certain types. Libraries like Mongoose (for MongoDB) formalize this with schema definitions at the application layer, recovering some of the structure that relational databases enforce at the storage layer.

The most important limitation to understand is the **transaction boundary**. Operations on a single document are atomic — the database guarantees you won't see a half-updated document. But operations that span multiple documents lack this guarantee by default. If you need to transfer money between two accounts stored as separate documents, you must either restructure your data so both accounts live in one document, use the database's multi-document transaction support (which carries performance overhead), or accept the risk of partial updates. This is the central design tension in document databases: the unit of atomicity is the document, so your document boundaries are also your consistency boundaries.
