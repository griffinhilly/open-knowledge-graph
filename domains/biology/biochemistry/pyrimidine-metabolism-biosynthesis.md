---
id: pyrimidine-metabolism-biosynthesis
title: Pyrimidine Biosynthesis
domain: biology
course: biochemistry
prerequisites:
- id: nucleotide-structure-and-nomenclature
  type: hard
builds-toward:
- nucleotide-salvage-pathways
tags:
- pyrimidine
- de-novo-synthesis
stage: advanced
status: draft
---

# Pyrimidine Biosynthesis

## Core Idea
Pyrimidine synthesis begins with the formation of orotic acid from carbamoyl phosphate and aspartate, then conversion to orotidylate, and finally decarboxylation to UMP. Unlike purine synthesis (which is de novo), pyrimidine synthesis produces the intact ring first, then attaches the sugar. Conversion to CTP and dTMP completes the pathway. UMPS (uridine 5'-monophosphate synthase) catalyzes the final steps.

## Explainer

If you understand nucleotide structure and nomenclature — the distinction between bases, nucleosides, and nucleotides, and how pyrimidine rings differ from purines — then pyrimidine biosynthesis is the story of how cells actually build these rings from scratch. The most important conceptual distinction to grasp is that pyrimidine synthesis assembles the **ring first, sugar second**, which is the exact opposite of purine synthesis (where the ring is built on top of an already-attached ribose).

The pathway begins with two familiar precursors: **carbamoyl phosphate** (synthesized from glutamine, CO₂, and ATP by carbamoyl phosphate synthetase II in the cytoplasm) and **aspartate**. These condense in a reaction catalyzed by aspartate transcarbamoylase (ATCase) — one of the most extensively studied allosteric enzymes in biochemistry. The product undergoes ring closure and oxidation to form **orotate**, a complete six-membered pyrimidine ring that is not yet attached to any sugar. Only at this point does orotate react with PRPP (phosphoribosyl pyrophosphate) to receive its ribose-5-phosphate group, producing **orotidylate** (OMP). The enzyme **UMPS** then decarboxylates OMP to yield **UMP** (uridine monophosphate), the first true pyrimidine nucleotide.

From UMP, the pathway branches to produce the other pyrimidine nucleotides the cell needs. UMP is phosphorylated to UDP and then UTP, which is aminated by **CTP synthetase** (using glutamine as the nitrogen donor) to produce **CTP** — the cytosine nucleotide used in RNA and, after reduction, in DNA. For DNA synthesis, the cell also needs thymidylate (dTMP), which is produced from dUMP by **thymidylate synthase** using N⁵,N¹⁰-methylene-tetrahydrofolate as both a one-carbon donor and a reductant. This step is a major target for anticancer drugs: methotrexate blocks dihydrofolate reductase (needed to regenerate the folate cofactor), and 5-fluorouracil is a suicide inhibitor of thymidylate synthase itself.

Regulation of pyrimidine biosynthesis operates primarily at the first committed step. In bacteria, ATCase is inhibited by CTP (the end product) and activated by ATP (signaling that the cell has energy and purines available, so pyrimidine production should keep pace). In mammals, the regulatory step shifts to carbamoyl phosphate synthetase II, which is inhibited by UTP and activated by PRPP. This feedback loop ensures that pyrimidine production matches cellular demand — ramping up during S phase when DNA replication requires massive nucleotide pools, and throttling back when pools are sufficient.
