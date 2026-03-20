---
id: sn1-sn2-reaction-selectivity-factors
title: 'SN1 vs SN2 Selectivity: Factors and Competition'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-reaction
  type: hard
- id: sn2-reaction
  type: hard
- id: nucleophilicity-and-leaving-groups
  type: hard
- id: polar-protic-aprotic-solvents
  type: hard
builds-toward:
- zaitsevs-rule-hofmann-elimination
tags:
- mechanism
- selectivity
- substrate-structure
- nucleophile
- solvent
stage: advanced
status: draft
---

# SN1 vs SN2 Selectivity: Factors and Competition

## Core Idea
SN1 occurs on tertiary substrates with weak nucleophiles in polar protic solvents (carbocation forms first). SN2 occurs on primary/secondary substrates with strong nucleophiles in polar aprotic solvents (single transition state, inversion). The selectivity depends on substrate steric hindrance (1° → SN2; 3° → SN1), nucleophile strength/basicity, and solvent polarity. Competing E1/E2 eliminations also occur.

## How It's Best Learned
Sketch transition states for SN1 (carbocation intermediate) and SN2 (back-side attack). Predict products for different substrates/nucleophiles. Consider which factor dominates in each scenario (steric vs electronic).

## Common Misconceptions
SN1 doesn't always mean racemization—some substrate/solvent pairs show modest stereoselectivity. SN2 with a good nucleophile still competes with E2. Secondary substrates can go either SN1 or SN2 depending on solvent and nucleophile strength.

## Explainer

You have learned the SN1 and SN2 mechanisms individually — now the real challenge is predicting which one wins when both are possible. The answer comes from evaluating four factors: **substrate structure**, **nucleophile strength**, **solvent**, and **leaving group**. No single factor decides the outcome; it is the combination that tips the balance.

**Substrate structure** is the most important factor. Primary substrates strongly favor SN2 because they are sterically unhindered — the nucleophile can easily access the electrophilic carbon from the back side. Tertiary substrates strongly favor SN1 because the resulting carbocation is stabilized by three alkyl groups through hyperconjugation and induction, and because steric crowding blocks the back-side attack required for SN2. Secondary substrates are the borderline case — either mechanism is possible, and you must look at the other factors to decide. Think of it as a tug-of-war: steric crowding pulls toward SN1 (dissociative), while openness pulls toward SN2 (associative).

**Nucleophile strength** breaks ties for secondary substrates and reinforces trends elsewhere. Strong nucleophiles (like hydroxide, cyanide, or iodide) push reactions toward SN2 because they actively attack the substrate — rate depends on nucleophile concentration. Weak nucleophiles (like water or alcohols) favor SN1 because they cannot force the displacement but can readily trap a carbocation once it forms. **Solvent** works in concert: polar aprotic solvents (DMSO, acetone, DMF) favor SN2 by leaving the nucleophile "naked" and reactive, while polar protic solvents (water, alcohols) favor SN1 by stabilizing the carbocation intermediate through solvation and simultaneously weakening nucleophilicity through hydrogen bonding.

The practical decision tree works like this: identify the substrate class first. If it is methyl or primary, predict SN2 (unless the nucleophile is very weak). If it is tertiary, predict SN1. If it is secondary, check the nucleophile — strong nucleophile in a polar aprotic solvent means SN2; weak nucleophile in a polar protic solvent means SN1. But always remember the elephant in the room: **elimination competes with substitution**. Strong bases at elevated temperatures favor E2 over SN2, and high temperatures push SN1 toward E1. A complete prediction considers all four pathways — SN1, SN2, E1, E2 — not just the two substitution mechanisms.
