---
id: planetary-formation-disk-instability
title: 'Planetary Formation II: Gravitational Instability and Direct Collapse'
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: planetary-formation
  type: soft
- id: protoplanetary-disk-structure
  type: soft
tags:
- planet-formation
- disk-instability
- direct-collapse
stage: formal-systems
status: draft
---

# Planetary Formation II: Gravitational Instability and Direct Collapse

## Core Idea
In sufficiently massive and cool protoplanetary disks, the disk itself can become gravitationally unstable, fragmenting into massive clumps that rapidly collapse into giant planets on timescales of hundreds to thousands of years. This mechanism is especially relevant for explaining the most distant, massive planets in exoplanet systems where core accretion alone would be too slow.

## Questions

```yaml
- question: "A massive giant planet is observed orbiting at 60 AU from its host star. Core accretion struggles to explain this planet's formation. What is the primary reason core accretion fails at such distances?"
  type: multiple-choice
  options:
    - "At 60 AU, the protoplanetary disk is too hot for planetesimals to stick together"
    - "Stellar radiation at 60 AU prevents gas from accumulating around rocky cores"
    - "At large orbital distances, orbital periods are long and disk material is sparse, making core growth too slow — the gas disk dissipates before a core can capture a hydrogen envelope"
    - "The Toomre Q parameter is always greater than 1 at large distances, preventing any planet formation"
  answer: 2
  explanation: "Core accretion is a bottom-up process requiring millions of years to build a rocky core large enough to capture gas. At large orbital distances (50–100 AU), the physical timescale problem is severe: orbital periods are long (objects move slowly relative to one another), the surface density of solids is low, and collisional growth is extremely slow. Protoplanetary disks typically disperse within a few million years. Core accretion simply cannot build a massive core quickly enough at these distances before the gas disk disappears. Disk instability, which can form a massive planet in thousands of years, provides the only plausible mechanism for observed planets at wide separations."

- question: "A protoplanetary disk has Toomre Q < 1, meaning it is gravitationally unstable. Under what additional condition will the disk actually fragment into bound objects rather than simply developing spiral density waves?"
  type: multiple-choice
  options:
    - "The disk must be rotating faster than the local orbital velocity"
    - "The disk must be closer than 10 AU to the host star"
    - "The cooling timescale must be short enough for collapsing regions to radiate away heat before thermal pressure halts contraction"
    - "The disk mass must exceed the mass of the host star"
  answer: 2
  explanation: "Gravitational instability is a necessary but not sufficient condition for fragmentation. When a disk region collapses, compression heats the gas. If this heat cannot be radiated away quickly (slow cooling), the pressure buildup halts the collapse and the perturbation instead develops into a spiral arm that redistributes angular momentum without forming a bound object. Only if cooling is rapid enough — the cooling timescale is short compared to the dynamical timescale — can a collapsing clump lose its pressure support and continue contracting into a planet. This cooling criterion is why fragmentation preferentially occurs in the outer, cooler regions of disks."

- question: "Disk instability can form giant planets on timescales of hundreds to thousands of years — orders of magnitude faster than core accretion."
  type: true-false
  answer: true
  explanation: "This is one of the most striking features of the disk instability mechanism. Because it works by direct gravitational collapse of the disk itself — rather than the incremental bottom-up process of core accretion — it can produce a giant planet in as little as hundreds to thousands of years. Core accretion typically requires millions of years to form a giant planet. This dramatic timescale difference is precisely why disk instability is invoked for planets at large orbital separations where core accretion cannot operate fast enough before the disk disperses."

- question: "A protoplanetary disk with Toomre Q < 1 will always fragment directly into planetary-mass objects, regardless of other disk properties."
  type: true-false
  answer: false
  explanation: "Q < 1 is necessary but not sufficient for fragmentation. Even a gravitationally unstable disk (Q < 1) may not fragment if its cooling timescale is too long. In that case, the disk develops spiral density waves — a non-fragmenting response that redistributes angular momentum and mass without forming bound clumps. The disk may also heat up due to the energy released by these waves, raising Q back above 1 and suppressing fragmentation. True fragmentation into bound objects requires Q < 1 AND rapid enough cooling, typically expressed as the cooling timescale being less than a few times the orbital period."

- question: "Why does disk instability preferentially operate in the outer regions of protoplanetary disks, and why is this complementary to core accretion rather than competing with it?"
  type: short-answer
  answer: "Disk instability requires a disk that is massive enough for self-gravity to overcome thermal pressure and rotational shear (Q < 1) and cool enough for the cooling timescale to be short. The outer disk naturally meets both conditions: it is cooler (lower temperatures give less thermal pressure support) and — in massive disks — can accumulate enough surface density relative to the reduced stellar tidal forces at large radii. Core accretion, by contrast, is most effective in the inner and middle disk where orbital timescales are short and solid density is higher, but it cannot form giant planets at large separations before the disk dissipates. The two mechanisms together explain the full range of observed planetary architectures: core accretion in the inner disk for terrestrial and gas giant planets at moderate distances, disk instability in the outer disk for directly-imaged super-Jupiters at tens to hundreds of AU."
  explanation: "The HR 8799 system, with four giant planets at 15–70 AU, is a key example that is very difficult to explain by core accretion alone and strongly suggests disk instability operated in that system's outer disk. Recognizing that the two mechanisms occupy different niches in parameter space (distance from star, disk mass, cooling efficiency) resolves what initially seems like a competition into a complementary picture."
```

