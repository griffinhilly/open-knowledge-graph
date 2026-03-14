---
id: nosql-data-models-scalability
title: 'NoSQL Data Models: Document, Key-Value, Columnar, and Graph'
domain: computer-science
course: databases
prerequisites:
- id: nosql-concepts
  type: hard
- id: relational-data-model
  type: soft
builds-toward:
- distributed-replication-consistency-models
tags:
- NoSQL
- document
- key-value
- columnar
- graph
stage: formal-systems
status: draft
---

# NoSQL Data Models: Document, Key-Value, Columnar, and Graph

## Core Idea
NoSQL databases trade strict consistency for scalability and flexibility. Document stores (MongoDB, CouchDB) store flexible JSON-like structures without enforcing schemas. Key-value stores (Redis, DynamoDB) provide ultra-fast lookups but limited query flexibility. Column-oriented databases (BigTable, HBase) store data by column, excelling at analytics. Graph databases store relationships explicitly. Each model involves trade-offs suited to different workloads.
