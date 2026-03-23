---
id: nitrogen-fixation-limitation-cycling
title: Nitrogen Fixation, Availability, and Cycling
domain: biology
course: ecology-and-evolution
prerequisites:
- id: biogeochemical-cycles
  type: hard
- id: ecosystem-structure-and-function
  type: soft
builds-toward:
- ecosystem-productivity-gpp-npp
- nutrient-cycling
tags:
- nitrogen
- fixation
- cycling
- limitation
stage: formal-systems
status: draft
---

# Nitrogen Fixation, Availability, and Cycling

## Core Idea
Nitrogen cycling involves fixation by bacteria, nitrification, uptake by plants, and mineralization. Nitrogen is often the limiting nutrient in terrestrial ecosystems because atmospheric N₂ is unavailable without fixation. Legume-Rhizobium symbiosis fixes atmospheric nitrogen; excess nitrogen from fertilizers causes eutrophication in aquatic systems.

## Questions

```yaml
- question: "An ecologist adds nitrogen fertilizer to an old-growth forest and observes a dramatic increase in plant biomass. A colleague claims this proves the forest was nitrogen-limited. A skeptic argues that nitrogen can't be limiting because the atmosphere is 78% N₂. Who is right, and why?"
  type: multiple-choice
  options:
    - "The skeptic — if N₂ is abundant, nitrogen cannot be the limiting nutrient regardless of the experimental response"
    - "The ecologist — the fertilizer experiment confirms nitrogen limitation, and the atmospheric N₂ is irrelevant because plants cannot access it directly"
    - "Neither — the response to fertilizer proves phosphorus, not nitrogen, was limiting"
    - "Both are partially right — plants use some N₂ through foliar absorption, making the limitation moderate rather than severe"
  answer: 1
  explanation: "The key insight is that abundance of N₂ is irrelevant to plant nutrition because the N≡N triple bond is too strong for most organisms to break. Plants use reactive nitrogen forms (NH₄⁺, NO₃⁻), not N₂. The atmosphere's 78% N₂ is biologically inaccessible without nitrogen fixation by specialized prokaryotes. This makes N₂ a kind of 'locked vault' of nitrogen — vast but unusable. The fertilizer experiment correctly identifies nitrogen limitation: adding bioavailable nitrogen relieves the bottleneck. The skeptic's reasoning fails by confusing elemental abundance with biological availability."

- question: "Why is nitrogen often the limiting nutrient in terrestrial ecosystems, despite the atmosphere being nearly 80% nitrogen gas?"
  type: multiple-choice
  options:
    - "Because nitrogen gas is heavier than air and sinks away from plant roots underground"
    - "Because plants preferentially use phosphorus and only require nitrogen as a trace element"
    - "Because the triple bond in N₂ makes it chemically inert to most organisms, and conversion to reactive forms requires specialized prokaryotes with nitrogenase"
    - "Because nitrification converts all reactive nitrogen back to N₂ gas within days, preventing accumulation"
  answer: 2
  explanation: "The paradox of nitrogen limitation despite atmospheric abundance is entirely explained by the chemistry of the N≡N triple bond, one of the strongest bonds in biochemistry. Breaking it requires the enzyme nitrogenase, found only in certain prokaryotes (Rhizobium, Azotobacter, cyanobacteria), and consumes 16 ATP per N₂ fixed. Most organisms — including all plants — lack this capability entirely. So the effective nitrogen available to ecosystems is limited by the rate at which these microbial fixers can convert atmospheric N₂, not by how much N₂ exists. This is why Haber-Bosch (industrial nitrogen fixation) so dramatically increased agricultural productivity."

- question: "Plants can absorb nitrogen directly from the atmosphere through their leaves, which is why atmospheric N₂ abundance does not lead to nitrogen limitation in most ecosystems."
  type: true-false
  answer: false
  explanation: "Plants cannot fix atmospheric N₂ — they lack nitrogenase entirely. Nitrogen gas passes through stomata but is not metabolized. Plants absorb nitrogen exclusively in reactive forms: ammonium (NH₄⁺) and nitrate (NO₃⁻) from soil water, or amino acids in some cases. The only pathway from atmospheric N₂ to plant-available nitrogen runs through biological nitrogen fixation by prokaryotes (or industrial fixation, or lightning). This is precisely why legume-Rhizobium symbiosis is so ecologically valuable — the plant houses fixers in root nodules and gains access to a nitrogen supply that most other plants lack."

- question: "Nitrogen fertilizer runoff can cause eutrophication in aquatic systems even though nitrogen is commonly a limiting nutrient in the terrestrial ecosystems where the fertilizer was applied."
  type: true-false
  answer: true
  explanation: "This is not a contradiction — limiting nutrient identity differs between ecosystem types. In most terrestrial systems, nitrogen limits productivity; in many marine and some freshwater systems, nitrogen or phosphorus (or both) can be limiting. When excess nitrogen from agricultural runoff enters rivers, lakes, or estuaries, it fertilizes algal growth just as it fertilizes crops on land. The resulting algal blooms, when they die and are decomposed by bacteria, deplete dissolved oxygen and create hypoxic 'dead zones.' Human industrial nitrogen fixation now exceeds all natural biological fixation combined, and the downstream consequences for water quality and biodiversity are global in scale."

- question: "Why is biological nitrogen fixation the rate-limiting step in the nitrogen cycle, and what structural feature of nitrogen gas makes enzymatic fixation so energetically costly?"
  type: short-answer
  answer: "Biological nitrogen fixation is rate-limiting because it is the only natural pathway that adds new reactive nitrogen to the biosphere from the atmospheric reservoir, and it can only be performed by a small subset of prokaryotes with the nitrogenase enzyme. All other nitrogen cycle steps (nitrification, denitrification, ammonification) merely transform nitrogen that has already been fixed — they don't increase the total reactive nitrogen pool. The energetic cost (16 ATP per N₂ fixed) stems from the N≡N triple bond, which is one of the strongest covalent bonds in chemistry. Nitrogenase must supply enough energy to break all three bonds simultaneously while reducing N₂ to 2 NH₃. The enzyme is also irreversibly inactivated by oxygen, requiring energy-expensive protective mechanisms in aerobic bacteria."
  explanation: "The triple bond strength (945 kJ/mol) is what makes N₂ so inert — essentially 'stale air' from a biological standpoint. Nitrogenase evolved in an anaerobic world and is still oxygen-sensitive, creating an interesting constraint for aerobic fixers like cyanobacteria (which evolve O₂ via photosynthesis while also fixing N₂ in specialized heterocysts). The energetic cost of fixation is why legumes invest in providing sugar to Rhizobium symbionts — the bacteria are essentially running a high-cost manufacturing process that the plant cannot do itself."
```

