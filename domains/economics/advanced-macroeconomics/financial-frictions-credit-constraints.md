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
stage: formal-systems
status: draft
---

# Financial Frictions and Credit Constraints

## Core Idea
Financial frictions arise when lenders have limited information about borrowers (adverse selection) or borrowers cannot be perfectly monitored (moral hazard). These frictions create credit constraints: borrowers can only borrow against collateral, or face interest rates that vary with their creditworthiness. Financial crises occur when collateral values plummet, suddenly tightening credit constraints and reducing investment and consumption. The interaction between the financial sector and real economy creates powerful amplification mechanisms that magnify real shocks.

## Explainer

From information asymmetry, you understand that when one party to a transaction knows more than the other, markets can malfunction — adverse selection drives out good risks, and moral hazard encourages excessive risk-taking. Financial frictions apply these ideas to credit markets, where the consequences are especially severe because lending is inherently an exchange of money today for a promise of money tomorrow. That promise depends entirely on the borrower's ability and willingness to repay — both of which are imperfectly observable by the lender.

Consider a bank evaluating a loan application. The borrower knows her project's true risk; the bank does not. If the bank charges a single interest rate, the safest borrowers (who know they will repay) may find the rate too high and drop out, leaving a riskier pool — this is **adverse selection** in credit markets, first formalized by Stiglitz and Weiss. Alternatively, once the loan is made, the borrower may take on riskier projects than promised because she keeps the upside while the bank bears the downside if the project fails — this is **moral hazard**. Lenders respond to these problems not by raising rates indefinitely (which would worsen adverse selection) but by imposing **credit constraints**: requiring collateral, limiting loan-to-value ratios, or rationing credit altogether. The result is that some borrowers with genuinely productive projects cannot obtain financing, and the economy operates below its potential.

The macroeconomic importance of financial frictions becomes dramatic during downturns through the **financial accelerator** mechanism. Suppose a negative shock — a recession, a fall in housing prices, or a stock market crash — reduces the value of borrowers' collateral. With lower collateral, credit constraints tighten: firms can borrow less, so they invest less; households can borrow less, so they consume less. Reduced spending deepens the recession, which further depresses asset prices and collateral values, which tightens credit constraints even more. This feedback loop — sometimes called the Bernanke-Gertler-Gilchrist accelerator — means that a modest initial shock can cascade into a severe downturn because the financial system amplifies rather than absorbs the disturbance.

The 2007-2009 financial crisis illustrated this mechanism vividly. Falling house prices eroded the collateral underlying mortgage-backed securities, triggering margin calls and fire sales that depressed asset prices further, tightening credit across the entire economy. Banks that had appeared well-capitalized suddenly faced insolvency because their assets (loans and securities) lost value while their liabilities (deposits and short-term borrowing) remained fixed. The lesson for macroeconomic modeling is clear: models without financial frictions — which treat credit markets as frictionless conduits between savers and borrowers — cannot explain the depth and persistence of financial crises. Incorporating information asymmetries, collateral constraints, and balance sheet effects is essential for understanding how modern economies actually behave under stress.
