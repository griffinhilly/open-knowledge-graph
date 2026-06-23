---
id: interest-rate-term-structure
title: Term Structure of Interest Rates
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: interest-rates-and-loanable-funds
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- spot-forward-rate-relationships
tags:
- bonds
- yield-curve
- interest-rates
- term-structure
stage: formal-systems
status: validated
---

# Term Structure of Interest Rates

## Core Idea
The term structure describes how interest rates vary across different maturity horizons. Yield curves can be upward-sloping, downward-sloping, or flat, reflecting market expectations about future rates, inflation, and risk premiums. The shape of the yield curve contains information about economic expectations and relative valuations of securities across maturities.

## How It's Best Learned
Start by plotting actual yield curve data from different time periods and learning to interpret the shapes. Then study the expectations hypothesis and liquidity preference theory to understand what drives different curve shapes.

## Common Misconceptions
- Assuming all interest rates move proportionally; different maturities respond differently to economic changes.
- Confusing the level of rates with the shape of the curve; they are independent phenomena.

## Questions

```yaml
- question: "The yield curve inverts — 2-year Treasury yields are now higher than 10-year yields. What does this most likely signal about market expectations?"
  type: multiple-choice
  options:
    - "Markets expect inflation to rise sharply over the next decade, pushing long-term rates up"
    - "The Federal Reserve has lost credibility, so long-term bonds are being sold off"
    - "Markets expect short-term rates to fall in the future — typically anticipating an economic slowdown or recession"
    - "The supply of long-term bonds has decreased, lowering their yields relative to short-term bonds"
  answer: 2
  explanation: "Under the expectations hypothesis, long-term rates reflect the market's average expected short-term rates over the horizon. If 10-year yields are below 2-year yields, it means the market expects short-term rates to fall substantially over the coming years. Historically, this pattern (central bank cutting rates in response to economic weakness) has reliably preceded recessions with a 6–18 month lag. Option A would predict rising long-term rates (to compensate for inflation), not falling ones. Yield curve inversion is one of the most closely watched leading indicators precisely because it aggregates market participants' expectations about future monetary policy and growth."

- question: "The liquidity premium theory of the yield curve argues that long-term rates exceed the pure expectations value because:"
  type: multiple-choice
  options:
    - "Longer bonds are more liquid (easier to trade), so investors accept lower yields on them"
    - "Longer bonds are more sensitive to interest rate changes (higher duration), so investors demand a risk premium"
    - "Central banks deliberately keep short-term rates low, creating a wedge between short and long rates"
    - "Inflation expectations are always higher for longer horizons, mechanically raising long rates"
  answer: 1
  explanation: "The liquidity premium (or term premium) theory adds a risk adjustment on top of the expectations hypothesis. Longer-maturity bonds have greater duration — their prices fluctuate more when interest rates move. An investor holding a 10-year bond is exposed to more interest rate risk than one holding a 1-year bond. To compensate for bearing this additional uncertainty, investors demand a higher yield. This premium is over and above whatever the expectations hypothesis predicts from expected future short rates. The term 'liquidity premium' is somewhat misleading — it's really a duration/risk premium, since long-term Treasuries are actually quite liquid. Option A confuses direction: higher liquidity would lower yields (investors accept less for easier-to-sell assets)."

- question: "An inverted yield curve signals that markets expect short-term interest rates to fall in the future, which is typically associated with anticipated economic slowdown."
  type: true-false
  answer: true
  explanation: "Under the expectations hypothesis, the long-term rate equals the geometric average of expected future short-term rates over that horizon. If 10-year yields fall below 2-year yields, the market is pricing in significant short-rate declines over the coming decade — a signal that monetary easing (rate cuts) is expected, which central banks typically do in response to recessions. This is why yield curve inversions have historically preceded recessions with high reliability: the bond market is aggregating millions of investors' forecasts into a single observable price signal. The inversion doesn't cause the recession; it reflects the expectation of one."

- question: "When the Federal Reserve raises the federal funds rate, most points on the yield curve shift upward proportionally, keeping the curve's shape unchanged."
  type: true-false
  answer: false
  explanation: "This is the misconception the topic's 'Common Misconceptions' directly flags: different maturities respond differently to economic changes. The Fed directly controls very short-term rates (overnight, 1-month), so the short end of the curve rises sharply. Long-term rates, however, are driven by long-run growth and inflation expectations, which the Fed influences only indirectly and over time. A rate hike cycle often steepens or flattens the curve — or even inverts it — depending on how markets interpret the Fed's actions for the long-run outlook. Level and shape are genuinely independent dimensions of the yield curve."

- question: "Explain why the level of interest rates and the slope of the yield curve are considered independent pieces of information, and what each one tells us about economic conditions."
  type: short-answer
  answer: "The level (the average height of the yield curve) reflects current monetary conditions — whether rates are generally high or low, driven by central bank policy and current inflation. The slope (upward, flat, or inverted) encodes market expectations about where rates are headed — it reflects the difference between what short-term rates are now versus what the market expects them to be in the future. A steeply upward-sloping curve can exist at either 2% or 8% average rates; a flat curve can also exist at either level. They measure different things."
  explanation: "Confusing level and slope leads to systematic errors in bond analysis. A high-rate, flat curve means rates are currently elevated but expected to stabilize — different from a high-rate, steeply upward-sloping curve (rates high now, expected to rise further). A low-rate, inverted curve is particularly significant: it signals that even though rates are low, the market expects them to go lower still — a recession warning. Reading both dimensions simultaneously gives a much richer picture of market expectations than tracking the overall rate level alone."
```

## Explainer

From present value and discounting, you know that the value of a future cash flow depends critically on the interest rate used to discount it — and that different cash flows arrive at different times. The term structure formalizes the fact that there is not one interest rate but a whole schedule of rates, one for each maturity. A **yield curve** is a snapshot of this schedule: plot maturity on the x-axis and the annualized interest rate on the y-axis, and you get a curve that reveals how the market prices time across different horizons.

The most common shape is **upward-sloping**: longer maturities carry higher rates. There are two main reasons for this. First, the **expectations hypothesis** says that long-term rates reflect the market's average expected short-term rates over that horizon. If the Fed is expected to raise rates over the next two years, a 2-year rate will be higher than today's 1-year rate to compensate investors for rolling over at expected higher future rates. Second, the **liquidity premium theory** adds a risk premium on top: longer bonds have more interest rate sensitivity (duration), meaning their prices fluctuate more when rates move. Investors demand a premium to bear this extra risk, so long-term rates tend to exceed the pure expectations value.

An **inverted (downward-sloping)** yield curve is unusual and closely watched. It signals that short-term rates exceed long-term rates — typically because markets expect the central bank to cut rates in the future, usually in response to an anticipated recession. Historically, yield curve inversions have reliably preceded economic downturns with a lag of 6–18 months. This makes the yield curve shape a leading economic indicator: the market is aggregating millions of investors' expectations about future growth and monetary policy into a single observable curve.

The **flat yield curve** is a transitional shape, often seen when the economy is at an inflection point between expansion and contraction, or when the central bank has raised short rates sharply while long-term inflation expectations remain anchored. A key point from the misconceptions: the overall level of the curve (whether rates are high or low) is independent of its slope (upward, flat, or inverted). You could have a steeply upward-sloping curve at either 2% or 7% average rates. Understanding the term structure means reading both pieces of information — the level reflects current monetary conditions; the shape encodes market expectations about where rates are headed.