## Explainer

From your study of biogeochemical cycles, you know that elements move between living organisms and the physical environment in continuous loops. Nitrogen is one of the most important of these cycles — and one of the most counterintuitive. The atmosphere is 78% nitrogen gas (N₂), so it might seem strange that nitrogen is the nutrient most often limiting plant growth in terrestrial ecosystems. The problem is that the **triple bond** in N₂ is extraordinarily strong, making atmospheric nitrogen essentially inert to most organisms. Plants cannot use N₂ directly; they need nitrogen in reactive forms like ammonium (NH₄⁺) or nitrate (NO₃⁻).

**Nitrogen fixation** is the process that converts atmospheric N₂ into biologically usable ammonium, and only certain prokaryotes can do it. The most ecologically important fixers are **Rhizobium** bacteria living in root nodules of legumes (beans, clover, alfalfa) and free-living soil bacteria like *Azotobacter*. These organisms use the enzyme **nitrogenase** to break the triple bond — an energetically expensive reaction requiring 16 ATP per molecule of N₂ fixed. Cyanobacteria fix nitrogen in aquatic systems and in symbiosis with some plants. Lightning also fixes small amounts of nitrogen abiotically, but biological fixation accounts for the vast majority of new reactive nitrogen entering ecosystems.

Once nitrogen enters the biological pool as ammonium, it moves through several transformations. **Nitrification** — carried out by specialized soil bacteria — converts ammonium to nitrite and then nitrate, the form most readily absorbed by plant roots. Plants incorporate this nitrogen into amino acids and proteins, which move through food webs as animals eat plants and each other. When organisms die or excrete waste, decomposers break down organic nitrogen back to ammonium through **ammonification** (also called mineralization), completing the cycle. **Denitrification** closes the loop by converting nitrate back to N₂ gas, returning nitrogen to the atmosphere. Each step is performed by different microbial specialists, making the nitrogen cycle a relay race among microorganisms.

The practical significance is enormous. Because nitrogen fixation is slow and energetically costly, nitrogen availability limits productivity in most natural terrestrial ecosystems — adding nitrogen fertilizer dramatically increases plant growth, which is why the Haber-Bosch process (industrial nitrogen fixation) revolutionized agriculture. But excess reactive nitrogen from fertilizer runoff enters waterways and causes **eutrophication**: nitrogen-fueled algal blooms deplete dissolved oxygen when they decompose, creating dead zones in lakes, estuaries, and coastal oceans. Humans now fix more nitrogen industrially than all natural processes combined, fundamentally altering the global nitrogen cycle with consequences for water quality, biodiversity, and atmospheric chemistry.
