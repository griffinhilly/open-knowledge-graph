---
id: jet-mixing-and-entrainment
title: 'Incompressible Jet Flow: Mixing and Entrainment'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: control-volume-momentum-applications
  type: hard
tags:
- jets
- mixing
- entrainment
stage: formal-systems
status: draft
---

# Incompressible Jet Flow: Mixing and Entrainment

## Core Idea
Free jets issuing from nozzles entrain surrounding fluid through turbulent mixing, which decreases centerline velocity and increases jet diameter with distance. The mass flow rate increases while total momentum decreases (momentum transferred to entrained fluid), eventually decaying to ambient conditions. Jet mixing is exploited in ejectors, jet fans, and mixing devices; accurate entrainment prediction requires understanding turbulent diffusion.

## Explainer

Picture a garden hose nozzle discharging a fast-moving stream into still air. The jet does not travel as a rigid column — it grows wider with distance, its edges become ragged and turbulent, and the centerline velocity gradually falls. The surrounding fluid is not passive; the turbulent shear at the jet boundary continuously pulls ambient fluid into the jet and accelerates it from rest up to nearly the local jet velocity. This process is **entrainment**, and it fundamentally changes both the mass flow and the velocity distribution along the jet.

From your control volume momentum analysis, you know that momentum is conserved only when no external force acts. For a free jet issuing into an open, quiescent environment with no pressure gradient, the streamwise momentum flux is essentially constant close to the nozzle. But as the jet entrains more and more ambient fluid — fluid that started with zero momentum — that added mass must share in the total momentum. The result is a tradeoff: mass flow rate increases continuously with downstream distance, while **centerline velocity** decreases to compensate. Far enough downstream, the original high-speed core is completely mixed with the surroundings and has decayed to ambient conditions.

The **entrainment rate** scales with the local velocity difference between the jet and the surrounding fluid. Turbulent eddies at the jet edge roll up and engulf ambient fluid — this is not smooth molecular diffusion but vigorous turbulent mixing. The jet spreads at a roughly constant half-angle (about 5–12° for a round jet in still air depending on conditions), meaning the jet diameter grows linearly with downstream distance. The centerline velocity decays inversely with distance from the nozzle exit.

This behavior is exploited in practical devices. An **ejector** or **jet pump** uses a high-velocity primary jet to entrain and accelerate a secondary fluid stream — the entrainment does the pumping work without any rotating parts. **Jet fans** in vehicle tunnels entrain large volumes of tunnel air to drive ventilation. In combustion chambers and chemical reactors, jet mixing controls how rapidly reactants blend, directly affecting reaction efficiency. Understanding the entrainment ratio — how many kilograms of ambient fluid are pulled in per kilogram of primary jet flow — is central to designing all of these systems.
