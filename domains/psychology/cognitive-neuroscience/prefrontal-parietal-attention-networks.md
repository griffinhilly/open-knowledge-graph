---
id: prefrontal-parietal-attention-networks
title: Prefrontal-Parietal Attention Networks and Control
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: attention-networks-brain
  type: hard
- id: spatial-attention-parietal-cortex
  type: hard
builds-toward:
- ventral-attention-circuit-salient-events
- attention-control-training-neural-mechanisms
tags:
- attention-networks
- dorsal-attention
- FPA
- IPS
- top-down-control
stage: advanced
status: draft
---

# Prefrontal-Parietal Attention Networks and Control

## Core Idea
The dorsal attention network comprises dorsolateral prefrontal cortex and intraparietal sulcus, which together orchestrate voluntary attention allocation through top-down control signals. This network is distinct from the ventral attention network (inferior frontal and temporoparietal cortex) that responds to behaviorally relevant stimuli captured from the environment. The two networks interact competitively, with dorsal network activity predicting reduced distraction by salient events.

## Questions

```yaml
- question: "A person is deeply absorbed in a cognitively demanding task when a loud, unexpected sound occurs nearby. Compared to when they are at rest, they are slower to orient toward the sound. Which network-level mechanism best explains this?"
  type: multiple-choice
  options:
    - "The auditory cortex is suppressed during demanding tasks, reducing perception of sounds"
    - "Strong engagement of the dorsal attention network suppresses ventral attention network activity, raising the threshold for stimulus-driven attentional capture"
    - "The temporoparietal junction is selectively activated during demanding tasks, blocking re-orienting"
    - "Dopamine released during focused work chemically inhibits sensory processing"
  answer: 1
  explanation: "The dorsal attention network (DAN: DLPFC + IPS) and ventral attention network (VAN: IFG + TPJ) interact competitively. When DAN engagement is high — as during demanding voluntary attention — VAN activity is suppressed, reducing the system's responsiveness to salient but task-irrelevant stimuli. The auditory cortex is not suppressed; the bottleneck is the attentional re-orienting system, not low-level perception."

- question: "Which brain region is most critical for automatic attentional re-orienting toward unexpected, behaviorally relevant stimuli?"
  type: multiple-choice
  options:
    - "Dorsolateral prefrontal cortex (DLPFC)"
    - "Intraparietal sulcus (IPS)"
    - "Right temporoparietal junction (TPJ)"
    - "Primary visual cortex (V1)"
  answer: 2
  explanation: "The right temporoparietal junction (TPJ) is the core node of the ventral attention network, which mediates bottom-up, stimulus-driven attentional capture. DLPFC and IPS belong to the dorsal attention network and support voluntary, top-down control. V1 is a sensory area, not an attentional control node. The right-lateralization of the VAN explains why right TPJ damage produces severe left-field spatial neglect."

- question: "The dorsal and ventral attention networks operate in parallel and independently, each handling separate categories of attention without directly influencing each other."
  type: true-false
  answer: false
  explanation: "The DAN and VAN interact competitively, not independently. When the DAN is strongly engaged, VAN activity is suppressed — reducing distractibility. When the VAN is activated by a salient event, it can interrupt or override DAN-mediated top-down control. Understanding this competitive balance is central to the prefrontal-parietal framework; the two networks are nodes in an ongoing negotiation over attentional allocation."

- question: "Damage to the right temporoparietal junction is more likely than damage to the left to produce hemispatial neglect of the contralesional visual field."
  type: true-false
  answer: true
  explanation: "The ventral attention network — responsible for re-orienting attention to unexpected, behaviorally relevant stimuli — is strongly right-lateralized, centered on the right IFG and TPJ. When the right TPJ is damaged, the re-orienting system fails: attention cannot be captured by left-field stimuli even when they are dramatically salient. Left TPJ damage produces much less severe neglect because the right hemisphere can partially compensate for bilateral attentional functions."

- question: "According to the DAN/VAN framework, why might stimulant medications that enhance prefrontal dopamine signaling reduce distractibility in individuals with ADHD?"
  type: short-answer
  answer: "Enhanced prefrontal dopamine strengthens dorsal attention network (DAN) engagement, which competitively suppresses ventral attention network (VAN) activity. Since ADHD is associated with reduced prefrontal control over the VAN — leaving individuals highly susceptible to stimulus-driven attentional capture — boosting DAN function raises the threshold at which salient but task-irrelevant stimuli can trigger VAN-mediated re-orienting, improving the signal-to-noise ratio for voluntary attention."
  explanation: "The key causal chain is: prefrontal dopamine → stronger DLPFC activity → stronger DAN → competitive suppression of VAN → reduced attentional capture by distractors. This maps the pharmacological mechanism directly onto the network-level framework. It also illustrates a general principle: drugs that modulate neurotransmission produce behavioral effects by shifting the balance between large-scale networks, not by acting on isolated neurons."
```

## Explainer

Your study of attention networks and the spatial functions of parietal cortex established that attention is not a single process — it is a collection of functions that can be anatomically dissociated. The prefrontal-parietal framework formalizes this dissociation into two large-scale networks that serve complementary and competing roles. The **dorsal attention network (DAN)** consists primarily of the **dorsolateral prefrontal cortex (DLPFC)** and the **intraparietal sulcus (IPS)**. These regions are engaged when you deliberately direct attention — when you decide to focus on the left side of a screen, search for a particular feature, or prepare for an expected target location. DLPFC supplies the goal representation ("attend to red objects") while IPS implements it by biasing sensory processing in posterior visual cortex. This is **top-down, voluntary** attentional control.

The **ventral attention network (VAN)** has a different anatomy and a different function. Centered on the **right inferior frontal gyrus (IFG)** and **temporoparietal junction (TPJ)**, this network is activated not by deliberate goal-setting but by stimuli that are behaviorally relevant, unexpected, or salient — a sudden loud sound, a face that appears in your peripheral vision, your own name in a noisy room. These events capture attention automatically, re-orienting it toward the stimulus regardless of current goals. This is **bottom-up, stimulus-driven** capture. Critically, the VAN is right-lateralized and plays a key role in re-orienting spatial attention following unexpected events, which is why right TPJ lesions produce severe spatial neglect of the contralesional (usually left) field.

The two networks interact **competitively**: when the DAN is strongly engaged — when you are deeply absorbed in a focused task — the VAN is suppressed, reducing susceptibility to distraction. Conversely, salient events that activate the VAN can interrupt or override the DAN's top-down control, producing an attentional capture effect. This competitive balance explains a wealth of everyday phenomena: why demanding tasks make you less responsive to irrelevant interruptions, why highly salient stimuli (motion, sudden onset, emotional salience) reliably pull attention away from ongoing work, and why the ability to voluntarily resist capture varies across individuals and conditions. The DAN and VAN are not simply "top-down" and "bottom-up" in isolation — they are nodes in an ongoing negotiation over where attention is allocated.

This circuit-level understanding has direct translational implications. In **ADHD**, reduced prefrontal control over the VAN may explain why salient but task-irrelevant stimuli are disproportionately distracting. In hemispatial neglect following right parietal damage, the VAN re-orienting system is disrupted so that attention cannot be captured by left-field stimuli even when they are dramatically salient. Interventions that strengthen top-down DAN engagement — whether through cognitive training or stimulant medication's enhancement of prefrontal dopamine signaling — should in principle raise the threshold for VAN-mediated capture, improving the signal-to-noise ratio for voluntary attention.

