---
id: bank-runs-and-deposit-insurance
title: Bank Runs, Deposit Insurance, and the Lender of Last Resort
domain: economics
course: macroeconomics
prerequisites:
- id: money-supply-and-money-creation
  type: hard
- id: central-banking-and-the-fed
  type: soft
- id: nash-equilibrium-microeconomics
  type: soft
builds-toward:
- financial-frictions-amplification
- financial-system-interconnectedness
tags:
- banking
- bank runs
- liquidity
- deposit insurance
- lender of last resort
- financial crises
- Diamond-Dybvig
stage: formal-systems
status: validated
---

# Bank Runs, Deposit Insurance, and the Lender of Last Resort

## Core Idea
Banks fund long-term, hard-to-sell loans with deposits that customers can withdraw at any time, so they keep only a fraction of deposits as reserves. This maturity transformation is useful, but it makes banks fragile: if many depositors withdraw at once, even a sound bank cannot pay everyone without selling assets at a loss. Because each depositor gains by withdrawing before others do, fear of a run can cause a run. Deposit insurance and central bank lending to solvent but illiquid banks remove the reason to run, at the cost of weakening depositors' incentive to watch how banks take risks.

## How It's Best Learned
Set up a small bank balance sheet with 10% reserves and 90% loans that sell at a discount if sold early. Ask what happens if 5% of depositors withdraw, then 40%. Then frame the depositor's choice as a game with two equilibria, "everyone waits" and "everyone runs," and show how a government guarantee removes the run equilibrium.

## Common Misconceptions
- Only banks that have made bad loans suffer runs. (A solvent bank can fail in a run because its loans cannot be turned into cash quickly at full value; liquidity and solvency are different problems.)
- Deposit insurance works mainly by paying depositors after failures. (Its main effect is to prevent runs; insured depositors have no reason to rush, so many runs never start.)
- A lender of last resort should rescue every troubled bank. (The classic guidance is to lend to solvent banks against good collateral at a penalty rate; lending to insolvent banks shifts losses to the public and invites risk-taking.)

## Questions

```yaml
- question: "A bank holds $10 million in reserves and $90 million in sound loans, funded by $92 million in deposits and $8 million of owners' equity. The loans would sell for only 60% of their value if sold today. Depositors suddenly demand $40 million. What happens?"
  type: multiple-choice
  options: ["The bank pays easily from reserves and loses nothing", "To raise the other $30 million it must sell $50 million of loans, losing $20 million, which exceeds its equity and leaves it insolvent", "The money multiplier automatically raises the bank's reserves", "Depositors must accept interest instead of cash"]
  answer: 1
  explanation: "Reserves cover $10 million. Raising $30 million more at 60 cents on the dollar means selling $50 million of loans, a $20 million loss. That loss is larger than the $8 million equity cushion, so the run itself turns a sound bank into an insolvent one."
- question: "In the Diamond-Dybvig model of banking, a bank run can occur even when no depositor has new information that the bank's loans are bad."
  type: true-false
  answer: true
  explanation: "The model has two equilibria. If each depositor expects others to wait, waiting is best. If each expects others to withdraw, withdrawing early is best, because late withdrawers may get nothing. A run can therefore be self-fulfilling, triggered by expectations alone."
- question: "Which drawback of deposit insurance do economists most often point to?"
  type: multiple-choice
  options: ["It increases the number of bank runs", "It reduces depositors' incentive to monitor bank risk, which can encourage banks to take more risk", "It makes bank deposits illiquid", "It forces banks to hold 100% reserves"]
  answer: 1
  explanation: "When deposits are guaranteed, depositors care less about how safely a bank invests. This is a form of moral hazard, and it is one reason insured banks are also subject to capital requirements and supervision."
- question: "Explain the difference between a bank being illiquid and a bank being insolvent, and why the distinction matters for a lender of last resort."
  type: short-answer
  answer: "An illiquid bank has assets worth more than its liabilities but cannot turn them into cash fast enough to meet withdrawals. An insolvent bank has assets worth less than its liabilities. A lender of last resort can lend safely to an illiquid bank against good collateral and stop a run, but lending to an insolvent bank only delays losses and shifts them to the lender."
  explanation: "This distinction underlies Walter Bagehot's 1873 advice in Lombard Street: lend freely, at a high rate, against good collateral."
```

## Explainer
From money creation you know that banks keep only a fraction of deposits as reserves and lend the rest. That arrangement does something valuable. Savers get deposits they can withdraw whenever they like, and borrowers get loans that last years. The bank stands between them, turning short-term, liquid claims into long-term, illiquid ones. This is called maturity transformation.

The same arrangement creates a weakness. On a normal day only a few depositors withdraw, and reserves cover them. But loans cannot be sold quickly at full value. If many depositors come at once, the bank must sell loans at a discount, and it may run out of cash before everyone is paid. Depositors know this. If you think others are about to withdraw, your best move is to withdraw first. So fear of a run can cause one. Douglas Diamond and Philip Dybvig formalized this in a 1983 model with two equilibria: one where everyone waits and the bank is fine, and one where everyone runs and the bank fails. Nothing about the bank's loans needs to change to move from one to the other. Diamond and Dybvig shared the 2022 Nobel Memorial Prize in Economic Sciences with Ben Bernanke, who studied how bank failures deepened the Great Depression.

Runs can spread. When one bank fails, depositors at similar banks may fear the same, and banks selling assets at once push prices down for everyone. In the early 1930s, waves of runs closed thousands of American banks, which shrank the money supply and credit.

Two policies address the problem. The first is **deposit insurance**. In the United States, the Banking Act of 1933 created the Federal Deposit Insurance Corporation, which today insures deposits up to $250,000 per depositor, per insured bank, for each account ownership category. Insured depositors have no reason to rush, so the run equilibrium largely disappears. The second is a **lender of last resort**: a central bank that lends cash to a bank facing withdrawals, accepting its loans as collateral. Walter Bagehot's 1873 advice was to lend freely, at a high rate, against good collateral.

Both tools have costs. Guarantees reduce depositors' incentive to watch how banks invest, a form of moral hazard, so insured banks face capital rules and supervision. Uninsured deposits can still run. In March 2023, depositors at Silicon Valley Bank, most of whose deposits exceeded the insurance limit, tried to withdraw tens of billions of dollars in a single day, and regulators closed the bank.
