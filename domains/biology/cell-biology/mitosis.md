---
id: mitosis
title: Mitosis
domain: biology
course: cell-biology
prerequisites:
- id: cell-cycle-overview
  type: hard
- id: nucleus-and-genetic-material
  type: hard
- id: cell-cycle-regulation
  type: soft
- id: cell-division-basics
  type: soft
builds-toward:
- cytokinesis
- meiosis
tags:
- mitosis
- prophase
- metaphase
- anaphase
- telophase
- chromosomes
stage: formal-systems
status: validated
---
# Mitosis

## Core Idea
Mitosis is the phase of the cell cycle in which the duplicated chromosomes are separated into two genetically identical daughter nuclei. It proceeds through four stages: prophase (chromosomes condense, spindle forms), metaphase (chromosomes align at the cell equator), anaphase (sister chromatids are pulled to opposite poles), and telophase (nuclear envelopes reform, chromosomes decondense). The spindle apparatus, made of microtubules from centrosomes, attaches to chromosomes at kinetochores and provides the mechanical force for chromosome segregation. Mitosis produces two daughter cells with the same chromosome number as the parent.

## How It's Best Learned
Sketch each phase and describe what is happening to chromosomes, spindle, and nuclear envelope at each stage. Then trace what happens to a single chromosome from G2 through cytokinesis. Use fluorescent imaging videos to see the dynamic nature of the process.

## Common Misconceptions
- Sister chromatids (joined after S phase) separate during anaphase of mitosis; homologous chromosomes do not separate during mitosis (that's meiosis I).
- Chromosomes don't 'choose' where to go — they are pulled by spindle fiber dynamics (microtubule polymerization/depolymerization).

## Questions

```yaml
- question: "During anaphase of mitosis, what exactly is being pulled to opposite poles of the cell?"
  type: multiple-choice
  options: ["Homologous chromosome pairs separating from each other", "Sister chromatids separating after the cohesin holding them is cleaved", "Replicated chromosomes moving before DNA synthesis", "Individual nucleotides being distributed to daughter cells"]
  answer: 1
  explanation: "During S phase, each chromosome is duplicated into two identical copies called sister chromatids, held together at the centromere by a protein complex called cohesin. During anaphase of mitosis, cohesin is cleaved, releasing the sister chromatids from each other, and spindle fibers pull them to opposite poles. Each former chromatid becomes a full chromosome in the daughter cell. Homologous chromosome separation happens in meiosis I, not mitosis."

- question: "Homologous chromosomes are separated from each other during anaphase of mitosis."
  type: true-false
  answer: false
  explanation: "This is a critical distinction between mitosis and meiosis. During mitosis, it is sister chromatids (copies of the same chromosome) that separate — homologous chromosomes never pair up or separate during mitosis. Homologous chromosome separation occurs in anaphase I of meiosis. Confusing these two processes is one of the most common errors in understanding cell division."

- question: "What role does the spindle apparatus play in mitosis, and how does it actually move chromosomes?"
  type: short-answer
  answer: "The spindle apparatus is a structure of microtubule fibers that attaches to chromosomes at protein complexes called kinetochores. It physically moves chromosomes by controlled polymerization and depolymerization of microtubules — shortening the kinetochore microtubules pulls chromosomes toward the poles, while polar microtubules push the poles apart. The force is mechanical, not chemical signaling."
  explanation: "Understanding the spindle as a mechanical pulling machine (not a passive scaffold) clarifies why chromosome segregation errors occur when spindle dynamics are disrupted. Many cancer chemotherapy drugs (e.g., taxol, vincristine) work by interfering with microtubule dynamics, which halts mitosis and triggers cell death — which is why they target rapidly dividing cancer cells."
```

## Explainer

From your study of the cell cycle, you know that a cell must duplicate its DNA during S phase before dividing. But copying the genome creates a problem: you now have two complete sets of chromosomes — one original and one copy — all tangled together in the nucleus. The cell's challenge during mitosis is to sort these duplicated chromosomes precisely, so each daughter cell gets exactly one complete copy of the genome. Mitosis is the elegant mechanical solution to this problem.

The stages of mitosis track the behavior of chromosomes and the machinery that moves them. During **prophase**, the chromosomes condense from diffuse chromatin into compact, visible structures, and the spindle apparatus begins to assemble from the centrosomes. The key structure at this stage is each chromosome: after DNA replication, each chromosome consists of two identical sister chromatids held together at the centromere by a protein called cohesin. Think of a single chromosome as an X shape — two identical copies joined at the middle.

In **metaphase**, the spindle fibers extend from both poles and attach to chromosomes at protein complexes called kinetochores, located at each centromere. The chromosomes are pushed and pulled until they align at the cell's equator (the metaphase plate). This alignment is not random — the cell checks that every kinetochore has a spindle attachment before proceeding, a quality-control checkpoint that ensures no chromosome is left behind.

**Anaphase** is when the actual separation occurs. An enzyme cleaves the cohesin holding sister chromatids together, and the spindle fibers shorten by depolymerizing — physically reeling the chromosomes toward opposite poles. The key point: it is sister chromatids separating, not homologous chromosomes. Each pole now has one complete set. In **telophase**, nuclear envelopes reform around each set, chromosomes decondense, and the spindle breaks down. The cell then undergoes cytokinesis — physical division of the cytoplasm — producing two genetically identical daughter cells.

A common confusion is between mitosis and meiosis. Remember that mitosis produces two diploid daughter cells identical to the parent — it is used for growth, tissue repair, and asexual reproduction. Homologous chromosomes never pair or separate during mitosis. That pairing and separation is the defining feature of meiosis I, which produces the genetic variation needed for sexual reproduction. If you keep this distinction sharp — sister chromatids in mitosis, homologs in meiosis I — the rest of cell division logic falls into place.

