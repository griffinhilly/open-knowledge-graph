---
id: resonance-in-organic-intermediates
title: Resonance in Organic Intermediates
domain: chemistry
course: organic-chemistry
prerequisites:
- id: resonance-and-formal-charge
  type: hard
- id: reaction-mechanisms-overview
  type: soft
builds-toward:
- conjugated-dienes
tags:
- resonance
- delocalization
- allylic
- benzylic
- carbocation
- carbanion
- radical
stage: formal-systems
status: validated
---
# Resonance in Organic Intermediates

## Core Idea
Reactive intermediates — carbocations, carbanions, and radicals — gain significant stability when the unpaired electron or empty/filled orbital can delocalize across adjacent p-orbitals through resonance. An allylic carbocation spreads positive charge over two carbons via overlap with a neighboring pi bond; a benzylic radical delocalizes the unpaired electron across the aromatic ring. The more resonance contributors that can be drawn (without moving atoms), the greater the stabilization. This principle governs regioselectivity in addition, substitution, and radical reactions: intermediates form preferentially at positions that maximize delocalization.

## How It's Best Learned
Draw all valid resonance structures for each intermediate, using curved arrows to show electron movement. Rank the structures by stability (equivalent contributors are best; charge on more electronegative atoms is better). Compare the stability of an allylic cation with a simple secondary cation to see why allylic/benzylic positions are favored in SN1 and radical reactions.

## Common Misconceptions
- Resonance structures are not equilibria — the molecule does not alternate between forms. The real structure is a single hybrid with partial charges/bonds.
- Moving atoms to draw a new structure is tautomerism, not resonance; resonance involves only electron redistribution.
- More resonance structures does not always mean more stability — the structures must be reasonably low-energy contributors to matter.

## Questions

```yaml
- question: "Bromination of an alkene via radical mechanism (using NBS) at an allylic position is highly favored. A student argues this is because the allylic carbon 'alternates rapidly between the two resonance structures.' What is the correct explanation?"
  type: multiple-choice
  options:
    - "The student is correct: the intermediate rapidly interconverts between two structures, trapping bromine at either carbon"
    - "The allylic radical is a single species with electron density delocalized simultaneously across both carbons — a resonance hybrid lower in energy than either individual structure"
    - "Radical reactions are inherently non-selective, so allylic positions are not especially preferred"
    - "The allylic position is preferred purely due to steric effects, not resonance stabilization"
  answer: 1
  explanation: "The most common resonance misconception is treating resonance structures as equilibrating species. The allylic radical is one real molecule whose electron density is spread across both carbons simultaneously — a hybrid lower in energy than either resonance structure alone. This delocalization thermodynamically stabilizes the intermediate, lowering the activation energy to form it. The radical does not 'bounce' between structures; it is a single entity with partial radical character at both allylic carbons."

- question: "A benzylic primary substrate undergoes SN1 reaction readily, while a simple primary alkyl substrate under the same conditions does not. What accounts for this reactivity difference?"
  type: multiple-choice
  options:
    - "Benzene rings are electron-withdrawing, destabilizing the nearby carbocation and forcing an alternative mechanism"
    - "Benzylic carbocations can delocalize positive charge into the aromatic ring (ortho and para positions), providing resonance stabilization unavailable to primary alkyl carbocations"
    - "The phenyl group provides steric bulk that prevents backside attack, making SN2 impossible and SN1 the only available path"
    - "Primary benzylic substrates react via radical mechanisms, not SN1"
  answer: 1
  explanation: "A benzylic carbocation can delocalize positive charge across the aromatic ring — resonance structures with charge at the ortho and para positions provide four or more resonance contributors. This extensive delocalization dramatically lowers the energy of the intermediate. A simple primary carbocation has no such stabilization, making it essentially too unstable to form in SN1. In SN1 reactions, feasibility depends on carbocation formation, so any feature that stabilizes the carbocation dramatically accelerates the reaction."

- question: "A molecule described by two resonance structures of equal energy is more stable than a molecule described by two resonance structures of unequal energy."
  type: true-false
  answer: true
  explanation: "When resonance contributors are equivalent (equal energy), electron delocalization is maximized and stabilization is greatest — this is why benzene is exceptionally stable (six equivalent contributors). When contributors are unequal in energy, the hybrid resembles the lower-energy structure more closely, and the stabilization gained from delocalization is reduced. The closer in energy the contributors, the more equal their contribution to the hybrid, and the greater the resonance stabilization."

- question: "More resonance structures can always be drawn for a more stable molecule — so counting resonance structures is a reliable measure of stability."
  type: true-false
  answer: false
  explanation: "While more equivalent, low-energy resonance contributors do increase stability, not all drawable resonance structures contribute meaningfully. High-energy structures — those with adjacent like charges, broken octets on electronegative atoms, or formal charge violations — contribute very little to the hybrid and provide almost no stabilization. You can draw many technically valid but energetically unfavorable resonance structures, inflating the apparent count without reflecting real stabilization. Quality of contributors matters, not raw quantity."

- question: "What is a resonance hybrid, and why does the concept of resonance matter for predicting where a reaction intermediate will form in a molecule?"
  type: short-answer
  answer: "A resonance hybrid is the actual electronic structure of a molecule — a single species with electron density distributed continuously across multiple atoms, not a mixture of alternating structures. The contributing resonance structures are bookkeeping tools showing which atoms share the electron density. For reaction intermediates, the position that can form the most stable hybrid — where the charge, radical, or empty orbital can be delocalized across the most atoms via low-energy contributors — is where the intermediate forms preferentially. This governs regioselectivity: reactions proceed through allylic or benzylic positions because those intermediates are resonance-stabilized hybrids lower in energy than their non-delocalized counterparts."
  explanation: "The practical import is that whenever you see a reaction site adjacent to a π system (double bond or aromatic ring), ask: would the intermediate at this position be resonance-stabilized? If yes, and if a competing non-stabilized pathway exists, the stabilized pathway dominates. This is why Markovnikov addition, NBS bromination, and SN1 at benzylic positions all follow from the same underlying principle."
```

