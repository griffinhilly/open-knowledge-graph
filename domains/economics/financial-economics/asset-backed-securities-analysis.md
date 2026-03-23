---
id: asset-backed-securities-analysis
title: Asset-Backed Securities and Securitization Analysis
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: credit-risk-and-default
  type: soft
builds-toward:
- default-recovery-modeling
tags:
- securitization
- abs
- mortgages
- credit-risk
stage: formal-systems
status: validated
---

# Asset-Backed Securities and Securitization Analysis

## Core Idea
Securitization pools cash-flowing assets (mortgages, auto loans, receivables) into tranched securities with different risk priorities. Senior tranches have priority in receiving payments and thus lower credit risk; junior and equity tranches absorb losses first. ABS valuation requires modeling prepayment risk, default rates, and recovery rates, which depend critically on macroeconomic conditions and portfolio composition.

## Questions

```yaml
- question: "A senior tranche of a mortgage-backed security is rated AAA despite the underlying mortgages being subprime. Which assumption, if violated, most directly destroys the senior tranche's protection?"
  type: multiple-choice
  options:
    - "The assumption that interest rates will remain stable over the life of the security"
    - "The assumption that borrower defaults are largely uncorrelated, so losses remain predictable and subordination absorbs them"
    - "The assumption that prepayment speeds follow the PSA benchmark convention"
    - "The assumption that recovery rates on individual mortgages are exactly 50%"
  answer: 1
  explanation: "Tranching provides protection through subordination: junior tranches absorb losses first, and only if losses exceed the junior tranches' capacity do senior tranches suffer. This structure works when defaults are approximately uncorrelated — some borrowers default, but not all at once. If defaults are highly correlated (a national housing price decline hits all borrowers simultaneously), losses can overwhelm all junior tranches and reach senior tranches. The 2008 crisis was precisely this: rating agencies assumed uncorrelated defaults, but macroeconomic shocks made defaults cluster, demolishing the correlation assumption and exposing AAA-rated seniors to catastrophic loss."

- question: "An investor paid a premium for a mortgage-backed security, expecting cash flows over 10 years. Interest rates then fall sharply. What risk is now most salient?"
  type: multiple-choice
  options:
    - "Credit risk — lower rates make it harder for borrowers to service their debt"
    - "Prepayment risk — borrowers will refinance at lower rates, returning principal early and shortening the security's duration below the investor's expectation"
    - "Liquidity risk — falling rates cause MBS prices to drop in the secondary market"
    - "Default risk — falling rates correlate with recessions that increase default rates"
  answer: 1
  explanation: "When rates fall, homeowners have a strong incentive to refinance — they can take out a new mortgage at the lower rate. From the investor's perspective, the principal is returned early, terminating the expected future cash flows. If the investor paid a premium (above par), they paid extra expecting to receive those future coupon payments; early repayment means they don't receive them and effectively overpaid. This is prepayment risk: the risk that cash flows are shorter than expected precisely when reinvestment rates are lower. Counterintuitively, falling rates — good news for most bond holders — are bad news for MBS premium holders."

- question: "In an ABS waterfall structure, the equity (residual) tranche is the last to absorb losses, making it the safest component of the structure."
  type: true-false
  answer: false
  explanation: "This reverses the waterfall. The equity tranche absorbs the FIRST losses from defaults and other shortfalls — it is the most exposed component of the structure, and investors in it demand the highest yield to compensate for this risk. The senior tranche is last to absorb losses and is therefore safest (and receives the lowest yield). 'Equity' here means residual claim — whatever is left after senior and mezzanine tranches are paid, which may be nothing if losses are large. The equity holder effectively provides insurance to senior tranche holders."

- question: "Securitization can transform a pool of below-investment-grade mortgages into senior securities with investment-grade credit ratings."
  type: true-false
  answer: true
  explanation: "This is the central purpose and power of tranching. By subordinating junior tranches, the structure concentrates credit risk in the lower tranches, shielding the senior tranche from all but catastrophic losses. If a pool of subprime mortgages is expected to have a 5% loss rate with low correlation, and the equity tranche absorbs the first 10% of losses and the mezzanine tranche the next 10%, the senior tranche — receiving the first 80% of cash flows — may legitimately warrant an AAA rating because its protection is thick. The problem arises when the underlying assumptions (loss rates, correlation) are wrong."

- question: "Explain why the 2008 financial crisis exposed a fundamental flaw in how ABS structures were modeled, and what that flaw was."
  type: short-answer
  answer: "ABS models assumed that defaults across the mortgage pool were largely uncorrelated — that individual borrowers might default for idiosyncratic reasons (job loss, divorce), but that widespread simultaneous default was unlikely. Tranching provides protection only if this holds: if 5% of borrowers default independently, the equity tranche absorbs the loss and senior tranches are safe. The flaw was that national housing price declines caused correlated defaults: when home prices fell everywhere simultaneously, millions of borrowers faced negative equity and could not refinance or sell, driving defaults across every geography and borrower type at once. The diversification that the models relied on disappeared exactly when it was needed most."
  explanation: "The 2008 lesson is that securitization models must stress-test correlation assumptions, not just expected loss rates. A model that uses historically low default correlations will dramatically understate risk during a macroeconomic shock. Rating agencies, originators, and investors all failed to account for the scenario where home prices fell nationally — an event with no recent precedent in their historical data, but not an impossible one. The result was that instruments rated AAA were, in reality, deeply correlated with the one risk that a systemic crisis would trigger."
```

