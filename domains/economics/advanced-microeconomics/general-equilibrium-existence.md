---
id: general-equilibrium-existence
title: 'Existence of General Equilibrium: Fixed-Point Theorems'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: walrasian-equilibrium
  type: hard
- id: fixed-point-iteration
  type: soft
- id: compact-sets
  type: hard
- id: topological-spaces-definition
  type: hard
- id: compact-sets-definition
  type: soft
tags:
- general-equilibrium
- mathematical-economics
stage: advanced
status: draft
---

# Existence of General Equilibrium: Fixed-Point Theorems

## Core Idea
General equilibrium existence is non-trivial and requires proof. Under convexity of preferences, continuous utility functions, and no free disposal, Brouwer and Kakutani fixed-point theorems establish that at least one Walrasian equilibrium exists. The proof models excess demand as a mapping from the price simplex to itself and applies fixed-point theory to find equilibrium prices.

## Explainer

From Walrasian equilibrium, you know the concept: a price vector at which every consumer maximizes utility subject to their budget constraint and all markets clear simultaneously. But knowing what equilibrium means is very different from knowing whether one actually exists. The economy is a system of potentially millions of interacting agents with diverse preferences and endowments. Why should there be any price vector that simultaneously satisfies everyone's optimization and clears every market? The existence proof answers this question and, in doing so, reveals what assumptions about the economy are truly essential for markets to function.

The proof strategy is elegant in structure. First, normalize prices so they lie on the **price simplex** — the set of all non-negative price vectors that sum to one. (Since only relative prices matter in general equilibrium, this normalization loses nothing.) At each price vector, every consumer solves their optimization problem, generating demands. Subtract total endowments from total demands to get the **excess demand function** *z(p)*, which maps each price vector to a vector of excess demands across all goods. Equilibrium means finding a price vector where *z(p) = 0* — supply equals demand in every market. Walras' law (which you know from general equilibrium theory) guarantees that the value of excess demand is always zero, so if all but one market clears, the last one must clear too. The problem reduces to: does the excess demand function have a zero?

This is where **fixed-point theorems** from topology enter. Rather than searching for a zero of *z(p)* directly, the proof constructs a continuous mapping from the price simplex to itself — essentially a rule that takes any price vector and adjusts it in the direction that excess demand suggests (raising prices of goods in excess demand, lowering prices of goods in excess supply). The price simplex is a **compact, convex set** (this is where your topology prerequisites matter). Brouwer's fixed-point theorem states that any continuous function from a compact convex set to itself must have at least one fixed point — a point that maps to itself. At a fixed point of this price-adjustment mapping, prices are not adjusting, which means excess demand is zero: equilibrium. When demand correspondences are set-valued (as with indifference leading to non-unique optimal bundles), **Kakutani's fixed-point theorem** extends the result to upper hemicontinuous correspondences.

The assumptions doing the heavy lifting are **convexity of preferences** (which ensures demand varies continuously with prices and rules out jumps), **continuity of utility** (which keeps demand well-behaved), and **positive endowments** (every consumer owns some of every good, preventing budget constraints from collapsing). If preferences are non-convex — for instance, if consumers have indivisible goods or increasing returns — the excess demand mapping may not be continuous and fixed-point theorems fail to apply. This is not merely a mathematical curiosity: it explains why markets for goods with strong increasing returns (like software or network platforms) may not reach competitive equilibrium naturally. The existence theorem thus tells us both when we can trust the invisible hand and when we should expect market outcomes to be problematic.
