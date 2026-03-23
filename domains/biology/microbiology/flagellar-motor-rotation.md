---
id: flagellar-motor-rotation
title: Bacterial Flagellar Motor and Rotation Mechanics
domain: biology
course: microbiology
prerequisites:
- id: bacterial-cell-structure
  type: hard
- id: motor-proteins-cellular-movement
  type: soft
builds-toward:
- chemotaxis-signaling-phosphorylation
tags:
- flagella
- motility
- motor-proteins
stage: formal-systems
status: draft
---

# Bacterial Flagellar Motor and Rotation Mechanics

## Core Idea
The bacterial flagellar motor is powered by the proton-motive force across the cell membrane, rotating the flagellar filament at speeds up to 100,000 rpm. The motor consists of a rotor (membrane-embedded proteins) and stator (FliG, FliM, FliN proteins) that interact with the potential across the membrane, converting electrochemical energy into mechanical rotation.

## Questions

```yaml
- question: "A bacteriologist treats E. coli with a drug that collapses the proton gradient across the inner membrane without affecting intracellular ATP levels. What effect would you predict on flagellar motility?"
  type: multiple-choice
  options:
    - "Motility continues normally because the flagellar motor runs on ATP, not proton flow"
    - "Motility slows slightly but is maintained by the remaining membrane potential"
    - "Motility stops because the flagellar motor is powered by proton-motive force, and eliminating the proton gradient removes its energy source"
    - "The bacterium switches to using NADH directly to power the motor as a backup energy source"
  answer: 2
  explanation: "The bacterial flagellar motor is directly powered by the proton-motive force (PMF) — the electrochemical gradient of protons across the inner membrane — not by ATP hydrolysis. Protons flow through the stator complex (MotA/MotB channels) and their passage exerts force on the rotor's FliG ring, generating torque. Collapsing the proton gradient eliminates the driving force for this ion flow, stopping the motor entirely even if ATP levels are unaffected. This contrasts with eukaryotic motor proteins like myosin and kinesin, which are ATPases and would be inhibited by ATP depletion rather than by ion gradient collapse."

- question: "When E. coli flagellar motors switch from counterclockwise (CCW) to clockwise (CW) rotation, what happens to the bacterium's movement and why?"
  type: multiple-choice
  options:
    - "The bacterium swims faster in the forward direction because CW rotation is more efficient"
    - "The bacterium reverses direction smoothly, like a car shifting into reverse"
    - "The bacterium tumbles randomly because CW rotation causes the flagellar bundle to fly apart, disrupting coordinated propulsion"
    - "The flagella retract into the cell during CW rotation to prepare for a new direction"
  answer: 2
  explanation: "In E. coli, multiple flagella bundle together into a coherent helical propeller only when all motors spin counterclockwise. This bundle pushes the cell forward in a 'run.' When one or more motors switch to clockwise rotation, the flagella cannot maintain the bundle geometry — they fly apart and the cell tumbles, reorienting randomly. When the motors switch back to CCW, the flagella rebundle and the cell swims forward in a new direction. This run-and-tumble mechanism is how bacteria navigate chemical gradients (chemotaxis): they tumble less frequently when moving toward attractants, and more frequently when moving away."

- question: "The bacterial flagellar motor is described as a 'true rotary motor' because the entire flagellar filament rotates continuously around its own axis relative to the cell body."
  type: true-false
  answer: true
  explanation: "Unlike eukaryotic motor proteins (myosin, kinesin, dynein), which are linear motors that generate force by stepping along a track, the bacterial flagellar motor produces continuous rotational torque. The rotor spins relative to the stator, and this rotation is transmitted through the hook to the flagellar filament, which rotates like a propeller. This is genuine rotation — the filament turns continuously, not in a reciprocating back-and-forth motion. This is remarkable because most biological motion-generating systems produce linear forces; the flagellar motor is one of the very few true biological rotary engines."

- question: "The bacterial flagellar motor operates on the same basic principle as eukaryotic motor proteins: it hydrolyzes ATP to drive conformational changes that generate mechanical force."
  type: true-false
  answer: false
  explanation: "The bacterial flagellar motor uses proton-motive force, not ATP hydrolysis. Protons flow down their electrochemical gradient through the MotA/MotB stator channels, and this ion flow drives conformational interactions between the stator and the FliG ring of the rotor, generating torque. ATP is not the direct energy currency of the motor. This makes the flagellar motor mechanistically distinct from myosin (ATP hydrolysis + actin filament), kinesin (ATP hydrolysis + microtubule), and dynein (ATP hydrolysis + microtubule). Some bacteria use sodium ions instead of protons, further demonstrating that ion gradients — not ATP — are the operating principle."

- question: "Explain why the bacterial flagellar motor is considered a 'true rotary engine' and how this distinguishes it mechanistically from the motor proteins found in eukaryotic cells."
  type: short-answer
  answer: "The bacterial flagellar motor generates continuous rotational torque: the rotor (including the C ring with FliG, FliM, FliN) spins relative to the stator (MotA/MotB) embedded in the cell membrane, and this rotation is transmitted through the hook to the flagellar filament, which turns like a propeller. The energy source is proton-motive force — protons flowing through stator channels drive the rotation by exerting successive forces on the rotor ring. Eukaryotic motor proteins (myosin, kinesin, dynein) are linear motors: they hydrolyze ATP to produce conformational changes that generate linear stepping along cytoskeletal tracks (actin or microtubules). They do not rotate; they walk. The flagellar motor is one of the only true biological rotary engines, operating on an entirely different principle."
  explanation: "The distinction matters for understanding the diversity of biological machines. Linear motors convert chemical energy into linear mechanical displacement; the flagellar motor converts electrochemical energy (ion gradient) directly into rotational motion. The motor can also reverse direction in milliseconds (by switching the interaction geometry between stator and rotor), dynamically recruit additional stator units to increase torque, and achieve speeds exceeding 1,000 revolutions per second — feats that have no direct parallel in the eukaryotic cytoskeletal motor repertoire."
```

