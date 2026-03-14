---
id: join-dependencies-fifth-nf
title: Join Dependencies and Fifth Normal Form
domain: computer-science
course: databases
prerequisites:
- id: multivalued-dependencies-fourth-nf
  type: hard
- id: database-normalization-3nf-bcnf
  type: hard
builds-toward:
- database-schema-design
- denormalization-strategy
tags:
- 5NF
- PJNF
- join-dependencies
- lossless-decomposition
stage: formal-systems
status: draft
---

# Join Dependencies and Fifth Normal Form

## Core Idea
Join dependencies generalize functional and multivalued dependencies to cases where a relation can be reconstructed from multiple projections without information loss. Fifth Normal Form (5NF, or Project-Join Normal Form) requires that only join dependencies implied by keys exist. While 5NF is the ultimate decomposition goal, most practical databases operate at BCNF; going beyond is rarely justified by the complexity it introduces.
