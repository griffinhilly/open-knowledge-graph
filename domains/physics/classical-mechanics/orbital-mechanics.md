---
id: orbital-mechanics
title: 'Orbital Mechanics: Circular and Elliptical Orbits'
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-law-of-gravitation
  type: hard
- id: circular-motion-dynamics
  type: hard
- id: conservation-of-energy
  type: soft
- id: polar-coordinates
  type: soft
- id: conic-sections-ellipses
  type: soft
- id: differential-equations-intro
  type: hard
builds-toward:
- keplers-laws
tags:
- orbits
- circular-orbit
- gravitational-force
- orbital-velocity
stage: formal-systems
status: validated
---

# Orbital Mechanics: Circular and Elliptical Orbits

## Core Idea
A satellite in a circular orbit is in free fall: gravity provides exactly the centripetal force needed to maintain circular motion. Setting GMm/r² = mv²/r gives orbital speed v = √(GM/r) and period T = 2π r^(3/2) / √(GM). The total mechanical energy of a circular orbit is E = −GMm/(2r): negative, indicating a bound orbit. Elliptical orbits are more general and governed by the same gravitational law with energy E = −GMm/(2a), where a is the semi-major axis.

## How It's Best Learned
Derive orbital speed and period for circular orbits, then extend to geostationary orbit calculations (find the orbital radius where T = 24 hours). Compare the energy of a circular orbit at different radii to understand why lower orbits move faster.

## Common Misconceptions
- Thinking astronauts in orbit are weightless because there is no gravity: they are in free fall, accelerating toward Earth at the same rate as their spacecraft, producing the sensation of weightlessness.
- Believing that firing rocket engines always speeds up a spacecraft: it depends on the burn direction relative to the velocity vector.

## Questions

```yaml
- question: "A satellite is moved from a circular orbit of radius r to a new circular orbit of radius 4r. By what factor does its orbital speed change?"
  type: multiple-choice
  options: ["It increases by a factor of 2", "It decreases by a factor of 2", "It decreases by a factor of 4", "It stays the same"]
  answer: 1
  explanation: "Orbital speed v = √(GM/r), so v ∝ 1/√r. When r increases by a factor of 4, v changes by a factor of 1/√4 = 1/2. The satellite in the larger orbit moves half as fast. This is counterintuitive: boosting a satellite to a higher orbit requires adding energy, yet the satellite ends up moving more slowly."

- question: "Astronauts aboard the International Space Station experience weightlessness because there is no significant gravity at that altitude."
  type: true-false
  answer: false
  explanation: "At ISS altitude (~400 km), Earth's gravitational field is roughly 90% as strong as on the surface. Astronauts feel weightless because the station and everything in it is in free fall — all objects accelerate toward Earth at the same rate. There is no normal force from the floor because the floor is also falling. Weightlessness is the sensation of free fall, not the absence of gravity."

- question: "Why is the total mechanical energy of a circular orbit negative?"
  type: short-answer
  answer: "A negative total energy indicates a bound orbit: the satellite lacks the kinetic energy to escape the gravitational potential well. E = KE + PE = GMm/(2r) − GMm/r = −GMm/(2r). The magnitude of potential energy exceeds kinetic energy, so the total is negative."
  explanation: "The sign of total mechanical energy distinguishes bound from unbound trajectories. E < 0 means the orbit is bound (circle or ellipse). E = 0 corresponds to an escape trajectory (parabola). E > 0 means the object escapes with kinetic energy to spare (hyperbola). This follows from how gravitational potential energy (negative by convention) relates to kinetic energy in orbit."
```

## Explainer

You know from Newton's law of gravitation that every mass attracts every other, and from circular motion dynamics that something moving in a circle requires a centripetal force directed inward. Orbital mechanics combines these ideas: a satellite in a circular orbit is in a state of continuous free fall where gravity provides exactly the centripetal force needed to curve the trajectory into a circle. Setting gravitational force equal to centripetal force: GMm/r² = mv²/r. Solving for v gives the orbital speed v = √(GM/r).

Two features of this result are crucial. First, the satellite's mass m cancels — orbital speed is independent of the object's mass. A feather and a boulder at the same altitude orbit at the same speed. Second, v ∝ 1/√r: satellites in lower orbits move *faster*. This seems backwards — you might expect adding energy to speed things up — but adding energy raises the orbital radius, and the speed formula says radius and speed trade off as 1/√r. The orbital period follows as T = 2πr/v = 2πr^(3/2)/√(GM), which is Kepler's third law: period grows as r^(3/2), so higher orbits have longer periods. A geostationary satellite (T = 24 hours) must orbit at a specific radius — approximately 42,000 km from Earth's center — uniquely determined by this formula.

The total mechanical energy of a circular orbit is E = KE + PE = ½mv² − GMm/r. Substituting v² = GM/r gives E = −GMm/(2r). The negative sign is significant: it means the satellite is gravitationally bound and lacks the energy to escape. The more negative E is (smaller r), the more tightly bound the orbit. To raise a satellite to a higher orbit you must add energy — making E less negative. Elliptical orbits generalize this: E = −GMm/(2a), where a is the semi-major axis. A circle is the special case where a = r; the same energy formula holds throughout.

The misconception about weightlessness deserves careful attention. The ISS orbits at about 400 km altitude, where Earth's gravity is still roughly 90% of its surface value. Astronauts are not outside gravity's reach — they are in continuous free fall toward Earth. Because the station and every object inside it fall at the same rate, there is no relative acceleration between them. The floor of the station does not push up on your feet because it is falling at the same rate you are. Weightlessness is the subjective experience of free fall — a distinction that becomes vivid once you understand that gravity is providing the centripetal acceleration keeping the station in orbit rather than sending it crashing to Earth.
