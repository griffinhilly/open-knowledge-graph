---
id: michael-addition-conjugate-addition
title: Conjugate Addition and the Michael Reaction
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enols-and-enolate-chemistry
  type: hard
- id: nucleophilic-addition-to-carbonyls
  type: hard
- id: resonance-in-organic-intermediates
  type: soft
- id: aldol-reaction
  type: soft
- id: organometallic-grignard-organolithium
  type: soft
builds-toward: []
tags:
- conjugate addition
- 1,4-addition
- Michael reaction
- Robinson annulation
- enones
- Gilman reagents
stage: formal-systems
status: validated
---

# Conjugate Addition and the Michael Reaction

## Core Idea
In an α,β-unsaturated carbonyl compound, resonance makes both the carbonyl carbon and the β carbon electrophilic. A nucleophile can therefore add directly to the carbonyl (1,2-addition) or to the β carbon (conjugate, or 1,4-addition). Stabilized, softer nucleophiles such as β-dicarbonyl enolates, cuprates, amines and thiols favor conjugate addition. The Michael reaction is the conjugate addition of an enolate to such an acceptor, and it builds 1,5-dicarbonyl compounds.

## How It's Best Learned
Draw the resonance form of an enone that puts positive charge on the β carbon before writing any mechanism. Then sort nucleophiles into those that add 1,2 (Grignard and organolithium reagents) and those that add 1,4 (Gilman reagents and stabilized enolates). Practise the Robinson annulation as two reactions you already know, a Michael addition followed by an intramolecular aldol condensation.

## Common Misconceptions
- Nucleophiles always attack the carbonyl carbon of an enone. (The β carbon is also electrophilic, and many nucleophiles add there.)
- Grignard reagents and Gilman reagents give the same product with an enone. (Grignard reagents usually add 1,2 to give an allylic alcohol, while lithium dialkylcuprates add 1,4 to give a β-substituted ketone.)
- The Michael product keeps the C=C double bond. (The double bond is used up; the intermediate enolate is protonated at the α carbon to give a saturated carbonyl compound.)

## Questions

```yaml
- question: "Which reagent adds mainly in a conjugate (1,4) fashion to cyclohex-2-en-1-one?"
  type: multiple-choice
  options: ["CH₃MgBr", "CH₃Li", "(CH₃)₂CuLi", "NaBH₄ with CeCl₃"]
  answer: 2
  explanation: "Lithium dimethylcuprate, a Gilman reagent, delivers a methyl group to the β carbon, giving 3-methylcyclohexanone. Methyl Grignard and methyllithium mainly add to the carbonyl carbon, and NaBH₄ with CeCl₃ (Luche conditions) reduces the carbonyl 1,2."
- question: "In a conjugate addition, the nucleophile forms a new bond to the carbonyl carbon."
  type: true-false
  answer: false
  explanation: "In conjugate addition the nucleophile bonds to the β carbon. The electrons move through the C=C and onto oxygen, forming an enolate that is later protonated at the α carbon."
- question: "The enolate of diethyl malonate adds to methyl vinyl ketone. What relationship do the new product's carbonyl groups have?"
  type: multiple-choice
  options: ["1,2-dicarbonyl", "1,3-dicarbonyl only", "1,5-dicarbonyl", "No carbonyl survives"]
  answer: 2
  explanation: "The donor's α carbon bonds to the acceptor's β carbon. Counting from an ester carbonyl through the new bond to the ketone carbonyl gives a 1,5 relationship, the signature of a Michael product."
- question: "Describe the two steps of a Robinson annulation and the type of product it forms."
  type: short-answer
  answer: "First, a ketone enolate adds to an α,β-unsaturated ketone such as methyl vinyl ketone in a Michael reaction, giving a 1,5-diketone. Second, an intramolecular aldol condensation closes a ring and dehydrates, giving a cyclohexenone."
  explanation: "The annulation combines two known reactions to build a new six-membered ring. Robert Robinson developed it, and it has been widely used in steroid and terpene synthesis."
```

## Explainer

Most nucleophiles attack a carbonyl at its carbon. In an α,β-unsaturated carbonyl compound, such as an enone, a second site appears. Draw the resonance form that moves the C=C electrons toward the carbonyl and pushes the C=O electrons onto oxygen. That form places a positive charge on the β carbon. So the molecule has two electrophilic sites: the carbonyl carbon and the β carbon.

Attack at the carbonyl carbon is called 1,2-addition. Attack at the β carbon is called conjugate addition or 1,4-addition, because the atoms involved are numbered 1 to 4 from oxygen. In a conjugate addition the nucleophile bonds to the β carbon, and the electrons flow through the double bond onto oxygen. The result is an enolate. When the enolate is protonated, it gives back a carbonyl group, now with the nucleophile on the β carbon and no C=C left.

Which path a nucleophile takes depends largely on its character. Highly reactive, strongly basic nucleophiles, such as Grignard and organolithium reagents, usually add 1,2 and give allylic alcohols. Weaker or more stabilized nucleophiles tend to add 1,4, because conjugate addition gives the more stable product. These include lithium dialkylcuprates (Gilman reagents), amines, thiols, cyanide and enolates of β-dicarbonyl compounds. Gilman reagents are the standard way to attach an alkyl group to the β carbon.

When the nucleophile is an enolate, the reaction is called a Michael reaction, after Arthur Michael, who reported it in 1887. The enolate is the Michael donor, and the unsaturated compound is the Michael acceptor. Malonic esters, β-keto esters and other doubly stabilized enolates are good donors. Enones, unsaturated esters and unsaturated nitriles are common acceptors. The new carbon-carbon bond joins the donor's α carbon to the acceptor's β carbon, and the two carbonyl groups end up in a 1,5 relationship.

A 1,5-dicarbonyl compound is set up to close a six-membered ring by an intramolecular aldol reaction. Combining the two steps gives the Robinson annulation, developed by Robert Robinson. A ketone enolate adds to methyl vinyl ketone, and the resulting 1,5-diketone then cyclizes and dehydrates to form a cyclohexenone.

When you meet an unsaturated carbonyl, check both electrophilic sites before choosing a product.
