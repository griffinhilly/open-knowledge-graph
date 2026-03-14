---
id: encapsulation-and-protocol-layers
title: Encapsulation and Protocol Layers
domain: computer-science
course: computer-networking
prerequisites:
- id: osi-model-layers
  type: hard
builds-toward:
- error-detection-and-correction
tags:
- layering
- encapsulation
- protocol-stack
- headers
stage: advanced
status: draft
---

# Encapsulation and Protocol Layers

## Core Idea
Each layer in the protocol stack encapsulates data from the layer above by prepending its own header, creating a nested structure of headers and payload. When data moves down the stack, each layer adds headers; when it moves up, each layer removes its headers. This encapsulation allows protocols to operate independently while maintaining the abstraction boundaries that define the layered architecture.
