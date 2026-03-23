---
id: endocytosis-clathrin-mediated-pathway
title: Clathrin-Mediated Endocytosis
domain: biology
course: cell-biology
prerequisites:
- id: receptor-mediated-endocytosis
  type: hard
- id: cell-membrane-structure
  type: soft
builds-toward:
- exocytosis-snare-proteins-membrane-fusion
tags:
- endocytosis
- vesicular-transport
- protein-trafficking
stage: formal-systems
status: validated
---

# Clathrin-Mediated Endocytosis

## Core Idea
Clathrin-mediated endocytosis internalizes receptor-bound ligands and membrane components into progressively invaginating coated pits that pinch off as coated vesicles. Clathrin heavy chains polymerize into lattices on the cytoplasmic membrane surface, with adaptor proteins (AP2 complex) recognizing cargo-bound receptors. After vesicle scission via dynamin GTPase, the clathrin coat is rapidly shed by Hsc70 and auxilin, exposing cargo for sorting in early endosomes.

## How It's Best Learned
Observe coated pits and vesicles by electron microscopy; track fluorescently-labeled cargo from coated vesicles to early endosomes. Inhibit clathrin with siRNA or dominant-negative dynamins to block endocytosis.

## Common Misconceptions
- Clathrin directly binds cargo; adaptor proteins mediate all cargo recognition. - Coated vesicles immediately fuse with endosomes; there's a brief transit phase before fusion.

## Questions

```yaml
- question: "A researcher mutates the cytoplasmic tail of the LDL receptor, eliminating its YXXΦ internalization signal. What is the most direct consequence for LDL receptor internalization?"
  type: multiple-choice
  options:
    - "Clathrin can no longer assemble into a lattice at the membrane near the LDL receptor"
    - "Dynamin cannot be recruited to sever the forming coated pit"
    - "AP2 cannot recognize the LDL receptor tail, so it cannot bridge the receptor to clathrin, blocking internalization"
    - "The LDL receptor is degraded in the endoplasmic reticulum before reaching the cell surface"
  answer: 2
  explanation: "The YXXΦ motif is a sorting signal recognized by the AP2 adaptor complex — not by clathrin directly. AP2 acts as a molecular bridge: one face binds the receptor's cytoplasmic tail (via its cargo-recognition domain), the other face recruits clathrin. Without the YXXΦ signal, AP2 cannot bind the receptor, so clathrin is not recruited to that location, no coated pit forms around the LDL receptor, and it cannot be internalized. This is the basis of familial hypercholesterolemia — mutations in the LDL receptor internalization signal block cholesterol uptake despite a normal receptor and normal clathrin machinery."

- question: "What is the role of dynamin in clathrin-mediated endocytosis?"
  type: multiple-choice
  options:
    - "It recruits clathrin triskelions to form the initial coated pit lattice"
    - "It recognizes cargo sorting signals on receptor cytoplasmic tails"
    - "It polymerizes into a helical collar around the vesicle neck and uses GTP hydrolysis to drive membrane scission"
    - "It uncoats the clathrin lattice from the vesicle after scission using ATP hydrolysis"
  answer: 2
  explanation: "Dynamin is the GTPase responsible for the final pinching-off step. It polymerizes into a helix around the narrow neck connecting the deepened coated pit to the plasma membrane. GTP hydrolysis drives a conformational change in the dynamin helix that constricts and severs the neck, releasing the coated vesicle into the cytoplasm. Dynamin is not involved in recognizing cargo (that is AP2), recruiting clathrin (that is AP2 and other adaptors), or removing the coat (that is Hsc70 and auxilin). Dominant-negative dynamin mutants block endocytosis specifically at the scission step, trapping coated pits with elongated necks."

- question: "The clathrin coat must be removed from a newly released vesicle before it can fuse with early endosomes."
  type: true-false
  answer: true
  explanation: "Coat removal is not optional — it is a prerequisite for membrane fusion. The clathrin lattice physically obstructs the fusion machinery (SNAREs and other membrane proteins) from accessing the vesicle surface. Immediately after scission, Hsc70 (a constitutive ATPase) and its cofactor auxilin disassemble the triskelion lattice, exposing the vesicle membrane. Only after uncoating can the vesicle be recognized by Rab5 and EEA1, the tethering factors that guide it to early endosomes. This is a general principle of vesicular transport: the coat drives cargo capture and membrane curvature, but must be shed before delivery."

- question: "Clathrin triskelions directly recognize and bind to internalization signals on the cytoplasmic tails of transmembrane cargo receptors."
  type: true-false
  answer: false
  explanation: "This is the key misconception explicitly flagged in this topic. Clathrin never directly contacts cargo or the membrane's cytoplasmic face in a cargo-specific way. Clathrin's role is structural: it self-assembles into a polyhedral lattice that imposes curvature on the membrane. All cargo specificity resides in the adaptor proteins — primarily the AP2 complex — which bind both the cargo receptor's sorting signal and the clathrin triskelion. This two-step logic (adaptors recognize cargo, clathrin provides mechanical force) allows the same clathrin machinery to internalize many different cargo types by swapping or combining different adaptor proteins."

- question: "Why must the cell rapidly shed the clathrin coat immediately after vesicle scission, and what molecular machinery accomplishes this?"
  type: short-answer
  answer: "The clathrin coat must be shed because it physically obstructs the fusion machinery required for the vesicle to merge with its target compartment (the early endosome). The coat also sterically blocks tethering factors and SNARE proteins from accessing the vesicle membrane. Coat removal is carried out by the ATPase Hsc70, a constitutive heat shock cognate protein, working with its cofactor auxilin. Auxilin binds to the clathrin lattice and recruits Hsc70; ATP hydrolysis by Hsc70 provides the mechanical energy to pry clathrin triskelions off the vesicle surface. The free triskelions are recycled into the cytoplasmic pool for the next round of endocytosis."
  explanation: "Understanding why coat removal is required — not just when it happens — reveals the logic of vesicular transport. Coats serve two purposes: capturing cargo (via adaptors) and deforming the membrane (via the rigid lattice). Once the vesicle is released, the coat's job is done, and its continued presence becomes an obstacle. This same logic applies to other coated transport vesicles (COPI, COPII): every coat must be shed before the vesicle can fuse with its destination compartment."
```

