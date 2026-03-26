---
id: bacterial-flagella-and-chemotaxis
title: Bacterial Flagella, Motility, and Chemotaxis
domain: biology
course: microbiology
prerequisites:
- id: bacterial-cell-structure
  type: hard
- id: cell-signaling-intro
  type: soft
- id: bacterial-flagella-pili-motility-adhesion
  type: soft
builds-toward:
- bacterial-virulence-and-disease-mechanisms
- microbial-ecology-biogeochemical-cycling
tags:
- motility
- flagella
- chemotaxis
- cell-signaling
stage: formal-systems
status: validated
---
# Bacterial Flagella, Motility, and Chemotaxis

## Core Idea
Bacterial flagella are rigid, helical protein filaments composed of flagellin that rotate at speeds up to 100,000 rpm, powered by a proton gradient across the cell membrane. This flagellar motor enables bacterial movement up to 60 μm/s. Chemotaxis allows bacteria to navigate chemical gradients by modulating rotation direction: tumbling (counterclockwise rotation) for random reorientation and smooth runs (clockwise) toward attractants.

## Questions

```yaml
- question: "A single E. coli cell is placed in a solution where glucose concentration is uniform but rising steadily everywhere. Despite swimming in any random direction, the cell runs longer and tumbles less. What explains this?"
  type: multiple-choice
  options:
    - "The cell senses a spatial concentration gradient across its body length and swims toward the higher-concentration end"
    - "The cell detects a temporal increase in glucose concentration and suppresses tumbling regardless of swimming direction"
    - "Higher glucose provides more energy to the flagellar motor, increasing rotation speed and reducing tumble frequency"
    - "Uniform glucose saturates all chemoreceptors symmetrically, locking the flagellar motor in the CCW (run) state"
  answer: 1
  explanation: "Bacteria are too small to detect spatial gradients — the concentration difference across a single cell is far below noise threshold. Instead, chemotaxis is a temporal comparison: the cell compares current attractant concentration to what it was a few seconds ago. A rising concentration signal (regardless of direction) is interpreted as 'swimming productively' and suppresses tumbling. The adaptation system (CheR/CheB) resets the baseline after a few seconds, which is why this is a comparison to the recent past rather than an absolute concentration measurement."

- question: "In E. coli chemotaxis, when an attractant binds to membrane chemoreceptors, the downstream signaling sequence is:"
  type: multiple-choice
  options:
    - "CheA activity is inhibited → less phospho-CheY → less clockwise (CW) flagellar rotation → longer runs"
    - "CheA activity is increased → more phospho-CheY → less CW flagellar rotation → longer runs"
    - "CheA activity is inhibited → less phospho-CheY → more CW flagellar rotation → more tumbles"
    - "CheY is directly activated by the attractant → flagellar bundle dissociates → tumble"
  answer: 0
  explanation: "The signaling logic is: attractant binding → inhibit CheA kinase → reduce phosphorylation of CheY → less phospho-CheY at the motor switch → less CW rotation → less tumbling → longer runs. Phospho-CheY is the 'tumble signal' — when it binds the flagellar motor switch, it promotes CW rotation and bundle dispersal. Attractants suppress CheA, drain the phospho-CheY pool, and the motor defaults to CCW (run). This inverted logic (less signal = more running) ensures that the cell runs *toward* attractants and tumbles *away* from repellents."

- question: "The bacterial flagellum generates thrust using the same bending and undulating mechanism as eukaryotic flagella, differing mainly in its energy source (proton motive force instead of ATP)."
  type: true-false
  answer: false
  explanation: "Bacterial and eukaryotic flagella are completely unrelated in structure and mechanism — a classic example of convergent evolution for a similar function. Bacterial flagella are rigid, helical filaments that rotate like propellers, driven by a rotary motor powered by proton flow. Eukaryotic flagella (and cilia) contain a '9+2' microtubule axoneme and generate movement through dynein-powered sliding of microtubule doublets — a bending/undulating mechanism driven by ATP hydrolysis. They share only the word 'flagellum' and the broad function of motility."

- question: "The CheR/CheB receptor methylation cycle allows bacteria to respond to changes in attractant concentration rather than absolute concentration levels, enabling navigation of gradients across a wide dynamic range."
  type: true-false
  answer: true
  explanation: "This adaptation mechanism is essential for robust chemotaxis. CheR continuously methylates MCPs (increasing their activity), while CheB (activated by phospho-CheA) demethylates them (reducing activity). After a step-change in attractant concentration, the system responds transiently and then adapts back to baseline behavior through this methylation feedback — regardless of the new absolute concentration. This means bacteria can continue responding to further increases even after adapting to a high background, allowing navigation across concentration ranges spanning many orders of magnitude."

- question: "Why can't bacteria sense chemical gradients by comparing concentrations at their front versus their back, and how do they achieve directed movement toward attractants instead?"
  type: short-answer
  answer: "A typical bacterium is only 1–2 micrometers long. The difference in attractant concentration between the front and back of the cell is far too small to detect against the noise of molecular diffusion — there is no meaningful spatial gradient signal across that distance. Instead, bacteria use temporal sensing: as they swim, they compare the current concentration to what it was a few seconds ago using the receptor methylation adaptation system as a 'molecular memory.' If concentration has increased, they suppress tumbling and keep running; if it has decreased, they tumble and randomly reorient. This biased random walk effectively navigates gradients using time rather than space."
  explanation: "This solution is elegant precisely because it converts a spatial problem (where is the food?) into a temporal problem (is my situation improving?). The adaptation time constant (~1–4 seconds) matches the timescale of a run, ensuring the comparison is 'recent enough' to reflect swimming direction but 'delayed enough' to span a meaningful distance. The molecular implementation — a reversible covalent modification (methylation) as memory — is one of the simplest and best-understood signal processing circuits in biology."
```

