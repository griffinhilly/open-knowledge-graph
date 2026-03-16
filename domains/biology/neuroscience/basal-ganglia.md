---
id: basal-ganglia
title: 'Basal Ganglia: Action Selection and Initiation'
domain: biology
course: neuroscience
prerequisites:
- id: motor-cortex
  type: hard
- id: dopamine-systems
  type: hard
tags:
- motor-systems
- action-selection
stage: advanced
status: draft
---

# Basal Ganglia: Action Selection and Initiation

## Core Idea
Direct pathway (facilitates action) and indirect pathway (inhibits action) to motor thalamus. Dopamine strengthens direct (D1) and weakens indirect (D2), enabling movement initiation.

## Explainer

The motor cortex, which you have already studied, generates the commands that drive voluntary movement. But the cortex does not act alone — it needs a gating mechanism that decides *which* of the many possible movements should be released at any given moment and which should be suppressed. This is the central job of the **basal ganglia**: action selection through a balance of facilitation and inhibition. The logic is elegant — the basal ganglia hold the motor system in a default state of inhibition, and selected actions are released by temporarily lifting that brake.

The circuit begins in the **striatum** (caudate and putamen), which receives excitatory glutamatergic input from nearly the entire cerebral cortex. From the striatum, two parallel pathways project to the output nuclei of the basal ganglia (the globus pallidus internal segment, GPi, and the substantia nigra pars reticulata, SNr). The **direct pathway** runs from the striatum straight to GPi/SNr. Striatal neurons in this pathway are inhibitory (GABAergic), and so are GPi/SNr neurons — which tonically inhibit the thalamus. So when the direct pathway fires, it inhibits the inhibitor: the striatum suppresses GPi/SNr, which releases the thalamus from inhibition, which then excites the motor cortex. The net effect is **disinhibition** — the selected action is released. The **indirect pathway** takes a longer route through the external globus pallidus (GPe) and subthalamic nucleus (STN), and its net effect is the opposite: it increases GPi/SNr activity, strengthening thalamic inhibition and suppressing unwanted movements.

This is where your knowledge of dopamine systems becomes essential. Dopamine from the **substantia nigra pars compacta** (SNc) modulates both pathways simultaneously but in opposite directions. Striatal neurons in the direct pathway express **D1 receptors**, which are excitatory — dopamine makes them more likely to fire, promoting movement. Striatal neurons in the indirect pathway express **D2 receptors**, which are inhibitory — dopamine makes them less likely to fire, reducing the suppressive brake. The combined effect of dopamine is therefore to tip the balance toward action: strengthening the "go" signal while weakening the "stop" signal.

The clinical consequences of this circuit are dramatic. In **Parkinson's disease**, dopaminergic neurons in the SNc degenerate, reducing dopamine input to the striatum. Without dopamine, the direct pathway is underactive (too little go) and the indirect pathway is overactive (too much stop). The result is the hallmark symptoms: bradykinesia (slow movement), rigidity, and difficulty initiating actions. In **Huntington's disease**, early degeneration of indirect pathway neurons removes the brake, producing the involuntary, excessive movements called chorea. These disorders are essentially opposite imbalances in the same circuit — Parkinson's is too much inhibition, Huntington's is too little — which underscores how precisely the basal ganglia must balance facilitation and suppression for normal motor function.
