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

## Questions

```yaml
- question: "A round turbulent jet issues from a nozzle at 20 m/s. At a cross-section 40 diameters downstream, the centerline velocity has dropped to 4 m/s. Compared to the nozzle exit, what has happened to the total mass flow rate and the total streamwise momentum flux at this cross-section?"
  type: multiple-choice
  options:
    - "Mass flow rate has decreased and momentum flux has decreased — energy is lost to viscous dissipation along the way"
    - "Mass flow rate has increased and momentum flux is approximately unchanged — ambient fluid has been entrained but it shares in the original momentum"
    - "Mass flow rate is unchanged because no new fluid enters, and momentum flux has decreased because velocity fell"
    - "Both mass flow rate and momentum flux have increased — turbulence generates additional momentum through pressure fluctuations"
  answer: 1
  explanation: "Entrainment continuously draws in ambient fluid with zero initial streamwise momentum, so mass flow rate grows continuously downstream. But in a free jet with no external pressure gradient, total streamwise momentum flux is approximately conserved. The original momentum is now shared over a much larger mass of fluid (jet plus entrained ambient), so centerline velocity falls to compensate. This tradeoff — increasing mass flow, decreasing centerline velocity, constant momentum — is the defining characteristic of jet flow."

- question: "What is the primary physical mechanism responsible for entrainment in a turbulent jet?"
  type: multiple-choice
  options:
    - "Viscous molecular diffusion gradually pulls adjacent fluid molecules into the jet through intermolecular attraction at the jet boundary"
    - "A favorable pressure gradient along the jet axis draws ambient fluid inward from the surrounding environment"
    - "Large-scale turbulent eddies at the jet shear layer engulf and accelerate whole parcels of ambient fluid into the jet"
    - "The Bernoulli effect reduces static pressure in the high-velocity jet core, causing ambient fluid to be pushed inward by the surrounding pressure"
  answer: 2
  explanation: "In a turbulent jet, entrainment is dominated by turbulent engulfment: large eddies roll up at the interface between the high-speed jet and the still surroundings, wrapping up and incorporating large volumes of ambient fluid. This is fundamentally different from molecular diffusion, which is far too slow to account for the observed spreading rates. While pressure gradients and Bernoulli effects play minor roles, the turbulent eddy mechanism is the primary driver and explains why jet spreading and entrainment increase dramatically once the flow becomes turbulent."

- question: "As a turbulent free jet travels downstream, its mass flow rate continuously increases while its centerline velocity continuously decreases."
  type: true-false
  answer: true
  explanation: "True. This is the core consequence of entrainment. Ambient fluid with zero momentum is continuously incorporated into the jet, increasing the total mass flowing through successive cross-sections. Since total streamwise momentum is approximately conserved (no external force), more mass must move at lower average velocity. For a round jet, centerline velocity decays approximately as 1/x (inversely with distance from the nozzle) while jet diameter grows approximately linearly with x."

- question: "Entraining more ambient fluid into a free jet increases the jet's total streamwise momentum flux, since more fluid mass is being transported downstream."
  type: true-false
  answer: false
  explanation: "False. The entrained ambient fluid starts with zero streamwise momentum. Adding zero-momentum fluid to the jet does not increase total momentum — it dilutes the existing momentum over a larger mass, causing velocity to decrease. For a free jet in a quiescent environment with no external pressure gradient, total streamwise momentum flux is approximately conserved, not increased. The mass flow rate grows but the momentum flux stays roughly constant. Confusing increasing mass flow with increasing momentum is the classic error in jet analysis."

- question: "Explain the tradeoff between mass flow rate and centerline velocity in a turbulent free jet, and why this tradeoff follows from momentum conservation."
  type: short-answer
  answer: "A free jet exits the nozzle with a fixed momentum flux (mass flow rate × velocity). As it travels downstream, turbulent mixing draws in ambient fluid that initially has zero streamwise momentum. No external force acts in the streamwise direction, so total momentum flux is conserved. But the mass flow rate now includes all the entrained fluid, so the same total momentum must be shared over a continuously growing mass. By conservation of momentum, larger mass at lower velocity carries the same momentum as smaller mass at higher velocity — hence centerline velocity falls as mass flow grows. The two effects are not independent: they are directly linked by the constraint that momentum is conserved."
  explanation: "This analysis is why ejectors work: a high-speed primary jet entrains and accelerates a secondary fluid stream, transferring momentum from the primary to the secondary without any moving parts. The momentum budget — fixed total shared over growing mass — is the mechanism behind all jet-pump and ejector designs."
```

## Explainer

Picture a garden hose nozzle discharging a fast-moving stream into still air. The jet does not travel as a rigid column — it grows wider with distance, its edges become ragged and turbulent, and the centerline velocity gradually falls. The surrounding fluid is not passive; the turbulent shear at the jet boundary continuously pulls ambient fluid into the jet and accelerates it from rest up to nearly the local jet velocity. This process is **entrainment**, and it fundamentally changes both the mass flow and the velocity distribution along the jet.

From your control volume momentum analysis, you know that momentum is conserved only when no external force acts. For a free jet issuing into an open, quiescent environment with no pressure gradient, the streamwise momentum flux is essentially constant close to the nozzle. But as the jet entrains more and more ambient fluid — fluid that started with zero momentum — that added mass must share in the total momentum. The result is a tradeoff: mass flow rate increases continuously with downstream distance, while **centerline velocity** decreases to compensate. Far enough downstream, the original high-speed core is completely mixed with the surroundings and has decayed to ambient conditions.

The **entrainment rate** scales with the local velocity difference between the jet and the surrounding fluid. Turbulent eddies at the jet edge roll up and engulf ambient fluid — this is not smooth molecular diffusion but vigorous turbulent mixing. The jet spreads at a roughly constant half-angle (about 5–12° for a round jet in still air depending on conditions), meaning the jet diameter grows linearly with downstream distance. The centerline velocity decays inversely with distance from the nozzle exit.

This behavior is exploited in practical devices. An **ejector** or **jet pump** uses a high-velocity primary jet to entrain and accelerate a secondary fluid stream — the entrainment does the pumping work without any rotating parts. **Jet fans** in vehicle tunnels entrain large volumes of tunnel air to drive ventilation. In combustion chambers and chemical reactors, jet mixing controls how rapidly reactants blend, directly affecting reaction efficiency. Understanding the entrainment ratio — how many kilograms of ambient fluid are pulled in per kilogram of primary jet flow — is central to designing all of these systems.
