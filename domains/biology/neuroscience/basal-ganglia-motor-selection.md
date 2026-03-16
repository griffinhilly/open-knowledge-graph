---
id: basal-ganglia-motor-selection
title: 'Basal Ganglia: Action Selection and Motor Planning'
domain: biology
course: neuroscience
prerequisites:
- id: synaptic-transmission
  type: soft
- id: dopamine-reward-system
  type: hard
builds-toward:
- cerebellum-motor-coordination
tags:
- motor-systems
- basal-ganglia
- action-selection
- planning
stage: advanced
status: draft
---

# Basal Ganglia: Action Selection and Motor Planning

## Core Idea
The basal ganglia (striatum, globus pallidus, substantia nigra) form interconnected loops that select which motor program to execute and suppress unwanted actions. Dopamine in the striatum modulates the balance between direct (movement-facilitating) and indirect (movement-inhibiting) pathways; loss of dopamine in Parkinson's disease tips the balance toward inhibition, causing bradykinesia and rigidity.

## Explainer

You already understand that neurons communicate through synaptic transmission and that dopamine functions as a neuromodulator in reward-related circuits. The basal ganglia take these principles and apply them to a specific, critical problem: out of the many possible actions your brain could execute at any moment, how does it select just one and suppress the rest?

Think of the basal ganglia as a gating system. At rest, the output nuclei of the basal ganglia — the **globus pallidus internal segment** (GPi) and the **substantia nigra pars reticulata** (SNr) — fire tonically at high rates, sending continuous inhibitory (GABAergic) signals to the thalamus. This tonic inhibition keeps the thalamus from activating motor cortex, effectively putting a brake on all movements. To move, the brain must release the brake on the specific motor program it wants while keeping the brakes on everything else. This is the essence of **action selection**: not generating movement from scratch, but selectively disinhibiting the right motor plan.

Two parallel pathways through the basal ganglia accomplish this. The **direct pathway** runs from the striatum (the input nucleus, receiving cortical excitation) directly to GPi/SNr. Striatal neurons in this pathway are inhibitory (GABAergic), so when cortex activates them, they inhibit GPi, which releases the thalamus from inhibition — a double negative that yields a positive: movement is facilitated. The **indirect pathway** takes a longer route through the external globus pallidus (GPe) and the subthalamic nucleus (STN), ultimately increasing GPi output and strengthening the inhibition of the thalamus. The indirect pathway thus suppresses competing motor programs. The two pathways work in concert: the direct pathway opens the gate for the selected action while the indirect pathway tightens the gate on everything else.

**Dopamine** from the substantia nigra pars compacta (SNc) is the critical modulator that balances these pathways. Dopamine excites direct-pathway neurons (which express D1 receptors) and inhibits indirect-pathway neurons (which express D2 receptors). The net effect of dopamine is to tip the system toward movement by simultaneously facilitating the "go" pathway and suppressing the "stop" pathway. This is why the loss of dopaminergic neurons in **Parkinson's disease** is so devastating: without dopamine, the indirect pathway dominates, tonic inhibition of the thalamus increases, and patients experience slowness of movement (bradykinesia), rigidity, and difficulty initiating actions. Conversely, excessive dopamine signaling can produce involuntary movements (dyskinesias) or impulsive action selection, as seen in some side effects of Parkinson's medications. The basal ganglia thus exemplify how neuromodulation tunes circuit-level computation to produce adaptive behavior.
