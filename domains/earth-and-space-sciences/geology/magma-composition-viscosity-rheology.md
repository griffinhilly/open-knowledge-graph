---
id: magma-composition-viscosity-rheology
title: Magma Composition and Physical Properties
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: igneous-rock-texture-classification
  type: hard
- id: oxidation-reduction-basics
  type: soft
- id: phase-diagrams-binary-mixtures
  type: soft
- id: viscosity-gas-liquid-transport
  type: soft
- id: thermochemistry-enthalpy
  type: soft
builds-toward:
- fractional-crystallization-magmatic-differentiation
- eruptive-styles-and-lava-rheology
tags:
- magmatism
- viscosity
- composition
stage: formal-systems
status: validated
---

# Magma Composition and Physical Properties

## Core Idea
Magma viscosity is controlled primarily by silica content, temperature, and dissolved volatile concentration. Higher silica content produces more viscous (andesitic to rhyolitic) magmas that generate explosive eruptions, while lower silica (basaltic) magmas are fluid and produce effusive eruptions. This composition-behavior relationship explains observed volcanic phenomena.

## Questions

```yaml
- question: "Two magmas have identical silica content. Magma A contains 5% dissolved water; Magma B is anhydrous (no water). Both remain at depth under high pressure. Which magma is more viscous?"
  type: multiple-choice
  options:
    - "Magma A — dissolved water adds mass to the silicate network, increasing resistance to flow"
    - "Magma B — without water, the silicate network is more completely polymerized and resists flow more strongly"
    - "Both are equally viscous — dissolved water has no effect on silicate melt viscosity"
    - "Magma A — water molecules insert into silicate chains, creating new cross-links that stiffen the melt"
  answer: 1
  explanation: "Dissolved water breaks Si-O-Si bridges by inserting OH groups into the silicate network, disrupting polymerization and dramatically lowering viscosity. Magma B, being anhydrous, has an intact, fully polymerized network — the silicate tetrahedra are maximally cross-linked and the melt is far more viscous. This is counterintuitive but critical: water makes magma *less* viscous at depth. The dangerous consequence comes when pressure drops during ascent and that water exsolves, generating explosive gas pressure."

- question: "A basaltic volcano rarely produces explosive eruptions primarily because:"
  type: multiple-choice
  options:
    - "Basaltic magma contains very few dissolved volatiles, so little gas forms during ascent"
    - "Basaltic magma's low viscosity allows exsolving gas bubbles to migrate freely through the melt and escape at the surface before pressure builds"
    - "Basaltic magma erupts at cooler temperatures than rhyolitic magma, which reduces gas expansion"
    - "Basalt solidifies quickly at the vent, sealing off gas before it can accumulate to explosive pressure"
  answer: 1
  explanation: "The decisive factor is viscosity, not volatile content. Basaltic magmas can contain significant volatiles, but their low viscosity (as low as 10¹ Pa·s, similar to warm honey) allows gas bubbles to rise freely through the melt and degas gradually at the surface — like bubbles in a thin soup. In high-viscosity rhyolitic magma (up to 10⁸ Pa·s), the same gas bubbles cannot migrate; pressure builds within them until the magma fragments catastrophically. It is the viscosity contrast, driven by silica content, that determines eruptive style."

- question: "In rhyolitic magmas, both high silica content and low eruption temperature independently increase viscosity, so the two effects compound each other."
  type: true-false
  answer: true
  explanation: "Silica content drives viscosity up through polymerization: more Si-O-Si linkages create a tangled molecular network. Temperature drives viscosity down by providing thermal energy to break those bonds. Rhyolitic magmas are doubly disadvantaged: they have the highest silica content (~65–75% SiO₂) AND erupt at the lowest temperatures (~700–900°C, versus ~1100–1250°C for basalt). These two factors amplify each other, producing viscosities up to 10⁸ Pa·s — roughly seven orders of magnitude higher than basalt. This compounding effect explains why felsic volcanoes produce the most dangerous eruptions."

- question: "Dissolved water in magma at depth increases viscosity because water molecules bond to and extend the silicate network."
  type: true-false
  answer: false
  explanation: "Dissolved water does the opposite: it decreases viscosity. Water molecules react with bridging oxygen atoms in the silicate network (Si-O-Si + H₂O → 2 Si-OH), breaking the cross-links that cause polymerization and viscosity. The more water dissolved in the melt, the more disrupted the network and the lower the viscosity. This is why volatile-rich rhyolitic magmas at depth are less viscous than their dry counterparts — but the danger emerges during ascent when that water exsolves and forms trapped gas bubbles."

- question: "Explain why the same dissolved water that decreases magma viscosity at depth can contribute to violent explosive eruptions as magma rises toward the surface."
  type: short-answer
  answer: "At depth, high confining pressure keeps water dissolved in the melt, where it disrupts silicate polymerization and reduces viscosity. As magma ascends and pressure drops, water's solubility decreases — it exsolves from solution and forms gas bubbles (vesiculation). In low-viscosity basaltic magma, these bubbles rise freely and degas at the surface. In high-viscosity rhyolitic magma, the thick melt prevents bubbles from migrating; gas pressure builds inside them. When the pressure exceeds the tensile strength of the melt, the magma fragments explosively into ash, pumice, and pyroclastic flows. Water's role therefore flips: a viscosity-reducer at depth becomes a fragmentation driver at shallow levels."
  explanation: "The key concept is that dissolved and exsolved water are fundamentally different in their effects. The phase transition from dissolved to exsolved — driven by pressure decrease during ascent — is the trigger for explosive behavior. High-silica magma's viscosity prevents the pressure release that low-viscosity magma achieves through gentle degassing."
```

