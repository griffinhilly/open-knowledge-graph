---
id: motor-planning-premotor-cortex
title: 'Motor Planning: Premotor and Supplementary Motor Cortex'
domain: psychology
course: biological-psychology
prerequisites:
- id: primary-motor-cortex-motor-representation
  type: hard
- id: dorsolateral-prefrontal-cortex-cognitive-control
  type: soft
- id: motor-cortex
  type: hard
builds-toward:
- basal-ganglia-selection-habits
- cerebellum-coordination-learning
tags:
- motor-systems
- planning
- cognition
stage: advanced
status: validated
---

# Motor Planning: Premotor and Supplementary Motor Cortex

## Core Idea
Premotor cortex and supplementary motor cortex (SMA) plan and sequence motor actions before M1 execution. These regions integrate sensory information, motivational signals, and goal representations to select and organize movement sequences. Damage to premotor areas produces apraxia (inability to execute learned motor sequences) despite preserved M1 function, demonstrating the distinction between planning and execution.

## Questions

```yaml
- question: "A patient sustains a stroke affecting premotor areas. She has full muscle strength, intact reflexes, and normal M1 function — yet she cannot pantomime brushing her teeth when asked. Which best explains this?"
  type: multiple-choice
  options:
    - "M1 damage has disrupted the somatotopic map, preventing muscle recruitment"
    - "Premotor/SMA damage has disrupted the planning system that sequences learned motor acts, even though execution capacity is intact"
    - "Cerebellar damage has impaired coordination of her hand movements"
    - "Spinal cord involvement has blocked the efferent signal to her arm muscles"
  answer: 1
  explanation: "This scenario describes apraxia — the hallmark of premotor damage. Because M1 and the muscles are intact, the patient can move her arm; what she cannot do is assemble and dispatch a purposeful, learned sequence. This dissociation is the clearest evidence that planning and execution are anatomically separable: PMC/SMA builds the motor program and sends it to M1; M1 executes it. Damage at the planning stage produces intact movement capacity but broken sequencing."

- question: "The readiness potential (Bereitschaftspotential) is a slow buildup of neural activity that appears up to a second before a voluntary movement begins. Which region is its primary source, and what does this tell us?"
  type: multiple-choice
  options:
    - "Primary motor cortex (M1) — it starts activating well before the movement to allow muscle warm-up"
    - "Supplementary motor area (SMA) — it reflects preparation for self-initiated sequences before M1 begins firing"
    - "Dorsolateral prefrontal cortex (DLPFC) — it generates goals that must precede any motor output"
    - "Cerebellum — it predicts the sensory consequences of movement before it occurs"
  answer: 1
  explanation: "The SMA is particularly active for internally-initiated, self-generated movements. The readiness potential originates largely in SMA (and to a lesser degree premotor cortex), building for hundreds of milliseconds before M1 begins firing and before the muscle contracts. This proves that the 'decision' to move and the preparation of its sequence happen upstream of execution — in the SMA — not simultaneously with it."

- question: "Apraxia results from damage to the primary motor cortex and is characterized by muscle weakness."
  type: true-false
  answer: false
  explanation: "Apraxia results from premotor or SMA damage, not M1 damage. By definition, a patient with apraxia has intact M1 function and normal muscular strength — they can move, but they cannot execute purposeful learned sequences. M1 damage produces paresis (weakness or paralysis). The distinction between these syndromes maps directly onto the planning-versus-execution architecture: apraxia = broken plan; paresis = broken execution."

- question: "The supplementary motor area (SMA) shows increased neural activity before self-initiated movements begin, even before primary motor cortex activation."
  type: true-false
  answer: true
  explanation: "This is well-established by both recording studies and the readiness potential. SMA activity ramps up hundreds of milliseconds before M1 fires and before any overt movement, reflecting its role in preparing and initiating internally generated motor sequences. PMC, by contrast, is more active for externally cued movements."

- question: "Explain why the premotor cortex and SMA are necessary for skilled voluntary movement, given that the primary motor cortex already contains a complete somatotopic map of the body."
  type: short-answer
  answer: "M1's somatotopic map tells the motor system *how* to activate individual muscles, but not *which* muscles to recruit, *in what order*, or *toward what goal*. PMC and SMA translate higher-level intentions and goal representations (passed down from DLPFC) into organized motor sequences that are then sent to M1 for execution. Without this planning stage, M1 would have no coherent instruction to execute — individual muscle movements would be possible but purposeful sequencing would be impossible."
  explanation: "The motor hierarchy (DLPFC → PMC/SMA → M1 → spinal cord) reflects successive levels of abstraction: goals become sequences, sequences become muscle commands. M1 alone is like a piano that can play any note but has no score. PMC/SMA is the conductor who selects the notes, their order, and their timing. Apraxia is what happens when the conductor is incapacitated but the piano is still functional."
```

## Explainer

You already know that the primary motor cortex (M1) contains a topographic map of the body — stimulate a specific point and a specific muscle contracts. But knowing *which* muscles to recruit, in *what order*, and toward *what goal* requires more than M1. That preparatory work is the job of the **premotor cortex (PMC)** and **supplementary motor area (SMA)**, two regions that sit just anterior to M1 and function as the choreographers of movement before execution begins.

Think of M1 as the orchestra playing the notes, and PMC/SMA as the conductor who has already decided the tempo, order, and phrasing. The SMA is particularly involved in **self-initiated sequences** — movements that arise from internal intention rather than external cues. When you decide to tap out a rhythm from memory, SMA is highly active even before movement begins; recording studies in monkeys and humans show a buildup of electrical activity called the **readiness potential** (Bereitschaftspotential) up to a second before the movement itself occurs. The PMC, by contrast, is more involved in **externally guided actions**, where a sensory cue (a visual target, a verbal instruction) triggers a learned response.

The clearest evidence that planning and execution are distinct comes from a neurological syndrome called **apraxia**. A patient with damage to premotor areas may have full muscular strength and intact M1 function — they can move their limbs — yet they cannot perform learned, purposeful sequences on command. Asked to pantomime using a toothbrush, they make fumbling, incoherent movements. The motor program itself exists in M1, but the system that assembles and dispatches it is disrupted. This dissociation maps cleanly onto the planning-versus-execution architecture: premotor damage breaks the plan; M1 damage breaks the execution. Your knowledge of the motor cortex's somatotopic organization makes this make sense — M1 knows *how* to fire muscle groups, but it needs upstream regions to tell it *when* and *in what sequence*.

Your soft prerequisite — dorsolateral prefrontal cortex and cognitive control — adds an important layer. DLPFC communicates goal representations (what you are trying to achieve) downward to premotor areas, which then translate those goals into motor sequences. This top-down connection explains why motor actions can be flexibly reorganized in novel contexts or overridden when goals change. The full motor hierarchy thus runs: DLPFC (goal) → PMC/SMA (plan and sequence) → M1 (execute) → spinal cord (muscle). Each stage converts a more abstract representation into a more concrete motor command, a principle called **hierarchical motor control**.