## Explainer

From your study of bacterial cell structure, you know that many bacteria possess **flagella** — long, helical filaments that extend from the cell surface and propel the bacterium through liquid environments. From your understanding of motor proteins, you know that biological movement requires molecular machines that convert chemical or electrochemical energy into mechanical work. The bacterial flagellar motor is one of the most remarkable examples of such a machine: a true rotary engine, fundamentally different from the linear motors (myosin, kinesin, dynein) found in eukaryotic cells.

The motor is built from about 25 different proteins assembled into a structure that spans the cell envelope. At its core is the **rotor**, a set of ring-shaped protein complexes embedded in the inner membrane and peptidoglycan layer. The C ring (composed of **FliG**, **FliM**, and **FliN**) sits on the cytoplasmic face of the membrane and functions as both the rotary element and the switching apparatus that controls rotational direction. Surrounding the rotor are multiple copies of the **stator** complex (MotA/MotB in most species), which are anchored to the peptidoglycan and form channels through the inner membrane. Each stator unit acts as a proton (H⁺) channel: protons flowing down their electrochemical gradient — the **proton-motive force (PMF)** you encountered in studies of membrane energetics — pass through the MotA/MotB channel and exert force on FliG in the rotor ring. The sequential interaction of protons with multiple stator units around the rotor's circumference generates continuous torque, spinning the rotor like a turbine driven by ion flow.

The flagellar filament is connected to the motor through a **hook** — a flexible universal joint that transmits the rotor's rotation to the rigid helical filament extending into the surrounding medium. When the motor spins counterclockwise (in *E. coli*), multiple flagella bundle together into a coherent helical propeller and the cell swims smoothly forward in a "**run**." When the motor switches to clockwise rotation, the flagellar bundle flies apart and the cell **tumbles**, randomly reorienting before the next run. This run-and-tumble behavior is the physical basis of bacterial movement, and the switching mechanism in the C ring is directly controlled by the chemotaxis signaling system that detects chemical gradients.

What makes this motor astonishing is its performance. It can spin at speeds exceeding **1,000 revolutions per second** in some species, it reverses direction in less than a millisecond, and its energy efficiency approaches nearly 100% — far exceeding any human-engineered rotary motor. The motor can also dynamically recruit or release stator units to adjust torque output in response to changes in viscous load. The entire assembly is built through a precisely ordered self-assembly process in which proteins are exported through the hollow core of the growing structure. The bacterial flagellar motor demonstrates that evolution can produce true rotary machinery at the nanoscale, operating on principles — ion-driven turbines, modular stator recruitment, reversible switching — that have no equivalent in the eukaryotic motor protein repertoire.
