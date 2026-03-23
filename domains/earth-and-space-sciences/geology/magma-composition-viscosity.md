---
id: magma-composition-viscosity
title: Magma Composition, Viscosity, and Eruption Style
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: bowen-fractional-crystallization
  type: hard
- id: eruptive-styles-and-lava-rheology
  type: soft
builds-toward:
- volcanic-hazards-assessment
tags:
- magma
- viscosity
- composition
- silica
stage: formal-systems
status: validated
---

# Magma Composition, Viscosity, and Eruption Style

## Core Idea
Magma viscosity increases dramatically with silica content (basalt < andesite < rhyolite) and decreases with temperature. Higher viscosity magmas trap gases, promoting explosive eruptions; low-viscosity basalts erupt effusively. This composition-viscosity-eruption-style relationship predicts volcanic hazards from magma type.

## How It's Best Learned
Use viscosity models to predict how silica content and temperature affect eruption behavior. Compare actual eruptions to predicted styles.

## Questions

```yaml
- question: "Geologists examining a volcano discover the underlying magma chamber contains dacitic magma (approximately 65% SiO₂). Based on the composition-viscosity-eruption framework, what eruption style should hazard planners anticipate?"
  type: multiple-choice
  options:
    - "Effusive — dacite has intermediate silica content, placing it between explosive and effusive styles with predictably gentle outflows"
    - "Effusive — eruption style is primarily controlled by temperature, and dacitic magma is typically cooler than basalt"
    - "Explosive — the elevated silica content creates a viscous melt that prevents dissolved gases from escaping, allowing pressure to build until the system fragments"
    - "Explosive — dacite is too dense to flow, so it always erupts as solid pyroclastic material"
  answer: 2
  explanation: "Dacite (65% SiO₂) is viscous enough that dissolved volatiles cannot bubble out freely as the magma rises and decompresses. Trapped gas pressure builds until the melt fragments explosively — this is exactly the scenario that made the 1991 Mount Pinatubo eruption predictable from its dacitic composition. Option A represents the misconception that 'intermediate' composition means 'intermediate' eruption style — in practice, there is a strong threshold effect. Temperature (option B) matters for viscosity but does not override the dominant effect of silica content in controlling eruption style."

- question: "Why does high-silica rhyolitic magma typically produce explosive eruptions while low-silica basaltic magma produces effusive lava flows, even when both contain similar amounts of dissolved water?"
  type: multiple-choice
  options:
    - "Rhyolitic magma contains chemically different volatiles that react more energetically with the atmosphere on eruption"
    - "High viscosity in rhyolitic magma traps gas bubbles that cannot rise and escape, so pressure builds in the melt until it fragments catastrophically"
    - "Basaltic magma erupts at much higher temperatures, causing rapid boiling of water that vents harmlessly"
    - "The silica tetrahedra in rhyolite react chemically with CO₂, generating additional gas pressure beyond what the original dissolved volatiles would produce"
  answer: 1
  explanation: "The key mechanism is not the amount of gas but whether the gas can escape. In low-viscosity basaltic magma, volatiles exsolve as bubbles that migrate freely upward through the fluid melt and degas at the surface — like bubbles in simmering water. In high-viscosity rhyolitic magma, the same bubbles cannot migrate; they are trapped in the sticky melt. As magma continues to rise and decompressurize, more gas exsolves into the trapped bubbles, pressure increases, and eventually the melt fragments explosively. The viscosity is the controlling variable, not the absolute gas content."

- question: "Dissolved water in magma increases viscosity by reinforcing the silicon-oxygen tetrahedral network structure."
  type: true-false
  answer: false
  explanation: "Dissolved water actually lowers viscosity by disrupting silica network structures. Water molecules (and OH⁻ groups) break Si-O-Si bonds, reducing the degree of polymerization and allowing the melt to flow more easily. This is why water-rich magmas can be more mobile than their silica content alone would predict. The viscosity-increasing factors are high silica content (more extensive Si-O networks) and low temperature (less thermal energy to break bonds). Water acts in opposition to silica's viscosity-increasing effect."

- question: "A basaltic lava flow and a rhyolitic eruption can both be driven by the same dissolved volatile content (same weight percent of H₂O and CO₂), yet produce dramatically different eruption styles."
  type: true-false
  answer: true
  explanation: "Eruption style is controlled by whether volatiles can escape, not by how much volatile is present. In basaltic magma (low silica, low viscosity), gas bubbles form and rise freely, producing gentle degassing and effusive eruption. In rhyolitic magma (high silica, high viscosity), the same bubbles are trapped, pressure builds, and the result is explosive fragmentation. Two magmas with identical volatile budgets can thus produce a Hawaiian lava fountain versus a Plinian eruption column, depending entirely on composition-controlled viscosity."

- question: "Explain the chain of causation from silica content to eruption style. Why might the same volcanic system produce both effusive and explosive eruptions at different points in time?"
  type: short-answer
  answer: "Higher silica content extends silicon-oxygen tetrahedral networks in the melt, increasing viscosity. High viscosity prevents dissolved gas bubbles (primarily H₂O and CO₂) from migrating upward and escaping as magma rises and decompresses. Trapped bubbles grow as pressure drops; if pressure buildup exceeds the tensile strength of the melt, the system fragments explosively. A single volcanic system can evolve: fractional crystallization concentrates silica in the remaining melt over time, gradually increasing viscosity. Eruption rate also matters — faster ascent gives less time for degassing even in moderately fluid magmas. So the same volcano may erupt effusively early in a magmatic episode (when melt is basaltic or andesitic) and explosively later (when evolved, silica-rich magma reaches the surface)."
  explanation: "This causal chain — composition → viscosity → gas escape (or trapping) → eruption style — is the organizing framework for volcanic hazard assessment. The 1991 Pinatubo case is instructive: the dacitic composition was identified weeks before the eruption, allowing successful evacuation. Understanding this chain is what made the prediction possible."
```

