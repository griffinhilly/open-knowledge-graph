---
id: eventual-consistency
title: Eventual Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- crdts-convergent-replicated-types
tags:
- eventual-consistency
- weak-consistency
- availability
stage: advanced
status: draft
---

# Eventual Consistency

## Core Idea
Eventual consistency guarantees that if no new writes occur, all replicas will converge to the same state. Writes succeed on any replica without waiting for others, providing high availability and partition tolerance. Applications must tolerate temporary divergence and resolve concurrent writes (conflict resolution), used widely in systems like Dynamo and Cassandra.