## Explainer

From your study of receptor-mediated endocytosis, you know that cells selectively internalize specific molecules by capturing them with surface receptors and pulling them inward in membrane-bound vesicles. **Clathrin-mediated endocytosis** is the best-characterized molecular mechanism for how this actually works — the step-by-step process by which a patch of membrane recognizes its cargo, curves inward, and pinches off as a vesicle. It is the cell's primary route for internalizing receptor-ligand complexes such as LDL-cholesterol, transferrin-iron, and activated growth factor receptors.

The process begins when cargo binds to its receptor on the cell surface. On the cytoplasmic side of the membrane, **adaptor protein complexes** — most notably **AP2** — recognize specific sorting signals (typically short amino acid motifs like YXXΦ or dileucine motifs) on the cytoplasmic tails of cargo-loaded receptors. AP2 serves as a molecular bridge: one face binds the receptor tail, while the other face recruits **clathrin**. This is a critical point — clathrin itself never touches the cargo or even the membrane directly. Clathrin molecules are three-legged structures called **triskelions**, and when recruited by AP2 and other adaptors, they self-assemble into a polyhedral lattice (resembling a soccer ball) on the cytoplasmic surface of the membrane. As the lattice grows, it imposes curvature on the underlying membrane, progressively bending it inward to form a **coated pit**.

The pit deepens until only a narrow neck connects the invagination to the plasma membrane. At this point, the GTPase **dynamin** is recruited to the neck, where it polymerizes into a helical collar. GTP hydrolysis drives a conformational change in the dynamin helix that constricts and severs the neck, releasing the **coated vesicle** into the cytoplasm. This scission step is remarkably fast — the entire process from pit formation to vesicle release takes about one to two minutes. Almost immediately after release, the clathrin coat is disassembled: the ATPase **Hsc70** (a constitutive heat shock protein) and its cofactor **auxilin** pry clathrin triskelions off the vesicle, recycling them for the next round of endocytosis. The coat must come off because it would physically block the vesicle from fusing with its target compartment.

The uncoated vesicle then delivers its contents to the **early endosome**, where cargo is sorted. Some receptors are recycled back to the plasma membrane (as with transferrin receptor), while others are directed to late endosomes and lysosomes for degradation (as with activated EGF receptor). This sorting decision has profound biological consequences: recycling keeps receptors available for reuse, while degradation permanently downregulates signaling. Defects in clathrin-mediated endocytosis cause real disease — for example, mutations in the LDL receptor's internalization signal prevent cholesterol uptake, causing familial hypercholesterolemia, one of the most common genetic disorders.