## Explainer

From your study of igneous rock classification, you know that igneous rocks are categorized by their mineral and chemical composition — from silica-poor (mafic) basalts to silica-rich (felsic) rhyolites. What determines whether a volcano gently oozes lava flows or violently explodes is not just *what* the magma is made of, but how that composition controls the magma's physical behavior — especially its **viscosity**, the resistance to flow.

**Silica content** is the master variable. Silicon and oxygen atoms form **silicate tetrahedra** (SiO₄ units) that link together into chains, sheets, and three-dimensional networks through shared oxygen atoms — a process called **polymerization**. In silica-rich magmas (65–75% SiO₂, like rhyolite), extensive polymerization creates a tangled molecular structure that resists flow, producing viscosities up to 10⁸ Pa·s — roughly the consistency of cold tar. In silica-poor magmas (45–52% SiO₂, like basalt), fewer linkages leave the melt more fluid, with viscosities as low as 10¹ Pa·s — comparable to warm honey. This difference of seven orders of magnitude in viscosity is the single most important factor separating gentle Hawaiian-style eruptions from catastrophic explosive eruptions like Mount St. Helens.

**Temperature** works against polymerization. Higher temperatures provide thermal energy that breaks silicate bonds and allows atoms to move past each other more freely, reducing viscosity. Basaltic magmas erupt at roughly 1100–1250°C, while rhyolitic magmas erupt at 700–900°C. The lower eruption temperature of felsic magmas compounds their already high viscosity from polymerization — they are both more polymerized *and* cooler, making them far more resistant to flow. This is why mafic magmas typically form long, thin lava flows that travel kilometers from the vent, while felsic magmas pile up in steep-sided domes or fragment explosively.

**Dissolved volatiles** — primarily water (H₂O) and carbon dioxide (CO₂) — have a dual role. While dissolved in the melt at depth, water actually *decreases* viscosity by breaking Si-O-Si bridges in the silicate network, inserting OH groups that disrupt polymerization. A rhyolite with 5% dissolved water is dramatically less viscous than the same composition when dry. But as magma rises toward the surface and pressure drops, these volatiles come out of solution and form gas bubbles — a process called **exsolution** or **vesiculation**. In low-viscosity basaltic magma, gas bubbles rise freely through the melt and escape at the surface (think of bubbles rising in a pot of water). In high-viscosity rhyolitic magma, gas cannot escape; pressure builds within the bubbles until the magma fragments explosively into ash, pumice, and pyroclastic flows. This is why the most dangerous volcanic eruptions are associated with silica-rich, volatile-rich magmas — the combination of high viscosity and trapped gas creates the conditions for violent fragmentation.
