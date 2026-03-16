---
id: money-multiplier-dynamics
title: The Money Multiplier and Money Supply Expansion
domain: economics
course: macroeconomics
prerequisites:
- id: monetary-base-and-money-creation
  type: hard
builds-toward:
- monetary-policy-implementation-and-tools
- monetary-policy-transmission
tags:
- money-supply
- banking
- leverage
stage: abstract-reasoning
status: draft
---

# The Money Multiplier and Money Supply Expansion

## Core Idea
The money multiplier m = M/H describes how much money supply is created from a unit of monetary base. When banks receive deposits, they lend out a fraction (determined by reserve requirements and desired excess reserves) while holding the rest in reserve; these loans become deposits at other banks, starting the process again. The money multiplier is m = 1 / (r + c) where r is the reserve ratio and c is the currency ratio, showing how lending cascades through the system.

## How It's Best Learned
Trace through a sequence of bank deposits and loans to see how an initial deposit expands into multiple deposits across the banking system. Calculate the multiplier for different reserve ratios and observe the relationship.

## Common Misconceptions
- Believing the money multiplier is a fixed constant—it varies with reserve requirements, currency preferences, and banks' willingness to lend.
- Assuming that all monetary base expansion results in the full multiplier effect—in financial crises, banks may not lend and the multiplier collapses.

## Explainer

From your study of monetary base and money creation, you understand the distinction between **high-powered money** (the monetary base H, also called M0) — currency in circulation plus bank reserves — and broad money measures like M1 or M2, which include deposits. The money multiplier describes how the banking system transforms a given stock of base money into a larger stock of money in the broader economy. The mechanism is fractional reserve banking: banks are required (or choose) to hold only a fraction of deposits as reserves, lending the rest out.

Trace the process through a concrete example. Suppose the reserve ratio r = 0.10 and the Fed injects $1,000 of base money into the banking system. Bank A receives $1,000 in deposits, holds $100 in reserves, and lends $900 to a borrower. That borrower spends the $900, which is deposited at Bank B. Bank B holds $90 in reserves and lends $810 to another borrower. Bank C receives $810, holds $81, lends $729. Each round, the lending-and-redepositing cycle creates a new layer of deposits. The total deposits created sum to a geometric series: $1,000 × (1 + 0.9 + 0.81 + ...) = $1,000 × 1/(1−0.9) = $10,000. The simple **deposit multiplier** is 1/r = 10.

The real-world multiplier m = 1/(r + c) adds the **currency ratio** c — the fraction of deposits that the public prefers to hold as cash rather than redepositing. If people drain some of each loan out of the banking system as cash, fewer deposits are created in each round. A higher currency ratio (more cash preference) reduces the multiplier just as a higher reserve ratio does. The formula M = m × H captures the relationship between base money and total money supply: broad money is a multiple of the monetary base, and the central bank influences M by controlling H through open market operations.

The crucial insight from the misconceptions is that the multiplier is not a mechanical constant — it is an equilibrium outcome that depends on bank behavior and public preferences. During the 2008–2009 financial crisis, the Fed injected massive quantities of base money through quantitative easing, but banks chose to hold enormous quantities of **excess reserves** rather than lending them out. The effective reserve ratio r rose sharply, the multiplier collapsed, and the money supply expanded far less than a naïve application of m = 1/r would have predicted. Banks had reason to hoard reserves — loan demand was weak, creditworthy borrowers were scarce, and excess reserves earned interest at the Fed. This experience illustrated that the central bank controls the monetary base directly but influences broad money only indirectly through the banking system's willingness to lend and the public's willingness to borrow and deposit.
