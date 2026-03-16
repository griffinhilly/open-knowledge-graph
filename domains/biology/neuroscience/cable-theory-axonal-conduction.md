---
id: cable-theory-axonal-conduction
title: Cable Theory and Axonal Conduction
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: hard
- id: neuron-structure-and-function
  type: hard
- id: partial-differential-equations
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- hodgkin-huxley-model
- saltatory-conduction
tags:
- cable-equation
- length-constant
- time-constant
stage: advanced
status: draft
---

# Cable Theory and Axonal Conduction

## Core Idea
Cable theory models axons as cylinders with resistive and capacitive properties. The cable equation describes voltage decay: V(x,t) = V₀ exp(−x/λ) where λ = √(rm/ri) is the length constant. This determines how far passive current spreads; τ = rm·cm determines the voltage time constant.

## How It's Best Learned
Solve the cable equation for simple geometries. Use compartmental modeling software to simulate branching dendrites.

## Common Misconceptions
Action potentials propagate passively along cables—they require active regeneration. The length constant is fixed—it depends on membrane and axial properties.

## Explainer

You already know from studying the resting membrane potential that neurons maintain a voltage difference across their membranes, and that current can flow through ion channels and along the cytoplasm. **Cable theory** takes this understanding and asks a quantitative question: when voltage changes at one point on an axon, how far does that electrical signal spread before it fades away? The answer turns out to depend on the same physical principles that govern signal loss in undersea telegraph cables — which is exactly where the theory gets its name.

Think of an axon as a leaky garden hose. Water (current) enters at one end, but the hose has tiny holes along its length (ion channels in the membrane) through which water leaks out. The farther you go from the input, the less water pressure (voltage) remains. Cable theory formalizes this intuition with two key parameters. The **length constant** (λ) tells you the distance over which voltage decays to 37% (1/e) of its original value. It equals √(rₘ/rᵢ), where rₘ is the membrane resistance per unit length (how leaky the hose is) and rᵢ is the intracellular axial resistance per unit length (how hard it is for current to flow down the interior). A large λ means the signal travels far before fading — you get this with high membrane resistance (fewer leak channels, tighter hose) or low axial resistance (wider axon, bigger hose diameter).

The second parameter is the **time constant** (τ = rₘ × cₘ), where cₘ is the membrane capacitance. This tells you how quickly the membrane voltage responds to a current injection. A large τ means the membrane charges slowly — like filling a large bucket through a narrow pipe. Together, λ and τ define the passive electrical properties of any stretch of neural membrane. If you inject a brief pulse of current at one point, the voltage change spreads outward as a decaying wave described by the **cable equation**: V(x,t) = V₀ × exp(−x/λ), with the temporal dynamics governed by τ. This is purely passive spread — no ion channels are opening or closing in response.

Why does this matter if action potentials are active, regenerative events? Because passive spread is what carries the depolarization from one cluster of voltage-gated sodium channels to the next. Between nodes of Ranvier in a myelinated axon, or between channel-dense patches in an unmyelinated one, current must travel passively. The length constant determines whether enough depolarization reaches the next channel cluster to trigger a new action potential. Myelination dramatically increases rₘ (the myelin sheath prevents current leak) and decreases cₘ (thicker insulation reduces capacitance), both of which increase λ and speed up conduction. This is why cable theory is the essential bridge between the resting membrane potential you already understand and the Hodgkin-Huxley model of active spike propagation that comes next — it explains the passive infrastructure on which active signaling depends.
