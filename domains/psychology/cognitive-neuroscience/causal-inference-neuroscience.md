---
id: causal-inference-neuroscience
title: Causal Inference in Neural Research
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: transcranial-magnetic-stimulation
  type: hard
- id: lesion-neuropsychology-dissociations
  type: soft
tags:
- methods
- causality
- inference
stage: advanced
status: draft
---

# Causal Inference in Neural Research

## Core Idea
Neuroimaging reveals correlations between brain activity and behavior, but doesn't establish causation. Only interventional methods—TMS, lesions, pharmacology, optogenetics—can determine whether a brain region is necessary or sufficient for a function. Single dissociations (region X damage impairs only function Y) show necessity; double dissociations (patient A loses Y but not X; patient B shows opposite) show functional independence. Null results from TMS or lesions are equally informative, showing regions aren't necessary for tested functions.

## Explainer

You have already studied transcranial magnetic stimulation (TMS) and know that it temporarily disrupts cortical function by inducing a rapidly changing magnetic field that depolarizes or suppresses neural activity in a targeted region. You also know about lesion neuropsychology—how patients with damage to specific brain areas lose specific cognitive abilities. Both are tools for making **causal claims** in neuroscience, and understanding why they matter requires understanding what standard neuroimaging cannot tell you on its own.

When an fMRI study shows that the fusiform face area activates more strongly when people view faces than houses, that correlation is a starting point, not a conclusion. The region is *associated* with face processing—but association doesn't establish necessity or sufficiency. Perhaps the region is active because face processing happens nearby and the BOLD signal spreads. Perhaps it's active because attention increases whenever faces appear, and the region actually responds to attention rather than face identity. Neuroimaging excels at generating hypotheses about which regions might be involved in a function, but confirming those hypotheses requires **interventional methods** that perturb the system and observe the consequences. The logic is identical to any causal inference: correlation tells you what goes together; intervention tells you what depends on what.

The **lesion method** provides one form of interventional evidence. If damage to a region reliably impairs a function, the region is *necessary* for that function. But single dissociations can mislead—maybe the damage disrupted white matter pathways passing through the region rather than the region itself, or maybe the impaired function is simply harder and more vulnerable to any brain damage. The stronger inference is the **double dissociation**: Patient A has damage to region X and loses function Y but not Z; Patient B has damage to region Z and loses function Z but not Y. This pattern rules out the "harder task" confound because both functions can be the spared one depending on lesion location. It demonstrates that Y and Z depend on genuinely independent neural systems, not just that one is more resource-intensive. Double dissociations are the gold standard for inferring functional independence in neuropsychology.

TMS provides a kind of "virtual lesion" in healthy participants: delivering pulses over a region at a specific moment during a task can slow or disrupt performance if the region is causally involved. Unlike permanent lesions, TMS can be precisely timed—delivered 100 ms after stimulus onset to disrupt early processing, or 200 ms later to disrupt later stages—allowing inference about *when* a region is necessary, not just *whether* it is. Null TMS results carry real information too: if disrupting a region produces no performance cost, that region probably isn't necessary for the tested function, even if it was active in fMRI. This asymmetry—activation is neither necessary nor sufficient for causal involvement—is why neuroscience requires converging evidence from correlational and interventional methods. A brain region becomes a convincing functional component when neuroimaging shows it activates, TMS shows its disruption impairs behavior, and ideally lesion evidence shows its loss produces the same deficit.
