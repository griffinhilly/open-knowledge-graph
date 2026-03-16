---
id: synaptic-vesicle-release-exocytosis
title: Synaptic Vesicle Release and Exocytosis
domain: biology
course: neuroscience
prerequisites:
- id: neurotransmitter-synthesis-storage
  type: hard
- id: cell-membrane-structure
  type: hard
builds-toward:
- ionotropic-vs-metabotropic-receptors
tags:
- synaptic-transmission
- exocytosis
stage: advanced
status: draft
---

# Synaptic Vesicle Release and Exocytosis

## Core Idea
Action potentials open voltage-gated Ca2+ channels; Ca2+ influx triggers SNARE-mediated vesicle fusion. One quantum (~5,000 molecules) released per vesicle; probabilistic, depends on Ca2+ level.

## Explainer

You already know that neurotransmitters are synthesized and loaded into small membrane-bound compartments called synaptic vesicles, and that the cell membrane is a lipid bilayer that naturally resists fusion with other membranes. The central question of synaptic transmission is: how does an electrical signal (the action potential) get converted into the physical release of chemical messengers across that membrane barrier? The answer is calcium-triggered **exocytosis** — a precisely controlled process in which a vesicle merges with the presynaptic membrane and dumps its contents into the synaptic cleft.

When an action potential arrives at the axon terminal, it depolarizes the membrane and opens **voltage-gated calcium channels** concentrated near docked vesicles. Calcium ions flood inward down their steep electrochemical gradient — extracellular calcium concentration is roughly 10,000 times higher than intracellular. This calcium influx is the trigger. Calcium binds to a sensor protein called **synaptotagmin** on the vesicle surface, which undergoes a conformational change that catalyzes the final step of membrane fusion. The entire sequence — from action potential arrival to neurotransmitter release — takes less than a millisecond, making it one of the fastest regulated secretory events in biology.

The molecular machinery that physically pulls the vesicle and plasma membranes together is the **SNARE complex**. Three proteins — synaptobrevin (on the vesicle), syntaxin, and SNAP-25 (on the plasma membrane) — zipper together into a tight four-helix bundle that forces the two lipid bilayers into close apposition. Think of it like twisting two ropes together: as the SNARE proteins wind around each other, they generate enough mechanical force to overcome the natural repulsion between lipid membranes. Before calcium arrives, a clamp protein called **complexin** holds the partially assembled SNARE complex in a primed but blocked state. Calcium-bound synaptotagmin releases this clamp and simultaneously inserts into the membrane, triggering fusion within microseconds.

Each vesicle releases a fixed packet — or **quantum** — of roughly 5,000 neurotransmitter molecules. Whether any given vesicle actually fuses when an action potential arrives is probabilistic, not deterministic: the **release probability** at a typical central synapse is only 10–30%. This means that most docked vesicles do not fire on any single action potential. The probability depends on the local calcium concentration, which in turn depends on how many calcium channels open and how close they are to the vesicle. This probabilistic nature gives synapses enormous flexibility: release probability can be turned up or down by modulatory signals, forming the basis of short-term synaptic plasticity. After fusion, the vesicle membrane is retrieved by endocytosis and recycled, reloaded with neurotransmitter, and re-docked — completing the vesicle cycle that sustains ongoing synaptic communication.
