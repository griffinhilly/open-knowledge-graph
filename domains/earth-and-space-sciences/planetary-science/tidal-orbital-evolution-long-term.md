---
id: tidal-orbital-evolution-long-term
title: Tidal Evolution and Long-Term Orbital Decay
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: tidal-heating-moon-interiors
  type: hard
- id: tides
  type: hard
- id: orbital-mechanics
  type: soft
builds-toward:
- thermal-evolution-terrestrial-planets
- resonance-heating-icy-bodies
tags:
- tidal-heating
- orbital-decay
- dissipation
- long-term-evolution
stage: advanced
status: draft
---

# Tidal Evolution and Long-Term Orbital Decay

## Core Idea
Tidal dissipation causes orbits to decay over gigayear timescales through frictional heating in planetary/lunar interiors. Orbits circularize and migrate (typically inward) at rates determined by the tidal quality factor Q, internal structure, and orbital parameters. This can trigger habitability loss (Venus hot runaway) or maintain subsurface oceans (Europa, Enceladus).

## Explainer

You already understand tidal heating — the way gravitational flexing converts orbital and rotational energy into heat inside a moon or planet. And from your study of tides, you know that tidal bulges are raised by differential gravitational forces across a body. Long-term tidal evolution asks the next question: if tidal friction is continuously removing energy from an orbit, where does the orbit end up after billions of years?

The central concept is **tidal dissipation as orbital damping**. When a tidal bulge is raised on a body, friction prevents the bulge from pointing exactly at the tide-raising companion — it gets carried slightly ahead (or behind) by the body's rotation. This misaligned bulge creates a gravitational torque that transfers angular momentum between the body's spin and the orbit. For Earth and the Moon, the bulge leads because Earth rotates faster than the Moon orbits. The torque accelerates the Moon, pushing it outward (~3.8 cm/year), while simultaneously slowing Earth's rotation (days are getting longer by about 2.3 milliseconds per century). Run this process backward and you find the Moon was much closer to Earth billions of years ago — and days were much shorter.

The rate of tidal evolution depends critically on the **tidal quality factor Q**, which measures how efficiently a body dissipates tidal energy. A low Q means high dissipation (the body is "squishy" and absorbs energy readily); a high Q means low dissipation (the body is rigid and elastic). Earth's Q is roughly 12 for the ocean tides, Jupiter's is estimated at ~10⁵, and rocky moons fall somewhere in between. Q determines whether tidal evolution is fast enough to matter: Europa's relatively low Q (driven by its subsurface ocean and warm silicate interior) means tidal heating supplies enough energy to maintain a liquid water ocean beneath its ice shell — a process sustained over the age of the solar system.

The most profound consequence of long-term tidal evolution is **orbital circularization**. Tidal dissipation preferentially removes energy from eccentric orbits (because tidal flexing is strongest at closest approach), driving eccentricities toward zero over time. For an isolated two-body system, this would be the end of the story — the orbit circularizes, tidal heating stops, and the interior freezes. But in multi-moon systems like Jupiter's Galilean satellites, **orbital resonances** continuously pump eccentricity back up, fighting against tidal damping. Io, Europa, and Ganymede are locked in a 1:2:4 resonance that forces Io's eccentricity to remain nonzero despite enormous tidal dissipation, producing Io's extreme volcanism. Without the resonance, Io would have circularized and frozen long ago. This interplay between resonant forcing and tidal damping is why some icy moons have subsurface oceans while others do not — and it is central to understanding which worlds in our solar system might harbor conditions for life.
