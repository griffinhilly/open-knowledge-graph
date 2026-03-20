---
id: marginal-rate-technical-substitution
title: Marginal Rate of Technical Substitution (MRTS)
domain: economics
course: microeconomics
prerequisites:
- id: production-with-two-variable-inputs
  type: hard
builds-toward:
- cost-minimization-and-factor-demand
tags:
- substitution
- inputs
- technical-efficiency
stage: formal-systems
status: draft
---

# Marginal Rate of Technical Substitution (MRTS)

## Core Idea
The Marginal Rate of Technical Substitution (MRTS) is the rate at which a firm can reduce one input in exchange for another while maintaining the same output level. It equals the ratio of marginal products (MP_L / MP_K for labor and capital). Like consumer theory's MRS, MRTS is the slope of an isoquant and drives cost minimization decisions.

## How It's Best Learned
Compute MP for each input, then calculate MRTS = MP_L / MP_K. Verify it equals the slope of the isoquant.

## Explainer

In your study of production with two variable inputs, you worked with **isoquants** — the firm-side analog of consumer indifference curves. Each isoquant shows all combinations of labor (L) and capital (K) that produce the same output level. The **Marginal Rate of Technical Substitution (MRTS)** is the slope of that isoquant at any given point: it tells you how many units of capital the firm can give up in exchange for one more unit of labor while keeping output exactly constant. Just as the consumer's MRS measured the rate of substitution in preferences, MRTS measures the rate of substitution in production.

The key formula is MRTS_{L,K} = MP_L / MP_K. To see why, consider giving the firm one additional unit of labor. This adds MP_L units of output. To keep total output unchanged, the firm must simultaneously reduce capital by enough to subtract the same amount — which requires giving up MP_L / MP_K units of capital. That ratio is the MRTS. As the firm uses more labor and less capital, diminishing marginal returns cause MP_L to fall and MP_K to rise, so the MRTS falls. This is why isoquants are **convex to the origin** — they bow inward just like indifference curves — reflecting the increasingly costly substitution as inputs become unbalanced.

The practical use of MRTS is in cost minimization. A firm minimizes production cost at the input mix where MRTS = w/r, the **wage-rental ratio**. Intuitively: if MRTS > w/r, the firm is giving up more capital than the market requires in exchange for an extra unit of labor — so it should substitute labor for capital (getting more labor cheaply) until the rates equalize. This is the exact production-side parallel to the consumer's optimality condition MRS = p_x/p_y. Both conditions express the same idea: equilibrium requires that the personal rate of substitution match the market rate.

Special cases sharpen the intuition. **Perfect substitutes** in production (e.g., two interchangeable grades of steel) give straight-line isoquants with constant MRTS — the firm simply uses whichever input is cheaper. **Perfect complements** (e.g., one driver per truck) give L-shaped isoquants with undefined MRTS — no substitution is possible at all; both inputs must be expanded together. Real production processes fall between these extremes, exhibiting **diminishing MRTS** that reflects a gradually harder tradeoff as the firm pushes toward extreme input ratios.
