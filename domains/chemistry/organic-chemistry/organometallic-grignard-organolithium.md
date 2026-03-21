---
id: organometallic-grignard-organolithium
title: Grignard and Organolithium Reagents in Synthesis
domain: chemistry
course: organic-chemistry
prerequisites:
- id: grignard-reagent
  type: soft
- id: nucleophile-electrophile-definitions
  type: hard
- id: carbonyl-reduction-to-alcohols
  type: soft
builds-toward:
- wittig-reaction-mechanism
tags:
- organometallic
- grignard
- organolithium
- nucleophile
- synthesis
stage: advanced
status: draft
---

# Grignard and Organolithium Reagents in Synthesis

## Core Idea
Grignard (RMgX) and organolithium (RLi) reagents are strong carbon nucleophiles and bases formed from alkyl halides. They react with carbonyl electrophiles (aldehydes, ketones, esters) and CO₂ to form C-C bonds. RLi is more reactive and less selective than RMgX. Both require anhydrous, aprotic conditions and are incompatible with protic functional groups.

## How It's Best Learned
Draw mechanisms for Grignard additions to various carbonyls. Compare the reactivity of RMgX and RLi. Identify functional groups that will interfere with organometallic reagents.

## Common Misconceptions
- Assuming Grignards and RLi can be used in protic solvents; they react with water and require aprotic conditions.
- Forgetting that organometallic reagents are strong bases and nucleophiles, reacting with multiple functional group types beyond carbonyls.

## Questions

```yaml
- question: "A chemist wants to prepare a Grignard reagent from a molecule that also contains a free carboxylic acid group. What happens when she attempts to form the reagent?"
  type: multiple-choice
  options:
    - "The Grignard forms normally; the carboxylic acid is too far from the reaction site to interfere"
    - "The Grignard reagent is destroyed by the acidic proton of the carboxylic acid before it can react with the intended electrophile"
    - "The carboxylic acid is reduced to an aldehyde by the organometallic reagent"
    - "The reaction proceeds in ethanol solvent, which stabilizes both functional groups"
  answer: 1
  explanation: "Grignard and organolithium reagents are destroyed by any protic source — including carboxylic acids, alcohols, water, and terminal alkynes — because these acidic protons react with the carbanion-like reagent immediately. The –COOH proton (pKa ~5) is far more acidic than the carbon being metalated, so the Grignard is instantly protonated and deactivated. Functional groups containing N–H or O–H bonds must be protected before attempting to form or use organometallic reagents."

- question: "A Grignard reagent RMgBr is added to an ester (R'COOR''). What is the final product after acidic workup?"
  type: multiple-choice
  options:
    - "A secondary alcohol with one R group from the Grignard"
    - "A tertiary alcohol with two R groups from the Grignard"
    - "An aldehyde, because esters are reduced by one oxidation state"
    - "A primary alcohol, because esters react more mildly than ketones"
  answer: 1
  explanation: "Ester addition proceeds in two steps: the Grignard attacks the carbonyl of the ester, and the alkoxide leaving group departs to produce a ketone intermediate. This ketone is more reactive toward nucleophilic addition than the original ester, so a second equivalent of Grignard attacks immediately. After acidic workup, the product is a tertiary alcohol carrying two identical R groups from the Grignard. This two-addition sequence is why Grignard + ester always gives a tertiary alcohol — you cannot stop at the ketone stage under normal conditions."

- question: "Organolithium reagents are more reactive and less selective than Grignard reagents because the C–Li bond is more ionic, giving the carbon a stronger partial negative charge."
  type: true-false
  answer: true
  explanation: "The C–Li bond is more polarized than the C–Mg bond because lithium is a smaller, less electronegative metal, making the bond more ionic in character. This stronger carbanion-like character makes organolithium reagents faster to react and less discriminating about which electrophiles they attack — they will add to functional groups (like certain amides) that Grignard reagents leave alone. When precise selectivity is needed, RMgX is preferred; when maximum nucleophilicity is needed, RLi is the choice."

- question: "A Grignard reaction can be successfully carried out in a slightly damp flask if the reaction is performed quickly, since water only slowly decomposes the reagent."
  type: true-false
  answer: false
  explanation: "Grignard and organolithium reagents react with water immediately and completely — there is no window where the reaction is 'slow enough' to tolerate moisture. Even trace water destroys the reagent by protonating the carbon nucleophile. This is why Grignard reactions require rigorously dried glassware, anhydrous solvents (dried ether or THF), and an inert atmosphere. The reaction of RMgX with water is essentially instantaneous, not slow. Any moisture contamination before or during the reaction results in failure."

- question: "Why do Grignard and organolithium reagents require anhydrous, aprotic conditions, and what happens at the molecular level when a protic solvent is present?"
  type: short-answer
  answer: "Grignard and organolithium reagents carry a strongly nucleophilic carbon that behaves as a carbanion. Protic solvents (water, alcohols) have O–H bonds whose protons are far more electrophilic than the carbonyl carbons these reagents are designed to attack. The carbanion immediately abstracts the proton, forming a simple alkane (R–H) and a magnesium or lithium alkoxide — destroying the C–metal bond entirely. Because this proton transfer is faster than carbonyl addition, even trace moisture converts the entire reagent to an unreactive alkane before it can form the desired C–C bond."
  explanation: "The key is the kinetic competition: proton transfer from O–H to a carbanion is among the fastest reactions in organic chemistry (essentially diffusion-controlled), while nucleophilic addition to a carbonyl is slower. Any protic source wins the competition, irreversibly converting the valuable organometallic reagent into a worthless alkane. This is also why terminal alkynes (R–C≡C–H, pKa ~25) destroy Grignard reagents despite being relatively weak acids — the carbanion of RMgBr is basic enough to deprotonate them."
```

