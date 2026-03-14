---
id: data-sharding-partitioning
title: Data Sharding and Partitioning Strategies
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-hash-tables
  type: hard
- id: consistent-hashing
  type: hard
tags:
- scalability
- partitioning
- sharding
stage: advanced
status: draft
---

# Data Sharding and Partitioning Strategies

## Core Idea
Data sharding partitions data across multiple nodes to enable horizontal scaling beyond a single machine's capacity. Range sharding assigns contiguous key ranges to nodes; hash sharding distributes based on hash(key) mod num_nodes; consistent hashing minimizes rebalancing when nodes join or leave. Each strategy involves tradeoffs in rebalancing cost, hot spot risk, and query efficiency.
