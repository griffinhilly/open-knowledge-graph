---
id: karnaugh-map-optimization
title: Karnaugh Map Simplification
domain: computer-science
course: computer-architecture
prerequisites:
- id: boolean-function-implementation
  type: hard
- id: boolean-algebra-and-laws
  type: soft
builds-toward:
- combinational-circuit-design
tags:
- optimization
- boolean-algebra
- logic-design
stage: formal-systems
status: draft
---

# Karnaugh Map Simplification

## Core Idea
Karnaugh maps simplify Boolean expressions visually by grouping adjacent 1s. Larger groups yield simpler expressions, reducing gate count and improving circuit efficiency.

## Explainer

You already know how to express logic functions as Boolean equations and implement them with gates. The problem is that a truth table or sum-of-products expression straight from a specification often contains redundancy — terms that can be combined because they differ in only one variable. Boolean algebra gives you the laws to simplify, but applying them algebraically is error-prone and unsystematic. The **Karnaugh map** (K-map) solves this by turning algebraic simplification into a visual pattern-matching exercise.

A K-map is a grid where each cell represents one row of the truth table. The key design choice is that adjacent cells differ in exactly one variable — the columns and rows are ordered using **Gray code**, not standard binary counting. This means that any two physically neighboring cells (including wrap-around from the last column back to the first) share all variable values except one. When two adjacent cells both contain a 1, those two minterms can be combined, eliminating the variable that differs between them. This is exactly the Boolean algebra rule A·B + A·B' = A, but you find it by sight instead of by manipulation.

The grouping rules are straightforward: groups must be rectangular, and their size must be a power of two (1, 2, 4, 8, or 16 cells). A group of two eliminates one variable, a group of four eliminates two, a group of eight eliminates three, and so on. Your goal is to cover every 1 in the map using the fewest, largest possible groups. Each group becomes one product term in the simplified expression, and the variables that stay constant across the group form that term. For example, in a 4-variable K-map, a group of four cells where A=1 and C=0 throughout (while B and D vary) simplifies to the term A·C'.

**Don't-care conditions** — inputs that will never occur or whose output doesn't matter — are marked with X and can be included in groups if doing so makes a group larger. This is where K-maps really shine compared to algebraic simplification: you can opportunistically absorb don't-cares to create bigger groups without affecting the circuit's behavior on valid inputs. The result is a **minimal sum-of-products** (or product-of-sums) expression that maps directly to a gate-level implementation with fewer gates, fewer inputs per gate, and lower propagation delay than the unsimplified version.
