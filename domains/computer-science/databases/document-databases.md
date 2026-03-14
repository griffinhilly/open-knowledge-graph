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
