---
id: credit-spreads-bond-yields
title: Credit Spreads and Bond Yields
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: yield-to-maturity
  type: hard
builds-toward:
- bond-portfolio-strategies
tags:
- fixed-income
- credit-risk
- yield-analysis
stage: formal-systems
status: validated
---

# Credit Spreads and Bond Yields

## Core Idea
Credit spreads are the difference between a corporate bond's yield and a risk-free government bond of the same maturity. They compensate investors for default risk and credit quality, widening when investor risk appetite declines and narrowing when credit conditions improve.

## How It's Best Learned
Compare yields across bond issuers with different credit ratings and maturities. Track how spreads move during economic downturns versus expansions. Use credit spread data to infer market expectations about default probability.

## Questions

```yaml
- question: "A corporate bond is trading at a 150 basis point spread over Treasuries. The Federal Reserve then holds interest rates constant, but the issuing company's earnings collapse and analysts downgrade its credit rating. What most likely happens to the corporate bond's price?"
  type: multiple-choice
  options:
    - "The bond price stays the same because interest rates didn't change"
    - "The bond price rises because lower earnings reduce future coupon payments"
    - "The bond price falls because the wider credit spread raises the required yield"
    - "The bond price is unaffected until the company actually misses a coupon payment"
  answer: 2
  explanation: "Credit risk and interest rate risk are separate drivers of bond prices. When the market reassesses an issuer's creditworthiness downward, investors demand a higher yield to hold the bond — the credit spread widens. Since bond price and yield move inversely, a higher required yield means a lower price, even with rates unchanged. This is credit risk in action: the bond's price fell purely because the market's estimate of default probability (and uncertainty around it) increased. Option A is the most common misconception — equating bond price changes exclusively with rate moves."

- question: "Which of the following best explains why a bond widely expected to be repaid in full still trades at a positive credit spread over Treasuries?"
  type: multiple-choice
  options:
    - "Bond investors always demand a spread to compensate for inflation risk"
    - "Investors require compensation for the *uncertainty* of that outcome, even if default is unlikely"
    - "Corporate bonds have longer maturities than government bonds, so the spread compensates for duration"
    - "Regulatory requirements force institutional investors to charge a minimum spread on all non-government bonds"
  answer: 1
  explanation: "Even a bond with very low default probability carries a risk premium for uncertainty — the chance that the expected outcome doesn't materialize. The credit spread has three components: expected default probability, expected loss given default, and a risk premium for bearing that uncertainty. Investors can't perfectly predict outcomes, and uncertainty itself has a price. A government bond is treated as risk-free because the sovereign can print currency; a corporate bond cannot make that guarantee, so some compensation for the non-zero (even if tiny) possibility of loss is always required."

- question: "A credit spread of 120 basis points means the corporate bond's yield includes 1.20 percentage points of compensation that reflects mainly the market's estimate of the probability the issuer will default."
  type: true-false
  answer: false
  explanation: "The credit spread captures three distinct components, not just default probability alone. It includes: (1) the expected default probability, (2) the expected loss given default — how much investors recover if default occurs, since bonds often recover 30-60 cents on the dollar — and (3) a risk premium for the *uncertainty* of those estimates. A bond with a 1% expected annual default probability and 50% expected recovery rate would not trade at exactly 50 basis points; it would trade wider because investors demand extra compensation for bearing the risk that their estimates are wrong. The spread is thus larger than a pure actuarial calculation would suggest."

- question: "Credit spreads tend to widen during recessions and narrow during economic expansions."
  type: true-false
  answer: true
  explanation: "This reflects the fundamental connection between economic conditions and credit risk. During recessions, corporate revenues fall, default rates rise, and investors become more risk-averse — they demand greater compensation for holding risky assets and often sell corporate bonds to buy safe government bonds ('flight to quality'). Both effects push spreads wider: higher required yield + lower corporate bond prices. During expansions, the reverse occurs: strong earnings reduce default probability, investor confidence rises, and demand for corporate bonds compresses spreads. The 2008 financial crisis is the extreme example, with investment-grade spreads widening from ~100 basis points to 500+ in months."

- question: "Explain the difference between interest rate risk and credit risk as drivers of bond price changes, and why understanding both is essential for fixed income analysis."
  type: short-answer
  answer: "Interest rate risk is the risk that benchmark rates (like Treasury yields) rise, mechanically reducing all bond prices because future cash flows are discounted more heavily. Credit risk is the risk that the specific issuer's ability or willingness to repay deteriorates, causing the credit spread to widen and the bond's yield to rise independently of any benchmark move. A bond's total yield is approximately the risk-free rate plus the credit spread. If rates rise, nearly all bonds fall in price together. If an issuer's credit quality deteriorates, only that issuer's bonds fall — the spread widens while comparable Treasury yields are unchanged."
  explanation: "Fixed income investors must decompose yield into these two components because they require different management strategies. Interest rate risk is hedged through duration management (holding shorter-maturity bonds or using rate swaps). Credit risk is managed through credit analysis, diversification across issuers, and sometimes credit default swaps. A portfolio manager who confuses the two might hedge against rate moves while ignoring a deteriorating credit, or vice versa — resulting in losses from a risk they thought they had controlled."
```

## Explainer

From bond pricing you know that a bond's yield is the discount rate that equates the present value of its cash flows to its current price — higher risk demands a higher yield to compensate investors. From yield-to-maturity you know how to compute that rate and interpret it as the annualized return if held to maturity. The **credit spread** is the next conceptual step: it isolates the part of a corporate bond's yield that compensates specifically for credit risk, by comparing it to a risk-free benchmark with the same maturity.

Concretely, if a 10-year U.S. Treasury note yields 4.0% and a 10-year investment-grade corporate bond yields 5.2%, the credit spread is 120 **basis points** (1.20 percentage points). That gap represents the market's collective judgment about the additional return required to hold the corporate bond rather than the safe government alternative. The spread incorporates three components: expected default probability, expected loss given default (how much is recovered if the issuer does default), and a **risk premium** for bearing the uncertainty of those outcomes. Even a bond that investors believe will almost certainly be repaid in full must offer a spread because investors demand compensation for the non-zero chance of loss.

Credit spreads are not static — they compress and widen in response to economic conditions, and this movement is itself an important market signal. During recessions or financial stress, spreads widen dramatically as investors demand more compensation for heightened default risk and flee toward safe assets (a "flight to quality"). During expansions, spreads narrow as credit conditions improve and investor confidence rises. The 2008 financial crisis produced historic spread widening; corporate bonds that had traded at 100 basis points over Treasuries suddenly traded at 500 or more. Watching spread dynamics is therefore a real-time indicator of credit market sentiment.

The relationship between credit spread and credit rating is systematic but imperfect. **Investment-grade bonds** (BBB/Baa and above) trade at tighter spreads reflecting low default probability; **high-yield bonds** (below investment grade, sometimes called "junk bonds") trade at much wider spreads reflecting elevated default risk. As an issuer's credit quality deteriorates, its spreads widen — its existing bonds fall in price even without any change in benchmark rates. This is **credit risk** in action: bond prices can fall not because interest rates moved, but because the market's assessment of the issuer's ability to repay has changed. Understanding credit spreads as a priced risk separate from interest rate risk is fundamental to fixed income analysis.
