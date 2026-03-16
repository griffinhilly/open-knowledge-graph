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

## Explainer

You already know the basics of NoSQL — that it emerged as an alternative to relational databases for workloads where rigid schemas, complex joins, and vertical scaling become bottlenecks. The next step is understanding the four major NoSQL data models and recognizing which problems each one solves best. The unifying theme is that each model optimizes for a specific **access pattern** by giving up the general-purpose query flexibility that relational databases provide.

**Key-value stores** are the simplest model: every piece of data is stored as a value associated with a unique key, like a giant dictionary or hash map. Redis, Memcached, and DynamoDB (in its simplest mode) follow this pattern. You can GET a value by key and PUT a value at a key — that is essentially the entire API. This radical simplicity enables extreme performance (sub-millisecond reads) and easy horizontal scaling (partition data across machines by hashing the key). The tradeoff is that you cannot query by anything other than the key. If you need to find all users in a particular city, you must either maintain a secondary index yourself or scan every entry. Key-value stores excel as caches, session stores, and real-time leaderboards — any workload dominated by direct lookups.

**Document stores** like MongoDB and CouchDB extend the key-value idea by making the value a structured document — typically JSON or BSON — that the database can inspect and index. You can query by fields inside the document ("find all users where city = 'Portland'"), create indexes on nested fields, and store complex objects in a single document without joining across tables. This **denormalized** approach means that a single read retrieves everything an application needs, avoiding the multi-table joins that slow down relational databases at scale. The tradeoff is data duplication: if the same address appears in many documents, updating it requires changing every copy. Document stores work best when data has a natural document boundary — user profiles, product catalogs, content management systems — where each document is relatively self-contained.

**Column-family stores** (BigTable, HBase, Cassandra) organize data by columns rather than rows. Physically, all values for a single column are stored contiguously on disk. This makes analytical queries that scan a single column across millions of rows — "compute the average order amount" — extremely fast because the disk reads only the relevant data. Row-oriented databases would read entire rows and discard the irrelevant columns. **Graph databases** (Neo4j, Amazon Neptune) take a completely different approach by storing **nodes** (entities) and **edges** (relationships) as first-class citizens. Traversing relationships — "find all friends-of-friends who also like jazz" — is a constant-time pointer hop per edge, whereas a relational database would need recursive joins that grow expensive with depth. Graph databases excel at social networks, recommendation engines, and fraud detection where relationship traversal is the primary operation. The key insight across all four models is that NoSQL is not one thing — it is a family of specialized tools, each making a deliberate tradeoff between flexibility, consistency, and performance for a particular class of workload.
