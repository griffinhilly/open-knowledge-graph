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
stage: advanced
status: draft
---

# Fear Conditioning and Circuit Plasticity

## Core Idea
Fear conditioning pairs a neutral stimulus (CS) with an aversive stimulus (US). Thalamic and cortical sensory inputs reach amygdala's lateral nucleus (LA); US input arrives via medial nucleus. Synaptic plasticity in LA (primarily LTP) underlies learning. Central nucleus projections mediate fear responses. Extinction involves new inhibitory learning rather than erasure.

## How It's Best Learned
Pair CS with US and measure freezing. Record amygdala neurons during learning and extinction.

## Common Misconceptions
Amygdala only processes fear—it processes emotional significance. Extinction erases memories—new learning inhibits expression.

## Explainer

Fear conditioning is one of the best-understood forms of associative learning in neuroscience, and it builds directly on the synaptic plasticity mechanisms — particularly **long-term potentiation** (LTP) — that you already know. The basic paradigm is simple: an animal hears a tone (the **conditioned stimulus**, CS) followed by a mild foot shock (the **unconditioned stimulus**, US). After a few pairings, the tone alone triggers a fear response — freezing, elevated heart rate, stress hormone release. The question is: where in the brain does this association form, and how?

The answer centers on the **amygdala**, specifically its **lateral nucleus** (LA). Sensory information about the tone reaches the LA through two parallel pathways: a fast, crude "low road" directly from the auditory thalamus and a slower, more processed "high road" from auditory cortex. Information about the shock arrives via somatosensory pathways and converges on the same LA neurons. When a tone-responsive neuron in the LA receives simultaneous input from the shock pathway, the conditions for **Hebbian plasticity** are met — the cell is being activated by the tone (presynaptic input) at the same time the shock depolarizes it strongly (postsynaptic activation). LTP at these synapses strengthens the tone input so that, after learning, the tone alone can drive the LA neuron strongly enough to trigger downstream fear responses. This is the same NMDA receptor-dependent LTP you studied, now performing a specific behavioral function.

The LA's output flows to the **central nucleus** (CE) of the amygdala, which acts as the command center for fear expression. Different subdivisions of the CE project to distinct brainstem and hypothalamic targets, each controlling a separate component of the fear response: the periaqueductal gray mediates freezing behavior, the lateral hypothalamus triggers sympathetic activation (increased heart rate, sweating), and the paraventricular nucleus of the hypothalamus activates the HPA stress axis to release cortisol. This anatomical organization explains why fear is not a single response but a coordinated suite of behavioral, autonomic, and endocrine changes — and why damage to different CE output pathways can selectively abolish individual fear components.

**Extinction** — the gradual reduction of fear responding when the CS is presented repeatedly without the US — is not the erasure of the original fear memory. This is one of the most important insights in the field. Instead, extinction represents new inhibitory learning: the prefrontal cortex (specifically the infralimbic region in rodents) forms a new association — "tone now predicts safety" — and projects to inhibitory interneurons in the amygdala that suppress CE output. The evidence is compelling: extinguished fear can return spontaneously after time passes, after stress, or when the animal is tested in a different context from where extinction occurred. The original fear trace persists in the LA; what changes is whether it gets expressed. This has direct clinical implications for treating anxiety disorders and PTSD — exposure therapy works through extinction-like mechanisms, and understanding that the fear memory remains latent explains why relapse is common and why strategies to strengthen extinction (rather than simply weaken fear) are a major focus of translational research.
