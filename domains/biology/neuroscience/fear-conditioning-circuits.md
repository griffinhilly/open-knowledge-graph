---
id: fear-conditioning-circuits
title: Fear Conditioning and Circuit Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: long-term-potentiation
  type: hard
- id: synaptic-transmission
  type: soft
builds-toward:
- extinction-learning
- ptsd-mechanisms
tags:
- fear
- conditioning
- learning
- memory
stage: expert
status: draft
---

# Fear Conditioning and Circuit Plasticity

## Core Idea
Fear conditioning pairs a neutral stimulus (CS) with an aversive stimulus (US). Thalamic and cortical sensory inputs reach amygdala's lateral nucleus (LA); US input arrives via medial nucleus. Synaptic plasticity in LA (primarily LTP) underlies learning. Central nucleus projections mediate fear responses. Extinction involves new inhibitory learning rather than erasure.

## How It's Best Learned
Pair CS with US and measure freezing. Record amygdala neurons during learning and extinction.

## Common Misconceptions
Amygdala only processes fear—it processes emotional significance. Extinction erases memories—new learning inhibits expression.

## Questions

```yaml
- question: "A patient with PTSD completes a 12-week exposure therapy program and shows no fear response to trauma-related stimuli at the end of treatment. Three months later, after a stressful period, the fear response fully returns. What does this clinical pattern demonstrate about fear extinction?"
  type: multiple-choice
  options:
    - "The therapy erased the original fear memory, but stress triggered the formation of a new one"
    - "Extinction created new inhibitory learning that suppressed the original fear trace; the fear memory remained intact and was reactivated by stress"
    - "The patient's amygdala regenerated the damaged circuits that originally stored the fear memory"
    - "Stress hormones directly activated fear circuits without requiring a stored fear memory"
  answer: 1
  explanation: "Spontaneous return of extinguished fear after stress is one of the key pieces of evidence that extinction does not erase the original memory — it creates competing inhibitory learning. The prefrontal cortex forms a 'CS predicts safety' association that suppresses amygdala output, but the original LTP-strengthened CS–US association in the lateral amygdala persists. Stress disrupts prefrontal inhibitory control, unmasking the latent fear trace. This is why exposure therapy is effective but relapses occur, and why strengthening extinction consolidation is a major research priority."

- question: "During fear conditioning, LTP is induced at tone-responsive synapses in the lateral amygdala because:"
  type: multiple-choice
  options:
    - "The unconditioned stimulus activates the central nucleus, which sends feedback to strengthen tone inputs in the lateral nucleus"
    - "The conditioned stimulus activates lateral amygdala neurons presynaptically at the same time the unconditioned stimulus strongly depolarizes them postsynaptically, fulfilling the Hebbian conditions for NMDA receptor-dependent LTP"
    - "Cortisol released during the shock globally strengthens all synapses in the amygdala through genomic mechanisms"
    - "Repeated tone presentations without shock gradually strengthen the tone synapse through homeostatic plasticity"
  answer: 1
  explanation: "This directly applies Hebbian LTP to fear learning. Tone arrives via thalamo-amygdalar and cortical pathways to the lateral amygdala (LA). Shock arrives via somatosensory pathways and strongly depolarizes the same LA neurons. When presynaptic tone activity coincides with strong postsynaptic depolarization from the shock, NMDA receptors at tone synapses are activated (their Mg²⁺ block removed by depolarization), triggering LTP. After learning, the tone alone drives LA neurons strongly enough to trigger fear responses. Option A confuses nucleus locations. Option C is partly true (stress hormones modulate consolidation) but not the primary LTP mechanism."

- question: "Extinction of a conditioned fear response represents new inhibitory learning rather than erasure of the original fear memory."
  type: true-false
  answer: true
  explanation: "The evidence is compelling: extinguished fear can recover spontaneously after time passes (spontaneous recovery), return after stress, or reappear when tested in a different context from where extinction occurred (renewal). If extinction had erased the memory, none of these phenomena could occur. Instead, extinction produces new cortical learning — prefrontal cortex projects to inhibitory interneurons in the amygdala that suppress central nucleus output. The original fear trace in the lateral amygdala remains; what changes is whether it gets expressed."

- question: "The amygdala is a specialized fear center whose only function is to detect threatening stimuli and produce fear responses."
  type: true-false
  answer: false
  explanation: "The amygdala processes emotional significance broadly, not fear exclusively. It is activated by positive stimuli (food rewards, attractive faces, pleasurable events), by novelty and uncertainty, and by social signals of many kinds. The amygdala's role in reward learning and social cognition is well-established. The 'fear center' label arose because fear conditioning is a methodologically convenient paradigm, but conflating the amygdala's experimental role in fear research with its broader function in evaluating motivational relevance misrepresents the neuroscience. Amygdala damage disrupts reward learning and social judgment as well as fear responses."

- question: "Why does extinction represent new inhibitory learning rather than erasure of the fear memory, and what evidence from animal studies supports this interpretation?"
  type: short-answer
  answer: "Extinction creates a new association (CS predicts safety) in prefrontal cortex, which projects to inhibitory interneurons in the amygdala to suppress fear expression. The original CS–US fear trace in the lateral amygdala persists. Three phenomena demonstrate this: (1) spontaneous recovery — fear returns after a rest interval with no further shocks; (2) renewal — fear returns when testing occurs in a different context from extinction; (3) reinstatement — a single unsignaled shock after extinction restores fear responses. All three require the original memory to be latent, not erased."
  explanation: "These three phenomena are the canonical evidence against the erasure interpretation. They show that extinction is context-dependent and time-limited in a way that complete erasure would not be. Clinically, this means exposure therapy creates a competing inhibitory memory, not a cure — relapse is predictable when inhibitory control is disrupted by stress, context change, or time. This understanding motivates research into pharmacological agents that enhance extinction consolidation, making the new inhibitory memory stronger and more resistant to disruption."
```

