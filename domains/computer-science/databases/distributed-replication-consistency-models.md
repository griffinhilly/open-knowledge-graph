---
id: distributed-replication-consistency-models
title: 'Distributed Databases: Replication Models and Consistency'
domain: computer-science
course: databases
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: cap-theorem
  type: hard
builds-toward:
- nosql-data-models-scalability
tags:
- replication
- consistency
- distributed
- sync
- async
stage: formal-systems
status: draft
---

# Distributed Databases: Replication Models and Consistency

## Core Idea
Distributed databases replicate data across sites for fault tolerance and scalability. Synchronous replication waits for replica acknowledgment before committing, ensuring strong consistency but reducing throughput. Asynchronous replication commits locally and updates replicas later, allowing higher throughput but risking inconsistency. Quorum replication requires acknowledgment from a majority, balancing consistency and availability. Understanding replication models is essential for choosing appropriate consistency levels.
