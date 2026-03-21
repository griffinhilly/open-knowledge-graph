---
id: igneous-rocks
title: Igneous Rocks
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: rock-forming-minerals
  type: hard
- id: phase-diagrams
  type: soft
- id: phase-diagrams-binary-mixtures
  type: soft
builds-toward:
- rock-cycle
- volcanoes-and-volcanism
- metamorphic-rocks
tags:
- igneous
- magma
- lava
- intrusive
- extrusive
- granite
- basalt
stage: advanced
status: validated
---

# Igneous Rocks

## Core Idea
Igneous rocks form from the cooling and crystallization of magma (molten rock underground) or lava (molten rock at the surface). Intrusive (plutonic) igneous rocks cool slowly deep in the crust, producing coarse-grained textures like granite; extrusive (volcanic) rocks cool rapidly at the surface, producing fine-grained or glassy textures like basalt or obsidian. Composition ranges from felsic (silica-rich, low density) to mafic (silica-poor, iron- and magnesium-rich, high density) and determines both mineralogy and physical properties. Bowen's Reaction Series describes the sequence in which minerals crystallize as a melt cools, explaining why different igneous rock types coexist.

## How It's Best Learned
Thin-section microscopy or hand-sample comparison of granite (coarse, felsic) versus basalt (fine, mafic) versus rhyolite (fine, felsic) makes texture-composition relationships tangible. Tracing Bowen's Reaction Series from olivine and pyroxene at high temperature to quartz and muscovite at low temperature connects thermodynamics to petrology.

## Common Misconceptions
- Obsidian is not a mineral; it is volcanic glass with no crystalline structure.
- Grain size reflects cooling rate, not composition: a granite and a rhyolite can have identical chemistry but vastly different textures.
- All magmas are not the same; basaltic and granitic magmas have very different viscosities, temperatures, and eruption styles.

## Questions

```yaml
- question: "A geologist finds two rocks: one is coarse-grained with visible quartz and feldspar crystals; the other is dark and very fine-grained with no visible crystals. What is the MOST reliable conclusion she can draw from texture alone?"
  type: multiple-choice
  options:
    - "They have different chemical compositions because they look different"
    - "The coarse-grained rock must have cooled faster, since larger grains require more rapid crystallization"
    - "They have different cooling histories — the coarse-grained rock cooled slowly (intrusive), the fine-grained one cooled rapidly (extrusive)"
    - "The dark rock is necessarily mafic because dark-colored rocks are always mafic"
  answer: 2
  explanation: "Grain size is controlled by cooling rate, not composition. A coarse-grained (phaneritic) texture indicates slow cooling underground; a fine-grained (aphanitic) texture indicates rapid surface cooling. Texture alone cannot tell you composition — a rhyolite and a granite can have identical chemistry but completely different textures. Option D is also wrong: color correlates with composition but is not diagnostic — rhyolite is felsic and can be light-colored, yet fine-grained."

- question: "A rock sample shows large, well-formed crystals (phenocrysts) embedded in a fine-grained groundmass. What cooling history does this porphyritic texture record?"
  type: multiple-choice
  options:
    - "Single-stage rapid cooling at the surface, with some crystals growing faster than others"
    - "Two-stage cooling: slow crystallization at depth (producing phenocrysts), followed by rapid cooling upon eruption (producing the fine groundmass)"
    - "Metamorphic recrystallization under high pressure that enlarged some original crystals"
    - "Chemical weathering that preferentially dissolved smaller crystals, leaving only large ones"
  answer: 1
  explanation: "Porphyritic texture is a textbook two-stage cooling story. Large crystals (phenocrysts) require time to grow — they formed during slow cooling at depth. When the magma was erupted, the remaining liquid cooled rapidly, forming the fine-grained groundmass. The single rock contains a record of both environments. This is why porphyritic rocks are particularly informative about magma history."

- question: "Obsidian is a fine-grained igneous rock because its crystals are present but too small to see without a microscope."
  type: true-false
  answer: false
  explanation: "Obsidian has no crystals at all — it is volcanic glass. Cooling was so rapid that atoms could not organize into crystalline lattices; the result is an amorphous solid. Fine-grained (aphanitic) rocks like basalt do have crystals, just too small to see without magnification. Obsidian represents the extreme end of fast cooling where crystallization is essentially bypassed entirely."

- question: "A granite and a rhyolite can have nearly identical chemical compositions despite looking completely different."
  type: true-false
  answer: true
  explanation: "This is the core insight of igneous petrology: texture and composition are independent variables. Granite (intrusive, coarse-grained) and rhyolite (extrusive, fine-grained) are the compositional equivalents in the felsic family — both silica-rich with similar mineral assemblages. Their dramatic textural difference reflects only cooling rate. Recognizing compositional equivalents (granite/rhyolite, gabbro/basalt) is fundamental to reading igneous rock classification."

- question: "Explain how Bowen's Reaction Series predicts that a single magma body can produce igneous rocks of different compositions."
  type: short-answer
  answer: "Bowen's Reaction Series describes the order in which minerals crystallize as a melt cools: high-temperature minerals like olivine and pyroxene crystallize first, removing iron and magnesium from the remaining liquid. If these early-forming crystals are physically separated from the melt (by sinking, for example) — a process called fractional crystallization — the remaining melt becomes progressively enriched in silica and depleted in iron and magnesium. Continued fractional crystallization can thus evolve a mafic starting magma toward increasingly felsic compositions."
  explanation: "This question tests whether students understand Bowen's Series as a dynamic process, not just a static list. The key is the separation step: if early crystals remain in equilibrium with the melt, the bulk composition doesn't change. Fractional crystallization is what allows compositional evolution, and it explains why a mantle-derived mafic magma can ultimately produce felsic rocks characteristic of continental crust."
```

