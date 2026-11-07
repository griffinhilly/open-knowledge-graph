---
id: ozonolysis-oxidative-cleavage
title: Ozonolysis and Oxidative Cleavage of Alkenes
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: aldehyde-and-ketone-structure-and-nomenclature
  type: hard
- id: alkene-hydroxylation-osmium-permanganate
  type: soft
- id: oxidation-reactions-organic
  type: soft
builds-toward: []
tags:
- ozonolysis
- oxidative cleavage
- ozonide
- Criegee mechanism
- reductive workup
- structure determination
stage: formal-systems
status: validated
---

# Ozonolysis and Oxidative Cleavage of Alkenes

## Core Idea
Ozone breaks a carbon-carbon double bond completely and replaces it with two carbon-oxygen double bonds. Each alkene carbon becomes a carbonyl carbon, so the product depends on what was attached: a carbon bearing two alkyl groups becomes a ketone, and a carbon bearing a hydrogen becomes an aldehyde. A reductive workup, such as dimethyl sulfide or zinc, keeps those aldehydes; an oxidative workup with hydrogen peroxide turns them into carboxylic acids. Because the fragments reveal where the double bond was, ozonolysis is also a tool for working out structures.

## How It's Best Learned
Use the "cut and cap" method: erase the C=C, then put =O on each carbon and read off the products. Practise with acyclic, cyclic and polyene examples, then run the method in reverse to find an unknown alkene from its fragments. Learn the Criegee mechanism after the product rule is secure.

## Common Misconceptions
- Ozonolysis adds two OH groups like OsO₄. (Ozonolysis cleaves both the σ and π bonds of the double bond and gives carbonyl compounds, not a diol.)
- Every ozonolysis gives carboxylic acids. (With a reductive workup, carbons bearing H give aldehydes; acids form only with an oxidative workup such as H₂O₂.)
- Ozonolysis of a cycloalkene gives two separate molecules. (The ring opens but stays one molecule, giving a single dicarbonyl compound.)

## Questions

```yaml
- question: "What are the products of treating 2-methylbut-2-ene with O₃, then (CH₃)₂S?"
  type: multiple-choice
  options: ["Two molecules of acetone", "Acetone and acetaldehyde", "Acetone and acetic acid", "2-Methylbutane-2,3-diol"]
  answer: 1
  explanation: "Cutting (CH₃)₂C=CHCH₃ and capping each carbon with oxygen gives (CH₃)₂C=O, acetone, and CH₃CHO, acetaldehyde. Dimethyl sulfide is a reductive workup, so the aldehyde survives."
- question: "What single product forms when cyclohexene is treated with O₃, then Zn in acetic acid?"
  type: multiple-choice
  options: ["Cyclohexanone", "Hexanedial", "Hexanedioic acid", "Two molecules of propanal"]
  answer: 1
  explanation: "The ring opens at the double bond, and both former alkene carbons, each bearing H, become aldehyde groups. The product is the six-carbon dialdehyde hexanedial. An oxidative workup would give hexanedioic (adipic) acid."
- question: "In an oxidative ozonolysis workup with H₂O₂, aldehyde fragments become carboxylic acids, but ketone fragments are unchanged."
  type: true-false
  answer: true
  explanation: "Hydrogen peroxide oxidizes the C–H bond of an aldehyde to give a carboxylic acid. A ketone carbon has no hydrogen to oxidize, so it stays a ketone."
- question: "An alkene with formula C₆H₁₂ gives only acetone on ozonolysis with reductive workup. What is its structure?"
  type: short-answer
  answer: "2,3-Dimethylbut-2-ene, (CH₃)₂C=C(CH₃)₂."
  explanation: "Two molecules of acetone account for all six carbons. Joining their carbonyl carbons with a double bond gives a symmetrical tetrasubstituted alkene."
```

## Explainer

Most alkene additions keep the carbon skeleton and add atoms across the double bond. Ozonolysis does something more drastic: it breaks the carbon skeleton at the double bond.

The reaction is usually run by bubbling ozone through a solution of the alkene at −78 °C, then adding a second reagent in a workup step. The mechanism, worked out mainly by Rudolf Criegee, has three stages. First, ozone adds across the C=C in one step, forming an unstable ring called a molozonide. Second, the molozonide splits into a carbonyl compound and a carbonyl oxide. Third, these two pieces recombine in a different orientation to form an ozonide, which has the two former alkene carbons joined through oxygens rather than to each other.

The workup decides the final products. In a reductive workup, dimethyl sulfide or zinc with acetic acid reduces the ozonide. Each former alkene carbon ends up as a C=O group. If that carbon carried two carbon groups, it becomes a ketone. If it carried a hydrogen, it becomes an aldehyde. If it was a terminal CH₂, it becomes formaldehyde. In an oxidative workup, hydrogen peroxide is used instead, and any aldehyde is oxidized further to a carboxylic acid. Ketones stay as ketones.

You can predict products with a simple routine. Erase the double bond, write =O on each of its carbons, and apply the workup. For 2-methylbut-2-ene, (CH₃)₂C=CHCH₃, this gives acetone and acetaldehyde. For a ring, the routine opens the ring rather than splitting the molecule. Cyclohexene gives a single six-carbon dialdehyde, hexanedial.

Hot, concentrated potassium permanganate also cleaves alkenes. It behaves like an oxidative workup: ketone carbons give ketones, carbons bearing H give carboxylic acids, and a terminal CH₂ is oxidized all the way to carbon dioxide. Ozonolysis is usually preferred because it is milder and easier to control.

Before spectroscopy became routine, chemists used ozonolysis to locate double bonds. Identify the carbonyl fragments, then join their carbonyl carbons with a double bond, and you recover the original alkene. The same reasoning still appears in problem sets. An alkene C₆H₁₂ that gives only acetone must be 2,3-dimethylbut-2-ene, because two acetone fragments rejoin to (CH₃)₂C=C(CH₃)₂.
