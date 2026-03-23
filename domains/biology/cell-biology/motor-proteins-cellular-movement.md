---
id: motor-proteins-cellular-movement
title: 'Motor Proteins: Molecular Motors'
domain: biology
course: cell-biology
prerequisites:
- id: cytoskeleton-cellular-framework
  type: hard
- id: atp-hydrolysis-and-free-energy
  type: hard
builds-toward:
- skeletal-muscle-contraction
tags:
- motor-protein
- myosin
- kinesin
stage: formal-systems
status: validated
---

# Motor Proteins: Molecular Motors

## Core Idea
Motor proteins are ATPases that convert chemical energy into mechanical work by 'walking' along cytoskeletal filaments. Myosin motors move along actin (driving muscle contraction and cytokinesis); kinesin and dynein move along microtubules (transporting organelles, positioning chromosomes). Each motor protein has a catalytic head hydrolyzing ATP, a mechanically sensitive neck translating energy into movement, and a cargo-binding tail.

## How It's Best Learned
Visualize the stepping mechanism: myosin head binds actin, pivots (using ATP energy), releases, detaches, resets. Measure velocities and processivity of different motors in single-molecule assays.

## Common Misconceptions
Motor proteins pull exclusively—many push. Myosin is only in muscle—it is involved in cytokinesis and intracellular transport. Energy is used to bind filament—energy is used after binding to produce power stroke.

## Questions

```yaml
- question: "A vesicle containing synaptic proteins must travel from a neuron's cell body to an axon terminal one meter away. Which motor protein and cytoskeletal track would accomplish this, and why can't diffusion do the job?"
  type: multiple-choice
  options:
    - "Dynein walking along actin filaments toward the minus end; diffusion is excluded from axons"
    - "Kinesin walking along microtubules toward the plus end; diffusion over meter-scale distances would take years"
    - "Myosin II walking along microtubules; myosin generates the most force per ATP"
    - "Kinesin walking along actin filaments; actin extends the full length of the axon"
  answer: 1
  explanation: "Kinesin is the anterograde motor that walks toward the plus end of microtubules — the cell periphery, including the axon tip. Microtubules, not actin, form the long-distance highway in axons, with their plus ends oriented toward the terminal. Diffusion at cellular temperatures can cover a few micrometers per second, but over one meter it would take years; directed motor transport covers it in days. Dynein moves in the opposite direction (retrograde, back to the cell body), and myosin walks along actin for local transport."

- question: "During the myosin power stroke, at which step does ATP hydrolysis actually provide energy for movement?"
  type: multiple-choice
  options:
    - "ATP binds to myosin, causing it to release from actin — ATP binding provides the detachment energy"
    - "ATP hydrolysis (ADP + Pi release) occurs while myosin is detached and re-cocks the head into the high-energy conformation; the power stroke fires when Pi is released after rebinding actin"
    - "ATP hydrolysis occurs as myosin pivots during the power stroke itself"
    - "Energy comes from the electrostatic attraction between myosin and actin, not from ATP"
  answer: 1
  explanation: "This is the key misconception addressed by the topic. ATP hydrolysis does not directly power the pivot — instead, it re-cocks the myosin head into a high-energy 'cocked' conformation while myosin is detached from actin. The power stroke (the pivot that moves actin) is driven by the release of inorganic phosphate (Pi) after the head rebinds actin, releasing the stored conformational energy. ATP binding (before hydrolysis) actually causes myosin to release from actin — it provides detachment, not movement."

- question: "Without motor proteins, large cells like neurons could not distribute organelles and vesicles effectively because diffusion alone is too slow over distances greater than a few micrometers."
  type: true-false
  answer: true
  explanation: "Diffusion is efficient over short distances (micrometers) but scales poorly — diffusion time scales as distance squared, so a 1,000-fold increase in distance means a 1,000,000-fold increase in time. A vesicle diffusing 1 meter down an axon would take years. Motor proteins on cytoskeletal tracks provide directed, active transport that covers the same distance in days. This is why large, polarized cells like neurons are absolutely dependent on motor proteins for their function."

- question: "Kinesin moves toward the minus end of microtubules, delivering cargo from the cell body toward the cell periphery."
  type: true-false
  answer: false
  explanation: "Kinesin moves toward the plus end of microtubules, which points toward the cell periphery. In axons, plus ends face the terminal, so kinesin performs anterograde transport (cell body → axon tip). Dynein moves toward the minus end (retrograde transport, axon tip → cell body). This directionality is determined by the motor's mechanochemical structure, not by cargo type."

- question: "Why is processivity — the ability to take many steps without detaching from the filament — especially important for kinesin, and how does kinesin's two-headed structure enable it?"
  type: short-answer
  answer: "Kinesin must transport cargo over long distances (up to a meter in axons) without dropping it. If kinesin detached after every few steps, cargo would be lost and delivery would fail. Kinesin's two heads alternate: while one head is bound to the microtubule, the other swings forward to the next binding site before the trailing head releases — a hand-over-hand mechanism that keeps at least one head attached at nearly all times. This coordination produces high processivity (hundreds of steps per run). Myosin II, by contrast, operates in large ensembles during muscle contraction where individual non-processivity is acceptable because many motors are always engaged."
  explanation: "Processivity is a functional requirement shaped by the task. Long-distance cargo transport demands processive motors; ensemble force generation (muscle contraction) can use non-processive ones. The two-headed coordination of kinesin is the structural solution to the processivity requirement, directly linking molecular structure to cellular function."
```

## Explainer

You already know that the cytoskeleton provides structural tracks — actin filaments and microtubules — and that ATP hydrolysis releases free energy the cell can harness. **Motor proteins** are the molecular machines that combine these two prerequisites: they grip cytoskeletal filaments and use ATP energy to walk along them, carrying cargo or generating force. They are, in effect, nanoscale engines running on chemical fuel.

The three major families each have a preferred track and direction. **Myosin** motors walk along actin filaments. The best-known example is muscle myosin II, which slides actin filaments past each other to shorten the sarcomere during contraction — but other myosins transport vesicles, help with cell crawling, and pinch the cell in half during cytokinesis. **Kinesin** motors walk along microtubules, generally toward the plus end (the cell periphery), carrying vesicles, organelles, and mRNA outward from the cell body. **Dynein** motors walk along microtubules in the opposite direction, toward the minus end (the cell center), hauling cargo inward and powering the beating of cilia and flagella.

The stepping mechanism follows a conserved cycle. Consider kinesin as an example: it has two globular **head domains**, each of which can bind both a microtubule and ATP. One head binds the microtubule and hydrolyzes ATP, which triggers a conformational change — the **neck linker** snaps forward, swinging the trailing head 16 nanometers ahead to the next binding site on the microtubule. The trailing head then binds, the leading head releases, and the cycle repeats. The result is a hand-over-hand walk, like a person walking on stepping stones, with each step consuming one ATP molecule. Kinesin is remarkably **processive** — a single molecule can take hundreds of steps without detaching, making it ideal for long-distance transport down an axon.

What makes motor proteins so important is that they solve a fundamental problem of cell biology: diffusion is too slow for directed transport over distances larger than a few micrometers. A vesicle diffusing randomly from the cell body to the tip of a one-meter neuron would take years to arrive. Kinesin walking along a microtubule delivers it in days. Without motor proteins, large cells simply could not function — organelles could not be positioned, chromosomes could not be segregated during division, and muscles could not contract. Every time you move a finger, billions of myosin motors are executing their power strokes in coordinated unison.
