---
id: oligodendrocytes
title: Oligodendrocytes and Myelination
domain: biology
course: neuroscience
prerequisites:
- id: myelinated-axon-saltatory-conduction
  type: hard
- id: neuron-structure-and-function
  type: soft
tags:
- glial-cells
- myelin
stage: expert
status: draft
---

# Oligodendrocytes and Myelination

## Core Idea
Wrap membrane around axons to form myelin insulation in CNS. Enable saltatory conduction. Myelin is compacted, insulating membrane with little cytoplasm. Disruption causes demyelinating disorders.

## Questions

```yaml
- question: "In multiple sclerosis, the immune system attacks oligodendrocytes. Why does damage to a single oligodendrocyte cause more widespread neurological disruption than damage to a single Schwann cell in the peripheral nervous system?"
  type: multiple-choice
  options:
    - "Oligodendrocytes produce thicker myelin than Schwann cells, so their loss removes more insulation per cell"
    - "A single oligodendrocyte can myelinate segments on up to 40–50 different axons simultaneously; a Schwann cell myelinates only one axon segment — so losing one oligodendrocyte demyelinates dozens of axons at once"
    - "Oligodendrocytes are located in the brain where the nervous system is more sensitive, not because of any difference in how many axons they serve"
    - "There is no fundamental difference — both cell types serve approximately the same number of axons per cell"
  answer: 1
  explanation: "The contrast in coverage is the key functional difference. Each Schwann cell wraps one axon segment; damage to one Schwann cell affects one segment on one axon. An oligodendrocyte extends several processes that each wrap different axons, myelinating up to 40–50 axon segments across many neurons. The efficiency of this arrangement in normal function becomes a vulnerability in disease: a single oligodendrocyte's death simultaneously disrupts conduction in dozens of axons, explaining why MS lesions (plaques) can cause such widespread and varied symptoms."

- question: "Prolonged demyelination in the CNS can eventually lead to permanent axonal degeneration, not just slowed signal conduction. What best explains this progression?"
  type: multiple-choice
  options:
    - "Demyelinated axons are directly attacked and destroyed by the same immune cells that targeted the oligodendrocyte"
    - "Without myelin, axons are mechanically fragile and fragment from normal brain movement"
    - "Oligodendrocytes supply lactate and metabolites to axons through channels in the myelin sheath; prolonged loss of this metabolic support starves the axon and eventually causes degeneration"
    - "Demyelinated axons fire continuously at high frequency until they deplete their ATP reserves and undergo metabolic failure"
  answer: 2
  explanation: "Oligodendrocytes are not merely passive insulators — they are metabolically coupled to the axons they myelinate, delivering lactate and other metabolites through channels in the compact myelin. When demyelination persists, the axon loses not just electrical insulation but this essential nutritional support. This explains why MS can cause irreversible neurological disability even after apparent clinical recovery from a relapse: if demyelination is prolonged, axonal degeneration may occur before remyelination restores metabolic supply."

- question: "Oligodendrocytes function purely as passive insulators — they wrap axons with myelin to speed signal conduction but have no metabolic relationship with the axons they myelinate."
  type: true-false
  answer: false
  explanation: "This is the classic misconception about oligodendrocyte function. Beyond insulation, oligodendrocytes actively support the axons they myelinate by supplying metabolites (including lactate) through channels in the myelin sheath. This metabolic coupling means the oligodendrocyte-axon relationship is symbiotic rather than purely structural. The clinical consequence is that demyelination eventually threatens axon survival through metabolic deprivation — not just conduction failure — which is why permanent disability can accumulate in MS."

- question: "One functional difference between oligodendrocytes and Schwann cells is that a single oligodendrocyte can simultaneously myelinate segments on many different axons, while each Schwann cell myelinates only a single axon segment."
  type: true-false
  answer: true
  explanation: "This is the defining structural difference. In the CNS, oligodendrocytes extend multiple flat sheet-like processes, each wrapping a segment of a different axon — one cell can serve 40–50 axons. In the PNS, each Schwann cell wraps a single internode of a single axon. The oligodendrocyte arrangement is more metabolically efficient (one cell maintains many myelinated segments) but creates greater vulnerability (damage to one cell simultaneously affects many axons)."

- question: "Why does the metabolic relationship between oligodendrocytes and axons mean that demyelinating diseases can cause permanent neurological damage that persists even after remyelination?"
  type: short-answer
  answer: "Oligodendrocytes supply lactate and other metabolites to the axons beneath their myelin through gap junctions and channels in the compact sheath. If demyelination persists long enough, this metabolic supply is withdrawn and axons begin to degenerate. Once axonal degeneration is established, restoring the myelin sheath through remyelination cannot recover function in the degenerated axons — the damage is irreversible. This is why early intervention matters in MS: remyelination therapies can restore function if applied before axonal degeneration occurs, but cannot reverse damage after the fact."
  explanation: "This insight has driven current MS research toward two targets: preventing demyelination (immunosuppression) and promoting remyelination (stimulating oligodendrocyte precursor cells) before the window for recovery closes. It also explains the progressive phase of MS, where disability accumulates even between acute relapses — slow ongoing axonal degeneration in chronically demyelinated regions."
```

## Explainer

From your study of saltatory conduction, you know that myelin sheaths wrap around axons and force action potentials to jump between nodes of Ranvier, dramatically increasing conduction speed. In the central nervous system, the cells responsible for producing this myelin are **oligodendrocytes** — a class of glial cells whose name literally means "cells with few branches," though those few branches do remarkable work.

A single oligodendrocyte extends several flat, sheet-like processes, each of which wraps concentrically around a segment of a nearby axon. Imagine wrapping a strip of tape around a wire — each turn adds another layer of insulation. The oligodendrocyte's membrane is extraordinarily rich in lipid (about 70% by dry weight), particularly **myelin basic protein (MBP)** and **proteolipid protein (PLP)**, which help compact the membrane layers tightly together with very little cytoplasm between them. This compaction is critical: the tightly packed lipid bilayers create a high-resistance, low-capacitance sheath that prevents ion leakage across the axon membrane, which is exactly what makes saltatory conduction possible.

One key difference from the peripheral nervous system is worth noting. In the PNS, **Schwann cells** perform myelination, but each Schwann cell wraps only a single axon segment. An oligodendrocyte, by contrast, can myelinate segments on up to 40–50 different axons simultaneously. This efficiency comes at a cost: if a single oligodendrocyte is damaged or dies, dozens of axon segments lose their myelin at once. This is exactly what happens in **multiple sclerosis (MS)**, where the immune system attacks oligodendrocytes and their myelin. The resulting demyelinated patches — called plaques — slow or block signal conduction along the affected axons, producing symptoms that depend on which tracts are involved: vision problems when optic nerve myelin is damaged, weakness when motor tracts are affected, numbness when sensory pathways lose insulation.

Oligodendrocytes are also metabolically coupled to the axons they myelinate. They supply lactate and other metabolites to the underlying axon through channels in the myelin sheath, meaning the relationship is not merely insulation but active metabolic support. This explains why demyelination does not just slow signals — it can eventually lead to **axonal degeneration** if the metabolic support is withdrawn for too long. Understanding oligodendrocyte biology is therefore central to developing therapies for demyelinating diseases, and current research focuses on promoting **remyelination** by stimulating oligodendrocyte precursor cells that persist in the adult brain.
