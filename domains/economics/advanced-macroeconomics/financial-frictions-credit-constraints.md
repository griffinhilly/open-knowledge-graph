---
id: financial-frictions-credit-constraints
title: Financial Frictions and Credit Constraints
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: asset-pricing-macro
  type: soft
- id: information-asymmetry
  type: hard
tags:
- financial-frictions
- credit-constraints
- lending
stage: expert
status: draft
---

# Financial Frictions and Credit Constraints

## Core Idea
Financial frictions arise when lenders have limited information about borrowers (adverse selection) or borrowers cannot be perfectly monitored (moral hazard). These frictions create credit constraints: borrowers can only borrow against collateral, or face interest rates that vary with their creditworthiness. Financial crises occur when collateral values plummet, suddenly tightening credit constraints and reducing investment and consumption. The interaction between the financial sector and real economy creates powerful amplification mechanisms that magnify real shocks.

## Questions

```yaml
- question: "A bank lends to small businesses but cannot monitor how borrowers use the funds. Borrowers have an incentive to take riskier projects than agreed because they keep any upside profit while the bank bears losses if the project fails. This is an example of:"
  type: multiple-choice
  options:
    - "Adverse selection, because the bank cannot identify risky borrowers before lending"
    - "Moral hazard, because the borrower's behavior changes after the loan is made"
    - "Credit rationing, because not all borrowers receive funds"
    - "Collateral constraint, because the bank should require assets as security"
  answer: 1
  explanation: "Moral hazard arises after a contract is signed when one party takes actions that the other cannot observe. Here, the borrower changes behavior after receiving funds — shifting to riskier projects. Adverse selection (option A) occurs before lending when lenders cannot distinguish good from bad borrowers. The scenario explicitly describes post-lending behavior change, which is the defining feature of moral hazard. Credit rationing (option C) and collateral requirements (option D) are lender responses to these problems, not descriptions of the problem itself."

- question: "During a recession, a firm's collateral value (its factory building) falls by 30%. According to the financial accelerator mechanism, what is the most likely macroeconomic consequence?"
  type: multiple-choice
  options:
    - "The firm borrows more to compensate for lost equity, stimulating investment"
    - "The firm's credit constraint tightens, reducing investment, which deepens the recession"
    - "The firm's interest rate falls because lenders compete for the remaining creditworthy borrowers"
    - "The recession ends sooner because falling asset prices make purchases attractive"
  answer: 1
  explanation: "The financial accelerator works through collateral constraints: when collateral values fall, lenders reduce the credit they extend because there is less security backing the loans. The firm can borrow less, so it invests less. Reduced investment deepens the recession, which further depresses asset prices and collateral values, tightening credit further. This feedback loop amplifies the original shock. Option A reverses the causation — firms cannot easily borrow more when their collateral has shrunk, because collateral is the basis for borrowing."

- question: "The financial accelerator mechanism means that financial frictions can amplify a modest initial economic shock into a severe recession through a self-reinforcing feedback loop."
  type: true-false
  answer: true
  explanation: "This is the core claim of the Bernanke-Gertler-Gilchrist model. A negative shock reduces asset prices, which reduces collateral values, which tightens credit constraints, which reduces investment and consumption, which deepens the recession, which further depresses asset prices. Each round of this cycle amplifies the original disturbance rather than absorbing it. The 2007-2009 financial crisis demonstrated this mechanism: falling house prices triggered cascading credit tightening far exceeding what the initial shock alone would have caused."

- question: "In a credit market with adverse selection, raising interest rates is the most effective tool for a lender to attract safer borrowers and improve loan portfolio quality."
  type: true-false
  answer: false
  explanation: "Raising interest rates actually worsens adverse selection — this is the Stiglitz-Weiss insight. When rates rise, the safest borrowers (who know they will repay) find the terms unfavorable and withdraw from the market. The pool of remaining applicants becomes riskier on average. Lenders understand this and respond by rationing credit (restricting quantity) rather than raising rates further, because beyond a point, higher rates reduce expected profit by selecting for riskier borrowers. Credit rationing, collateral requirements, and relationship lending are the actual responses to adverse selection."

- question: "Explain why economists say financial frictions 'amplify' rather than simply 'transmit' economic shocks. What mechanism creates this amplification?"
  type: short-answer
  answer: "Amplification occurs because the financial system creates a feedback loop rather than a one-time transmission. A shock reduces asset prices → collateral values fall → credit constraints tighten → firms and households invest and consume less → the recession deepens → asset prices fall further. Each pass through this loop intensifies the shock. Without financial frictions, credit markets would continue to intermediate between savers and borrowers, dampening the shock. With frictions, credit supply contracts precisely when it is most needed, turning a manageable downturn into a crisis."
  explanation: "The key word is 'feedback.' A passive transmission would mean a shock passes through the economy once and dissipates. Amplification means the shock feeds back on itself. Financial frictions create this loop by making credit availability contingent on collateral values, which are themselves depressed by the recession that the credit crunch helped create. This is why models without financial frictions — which treat credit markets as neutral intermediaries — systematically underestimate the depth and persistence of financial crises."
```

## Explainer

From information asymmetry, you understand that when one party to a transaction knows more than the other, markets can malfunction — adverse selection drives out good risks, and moral hazard encourages excessive risk-taking. Financial frictions apply these ideas to credit markets, where the consequences are especially severe because lending is inherently an exchange of money today for a promise of money tomorrow. That promise depends entirely on the borrower's ability and willingness to repay — both of which are imperfectly observable by the lender.

Consider a bank evaluating a loan application. The borrower knows her project's true risk; the bank does not. If the bank charges a single interest rate, the safest borrowers (who know they will repay) may find the rate too high and drop out, leaving a riskier pool — this is **adverse selection** in credit markets, first formalized by Stiglitz and Weiss. Alternatively, once the loan is made, the borrower may take on riskier projects than promised because she keeps the upside while the bank bears the downside if the project fails — this is **moral hazard**. Lenders respond to these problems not by raising rates indefinitely (which would worsen adverse selection) but by imposing **credit constraints**: requiring collateral, limiting loan-to-value ratios, or rationing credit altogether. The result is that some borrowers with genuinely productive projects cannot obtain financing, and the economy operates below its potential.

The macroeconomic importance of financial frictions becomes dramatic during downturns through the **financial accelerator** mechanism. Suppose a negative shock — a recession, a fall in housing prices, or a stock market crash — reduces the value of borrowers' collateral. With lower collateral, credit constraints tighten: firms can borrow less, so they invest less; households can borrow less, so they consume less. Reduced spending deepens the recession, which further depresses asset prices and collateral values, which tightens credit constraints even more. This feedback loop — sometimes called the Bernanke-Gertler-Gilchrist accelerator — means that a modest initial shock can cascade into a severe downturn because the financial system amplifies rather than absorbs the disturbance.

The 2007-2009 financial crisis illustrated this mechanism vividly. Falling house prices eroded the collateral underlying mortgage-backed securities, triggering margin calls and fire sales that depressed asset prices further, tightening credit across the entire economy. Banks that had appeared well-capitalized suddenly faced insolvency because their assets (loans and securities) lost value while their liabilities (deposits and short-term borrowing) remained fixed. The lesson for macroeconomic modeling is clear: models without financial frictions — which treat credit markets as frictionless conduits between savers and borrowers — cannot explain the depth and persistence of financial crises. Incorporating information asymmetries, collateral constraints, and balance sheet effects is essential for understanding how modern economies actually behave under stress.
