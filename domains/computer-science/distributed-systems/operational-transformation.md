---
id: operational-transformation
title: Operational Transformation for Collaborative Editing
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: crdts-convergent-replicated-types
  type: soft
tags:
- collaboration
- conflict-resolution
- editing
stage: advanced
status: draft
---

# Operational Transformation for Collaborative Editing

## Core Idea
Operational transformation (OT) enables real-time collaborative editing by transforming concurrent edits to commute, ensuring all replicas converge. When edits arrive out of order, OT 'rewrites' them relative to other concurrent operations. This requires defining transformation functions for all operation pairs and carefully handling causality and intention preservation.
