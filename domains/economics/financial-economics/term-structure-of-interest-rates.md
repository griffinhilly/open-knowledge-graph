---
id: term-structure-of-interest-rates
title: Term Structure of Interest Rates
domain: economics
course: financial-economics
prerequisites:
- id: yield-to-maturity
  type: hard
- id: inflation-and-price-level
  type: soft
- id: monetary-policy-tools
  type: soft
- id: duration-and-convexity
  type: soft
builds-toward:
- risk-and-return-tradeoff
tags:
- yield-curve
- term-structure
- spot-rates
- forward-rates
- expectations
stage: formal-systems
status: validated
---
# Term Structure of Interest Rates

## Core Idea
The term structure of interest rates describes how yields on otherwise equivalent bonds vary with maturity, visualized as the yield curve. Three main theories explain its shape: the pure expectations theory (long rates equal the geometric average of expected future short rates), the liquidity preference theory (investors demand a term premium for longer maturities), and the market segmentation theory (supply and demand in each maturity segment independently determine yields). An inverted yield curve — where short-term rates exceed long-term rates — has historically been a reliable recession predictor. Forward rates, derived from spot rates, represent market expectations of future short-term rates.

## How It's Best Learned
Plot the current Treasury yield curve and identify its shape: normal (upward-sloping), flat, or inverted. Study historical inversions before the 2001 and 2008 recessions. Bootstrap forward rates from spot rates to extract implied expectations about future policy rates.

## Common Misconceptions
- A normal, upward-sloping yield curve is not 'natural' or mathematically required — it reflects term premiums and growth expectations that can and do disappear.
- The yield curve is not the same as the discount rate schedule used in DCF analysis; risk-appropriate discount rates depend on project risk, not just maturity.

## Questions

```yaml
- question: "The yield curve is currently upward-sloping (normal). Under the pure expectations theory, what does this shape imply?"
  type: multiple-choice
  options:
    - "The market expects interest rates to remain stable — the slope just reflects inflation risk"
    - "The market expects future short-term rates to be higher than today's short-term rates"
    - "Long-term bonds are riskier, so investors automatically demand higher yields regardless of rate expectations"
    - "The central bank has set long-term rates higher than short-term rates"
  answer: 1
  explanation: "Under pure expectations theory, the long-term rate equals the geometric average of expected future short-term rates. An upward-sloping curve means long rates exceed short rates, which requires expected future short rates to be higher than current short rates. Option C describes the liquidity preference theory, not pure expectations. Option D misunderstands the yield curve: the central bank directly controls only short-term rates; long-term rates are set by bond markets reflecting expectations and term premiums."

- question: "Under the liquidity preference theory, why does the yield curve typically slope upward even when short-term rates are expected to remain flat for years?"
  type: multiple-choice
  options:
    - "Because longer-maturity bonds have higher default risk"
    - "Because investors demand a term premium to compensate for the uncertainty and illiquidity of holding long-term bonds"
    - "Because the central bank pegs long rates above short rates to encourage saving"
    - "Because inflation is always expected to rise in the long run"
  answer: 1
  explanation: "The liquidity preference theory adds a positive term premium on top of expected future rates. Even if investors expect short rates to stay flat at 2% forever, they still demand something extra — say 0.5–1% — to lock up money for 10 years rather than rolling over short-term bonds. This term premium compensates for price volatility risk (long bonds fall more when rates rise) and liquidity risk. This is why a flat-expectation world still produces an upward-sloping curve. The normal upward slope reflects both expectations and this premium layered on top."

- question: "An upward-sloping yield curve typically indicates that the market expects interest rates to rise in the future."
  type: true-false
  answer: false
  explanation: "Under liquidity preference theory, the yield curve can slope upward even when the market expects future short rates to stay flat or even fall slightly, because the term premium adds a positive increment to long-term yields regardless of rate expectations. A steeply upward-sloping curve might reflect high term premiums rather than strong expectations of rate increases. Distinguishing expectations from term premiums requires additional analysis (e.g., comparing implied forward rates to survey-based rate expectations)."

- question: "A yield curve inversion (short-term rates exceeding long-term rates) has historically been a reliable leading indicator of recessions."
  type: true-false
  answer: true
  explanation: "Every U.S. recession since the 1970s has been preceded by an inverted yield curve, typically 12–18 months earlier. The mechanism: an inversion means markets expect future short rates to fall substantially, which happens when recession and central bank easing are anticipated. Additionally, an inverted curve directly tightens bank lending — banks borrow short and lend long, and when short rates exceed long rates, this spread turns negative, making new lending unprofitable. This credit tightening itself contributes to the recession the curve predicted."

- question: "Why has an inverted yield curve historically predicted recessions? Explain the mechanism, not just the correlation."
  type: short-answer
  answer: "An inverted yield curve (short rates > long rates) signals that bond markets expect future short-term rates to fall substantially. Under most theories, long rates reflect expected future short rates. Rates fall when the central bank eases policy — which typically happens in response to recession. So the inversion itself is the market's forecast of future easing, which implies an expected recession. Beyond prediction, the inversion also causes economic damage: banks fund themselves short-term and lend long-term, so when the yield curve inverts, the spread on new loans turns negative, causing banks to tighten credit. This credit contraction reduces business investment and consumer spending, helping to create the very recession the curve predicted."
  explanation: "The yield curve is both a predictor and a partial cause of recessions — the mechanism runs both ways. Understanding this requires connecting the term structure theories (why the inversion signals expectations of lower future rates) with the banking channel (why a negative spread directly impairs lending). Neither alone tells the full story."
```