## Explainer

From your work on resonance and formal charge, you know that molecules with delocalized electrons are described as hybrids of multiple resonance structures, and that the real electron distribution is a weighted blend of all contributors. This same principle becomes the dominant factor controlling the stability — and therefore the reactivity — of organic intermediates like carbocations, carbanions, and radicals.

Consider a simple secondary carbocation, like the one at carbon-2 of propane. The empty p-orbital sits on a single carbon, and the only stabilization comes from hyperconjugation with neighboring C–H bonds. Now move that positive charge to the **allylic position** — the carbon adjacent to a double bond. Suddenly the empty p-orbital can overlap with the adjacent pi bond, and you can draw two resonance structures: one with the positive charge on the original carbon, and one with it shifted to the carbon two positions away. The charge is spread over two carbons instead of concentrated on one. This delocalization lowers the energy of the intermediate substantially, which is why allylic carbocations form far more readily than comparably substituted non-allylic ones.

The **benzylic position** takes this further. A carbocation, radical, or carbanion adjacent to a benzene ring can delocalize into the aromatic pi system. For a benzylic carbocation, you can draw resonance structures placing the positive charge on the benzylic carbon and on the ortho and para positions of the ring — that is four or more contributing structures. The extensive delocalization makes benzylic intermediates remarkably stable. This is why benzylic halides undergo SN1 reactions with surprising ease, even when they are technically primary substrates: the intermediate carbocation gains enough resonance stabilization to form readily.

The practical consequence is that **resonance stabilization governs regioselectivity**. In electrophilic additions to conjugated dienes, the intermediate that places the positive charge at an allylic position is favored over one that does not. In radical halogenation, abstraction at the benzylic or allylic position is preferred because the resulting radical is resonance-stabilized. When you evaluate competing reaction pathways, always ask: can the intermediate delocalize its charge or unpaired electron? If one pathway produces a resonance-stabilized intermediate and another does not, the resonance-stabilized path will generally dominate, even if other factors like substitution patterns might suggest otherwise.
