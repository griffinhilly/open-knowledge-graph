---
id: froude-number-gravity-waves
title: Froude Number and Gravity Wave Propagation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: dimensional-analysis-and-similarity
  type: hard
- id: open-channel-flow
  type: hard
tags:
- froude-number
- surface-waves
- open-channel
stage: formal-systems
status: draft
---

# Froude Number and Gravity Wave Propagation

## Core Idea
The Froude number, Fr = V/√(gh), compares flow velocity to surface wave speed. For Fr < 1 (subcritical), gravity waves propagate upstream and control upstream boundary conditions. For Fr > 1 (supercritical), waves cannot propagate upstream and flow is controlled by downstream conditions. The transition at Fr = 1 produces a hydraulic jump—essential concepts for spillway design and open channel flow control.

## Questions

```yaml
- question: "A dam spillway discharges flow at Fr = 2.4 into a downstream channel. An operator partially closes a gate far downstream. What effect does this have on the flow on the spillway face?"
  type: multiple-choice
  options:
    - "The gate closure raises the water level on the spillway because it backs water upstream"
    - "The flow on the spillway is unaffected — supercritical flow cannot receive information from downstream"
    - "The gate closure increases the Froude number on the spillway by restricting outflow"
    - "The gate causes a hydraulic jump to propagate back up the spillway"
  answer: 1
  explanation: "In supercritical flow (Fr > 1), the flow velocity exceeds the wave speed, so no gravity wave — which carries information about downstream conditions — can propagate upstream. The gate closure creates a disturbance that propagates upstream only at wave speed c, but the flow sweeps it back downstream faster. The spillway flow is therefore completely controlled by upstream conditions (reservoir head and spillway geometry) and is indifferent to the gate. This is the central practical consequence of the Froude number: it determines which end of a channel controls the flow."

- question: "At critical flow (Fr = 1), surface gravity waves are stationary relative to the ground."
  type: true-false
  answer: true
  explanation: "Critical flow is defined as the condition where the flow velocity V equals the surface wave speed c = √(gD). A small gravity wave propagating upstream at speed c against a current moving downstream at speed V = c has zero net velocity relative to the ground — it is stationary. This is the open-channel analogue of a sonic condition in compressible flow. It is also why critical flow is the control point in many structures: at a weir, sluice gate, or channel contraction, flow passes through Fr = 1 and the structure 'controls' discharge independently of downstream depth."

- question: "In subcritical flow, downstream boundary conditions have no influence on the upstream flow profile."
  type: true-false
  answer: false
  explanation: "This is precisely backwards. In subcritical flow (Fr < 1), the flow velocity is less than the wave speed, so gravity waves can propagate upstream. Downstream conditions — such as a dam, a gate, or a change in channel slope — send wave signals upstream that modify the water surface profile. This is why backwater curves in subcritical channels are calculated starting from the downstream boundary and working upstream. In supercritical flow (Fr > 1), the statement would be true: downstream conditions cannot communicate upstream and have no influence on the upstream profile."

- question: "Why must the transition from supercritical to subcritical flow occur abruptly as a hydraulic jump rather than gradually?"
  type: short-answer
  answer: "In supercritical flow, waves cannot propagate upstream, so the downstream subcritical region cannot send information upstream to signal 'slow down gradually.' Without this upstream communication, no smooth deceleration profile can be established. The transition must therefore occur abruptly and locally — the hydraulic jump — where depth increases sharply, velocity drops, and energy is dissipated as turbulence. The inability to communicate upstream is the same reason a supersonic aircraft produces a shock wave rather than gradually decelerating to subsonic: the physics of signal propagation prevents a smooth transition across the critical threshold."
  explanation: "The Froude number analogy to the Mach number is deep here. In both cases, the transition across the critical value (Fr = 1 or M = 1) is violent because the mechanism that allows gradual adjustment — wave propagation upstream — is disabled. Engineers exploit hydraulic jumps deliberately in stilling basins to dissipate the kinetic energy of high-velocity spillway discharge, converting it to heat and turbulence rather than erosive force on the downstream channel."

- question: "A river transitions from a steep gorge (fast, shallow) to a flat floodplain (slow, deep). Which Froude regime applies in each reach, and what flow feature likely occurs at the transition?"
  type: multiple-choice
  options:
    - "Subcritical in the gorge, supercritical on the floodplain; a hydraulic jump occurs at the gorge entrance"
    - "Supercritical in the gorge, subcritical on the floodplain; a hydraulic jump occurs at the transition"
    - "Critical flow in both reaches because total energy is conserved"
    - "The Froude number is the same in both reaches because discharge is constant"
  answer: 1
  explanation: "Steep channels with high velocity and shallow depth produce high Froude numbers (supercritical). Flat channels with low velocity and deep water produce low Froude numbers (subcritical). When the supercritical flow from the gorge meets the subcritical conditions on the floodplain, a hydraulic jump forms at the transition point. The jump abruptly raises the water depth, drops the velocity, and dissipates a large fraction of kinetic energy as turbulence. This is why hydraulic jumps are common where mountain streams enter flat valleys. Option D is wrong: equal discharge doesn't imply equal Fr — velocity and depth can change together while Q = VA·D remains constant."
```

## Explainer

From your study of dimensional analysis, you know that dimensionless groups compress the relevant physics of a problem into a single ratio. The **Froude number** Fr = V/√(gD) is the group that governs free-surface flows — rivers, spillways, canals, and any flow with an air-water interface. It compares the local flow velocity V to the speed at which small gravity waves propagate on the surface, c = √(gD), where D is the depth. This ratio controls everything about open-channel hydraulics: which boundary conditions matter, whether disturbances can travel upstream, and whether flow transitions occur smoothly or violently.

Think of it this way: a gravity wave is information. When you throw a pebble into still water, ripples propagate outward in all directions at speed c. In a moving stream, those ripples still propagate at speed c relative to the water, but the water itself is moving at speed V. If V < c (Fr < 1), ripples can still move upstream relative to the ground — the flow is **subcritical** (also called tranquil). Downstream conditions can send signals upstream and influence the flow. If V > c (Fr > 1), ripples are swept downstream faster than they can propagate upstream — the flow is **supercritical** (also called rapid). Downstream conditions have no upstream influence. The boundary Fr = 1 is called **critical flow**, the condition at which a small wave is stationary relative to the ground. This is precisely analogous to the Mach number in compressible flow: in subsonic flow pressure disturbances propagate upstream; in supersonic flow they cannot.

The most dramatic consequence of this physics is the **hydraulic jump**: when a supercritical flow is forced to transition to subcritical — for example, when a high-velocity jet off a spillway meets the deeper, slower-moving water downstream — the transition cannot occur smoothly because no gradual upstream information exchange is possible. Instead, the flow undergoes an abrupt, turbulent jump in which depth increases sharply, velocity drops, and a significant fraction of kinetic energy is dissipated as heat and turbulence. Hydraulic jumps are deliberately designed into stilling basins below dams to dissipate energy harmlessly before flow re-enters a downstream channel. The Froude number of the incoming supercritical flow determines how strong the jump is and how much energy is dissipated.