## Explainer

You already understand yield-to-maturity: for a single bond, it is the single discount rate that sets the present value of all cash flows equal to the current price. The **term structure of interest rates** steps back from individual bonds and asks: what pattern of yields do we observe across all maturities at a single point in time? Plot the YTM of risk-free (Treasury) bonds on the vertical axis and time to maturity on the horizontal axis, and you get the **yield curve**. In normal times it slopes upward — longer maturities yield more than shorter ones. But it can flatten, hump, or invert, and those shapes carry important information about the economy's expected future.

Three competing theories explain why the yield curve has the shape it does at any moment. The **pure expectations theory** says the long rate is the geometric average of expected future short rates: if 1-year rates are 3% today and expected to be 5% next year, the 2-year rate should be approximately 4%. No term premiums, no preferences — just expectations. The **liquidity preference theory** modifies this by noting that investors dislike locking up money for long periods and demand compensation for the uncertainty of holding long bonds. This adds a positive **term premium** to long rates, explaining why the curve usually slopes upward even when short rates are expected to stay flat. The **market segmentation theory** goes further: different investors (pension funds, banks, money market funds) operate in different maturity segments and do not easily substitute, so supply and demand in each segment independently influence yields.

**Forward rates** are the key analytical tool derived from spot rates. The 1-year forward rate one year from now is the rate implied by the relationship between the 1-year spot rate and the 2-year spot rate: it is the break-even rate that makes rolling over 1-year bonds equivalent to buying a 2-year bond today. Under pure expectations, forward rates equal expected future spot rates. With term premiums, forward rates exceed expected future short rates. This matters enormously for monetary policy analysis: when the central bank cuts short-term rates, the effect on long rates depends on how much of the long rate reflects expectations versus term premiums — a distinction that inflation and duration knowledge illuminates.

The **inverted yield curve** — where short-term rates exceed long-term rates — is the most watched shape because of its predictive record. It typically signals that the market expects future short rates to fall substantially, which happens when the market anticipates a recession and subsequent central bank easing. Every U.S. recession since the 1970s has been preceded by a yield curve inversion, often by 12–18 months. The mechanism is partly self-fulfilling: an inverted curve tightens bank lending (banks borrow short and lend long; when the spread inverts, lending becomes unprofitable) and signals economic stress that can dampen investment and consumption.
