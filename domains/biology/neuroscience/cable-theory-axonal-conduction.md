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
stage: expert
status: draft
---

# Cable Theory and Axonal Conduction

## Core Idea
Cable theory models axons as cylinders with resistive and capacitive properties. The cable equation describes voltage decay: V(x,t) = V₀ exp(−x/λ) where λ = √(rm/ri) is the length constant. This determines how far passive current spreads; τ = rm·cm determines the voltage time constant.

## How It's Best Learned
Solve the cable equation for simple geometries. Use compartmental modeling software to simulate branching dendrites.

## Common Misconceptions
Action potentials propagate passively along cables—they require active regeneration. The length constant is fixed—it depends on membrane and axial properties.

## Questions

```yaml
- question: "A neurotoxin blocks all voltage-gated ion channels in an axon membrane, leaving only the passive membrane resistance and capacitance intact. When current is injected at one point, what happens?"
  type: multiple-choice
  options:
    - "Action potentials propagate normally because passive spread is sufficient to carry the signal the full length of the axon"
    - "Voltage decays exponentially with distance from the injection site, described by V(x) = V₀ exp(−x/λ), with no regeneration at distant sites"
    - "The membrane potential does not change at all because all ion movement is blocked"
    - "The signal propagates faster than normal because the slow sodium channel activation step is bypassed"
  answer: 1
  explanation: "Without voltage-gated channels, only passive cable spread operates. The voltage change decreases exponentially with distance, decaying to 37% of its original value at x = λ (the length constant). No new action potentials can be initiated at distant sites because there are no channels to regenerate the signal. This is the 'leaky hose' model: current enters at one point, leaks out through passive membrane conductance along the way, and the pressure (voltage) drops steadily with distance. Action potentials require active channel gating — they are not passively conducted."

- question: "Myelination increases the length constant (λ) of an axon, which speeds action potential conduction. The mechanism is:"
  type: multiple-choice
  options:
    - "Myelin adds voltage-gated sodium channels at regular intervals, reducing the distance current must travel passively"
    - "Myelin increases intracellular axial resistance, forcing current to flow more rapidly down the axon interior"
    - "Myelin increases membrane resistance (reducing current leak) and decreases membrane capacitance (reducing the charge needed to change membrane voltage), both of which increase λ"
    - "Myelin decreases axon diameter, which concentrates current flow and increases signal amplitude"
  answer: 2
  explanation: "λ = √(rₘ/rᵢ). Myelin wraps around the axon, making the membrane much thicker — this dramatically increases rₘ (less current leaks out per unit length, like a better-insulated hose) and decreases cₘ (thicker insulation reduces capacitance, so less charge is needed to change the membrane voltage). Both effects increase λ. The result is that passive depolarization can spread much farther before decaying below threshold, allowing the next node of Ranvier to be triggered from much greater distance. Fewer nodes = fewer regeneration steps = faster conduction."

- question: "The length constant (λ) of a given axon is a fixed physical property that cannot be altered by changes in the axon's structural or molecular properties."
  type: true-false
  answer: false
  explanation: "λ = √(rₘ/rᵢ) depends on membrane resistance per unit length (rₘ) and intracellular axial resistance per unit length (rᵢ). Both are variable: rₘ changes with myelination and with the number and type of open ion channels in the membrane; rᵢ changes with axon diameter (wider axons have lower axial resistance, increasing λ). Myelination is the clearest biological example — it dramatically increases rₘ and decreases cₘ, increasing λ by orders of magnitude compared to unmyelinated axons of similar diameter."

- question: "Passive current spread governed by cable theory is essential for action potential propagation even though action potentials are active, regenerative events."
  type: true-false
  answer: true
  explanation: "Between active channel clusters (between nodes of Ranvier in myelinated axons, or between channel-dense patches in unmyelinated ones), current must travel passively. The depolarization from one action potential must spread passively far enough to bring the next cluster of voltage-gated sodium channels to threshold. The length constant determines how far this passive spread reaches before decaying. If λ is too small (as in demyelination), the passive current does not reach the next node at sufficient amplitude, and propagation fails. Cable theory describes the passive infrastructure on which active propagation depends."

- question: "Explain why a larger length constant (λ) speeds action potential conduction in a myelinated axon, even though action potentials themselves are not passive signals."
  type: short-answer
  answer: "Action potentials require active regeneration at each node of Ranvier — voltage-gated sodium channels must be triggered to sustain the signal. Between nodes, current spreads passively. A larger λ means passive depolarization travels farther before decaying below the threshold for triggering the next node. In myelinated axons, myelin increases rₘ and decreases cₘ, both increasing λ, so the passive current can jump across longer internodal distances and still trigger the next node. Fewer nodes are needed to cover the same axon length, and each passive 'jump' covers more ground, making conduction faster overall."
  explanation: "This is the mechanistic explanation for saltatory conduction (the action potential 'jumping' from node to node). Cable theory explains *why* the jump works: sufficient passive depolarization reaches each node because λ is large enough. Without this understanding, myelin's effect on speed is mysterious; with it, the physics is transparent."
```

## Explainer

You already know from studying the resting membrane potential that neurons maintain a voltage difference across their membranes, and that current can flow through ion channels and along the cytoplasm. **Cable theory** takes this understanding and asks a quantitative question: when voltage changes at one point on an axon, how far does that electrical signal spread before it fades away? The answer turns out to depend on the same physical principles that govern signal loss in undersea telegraph cables — which is exactly where the theory gets its name.

Think of an axon as a leaky garden hose. Water (current) enters at one end, but the hose has tiny holes along its length (ion channels in the membrane) through which water leaks out. The farther you go from the input, the less water pressure (voltage) remains. Cable theory formalizes this intuition with two key parameters. The **length constant** (λ) tells you the distance over which voltage decays to 37% (1/e) of its original value. It equals √(rₘ/rᵢ), where rₘ is the membrane resistance per unit length (how leaky the hose is) and rᵢ is the intracellular axial resistance per unit length (how hard it is for current to flow down the interior). A large λ means the signal travels far before fading — you get this with high membrane resistance (fewer leak channels, tighter hose) or low axial resistance (wider axon, bigger hose diameter).

The second parameter is the **time constant** (τ = rₘ × cₘ), where cₘ is the membrane capacitance. This tells you how quickly the membrane voltage responds to a current injection. A large τ means the membrane charges slowly — like filling a large bucket through a narrow pipe. Together, λ and τ define the passive electrical properties of any stretch of neural membrane. If you inject a brief pulse of current at one point, the voltage change spreads outward as a decaying wave described by the **cable equation**: V(x,t) = V₀ × exp(−x/λ), with the temporal dynamics governed by τ. This is purely passive spread — no ion channels are opening or closing in response.

Why does this matter if action potentials are active, regenerative events? Because passive spread is what carries the depolarization from one cluster of voltage-gated sodium channels to the next. Between nodes of Ranvier in a myelinated axon, or between channel-dense patches in an unmyelinated one, current must travel passively. The length constant determines whether enough depolarization reaches the next channel cluster to trigger a new action potential. Myelination dramatically increases rₘ (the myelin sheath prevents current leak) and decreases cₘ (thicker insulation reduces capacitance), both of which increase λ and speed up conduction. This is why cable theory is the essential bridge between the resting membrane potential you already understand and the Hodgkin-Huxley model of active spike propagation that comes next — it explains the passive infrastructure on which active signaling depends.
