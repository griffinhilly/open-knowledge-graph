---
id: bond-basics
title: Bonds and Fixed Income Instruments
domain: economics
course: financial-economics
prerequisites:
- id: interest-rates-and-loanable-funds
  type: hard
- id: time-value-of-money
  type: soft
builds-toward:
- bond-pricing
- yield-to-maturity
- term-structure-of-interest-rates
tags:
- bonds
- fixed-income
- coupon
- face-value
- debt-securities
stage: formal-systems
status: validated
---

# Bonds and Fixed Income Instruments

## Core Idea
A bond is a debt security in which the issuer borrows from investors and commits to pay periodic interest (coupon payments) plus return the principal (face value) at maturity. Bonds are characterized by their face value, coupon rate, maturity date, and credit quality. Government bonds (Treasuries) carry essentially no default risk in nominal terms, while corporate bonds bear default risk and pay a credit spread above Treasuries. The bond market globally exceeds the equity market in total value and is central to monetary policy transmission, government financing, and portfolio construction.

## How It's Best Learned
Study a real Treasury bond prospectus to connect terminology to actual instruments. Distinguish between zero-coupon bonds (no interim payments), coupon bonds, and callable bonds (where the issuer may redeem early). Compare bonds across different credit ratings and maturities side by side.

## Common Misconceptions
- The coupon rate is fixed at issuance; the current yield and yield to maturity change daily as the market price moves.
- Government bonds have no default risk but carry substantial interest rate risk — their prices fall when rates rise.

## Questions

```yaml
- question: "You hold a corporate bond with a 6% coupon rate on a $1,000 face value. Market interest rates rise to 8%. What happens to the market price of your bond?"
  type: multiple-choice
  options:
    - "It rises — investors pay a premium because the 6% coupon is now above the market rate"
    - "It stays the same — the coupon rate is fixed at 6% regardless of market conditions"
    - "It falls — investors won't pay full price when new bonds offer 8% coupons"
    - "It rises — higher interest rates signal a stronger economy, which improves bond values"
  answer: 2
  explanation: "When market rates rise to 8%, newly issued bonds pay $80 per year on $1,000 face value. Your bond pays only $60 per year. Rational investors won't pay $1,000 for your bond when they can buy a new one yielding 8%. The price of your bond must fall until the $60 coupon represents an 8% return on the lower price — the bond becomes a 'discount bond.' This inverse relationship between bond prices and interest rates is mechanical: it follows directly from the present-value formula. This is the most important thing to internalize about bonds."

- question: "A bond with a 5% coupon rate is currently trading at $920 (below its $1,000 face value). What can you conclude about its yield to maturity (YTM)?"
  type: multiple-choice
  options:
    - "YTM is less than 5% — the discount reduces the effective return"
    - "YTM equals 5% — the coupon rate defines the return regardless of price"
    - "YTM is greater than 5% — buying below par increases the effective return"
    - "YTM cannot be determined without knowing the maturity date"
  answer: 2
  explanation: "When a bond trades below par (a discount bond), its YTM exceeds its coupon rate. The buyer pays $920 for a bond that will return $1,000 at maturity — that $80 capital gain adds to the $50 annual coupon payment, so the total return exceeds 5%. The coupon rate is a fixed contractual feature set at issuance; YTM is the actual return earned by buying at today's market price and holding to maturity. Coupon rate = YTM only when the bond trades at exactly face value. The maturity date is needed for the precise YTM calculation, but the directional relationship (YTM > coupon rate when trading at a discount) holds as stated."

- question: "US Treasury bonds are essentially risk-free because the US government cannot default on dollar-denominated debt."
  type: true-false
  answer: false
  explanation: "Treasury bonds have essentially no *default* risk in nominal terms — the government can always create dollars to repay. But they carry substantial *interest rate risk*: if market rates rise, the market value of existing Treasury bonds falls, potentially significantly. A 30-year Treasury bond is highly sensitive to rate changes; a 1% rise in rates can reduce its market value by 15–20%. For investors who may need to sell before maturity, this is very real risk. The common misconception is equating 'no default risk' with 'no risk' — two distinct things."

- question: "A bond's coupon rate and its yield to maturity are both measures of the bond's return, so they will converge to the same value over time."
  type: true-false
  answer: false
  explanation: "The coupon rate is a fixed contractual feature set at issuance — it never changes. The yield to maturity changes every day as the bond's market price changes. They are equal only when the bond trades at exactly face value (par). If the bond trades at a discount, YTM > coupon rate; at a premium, YTM < coupon rate. They do not 'converge' over time — if anything, as a bond approaches maturity its price gravitates toward face value (pulling price toward par), which in turn brings YTM toward the coupon rate, but this is a price-convergence effect, not an inherent feature of the two rates themselves."

- question: "Explain in your own words why bond prices fall when market interest rates rise. What is the underlying logic, and why is this relationship described as 'mechanical'?"
  type: short-answer
  answer: "A bond's price is the present value of all its future cash flows (coupons plus face value). When market interest rates rise, the discount rate used to calculate present value rises, so the present value of each future payment falls. Equivalently: new bonds now offer higher coupons, so existing bonds with lower fixed coupons must sell at a discount to offer the same total return. The relationship is 'mechanical' because it follows necessarily from the present-value formula — it's not a market sentiment effect but arithmetic."
  explanation: "The intuition: your bond is locked into paying $50/year when the market now demands $70/year for the same risk. The only way your bond can compete is if its purchase price drops enough that the $50 coupon plus the capital gain at maturity (buying at a discount, receiving face value) equals the market return. Present value math converts this intuition into a precise price. Every percentage-point rise in rates translates into a price drop whose magnitude depends on the bond's maturity and coupon — longer maturities are more sensitive because there are more future cash flows being discounted at the higher rate."
```

