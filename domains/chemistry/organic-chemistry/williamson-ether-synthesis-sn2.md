---
id: williamson-ether-synthesis-sn2
title: Williamson Ether Synthesis via SN2
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: alcohols-and-ethers
  type: hard
- id: sn2-mechanism-kinetics-and-factors
  type: hard
builds-toward:
- ether-cleavage-and-fragmentation
tags:
- williamson-ether-synthesis
- sn2
- alkoxide
- ether-formation
stage: formal-systems
status: validated
---

# Williamson Ether Synthesis via SN2

## Core Idea
Williamson ether synthesis couples an alkoxide nucleophile (RO⁻) with a primary alkyl halide or tosylate in an SN2 reaction to form an ether. The reaction works best with primary substrates to avoid elimination. This is the most general method for ether synthesis and is widely used because the regiochemistry is predictable: the alkoxide attacks the alkyl halide at the carbon bearing the leaving group.

## Questions

```yaml
- question: "You want to synthesize tert-butyl methyl ether (CH₃OC(CH₃)₃) via Williamson synthesis. Which reagent combination is correct?"
  type: multiple-choice
  options:
    - "tert-Butyl alcohol + NaH, then methyl iodide — the tert-butoxide attacks the primary methyl electrophile"
    - "Methanol + NaH, then tert-butyl bromide — the methoxide attacks the tert-butyl electrophile"
    - "tert-Butyl alcohol reacted directly with methanol under acidic conditions"
    - "Sodium tert-butoxide reacted with tert-butyl bromide in DMSO"
  answer: 0
  explanation: "The SN2 reaction requires a primary (or methyl) electrophile. Methyl iodide is the best possible SN2 substrate — no steric hindrance whatsoever. tert-Butyl alcohol is deprotonated with NaH to form tert-butoxide, which serves as the nucleophile. Option B is the classic disconnection error: using tert-butyl bromide as the electrophile places the SN2 reaction at a tertiary carbon, where the bulky alkoxide base instead abstracts a β-proton (E2 elimination), yielding isobutene instead of the ether. Whenever one fragment is tertiary, it must be the alkoxide, never the halide."

- question: "Why does Williamson ether synthesis fail when a tertiary alkyl halide is used as the electrophile?"
  type: multiple-choice
  options:
    - "Tertiary alkyl halides cannot form a leaving group because the C–X bond is too strong"
    - "The alkoxide is a strong base; at a tertiary substrate the backside carbon is too hindered for SN2 attack, so the alkoxide abstracts a β-proton instead, giving E2 elimination"
    - "Tertiary carbons are too electronegative to be attacked by oxygen nucleophiles"
    - "The reaction produces a carbocation intermediate at the tertiary center that immediately rearranges"
  answer: 1
  explanation: "Alkoxide ions are simultaneously strong nucleophiles and strong bases. For primary substrates, the backside is accessible and SN2 dominates. For tertiary substrates, three substituents block backside approach, making SN2 effectively impossible — but the exposed β-hydrogens are easily abstracted. The alkoxide acts as a base (E2 path) instead of a nucleophile (SN2 path), and the product is an alkene, not an ether. Option D is wrong: Williamson synthesis is strictly SN2 and does not proceed through carbocation intermediates."

- question: "In Williamson ether synthesis, the alkoxide nucleophile should always be derived from the more substituted (more hindered) alcohol."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The governing rule is not which alcohol is more substituted — it is that the *electrophilic alkyl halide* must be primary. The alkoxide can come from any alcohol, including tertiary ones. When making tert-butyl methyl ether, the tert-butyl group correctly becomes the alkoxide (nucleophile) and methyl becomes the halide (electrophile) — even though tert-butoxide is highly hindered — because the alternative (tert-butyl halide as electrophile) gives only elimination. Substitution level of the alkoxide is not the relevant constraint; substitution level of the electrophile is."

- question: "Tosylates (OTs) can replace alkyl halides as the electrophilic partner in Williamson ether synthesis because the tosylate group is a competent leaving group in SN2 reactions."
  type: true-false
  answer: true
  explanation: "Tosylates are prepared from alcohols by reaction with toluenesulfonyl chloride (TsCl). The tosylate group (–OTs) is a good leaving group — comparable to iodide — because the negative charge is stabilized by the sulfonyl group and aromatic ring. The alkoxide attacks the carbon bearing the tosylate with inversion, displacing –OTs exactly as it would displace –Br or –I. Tosylates are sometimes preferred when the corresponding alkyl halide is inconvenient to prepare or unstable."

- question: "Explain the disconnection analysis used in planning a Williamson synthesis for an unsymmetrical ether, and identify what governs which fragment becomes the alkoxide versus the alkyl halide."
  type: short-answer
  answer: "To plan the synthesis of R–O–R', mentally break the C–O bond on one side and ask which fragment should be the nucleophile (alkoxide, RO⁻) and which should be the electrophile (alkyl halide, R'–X). The governing rule is that the alkyl halide must be primary — or methyl — to avoid E2 elimination competing with SN2. So you break the bond such that the primary carbon becomes the halide and the other fragment (which may be secondary or tertiary) becomes the alkoxide. If both sides are primary, either disconnection works. If one side is tertiary, it must become the alkoxide without exception — the tertiary group cannot serve as the electrophile."
  explanation: "Disconnection analysis is the key synthetic planning skill. The synthesis only works when the SN2 step occurs at an unhindered carbon. Choosing the wrong disconnection — putting a secondary or tertiary carbon on the halide side — gives elimination instead of substitution. The ability to recognize and apply the correct disconnection distinguishes students who understand the mechanism from those who have only memorized reaction names."
```

## Explainer

You already understand that SN2 reactions involve backside attack of a nucleophile on an electrophilic carbon, displacing a leaving group in a single concerted step. The **Williamson ether synthesis** is one of the most important applications of this mechanism: an **alkoxide ion** (RO⁻), formed by deprotonating an alcohol with a strong base like NaH, attacks a **primary alkyl halide** (or tosylate) to form a new C–O bond. The product is an ether, R–O–R'.

The power of this reaction lies in its predictability. Because it proceeds through SN2, the outcome follows all the rules you learned for that mechanism. **Primary substrates** work best because the transition state is unhindered — the nucleophile can access the electrophilic carbon easily. **Secondary substrates** are borderline: the bulky alkoxide is a strong base as well as a nucleophile, so E2 elimination competes heavily. **Tertiary substrates** are effectively useless — elimination dominates completely, and you get alkene instead of ether. This means that when planning a Williamson synthesis for an unsymmetrical ether like methyl tert-butyl ether, you must choose the correct disconnection: the tert-butyl group must come from the alkoxide (since tert-butoxide is easily formed and acts as the nucleophile), while the methyl group comes from a methyl halide (an excellent SN2 substrate). Reversing this assignment — trying to use a tert-butyl halide as the electrophile — would give elimination.

The practical setup is straightforward. First, deprotonate the alcohol with a strong base (NaH is standard because it produces H₂ gas as the only byproduct and drives the reaction forward). The resulting alkoxide then attacks the alkyl halide in a polar aprotic or mildly protic solvent. Tosylates (OTs) work just as well as halides and are sometimes preferred because they are easily prepared from the corresponding alcohol and toluenesulfonyl chloride. The key synthetic planning skill is the **disconnection analysis**: for any target ether R–O–R', break the C–O bond on the less hindered side to identify which fragment becomes the alkoxide and which becomes the electrophile. Choose the combination that puts the SN2 reaction on the least substituted carbon, and the synthesis will work cleanly.
