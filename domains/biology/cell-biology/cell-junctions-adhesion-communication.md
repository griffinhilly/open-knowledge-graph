---
id: cell-junctions-adhesion-communication
title: 'Cell Junctions: Adhesion and Communication'
domain: biology
course: cell-biology
prerequisites:
- id: cell-membrane-fluid-mosaic
  type: hard
- id: cytoskeleton-cellular-framework
  type: hard
- id: gap-junctions-communication
  type: soft
tags:
- junction
- adhesion
- contact
stage: formal-systems
status: validated
---
# Cell Junctions: Adhesion and Communication

## Core Idea
Cells adhere through specialized junction proteins: tight junctions seal tissues and prevent paracellular passage; desmosomes anchor cytoskeletons of adjacent cells for mechanical strength; adherens junctions form contacting belts; hemidesmosomes anchor cells to the extracellular matrix. Each junction type involves specific protein families (claudins, cadherins, integrins) linked to cytoskeletal elements. Loss of junction integrity is a hallmark of cancer metastasis.

## How It's Best Learned
Examine electron micrographs of junction structures. Identify protein components and their cytoskeletal links. Explain how tight junctions create selective barriers in epithelial tissues.

## Common Misconceptions
All junctions are identical—each has distinct structure and function. Tight junctions are absolutely impermeable—they are selectively permeable. Cell adhesion is a weakness—it provides essential mechanical integrity and tumor suppression.

## Questions

```yaml
- question: "A drug blocks a specific membrane channel that allows small ions and second messengers to pass directly between adjacent cardiac muscle cell cytoplasms. The cardiac muscle cells begin to contract asynchronously. Which junction type is being disrupted?"
  type: multiple-choice
  options:
    - "Tight junctions, because they control the movement of molecules between cells"
    - "Desmosomes, because they link the cytoskeletons of adjacent cardiac cells"
    - "Gap junctions, because connexon channels electrically couple cardiac cells by allowing current to spread directly between cytoplasms"
    - "Hemidesmosomes, because they anchor cardiac cells to the extracellular matrix"
  answer: 2
  explanation: "Gap junctions are composed of connexin proteins that form connexon channels docking between adjacent cells. These channels allow ions (including K⁺ and Ca²⁺) and small second messengers to pass directly from one cytoplasm to the next, spreading electrical depolarization without requiring neurotransmitter release. Cardiac synchrony depends critically on this electrical coupling — blocking gap junctions severs the cell-to-cell current flow and disrupts coordinated contraction. Tight junctions control paracellular flow (between cells, not through them), and desmosomes provide mechanical anchoring, not electrical communication."

- question: "Patients with pemphigus vulgaris develop severe skin blistering because autoimmune antibodies attack desmosomal cadherins (desmogleins). This outcome best illustrates which property of desmosomes?"
  type: multiple-choice
  options:
    - "Desmosomes form the primary barrier preventing paracellular passage of toxins through skin"
    - "Desmosomes anchor intermediate filament networks of adjacent cells into a continuous mechanical network; their disruption destroys the tissue's ability to resist shear and tensile forces"
    - "Desmosomes couple skin cells electrically, and their loss desynchronizes the shedding cycle"
    - "Desmosomes attach the basal layer of skin to the basement membrane, and their loss causes cells to detach from below"
  answer: 1
  explanation: "Desmosomes act as spot-welds between cells, with cadherin family proteins (desmogleins, desmocollins) linking the intermediate filament cytoskeletons of neighboring cells. This creates a continuous mechanical network that distributes tensile and shear forces across the entire epithelium. When autoantibodies in pemphigus target desmogleins, the rivets are dissolved — adjacent cells lose their attachment to each other and the tissue tears apart under normal mechanical stress, causing blisters. This is a direct demonstration that desmosomes are load-bearing structures essential for tissue integrity under stress, not just 'sticky proteins.'"

- question: "Tight junctions form an absolute impermeable seal between epithelial cells, preventing all transport between cells."
  type: true-false
  answer: false
  explanation: "Tight junctions are selectively permeable, not absolutely impermeable. Different epithelial tissues express different claudin isoforms that create junctions of varying tightness. The kidney tubule, for example, strategically places 'leaky' tight junctions (expressing claudins that allow paracellular ion flow) in segments where passive reabsorption is needed, and 'tight' junctions in segments requiring precise concentration control. The intestinal epithelium uses tight junctions to prevent most luminal contents from entering the bloodstream while still permitting regulated paracellular transport. 'Tight' is a relative term — the defining feature is selectivity and controlled permeability, not absolute impermeability."

- question: "Gap junctions primarily serve mechanical adhesion between neighboring cells, which is why their disruption in cardiac tissue impairs the structural integrity of the heart wall."
  type: true-false
  answer: false
  explanation: "Gap junctions serve communication, not mechanical adhesion. They allow ions, small second messengers, and metabolites to pass directly between cytoplasms — this is what electrically couples cardiac cells for synchronized contraction. Mechanical integrity in the heart is provided by desmosomes (spot-welding intermediate filaments of adjacent cells) and adherens junctions (actin-linked belts). If gap junctions in cardiac tissue were disrupted, the structural integrity would be largely unaffected, but the cells would lose electrical coupling and contract asynchronously — which is exactly what happens in some arrhythmia-associated gap junction diseases."

- question: "How does loss of E-cadherin function contribute to cancer metastasis, and why does this make mechanistic sense given E-cadherin's role in adherens junctions?"
  type: short-answer
  answer: "E-cadherin in adherens junctions physically links adjacent epithelial cells into a continuous sheet via actin cytoskeleton connections, and also suppresses pro-migratory signaling intracellularly. When E-cadherin is lost (through mutation, epigenetic silencing, or proteolytic cleavage), cells lose both physical adhesion to neighbors and the restraining signal. This triggers epithelial-to-mesenchymal transition: cells adopt a migratory phenotype, detach from the epithelial layer, and invade surrounding tissue. Loss of E-cadherin is thus not merely a loss of 'glue' — it simultaneously removes a structural anchor and a tumor suppressor signal."
  explanation: "E-cadherin loss is one of the most common molecular events in epithelial cancer progression. It is a canonical hallmark of the transition from carcinoma in situ (confined) to invasive cancer. Understanding it mechanistically — as disruption of a junction that integrates both structural and signaling functions — explains why simple adhesion mutants (which only affect stickiness) do not fully recapitulate metastasis, while E-cadherin loss does: the full phenotypic consequence requires loss of both the physical linkage and the downstream signaling suppression."
```

