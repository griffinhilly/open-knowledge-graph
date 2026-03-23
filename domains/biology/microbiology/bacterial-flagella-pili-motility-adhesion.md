---
id: bacterial-flagella-pili-motility-adhesion
title: Bacterial Flagella, Pili, and Cell-Surface Structures
domain: biology
course: microbiology
prerequisites:
- id: bacterial-pili-fimbriae-types
  type: hard
- id: bacterial-cell-organization-and-ultrastructure
  type: soft
builds-toward:
- chemotaxis-signaling-phosphorylation
- bacterial-virulence-mechanisms
tags:
- motility
- adhesion
- cell-surface
stage: formal-systems
status: draft
---

# Bacterial Flagella, Pili, and Cell-Surface Structures

## Core Idea
Flagella are helical, rotating appendages that propel bacteria through liquids, driven by proton gradients across the membrane. Pili (fimbriae) are hair-like structures that mediate adhesion to surfaces and host cells. Type IV pili enable twitching motility. These structures are essential for pathogenesis and environmental survival.

## Questions

```yaml
- question: "A researcher hypothesizes that blocking ATP synthase will immobilize bacteria by starving the flagellar motor of ATP. Based on how the flagellar motor actually works, this hypothesis is:"
  type: multiple-choice
  options:
    - "Correct — ATP is the direct fuel for flagellar rotation via the stator proteins"
    - "Incorrect — the flagellar motor is powered by proton flow through the stator proteins (the proton motive force), not by ATP hydrolysis; blocking ATP synthase would collapse the PMF and stop the motor, but not because ATP was removed"
    - "Incorrect — the flagellar motor uses GTP, not ATP or PMF"
    - "Correct — ATP powers the MotA/MotB stator proteins that rotate the basal body"
  answer: 1
  explanation: "The bacterial flagellar motor is powered by the proton motive force: protons flow down their electrochemical gradient through the stator proteins (MotA/MotB), driving rotation of the rotor at up to 1,000 rpm. ATP is not the direct energy source. ATP synthase uses PMF to make ATP — so blocking ATP synthase collapses PMF (and thus would stop the motor), but the mechanism is indirect and the reasoning in the hypothesis is wrong. The flagellar motor and ATP synthase are two different consumers of the same PMF currency."

- question: "A bacterium possesses Type IV pili but no flagella. Which phenotype would you predict?"
  type: multiple-choice
  options:
    - "The bacterium can swim through liquid but cannot attach to host cells"
    - "The bacterium can move on solid surfaces via twitching motility and can take up environmental DNA, but cannot swim through liquid"
    - "The bacterium is completely immotile and cannot adhere to surfaces"
    - "The bacterium can swim through liquid because Type IV pili can bundle and rotate like flagellar filaments"
  answer: 1
  explanation: "Type IV pili extend, adhere, then retract (via PilT) to generate twitching motility on surfaces — but this does not propel bacteria through liquid. Swimming requires the helical rotation of flagellar filaments. Type IV pili also mediate natural transformation (DNA uptake uses the same extension-retraction mechanism). Option D is wrong: twitching is jerky surface movement, not swimming, and pili cannot rotate like flagella."

- question: "Both flagella and pili are used by bacteria for locomotion — the difference is only whether they move in liquid or on surfaces."
  type: true-false
  answer: false
  explanation: "Most pili and fimbriae are primarily adhesion structures, not motility structures — they anchor bacteria to surfaces and host cells. Type I pili (with FimH adhesins), for example, mediate adhesion to bladder epithelium and do not generate movement. Only Type IV pili produce motility (twitching), and that is a special case. The primary functional distinction between flagella and most pili is motility versus adhesion, not liquid versus surface — conflating the two misrepresents how these distinct molecular machines are used."

- question: "In E. coli, when all flagellar motors spin counterclockwise, the helical filaments bundle together and propel the cell forward; when any motor switches to clockwise rotation, the bundle disperses and the cell tumbles."
  type: true-false
  answer: true
  explanation: "This run-and-tumble mechanism is the basis of bacterial chemotaxis. Counterclockwise rotation causes filaments to form a coherent left-handed helical bundle — a propeller that drives smooth forward swimming. Clockwise rotation by any one motor breaks the bundle geometry; the filaments interfere with each other and the cell reorients randomly. Chemotaxis signaling modulates the probability of the clockwise switch, biasing runs toward attractants and tumbles away from repellents."

- question: "Explain how the same molecular mechanism — Type IV pilus extension and retraction — serves two seemingly unrelated functions: twitching motility and natural transformation (DNA uptake)."
  type: short-answer
  answer: "Both functions use extension of the Type IV pilus, followed by retraction driven by the PilT motor, which depolymerizes pilin subunits back into the membrane. For twitching: the pilus tip adheres to a surface, then retraction pulls the cell toward the attachment point, producing jerky movement. For natural transformation: the pilus tip binds extracellular DNA, then retraction pulls the DNA into the cell. The same force-generating retraction mechanism is applied to different substrates — a surface versus a DNA molecule."
  explanation: "This illustrates how evolution co-opts a single molecular machine for multiple functions. PilT-driven retraction generates some of the strongest forces known in biology relative to the cell's scale. The key insight is that the mechanism (extend, grip, retract) is substrate-agnostic — whether it is pulling the bacterium toward a surface or pulling DNA into the cell depends entirely on what the pilus tip happens to bind."
```

