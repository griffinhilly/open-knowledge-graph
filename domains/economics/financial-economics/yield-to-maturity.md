---
id: yield-to-maturity
title: Yield to Maturity
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
builds-toward:
- term-structure-of-interest-rates
- risk-and-return-tradeoff
- duration-and-convexity
tags:
- ytm
- yield
- internal-rate-of-return
- fixed-income
stage: formal-systems
status: validated
---

# Yield to Maturity

## Core Idea
Yield to maturity (YTM) is the single discount rate that equates a bond's current price to the present value of all its future cash flows — the bond's internal rate of return. It represents the annualized return an investor earns if they hold the bond to maturity and all coupons are reinvested at the same rate. Because YTM is embedded in the bond pricing equation, it must generally be solved numerically. YTM is the standard metric for comparing bonds with different coupon rates and maturities on equal footing.

## How It's Best Learned
Use trial and error or a financial calculator to find YTM for a given price, then verify by plugging back into the bond pricing formula. Understand that YTM assumes reinvestment at the YTM rate — an assumption that rarely holds exactly in practice.

## Common Misconceptions
- YTM equals the coupon rate only when the bond trades at par; for a discounted bond, YTM exceeds the coupon rate.
- YTM is not a guaranteed return — it depends on the reinvestment rate assumption and on holding to maturity without default.

## Explainer

From bond pricing, you know that a bond's price equals the present value of its future cash flows — coupon payments and face value — discounted at a rate r: P = Σ C/(1+r)^t + F/(1+r)^T. In that framework, r is given and you compute P. **Yield to maturity** inverts this: you observe the market price P and solve for the discount rate r that makes the equation hold. YTM is the bond's **internal rate of return** — the single annualized rate that equates the bond's cost to the present value of everything it will pay you if held to maturity.

The intuition for the price-yield relationship follows directly from bond pricing. Because coupon payments are fixed in dollar terms, a bond's return comes from two sources: coupon income and any capital gain or loss as the price converges to face value at maturity. If you buy a bond at a **discount** (price below par), you earn extra return from the price appreciation to par — YTM exceeds the coupon rate. If you buy at a **premium** (price above par), you suffer a capital loss as the price falls to par — YTM is below the coupon rate. At par, there is no capital gain or loss, so YTM equals the coupon rate exactly. This is the clearest way to read bond prices: a bond trading at a discount is yielding more than its coupon; a bond trading at a premium is yielding less.

YTM is the standard comparison metric for bonds because it puts all bonds on equal footing regardless of coupon rate, maturity, or current price. Comparing a 3% coupon bond at $950 against a 5% coupon bond at $1,080 by coupon rate alone is meaningless — the purchase price affects total return. YTM computes what each bond actually returns over its remaining life, compressing all the complexity of coupon timing, price, and maturity into a single number. This is why bond markets quote yields rather than prices as the primary metric: a Treasury "yielding 4.2%" communicates more efficiently than "priced at $971.34 with a 4% coupon maturing in 7 years."

The reinvestment assumption embedded in YTM is its most important limitation. YTM assumes every coupon payment is reinvested at the YTM rate for the remainder of the bond's life. If you receive a $50 coupon in year 1 and can only reinvest it at 3% when YTM was 5%, your realized return falls short of YTM. For short-maturity bonds or low-coupon bonds, this gap is small — most of the return is in the final principal repayment, not in reinvested coupons. For long-maturity, high-coupon bonds, reinvestment income can constitute a large fraction of total return, making the realized return sensitive to the path of interest rates over the holding period.

Understanding YTM also clarifies bond market dynamics. When market interest rates rise, newly issued bonds offer higher coupons; existing bonds with lower fixed coupons must fall in price to offer a competitive YTM — prices and yields always move in opposite directions. This inverse relationship is not a market quirk but the direct consequence of the bond pricing formula. The sensitivity of price to yield changes is captured by **duration** — the next concept in your sequence — which quantifies how much a bond's price changes for a given change in YTM, varying systematically with maturity and coupon structure.
