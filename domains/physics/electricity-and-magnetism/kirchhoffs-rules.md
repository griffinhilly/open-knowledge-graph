---
id: kirchhoffs-rules
title: Kirchhoff's Rules
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dc-circuits-series-parallel
  type: hard
- id: conservation-of-energy
  type: soft
- id: systems-elimination
  type: soft
builds-toward:
- rc-circuits
- rl-circuits
tags:
- kirchhoff
- junction-rule
- loop-rule
- circuit-analysis
stage: abstract-reasoning
status: validated
---

# Kirchhoff's Rules

## Core Idea
Kirchhoff's Junction Rule states that the algebraic sum of currents entering any node equals zero (charge conservation). The Loop Rule states that the sum of all potential differences around any closed loop is zero (energy conservation). Together they provide a systematic method to solve any DC circuit, regardless of complexity, by setting up a system of linear equations — one per independent loop — for unknown currents.

## How It's Best Learned
Label all currents with assumed directions before applying the rules — wrong assumed direction will give a negative answer, which is physically meaningful. Practice with 2-loop circuits before 3-loop ones. Connect the Loop Rule explicitly to energy conservation.

## Common Misconceptions
- If you assume a current direction and get a negative value, the current flows opposite to your assumption — this is correct, not an error.
- Both rules must be applied; neither alone is sufficient.
- The number of independent loop equations equals the number of loops minus the number of junctions plus one.

## Explainer

You already know how to analyze series and parallel circuits using simplified formulas. Kirchhoff's rules are what those formulas are secretly built on — and they generalize to any circuit, no matter how entangled. The two rules are really just two conservation laws wearing circuit clothes.

The **Junction Rule** (or node rule) is charge conservation in disguise. Because charge neither accumulates nor disappears at a wire junction in steady state, every coulomb that flows in must flow out. Sum all currents at a node, calling incoming currents positive and outgoing negative (or vice versa, as long as you're consistent): the sum equals zero. In a two-branch parallel circuit you already know this — the current splits. But in a circuit with three or four junctions this rule generates multiple equations linking the branch currents together.

The **Loop Rule** is energy conservation. A charge carrier that travels around any closed path and returns to its starting point has undergone zero net change in potential energy. Each resistor it passes through drops potential by IR (energy dissipated); each battery or EMF source it passes through raises or lowers potential by the source voltage. Going around a loop and summing all these rises and drops gives zero. This is analogous to the work done by gravity on a hiker who returns to the starting elevation: the net work is zero regardless of the path taken.

To apply both rules systematically: first, label each branch current with an assumed direction (drawn with an arrow). Wrong guesses give negative values — not errors, just corrections. Then write one junction equation per independent node (if there are n nodes, you get n−1 independent equations). Then write loop equations, one per independent loop, using the sign convention: going through a resistor in the direction of your assumed current gives −IR; against the current gives +IR. Going through a battery from − to + gives +ε; from + to − gives −ε. The resulting system of linear equations (here is where your prerequisite on systems elimination pays off) yields all unknown currents. The method is mechanical and guaranteed to work for any DC network.
