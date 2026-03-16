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
status: draft
---

# Interest Rate Swap Contracts

## Core Idea
An interest rate swap exchanges fixed-rate cash flows for floating-rate (or vice versa), allowing firms to adjust their interest rate exposure without restructuring debt. Swaps are priced using bond pricing principles and the term structure. They are the most liquid OTC derivatives and widely used for asset-liability management and speculation.

## Explainer

You know from bond pricing that a fixed-rate bond obligates the issuer to pay a fixed coupon on a fixed schedule regardless of what happens to interest rates. If rates rise, the bond's market value falls, which hurts the holder but benefits the issuer who locked in cheap fixed financing. If rates fall, the reverse. A **plain vanilla interest rate swap** is essentially a way to change your interest rate exposure without refinancing the underlying debt.

The mechanics are straightforward. Two counterparties agree to exchange periodic interest payments on a notional principal amount — the principal itself never changes hands, only the interest cash flows. In the most common structure, one party pays a **fixed rate** (the swap rate) and receives a **floating rate** (typically based on SOFR or, historically, LIBOR). The other party does the reverse. For example, a firm with floating-rate debt (paying SOFR + 2%) might enter a swap as the fixed payer: it pays 4% fixed and receives SOFR from the swap counterparty. Combining the debt obligation and the swap, the firm's net cost is 4% + 2% = 6% fixed — converting variable-rate financing to fixed-rate financing without refinancing the loan. The swap is not the loan; it is a separate contract that synthetically transforms the interest rate profile.

**Pricing** a swap uses exactly the bond pricing tools you already know. At initiation, the swap has zero value to both parties — neither side pays a premium. The **swap rate** (the fixed rate that makes the contract fairly priced) is the coupon rate that equates the present value of fixed cash flows to the present value of floating cash flows, discounted using the current yield curve. Intuitively, the swap rate equals the par coupon rate of a fixed-rate bond whose cash flows exactly replicate the fixed leg, given current forward rates implied by the term structure. After initiation, as interest rates move, the swap develops a positive or negative market value: if rates rise, paying fixed becomes cheap (you're locked in below market), so the fixed-payer's position gains value.

Swaps are the most widely traded OTC derivative for a reason: they are enormously useful for **asset-liability management**. Banks, pension funds, and insurers routinely hold assets and liabilities with mismatched interest rate durations. A pension fund holding mostly floating-rate assets but facing fixed nominal liabilities can use a swap to receive fixed and pay floating, aligning its duration exposure without liquidating the underlying portfolio. Swaps also serve speculative purposes — a trader expecting rates to fall would receive fixed and pay floating, profiting if long-term rates decline. Post-2008, most standardized swaps are cleared through central counterparties (CCPs), which eliminate bilateral counterparty credit risk that was a major vulnerability during the financial crisis.