## Explainer

You know from the fluid mosaic model that the cell membrane is a dynamic lipid bilayer studded with proteins, and from your study of the cytoskeleton that cells have internal structural networks of actin, intermediate filaments, and microtubules. Cell junctions are where these two systems meet: they are specialized protein complexes that physically connect neighboring cells (or anchor cells to the extracellular matrix), linking the membranes and cytoskeletons of adjacent cells into a mechanically and functionally integrated tissue.

**Tight junctions** (also called zonula occludens) form a continuous seal near the apical surface of epithelial cells. Transmembrane proteins called **claudins** and **occludins** from adjacent cells interlock like the teeth of a zipper, creating a barrier that controls what can pass between cells. Think of the epithelial lining of your intestine: tight junctions prevent stomach acid and digestive enzymes from leaking between cells into the bloodstream. However, tight junctions are not absolute seals — different claudin isoforms create junctions of varying "tightness," allowing selective paracellular transport of ions and small molecules. The kidney tubule exploits this by expressing different claudins in different segments to fine-tune ion reabsorption.

**Anchoring junctions** provide mechanical strength, and there are two main types. **Desmosomes** (macula adherens) connect the intermediate filament networks of adjacent cells via **cadherin** family proteins called desmogleins and desmocollins. Picture two cells riveted together at spot-welds, with each rivet anchored deep into the cell's internal cable network — that is a desmosome. They are abundant in tissues under mechanical stress, such as skin and cardiac muscle. **Adherens junctions** (zonula adherens) form continuous belts around cells using classical cadherins linked to the actin cytoskeleton, coordinating cell shape changes during development and wound healing. **Hemidesmosomes** anchor the basal surface of epithelial cells to the underlying **extracellular matrix** via **integrins** rather than cadherins, connecting to intermediate filaments inside the cell and to laminin in the basement membrane outside.

**Gap junctions** serve communication rather than adhesion. Six **connexin** proteins assemble into a channel called a **connexon**, and connexons from adjacent cells dock to form a continuous pore between the two cytoplasms. These channels allow ions, second messengers (like cAMP and Ca²⁺), and small metabolites (up to ~1 kDa) to pass directly between cells, electrically and metabolically coupling them. This is how cardiac muscle cells synchronize their contractions — an action potential spreads from cell to cell through gap junctions without requiring synaptic neurotransmission. The clinical relevance of junctions is profound: autoimmune diseases like pemphigus target desmosomal cadherins, causing skin blistering, and the loss of E-cadherin function in adherens junctions is one of the hallmarks of epithelial cancers transitioning to invasive, metastatic behavior.
