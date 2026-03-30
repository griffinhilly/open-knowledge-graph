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
status: validated
---

# Causal Inference in Neural Research

## Core Idea
Neuroimaging reveals correlations between brain activity and behavior, but doesn't establish causation. Only interventional methods—TMS, lesions, pharmacology, optogenetics—can determine whether a brain region is necessary or sufficient for a function. Single dissociations (region X damage impairs only function Y) show necessity; double dissociations (patient A loses Y but not X; patient B shows opposite) show functional independence. Null results from TMS or lesions are equally informative, showing regions aren't necessary for tested functions.

## Questions

```yaml
- question: "An fMRI study shows that brain region X activates significantly more during face recognition than during object recognition. A researcher concludes that region X is necessary for face processing. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "fMRI cannot detect neural activity, only blood flow changes"
    - "Activation demonstrates association, not necessity — a TMS or lesion study is needed to show the region is causally required"
    - "The study should have used a different baseline condition"
    - "Region X may simply be the only face-processing region, making the result trivially true"
  answer: 1
  explanation: "Neuroimaging reveals correlations — region X co-varies with face processing — but cannot establish that the region is necessary or sufficient. The region might be active because of attention, emotional salience, or proximity to the true face-processing circuit. Only interventional methods that perturb the region (TMS, lesions) and observe behavioral consequences can establish necessity. This is the core causal inference problem in neuroimaging research."

- question: "Patient A has damage to region X and loses function Y but retains function Z. Patient B has damage to region Z and loses function Z but retains function Y. This pattern is called a double dissociation and it demonstrates what?"
  type: multiple-choice
  options:
    - "That function Y is more cognitively demanding than function Z"
    - "That functions Y and Z depend on genuinely independent neural systems"
    - "That region X and region Z are the only brain areas involved in these functions"
    - "That lesion studies are more reliable than TMS studies"
  answer: 1
  explanation: "A double dissociation rules out the 'harder task' confound: if Y were simply harder than Z, any brain damage might impair Y while sparing Z. The double dissociation shows that either function can be selectively preserved depending on lesion location, which is only possible if they depend on distinct neural substrates. This is why double dissociations are the gold standard for inferring functional independence in neuropsychology."

- question: "If a TMS pulse delivered over brain region X produces no measurable impairment on task Y, this result proves that region X is not involved in task Y."
  type: true-false
  answer: false
  explanation: "A null TMS result shows that region X is not *necessary* for task Y as tested, but it does not prove the region is entirely uninvolved. The TMS timing might have missed the critical window, the spatial targeting might be imprecise, or the region might contribute redundantly with other areas. Null results are genuinely informative — they rule out necessity under specific conditions — but they cannot establish that a region is completely uninvolved. This is an important asymmetry in causal inference from interventional neuroscience."

- question: "A double dissociation provides stronger causal evidence for functional independence between two cognitive processes than a single dissociation alone."
  type: true-false
  answer: true
  explanation: "A single dissociation (damage to X impairs only Y) can be explained by task difficulty differences — harder tasks are always more vulnerable to any brain damage. The double dissociation eliminates this confound because it shows each function can be selectively preserved while the other is impaired, depending only on which region is damaged. The pattern is only coherent if the two functions genuinely rely on separate neural systems, not just if one is harder than the other."

- question: "Why can neuroimaging alone not establish that a brain region is necessary for a cognitive function, and what kind of evidence is required?"
  type: short-answer
  answer: "Neuroimaging shows correlation — a region is active when a function is engaged — but correlation does not imply necessity. A region could be active due to associated processes (attention, effort, emotional response) rather than the function itself. Establishing necessity requires interventional evidence: showing that when the region is disrupted (via TMS, lesion, or pharmacology), the function is impaired. TMS provides virtual lesions in healthy participants; permanent lesion studies provide complementary evidence. Ideally, converging evidence from both imaging and intervention gives the strongest causal claim."
  explanation: "The logic parallels causal inference generally: observational co-variation generates hypotheses, but only experimental manipulation — holding everything else constant while perturbing the variable of interest — can establish causation. In neuroscience, the 'experiment' is an intervention on brain function, not just measuring it."
```

## Explainer

You have already studied transcranial magnetic stimulation (TMS) and know that it temporarily disrupts cortical function by inducing a rapidly changing magnetic field that depolarizes or suppresses neural activity in a targeted region. You also know about lesion neuropsychology—how patients with damage to specific brain areas lose specific cognitive abilities. Both are tools for making **causal claims** in neuroscience, and understanding why they matter requires understanding what standard neuroimaging cannot tell you on its own.

When an fMRI study shows that the fusiform face area activates more strongly when people view faces than houses, that correlation is a starting point, not a conclusion. The region is *associated* with face processing—but association doesn't establish necessity or sufficiency. Perhaps the region is active because face processing happens nearby and the BOLD signal spreads. Perhaps it's active because attention increases whenever faces appear, and the region actually responds to attention rather than face identity. Neuroimaging excels at generating hypotheses about which regions might be involved in a function, but confirming those hypotheses requires **interventional methods** that perturb the system and observe the consequences. The logic is identical to any causal inference: correlation tells you what goes together; intervention tells you what depends on what.

The **lesion method** provides one form of interventional evidence. If damage to a region reliably impairs a function, the region is *necessary* for that function. But single dissociations can mislead—maybe the damage disrupted white matter pathways passing through the region rather than the region itself, or maybe the impaired function is simply harder and more vulnerable to any brain damage. The stronger inference is the **double dissociation**: Patient A has damage to region X and loses function Y but not Z; Patient B has damage to region Z and loses function Z but not Y. This pattern rules out the "harder task" confound because both functions can be the spared one depending on lesion location. It demonstrates that Y and Z depend on genuinely independent neural systems, not just that one is more resource-intensive. Double dissociations are the gold standard for inferring functional independence in neuropsychology.

TMS provides a kind of "virtual lesion" in healthy participants: delivering pulses over a region at a specific moment during a task can slow or disrupt performance if the region is causally involved. Unlike permanent lesions, TMS can be precisely timed—delivered 100 ms after stimulus onset to disrupt early processing, or 200 ms later to disrupt later stages—allowing inference about *when* a region is necessary, not just *whether* it is. Null TMS results carry real information too: if disrupting a region produces no performance cost, that region probably isn't necessary for the tested function, even if it was active in fMRI. This asymmetry—activation is neither necessary nor sufficient for causal involvement—is why neuroscience requires converging evidence from correlational and interventional methods. A brain region becomes a convincing functional component when neuroimaging shows it activates, TMS shows its disruption impairs behavior, and ideally lesion evidence shows its loss produces the same deficit.
