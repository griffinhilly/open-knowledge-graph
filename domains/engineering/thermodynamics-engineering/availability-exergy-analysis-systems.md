---
id: availability-exergy-analysis-systems
title: Availability and Exergy Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: exergy-concept-availability
  type: hard
- id: second-law-analysis-practical
  type: hard
builds-toward:
- exergy-destruction-irreversibility
- exergy-balance-control-volume
tags:
- exergy
- availability
- maximum-work
- destroyed-work
stage: advanced
status: draft
---

# Availability and Exergy Analysis

## Core Idea
Exergy is the maximum useful work obtainable from a system reaching equilibrium with surroundings: Ex = (H - H₀) - T₀(S - S₀) + (KE + PE). Unlike energy which is conserved, exergy is destroyed by irreversibilities: Ex_destroyed = T₀*S_gen. Exergy balance pinpoints where efficiency is lost and guides design improvements to power cycles, refrigerators, and industrial processes.

## Questions

```yaml
- question: "A power plant's turbine is 90% isentropically efficient, but exergy analysis reveals that the combustion chamber destroys far more exergy than the turbine. What does this reveal about first-law energy analysis alone?"
  type: multiple-choice
  options:
    - "Energy analysis is wrong — it must have underestimated turbine losses"
    - "Energy analysis cannot show where work potential is wasted, since combustion conserves energy while massively generating entropy"
    - "Exergy and energy analysis always agree on which component causes the largest losses"
    - "This result is impossible — a 90% efficient turbine must be the dominant loss component"
  answer: 1
  explanation: "Energy is conserved in combustion — chemical energy becomes thermal energy of hot gases, with no energy 'lost.' But burning fuel at a flame temperature far above the working fluid temperature is highly irreversible: entropy is generated massively. Exergy analysis converts this entropy generation to destroyed work potential via Ex_destroyed = T₀·Ṡ_gen, revealing that the combustion chamber can dominate losses even when the turbine is highly efficient. Energy analysis treats all joules as equivalent regardless of source temperature; exergy analysis penalizes irreversible temperature differences, making this invisible-to-energy loss visible."

- question: "A heat exchanger operates steadily and generates 5 W/K of entropy at an environment temperature T₀ = 300 K. How much work potential does it destroy per second?"
  type: multiple-choice
  options:
    - "5 W, because entropy generation rate equals work destruction rate"
    - "300 W, because the dead-state temperature sets the scale"
    - "1500 W, by the Gouy-Stodola theorem: Ex_destroyed = T₀ × Ṡ_gen"
    - "The work destruction cannot be determined without knowing the heat transfer rate"
  answer: 2
  explanation: "The Gouy-Stodola theorem states Ex_destroyed = T₀ × Ṡ_gen. With Ṡ_gen = 5 W/K and T₀ = 300 K: Ex_destroyed = 300 × 5 = 1500 W. This converts entropy generation (which has units W/K, not useful for engineering comparisons) into destroyed work potential in watts, the same units as power output. Option A confuses entropy generation rate with power. Option D is wrong because Gouy-Stodola requires only Ṡ_gen and T₀ — no heat transfer details are needed."

- question: "Exergy, unlike energy, can be destroyed by irreversible processes — every real process destroys some exergy."
  type: true-false
  answer: true
  explanation: "This is the fundamental distinction between energy and exergy. The first law says energy is always conserved — it transforms from one form to another but never disappears. Exergy measures the ability to do useful work relative to the dead state. Every irreversibility (friction, heat transfer across a temperature difference, mixing, unrestrained expansion) generates entropy, and the Gouy-Stodola theorem directly links entropy generation to exergy destruction: Ex_destroyed = T₀ × Ṡ_gen > 0 for any irreversible process. Only a reversible process achieves zero exergy destruction."

- question: "Energy analysis and exergy analysis always agree on which component of a power cycle causes the greatest thermodynamic losses."
  type: true-false
  answer: false
  explanation: "This is false — and this disagreement is precisely why exergy analysis is valuable. Energy analysis tracks quantities in and out and identifies losses as heat rejected to the environment. It cannot distinguish between heat rejected at high temperature (large work potential squandered) and heat rejected at low temperature (small work potential lost). Exergy analysis penalizes irreversibilities by their Carnot factor (1 − T₀/T), revealing that combustion chambers — which operate at extreme temperatures with massive entropy generation — often destroy far more work potential than the turbine or condenser. Energy analysis would miss this because all joules look the same to it."

- question: "Why does the Gouy-Stodola theorem (Ex_destroyed = T₀ × Ṡ_gen) make exergy analysis more useful than entropy analysis alone for identifying sources of inefficiency in thermal systems?"
  type: short-answer
  answer: "Entropy generation Ṡ_gen has units of W/K, which makes it impossible to compare directly against work outputs or to aggregate losses across components with different temperatures. Multiplying by T₀ converts entropy generation to destroyed work potential in watts — the same units as power output. This allows direct comparison: a heat exchanger generating 2 W/K and a turbine generating 5 W/K can be ranked by their exergy destruction (600 W vs 1500 W at T₀ = 300 K). The result is an engineering diagnostic ranking inefficiencies in units directly relevant to the system's purpose: how much work could have been produced but wasn't."
  explanation: "Exergy analysis is used in industrial process design because it answers the question engineers care about: 'Where is useful work being wasted, and by how much?' Entropy generation is a correct thermodynamic indicator but an inconvenient engineering one. Gouy-Stodola bridges the gap by converting the abstract measure into actionable units."
```

