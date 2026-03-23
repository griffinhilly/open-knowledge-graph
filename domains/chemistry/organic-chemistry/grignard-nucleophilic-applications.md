---
id: grignard-nucleophilic-applications
title: Grignard Reagents and Carbon-Carbon Bond Formation
domain: chemistry
course: organic-chemistry
prerequisites:
- id: grignard-reagent
  type: hard
- id: nucleophilic-addition-to-carbonyls
  type: hard
tags:
- grignard
- c-c-coupling
- nucleophile
- organometallic
- synthetic-strategy
stage: formal-systems
status: validated
---

# Grignard Reagents and Carbon-Carbon Bond Formation

## Core Idea
Grignard reagents (RMgX) are powerful nucleophiles formed from alkyl/aryl halides and magnesium. They attack electrophilic carbons in carbonyls (aldehydes, ketones, esters, CO₂) to form C-C bonds and (after aqueous workup) alcohols or carboxylic acids. Grignards also react with alkyl halides (SN2-like, for 1° halides), epoxides (ring-opening), and carbon dioxide. They cannot tolerate water, alcohols, amines, or carbonyl groups in the starting halide.

## Questions

```yaml
- question: "A Grignard reagent RMgX is added to excess ethyl acetate (CH₃COOEt), then quenched with aqueous acid. What is the major product?"
  type: multiple-choice
  options:
    - "A secondary alcohol — the Grignard adds once to the ester carbonyl"
    - "A tertiary alcohol with two R groups flanking the central carbon"
    - "A carboxylic acid — esters hydrolyze under Grignard conditions"
    - "An aldehyde — the ester is partially reduced by the Grignard"
  answer: 1
  explanation: "Esters undergo double addition. The first equivalent of Grignard adds to give a tetrahedral intermediate, which collapses by expelling ethoxide to give a ketone intermediate. That ketone is more reactive than the original ester, so a second Grignard equivalent attacks immediately, yielding a tertiary alcohol in which two R groups (from the Grignard) and one methyl group (from the ester carbonyl carbon) surround the central carbon. You cannot stop the reaction at the ketone stage — option A (single addition) would only apply to aldehydes or ketones, not esters."

- question: "A chemist wants to prepare 2-phenyl-2-propanol via a Grignard reaction. Which combination of starting materials is correct?"
  type: multiple-choice
  options:
    - "PhMgBr + acetone (propan-2-one)"
    - "PhMgBr + acetaldehyde (ethanal)"
    - "CH₃MgBr + benzaldehyde (PhCHO)"
    - "PhMgBr + formaldehyde (methanal)"
  answer: 0
  explanation: "2-Phenyl-2-propanol is Ph–C(CH₃)₂–OH, a tertiary alcohol. Retrosynthetic disconnection of the C–C bond to the carbinol carbon gives PhMgBr + acetone (CH₃COCH₃): phenyl adds to the ketone carbon, which already bears two methyl groups, giving the correct tertiary alcohol. Option B gives Ph–CH(OH)–CH₃ (a secondary alcohol), option C gives the same secondary alcohol from the other direction, and option D gives Ph–CH₂OH (a primary alcohol)."

- question: "A Grignard reagent can be prepared from an alkyl halide that also contains a ketone group elsewhere in the molecule."
  type: true-false
  answer: false
  explanation: "False. The Grignard carbon is an extremely powerful nucleophile and base that immediately reacts with any electrophilic functional group — including ketones, aldehydes, and esters — in the same molecule. An intramolecular reaction would occur before the reagent could be isolated and used synthetically. This functional group incompatibility is one of the central strategic constraints in Grignard chemistry: the starting halide must contain no carbonyl groups, acidic protons (OH, NH, COOH), or other electrophilic sites."

- question: "Treating a Grignard reagent with CO₂ followed by aqueous acid workup produces a carboxylic acid with one more carbon than the original alkyl halide."
  type: true-false
  answer: true
  explanation: "True. CO₂ acts as a one-carbon electrophile. The Grignard carbanion (R–MgX) attacks the electrophilic carbon of CO₂ to form a magnesium carboxylate (R–CO₂MgX). Aqueous acid workup protonates this to give R–COOH — a carboxylic acid containing exactly one more carbon than the R group derived from the original halide R–X. This reaction is a reliable route to carboxylic acids in synthesis."

- question: "Why does a Grignard reagent attacking an ester yield a tertiary alcohol rather than the secondary alcohol one might expect by analogy with aldehyde additions?"
  type: short-answer
  answer: "Esters have a leaving group (the alkoxide) attached to the carbonyl carbon; aldehydes do not. The first Grignard addition to an ester generates a tetrahedral intermediate that collapses by expelling the alkoxide, regenerating a carbonyl in the form of a ketone. Because this ketone is more electrophilic than the original ester, a second equivalent of Grignard attacks immediately. The result is a tertiary alcohol with two R groups from the Grignard — not the secondary alcohol that would form if the reaction stopped after one addition."
  explanation: "The mechanistic key is leaving group elimination: esters can unmask a ketone after the first addition, whereas aldehydes and ketones have no leaving group and simply give alkoxides that are protonated on workup. This 'double addition' is unavoidable under normal conditions, which is why esters are specifically chosen (or avoided) in retrosynthetic planning depending on whether a tertiary alcohol is desired."
```

