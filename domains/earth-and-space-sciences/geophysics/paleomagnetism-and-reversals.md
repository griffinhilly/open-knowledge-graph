---
id: paleomagnetism-and-reversals
title: Paleomagnetism and Magnetic Reversals
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: magnetic-field-definition
  type: soft
- id: electromagnetic-field-tensor
  type: soft
builds-toward:
- paleomagnetic-dating-and-stratigraphy
tags:
- paleomagnetism
- reversals
- magnetostratigraphy
- remanence
stage: expert
status: validated
---

# Paleomagnetism and Magnetic Reversals

## Core Idea
Rock magnetization acquires a remanent magnetization (TRM in igneous rocks, DRM in sediments) parallel to Earth's magnetic field at the time of formation, preserving a record of ancient field directions. Paleomagnetic reversals—sudden switches of the dipole polarity (north ↔ south)—occur irregularly on timescales of 200,000 to millions of years; the reversal rate accelerated in the Cenozoic. The paleomagnetic record provides a dating tool and reveals true polar wander and apparent polar wander paths used in plate reconstruction.

## Questions

```yaml
- question: "Geologists sample an ancient volcanic layer and find its magnetic minerals have reversed polarity — pointing toward the current south magnetic pole. What is the most direct interpretation?"
  type: multiple-choice
  options:
    - "The volcanic rock was erupted at high southern latitudes where field polarity is reversed"
    - "Earth's magnetic field had opposite polarity when the rock cooled through its Curie temperature"
    - "The rock's minerals were chemically altered after formation, reversing the recorded direction"
    - "The rock was physically rotated 180° by tectonic forces after it formed"
  answer: 1
  explanation: "Thermoremanent magnetization (TRM) locks in the ambient field direction when an igneous rock cools below its Curie temperature (~580°C for magnetite). Reversed polarity in the rock records reversed polarity in Earth's field at that time — not the rock's latitude, not post-formation alteration (which would require specific conditions and usually leaves other geochemical signatures), and not tectonic rotation (which would also rotate other features in a recognizable way). The clean interpretation is that the geodynamo was running in reverse when the rock solidified."

- question: "Paleomagnetic data from a continent show that the apparent polar wander path (APWP) diverges significantly from the modern pole position going back 300 million years. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "Earth's geographic poles migrated substantially over the past 300 million years"
    - "The continent moved relative to a relatively stable pole, changing the inclination recorded in rocks"
    - "The paleofield was much weaker 300 million years ago, giving unreliable inclination data"
    - "The magnetic field completely reorganized into a non-dipolar configuration 300 million years ago"
  answer: 1
  explanation: "The APWP traces the apparent position of the pole as reconstructed from the inclination of remanent magnetization in rocks. The field's dipole axis has not dramatically wandered; rather, the continent moved. Since inclination encodes latitude (tan I = 2 tan λ), a rock formed at lower latitude shows shallower inclination. If a continent was near the equator 300 Ma and is now at 50°N, rocks of that age show shallow inclination — the 'pole' appears to have been at low latitude relative to the continent's current position. Two continents that share an APWP were joined; divergent APWPs record separation."

- question: "Geomagnetic reversals occur at regular, predictable intervals — roughly every 200,000 years — and can therefore be forecast."
  type: true-false
  answer: false
  explanation: "Polarity reversals are highly irregular. The intervals between reversals range from tens of thousands to tens of millions of years, with no detectable periodicity. The Cretaceous Normal Superchron lasted ~40 million years without a reversal; other intervals have seen many reversals in rapid succession. This irregularity is why the geomagnetic polarity timescale (GPTS) must be calibrated by radiometric dating of individual volcanic horizons rather than extrapolated from a regular clock. Reversals cannot be forecast from the timing of past reversals."

- question: "An apparent polar wander path represents the actual movement of Earth's geographic and magnetic poles through geological time."
  type: true-false
  answer: false
  explanation: "The 'apparent' in APWP is crucial — the pole's apparent position relative to the continent changed primarily because the continent moved, not because the pole itself migrated substantially. Earth's dipole axis stays roughly aligned with the rotation axis over long time averages (the geocentric axial dipole hypothesis). When two continents that were once joined show APWPs that converge into a single path going back in time, it is because they shared the same pole position when joined. The continent is the mobile object; the pole is the relatively stable reference."

- question: "Why can the paleomagnetic inclination recorded in a rock tell you the latitude at which that rock formed?"
  type: short-answer
  answer: "Earth's dipole field produces inclination that varies systematically with latitude: the field is horizontal at the equator (inclination = 0°) and vertical at the poles (inclination = 90°). The relationship is tan(I) = 2·tan(λ), where I is inclination and λ is latitude. When magnetic minerals lock in TRM or DRM, they record the inclination of the ambient field. By measuring the remanent inclination in the rock and applying this formula, you can calculate the latitude at which the rock formed. If that paleolatitude differs from the rock's current latitude, the plate has moved."
  explanation: "This is the quantitative basis for plate tectonic reconstruction from paleomagnetism. The geocentric axial dipole hypothesis — that Earth's field averages to a geocentric dipole aligned with the rotation axis over ~10,000-year timescales — is what allows inclination to serve as a paleolatitude indicator. Without this assumption, inclination would not have a predictable relationship to latitude."
```

## Explainer

From your understanding of Earth's magnetic dipole field, you know that our planet generates a roughly dipolar magnetic field through convection in the liquid outer core. This field has a north and south magnetic pole, and at any point on the surface it has a specific **declination** (the angle from geographic north) and **inclination** (the angle below horizontal, which varies with latitude). Paleomagnetism is the science of reading ancient field directions preserved in rocks — essentially using rocks as fossil compasses.

The recording mechanism depends on the rock type. When an igneous rock cools through its **Curie temperature** (about 580°C for magnetite), the magnetic minerals lock in a magnetization parallel to the ambient field. This **thermoremanent magnetization (TRM)** is strong and stable over billions of years. In sedimentary rocks, tiny magnetic grains physically rotate to align with the field as they settle through water, producing a **detrital remanent magnetization (DRM)** that is weaker but still preserves the field direction at the time of deposition. In both cases, the key insight is the same: the rock becomes a snapshot of the magnetic field at a specific moment in geological time.

The most dramatic feature of the paleomagnetic record is that Earth's field periodically **reverses polarity** — magnetic north and south swap places. During a reversal, the field weakens, becomes complex and multipolar for a few thousand years, then re-establishes with opposite polarity. These reversals are not periodic; they occur irregularly, with intervals between reversals ranging from tens of thousands to tens of millions of years. The record of normal and reversed polarity intervals has been compiled into the **geomagnetic polarity timescale (GPTS)**, calibrated by radiometric dating of volcanic rocks. This timescale is one of the most powerful dating tools in geology: if you measure the polarity sequence in a sedimentary or volcanic section, you can correlate it to the GPTS like matching a barcode — a technique called **magnetostratigraphy**.

Beyond dating, paleomagnetism is the backbone of plate tectonic reconstructions. Because inclination depends on latitude (tan(I) = 2·tan(λ)), measuring the remanent inclination of an ancient rock tells you the latitude at which it formed. If that latitude differs from the rock's present position, the plate has moved. By compiling paleomagnetic directions from rocks of many ages on a single continent, you trace an **apparent polar wander path (APWP)** — a curve showing where the magnetic pole appeared to be over time. The pole did not actually wander that much; the continent moved. When APWPs from two continents diverge back in time and then converge, it reveals when the continents were joined and when they separated, providing quantitative constraints on paleogeography that no other method can match.
