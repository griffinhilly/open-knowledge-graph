---
id: bcnf-higher-normalization
title: Boyce-Codd Normal Form and Higher Normal Forms
domain: computer-science
course: databases
prerequisites:
- id: normalization-first-second-third
  type: hard
builds-toward:
- denormalization-strategy
tags:
- BCNF
- normalization
- higher normal forms
- 4NF
- 5NF
stage: formal-systems
status: draft
---

# Boyce-Codd Normal Form and Higher Normal Forms

## Core Idea
Boyce-Codd Normal Form (BCNF) is a stricter form of 3NF where every determinant is a candidate key. Fourth and Fifth Normal Forms address multivalued and join dependencies. While theoretically superior, BCNF and higher forms may not always be practical; understanding when to stop normalizing is crucial.