## Explainer

Fear conditioning is one of the best-understood forms of associative learning in neuroscience, and it builds directly on the synaptic plasticity mechanisms — particularly **long-term potentiation** (LTP) — that you already know. The basic paradigm is simple: an animal hears a tone (the **conditioned stimulus**, CS) followed by a mild foot shock (the **unconditioned stimulus**, US). After a few pairings, the tone alone triggers a fear response — freezing, elevated heart rate, stress hormone release. The question is: where in the brain does this association form, and how?

The answer centers on the **amygdala**, specifically its **lateral nucleus** (LA). Sensory information about the tone reaches the LA through two parallel pathways: a fast, crude "low road" directly from the auditory thalamus and a slower, more processed "high road" from auditory cortex. Information about the shock arrives via somatosensory pathways and converges on the same LA neurons. When a tone-responsive neuron in the LA receives simultaneous input from the shock pathway, the conditions for **Hebbian plasticity** are met — the cell is being activated by the tone (presynaptic input) at the same time the shock depolarizes it strongly (postsynaptic activation). LTP at these synapses strengthens the tone input so that, after learning, the tone alone can drive the LA neuron strongly enough to trigger downstream fear responses. This is the same NMDA receptor-dependent LTP you studied, now performing a specific behavioral function.

The LA's output flows to the **central nucleus** (CE) of the amygdala, which acts as the command center for fear expression. Different subdivisions of the CE project to distinct brainstem and hypothalamic targets, each controlling a separate component of the fear response: the periaqueductal gray mediates freezing behavior, the lateral hypothalamus triggers sympathetic activation (increased heart rate, sweating), and the paraventricular nucleus of the hypothalamus activates the HPA stress axis to release cortisol. This anatomical organization explains why fear is not a single response but a coordinated suite of behavioral, autonomic, and endocrine changes — and why damage to different CE output pathways can selectively abolish individual fear components.

**Extinction** — the gradual reduction of fear responding when the CS is presented repeatedly without the US — is not the erasure of the original fear memory. This is one of the most important insights in the field. Instead, extinction represents new inhibitory learning: the prefrontal cortex (specifically the infralimbic region in rodents) forms a new association — "tone now predicts safety" — and projects to inhibitory interneurons in the amygdala that suppress CE output. The evidence is compelling: extinguished fear can return spontaneously after time passes, after stress, or when the animal is tested in a different context from where extinction occurred. The original fear trace persists in the LA; what changes is whether it gets expressed. This has direct clinical implications for treating anxiety disorders and PTSD — exposure therapy works through extinction-like mechanisms, and understanding that the fear memory remains latent explains why relapse is common and why strategies to strengthen extinction (rather than simply weaken fear) are a major focus of translational research.
