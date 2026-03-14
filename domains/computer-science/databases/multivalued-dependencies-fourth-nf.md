---
id: multivalued-dependencies-fourth-nf
title: Multivalued Dependencies and Fourth Normal Form
domain: computer-science
course: databases
prerequisites:
- id: database-normalization-3nf-bcnf
  type: hard
- id: functional-dependencies
  type: hard
builds-toward:
- join-dependencies-fifth-nf
tags:
- 4NF
- multivalued-dependencies
- MVD
- normalization
stage: formal-systems
status: draft
---

# Multivalued Dependencies and Fourth Normal Form

## Core Idea
Multivalued dependencies occur when one column determines multiple independent set-valued attributes: if a course has independent lists of instructors and textbooks, storing all combinations creates redundancy and update anomalies. Fourth Normal Form (4NF) requires all non-trivial MVDs to also be functional dependencies. A relation in BCNF might still violate 4NF, requiring decomposition into separate relations.