## Explainer

From your study of rock-forming minerals and phase diagrams, you know that minerals have specific chemical compositions and that melts crystallize different minerals at different temperatures. Igneous rocks are the direct products of this crystallization process — they form when molten rock cools and solidifies. The two fundamental variables that control what an igneous rock looks like are **where it cools** (which determines texture) and **what it's made of** (which determines composition and mineralogy).

**Texture** is controlled almost entirely by cooling rate. When magma is trapped deep underground in large chambers, it loses heat slowly — over thousands to millions of years — giving atoms ample time to migrate through the melt and attach to growing crystal faces. The result is a **coarse-grained (phaneritic)** rock like granite, where individual mineral crystals are easily visible to the naked eye. When lava erupts at the surface and is exposed to air or water, it cools in days to weeks, and crystals have almost no time to grow. This produces **fine-grained (aphanitic)** rocks like basalt, where crystals are too small to see without a microscope. In extreme cases — obsidian, for instance — cooling is so rapid that no crystals form at all, and the result is volcanic glass. Sometimes magma begins cooling slowly at depth (growing large crystals) before being erupted rapidly, producing a **porphyritic** texture: large crystals (phenocrysts) embedded in a fine-grained groundmass, recording the two-stage cooling history in a single rock.

**Composition** ranges along a spectrum from **felsic** to **mafic** (and further to **ultramafic**). Felsic rocks like granite and rhyolite are rich in silica (65–75% SiO₂), aluminum, sodium, and potassium; their dominant minerals are quartz, potassium feldspar, and plagioclase, giving them light colors and relatively low densities. Mafic rocks like basalt and gabbro are lower in silica (45–55% SiO₂) but rich in iron and magnesium; their dominant minerals are pyroxene, olivine, and calcium-rich plagioclase, making them dark and dense. This compositional spectrum is not arbitrary — it is governed by **Bowen's Reaction Series**, which describes the order in which minerals crystallize from a cooling melt. High-temperature minerals like olivine and pyroxene crystallize first, removing iron and magnesium from the remaining liquid and enriching it in silica. If these early crystals are separated from the melt (by sinking, for example), the remaining magma evolves toward a more felsic composition — a process called **fractional crystallization**. This is why a single magma source can produce rocks of different compositions.

Recognizing igneous rocks in the field means reading both texture and composition simultaneously. A coarse-grained, light-colored rock rich in quartz and feldspar is granite (intrusive, felsic). A fine-grained, dark rock dominated by pyroxene and plagioclase is basalt (extrusive, mafic). A coarse-grained, dark rock with the same minerals as basalt is gabbro — same composition, different cooling history. This texture-composition grid is the classification system for all igneous rocks, and it connects directly to the tectonic settings where they form: basalt dominates at mid-ocean ridges and hotspots where mantle melting produces mafic magma, while granite is characteristic of continental crust where fractional crystallization and crustal melting generate felsic compositions.