## Explainer

You already know that nucleophiles attack electrophiles — that electron-rich species seek out electron-poor centers. Grignard and organolithium reagents take this idea to its most powerful extreme by turning carbon itself into the nucleophile. When an alkyl halide like CH₃Br reacts with magnesium metal in dry ether, the result is CH₃MgBr — a **Grignard reagent** where the carbon-magnesium bond is so polarized that the carbon carries a strong partial negative charge. It behaves, for all practical purposes, as a carbanion: a carbon nucleophile ready to attack electrophilic carbon centers. **Organolithium reagents** (like CH₃Li, formed from alkyl halides and lithium metal) are even more reactive because the C–Li bond is more ionic, making the carbon an even stronger nucleophile and base.

The signature reaction of these reagents is **nucleophilic addition to carbonyls**. When a Grignard reagent attacks formaldehyde (HCHO), you get a primary alcohol after acidic workup. Attack on any other aldehyde yields a secondary alcohol. Attack on a ketone yields a tertiary alcohol. Attack on an ester proceeds through two additions (since the first addition produces a ketone intermediate) to give a tertiary alcohol where two of the substituents come from the Grignard. These transformations are among the most important C–C bond-forming reactions in organic synthesis, because they let you build up a carbon skeleton one piece at a time from simpler starting materials.

The critical constraint is **functional group compatibility**. Both Grignard and organolithium reagents are destroyed by any protic source — water, alcohols, amines, carboxylic acids, even terminal alkynes. They are also strong enough bases to deprotonate many weakly acidic functional groups. This means you cannot prepare or use these reagents in the presence of –OH, –NH, or –COOH groups unless those groups are protected first. Solvents must be rigorously dried and aprotic; diethyl ether and THF are standard choices. Forgetting this incompatibility is the single most common source of failed Grignard reactions.

The difference between RMgX and RLi matters in practice. Organolithium reagents are more reactive and less selective — they react faster but are harder to control, and they can add to functional groups that Grignard reagents leave alone (such as certain amides). When you need a powerful, indiscriminate carbon nucleophile, RLi is the tool. When you need more selectivity or milder conditions, RMgX is preferred. Choosing between them is a judgment call that depends on the substrate's other functional groups and the desired product, and it is a recurring decision in synthetic planning.
