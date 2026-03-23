---
id: interest-rate-swap-contracts
title: Interest Rate Swap Contracts
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: interest-rates-and-loanable-funds
  type: hard
builds-toward:
- hedging-with-derivatives
tags:
- swaps
- interest-rates
- derivatives
stage: formal-systems
status: validated
---

# Interest Rate Swap Contracts

## Core Idea
An interest rate swap exchanges fixed-rate cash flows for floating-rate (or vice versa), allowing firms to adjust their interest rate exposure without restructuring debt. Swaps are priced using bond pricing principles and the term structure. They are the most liquid OTC derivatives and widely used for asset-liability management and speculation.

## Questions

```yaml
- question: "A corporation has a $100M floating-rate loan at SOFR + 1.5%. It enters a swap paying 3.5% fixed and receiving SOFR. What is the corporation's effective net interest cost after combining the loan and swap?"
  type: multiple-choice
  options:
    - "3.5% fixed — the swap rate replaces the original loan rate"
    - "SOFR + 1.5% — the swap is a separate contract and does not affect the loan"
    - "5.0% fixed — the SOFR payments cancel, leaving the fixed rate plus the spread"
    - "2.0% fixed — the swap rate minus the floating spread"
  answer: 2
  explanation: "Combining the loan and the swap: pay SOFR + 1.5% (loan) + pay 3.5% fixed (swap) − receive SOFR (swap) = 3.5% + 1.5% = 5.0% fixed. The SOFR component in the loan and the SOFR received from the swap cancel exactly. The firm has synthetically converted floating-rate debt into 5.0% fixed-rate debt without refinancing the underlying loan. This is the essential function of an interest rate swap — not replacing the debt, but layering a separate contract that transforms the interest rate exposure."

- question: "Six months after entering a pay-fixed, receive-floating swap at a 4% fixed rate, long-term rates rise to 6%. What happens to the market value of the swap for the fixed payer?"
  type: multiple-choice
  options:
    - "The value falls — being locked into paying 4% when market rates are 6% is unfavorable"
    - "The value rises — the firm is paying a below-market fixed rate, making the position favorable"
    - "The value is unchanged — swaps are always priced at zero by construction"
    - "The value depends only on changes in the floating rate received, not the fixed rate paid"
  answer: 1
  explanation: "When rates rise to 6%, new fixed payers would have to pay 6% on a new swap. This firm is locked in at only 4% — below the current market rate. The fixed payer is now paying cheap relative to what a new swap would cost, while receiving floating payments that have risen. The net present value of remaining cash flows has turned positive for the fixed payer. Option A commits the key error: 'paying 4% when rates are 6%' sounds unfavorable, but being locked in at 4% when the market demands 6% is the favorable side of the trade."

- question: "In an interest rate swap, the notional principal is exchanged between counterparties at the initiation of the contract."
  type: true-false
  answer: false
  explanation: "This is the most fundamental structural feature of swaps. The 'notional' in notional principal means the amount exists in name only — it determines the size of the interest payments but is never transferred between parties. Only the periodic interest cash flows are exchanged. This is what makes swaps efficient: a firm can transform the rate profile of a $100M loan by exchanging only the interest differential, without moving or encumbering the principal itself."

- question: "At the moment an interest rate swap is initiated, it has zero net present value to both counterparties."
  type: true-false
  answer: true
  explanation: "The swap rate — the fixed rate paid by the fixed payer — is specifically chosen so that the present value of the fixed cash flows equals the present value of the expected floating cash flows on the initiation date. This makes the initial value zero for both sides: neither party pays a premium to enter. Compare this to an option, where one side pays a premium upfront. After initiation, as interest rates move, the swap develops a positive value for one side and an equal negative value for the other."

- question: "Why do companies use interest rate swaps rather than simply refinancing their debt to achieve a different interest rate profile? What advantages do swaps offer?"
  type: short-answer
  answer: "Refinancing is costly, time-consuming, and may require paying prepayment penalties, renegotiating loan terms, and reestablishing credit relationships. A swap achieves the same economic transformation — converting fixed to floating or floating to fixed — through a separate contract that leaves the underlying debt untouched. Swaps are also liquid and reversible: a position can be exited by entering an offsetting swap or selling the position in the OTC market. The combination of low transaction costs, flexibility, and speed makes swaps far more practical than repeated debt restructuring for managing interest rate exposure."
  explanation: "The key organizational insight is that funding decisions and risk management decisions can be separated. A firm might raise fixed-rate debt because the bond market is favorable at that moment, then use a swap to convert to floating if that better matches their asset profile — without issuing new debt. This decomposition lets treasury and risk management operate independently. It also enables temporary adjustments: a swap can be unwound when the exposure no longer exists, without modifying the underlying financing."
```

## Explainer

You know from bond pricing that a fixed-rate bond obligates the issuer to pay a fixed coupon on a fixed schedule regardless of what happens to interest rates. If rates rise, the bond's market value falls, which hurts the holder but benefits the issuer who locked in cheap fixed financing. If rates fall, the reverse. A **plain vanilla interest rate swap** is essentially a way to change your interest rate exposure without refinancing the underlying debt.

The mechanics are straightforward. Two counterparties agree to exchange periodic interest payments on a notional principal amount — the principal itself never changes hands, only the interest cash flows. In the most common structure, one party pays a **fixed rate** (the swap rate) and receives a **floating rate** (typically based on SOFR or, historically, LIBOR). The other party does the reverse. For example, a firm with floating-rate debt (paying SOFR + 2%) might enter a swap as the fixed payer: it pays 4% fixed and receives SOFR from the swap counterparty. Combining the debt obligation and the swap, the firm's net cost is 4% + 2% = 6% fixed — converting variable-rate financing to fixed-rate financing without refinancing the loan. The swap is not the loan; it is a separate contract that synthetically transforms the interest rate profile.

**Pricing** a swap uses exactly the bond pricing tools you already know. At initiation, the swap has zero value to both parties — neither side pays a premium. The **swap rate** (the fixed rate that makes the contract fairly priced) is the coupon rate that equates the present value of fixed cash flows to the present value of floating cash flows, discounted using the current yield curve. Intuitively, the swap rate equals the par coupon rate of a fixed-rate bond whose cash flows exactly replicate the fixed leg, given current forward rates implied by the term structure. After initiation, as interest rates move, the swap develops a positive or negative market value: if rates rise, paying fixed becomes cheap (you're locked in below market), so the fixed-payer's position gains value.

Swaps are the most widely traded OTC derivative for a reason: they are enormously useful for **asset-liability management**. Banks, pension funds, and insurers routinely hold assets and liabilities with mismatched interest rate durations. A pension fund holding mostly floating-rate assets but facing fixed nominal liabilities can use a swap to receive fixed and pay floating, aligning its duration exposure without liquidating the underlying portfolio. Swaps also serve speculative purposes — a trader expecting rates to fall would receive fixed and pay floating, profiting if long-term rates decline. Post-2008, most standardized swaps are cleared through central counterparties (CCPs), which eliminate bilateral counterparty credit risk that was a major vulnerability during the financial crisis.
