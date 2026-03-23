---
id: bonds-and-fixed-income-securities
title: Bonds and Fixed Income Securities
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: apr-apy-and-interest-rate-calculation
  type: hard
- id: saving-versus-investing-fundamental-distinction
  type: soft
builds-toward:
- investment-diversification
- risk-tolerance-asset-allocation
tags:
- bonds
- fixed-income
- government-bonds
- corporate-bonds
- interest-payments
stage: formal-systems
status: validated
---

# Bonds and Fixed Income Securities

## Core Idea
Bonds are debt instruments where you lend money to governments or corporations in exchange for periodic interest payments (coupons) and the return of principal at maturity. Bonds offer lower volatility and more predictable returns than stocks, making them valuable for conservative investors and portfolio diversification. Bond prices move inversely to interest rates.

## How It's Best Learned
Research current bond yields and compare them to stock market returns. Understand why investors might choose bonds despite lower returns when seeking stability.

## Common Misconceptions
Bonds are always safe (bond prices fluctuate with interest rates; default risk exists). If a bond's yield is low, it's not worth buying (low yields reflect strong credit quality and current rate environment).

## Questions

```yaml
- question: "You own a bond paying a 3% annual coupon. Market interest rates rise to 5%. What happens to your bond's market price if you try to sell it?"
  type: multiple-choice
  options:
    - "It rises — higher market rates make all bonds more attractive"
    - "It stays the same — the coupon payment is contractually fixed"
    - "It falls — investors can now get 5% elsewhere, so your 3% bond is less attractive without a price discount"
    - "It rises — the government adjusts bond values to compensate existing holders"
  answer: 2
  explanation: "When market rates rise above your bond's coupon, new bonds offer better income. Buyers will only purchase your bond at a discount — a lower price that raises its effective yield to be competitive with the 5% market rate. This is the fundamental inverse relationship: rising rates → falling bond prices. The coupon itself never changes; only the market price adjusts."

- question: "A corporation's credit rating is downgraded from AA to BBB. What would you expect to happen to the market prices of its existing bonds?"
  type: multiple-choice
  options:
    - "They rise — the corporation will now offer higher coupons on future bonds to attract investors"
    - "They remain unchanged — the face value is guaranteed at maturity regardless of credit rating"
    - "They fall — higher perceived default risk makes these bonds less desirable, requiring a lower price to compensate investors"
    - "They rise — lower-rated bonds are rarer and thus command a premium"
  answer: 2
  explanation: "A credit downgrade signals higher default risk — a greater chance the company won't repay. To compensate for that risk, the market demands a higher yield, which means existing bond prices must fall. The face value at maturity is only guaranteed if the company doesn't default, which is now perceived as less certain. Risk and price move in opposite directions."

- question: "A bond held all the way to its maturity date is completely protected from interest rate risk."
  type: true-false
  answer: false
  explanation: "If held to maturity, you do receive the full face value — so market price fluctuations don't result in realized losses. However, opportunity cost remains: if rates rise, you're locked into a lower yield and forgo the higher returns available from newly issued bonds. For investors who might need cash before maturity, falling market prices represent real losses. 'No realized price loss at maturity' is true; 'completely safe from interest rate risk' overstates the case."

- question: "All else equal, a 30-year bond will experience a larger price change in response to a given change in interest rates than a 5-year bond."
  type: true-false
  answer: true
  explanation: "Longer-maturity bonds are more sensitive to interest rate changes because their cash flows extend further into the future — a given change in the discount rate affects a larger total of discounted payments. This sensitivity is captured by a concept called duration: the longer the duration, the greater the price movement per unit change in rates. A 30-year bond might lose 15% of its value when rates rise 1%, while a 5-year bond might lose only 4%."

- question: "Explain in plain terms why bond prices and interest rates move in opposite directions."
  type: short-answer
  answer: "A bond's coupon payments are fixed at issuance. When market rates rise, newly issued bonds offer higher coupons, making existing bonds with lower coupons less attractive. For an existing bond to remain competitive, its price must fall enough that the fixed coupon represents a yield equivalent to current market rates. When rates fall, the fixed coupon becomes more attractive relative to new bonds, so the price rises. The price adjusts continuously to keep the bond's effective yield in line with the prevailing market."
  explanation: "The key insight is that the coupon is fixed but the price is not. Any time market conditions change, the price moves to make the effective return competitive — this is the market mechanism that keeps bond markets in equilibrium. Understanding this prevents the common mistake of thinking a bond is 'safer' just because it has a fixed payment."
```

## Explainer

When you learned about APR and interest rates, you were mostly thinking about debt from the borrower's side — the bank lends you money and charges you interest. A bond flips that relationship: now *you* are the lender. When a company or government needs to raise money, they can issue bonds, which are formal IOUs. You hand over cash today, and in return they promise to pay you regular interest (**coupons**) over time and return your original amount (**principal** or **face value**) when the bond reaches its **maturity date**.

The vocabulary is easiest to understand through a concrete example. Suppose the U.S. Treasury issues a 10-year bond with a face value of $1,000 and a coupon rate of 4%. You lend the Treasury $1,000. Every year for ten years, you receive $40 (4% of $1,000). At the end of year 10, you get your $1,000 back. Total received: $1,400. The $400 in interest is your compensation for letting someone else use your money for a decade — and for accepting the (small) risk that they might not pay you back.

The trickiest concept in bonds is the inverse relationship between bond prices and interest rates, and it's one that trips up new investors. Imagine you buy that 4% bond today. Tomorrow, new bonds are issued at 5% because rates rose. Your bond — still paying only 4% — is now less attractive. If you tried to sell it, no one would pay full price for $40 per year when they could get $50 for the same $1,000 investment. So your bond's market price drops. The reverse is also true: if rates fall to 3%, your 4% bond becomes *more* attractive, and its price rises. The coupon payment never changes; it's the price of the bond in the secondary market that adjusts to keep its effective return competitive. This is why bond values fall when interest rates rise — a critical pattern for any investor holding bonds in a portfolio.

From your study of saving versus investing, you know that different financial instruments involve different tradeoffs between risk and return. Bonds sit in the middle of that spectrum. They're riskier than a savings account (prices can fall, and issuers can default) but generally less volatile than stocks. That predictability is why bonds play an important role in diversified portfolios — especially for investors nearing retirement who need reliable income and can't afford to wait out a stock market downturn. The mix of stocks and bonds in a portfolio is one of the most consequential decisions in personal investing.
