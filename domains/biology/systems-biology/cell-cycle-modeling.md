---
id: cell-cycle-modeling
title: Cell Cycle Modeling
domain: biology
course: systems-biology
prerequisites:
- id: ode-models-in-biology
  type: hard
- id: boolean-network-models
  type: hard
- id: mitosis
  type: soft
builds-toward: []
tags:
- cell-cycle
- cyclin-CDK
- bistability
- checkpoint
- oscillator
stage: expert
status: validated
---
# Cell Cycle Modeling

## Core Idea
Cell cycle modeling applies dynamical systems theory to understand how cells progress through G1, S, G2, and M phases in a robust, irreversible, and precisely timed sequence. The core machinery — cyclin-CDK complexes regulated by synthesis, degradation, phosphorylation, and inhibitor binding — creates a biochemical oscillator with embedded bistable switches that ensure irreversible phase transitions. John Tyson and Bela Novak pioneered ODE models showing that the G1/S and metaphase/anaphase transitions are driven by bistable switches (hysteresis ensures commitment once a threshold is crossed), while the overall cycle is an autonomous oscillation driven by periodic cyclin accumulation and APC/C-mediated degradation. Boolean models by Faure et al. showed that the cell cycle's sequential logic can be captured without kinetic parameters.

## Questions

```yaml
- question: "The G1/S transition is modeled as a bistable switch. What does bistability mean functionally for cell cycle commitment?"
  type: multiple-choice
  options:
    - "The cell gradually eases into S phase over many hours with no sharp transition point"
    - "Once the cell crosses the restriction point, positive feedback between cyclin E-CDK2 and Rb phosphorylation creates a self-reinforcing loop that drives irreversible commitment to S phase — the cell cannot return to G1 without a drastic perturbation"
    - "The cell alternates rapidly between G1 and S phase before settling"
    - "Bistability means the cell can be in either G1 or S phase randomly at any time"
  answer: 1
  explanation: "Bistability creates two stable states (G1 and S-committed) separated by an unstable threshold. At low cyclin E levels, Rb represses E2F, keeping cyclin E low — a stable G1 state. When growth factor signaling pushes cyclin E above a threshold, cyclin E-CDK2 phosphorylates Rb, releasing E2F, which drives more cyclin E expression — positive feedback pushes the system to the high-cyclin-E stable state (S commitment). The hysteresis inherent in bistable switches means that even if the growth signal is removed after crossing the threshold, the cell remains committed. This irreversibility is essential: once DNA replication begins, returning to G1 would be catastrophic."

- question: "The cell cycle can be modeled either as a single autonomous oscillator or as a series of linked bistable switches. These two views are contradictory."
  type: true-false
  answer: false
  explanation: "These views are complementary, not contradictory. The Novak-Tyson framework unifies them: the cell cycle is an oscillator composed of linked bistable switches. Each phase transition (G1/S, G2/M, metaphase/anaphase) is a bistable switch that ensures irreversible commitment. But the switches are coupled so that completing one transition sets up the conditions for the next — cyclin accumulation drives entry into a phase, and APC/C-mediated degradation resets the system for the next phase. The result is an autonomous oscillation where each cycle passes through a sequence of irreversible transitions. Bistable switches provide robustness to noise at each transition; the oscillatory coupling provides the periodic timing."

- question: "What insight did mathematical modeling reveal about cell cycle control that purely experimental approaches had not established?"
  type: short-answer
  answer: "Mathematical modeling revealed that the cell cycle transitions are bistable switches with hysteresis — once the transition is triggered, the system commits irreversibly and cannot return to the previous phase without a large perturbation. Experimental biology had identified the molecular components (cyclins, CDKs, CKIs, APC/C) and many of their interactions, but the dynamical consequence of these interactions — that positive feedback loops create bistability and that this bistability explains the all-or-nothing, irreversible character of phase transitions — was not apparent from the molecular parts list. The models made quantitative predictions (e.g., the threshold cyclin concentration for entry into mitosis, the size of the hysteresis loop) that were subsequently confirmed experimentally."
  explanation: "Pomerening et al. (2003) experimentally demonstrated hysteresis in Xenopus egg extract CDK1 activation — exactly as Novak-Tyson models predicted. The system required a higher cyclin concentration to activate CDK1 than to maintain it, confirming bistability. This bridging of modeling prediction and experimental validation is a paradigm of how systems biology generates biological insight."
```

## Explainer

The cell cycle is one of the most important and best-studied oscillatory processes in biology. Every dividing cell must replicate its DNA exactly once, segregate chromosomes accurately, and divide — in that order, with no step skipped or repeated. The molecular machinery that ensures this precise sequence involves dozens of interacting proteins, including cyclins (whose levels oscillate), cyclin-dependent kinases (CDKs, whose activity depends on cyclin binding and post-translational modifications), CDK inhibitors (CKIs), and the anaphase-promoting complex/cyclosome (APC/C, which targets cyclins for degradation). Understanding how this molecular network generates reliable, precisely timed oscillations is a central question in systems biology.

**ODE models** of the cell cycle, pioneered by John Tyson, Bela Novak, and colleagues, revealed that the network's core design principle is **linked bistable switches driving an oscillator**. The G1/S transition is controlled by a bistable switch involving cyclin E-CDK2, Rb, and E2F. In G1, Rb represses E2F, keeping cyclin E levels low — a stable resting state. Growth factor signaling gradually increases cyclin D-CDK4/6, which partially phosphorylates Rb. Once cyclin E-CDK2 activity crosses a critical threshold, a positive feedback loop engages: cyclin E-CDK2 hyper-phosphorylates Rb, fully releasing E2F, which drives more cyclin E transcription. The system flips to a high-cyclin-E state and commits to S phase. The hysteresis of the bistable switch ensures this commitment is irreversible — even if the growth signal is removed, the cell stays committed.

A similar bistable switch governs the **G2/M transition** (cyclin B-CDK1 activation through mutual antagonism between CDK1 and Wee1/Cdc25) and the **metaphase/anaphase transition** (APC/C activation). The cell cycle oscillation arises because these switches are coupled: S-phase completion triggers cyclin B accumulation, which triggers the G2/M switch; mitotic exit requires APC/C-mediated cyclin B destruction, which resets the system to a state competent for the next G1. The alternation between cyclin accumulation and APC/C-mediated destruction drives the oscillation, while the bistable switches at each transition ensure irreversible, all-or-nothing phase commitment.

**Boolean models** complement the ODE approach by capturing the logical structure of cell cycle regulation without kinetic parameters. Faure et al. built a Boolean model of the mammalian cell cycle where each regulatory protein is ON or OFF and update rules encode the regulatory logic. The model correctly reproduces the sequential activation of cyclins (D, E, A, B), the ordered phase transitions, and the existence of a stable G1 quiescent state. The fact that a parameter-free logical model captures the essential cell cycle sequence demonstrates that the qualitative wiring — which proteins activate or inhibit which — is sufficient to explain the cell cycle's ordered progression. The quantitative ODE models add timing, explain thresholds, and predict the consequences of parameter perturbations, but the qualitative logic is the skeleton on which quantitative dynamics are draped.
