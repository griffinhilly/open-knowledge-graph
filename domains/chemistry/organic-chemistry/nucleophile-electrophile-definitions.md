---
id: nucleophile-electrophile-definitions
title: 'Nucleophiles and Electrophiles: Definitions and Reactivity'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: lewis-structures
  type: hard
- id: acid-base-definitions
  type: soft
builds-toward:
- sn1-reaction
- sn2-reaction
- electrophilic-addition-to-alkenes
tags:
- mechanism
- reactivity
- nucleophile
- electrophile
stage: formal-systems
status: validated
---

# Nucleophiles and Electrophiles: Definitions and Reactivity

## Core Idea
Nucleophiles are electron-rich species (lone pairs or π-bonds) that attack electron-deficient centers (electrophiles). Carbocations, carbonyl carbons, and electrophilic double bonds are examples of electrophilic sites. Nucleophilicity is context-dependent, related to basicity but also influenced by solvent, substrate, and leaving group ability.

## How It's Best Learned
Identify nucleophilic and electrophilic sites in molecules by analyzing electron density and formal charges. Correlate nucleophilicity rankings with basicity and solvent effects.

## Common Misconceptions
- Assuming nucleophilicity always equals basicity; solvent effects and steric hindrance can decouple these properties.
- Overlooking π-electrons in alkenes and alkynes as nucleophilic sites.

## Questions

```yaml
- question: "In a protic polar solvent (e.g., water or methanol), which halide ion is the strongest nucleophile?"
  type: multiple-choice
  options:
    - "F⁻"
    - "Cl⁻"
    - "Br⁻"
    - "I⁻"
  answer: 3
  explanation: "In protic solvents, nucleophilicity follows the reverse of basicity for halides: I⁻ > Br⁻ > Cl⁻ > F⁻. Although F⁻ is the strongest base (most tightly held electrons), it is also the most heavily solvated — protic solvents form strong hydrogen bonds around it, shielding its electrons and slowing attack on electrophiles. Iodide, being large and polarizable with loosely held electrons, is weakly solvated and attacks electrophiles readily. In aprotic solvents the order can reverse, illustrating that nucleophilicity is not the same as basicity."

- question: "A stronger base is always a stronger nucleophile."
  type: true-false
  answer: false
  explanation: "Basicity (affinity for a proton, measured by pKa) and nucleophilicity (rate of attack on a carbon electrophile) are related but distinct properties that can be decoupled by solvent and steric effects. In protic solvents, large, polarizable species like I⁻ are strong nucleophiles despite being weak bases. Bulky bases like tert-butoxide are very basic but poor nucleophiles because steric hindrance blocks approach to carbon. The two properties diverge whenever size, polarizability, or solvation is the dominant factor."

- question: "Why can an alkene act as a nucleophile even though it carries no formal negative charge and no lone pairs?"
  type: short-answer
  answer: "The π-bond of an alkene consists of electron density above and below the plane of the double bond. These electrons are loosely held and accessible to electron-deficient species (electrophiles), making the alkene nucleophilic without requiring a lone pair or negative charge."
  explanation: "Nucleophilicity requires electron-rich sites capable of donating electrons to an electrophile — it does not require a formal charge or a lone pair specifically. The π-electrons in a C=C double bond occupy a diffuse region of space that is easily polarized toward an approaching electrophile. This is why electrophilic addition to alkenes begins with electrophile attack on the π-system: the alkene donates its π-electrons to the electrophile in the first mechanistic step. Recognizing π-bonds as nucleophilic sites is essential for understanding electrophilic addition reactions."
```

## Explainer

Every organic reaction mechanism can be described in terms of electron flow from an electron-rich site to an electron-poor site. The electron-rich partner is the **nucleophile** ("nucleus-loving"), the electron-poor partner is the **electrophile** ("electron-loving"). This framework, rooted in Lewis acid–base theory, is the conceptual backbone of all mechanistic organic chemistry.

Nucleophiles supply electron pairs: they can be anions (Cl⁻, OH⁻, CN⁻), neutral species with lone pairs (water, ammonia, alcohols), or molecules with π-bonds (alkenes, alkynes). Electrophiles receive electron pairs: they can be cations (carbocations, H⁺), neutral molecules with a partial positive charge (alkyl halides, carbonyl carbons), or any atom with an empty or low-lying orbital. Identifying which partner is nucleophilic and which is electrophilic is the first step in predicting what bond forms and where. When you look at a molecule, map out where electron density is concentrated (lone pairs, π-clouds, negative formal charges) versus where it is depleted (partial or full positive charges, polarized bonds to electronegative atoms). The nucleophile attacks the electrophilic site.

A crucial subtlety is that **nucleophilicity is not the same as basicity**, even though both measure how well a species donates electrons. Basicity is measured thermodynamically — the equilibrium affinity for a proton (pKa). Nucleophilicity is measured kinetically — how fast the species attacks a carbon electrophile. These can diverge significantly depending on three factors: (1) **Polarizability** — larger atoms (e.g., iodine vs. fluorine) have more diffuse, loosely held electrons that are faster to donate to carbon even though they bind protons weakly. (2) **Solvation** — protic solvents cage small, hard anions like F⁻ in hydrogen-bond networks, slowing their approach to electrophilic carbons; large, soft anions like I⁻ escape solvation more easily. (3) **Steric hindrance** — a very bulky nucleophile may be a strong base (proton is tiny) but a poor nucleophile (the electrophilic carbon is too hindered to approach). tert-Butoxide is the textbook example: excellent base, poor nucleophile, so it drives E2 elimination rather than SN2 substitution.

The class of nucleophiles most commonly overlooked by beginners is **π-systems**. An alkene's π-bond consists of electron density above and below the molecular plane, accessible and polarizable. When an electrophile (say, HBr or Br₂) approaches, the alkene donates its π-electrons to the electrophile — that donation *is* the first mechanistic step of electrophilic addition. The alkene doesn't need a lone pair or a negative charge to be nucleophilic; it needs accessible, loosely held electrons. The same logic applies to aromatic rings in electrophilic aromatic substitution.

With this framework established, the downstream reactions you will encounter — SN1, SN2, E1, E2, electrophilic addition, nucleophilic addition to carbonyls — all become variations on the same theme: nucleophile finds electrophile, electrons flow, bonds form and break. Learning to identify the nucleophilic and electrophilic sites in any molecule before trying to predict the mechanism is the single most useful habit you can develop at this stage of organic chemistry.
