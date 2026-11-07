---
id: alkene-epoxidation-peroxy-acids
title: Epoxidation of Alkenes with Peroxy Acids
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: alkene-structure-and-nomenclature
  type: soft
- id: stereochemistry-intro
  type: soft
- id: alkene-hydroxylation-osmium-permanganate
  type: soft
builds-toward:
- epoxide-ring-opening
tags:
- epoxidation
- mCPBA
- peroxy acids
- stereospecific reactions
- anti dihydroxylation
- oxiranes
stage: formal-systems
status: validated
---

# Epoxidation of Alkenes with Peroxy Acids

## Core Idea
A peroxy acid such as meta-chloroperoxybenzoic acid (mCPBA) transfers one oxygen atom to an alkene, forming an epoxide, a three-membered cyclic ether. The reaction is concerted, so both C–O bonds form on the same face and the alkene's geometry is kept: a cis alkene gives a cis epoxide and a trans alkene gives a trans epoxide. Electron-rich, more substituted alkenes react faster. Opening the epoxide with aqueous acid then gives an anti 1,2-diol, the complement of syn dihydroxylation with OsO₄.

## How It's Best Learned
Draw the one-step "butterfly" transition state, showing the alkene π bond attacking the terminal peroxide oxygen while the O–H proton shifts to the carbonyl oxygen. Then predict products from cis and trans alkenes and check with models that the substituents keep their relationship. Finish by pairing epoxidation and acid-catalyzed ring opening as a two-step route to anti diols, set beside OsO₄ for syn diols.

## Common Misconceptions
- Epoxidation goes through a carbocation, so a cis alkene can give some trans epoxide. (The reaction is concerted with no intermediate, so it is stereospecific.)
- A peroxy acid acts as a nucleophile toward the alkene. (The alkene is the nucleophile; the weak O–O bond makes the terminal oxygen electrophilic.)
- Epoxidation followed by hydrolysis gives the same diol as OsO₄. (Ring opening occurs with backside attack, so the two OH groups end up anti; OsO₄ gives syn diols.)

## Questions

```yaml
- question: "What is the product when cis-but-2-ene is treated with mCPBA?"
  type: multiple-choice
  options: ["trans-2,3-dimethyloxirane", "cis-2,3-dimethyloxirane", "A 50:50 mixture of cis and trans epoxides", "Butane-2,3-diol"]
  answer: 1
  explanation: "Both new C–O bonds form at the same time on one face of the alkene. The two methyl groups keep their cis relationship, giving cis-2,3-dimethyloxirane, a meso compound."
- question: "Peroxy acid epoxidation proceeds through a carbocation intermediate, so its stereochemistry is scrambled."
  type: true-false
  answer: false
  explanation: "The reaction is a single concerted step. Because no intermediate forms, rotation about the former C=C bond cannot occur, and the reaction is stereospecific."
- question: "Which sequence converts cyclohexene into trans-cyclohexane-1,2-diol?"
  type: multiple-choice
  options: ["OsO₄, then NaHSO₃", "Cold dilute KMnO₄", "mCPBA, then H₃O⁺", "H₂ with Pd"]
  answer: 2
  explanation: "mCPBA forms the epoxide, and aqueous acid opens it by backside attack of water. The two OH groups end up on opposite faces, giving the trans diol. OsO₄ and cold KMnO₄ give the cis diol."
- question: "Which reacts faster with mCPBA, 2-methylbut-2-ene or but-1-ene? Explain."
  type: short-answer
  answer: "2-Methylbut-2-ene. Its three alkyl groups donate electron density to the double bond, making it a better nucleophile toward the electrophilic oxygen of the peroxy acid."
  explanation: "Epoxidation rates rise with the number of alkyl substituents on the alkene. This lets chemists epoxidize the most substituted double bond selectively in a molecule with several."
```

## Explainer

An epoxide, also called an oxirane, is a cyclic ether with a three-membered ring of two carbons and one oxygen. The ring is strained, so epoxides open readily and serve as useful intermediates. The most common way to make one is to treat an alkene with a peroxy acid, RCO₃H. In the laboratory the usual choice is meta-chloroperoxybenzoic acid, mCPBA, a fairly stable solid.

A peroxy acid has an extra oxygen in a weak O–O bond. The terminal oxygen is electrophilic, and the alkene π bond attacks it. In a single step, the alkene forms bonds to that oxygen from both carbons, the O–O bond breaks, and the O–H proton moves to the carbonyl oxygen of the peroxy acid. The by-product is a carboxylic acid. Because the transition state looks like a butterfly, this is often called the butterfly mechanism. The reaction is named after Nikolai Prilezhaev, who reported it in 1909.

The single concerted step has a direct consequence for stereochemistry. Both C–O bonds form on the same face, and no intermediate allows rotation. So the substituents keep their arrangement. cis-But-2-ene gives only cis-2,3-dimethyloxirane, and trans-but-2-ene gives only the trans epoxide. Such a reaction is called stereospecific.

The alkene acts as the nucleophile, so electron-rich alkenes react faster. Each alkyl group on the double bond raises the rate. In a molecule with two double bonds, mCPBA usually attacks the more substituted one first.

Epoxidation pairs well with ring opening. In aqueous acid, the epoxide oxygen is protonated and water attacks a ring carbon from the back side. The two OH groups end up on opposite faces, giving an anti diol. From cyclohexene, this two-step sequence gives trans-cyclohexane-1,2-diol. OsO₄ or cold permanganate gives the cis diol instead. Having both routes lets you choose the relative stereochemistry.

Epoxidation can also be made enantioselective. The Sharpless asymmetric epoxidation of allylic alcohols uses a titanium catalyst with a chiral tartrate ester, work recognized in K. Barry Sharpless's share of the 2001 Nobel Prize in Chemistry.
