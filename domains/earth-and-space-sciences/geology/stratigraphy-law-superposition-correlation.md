---
id: stratigraphy-law-superposition-correlation
title: 'Stratigraphy: Superposition, Cross-Cutting, and Lateral Correlation'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: geochronology-radiometric-relative-dating
  type: hard
- id: sedimentary-depositional-environments
  type: soft
builds-toward:
- paleontology-trace-fossils-interpretation
- ocean-sediments-and-stratigraphy
tags:
- stratigraphy
- sedimentology
- correlation
stage: advanced
status: draft
---

# Stratigraphy: Superposition, Cross-Cutting, and Lateral Correlation

## Core Idea
Stratigraphy applies principles of superposition (younger layers overlie older), cross-cutting relationships, and lateral continuity to interpret sedimentary sequences. Stratigraphic correlation across regions using distinctive marker beds, fossils, and magnetic signatures reveals synchronous events and basin-scale depositional patterns.

## Questions

```yaml
- question: "An outcrop shows: (1) folded shale layers, (2) a granite mass that cuts across the shale folds, and (3) horizontal sandstone sitting above both with an erosional contact. What is the correct sequence of events?"
  type: multiple-choice
  options:
    - "Granite formed first (igneous rocks predate sedimentary ones), then shale was deposited around it, then folding, then sandstone"
    - "Shale deposited → shale folded → granite intruded → erosion → sandstone deposited unconformably on top"
    - "Shale and granite formed simultaneously as the basement, then were folded together, then sandstone was deposited"
    - "Sandstone is oldest (deepest protolith), then granite intruded, then shale was deposited, then folding"
  answer: 1
  explanation: "Three principles work together here. Superposition: shale layers were deposited sequentially before folding. Cross-cutting: the granite cuts across already-folded shale, so it is younger than the folded shale. The erosional contact (angular unconformity) between folded rocks and horizontal sandstone means erosion followed granite intrusion, and sandstone was deposited last. Option A is a common misconception — rock type (igneous vs. sedimentary) does not determine age order; relative principles do."

- question: "Two outcrops 400 km apart each contain a thin, distinctive volcanic ash layer with an identical geochemical fingerprint. What does this marker bed allow geologists to infer about the strata immediately above the ash in both sections?"
  type: multiple-choice
  options:
    - "They formed in identical depositional environments because the same ash was deposited in both places"
    - "They are isochronous — the same age — because the ash was deposited in a geologically instantaneous single eruption event"
    - "They are lithostratigraphically equivalent but cannot be correlated temporally without radiometric dates"
    - "They represent the same rock type and must therefore share the same mineral composition"
  answer: 1
  explanation: "A single volcanic eruption deposits ash globally within days to weeks — geologically instantaneous. This makes the ash a perfect time-stratigraphic marker: strata immediately above the ash in both sections post-date the same event and are the same age. This is isochronous correlation, far more powerful than lithological similarity alone (two limestones that look alike could have formed millions of years apart). Ash beds, along with index fossils and magnetic reversals, are the primary tools for correlating strata across great distances."

- question: "According to the law of superposition, the deepest rock layer exposed in any outcrop is always the oldest."
  type: true-false
  answer: false
  explanation: "False. The law of superposition applies only to undisturbed sequences. Tectonic deformation — folding, thrust faulting, or overturning — can invert entire sequences, placing younger rocks structurally below older ones. Identifying whether strata are right-side-up or overturned (using facing indicators like graded bedding, ripple marks, and fossil orientations) is a critical step before applying superposition. In tectonically active regions, assuming depth = age without checking for structural complications is a common and consequential error."

- question: "The principle of cross-cutting relationships applies only to igneous intrusions — dikes, sills, and batholiths — that physically cut across existing rock layers."
  type: true-false
  answer: false
  explanation: "False. Cross-cutting applies to any geological feature that truncates or disrupts existing strata: faults, joints, unconformities (erosional surfaces), and igneous intrusions of all kinds. A fault that offsets layers must be younger than the youngest layer it cuts. An erosional unconformity that truncates tilted beds must post-date those beds. The principle is about any geometrical cutting relationship, not a specific rock type. Faults and unconformities are often more useful cross-cutting relationships than intrusions because they are more common."

- question: "Why are index fossils more useful for stratigraphic correlation than fossils of long-lived species?"
  type: short-answer
  answer: "Index fossils are organisms that lived for a geologically brief time span but were geographically widespread. Their short temporal range constrains the age of the enclosing rock to a narrow time window — sometimes less than a million years. A long-lived species (persisting for tens of millions of years) provides only broad, imprecise age constraints, making correlation ambiguous. The brevity of the species' existence is precisely what makes it a sharp chronological marker. When the same index fossil appears in two sections on different continents, those sections must be approximately contemporaneous."
  explanation: "This is biostratigraphy's core principle. The best index fossils combine three traits: short temporal range (precise age constraint), wide geographic distribution (useful for distant correlation), and abundance (easy to find). Ammonites and trilobites are classic examples for Paleozoic and Mesozoic strata. The logic parallels using a precisely dated event — if you find the same ash from a dated eruption in two places, both sections must contain strata of that exact age. Index fossils work the same way but are more widely distributed than individual ash layers."
```

## Explainer

From your study of radiometric and relative dating, you know how to assign ages to rocks — both absolute ages from radioactive decay and relative ages from the order of geological events. **Stratigraphy** is the science of reading layered rock sequences, and it rests on a handful of principles so intuitive they seem obvious, yet they are powerful enough to reconstruct Earth history across continents.

The **law of superposition** states that in an undisturbed sequence of sedimentary layers, each bed is younger than the one below it and older than the one above it. This is simply gravity at work: sediment settles on top of what is already there. The **principle of original horizontality** adds that sediments are deposited in roughly horizontal layers; if you find tilted or folded strata, something happened after deposition to deform them. The **principle of cross-cutting relationships** says that any geological feature — a fault, an igneous intrusion, an erosional surface — that cuts across existing layers must be younger than those layers. Together, these three principles let you reconstruct the chronological sequence of events at any single outcrop: first these layers were deposited, then they were tilted, then a dike intruded through them, then erosion truncated everything, then a new horizontal layer was deposited on top.

The real power of stratigraphy emerges when you move beyond a single outcrop to **correlation** — matching rock layers across different locations to build a regional or even global picture. The principle of **lateral continuity** says that a sedimentary layer extends laterally in all directions until it thins to zero or terminates against a basin edge. So if you find limestone with the same distinctive fossils and mineral composition at two sites 100 km apart, you can reasonably infer they represent the same depositional event. **Marker beds** — thin, distinctive layers with unique characteristics, such as volcanic ash falls or chemically unusual limestone beds — are especially useful because they were deposited essentially instantaneously over wide areas. Fossil content provides another correlation tool: if two layers contain the same index fossil species (organisms that existed for a geologically brief time but were geographically widespread), those layers must be approximately the same age.

**Magnetostratigraphy** adds yet another correlation method. Earth's magnetic field has reversed polarity hundreds of times, and these reversals are recorded in iron-bearing minerals within sediments as they are deposited. The pattern of normal and reversed polarity intervals creates a barcode-like signature that can be matched between distant sections and tied to the global magnetic polarity timescale. By combining lithostratigraphy (rock type), biostratigraphy (fossils), magnetostratigraphy (magnetic reversals), and chemostratigraphy (chemical signatures like carbon isotope excursions), geologists can correlate rock sequences across basins, continents, and even oceans — reconstructing how environments changed synchronously around the world during events like mass extinctions, sea-level changes, or major volcanic episodes.