## Explainer

You already know about the basic types of pili and fimbriae and their roles in bacterial biology, and you have a sense of bacterial cell surface architecture. Now we can examine how these appendages actually work as molecular machines and why they matter so much for both free-living survival and pathogenesis.

**Bacterial flagella** are among the most remarkable molecular machines in biology. Each flagellum consists of three parts: a long helical **filament** made of thousands of copies of the protein flagellin, a short curved **hook** that acts as a universal joint, and a **basal body** embedded in the cell envelope that functions as a rotary motor. The motor is powered by the **proton motive force** — the same electrochemical gradient across the cytoplasmic membrane that drives ATP synthesis. Protons flowing through the stator proteins (MotA/MotB) drive rotation of the rotor at speeds up to 1,000 revolutions per second in some species. When the motor spins counterclockwise (in *E. coli*), the flagellar filaments bundle together and the cell swims forward in a smooth "run." When one or more motors switch to clockwise rotation, the bundle flies apart and the cell "tumbles," reorienting randomly. This **run-and-tumble** pattern, modulated by chemotaxis signaling, allows bacteria to navigate chemical gradients — swimming toward nutrients and away from toxins.

**Pili** (also called fimbriae) serve a fundamentally different purpose: **attachment**. Common Type I pili, found on many Enterobacteriaceae, are assembled from pilin subunits via the chaperone-usher pathway and tipped with adhesin proteins like **FimH**, which binds mannose residues on host epithelial cells. This is why uropathogenic *E. coli* can colonize the bladder — FimH locks onto mannose-rich uroplakin proteins lining the bladder wall. Without these pili, the bacteria would be flushed out by urine flow. The clinical relevance is direct: adhesion is typically the first step in infection, and blocking it (with mannose analogs, for example) is an active area of antimicrobial research.

**Type IV pili** deserve special attention because they do something no other pilus type can: generate movement on solid surfaces. These pili extend from the cell, attach to a surface, and then **retract** by depolymerizing pilin subunits back into the membrane — physically pulling the cell forward in a jerky motion called **twitching motility**. The retraction motor (PilT) generates remarkable force, among the strongest known in biology relative to scale. Type IV pili also mediate **natural transformation** — the uptake of free DNA from the environment — and are major virulence factors in pathogens like *Neisseria gonorrhoeae* and *Pseudomonas aeruginosa*. Together, flagella and pili illustrate a broader principle: bacteria use distinct molecular machines for movement through liquids versus attachment and movement on surfaces, and the presence or absence of these structures directly determines which ecological niches and host tissues a bacterium can colonize.
