---
id: homotopy-definition
title: Homotopy of Continuous Maps
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-definition
  type: hard
- id: path-connected-spaces
  type: soft
builds-toward:
- fundamental-group-definition
tags:
- homotopy
- algebraic-topology
stage: abstract-reasoning
status: draft
---

# Homotopy of Continuous Maps

## Core Idea
Maps f, g: X → Y are homotopic if there exists a continuous map H: X × [0,1] → Y with H(x,0) = f(x) and H(x,1) = g(x). Homotopy measures when maps are 'continuously deformable.' Homotopy equivalence is weaker than homeomorphism but strong enough to detect topological structure. Fundamental groups and higher homotopy groups are invariants of homotopy type.