## Explainer

A bond is simply a loan that has been packaged into a tradeable security. When you lend money by buying a bond, the borrower (the **issuer**) promises to pay you a series of fixed cash flows: periodic **coupon payments** (typically semiannual) equal to the coupon rate times the **face value** (also called par value), plus the face value itself returned at **maturity**. Your prerequisite on the time value of money is the key to understanding everything that follows: each of these future cash flows is worth less than its face amount today, and the bond's market price is exactly the present value of all those future payments.

The relationship between bond prices and interest rates is the most important thing to internalize. Suppose you hold a bond paying 5% coupons on $1,000 face value — that's $50 per year. Now imagine market interest rates rise to 7%. New bonds are being issued paying $70 per year on a $1,000 face value. Nobody will pay $1,000 for your old 5% bond when they can get a 7% bond instead. The price of your bond must fall until the $50 coupon represents a 7% return on the lower price. This inverse relationship — **when rates rise, bond prices fall; when rates fall, bond prices rise** — is mechanical, not incidental. It follows directly from the present-value formula you already know.

This is why the common misconception in the notes deserves emphasis: the **coupon rate** is a fixed contractual feature set at issuance, like a printed label. The **yield to maturity (YTM)** is the actual return you earn by buying the bond at today's market price and holding it to maturity — it changes every day as the price changes. When the bond trades at face value, coupon rate equals YTM. When it trades below par (a **discount bond**), YTM > coupon rate. When it trades above par (a **premium bond**), YTM < coupon rate. The market price adjusts until the YTM matches what investors demand for the bond's risk.

Credit quality introduces the second dimension. A **Treasury bond** backed by the US government carries essentially no **default risk** — the government can always print dollars. But as noted, it carries substantial **interest rate risk**. A **corporate bond** adds **default risk**: the issuer might fail to make payments. Investors demand a **credit spread** — extra yield above the Treasury rate — as compensation. This spread widens when the issuer's finances deteriorate and narrows when they improve. Investment-grade bonds carry lower spreads; high-yield (junk) bonds carry higher spreads, compensating investors for the higher probability of default. The bond's price encodes all of this: it is whatever price makes the YTM (including the credit spread) match what the market demands given the issuer's risk profile and the current level of interest rates. Mastering this interplay between price, yield, maturity, and credit quality is the foundation of all fixed-income analysis.