## Explainer

From your study of bacterial cell structure, you know that bacteria possess a variety of surface appendages — pili for attachment, capsules for protection, and flagella for motility. The **bacterial flagellum** is one of the most remarkable molecular machines in biology. Unlike eukaryotic flagella (which bend and undulate), the bacterial flagellum is a rigid, corkscrew-shaped filament that literally rotates like a propeller. The filament is made of thousands of copies of the protein **flagellin**, assembled into a hollow helix that extends several cell lengths from the surface. At its base sits a rotary motor embedded in the cell envelope — a structure with a rotor, stator, and drive shaft, functionally analogous to an electric motor but only about 45 nanometers in diameter.

The energy source for this motor is the **proton motive force** — the same electrochemical gradient across the inner membrane that drives ATP synthesis. Protons flowing through the stator proteins (MotA/MotB) exert force on the rotor ring, spinning it at extraordinary speeds. In *E. coli*, the motor turns at roughly 300 revolutions per second; in some marine bacteria like *Vibrio*, it exceeds 1,000 rps. The hook, a flexible coupling between the motor and the filament, transmits this rotation to the rigid flagellar helix. When all flagella on a peritrichous bacterium (one with flagella distributed around the cell) rotate counterclockwise, they bundle together into a single coherent propeller that pushes the cell forward in a straight **run**. When one or more motors switch to clockwise rotation, the bundle flies apart and the cell **tumbles** — reorienting randomly before the next run.

**Chemotaxis** is the signaling system that biases this random walk toward favorable environments. The key insight is that bacteria are too small to sense a spatial gradient across their body length — instead, they sense changes in chemical concentration over time as they swim. Chemoreceptors (methyl-accepting chemotaxis proteins, or MCPs) in the cell membrane detect attractants like sugars and amino acids or repellents like toxins. When an attractant concentration is increasing (meaning the cell is swimming in the right direction), the signaling pathway suppresses tumbling, so the cell continues its run for longer. When the concentration decreases, tumbling frequency increases, causing random reorientation until the cell happens to head up the gradient again. The molecular mechanism involves the kinase **CheA**, which phosphorylates **CheY**; phospho-CheY binds the flagellar motor switch and promotes clockwise rotation (tumbling). Attractant binding inhibits CheA, reducing phospho-CheY, and the cell runs longer.

An elegant feature of this system is **adaptation** through receptor methylation. The enzyme CheR continuously adds methyl groups to the MCPs, while CheB (activated by CheA phosphorylation) removes them. This creates a feedback loop that resets the signaling baseline after a few seconds, regardless of the absolute concentration of attractant. The result is that bacteria respond to *changes* in concentration rather than absolute levels — they are always comparing "now" to "a moment ago." This temporal comparison strategy allows bacteria to navigate gradients efficiently despite their microscopic size, and it represents one of the simplest and best-understood examples of signal transduction and behavioral decision-making in any organism.
