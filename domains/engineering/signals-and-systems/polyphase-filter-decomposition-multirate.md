---
id: polyphase-filter-decomposition-multirate
title: Polyphase Filter Decomposition and Structure
domain: engineering
course: signals-and-systems
prerequisites:
- id: multirate-decimation-interpolation
  type: hard
builds-toward:
- decimation-anti-aliasing-and-downsampling
- interpolation-filtering-image-rejection
tags:
- polyphase
- multirate
- decomposition
- efficiency
stage: abstract-reasoning
status: draft
---

# Polyphase Filter Decomposition and Structure

## Core Idea
Polyphase decomposition factors a filter into M subfilters (for decimation by M) or K subfilters (for interpolation by K), each operating at the lower or higher rate. This reduces computation by moving downsampling/upsampling before filtering, avoiding computations discarded in decimation. Polyphase structures are computationally efficient for multirate signal processing and form the basis of practical audio codecs and multirate systems.

## How It's Best Learned
Decompose a 64-tap FIR filter for 4:1 decimation into 4 polyphase subfilters. Compare computational complexity of direct decimation vs polyphase form.

## Common Misconceptions
- Thinking polyphase changes the filtering operation (it's a reorganization, not modification).
- Confusing polyphase decomposition with parallel filter structures.
- Not recognizing that polyphase enables real-time multirate processing.
