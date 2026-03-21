---
id: photosynthesis-in-bacteria-and-cyanobacteria
title: Photosynthesis in Bacteria and Cyanobacteria
domain: biology
course: microbiology
prerequisites:
- id: photosynthesis-overview
  type: hard
- id: bacterial-metabolism-overview
  type: soft
builds-toward:
- microbial-ecology-overview
tags:
- photosynthesis
- cyanobacteria
- energy
stage: advanced
status: draft
---

# Photosynthesis in Bacteria and Cyanobacteria

## Core Idea
Photosynthetic bacteria include anoxygenic purple and green bacteria (which use bacteriochlorophyll) and cyanobacteria (which use chlorophyll a and produce O₂ like plants). All perform light reactions and carbon fixation, but only cyanobacteria evolved oxygenic photosynthesis, fundamentally reshaping Earth's atmosphere and ecology.

## Questions

```yaml
- question: "Purple sulfur bacteria can photosynthesize and grow in the light but do not produce oxygen. Why not?"
  type: multiple-choice
  options:
    - "They lack chlorophyll and therefore cannot drive the energetically demanding water-splitting reaction"
    - "They use hydrogen sulfide (H₂S) rather than water as their electron donor, so they never split water or release O₂"
    - "They have only one photosystem, which produces insufficient energy to drive any oxidation reaction"
    - "They perform photosynthesis in anaerobic environments where oxygen would immediately react with sulfide"
  answer: 1
  explanation: "The key difference between anoxygenic and oxygenic photosynthesis is the electron donor. Purple sulfur bacteria oxidize H₂S → elemental sulfur (or H₂, or organic compounds), extracting electrons without ever splitting water. Since water-splitting is the only source of O₂ in biological photosynthesis, these organisms produce no oxygen. Option A is incorrect — bacteriochlorophyll efficiently absorbs light energy; the constraint is the electron source, not the pigment. Option C is partially true (they use one photosystem) but the real reason is the electron donor, not energy insufficiency."

- question: "What made the evolution of cyanobacteria so ecologically transformative compared to the anoxygenic photosynthetic bacteria that preceded them?"
  type: multiple-choice
  options:
    - "Cyanobacteria absorbed light more efficiently, outcompeting anoxygenic bacteria and occupying a broader range of habitats"
    - "Cyanobacteria evolved the Z-scheme — two linked photosystems — enabling them to use water as an electron donor and release O₂, transforming Earth's atmosphere"
    - "Cyanobacteria were the first organisms to fix CO₂, inventing carbon fixation where none had existed before"
    - "Cyanobacteria evolved cell walls that protected them from the UV radiation previously responsible for limiting bacterial photosynthesis"
  answer: 1
  explanation: "The Z-scheme — Photosystem II and Photosystem I working in series — was the innovation that made oxygenic photosynthesis possible. PSII has sufficient oxidizing power to strip electrons from water (a very stable molecule), releasing O₂. A single photosystem (as in anoxygenic bacteria) lacks the energy to oxidize water; two photosystems working in series provide enough. The accumulated O₂ output triggered the Great Oxidation Event (~2.4 Gya), rusting dissolved iron from the oceans, transforming atmospheric chemistry, and establishing the oxygen-rich environment that all aerobic life depends on."

- question: "Anoxygenic photosynthetic bacteria — the purple and green sulfur bacteria — are evolutionarily more ancient than cyanobacteria and dominated Earth's photic zone for over a billion years before oxygen-producing photosynthesis evolved."
  type: true-false
  answer: true
  explanation: "This is correct. Life existed for over a billion years before the evolution of oxygenic photosynthesis. During this time, anoxygenic phototrophs dominated, and Earth's atmosphere was reducing — essentially devoid of free oxygen. Cyanobacteria evolved around 2.7 Gya (with their full ecological impact from ~2.4 Gya onward), fundamentally changing the planet. This history matters for understanding the origin of chloroplasts: plant chloroplasts derive from cyanobacteria via endosymbiosis, not from the earlier anoxygenic bacteria."

- question: "Plant chloroplasts perform photosynthesis using fundamentally different molecular machinery from cyanobacteria, because they evolved independently within the eukaryotic lineage."
  type: true-false
  answer: false
  explanation: "Chloroplasts did not evolve independently — they are the descendants of ancient cyanobacteria that were engulfed by a eukaryotic host cell through endosymbiosis. Over evolutionary time, most cyanobacterial genes were transferred to the nuclear genome or lost, but the core photosynthetic machinery — including Photosystem I, Photosystem II, the cytochrome b₆f complex, and ATP synthase — is directly homologous between cyanobacteria and plant chloroplasts. Modern cyanobacteria and chloroplasts use the same Z-scheme, the same pigments (chlorophyll a), and essentially the same protein complexes. The endosymbiotic origin is why they are so similar."

- question: "Explain why two linked photosystems (the Z-scheme) are required for oxygenic photosynthesis but not for anoxygenic photosynthesis."
  type: short-answer
  answer: "Water is a very stable molecule with a high oxidation potential — stripping electrons from it requires delivering very high-energy, strongly oxidizing 'electron holes.' A single photosystem can generate enough energy to oxidize easier electron donors like H₂S or H₂, but not enough to oxidize water. The Z-scheme solves this by using two photons in series: Photosystem II generates the strong oxidant needed to split water, producing low-energy electrons that then pass through an electron transport chain to Photosystem I, which uses a second photon to boost these electrons to the high-energy state needed to reduce NADP⁺. Two sequential light-driven reactions achieve what one cannot."
  explanation: "This is the fundamental constraint distinguishing oxygenic from anoxygenic photosynthesis. Thermodynamically, the oxidation of water (E° = +0.82 V) requires a much stronger oxidizing agent than the oxidation of H₂S (E° ≈ −0.23 V). PSII generates an exceptionally strong oxidant (E° ≈ +1.1 V) specifically to accomplish water-splitting — the strongest biological oxidant known. Anoxygenic bacteria, using only one photosystem, can generate moderately strong oxidants sufficient for H₂S or H₂ but fall far short of the oxidizing power needed for water."
```

