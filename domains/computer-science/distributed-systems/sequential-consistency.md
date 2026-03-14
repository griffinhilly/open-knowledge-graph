---
id: sequential-consistency
title: Sequential Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- read-after-write-consistency
- strong-eventual-consistency
tags:
- consistency
- ordering
- formal-semantics
stage: advanced
status: draft
---

# Sequential Consistency

## Core Idea
Sequential consistency guarantees that there exists a total order on all operations that respects the program order of each individual process. Unlike linearizability, this total order does not have to correspond to real time—operations can appear to execute in any order as long as each process's sequence is preserved. This weaker model can be more efficient to implement.