## Explainer

From your study of planetary formation, you know the standard **core accretion** model: small dust grains stick together into pebbles, then planetesimals, then rocky cores, and if the core grows massive enough before the gas disk dissipates, it captures a hydrogen-helium envelope to become a gas giant. This process works well for explaining planets like Jupiter at moderate orbital distances, but it has a timescale problem. Core accretion requires millions of years, and at large orbital distances (50–100 AU from the star), the orbital periods are so long and the disk material so sparse that building a core big enough to capture gas would take longer than the disk itself survives. Yet we observe massive planets at exactly these distances. Something else must be at work.

**Gravitational instability** offers an alternative pathway. Instead of building a planet from the bottom up, this mechanism works from the top down. If a protoplanetary disk is sufficiently massive relative to its host star and cool enough that thermal pressure cannot resist its own self-gravity, the disk can fragment directly into dense clumps. Each clump contains enough mass to collapse under its own gravity into a giant planet — or even a brown dwarf — on astonishingly short timescales of just hundreds to thousands of years. Think of it like the difference between building a snowman one handful at a time versus watching a snow cornice fracture and collapse into a massive block all at once.

The key criterion governing this process is the **Toomre stability parameter** (Q). When Q drops below a critical threshold (roughly Q ≈ 1), the disk becomes unstable to fragmentation. Q depends on the balance between three competing effects: the disk's self-gravity (which promotes collapse), thermal pressure (which resists it), and rotational shear (which tears clumps apart). A disk fragments when it is massive enough for gravity to dominate, cool enough for pressure support to be weak, and when the cooling timescale is short enough that collapsing regions can radiate away their heat before pressure halts the contraction. If cooling is too slow, the disk develops spiral density waves — redistributing angular momentum — without actually fragmenting into bound objects.

This mechanism is most effective in the outer regions of massive disks, precisely where core accretion struggles. It naturally produces planets that are very massive (several Jupiter masses or more) at wide separations from their host star. Observations of directly imaged exoplanets — such as the HR 8799 system, where four giant planets orbit at distances of 15–70 AU — are difficult to explain by core accretion alone and are strong candidates for disk instability formation. The two mechanisms are not mutually exclusive: core accretion likely dominates in the inner disk, while gravitational instability may operate in the outer disk, together explaining the full diversity of planetary architectures we observe.