## Explainer

From bond pricing, you know how to value a fixed stream of cash flows: discount each payment at the appropriate risk-adjusted rate. Asset-backed securities extend this framework, but with a twist — the cash flows themselves are uncertain. A mortgage-backed security, for example, represents a claim on monthly principal and interest payments from hundreds or thousands of homeowners. These payments can stop (default) or accelerate (prepayment when homeowners refinance), making the timing and size of cash flows stochastic. Securitization is the process of packaging these uncertain claims into marketable bonds.

The central innovation of securitization is **tranching** — the waterfall structure that allocates cash flows and losses in a predetermined priority order. Imagine a pool of 1,000 mortgages generating monthly cash flows. The **senior tranche** is paid first from these flows and absorbs losses last; if only 10% of mortgages default, the senior tranche might be fully protected. The **junior (mezzanine) tranche** is paid next and absorbs losses after the equity tranche is wiped out. The **equity (residual) tranche** is paid last and absorbs the first losses. By subordinating lower tranches, the structure transforms a pool of risky assets into securities with a range of credit profiles — the senior tranche can be rated AAA even if the underlying mortgages are subprime.

Valuing an ABS requires three key inputs beyond standard bond pricing. **Prepayment risk** is the possibility that borrowers repay early — often because interest rates fall and they refinance. Prepayment is modeled using the **PSA (Public Securities Association) prepayment speed** convention, which measures prepayments as a percentage of a standard benchmark. Early prepayment shortens the security's duration and can hurt investors who paid a premium expecting longer cash flows. **Default rates** estimate what fraction of the underlying borrowers will fail to pay, typically modeled using historical loss curves and macroeconomic scenarios. **Recovery rates** estimate how much is recouped after default through collateral liquidation (e.g., foreclosure on the house).

The 2008 financial crisis revealed how these models can fail catastrophically. Rating agencies assumed home prices could not fall nationally, making their default and recovery models drastically overoptimistic for subprime MBS. Senior tranches rated AAA were, in reality, much riskier than their ratings implied because the underlying assumptions were wrong and correlations across the pool were far higher than assumed — when housing fell, defaults spiked everywhere simultaneously. This experience established that ABS analysis must stress-test correlation assumptions: diversification across a portfolio of loans only protects you if defaults are uncorrelated, but macroeconomic shocks can make them highly correlated at exactly the wrong moment.
