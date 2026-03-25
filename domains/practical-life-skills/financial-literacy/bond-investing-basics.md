---
id: bond-investing-basics
title: Bond Investing Basics
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: bonds-and-fixed-income
  type: hard
- id: apr-apy-and-interest-rate-calculation
  type: hard
- id: behavioral-finance-and-investing-psychology
  type: soft
- id: sustainable-and-values-based-investing
  type: soft
builds-toward:
- diversification-and-asset-allocation
tags:
- bonds
- fixed-income
- investing
stage: formal-systems
status: validated
---
# Bond Investing Basics

## Core Idea
Bonds are debt securities where investors lend money to governments or corporations in exchange for periodic interest payments and return of principal at maturity. Bond prices and interest rates move inversely; rising market rates cause existing bond prices to fall while providing entry points for new investors.

## Questions

```yaml
- question: "You bought a 10-year Treasury bond paying 3% annually when it was issued. Market interest rates then rise to 5%. What happens to the market price of your bond if you try to sell it today?"
  type: multiple-choice
  options:
    - "It rises — your bond is backed by the government and pays reliable income, making it more desirable"
    - "It stays the same — your bond's coupon rate is fixed by contract and cannot change"
    - "It falls — new bonds now pay 5%, so buyers will only purchase your 3% bond at a discount large enough to make its effective yield competitive"
    - "It rises — higher interest rates signal a stronger economy, which increases bond demand"
  answer: 2
  explanation: "This is the core bond insight: price and yield move inversely. Your bond's 3% coupon is fixed, but new bonds pay 5%. A rational buyer will only purchase your bond at a price low enough that the fixed $30/year payment (on $1,000 face value) represents a 5% yield on what they actually pay — roughly $600. The bond itself hasn't changed; the discount compensates the buyer for receiving a below-market coupon. The opposite is also true: if rates fall to 1%, your 3% bond becomes a premium asset, and its price rises above face value."

- question: "An investor needs their money back in 18 months. They are choosing between a 2-year Treasury bond and a 20-year Treasury bond. If interest rates unexpectedly rise by 2%, which position creates more risk for this investor?"
  type: multiple-choice
  options:
    - "The 2-year bond — short-term interest rates are more volatile than long-term rates"
    - "The 20-year bond — its much longer duration means its price will fall far more per percentage point of rate increase, creating a large potential loss if sold before maturity"
    - "Both are equally risky because both are backed by the U.S. government and guaranteed to repay face value"
    - "Neither creates risk because Treasury bonds cannot lose value"
  answer: 1
  explanation: "Duration is the key. The 20-year bond's cash flows extend far into the future; discounting all those future payments at a higher rate dramatically reduces their present value — the bond price could fall 20–25% or more. The 2-year bond matures in 24 months, so there are few future cash flows to reprice, and the price drops only modestly. The investor who needs cash in 18 months and holds the 20-year bond must sell at a large loss if rates rise. Government guarantee matters for repayment at maturity — but if you sell before maturity, market price is what you receive."

- question: "When market interest rates rise, bond prices rise because investors are receiving more income from their fixed coupon payments."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. When market rates rise, existing bond prices FALL. The coupon payment is fixed — it does not increase when rates rise. What changes is that new bonds entering the market offer higher coupon rates, making existing lower-coupon bonds less attractive. Their prices must fall until their yield (coupon divided by current price) matches the prevailing market rate. The investor's income from holding the bond to maturity is indeed fixed, but the bond's resale value drops immediately when rates rise."

- question: "A bond purchased below its face value (at a discount) will return exactly the face value at maturity, regardless of the purchase price."
  type: true-false
  answer: true
  explanation: "Yes — the bond contract specifies that the issuer will repay the face value (typically $1,000) at maturity, regardless of what the bondholder paid in the secondary market. If you buy a bond at $850 and hold it to maturity, you receive $1,000 — a $150 gain above what you paid, in addition to the coupon payments received along the way. This capital gain is part of the total return and is why discount bonds can offer attractive yields even with low coupon rates. The yield to maturity (YTM) calculation incorporates both the coupon payments and this price-to-face-value change."

- question: "Why do long-term bonds fall in price more than short-term bonds when interest rates rise by the same amount?"
  type: short-answer
  answer: "A long-term bond locks in its fixed coupon rate for many more years into the future. When interest rates rise, all those future cash flows — coupons and eventual principal repayment — must be discounted at the new, higher rate, which reduces their present value substantially. A short-term bond has few future cash flows to reprice: it matures soon, returning principal quickly, after which the investor can reinvest at the new higher rates. The longer the duration, the more sensitive the price to rate changes."
  explanation: "This is why duration is used as the measure of price sensitivity: it reflects the weighted average time until you receive your cash flows. A 30-year bond has a high duration because most of the value comes from distant future payments; a 6-month T-bill has near-zero duration because the entire value is received almost immediately. A 1% rise in rates causes roughly a 1% price drop for a bond with 1-year duration, but a ~15–20% price drop for a bond with 15–20-year duration. Matching bond duration to your investment time horizon is the core practical insight of bond investing."
```

## Explainer

When you buy a bond, you are acting as a lender. You hand money to a government or corporation, and in exchange they promise to pay you a fixed interest rate (the **coupon rate**) on regular intervals and return your original amount (the **principal** or **face value**) on a specific future date (the **maturity date**). This is why bonds are called **fixed-income** instruments — the cash flows are predetermined and contractual, unlike stock dividends which can be cut or eliminated. The fixed-income concept from your prerequisites applies directly here: you already understand APR and APY, so you can evaluate a bond's coupon rate as an annualized return on the amount lent.

The most important and initially confusing property of bonds is the **inverse price-rate relationship**: when market interest rates rise, the prices of existing bonds fall, and vice versa. Here is the intuition: imagine you own a bond paying 3% annual interest. If market rates suddenly rise to 5%, new bonds offer better returns. Your 3% bond becomes less attractive — the only way a buyer will purchase it from you is at a discount, so the effective yield matches the new market rate. The bond pays the same fixed coupon, but because the price fell, that coupon now represents a higher yield relative to what was paid. The reverse is equally true: if rates fall, your 3% bond becomes premium — buyers will pay more for it, driving its price above face value.

**Duration** is the key measure of this price sensitivity. A bond maturing in 30 years is far more sensitive to rate changes than one maturing in 2 years, because the fixed cash flows extend further into the future and therefore suffer more when discounted at a higher rate. Short-duration bonds (short-term) are more stable in price; long-duration bonds (long-term) offer higher yields but swing more when rates move. For practical investing, this means matching bond duration to your time horizon: money you need in two years belongs in short-term bonds, while money you will not need for decades can tolerate the price volatility of longer maturities.

Different **bond types** carry different risk levels. U.S. Treasury bonds are considered nearly risk-free because the federal government can always raise revenue or money supply to repay; their yields are the baseline against which all other bonds are compared. **Corporate bonds** pay higher yields because corporations can default — the spread above Treasuries reflects the market's assessment of default risk. **Municipal bonds** (issued by state and local governments) often carry tax advantages that make their lower nominal yield equivalent to higher after-tax returns for investors in high tax brackets. Understanding which type fits your needs means integrating the yield, risk, tax treatment, and your investment time horizon simultaneously.
