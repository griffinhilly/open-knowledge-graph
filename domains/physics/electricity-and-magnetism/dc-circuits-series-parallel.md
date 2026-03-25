---
id: dc-circuits-series-parallel
title: 'DC Circuits: Series and Parallel'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ohms-law
  type: hard
- id: electric-power
  type: soft
- id: capacitor-networks
  type: soft
builds-toward:
- kirchhoffs-rules
- rc-circuits
tags:
- dc-circuits
- series
- parallel
- resistors
- EMF
stage: formal-systems
status: validated
---
# DC Circuits: Series and Parallel

## Core Idea
In a series circuit, components share the same current; equivalent resistance is R_eq = ΣRᵢ, and voltage divides among components. In a parallel circuit, components share the same voltage; equivalent resistance follows 1/R_eq = Σ(1/Rᵢ), and current divides. A real battery has an internal resistance r that reduces the terminal voltage below its EMF ε by an amount Ir. Multi-loop circuits with combinations of series and parallel elements are analyzed by successive reduction of equivalent resistances.

## How It's Best Learned
Build intuition by reducing complex resistor networks step by step: identify series pairs and parallel pairs, replace each with equivalent resistors, and repeat until one equivalent resistance remains. Always check limiting cases.

## Common Misconceptions
- Adding more resistors in series increases total resistance; in parallel, it decreases it.
- The terminal voltage of a battery is not equal to its EMF when current flows.
- Current does not 'choose' one path — in parallel branches, all paths carry current.

## Questions

```yaml
- question: "A technician adds a second identical light bulb in parallel with the first in a simple circuit. Assuming an ideal voltage source, what happens to each bulb's brightness and the total current drawn?"
  type: multiple-choice
  options:
    - "Each bulb dims because the added bulb steals current from the first"
    - "Each bulb burns as brightly as before, and total current from the source doubles"
    - "Each bulb brightens because total resistance has decreased"
    - "The first bulb dims while the second burns at full brightness"
  answer: 1
  explanation: "In a parallel circuit, both branches connect across the same voltage. Each bulb sees the same voltage as before, so each draws the same current as before and burns equally bright. Total current doubles because two independent branches now draw from the source. The common misconception — that added parallel components 'steal' current — applies to series circuits, not parallel ones."

- question: "A battery has EMF ε = 12 V and internal resistance r = 2 Ω. When it supplies a current of 3 A, what is the terminal voltage?"
  type: multiple-choice
  options:
    - "12 V, because the EMF equals the terminal voltage by definition"
    - "18 V, because internal resistance adds to the output voltage under load"
    - "6 V, because the internal resistance drops 6 V leaving 6 V at the terminals"
    - "10 V, because terminal voltage is always slightly less than EMF"
  answer: 2
  explanation: "Terminal voltage V = ε − Ir = 12 − (3)(2) = 12 − 6 = 6 V. The internal resistance drops Ir volts, reducing what appears at the terminals below the open-circuit EMF. Option A is the most common misconception — EMF equals terminal voltage only when no current flows. Under load, terminal voltage always sags below EMF by exactly Ir."

- question: "Adding a resistor in parallel with an existing resistor always decreases the equivalent resistance, even if the added resistor has a very large value."
  type: true-false
  answer: true
  explanation: "Any finite resistance added in parallel creates an additional current path. Even a very large resistor carries a tiny current, and that additional current means the source 'sees' less total resistance. Mathematically, 1/R_eq = 1/R₁ + 1/R₂ always produces an R_eq smaller than either R₁ or R₂ alone, regardless of how large one of them is."

- question: "In a series circuit, resistors with higher resistance carry more current than those with lower resistance."
  type: true-false
  answer: false
  explanation: "In a series circuit there is only one path, so every component carries exactly the same current. Resistance determines how much voltage is 'used up' across each component (V = IR), not how much current flows through it. More resistance means a larger voltage drop across that component, but the current through all series components is identical."

- question: "Why does the equivalent resistance of a parallel combination always end up smaller than the smallest individual resistor in the group?"
  type: short-answer
  answer: "Because each additional parallel branch provides a new independent path for current. The source no longer forces all current through a single resistor — it splits current across multiple paths simultaneously. The equivalent resistance represents the total opposition to current flow, and since more paths means more total current for the same voltage, the equivalent resistance must be lower. Mathematically, every term added to 1/R_eq = Σ(1/Rᵢ) increases the sum, which decreases R_eq."
  explanation: "A useful physical intuition: think of resistors as lanes on a highway. Adding a lane (even a slow one) always increases total throughput, meaning less resistance to flow overall. The equivalent resistance can never exceed — and always falls below — the smallest individual branch resistance."
```

## Explainer

The fundamental difference between series and parallel comes down to what is shared. In a **series circuit**, the same current flows through every element — there is only one path, so every coulomb of charge must pass through each resistor in turn. The voltage, however, divides: each resistor "uses up" a portion proportional to its resistance, and those portions sum to the total voltage. Adding resistors in series always increases the total resistance because every resistor adds another obstacle to the same current.

In a **parallel circuit**, all elements share the same voltage — each branch connects directly across the same two terminals. But now the current divides among the branches, and each branch draws current independently of the others. Adding a new parallel branch creates an additional path, so total current increases and equivalent resistance decreases. The formula 1/R_eq = Σ(1/Rᵢ) reflects this: each new branch contributes a new term, and the equivalent resistance is always less than the smallest individual resistance.

A real battery introduces a practical complication: **internal resistance** r. No battery is a perfect voltage source — the electrochemical materials inside have finite resistance. When current I flows, the internal resistance drops voltage by Ir, so the **terminal voltage** (what you measure at the battery terminals) is V = ε − Ir, where ε is the EMF (the open-circuit voltage from the chemistry). Under heavy load (large I), terminal voltage sags noticeably below ε. This is why a nearly-dead battery reads close to its nominal voltage with no load but collapses when a motor draws current.

Analyzing a complex resistor network is a process of successive reduction. Look for resistors carrying identical current — that's series, and you can replace them with their sum. Look for resistors sharing identical terminal voltage — that's parallel, and you can replace them with 1/Σ(1/Rᵢ). Repeat until you have one equivalent resistor. The key discipline is checking limiting cases: short-circuiting one branch of a parallel network should drive R_eq toward zero; opening a series branch should drive R_eq toward infinity. If your formula gives the wrong limiting behavior, find the error before solving the full problem.
