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
status: draft
---

# Grignard Reagents and Carbon-Carbon Bond Formation

## Core Idea
Grignard reagents (RMgX) are powerful nucleophiles formed from alkyl/aryl halides and magnesium. They attack electrophilic carbons in carbonyls (aldehydes, ketones, esters, CO₂) to form C-C bonds and (after aqueous workup) alcohols or carboxylic acids. Grignards also react with alkyl halides (SN2-like, for 1° halides), epoxides (ring-opening), and carbon dioxide. They cannot tolerate water, alcohols, amines, or carbonyl groups in the starting halide.

## Explainer

You already know that Grignard reagents (RMgX) are formed by inserting magnesium into a carbon-halogen bond, and you understand nucleophilic addition to carbonyls. The Grignard reaction combines these ideas into one of organic chemistry's most versatile tools for building **carbon-carbon bonds**. The carbon bonded to magnesium is effectively a carbanion — an extraordinarily powerful nucleophile and strong base. This carbanion character is what makes Grignard reagents so reactive and so useful, but it is also what makes them so demanding about reaction conditions.

The most important Grignard reactions are additions to carbonyl compounds. When a Grignard reagent attacks an **aldehyde** (other than formaldehyde), the carbanion adds to the electrophilic carbonyl carbon, forming a magnesium alkoxide. Aqueous acid workup protonates the alkoxide to give a **secondary alcohol**. Attack on **formaldehyde** (H₂C=O) gives a primary alcohol, while attack on a **ketone** gives a tertiary alcohol. Attack on an **ester** is a double addition — the first equivalent of Grignard adds, the alkoxide leaves (producing a ketone intermediate), and a second equivalent adds to that ketone, yielding a tertiary alcohol with two identical R groups from the Grignard. Attack on **CO₂** followed by acid workup gives a carboxylic acid with one more carbon than the original halide. Each of these reactions follows the same mechanistic pattern: nucleophilic carbon attacks electrophilic carbon, forming a new C–C bond.

The critical constraint on Grignard chemistry is **functional group compatibility**. Because the Grignard carbon is such a strong base and nucleophile, it reacts instantly with any acidic proton — water, alcohols, terminal alkynes, amines, and carboxylic acids all destroy the reagent by protonation before it can reach the intended electrophile. It also reacts with any electrophilic functional group in the same molecule, so you cannot prepare a Grignard from a substrate that contains a ketone, aldehyde, ester, or epoxide elsewhere in the structure. All reactions must be run in anhydrous, aprotic solvents (typically diethyl ether or THF), and glassware must be thoroughly dried. These restrictions are not minor inconveniences — they are the central strategic consideration in planning any synthesis that uses a Grignard reagent.

In retrosynthetic thinking, Grignard disconnections are among the first you should consider whenever you see an alcohol target. Ask: which C–C bond adjacent to the hydroxyl could have been formed by a Grignard addition? Then identify the carbonyl electrophile and the alkyl halide precursor. A secondary alcohol can be disconnected to an aldehyde plus RMgX in two different ways (cut either C–C bond flanking the carbinol carbon). A tertiary alcohol offers three possible disconnections. This flexibility makes the Grignard reaction a cornerstone of synthetic strategy.