## Explainer

From your second-law studies you know that entropy is generated by every real, irreversible process — friction, heat transfer across a temperature difference, unrestrained expansion. But entropy generation alone doesn't tell you how much work you've wasted. **Exergy** (also called availability) answers that question directly: it is the maximum useful work extractable from a system as it comes to equilibrium with its surroundings (the **dead state**), characterized by T₀ and P₀. Anything the system can do that the surroundings can't "undo" is exergy; anything the surroundings could always supply for free (e.g., pushing against atmospheric pressure) is not.

The exergy of a flowing stream is Ex = (H − H₀) − T₀(S − S₀) + KE + PE. The term (H − H₀) represents the enthalpy the stream carries above the dead state — the potential to do flow work. The term −T₀(S − S₀) is the penalty: higher entropy relative to the dead state means less ability to do work. This is exactly the Carnot logic you already know: a heat source at T delivers less work per unit of heat as T approaches T₀, because the Carnot efficiency η = 1 − T₀/T shrinks. The exergy formula generalizes that logic to any stream or system state.

The crucial connection to your second-law prerequisite is the **Gouy-Stodola theorem**: exergy destroyed equals T₀ times the entropy generated: Ex_destroyed = T₀ · Ṡ_gen. Every source of irreversibility you learned to quantify with entropy generation — heat exchangers, turbines, mixing — now has a direct work cost. A heat exchanger that generates 2 W/K of entropy at T₀ = 300 K destroys 600 W of work potential, even if it moves the right amount of energy. This makes exergy analysis a practical diagnostic: it converts entropy generation (which has no units of work) into destroyed work potential (in watts or joules), making different types of inefficiency directly comparable.

To perform an **exergy balance on a control volume**, you account for exergy entering (with mass flows and heat transfers), exergy leaving, and exergy destroyed. For a heat transfer Q̇ at temperature T, the exergy transferred is Q̇(1 − T₀/T) — the Carnot-factor-weighted portion. For a Rankine turbine, you can now split losses into three categories: isentropic inefficiency (entropy generated inside the turbine), condenser heat rejection (unavoidable exergy loss to the environment), and auxiliary losses. This decomposition tells you where design improvements will actually help: improving turbine isentropic efficiency recovers the internal destruction, but no improvement in condenser design eliminates the fundamental T₀/T limit on heat rejection.

**Exergy efficiency** ε = Ex_out/Ex_in (sometimes written as the ratio of exergy gain to exergy cost) provides a second-law analog to first-law efficiency. Unlike first-law efficiency, it reaches 100% only for reversible processes, and values above 100% are impossible. For a power plant, comparing ε across components reveals the biggest opportunities: a combustion chamber often has the largest exergy destruction (mixing fuels at high temperature irreversibly), not the turbine or condenser. This insight — that the biggest thermodynamic loss is often at the flame, not the rotating machinery — could not be reached from energy balances alone, and is the primary reason exergy analysis is used in industrial process design.
