---
id: skeletal-muscle-anatomy-and-contraction
title: Skeletal Muscle Anatomy and Contraction
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: skeletal-joints-and-movement-mechanics
  type: hard
- id: skeletal-muscle-contraction
  type: soft
- id: atp-hydrolysis-and-free-energy
  type: soft
builds-toward:
- smooth-muscle-structure-and-distribution
- cardiac-muscle-anatomy-and-properties
tags:
- muscle
- contraction
- actin
- myosin
- sarcomere
stage: formal-systems
status: draft
---

# Skeletal Muscle Anatomy and Contraction

## Core Idea
Skeletal muscle is organized into bundles (fascicles) of fibers, each containing myofibrils made of sarcomeres. Sarcomeres contain thick filaments (myosin) and thin filaments (actin). During contraction, myosin heads pull actin, shortening the sarcomere. This sliding filament mechanism explains how muscles generate force.

## Questions

```yaml
- question: "During a muscle contraction that shortens the sarcomere, what happens to the lengths of the individual actin and myosin filaments?"
  type: multiple-choice
  options:
    - "Both filaments shorten as the protein molecules compress under the contractile force"
    - "Myosin shortens by coiling, while actin remains the same length"
    - "Actin filaments shorten as they are reeled in by myosin cross-bridges"
    - "Neither filament changes length — the filaments slide past each other, increasing their overlap"
  answer: 3
  explanation: "This is the central claim of the sliding filament model: the filaments themselves do not shorten. Myosin cross-bridges attach to actin and pull the actin filaments toward the center of the sarcomere (M-line), increasing filament overlap while the Z-lines move closer together. The sarcomere shortens; the filament lengths are unchanged. This can be verified microscopically: the A-band (where myosin resides) stays the same width during contraction, while the I-band and H-zone narrow as overlap increases."

- question: "A person dies and their muscles enter rigor mortis — a rigid, locked state. What explains this at the molecular level of the cross-bridge cycle?"
  type: multiple-choice
  options:
    - "Calcium floods out of the sarcoplasmic reticulum and cannot be pumped back, locking troponin in the activated state indefinitely"
    - "Actin filaments polymerize further after death, rigidly linking adjacent sarcomeres"
    - "Without ATP, myosin heads cannot detach from actin after completing the power stroke, freezing cross-bridges in the attached state"
    - "ATP floods the cell after death, causing all available myosin heads to simultaneously undergo the power stroke"
  answer: 2
  explanation: "The cross-bridge cycle requires ATP for two distinct purposes: (1) to cock the myosin head into its high-energy configuration before binding actin, and (2) to allow the myosin head to DETACH from actin after the power stroke. Without ATP, detachment cannot occur — myosin heads remain rigidly attached to actin filaments. This produces the characteristic stiffness of rigor mortis. Muscle relaxation thus requires ATP not just for contraction but as a 'release factor' for every cross-bridge."

- question: "Calcium ions initiate muscle contraction by binding directly to myosin heads, enabling them to reach and attach to actin."
  type: true-false
  answer: false
  explanation: "Calcium acts on the THIN filament, not on myosin. At rest, tropomyosin physically blocks myosin-binding sites on actin. When calcium is released from the sarcoplasmic reticulum, it binds to troponin (a protein associated with tropomyosin on the actin filament), causing a conformational change that shifts tropomyosin away from the binding sites. This exposes the sites, allowing myosin heads — which were already in their high-energy cocked state — to bind. The regulation system gates access to actin, not activity of myosin."

- question: "ATP is required for both the active (power stroke) phase and the relaxation phase of the cross-bridge cycle."
  type: true-false
  answer: true
  explanation: "ATP plays two distinct roles in the cross-bridge cycle. First, it is hydrolyzed to ADP + Pi to cock the myosin head into its high-energy configuration — this provides the energy for the subsequent power stroke. Second, a NEW ATP molecule must bind to myosin AFTER the power stroke to allow the head to detach from actin. Without this second ATP, detachment cannot occur (as in rigor mortis). Relaxation also requires ATP to actively pump calcium back into the sarcoplasmic reticulum via the SERCA pump."

- question: "Explain why the sliding filament model means that sarcomere shortening does not require protein filaments to shorten. What does change during contraction, and how does filament sliding produce force?"
  type: short-answer
  answer: "In the sliding filament model, actin and myosin filaments maintain constant length throughout contraction. What changes is the degree of overlap between them. Myosin heads (cross-bridges) bind to actin, then perform a power stroke — rotating approximately 70° to pull actin toward the center of the sarcomere. This increases overlap and draws the Z-lines (which anchor actin) closer together, shortening the sarcomere. Hundreds of cross-bridges cycling repeatedly per second across thousands of sarcomeres in series generate macroscopic shortening and force."
  explanation: "The sliding filament model resolved a key controversy in mid-20th century muscle research. It predicts specific microscopic observations: the A-band (myosin) width is constant during contraction; the I-band (actin without overlap) and H-zone (myosin without overlap) both narrow as overlap increases. These predictions were confirmed by electron microscopy, providing strong evidence for the model. The key insight is that mechanical work comes from the cross-bridge power stroke — a conformational change in the myosin molecule — not from filament shortening."
```

