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
stage: formal-systems
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

## Questions

```yaml
- question: "After applying Kirchhoff's rules to a two-loop circuit, you find that one branch current has a value of −3 A. What does this mean?"
  type: multiple-choice
  options:
    - "You made an arithmetic error — currents cannot be negative in a DC circuit"
    - "The current in that branch flows opposite to the direction you assumed, with a magnitude of 3 A"
    - "That branch carries no current — negative indicates zero in circuit analysis"
    - "Your loop equation was set up incorrectly and must be redone with a revised assumed direction"
  answer: 1
  explanation: "A negative current value is not an error — it is the method self-correcting. It means the actual current flows opposite to the direction you assumed, with magnitude 3 A. You assumed a direction as a label for the unknown; the algebra determined both the magnitude and the true direction. The explainer states: 'Wrong guesses give negative values — not errors, just corrections.' No re-setup is needed."

- question: "Kirchhoff's Loop Rule states that the sum of all potential differences around any closed loop equals zero. Which fundamental principle does this directly express?"
  type: multiple-choice
  options:
    - "Conservation of charge — charge cannot accumulate at a wire junction in steady state"
    - "Conservation of energy — a charge carrier returning to its starting point has undergone zero net energy change"
    - "Ohm's law — voltage and current are proportional in all resistive elements"
    - "Newton's third law — every voltage rise must be paired with an equal and opposite voltage drop"
  answer: 1
  explanation: "The Junction Rule expresses charge conservation; the Loop Rule expresses energy conservation. The explainer makes this explicit: a charge traveling around a closed loop and returning to its starting point undergoes zero net change in potential energy — just like a hiker returning to starting elevation does zero net gravitational work. Each resistor drops potential (−IR), each EMF source raises or lowers it, and the sum around any closed path must be zero by energy conservation."

- question: "Kirchhoff's Junction Rule — the sum of currents at a node equals zero — is a direct statement of conservation of charge in steady state."
  type: true-false
  answer: true
  explanation: "In steady state, charge neither accumulates nor disappears at a wire junction. Every coulomb flowing in must flow out — this is exactly what charge conservation requires. The Junction Rule is not an arbitrary convention; it is a consequence of the fundamental principle that charge is conserved. The explainer calls it 'charge conservation in disguise.'"

- question: "When applying the Loop Rule, traversing a resistor in the direction opposite to the assumed current gives a voltage contribution of −IR."
  type: true-false
  answer: false
  explanation: "The sign convention is the reverse: traversing a resistor opposite to the assumed current direction gives +IR (a voltage rise), not −IR. Going through a resistor in the same direction as assumed current gives −IR (a drop, consistent with energy dissipation). Getting this sign convention backwards is one of the most common sources of errors when setting up Kirchhoff loop equations."

- question: "Why is it valid to assume any direction for branch currents when setting up Kirchhoff's equations, even if your guess turns out to be wrong?"
  type: short-answer
  answer: "Because the sign of the result carries the directional information. An assumed direction is just a label for the unknown — you're telling the algebra which direction to call 'positive.' If you get a positive value, current flows in the assumed direction; if negative, it flows opposite. The system of linear equations enforces self-consistency: wrong assumptions produce negative answers, not wrong answers. The method is self-correcting because direction information is encoded in the sign."
  explanation: "This is the elegant feature of the Kirchhoff method: you don't need to know the correct direction before solving, which would require knowing the answer in advance. The algebra determines both magnitude and direction simultaneously. All that matters is that you apply the sign convention consistently throughout each equation."
```

## Explainer

You already know how to analyze series and parallel circuits using simplified formulas. Kirchhoff's rules are what those formulas are secretly built on — and they generalize to any circuit, no matter how entangled. The two rules are really just two conservation laws wearing circuit clothes.

The **Junction Rule** (or node rule) is charge conservation in disguise. Because charge neither accumulates nor disappears at a wire junction in steady state, every coulomb that flows in must flow out. Sum all currents at a node, calling incoming currents positive and outgoing negative (or vice versa, as long as you're consistent): the sum equals zero. In a two-branch parallel circuit you already know this — the current splits. But in a circuit with three or four junctions this rule generates multiple equations linking the branch currents together.

The **Loop Rule** is energy conservation. A charge carrier that travels around any closed path and returns to its starting point has undergone zero net change in potential energy. Each resistor it passes through drops potential by IR (energy dissipated); each battery or EMF source it passes through raises or lowers potential by the source voltage. Going around a loop and summing all these rises and drops gives zero. This is analogous to the work done by gravity on a hiker who returns to the starting elevation: the net work is zero regardless of the path taken.

To apply both rules systematically: first, label each branch current with an assumed direction (drawn with an arrow). Wrong guesses give negative values — not errors, just corrections. Then write one junction equation per independent node (if there are n nodes, you get n−1 independent equations). Then write loop equations, one per independent loop, using the sign convention: going through a resistor in the direction of your assumed current gives −IR; against the current gives +IR. Going through a battery from − to + gives +ε; from + to − gives −ε. The resulting system of linear equations (here is where your prerequisite on systems elimination pays off) yields all unknown currents. The method is mechanical and guaranteed to work for any DC network.
