---
id: knowledge-distillation
title: Knowledge Distillation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: ensemble-methods-advanced
  type: soft
builds-toward:
- model-compression
- student-teacher
tags:
- distillation
- teacher-student
- compression
stage: advanced
status: draft
---

# Knowledge Distillation

## Core Idea
Knowledge distillation transfers knowledge from large, accurate teacher models to smaller, faster student models by training students to mimic teacher outputs. Using soft probability distributions instead of hard labels provides richer supervision signals. Students achieve similar accuracy with orders of magnitude fewer parameters.
