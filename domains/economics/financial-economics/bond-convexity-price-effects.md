---
id: bond-convexity-price-effects
title: Convexity and Non-Linear Price-Yield Relationships
domain: economics
course: financial-economics
prerequisites:
- id: duration-and-convexity
  type: hard
- id: bond-pricing
  type: soft
builds-toward:
- bond-duration-application
tags:
- bonds
- convexity
- interest-rate-sensitivity
- pricing
stage: formal-systems
status: draft
---

# Convexity and Non-Linear Price-Yield Relationships

## Core Idea
Bond prices are convex functions of yields: large yield changes violate the linear duration approximation. Convexity measures this curvature, and the full price change formula is: ΔP ≈ -D × Δy + (C/2) × (Δy)². Positive convexity means bond prices fall less when yields rise and rise more when yields fall, making long-duration bonds with high convexity especially attractive.

## How It's Best Learned
Compare actual bond price changes from large yield moves against duration-only approximations to see where convexity becomes important.
