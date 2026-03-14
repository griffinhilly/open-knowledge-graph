---
id: content-based-filtering
title: Content-Based Filtering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recommendation-systems
  type: hard
- id: feature-engineering-selection
  type: soft
builds-toward:
- hybrid-recommendation
tags:
- content-based
- item-features
- user-profile
stage: advanced
status: draft
---

# Content-Based Filtering

## Core Idea
Content-based filtering recommends items similar to those a user previously liked, using rich item features (genre, actors, keywords). User profiles aggregate interaction history; recommendations match profiles to item features using similarity metrics. This approach handles new items well but requires detailed metadata and can lead to narrow recommendations.
