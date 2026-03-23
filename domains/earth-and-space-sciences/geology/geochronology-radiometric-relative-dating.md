---
id: geochronology-radiometric-relative-dating
title: 'Geochronology: Radiometric and Relative Dating Methods'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: radiometric-dating
  type: hard
- id: radiometric-dating-isotope-systems-geochronology
  type: soft
- id: nuclear-chemistry
  type: hard
builds-toward:
- stratigraphy-law-superposition-correlation
- geological-time-scale
tags:
- geochronology
- dating
- time-scale
stage: formal-systems
status: draft
---

# Geochronology: Radiometric and Relative Dating Methods

## Core Idea
Absolute (radiometric) dating measures radioactive isotope decay in rocks to assign precise ages; common systems include K-Ar, Rb-Sr, and U-Pb. Relative dating uses fossil assemblages and cross-cutting relationships to order events. Combined, these methods construct the geological time scale and date major Earth events.

## Questions

```yaml
- question: "A geologist finds a sedimentary sequence cut by an igneous dike. She radiometrically dates the dike at 250 million years old. What can she conclude about the age of the sedimentary rocks?"
  type: multiple-choice
  options:
    - "The sedimentary rocks are exactly 250 million years old, since they were heated by the intrusion"
    - "The sedimentary rocks are older than 250 million years, since the dike must post-date the rocks it intrudes"
    - "The sedimentary rocks are younger than 250 million years, since the dike brought material upward from below"
    - "The sedimentary rocks cannot be dated without direct radiometric samples from the sediment itself"
  answer: 1
  explanation: "The Principle of Cross-Cutting Relationships: a geological feature must be younger than whatever it cuts through. The dike intruded into pre-existing sedimentary rock, so the sedimentary rocks formed first — they are older than 250 Ma. This is bracketing: the dike's radiometric date gives a minimum age for the sedimentary sequence. To get a maximum age, the geologist would look for an overlying feature (another dated layer or intrusion) that post-dates the sediment."

- question: "Why is the U-Pb system in zircon the preferred method for dating the oldest rocks on Earth, rather than K-Ar?"
  type: multiple-choice
  options:
    - "Uranium is far more abundant than potassium in ancient crustal rocks"
    - "Zircon excludes lead when it crystallizes (so all daughter Pb comes from decay), and uranium's ~4.5 Ga half-life is matched to billion-year timescales"
    - "The K-Ar system gives systematically inaccurate ages for rocks older than 1 billion years due to argon production rates changing"
    - "Zircon always contains equal amounts of uranium and lead at the time of crystallization, providing a precise starting ratio"
  answer: 1
  explanation: "Two properties make U-Pb in zircon ideal for ancient rocks: (1) Zircon is chemically resistant and excludes lead from its crystal structure when it forms — so the entire daughter-lead inventory comes from uranium decay, not contamination, giving a well-defined initial condition. (2) U-238 has a half-life of ~4.5 billion years, comparable to Earth's age, so the decay product has accumulated to measurable levels without the parent being exhausted. K-Ar can technically date old rocks, but argon can leak from some minerals at elevated temperatures, resetting the clock."

- question: "The geological time scale (eras, periods, epochs) was originally constructed using radiometric dating before relative dating methods were developed."
  type: true-false
  answer: false
  explanation: "The reverse is true. Geologists assembled the geological time scale from fossil succession, superposition, and cross-cutting relationships — all relative dating methods — long before radioactive decay was even discovered. By the early 19th century, the broad framework of geological periods existed based purely on fossil evidence. Radiometric dating, developed in the 20th century, then calibrated this existing relative framework with absolute numbers (e.g., confirming the Cambrian began ~539 Ma). Relative dating was historically first and remains indispensable for field geology."

- question: "An index fossil with a short stratigraphic range (it existed for only a brief time) is more useful for relative dating than a fossil that persisted for hundreds of millions of years, even if the latter is far more common in the rock record."
  type: true-false
  answer: true
  explanation: "An index fossil functions as a geological 'timestamp.' Its usefulness scales with precision: a short-lived fossil places rocks within a narrow time interval (e.g., a specific zone of a few million years), while a long-ranging fossil tells you only that the rock formed sometime during its entire duration — potentially hundreds of millions of years of uncertainty. Wide geographic distribution is also valued (for correlation across continents), but narrow time range is the primary criterion for precision. Rarity can be a practical obstacle but does not affect the theoretical precision."

- question: "Why do geologists combine radiometric and relative dating rather than relying exclusively on radiometric dating, given that radiometric methods produce precise numerical ages?"
  type: short-answer
  answer: "Radiometric dating applies best to igneous and metamorphic rocks that contain datable minerals — not to the sedimentary rocks and fossil assemblages that record most of Earth's biological and environmental history. You cannot directly radiometrically date a fossil or a sandstone layer. Relative dating fills this gap: superposition, fossil succession, and cross-cutting relationships establish the sequence of events from field observations, without laboratory measurements. Combining both allows bracketing — for example, a sedimentary sequence between two dated igneous layers must have formed between their ages. Each method has a different domain of applicability, and together they cover the full range of geological materials and timescales."
  explanation: "The geological time scale is the product of this combination: relative methods built the framework, radiometric methods anchored it numerically. Neither alone would have produced a complete, quantitative history of Earth."
```