## Explainer

From your study of skeletal joints and movement mechanics, you know that muscles attach to bones via tendons and that contraction produces force across joints. But understanding *how* a muscle fiber generates that force requires zooming in through several levels of organization, each level adding a layer of structural logic. Skeletal muscle is organized hierarchically: the whole muscle is wrapped in connective tissue (epimysium) and divided into **fascicles** (bundles), each wrapped in perimysium. Within each fascicle are individual **muscle fibers** — single multinucleated cells that can span the entire length of the muscle. Each fiber is packed with **myofibrils**: cylindrical organelles that run parallel to the fiber's long axis and are the contractile units.

Myofibrils reveal the fundamental repeating unit of contraction: the **sarcomere**. A sarcomere is the segment between two Z-lines (or Z-discs), which anchor the thin filaments. Looking at a sarcomere under a microscope, you see alternating light (I-band) and dark (A-band) regions — this is the striated appearance characteristic of skeletal and cardiac muscle. The dark A-band is where thick filaments (**myosin**) reside; the lighter H-zone in the center is where thick filaments exist without thin filament overlap; the Z-line anchors thin filaments (**actin** plus regulatory proteins troponin and tropomyosin). During contraction, the Z-lines move closer together — the sarcomere shortens — but the filament lengths themselves do not change. This is the core insight of the **sliding filament model**.

The molecular mechanism driving sliding is the **cross-bridge cycle**, which depends on ATP — connecting to your prerequisite knowledge of ATP hydrolysis. A myosin head binds ATP, which is hydrolyzed to ADP + Pi; this cocks the head into a high-energy configuration. The head then binds to actin (forming a **cross-bridge**), releases Pi, and performs the **power stroke** — rotating approximately 70° to pull the actin filament toward the sarcomere center. ADP is released. A new ATP molecule must bind for the myosin head to detach; without ATP (as in rigor mortis), myosin heads stay locked to actin. Hundreds of cross-bridge cycles per second across thousands of sarcomeres in series and parallel produce macroscopic muscle force and shortening.

The regulation layer explains why muscles don't contract spontaneously. At rest, **tropomyosin** physically blocks the myosin-binding sites on actin filaments. Calcium ions released from the sarcoplasmic reticulum (triggered by a motor neuron action potential via the T-tubule system) bind to **troponin**, which undergoes a conformational change that shifts tropomyosin, uncovering the binding sites and allowing cross-bridge cycling to begin. When the neural signal ceases, calcium is actively pumped back into the sarcoplasmic reticulum, tropomyosin re-covers the binding sites, and the muscle relaxes. This calcium-dependent regulation means that force production is precisely tunable: the frequency and pattern of motor neuron firing, combined with the number of motor units recruited, determine how much force a muscle generates — from a gentle grip to a maximal lift.
