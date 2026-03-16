---
id: money-supply-and-money-creation
title: Money Supply and the Money Multiplier
domain: economics
course: macroeconomics
prerequisites:
- id: money-and-its-functions
  type: hard
builds-toward:
- central-banking-and-the-fed
- quantity-theory-of-money
- interest-rates-and-loanable-funds
tags:
- money-creation
- fractional-reserve
- money-multiplier
- required-reserves
- banking
stage: abstract-reasoning
status: validated
---

# Money Supply and the Money Multiplier

## Core Idea
Banks create money through the process of fractional reserve banking: they hold only a fraction of deposits as reserves and lend out the rest, which gets re-deposited and re-lent. Starting from a new deposit, the money multiplier (1 / reserve ratio) describes the maximum eventual increase in the money supply. In practice, the multiplier is smaller because banks hold excess reserves and households hold cash outside the banking system. Central banks control the monetary base (currency + reserves), and the money supply emerges from the banking system's lending behavior.

## How It's Best Learned
Trace a $1,000 deposit through several rounds of a T-account (balance sheet) example with a 10% reserve requirement: loan → deposit → loan. Calculate total new money created. Then discuss what happens when banks hold excess reserves.

## Common Misconceptions
- Banks do not lend out existing deposits; they create new deposits when they make loans — lending precedes deposits in a modern banking system.
- The money multiplier is a theoretical maximum, not a precise prediction of actual money creation.
- Central banks do not 'print money' in the simple sense; they expand the monetary base, and private banks create most money.

## Explainer

From your prerequisite study of money and its functions, you know that money is whatever serves as a medium of exchange, unit of account, and store of value. Now the question is: where does money come from? The answer is more surprising than it first appears. Most of the money in a modern economy is not created by governments printing banknotes — it is created by commercial banks when they make loans. Understanding this process requires following the T-accounts (balance sheets) of a banking system step by step.

Start with a single deposit. A household deposits $1,000 in cash at Bank A. Bank A's liabilities rise by $1,000 (it owes the depositor $1,000) and its assets rise by $1,000 in cash. If the **required reserve ratio** is 10%, Bank A must hold $100 in reserve but can lend out $900. When Bank A makes a $900 loan, it does not hand over cash — it credits $900 to the borrower's deposit account. This is the crucial step: the loan *creates* a new deposit of $900. The borrower spends it; that $900 eventually arrives as a deposit at Bank B. Bank B holds 10% ($90) and lends out $810, which becomes a deposit at Bank C. At each stage, 90% is re-lent and re-deposited. Summing the geometric series: total deposits created = $1,000 × 1/(reserve ratio) = $1,000 × 10 = $10,000. The **money multiplier** is 1/r = 10.

The multiplier formula gives a theoretical ceiling, not a prediction of what actually happens. Two frictions shrink the real-world multiplier. First, banks voluntarily hold **excess reserves** beyond the regulatory minimum — especially after the 2008 crisis, when the Federal Reserve began paying interest on reserves, making it attractive for banks to park funds at the Fed rather than lend. Second, households hold some fraction of money as **cash** outside the banking system. Every dollar held as cash rather than a bank deposit is a dollar that cannot be re-lent, breaking the chain. Because of these leakages, the actual money multiplier is typically well below the simple 1/r formula.

The central bank controls the **monetary base** — currency in circulation plus bank reserves — through open market operations (buying or selling government bonds). When the Fed buys bonds, it credits the selling bank's reserve account, expanding the base. But the Fed cannot directly control how much of that base gets multiplied into broad money — that depends on banks' willingness to lend and households' preferences for cash versus deposits. This is why quantitative easing (large-scale asset purchases) expanded the monetary base dramatically after 2008 without producing proportional money supply growth or inflation: banks held the extra reserves rather than lending them out. The money multiplier collapsed. This history is a reminder that the monetary base and the money supply are related but not the same thing, and that central bank control over money is indirect — mediated through the banking system's lending decisions.