## Explainer

You already understand the general framework of photosynthesis — light reactions capturing solar energy to generate ATP and NADPH, followed by carbon fixation in the Calvin cycle. You also know the basics of bacterial metabolism. What this topic reveals is that the photosynthesis you learned about in plants is actually a bacterial invention, and the version found in plant chloroplasts represents just one branch of a much older and more diverse family of light-harvesting strategies. Bacterial photosynthesis came first by billions of years, and understanding its variations illuminates how the oxygen-rich atmosphere we breathe came to exist.

The earliest photosynthetic bacteria were **anoxygenic** — they harvested light energy but did not produce oxygen. **Purple bacteria** (like *Rhodobacter*) and **green sulfur bacteria** (like *Chlorobium*) use **bacteriochlorophyll** instead of chlorophyll a, absorbing light at longer wavelengths (in the infrared range, 800–1000 nm) that penetrate deeper into water and sediments. Crucially, these organisms use only **one photosystem** (either a Type I or Type II reaction center, but not both) and obtain electrons from donors other than water — hydrogen sulfide (H₂S), hydrogen gas (H₂), or organic compounds like succinate. Because they never split water, they never release O₂. Purple sulfur bacteria, for instance, oxidize H₂S to elemental sulfur, depositing yellow sulfur granules inside or outside their cells. These anoxygenic phototrophs dominated Earth's surface waters for over a billion years before oxygen-producing photosynthesis evolved.

**Cyanobacteria** changed everything. They are the only prokaryotes that perform **oxygenic photosynthesis**, and they do so using the same fundamental machinery found in plant chloroplasts: **Photosystem II (PSII)** and **Photosystem I (PSI)** linked in series by an electron transport chain. PSII uses light energy to split water (H₂O → 2H⁺ + ½O₂ + 2e⁻), extracting electrons and releasing molecular oxygen as a byproduct. These electrons pass through the cytochrome b₆f complex to PSI, which uses a second photon of light to boost them to a high enough energy level to reduce NADP⁺ to NADPH. This **Z-scheme** of two linked photosystems — which you may recognize from plant biology — originated in cyanobacteria. In fact, chloroplasts are descendants of ancient cyanobacteria captured by a eukaryotic host cell through **endosymbiosis**, which is why chloroplast structure, genome, and photosynthetic machinery so closely resemble those of modern cyanobacteria.

The evolutionary consequences of cyanobacterial photosynthesis were staggering. Before cyanobacteria, Earth's atmosphere contained virtually no free oxygen — it was a reducing environment dominated by CO₂, N₂, and trace gases. Beginning around 2.4 billion years ago, the accumulated oxygen output from cyanobacteria triggered the **Great Oxidation Event**, which transformed atmospheric chemistry, rusted dissolved iron out of the oceans (forming the banded iron formations visible in the geological record), and drove most obligate anaerobes into restricted anoxic habitats. Today, cyanobacteria remain enormously important: marine cyanobacteria like *Prochlorococcus* and *Synechococcus* are responsible for roughly 25% of global net primary productivity and are the most abundant photosynthetic organisms on Earth. Some cyanobacteria can also fix atmospheric nitrogen using specialized cells called **heterocysts**, which maintain an anaerobic interior to protect the oxygen-sensitive nitrogenase enzyme — making these organisms capable of both carbon and nitrogen fixation, a metabolic versatility unmatched by any plant.
