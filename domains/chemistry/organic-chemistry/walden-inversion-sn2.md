---
id: walden-inversion-sn2
title: Walden Inversion in SN2 Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: stereochemistry-intro
  type: hard
- id: r-s-nomenclature-cahn-ingold-prelog-rules
  type: hard
builds-toward:
- substitution-vs-elimination
tags:
- Walden inversion
- backside attack
- stereochemistry
- SN2
- steric effects
- configuration
stage: formal-systems
status: validated
---
# Walden Inversion in SN2 Reactions

## Core Idea
In an SN2 reaction the nucleophile attacks from the side opposite the leaving group (backside attack), passing through a trigonal bipyramidal transition state that results in complete inversion of configuration at the carbon center — the Walden inversion. This stereochemical outcome is as reliable as an umbrella flipping inside-out in the wind: every substituent swaps to the opposite face. The requirement for backside attack also explains why SN2 rates drop sharply with increasing steric bulk around the electrophilic carbon, since bulky groups physically block the nucleophile's approach.

## How It's Best Learned
Use three-dimensional models (physical or software) to visualize the approach trajectory and the umbrella-flip transition state. Practice assigning R/S before and after reaction to confirm inversion occurred. Work through examples where inversion does and does not change the R/S label (it depends on CIP priority changes when the incoming group replaces the leaving group).

## Common Misconceptions
- Inversion of spatial arrangement does not automatically mean R switches to S; the CIP priority of the new substituent may reorder rankings, keeping the same label.
- Walden inversion is not partial — it is complete (100%) inversion at the attacked carbon, distinguishing SN2 from SN1 which gives racemization.
- Steric effects on SN2 are about the transition state geometry, not about thermodynamic stability of the product.

## Questions

```yaml
- question: "An SN2 reaction converts (R)-2-bromobutane to a product using cyanide (CN⁻) as the nucleophile. Complete inversion of spatial arrangement occurs at C2. Which statement about the product's R/S designation is correct?"
  type: multiple-choice
  options:
    - "The product must be (S)-2-cyanobutane, since SN2 inversion always converts R to S"
    - "The product must be (R)-2-cyanobutane, since inversion does not change the R/S designation"
    - "The product is a racemic mixture of R and S, since inversion is not stereospecific"
    - "The R/S designation of the product cannot be determined from inversion alone; it requires assigning CIP priorities to the new substituent arrangement"
  answer: 3
  explanation: "Spatial inversion (the umbrella flip) always occurs in SN2, but whether the R/S letter changes depends on CIP priority reassignment. If the incoming group (CN) has a different priority rank than the departing group (Br), the priority order of the four substituents may reshuffle, potentially keeping the same R/S label despite complete geometric inversion. The safe approach is always to draw the three-dimensional structure after reaction and assign priorities directly. The common misconception (option A) assumes inversion automatically flips the R/S label, which is only sometimes true."

- question: "Why do tertiary alkyl halides essentially never undergo SN2 reactions, while methyl halides react fastest of all?"
  type: multiple-choice
  options:
    - "Tertiary substrates form more stable carbocations, making them prefer SN1 for thermodynamic reasons"
    - "The three alkyl groups surrounding the electrophilic carbon in tertiary substrates physically block the nucleophile from approaching the backside of the C–X bond"
    - "The C–X bond is significantly stronger in tertiary substrates, requiring prohibitively high activation energy"
    - "Tertiary carbons lack a suitable σ* antibonding orbital for the nucleophile to attack"
  answer: 1
  explanation: "SN2 requires backside attack — the nucleophile must approach along the C–X bond axis from the face opposite the leaving group. In a tertiary substrate, three bulky alkyl groups surround the carbon and physically block access to this approach trajectory. In a methyl substrate, three small hydrogen atoms leave the backside open. This is a purely steric (geometric) argument about transition-state accessibility, not about bond strength or carbocation stability. Option A describes why tertiary substrates prefer SN1, which is a separate mechanism — the SN2 failure is a steric issue, not a thermodynamic preference."

- question: "In every SN2 reaction at a stereocenter, the spatial arrangement of substituents around the reacting carbon is completely inverted — every group moves to the opposite face — regardless of which nucleophile or leaving group is involved."
  type: true-false
  answer: true
  explanation: "Walden inversion is a mechanistic inevitability of the SN2 pathway, not a property of specific reactants. The backside attack geometry — mandated by orbital symmetry (nucleophile lone pair into C–LG σ*) — forces the three remaining substituents to pass through a trigonal planar arrangement and emerge on the opposite face. This happens 100% of the time in every SN2 event, which is why SN2 is stereospecific: it produces a single enantiomer rather than a mixture."

- question: "If an SN2 reaction causes complete spatial inversion at a chiral carbon, the product is expected to have the opposite R/S configuration label (R→S or S→R)."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about Walden inversion. The spatial arrangement always inverts, but the R/S label is assigned by CIP priority rules — and those rules can reshuffle when a new group replaces the leaving group. If the incoming nucleophile has the same CIP priority rank as the leaving group it replaces, priorities are unchanged and the letter flips. But if the nucleophile has a different rank, the new priority ordering may yield the same letter as the starting material even though every group is now on the opposite face. R and S are labels applied to spatial arrangements, not properties of those arrangements themselves."

- question: "Explain why the requirement for backside attack in SN2 reactions creates a direct connection between reaction rate and the steric environment around the electrophilic carbon."
  type: short-answer
  answer: "SN2 requires the nucleophile to approach along the axis of the C–leaving group bond, from the face directly opposite the leaving group. Any substituents on the electrophilic carbon occupy space near this backside approach trajectory. More and larger substituents (primary → secondary → tertiary) increasingly block the nucleophile's path, raising the transition-state energy and slowing (or preventing) the reaction. This is entirely a geometric argument about the trigonal bipyramidal transition state: the rate drops with steric bulk not because the bond is harder to break, but because the transition state geometry becomes inaccessible."
  explanation: "This link between geometry and reactivity is what makes SN2 a predictable, stereochemically controlled reaction. The same geometric constraint that causes the umbrella-flip inversion is what makes tertiary substrates unreactive — both effects trace back to the requirement that the nucleophile approach from the backside. Knowing this, you can predict both the stereochemical outcome (complete inversion) and the substrate scope (methyl > primary > secondary >> tertiary) from one structural principle."
```

