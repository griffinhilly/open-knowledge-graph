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

## Explainer

From your study of bacterial cell structure, you know that many bacteria possess **flagella** — long, helical filaments that extend from the cell surface and propel the bacterium through liquid environments. From your understanding of motor proteins, you know that biological movement requires molecular machines that convert chemical or electrochemical energy into mechanical work. The bacterial flagellar motor is one of the most remarkable examples of such a machine: a true rotary engine, fundamentally different from the linear motors (myosin, kinesin, dynein) found in eukaryotic cells.

The motor is built from about 25 different proteins assembled into a structure that spans the cell envelope. At its core is the **rotor**, a set of ring-shaped protein complexes embedded in the inner membrane and peptidoglycan layer. The C ring (composed of **FliG**, **FliM**, and **FliN**) sits on the cytoplasmic face of the membrane and functions as both the rotary element and the switching apparatus that controls rotational direction. Surrounding the rotor are multiple copies of the **stator** complex (MotA/MotB in most species), which are anchored to the peptidoglycan and form channels through the inner membrane. Each stator unit acts as a proton (H⁺) channel: protons flowing down their electrochemical gradient — the **proton-motive force (PMF)** you encountered in studies of membrane energetics — pass through the MotA/MotB channel and exert force on FliG in the rotor ring. The sequential interaction of protons with multiple stator units around the rotor's circumference generates continuous torque, spinning the rotor like a turbine driven by ion flow.

The flagellar filament is connected to the motor through a **hook** — a flexible universal joint that transmits the rotor's rotation to the rigid helical filament extending into the surrounding medium. When the motor spins counterclockwise (in *E. coli*), multiple flagella bundle together into a coherent helical propeller and the cell swims smoothly forward in a "**run**." When the motor switches to clockwise rotation, the flagellar bundle flies apart and the cell **tumbles**, randomly reorienting before the next run. This run-and-tumble behavior is the physical basis of bacterial movement, and the switching mechanism in the C ring is directly controlled by the chemotaxis signaling system that detects chemical gradients.

What makes this motor astonishing is its performance. It can spin at speeds exceeding **1,000 revolutions per second** in some species, it reverses direction in less than a millisecond, and its energy efficiency approaches nearly 100% — far exceeding any human-engineered rotary motor. The motor can also dynamically recruit or release stator units to adjust torque output in response to changes in viscous load. The entire assembly is built through a precisely ordered self-assembly process in which proteins are exported through the hollow core of the growing structure. The bacterial flagellar motor demonstrates that evolution can produce true rotary machinery at the nanoscale, operating on principles — ion-driven turbines, modular stator recruitment, reversible switching — that have no equivalent in the eukaryotic motor protein repertoire.