## Explainer

From your study of nuclear chemistry and radiometric dating, you know that certain isotopes are unstable and decay at constant, measurable rates described by their half-lives. Geochronology harnesses this principle to answer one of geology's most fundamental questions: how old is this rock? The power of the approach lies in combining **absolute dating** (which gives numerical ages in years) with **relative dating** (which establishes the order of events without assigning numbers), building a complete timeline of Earth history.

**Radiometric dating** works because when a mineral crystallizes from magma, it locks in a known ratio of parent to daughter isotopes. From that moment, the parent isotope decays at a rate set by its half-life, and the daughter isotope accumulates. By measuring the current parent-to-daughter ratio and knowing the decay constant, geologists calculate how much time has passed since crystallization. Different isotope systems are suited to different timescales and rock types. The **U-Pb system** in zircon is the gold standard for ancient rocks because zircon is chemically resistant, incorporates uranium but excludes lead when it crystallizes, and uranium's long half-life (4.5 billion years for U-238) makes it effective for dating rocks from the earliest Earth. The **K-Ar system** is widely used for volcanic rocks from a few thousand to billions of years old, exploiting the decay of potassium-40 to argon-40. The **Rb-Sr system** works well for granites and metamorphic rocks by measuring rubidium-87 decay to strontium-87 across multiple minerals to construct an isochron.

**Relative dating** does not require any laboratory measurements. It relies on a set of logical principles that geologists apply in the field. The **Law of Superposition** states that in an undisturbed sequence, older layers lie below younger ones. The **Principle of Cross-Cutting Relationships** says that a geological feature (a fault, an intrusion) must be younger than the rock it cuts through. **Fossil succession** — the observation that fossil assemblages change in a consistent, recognizable order through the rock record — allows geologists to correlate rocks across continents even when they cannot be physically traced. An index fossil with a short time range and wide geographic distribution acts like a timestamp, placing rocks within a specific interval without needing a radiometric age.

The geological time scale was originally built entirely from relative dating: geologists assembled the sequence of fossil assemblages into eras, periods, and epochs long before anyone could assign numerical ages. Radiometric dating later calibrated this relative framework with absolute numbers, revealing, for example, that the Cambrian Period began around 539 million years ago and that Earth itself is approximately 4.54 billion years old. Today, geochronology integrates both approaches. A geologist might use cross-cutting relationships to establish that an igneous dike is younger than the sedimentary rocks it intrudes, then date the dike radiometrically to bracket the age of the sedimentary sequence. This combination of logical ordering and precise measurement is what makes it possible to construct a unified timeline spanning from Earth's formation to the present.
