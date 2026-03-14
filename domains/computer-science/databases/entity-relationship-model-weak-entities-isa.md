---
id: entity-relationship-model-weak-entities-isa
title: 'ER Model: Weak Entities and Specialization Hierarchies'
domain: computer-science
course: databases
prerequisites:
- id: entity-relationship-diagrams
  type: hard
builds-toward:
- er-to-relational-schema-conversion
tags:
- ER-model
- weak-entities
- specialization
- inheritance
- ISA
stage: formal-systems
status: draft
---

# ER Model: Weak Entities and Specialization Hierarchies

## Core Idea
The extended ER model includes weak entities (those requiring a strong entity for identity, like apartments within buildings) and specialization/generalization hierarchies (ISA relationships like Employee → FullTimeEmployee, PartTimeEmployee). These advanced constructs enable modeling of real-world structures with inheritance and dependency relationships that basic ER diagrams cannot express.
