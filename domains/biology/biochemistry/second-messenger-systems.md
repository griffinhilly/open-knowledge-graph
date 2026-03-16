---
id: second-messenger-systems
title: 'Second Messenger Systems: cAMP, IP₃, and DAG'
domain: biology
course: biochemistry
prerequisites:
- id: receptor-signaling-pathways
  type: hard
- id: hormone-signaling-mechanisms
  type: soft
builds-toward:
- protein-kinase-signaling-cascades
tags:
- cAMP
- IP3
- DAG
- second-messengers
stage: advanced
status: draft
---

# Second Messenger Systems: cAMP, IP₃, and DAG

## Core Idea
Second messengers relay signals from cell surface receptors to intracellular targets. cAMP (via adenylyl cyclase) activates protein kinase A; IP₃ and DAG (via phospholipase C) activate IP₃ receptors (Ca²⁺ release) and protein kinase C. Ca²⁺ is both a second messenger and a crucial intracellular regulator, controlling metabolism, muscle contraction, and gene expression.

## Explainer

From your study of receptor signaling, you understand that hormones and other extracellular signals bind to receptors on the cell surface. But most of these signaling molecules cannot enter the cell — they are the "first messengers" that deliver information to the outside of the membrane. The cell needs a way to relay that signal internally, and this is the job of **second messengers**: small, rapidly produced intracellular molecules that amplify and propagate the signal to downstream targets throughout the cytoplasm.

The **cAMP pathway** is the best-studied example. When a hormone like epinephrine binds a G protein-coupled receptor (GPCR), the activated Gα subunit stimulates **adenylyl cyclase**, an enzyme embedded in the plasma membrane. Adenylyl cyclase converts ATP into **cyclic AMP** (cAMP) by forming an internal phosphodiester bond and releasing pyrophosphate. A single activated receptor can stimulate many adenylyl cyclase molecules, and each adenylyl cyclase produces many cAMP molecules — this is signal amplification in action. cAMP then activates **protein kinase A (PKA)** by binding to its regulatory subunits and releasing the catalytic subunits, which phosphorylate dozens of target proteins. The signal is terminated by **phosphodiesterase**, which hydrolyzes cAMP to ordinary AMP. Caffeine works partly by inhibiting phosphodiesterase, prolonging cAMP signaling — which is why it makes you feel alert and energized.

The **phospholipase C (PLC) pathway** produces two second messengers simultaneously from a single membrane lipid. When a GPCR activates PLC, the enzyme cleaves **phosphatidylinositol 4,5-bisphosphate (PIP₂)** in the plasma membrane into **inositol 1,4,5-trisphosphate (IP₃)** and **diacylglycerol (DAG)**. IP₃ is water-soluble and diffuses through the cytoplasm to the endoplasmic reticulum, where it opens IP₃-gated calcium channels, releasing stored Ca²⁺ into the cytoplasm. DAG remains in the membrane and, together with the released Ca²⁺, activates **protein kinase C (PKC)**, which phosphorylates its own set of target proteins. This branching design allows a single receptor activation event to trigger two parallel downstream cascades.

**Calcium ions** deserve special attention because Ca²⁺ functions as a second messenger in its own right, participating in an extraordinary range of cellular processes — from muscle contraction to neurotransmitter release to gene activation. Cells maintain cytoplasmic Ca²⁺ at extremely low concentrations (around 100 nM) by actively pumping it into the ER and out of the cell. This steep gradient means that even a small release through IP₃ receptors or voltage-gated channels produces a dramatic concentration spike that can be detected by sensor proteins like **calmodulin**. Calmodulin binds four Ca²⁺ ions, changes shape, and activates calmodulin-dependent kinases (CaM kinases) and other effectors. The common theme across all second messenger systems is amplification, speed, and reversibility: a few receptor events produce thousands of messenger molecules within seconds, and dedicated enzymes (phosphodiesterases, phosphatases, Ca²⁺ pumps) rapidly shut the signal off when the first messenger is removed.
