---
id: cavitation-pressure-vapor-dynamics
title: Cavitation and Vapor Pressure Dynamics
domain: engineering
course: fluid-mechanics
prerequisites:
- id: absolute-gauge-atmospheric-pressure
  type: hard
- id: cavitation-sigma-number-prediction
  type: soft
tags:
- cavitation
- vapor
- pressure
- damage
stage: formal-systems
status: validated
---
# Cavitation and Vapor Pressure Dynamics

## Core Idea
Cavitation occurs when pressure in a flowing liquid drops below the vapor pressure, causing liquid to vaporize and form bubbles. These bubbles collapse when they reach high-pressure regions, creating pressure spikes that can damage surfaces. Cavitation is a concern in pumps, turbines, and behind propellers; it is avoided by maintaining minimum pressure or reducing fluid temperature, and its onset is predicted using the cavitation number σ = (P − P_v)/(½ρV²).

## Questions

```yaml
- question: "A pump handling cold water at 10°C experiences a pressure drop at the impeller inlet. At what point does cavitation begin?"
  type: multiple-choice
  options:
    - "When the water temperature rises above 100°C due to frictional heating"
    - "When local pressure drops below the vapor pressure of water at 10°C"
    - "When flow velocity exceeds the speed of sound in water"
    - "When the pump draws more water than it can discharge, causing backflow"
  answer: 1
  explanation: "Cavitation is triggered when local pressure falls below the vapor pressure at the prevailing temperature — not when temperature rises to the boiling point at atmospheric pressure. At 10°C, water's vapor pressure is only about 1,230 Pa (much less than atmospheric). If local pressure at the impeller inlet drops below this value due to high velocity (via Bernoulli), the water locally vaporizes and forms bubbles. Cavitation is a pressure-relative-to-vapor-pressure phenomenon, not a thermal boiling phenomenon."

- question: "Where does cavitation damage primarily occur, and what mechanism causes it?"
  type: multiple-choice
  options:
    - "At the point of lowest pressure, where bubbles form and physically erode the surface"
    - "Uniformly across the wetted surface, as vapor bubbles abrade the material"
    - "In high-pressure zones downstream, where collapsing bubbles generate intense pressure spikes and microjets"
    - "At the pump inlet, where turbulent flow creates direct mechanical impact"
  answer: 2
  explanation: "Cavitation damage occurs downstream, where cavitation bubbles travel into higher-pressure regions and violently implode. The collapse is asymmetric: liquid rushes inward faster than the speed of sound, generating focused microjets and pressure pulses reaching thousands of atmospheres. These repeated impacts pit and erode the surface. The formation of bubbles causes little direct damage — the danger is the collapse. This is why cavitation damage appears on impeller blades and turbine runners in zones of flow reattachment, not at the suction inlet."

- question: "Cavitation can occur in cold water at temperatures well below 100°C if local pressure drops low enough."
  type: true-false
  answer: true
  explanation: "Boiling at atmospheric pressure requires 100°C, but cavitation is vaporization at reduced pressure — the phase transition occurs whenever local pressure falls below the vapor pressure at the current temperature. At 10°C, water's vapor pressure is about 1,230 Pa; at 20°C, about 2,300 Pa. In a fast-flowing pump or turbine, the Bernoulli effect can reduce local pressure to these levels even in cold water. The thermodynamics are the same: vapor pressure depends on temperature, and vaporization occurs whenever ambient pressure drops below it."

- question: "Cavitation damage is caused primarily by the formation of vapor bubbles, which create voids that weaken the surface material."
  type: true-false
  answer: false
  explanation: "Formation of bubbles is not the damaging event — collapse is. When a cavitation bubble moves from a low-pressure zone into a higher-pressure zone, it implodes violently and asymmetrically. The surrounding liquid collapses inward, producing microjets directed at the nearby surface with pressures reaching thousands of atmospheres. These repeated micro-impacts fatigue and pit the surface over time. The appearance resembles sandblasting from the inside. Understanding that damage comes from collapse (not formation) explains why damage occurs on the downstream, high-pressure faces of impeller blades."

- question: "Explain why cavitation is described as a 'pressure-relative-to-vapor-pressure' problem rather than simply a boiling or overheating problem, and what this means for prevention."
  type: short-answer
  answer: "Cavitation and boiling are the same phase transition (liquid to vapor) but triggered by different mechanisms. Boiling is caused by raising temperature until vapor pressure exceeds ambient pressure; cavitation is caused by lowering local pressure (via high-velocity flow) below vapor pressure at the existing temperature. Prevention therefore targets the pressure margin: increase static pressure at the problem location, lower fluid temperature (which reduces vapor pressure), reduce velocity, or raise inlet head. Simply cooling the fluid is not always practical, but raising inlet pressure or reducing flow speed directly addresses the root cause."
  explanation: "The cavitation number σ = (P − P_v)/(½ρV²) formalizes the 'pressure margin' concept: the numerator is how far local pressure exceeds vapor pressure, and the denominator is the dynamic pressure. A high σ means cavitation is unlikely; a low σ signals risk. Prevention strategies all increase σ: raising P (inlet pressure), lowering P_v (cooler fluid), or reducing V (lower velocity). This framing also explains why NPSH (Net Positive Suction Head) specifications exist — they guarantee that inlet pressure stays above vapor pressure with a safety margin."
```

## Explainer

From your work with absolute and gauge pressure, you know that every liquid has a **vapor pressure** P_v — the pressure at which it transitions from liquid to vapor at a given temperature. At sea level and room temperature, water's vapor pressure is only about 2,300 Pa (much less than atmospheric 101,325 Pa), so you don't normally worry about it. But in high-speed flows, local pressure can drop dramatically. By Bernoulli's equation, regions of high velocity correspond to low pressure. When that local pressure falls below P_v, the liquid instantaneously vaporizes, forming vapor-filled voids called **cavitation bubbles**.

The damage comes not from the bubble's formation but from its collapse. As a cavitation bubble travels downstream into a region of higher pressure, it implodes asymmetrically and violently — the surrounding liquid rushes inward faster than the speed of sound in the liquid, generating a focused **microjet** and pressure pulses reaching thousands of atmospheres. These repeated impacts erode metal surfaces, pitting pump impellers, propeller blades, and turbine runner faces even in hardened steel. The damage looks like the surface has been sand-blasted from the inside. In extreme cases, cavitation destroys impellers within months of installation.

Engineers quantify cavitation tendency with the dimensionless **cavitation number** σ = (P − P_v)/(½ρV²). The numerator is how far the local pressure exceeds vapor pressure — the margin before vaporization. The denominator is the dynamic pressure associated with flow velocity. A small σ means cavitation is likely; a large σ means the flow is safely above vapor pressure. For pump systems, this becomes the **Net Positive Suction Head (NPSH)**: the minimum head at the pump inlet that prevents cavitation. If NPSH available (from system geometry and fluid pressure) falls below NPSH required (from the pump manufacturer), cavitation occurs.

Prevention strategies all work by raising local pressure relative to vapor pressure: lower the fluid temperature (reducing P_v), increase the static pressure at the problem location (raise inlet pressure, shorten the suction pipe, add head), reduce flow velocity (operate away from peak flow), or use materials and coatings that resist pitting. Inducer impellers placed upstream of the main impeller are specifically designed to raise local pressure before the main rotor, buying margin against cavitation. Understanding that cavitation is fundamentally a **pressure-relative-to-vapor-pressure** problem — not simply a boiling problem — is the key to diagnosing and preventing it.