## Explainer

From your understanding of Bowen's reaction series and fractional crystallization, you know that magmas evolve in composition as minerals crystallize and separate from the melt. A basaltic magma that starts with roughly 50% silica can evolve through andesite (60%) to rhyolite (70%+) as crystallization removes iron- and magnesium-rich minerals, concentrating silica in the remaining liquid. This compositional evolution has profound consequences for how magma behaves — and whether a volcano oozes lava gently or explodes catastrophically.

The critical physical property linking composition to eruption style is **viscosity** — a fluid's resistance to flow. Silica molecules in magma form interconnected networks of silicon-oxygen tetrahedra that act like molecular chains, tangling together and resisting movement. The more silica in the melt, the more extensive these networks become, and the more viscous the magma. Basaltic magma (low silica) flows almost like heavy motor oil — you can watch it pour down a Hawaiian hillside in glowing rivers. Rhyolitic magma (high silica) is so viscous it barely flows at all, behaving more like cold tar or even glass. Temperature matters too: hotter magma has more thermal energy to break silicon-oxygen bonds, reducing viscosity. Dissolved water also lowers viscosity by disrupting silica networks. So the full picture involves composition, temperature, and volatile content working together.

The connection to eruption style follows directly from gas behavior in fluids of different viscosity. All magmas contain **dissolved volatiles** — primarily water and CO₂ — that come out of solution as magma rises and pressure drops, forming gas bubbles. In low-viscosity basaltic magma, these bubbles rise freely through the fluid and escape at the surface, like bubbles in a pot of simmering water. The result is **effusive eruption**: lava flows, lava fountains, and gentle degassing. In high-viscosity rhyolitic magma, gas bubbles cannot escape — they are trapped in the sticky melt like air bubbles in thick honey. As the magma continues to rise and decompress, more gas exsolves, pressure builds inside the trapped bubbles, and eventually the entire mass fragments explosively. This produces **explosive eruptions**: pyroclastic flows, ash columns reaching the stratosphere, and devastating lateral blasts.

This composition-viscosity-eruption framework is the basis of **volcanic hazard assessment**. When geologists analyze the composition of volcanic deposits — the silica content of pumice, the crystal assemblage, the volatile content preserved in melt inclusions — they can reconstruct past eruption styles and predict future behavior. A volcano that has historically erupted low-silica basalt is unlikely to produce a Plinian eruption column, while a volcano sitting on evolved rhyolitic magma demands serious hazard planning. The 1991 eruption of Mount Pinatubo, for example, was predicted to be explosive precisely because the erupted magma was dacitic (65% silica) — viscous enough to produce the massive ash column and pyroclastic flows that followed.
