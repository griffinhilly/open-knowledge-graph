---
id: reaction-mechanisms-overview
title: Organic Reaction Mechanisms and Arrow Pushing
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: resonance-and-formal-charge
  type: hard
- id: acid-base-chemistry
  type: soft
builds-toward:
- sn2-reaction
- sn1-reaction
- e2-elimination
- e1-elimination
- electrophilic-addition-to-alkenes
- electrophilic-aromatic-substitution
- nucleophilic-addition-to-carbonyls
tags:
- mechanism
- arrow pushing
- electron flow
- nucleophile
- electrophile
- leaving group
- intermediate
stage: advanced
status: validated
---

# Organic Reaction Mechanisms and Arrow Pushing

## Core Idea
Organic reaction mechanisms describe the step-by-step electron flow in a chemical transformation using curved arrow notation. Each double-headed curved arrow represents movement of an electron pair from a source (nucleophile, lone pair, or bond) to a sink (electrophile or antibonding orbital). Key concepts include nucleophiles (electron-pair donors), electrophiles (electron-pair acceptors), leaving groups, and reactive intermediates such as carbocations, carbanions, and radicals. Drawing mechanistic arrows correctly — always from electron-rich to electron-poor — is the central skill of organic chemistry.

## How It's Best Learned
Begin with proton-transfer reactions to build arrow-pushing discipline, then progress to substitution and addition. Before drawing any arrows, identify the nucleophilic site and the electrophilic site in each reactant. Check each step by verifying that formal charges balance correctly.

## Common Misconceptions
- Arrows always originate from electron-rich sources and point to electron-poor sinks — never the reverse.
- Fishhook (half-headed) arrows represent single-electron movement in radical mechanisms; standard curved arrows represent two electrons.
- A plausible mechanism is a hypothesis consistent with evidence — it doesn't prove the actual molecular pathway.

## Questions

```yaml
- question: "In curved arrow notation, a double-headed curved arrow represents the movement of:"
  type: multiple-choice
  options: ["A single electron", "An electron pair from a nucleophile to an electrophile", "A proton from one atom to another", "An entire atom between two molecules"]
  answer: 1
  explanation: "Double-headed (full) curved arrows always represent the movement of two electrons — an electron pair. They originate at an electron-rich source (a lone pair, a pi bond, or a sigma bond) and point toward an electron-poor sink (an electrophile or antibonding orbital). Single-electron movement uses fishhook (half-headed) arrows in radical mechanisms."

- question: "A fishhook (half-headed) curved arrow in a reaction mechanism means the same thing as a regular double-headed curved arrow, just drawn differently for stylistic reasons."
  type: true-false
  answer: false
  explanation: "The distinction is mechanistically significant, not stylistic. A double-headed arrow represents a two-electron movement (ionic mechanism), while a fishhook arrow represents a one-electron movement (radical mechanism). Confusing them changes the entire mechanistic interpretation — radical and ionic pathways involve different intermediates, conditions, and reactivity patterns."

- question: "In the reaction step where H₂O donates a lone pair to H⁺ forming H₃O⁺, which species is the nucleophile and which is the electrophile? Explain why."
  type: short-answer
  answer: "H₂O is the nucleophile because its oxygen has lone pairs (electron-rich) and donates them to H⁺. H⁺ is the electrophile because it has an empty orbital and no electrons to contribute — it accepts the electron pair. The curved arrow is drawn from the lone pair on oxygen pointing to H⁺."
  explanation: "This proton-transfer is the simplest example of nucleophile/electrophile thinking. Nucleophiles are electron-pair donors (Lewis bases); electrophiles are electron-pair acceptors (Lewis acids). Practicing on familiar acid-base reactions builds the arrow-pushing intuition needed for more complex substitution and addition mechanisms."
```

## Explainer

Arrow pushing is the language of organic chemistry — a compact notation for describing how electrons move as chemical bonds form and break. Every organic reaction, no matter how complex it appears, can be described as a sequence of steps where electron pairs move from electron-rich sites to electron-poor sites. Learning to draw and interpret these arrows correctly is the single most transferable skill in the course.

The two characters in every mechanistic step are the nucleophile and the electrophile. A nucleophile ("nucleus lover") is electron-rich and donates electrons: it could be a lone pair on an oxygen or nitrogen, a pi bond in an alkene or aromatic ring, or a carbanion. An electrophile ("electron lover") is electron-poor and accepts electrons: a proton, a carbon bearing a partial positive charge, or a carbon bonded to a leaving group. Before drawing any arrows, identify these roles — the arrow originates at the nucleophile and points to the electrophile. Never draw it backward.

Each arrow must be balanced. After drawing the arrow, update the structure and verify formal charges. If an electron pair from a lone pair on oxygen attacks a carbon, that oxygen loses a lone pair (gaining a positive formal charge) and the carbon gains an electron pair (losing a positive formal charge if it was a carbocation, or forming a new bond). Tracking formal charges is your consistency check: the total charge must be conserved across each step. When a step produces an intermediate with implausible formal charge or an atom with too many bonds, your arrow is wrong.

Two types of arrows are in play: the standard double-headed curved arrow (two electrons, ionic mechanisms) and the fishhook half-headed arrow (one electron, radical mechanisms). The visual difference is intentional and important — radical chemistry involves unpaired electrons and completely different reactive intermediates (radicals rather than carbocations or carbanions). Mixing the two notations in one mechanism is a conceptual error, not just a drawing error.

Finally, a drawn mechanism is a hypothesis, not a proven fact. Chemists propose mechanisms that are consistent with experimental evidence — stereochemical outcomes, isotope labeling studies, kinetic rate laws — but the arrows represent a model of electron flow, not a direct observation. The power of mechanisms is that a small set of arrow-pushing patterns (nucleophilic substitution, electrophilic addition, elimination) recurs across thousands of reactions. Once you recognize the pattern, you can predict products for reactions you have never seen before.