## Explainer

You already know that Grignard reagents (RMgX) are formed by inserting magnesium into a carbon-halogen bond, and you understand nucleophilic addition to carbonyls. The Grignard reaction combines these ideas into one of organic chemistry's most versatile tools for building **carbon-carbon bonds**. The carbon bonded to magnesium is effectively a carbanion — an extraordinarily powerful nucleophile and strong base. This carbanion character is what makes Grignard reagents so reactive and so useful, but it is also what makes them so demanding about reaction conditions.

The most important Grignard reactions are additions to carbonyl compounds. When a Grignard reagent attacks an **aldehyde** (other than formaldehyde), the carbanion adds to the electrophilic carbonyl carbon, forming a magnesium alkoxide. Aqueous acid workup protonates the alkoxide to give a **secondary alcohol**. Attack on **formaldehyde** (H₂C=O) gives a primary alcohol, while attack on a **ketone** gives a tertiary alcohol. Attack on an **ester** is a double addition — the first equivalent of Grignard adds, the alkoxide leaves (producing a ketone intermediate), and a second equivalent adds to that ketone, yielding a tertiary alcohol with two identical R groups from the Grignard. Attack on **CO₂** followed by acid workup gives a carboxylic acid with one more carbon than the original halide. Each of these reactions follows the same mechanistic pattern: nucleophilic carbon attacks electrophilic carbon, forming a new C–C bond.

The critical constraint on Grignard chemistry is **functional group compatibility**. Because the Grignard carbon is such a strong base and nucleophile, it reacts instantly with any acidic proton — water, alcohols, terminal alkynes, amines, and carboxylic acids all destroy the reagent by protonation before it can reach the intended electrophile. It also reacts with any electrophilic functional group in the same molecule, so you cannot prepare a Grignard from a substrate that contains a ketone, aldehyde, ester, or epoxide elsewhere in the structure. All reactions must be run in anhydrous, aprotic solvents (typically diethyl ether or THF), and glassware must be thoroughly dried. These restrictions are not minor inconveniences — they are the central strategic consideration in planning any synthesis that uses a Grignard reagent.

In retrosynthetic thinking, Grignard disconnections are among the first you should consider whenever you see an alcohol target. Ask: which C–C bond adjacent to the hydroxyl could have been formed by a Grignard addition? Then identify the carbonyl electrophile and the alkyl halide precursor. A secondary alcohol can be disconnected to an aldehyde plus RMgX in two different ways (cut either C–C bond flanking the carbinol carbon). A tertiary alcohol offers three possible disconnections. This flexibility makes the Grignard reaction a cornerstone of synthetic strategy.
