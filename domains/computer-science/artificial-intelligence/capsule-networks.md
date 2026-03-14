---
id: capsule-networks
title: Capsule Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: convolutional-neural-networks
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- 3d-vision
- routing-algorithms
tags:
- capsule-network
- capsnet
- routing
stage: advanced
status: draft
---

# Capsule Networks

## Core Idea
Capsule networks replace scalar neurons with vector-valued capsules encoding domain-specific properties (position, rotation). Routing-by-agreement algorithms dynamically route information based on capsule predictions. CapsNets improve viewpoint equivariance and reduce data requirements compared to CNNs, though computation is higher.
