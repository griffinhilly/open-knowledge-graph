---
id: polymer-mechanical-properties
title: Polymer Structure and Mechanical Behavior
domain: engineering
course: materials-science
prerequisites:
- id: stress-and-strain-fundamentals
  type: hard
tags:
- polymers
- elasticity
- viscoelasticity
- glass-transition
- crystallinity
stage: formal-systems
status: draft
---

# Polymer Structure and Mechanical Behavior

## Core Idea
Polymers are large chains of atoms (typically carbon) linked by covalent bonds; mechanical behavior depends on chain length, branching, cross-linking, and crystallinity. Amorphous polymers exhibit glass transition (T_g) above which they transition from glassy (hard, brittle) to rubbery (soft, deformable) behavior. Polymers are viscoelastic—they exhibit both elastic recovery and viscous flow depending on temperature and loading rate. Semicrystalline polymers (partly ordered chains) show intermediate behavior between crystalline and amorphous.

## Explainer

From stress and strain fundamentals, you know that metals deform elastically (recover fully) at small strains and plastically (permanent set) beyond yield, with the stiffness governed by the interatomic bond stiffness of the crystal lattice. Polymers add a third mode of deformation entirely: **viscoelasticity**, where the response is simultaneously elastic (spring-like, recoverable) and viscous (dashpot-like, rate-dependent and partially permanent). This behavior arises directly from the chain architecture. A long polymer chain can coil, uncoil, and reptate (snake through entanglements with neighboring chains) — processes with their own timescales that are sensitive to temperature.

The most practically important concept is the **glass transition temperature** T_g. Below T_g, polymer chains are frozen in place — there is not enough thermal energy to allow large-scale cooperative segmental motion. The material behaves like a stiff, brittle glassy solid: high modulus, low elongation, fractures without much warning. Above T_g, chain segments gain mobility, entanglements can slide, and the material becomes rubbery — low modulus, large recoverable deformation, much higher toughness. The transition is not a sharp melting point (no latent heat) but a range over which stiffness can drop by three orders of magnitude. This is why plastics that work fine at room temperature become brittle in Arctic conditions (where T_g is surpassed from above), or conversely why an elastomeric seal that works well in summer fails in winter: T_g relative to operating temperature is the key design parameter.

**Crystallinity** modifies this picture. A perfectly amorphous polymer has only T_g. A **semicrystalline** polymer (polyethylene, nylon, PEEK) contains ordered crystalline lamellae embedded in an amorphous matrix, with a true melting point T_m >> T_g. Below T_g, both phases are stiff. Between T_g and T_m, the amorphous phase is rubbery but crystalline regions act as physical cross-links, maintaining structural integrity and raising the effective stiffness far above what a purely amorphous rubber would show. Above T_m, the crystalline regions melt and the material flows. This two-phase architecture is why semicrystalline polymers are engineering plastics — they are useful across a much wider temperature range than fully amorphous ones.

Loading rate matters in ways it does not for metals, because viscoelastic relaxation has characteristic timescales. A quick impact loads a polymer faster than the chains can rearrange, so the material behaves stiffer and often more brittle — this is why some plastics shatter under impact but creep under sustained load. The ratio of loading time to the material's **relaxation time** determines which regime you are in. Engineers characterize this with the **Deborah number** (De = τ/t_load): at De >> 1 the material behaves elastically; at De << 1 it flows viscously; at De ≈ 1 you are in the complex viscoelastic regime. Creep (slow deformation under constant stress) and stress relaxation (stress decay under constant strain) are the practical manifestations of this time-dependence and must be accounted for in any polymer structural design that operates under sustained load or elevated temperature.
