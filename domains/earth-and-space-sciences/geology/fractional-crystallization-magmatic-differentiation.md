---
id: fractional-crystallization-magmatic-differentiation
title: Fractional Crystallization and Magmatic Differentiation
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: magma-composition-viscosity-rheology
  type: hard
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: bowen-fractional-crystallization
  type: soft
builds-toward:
- crustal-composition-differentiation
tags:
- magmatism
- crystallization
- differentiation
stage: advanced
status: validated
---
# Fractional Crystallization and Magmatic Differentiation

## Core Idea
As magma cools, minerals crystallize in a sequence determined by equilibrium thermodynamics (Bowen's reaction series). Early-formed crystals are typically denser and sink; liquid becomes progressively enriched in incompatible elements. This process explains compositional variation within individual magma chambers and layered igneous complexes.

## Questions

```yaml
- question: "A basaltic magma is cooling in a deep chamber. Early-formed olivine and pyroxene crystals settle to the chamber floor. How does the composition of the residual liquid evolve?"
  type: multiple-choice
  options:
    - "It becomes enriched in magnesium and iron as less dense olivine buoys upward and concentrates near the top."
    - "It becomes progressively enriched in silica, sodium, potassium, and incompatible elements as iron- and magnesium-rich minerals are removed."
    - "It remains constant in composition because total mass is conserved when crystals settle."
    - "It becomes more mafic because removing dense minerals concentrates the remaining mafic constituents."
  answer: 1
  explanation: "Olivine and pyroxene are rich in Mg and Fe but poor in Si, Na, K, and incompatible elements like Rb, Ba, and U. When these minerals are physically removed by settling, the residual liquid is depleted in Mg and Fe and therefore relatively enriched in everything else — Si, Na, K, and incompatible elements. Continued fractionation can evolve basaltic liquid through andesitic to rhyolitic compositions. Option C is the classic misconception: mass conservation applies to the whole system (crystals + liquid), not to the liquid alone."

- question: "Two geologists debate whether fractional crystallization occurred in a magma body. The first argues that sequential crystallization (olivine before pyroxene before plagioclase) proves differentiation. The second says the crystallization sequence alone is insufficient. Who is correct?"
  type: multiple-choice
  options:
    - "The first geologist — sequential crystallization according to Bowen's reaction series guarantees compositional evolution of the melt."
    - "The second geologist — differentiation requires physical removal of crystals; if they remain and react with the melt, the system re-equilibrates and no net compositional change occurs."
    - "Both are wrong — fractional crystallization only occurs in shallow volcanic systems, not deep intrusions where pressure inhibits crystal settling."
    - "The first geologist — Bowen's reaction series predicts the same differentiation path regardless of crystal fate."
  answer: 1
  explanation: "The critical word is 'fractional': it means removal of crystalline phases from the system. If early crystals remain in contact with the melt and continue reacting with it (equilibrium crystallization), the system follows Bowen's series but re-equilibrates at each temperature step — the bulk composition of the melt tracks the equilibrium path and there is no net differentiation. Only when crystals are physically isolated (by settling, wall crystallization, or filter pressing) does the remaining liquid permanently lose those components, driving compositional evolution. The sequence itself proves only that minerals crystallized; it says nothing about whether they were removed."

- question: "If early-formed crystals in a magma chamber remain in contact with the cooling melt and react continuously with it, the residual liquid will still evolve toward a more silica-rich composition over time."
  type: true-false
  answer: false
  explanation: "This is the key distinction between equilibrium and fractional crystallization. When crystals remain in contact with the melt, they undergo back-reactions according to Bowen's reaction series — olivine reacts with melt to form pyroxene, etc. The system maintains chemical equilibrium at each temperature, and the bulk composition of the melt does not permanently change (crystals and melt exchange components). Only physical removal of crystals prevents back-reaction and allows the melt to 'lock in' a depleted composition, driving differentiation."

- question: "Layered igneous intrusions like the Bushveld Complex preserve direct physical evidence of fractional crystallization as compositional layers of dense, early-crystallizing minerals concentrated at the base of the intrusion."
  type: true-false
  answer: true
  explanation: "Layered intrusions are essentially the stratigraphic record of fractional crystallization frozen in rock. Dense early-crystallizing minerals (chromite, olivine, pyroxene) settled to the chamber floor, forming cumulate layers. Higher in the sequence, the composition becomes progressively more evolved (less mafic), reflecting the changing liquid composition as fractionation proceeded. These rhythmic layers of contrasting mineral assemblages are the most direct evidence that crystal settling and melt evolution occurred, and they allow geologists to reconstruct the differentiation history of the magma."

- question: "Why is physical separation of crystals from the melt the essential step in fractional crystallization? What happens if crystals are not removed?"
  type: short-answer
  answer: "Physical separation prevents early-formed crystals from reacting back with the melt. If crystals remain in contact, they exchange elements with the melt to maintain chemical equilibrium at each temperature step — Bowen's back-reactions proceed, and the melt's bulk composition re-equilibrates rather than diverging. Only once crystals are removed (by gravitational settling, convective plastering against walls, or filter pressing) does the melt permanently lose those elements, creating a compositional gap between the crystallized fraction and the residual liquid. Each removal step permanently shifts the melt composition, and repeated steps can drive it from basaltic to andesitic to rhyolitic — the full suite of differentiation products."
  explanation: "The word 'fractional' encodes the concept: the system is separated into fractions (crystal fraction vs. liquid fraction) before equilibrium is re-established. Without separation, it is simply 'equilibrium crystallization,' which produces a single rock type with the same bulk composition as the original magma. Fractional crystallization produces a spectrum of rock types from a single parent magma — which is why it is the primary explanation for igneous diversity."
```

## Explainer

You already understand that magma composition controls its viscosity and behavior. Fractional crystallization explains how a single parent magma can produce a whole family of different rock types as it cools — it is the primary engine of **magmatic differentiation**. The process follows directly from thermodynamics: as temperature drops, the minerals with the highest melting points crystallize first, removing certain elements from the liquid and changing the composition of what remains.

**Bowen's reaction series** provides the roadmap. On the discontinuous branch, olivine crystallizes first from a basaltic melt, followed by pyroxene, amphibole, and biotite as temperature falls. On the continuous branch, calcium-rich plagioclase crystallizes early and becomes progressively more sodium-rich. The key to differentiation is *separation*: if early-formed crystals remain in contact with the liquid, they react with it and the system stays in equilibrium — no differentiation occurs. But if crystals are physically removed — by settling to the chamber floor under gravity, by being plastered against chamber walls by convection currents, or by filter pressing — the remaining liquid evolves to a new, more silica-rich composition. This is **fractional** crystallization: the progressive removal of crystalline phases from a cooling melt.

Consider a basaltic magma crystallizing olivine and pyroxene early on. These minerals are rich in magnesium and iron but poor in silica, sodium, and potassium. As they settle out, the remaining liquid becomes depleted in Mg and Fe but enriched in Si, Na, K, and elements that do not fit easily into early-crystallizing mineral structures — the so-called **incompatible elements** like rubidium, barium, and uranium. Through continued fractionation, an initially basaltic liquid can evolve through intermediate (andesitic) compositions toward silica-rich (rhyolitic or granitic) compositions. This is why a single volcanic system can erupt basalt early in its history and rhyolite later — the magma chamber has been differentiating.

The physical evidence for this process is beautifully preserved in **layered igneous intrusions** like the Bushveld Complex in South Africa or the Skaergaard intrusion in Greenland. These bodies show rhythmic layers of dense, early-crystallizing minerals (chromite, olivine, pyroxene) alternating with more evolved compositions higher in the sequence — essentially a frozen record of fractional crystallization captured in rock. The equilibrium constant concepts from chemistry apply here: each mineral crystallizes when the melt composition reaches the saturation point for that phase, and the sequence of saturation points defines the crystallization path. Understanding this process is essential for explaining crustal composition and differentiation at the planetary scale, where billions of years of fractional crystallization have progressively concentrated incompatible elements into the continental crust.
