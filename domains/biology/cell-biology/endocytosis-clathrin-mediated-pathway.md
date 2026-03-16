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
stage: abstract-reasoning
status: draft
---

# Clathrin-Mediated Endocytosis

## Core Idea
Clathrin-mediated endocytosis internalizes receptor-bound ligands and membrane components into progressively invaginating coated pits that pinch off as coated vesicles. Clathrin heavy chains polymerize into lattices on the cytoplasmic membrane surface, with adaptor proteins (AP2 complex) recognizing cargo-bound receptors. After vesicle scission via dynamin GTPase, the clathrin coat is rapidly shed by Hsc70 and auxilin, exposing cargo for sorting in early endosomes.

## How It's Best Learned
Observe coated pits and vesicles by electron microscopy; track fluorescently-labeled cargo from coated vesicles to early endosomes. Inhibit clathrin with siRNA or dominant-negative dynamins to block endocytosis.

## Common Misconceptions
- Clathrin directly binds cargo; adaptor proteins mediate all cargo recognition. - Coated vesicles immediately fuse with endosomes; there's a brief transit phase before fusion.

## Explainer

From your study of receptor-mediated endocytosis, you know that cells selectively internalize specific molecules by capturing them with surface receptors and pulling them inward in membrane-bound vesicles. **Clathrin-mediated endocytosis** is the best-characterized molecular mechanism for how this actually works — the step-by-step process by which a patch of membrane recognizes its cargo, curves inward, and pinches off as a vesicle. It is the cell's primary route for internalizing receptor-ligand complexes such as LDL-cholesterol, transferrin-iron, and activated growth factor receptors.

The process begins when cargo binds to its receptor on the cell surface. On the cytoplasmic side of the membrane, **adaptor protein complexes** — most notably **AP2** — recognize specific sorting signals (typically short amino acid motifs like YXXΦ or dileucine motifs) on the cytoplasmic tails of cargo-loaded receptors. AP2 serves as a molecular bridge: one face binds the receptor tail, while the other face recruits **clathrin**. This is a critical point — clathrin itself never touches the cargo or even the membrane directly. Clathrin molecules are three-legged structures called **triskelions**, and when recruited by AP2 and other adaptors, they self-assemble into a polyhedral lattice (resembling a soccer ball) on the cytoplasmic surface of the membrane. As the lattice grows, it imposes curvature on the underlying membrane, progressively bending it inward to form a **coated pit**.

The pit deepens until only a narrow neck connects the invagination to the plasma membrane. At this point, the GTPase **dynamin** is recruited to the neck, where it polymerizes into a helical collar. GTP hydrolysis drives a conformational change in the dynamin helix that constricts and severs the neck, releasing the **coated vesicle** into the cytoplasm. This scission step is remarkably fast — the entire process from pit formation to vesicle release takes about one to two minutes. Almost immediately after release, the clathrin coat is disassembled: the ATPase **Hsc70** (a constitutive heat shock protein) and its cofactor **auxilin** pry clathrin triskelions off the vesicle, recycling them for the next round of endocytosis. The coat must come off because it would physically block the vesicle from fusing with its target compartment.

The uncoated vesicle then delivers its contents to the **early endosome**, where cargo is sorted. Some receptors are recycled back to the plasma membrane (as with transferrin receptor), while others are directed to late endosomes and lysosomes for degradation (as with activated EGF receptor). This sorting decision has profound biological consequences: recycling keeps receptors available for reuse, while degradation permanently downregulates signaling. Defects in clathrin-mediated endocytosis cause real disease — for example, mutations in the LDL receptor's internalization signal prevent cholesterol uptake, causing familial hypercholesterolemia, one of the most common genetic disorders.
