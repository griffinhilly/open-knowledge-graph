---
id: rocket-propulsion-variable-mass
title: Rocket Propulsion and Variable-Mass Systems
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-momentum
  type: hard
- id: momentum-and-impulse
  type: hard
- id: natural-logarithm-and-e
  type: soft
- id: definite-integral-definition
  type: soft
builds-toward:
- space-mission-design-planetary
tags:
- momentum
- rockets
- variable-mass
- tsiolkovsky
stage: formal-systems
status: validated
---

# Rocket Propulsion and Variable-Mass Systems

## Core Idea
A rocket speeds up by throwing mass backward. Momentum conservation, applied to the rocket plus the gas it ejects, gives m dv = −v_e dm, where v_e is the exhaust speed relative to the rocket. Integrating gives the Tsiolkovsky rocket equation Δv = v_e ln(m₀/m_f), and the thrust is v_e times the rate at which mass is ejected. The logarithm explains why reaching orbit needs rockets that are mostly fuel.

## How It's Best Learned
Start with a cart on which a person throws bricks backward one at a time, and compute the speed gained per throw. Then shrink the bricks to a continuous stream and set up the momentum balance over a short time dt. Plot Δv against the mass ratio to see the logarithmic growth. Finish by adding gravity for a rocket launched vertically.

## Common Misconceptions
- A rocket needs air to push against. (The rocket pushes on its own exhaust gas; it works in a vacuum, and works slightly better there.)
- Doubling the fuel doubles the final speed. (Δv grows with the logarithm of the mass ratio, so each extra kilogram of fuel adds less speed than the last.)
- F = d(mv)/dt can be applied to the rocket alone with v dm/dt as a force. (This form is not valid for a body losing mass; the correct result comes from momentum conservation for rocket plus exhaust.)

## Questions

```yaml
- question: "A rocket in deep space starts at rest. Its exhaust speed relative to the rocket is 3000 m/s. It burns fuel until its mass falls from m₀ to m₀/e², where e ≈ 2.718. What is its final speed?"
  type: multiple-choice
  options: ["1500 m/s", "3000 m/s", "6000 m/s", "22,000 m/s"]
  answer: 2
  explanation: "Δv = v_e ln(m₀/m_f) = 3000 m/s × ln(e²) = 3000 × 2 = 6000 m/s."
- question: "A rocket engine would produce no thrust in the vacuum of space, because there is no air for the exhaust to push against."
  type: true-false
  answer: false
  explanation: "Thrust comes from the momentum given to the exhaust. By momentum conservation, the rocket gains equal and opposite momentum. No outside medium is needed."
- question: "A rocket has mass ratio m₀/m_f = 4. Which change gives the larger final speed: doubling the exhaust speed, or doubling the mass ratio to 8?"
  type: multiple-choice
  options: ["Doubling the exhaust speed", "Doubling the mass ratio", "Both give the same final speed", "Neither changes the final speed"]
  answer: 0
  explanation: "Doubling v_e doubles Δv, from v_e ln 4 to 2v_e ln 4. Doubling the mass ratio gives v_e ln 8 = 1.5 v_e ln 4, only 50% more."
- question: "An engine ejects 40 kg of gas per second at 2500 m/s relative to the rocket. What thrust does it produce?"
  type: short-answer
  answer: "100,000 N (100 kN)"
  explanation: "Thrust = v_e |dm/dt| = 2500 m/s × 40 kg/s = 1.0 × 10⁵ N."
```

## Explainer
Picture a rocket of mass m moving at speed v in empty space. In a short time dt it ejects a small mass of gas, dm_gas, backward at speed v_e relative to itself. Treat the rocket and that gas as one system. No outside force acts, so the total momentum stays the same. Before the burn the momentum is mv. After the burn the rocket has mass m − dm_gas and speed v + dv, and the gas moves at v − v_e. Writing out the momentum before and after, and dropping the tiny product of two small quantities, gives m dv = v_e dm_gas.

The rocket's mass falls by exactly the mass of gas it ejects, so dm = −dm_gas. The equation becomes dv = −v_e dm/m. Integrating from the starting mass m₀ to the final mass m_f gives

Δv = v_e ln(m₀/m_f).

Konstantin Tsiolkovsky published this result in 1903, and it carries his name. Two features stand out. First, the speed gained does not depend on how fast the fuel burns. Only the exhaust speed and the mass ratio matter. Second, the dependence on mass ratio is a logarithm. A mass ratio of e (about 2.7) gives Δv = v_e. A mass ratio of 10 gives only about 2.3 v_e. Reaching low Earth orbit needs roughly 9 to 10 km/s once losses to gravity and drag are counted. Chemical exhausts reach about 2.5 to 4.5 km/s, so a single stage would need to be overwhelmingly fuel. Engineers use stages for this reason: dropping empty tanks restores a good mass ratio for the next burn.

Dividing the momentum balance by dt gives the thrust, F = v_e |dm/dt|. For a launch from the ground, gravity acts on the rocket as well, so m dv/dt = v_e |dm/dt| − mg. The rocket lifts off only if the thrust exceeds its weight.

The same method of tracking momentum for the whole system works for any variable-mass problem. Examples include a conveyor belt that collects sand, a raindrop that grows as it falls, and a chain that slides off a table. In each case, draw the system boundary to include the mass that enters or leaves, then apply conservation of momentum or the impulse-momentum theorem to the whole system.