## Explainer

From your study of the SN2 mechanism, you know it is a one-step, concerted process: the nucleophile attacks the electrophilic carbon at the same time the leaving group departs. But there is a critical geometric constraint that your stereochemistry background makes clear. The nucleophile does not approach from just any direction — it attacks from the **backside**, the face directly opposite the leaving group. This approach angle is not a preference; it is a requirement dictated by orbital symmetry. The nucleophile's lone pair donates into the σ* antibonding orbital of the C–LG bond, and that orbital has its largest lobe on the backside of the carbon.

As the nucleophile approaches and the leaving group begins to depart, the three remaining substituents on the carbon flatten out into a plane, creating a **trigonal bipyramidal transition state** — the nucleophile on one side, the leaving group on the other, and the three groups arranged in a plane between them. Then, as the leaving group fully departs, those three groups swing through to the opposite side, like an umbrella flipping inside-out in a strong wind. This is the **Walden inversion**: every substituent ends up on the opposite face of the carbon from where it started. The inversion is complete — 100% of product molecules have the inverted configuration.

One subtlety that frequently causes confusion is the relationship between inversion and R/S designation. Inversion of the spatial arrangement always occurs, but whether the R/S label changes depends on the CIP priority rules. If the incoming nucleophile has a different CIP priority than the leaving group, the priority rankings may reshuffle, and the product might carry the same letter designation (R or S) despite having inverted geometry. The safe approach is to draw the three-dimensional arrangement before and after reaction and assign configurations directly, rather than assuming inversion automatically means R→S or S→R.

The backside-attack requirement also explains why **steric bulk** is the primary enemy of SN2 reactions. If the carbon bearing the leaving group is surrounded by large substituents — as in a tertiary carbon with three alkyl groups — those groups physically block the nucleophile's approach to the backside. Methyl and primary substrates react fastest because the backside is relatively open. Secondary substrates are slower, and tertiary substrates essentially do not undergo SN2 at all. This steric argument is purely about the geometry of the transition state; it has nothing to do with the thermodynamic stability of the product. Walden inversion thus connects stereochemical outcome and reaction rate to a single geometric principle: the nucleophile must come in from behind.
