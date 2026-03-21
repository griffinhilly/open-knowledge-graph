---
id: bonds-and-fixed-income
title: Bonds and Fixed Income
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: investment-risk-and-return
  type: hard
- id: time-value-of-money-personal
  type: hard
- id: percent-concept
  type: soft
builds-toward:
- index-fund-investing
tags:
- bonds
- fixed-income
- yield
- duration
- interest-rate-risk
stage: formal-systems
status: validated
---

# Bonds and Fixed Income

## Core Idea
A bond is a debt instrument: the issuer borrows money, promises to pay periodic coupon interest, and repays principal at maturity. Bond prices and interest rates move inversely — when prevailing rates rise, existing bonds with lower coupons become less valuable. Duration measures a bond's price sensitivity to rate changes. Government bonds (Treasuries) carry minimal default risk; corporate and municipal bonds carry varying credit risk and pay higher yields as compensation. Bonds provide portfolio stability and income, serving as a counterweight to equity volatility.

## How It's Best Learned
Model a simple bond: price it at par, then recalculate its price if prevailing rates rise by 2%. Understanding this inverse relationship numerically makes the abstract principle concrete. Then look up current yield curves to see how real bond markets price different maturities.

## Common Misconceptions
- Bonds are always safe; they carry interest rate risk (price loss if rates rise) and credit risk (default risk for non-government issuers).
- Holding a bond fund is the same as holding bonds to maturity; bond funds have perpetually fluctuating prices and no guaranteed return of principal.

## Questions

```yaml
- question: "You hold a bond paying a 4% annual coupon. Market interest rates rise from 4% to 7%. What happens to the market price of your bond?"
  type: multiple-choice
  options:
    - "It rises, because your bond now yields more relative to the new rate"
    - "It stays the same, since the coupon payment is contractually fixed"
    - "It falls, because new bonds offer higher rates, making your lower-coupon bond less attractive"
    - "It depends on whether the issuer is a government or corporation"
  answer: 2
  explanation: "This is the fundamental inverse relationship: when rates rise, existing bond prices fall. Your 4% bond now competes with new bonds paying 7%. No one will pay full price for your bond when they can get a better return elsewhere. The price of your bond must fall far enough that its yield (coupon ÷ discounted price) matches the 7% market rate. This price adjustment is not optional — it is an arithmetic identity that follows from present-value discounting."

- question: "Bond A matures in 2 years. Bond B has identical coupon and face value but matures in 20 years. Interest rates rise by 1%. Which bond loses more market value?"
  type: multiple-choice
  options:
    - "Bond A, because shorter bonds are more sensitive to rate changes"
    - "They lose the same value since both have identical coupons"
    - "Bond B, because longer duration means greater price sensitivity to rate changes"
    - "Bond A, because shorter bonds have less income to offset the price loss"
  answer: 2
  explanation: "Duration — a bond's weighted-average time to receive cash flows — measures interest rate sensitivity. Bond B's 20-year maturity means its cash flows are spread far into the future, so small changes in the discount rate have a large compounding effect on their present value. A rough rule: a bond with duration of 20 years loses about 20% of its price for a 1% rate rise. Bond A's cash flows are received soon, so discounting them slightly more has a small effect. Longer maturity → higher duration → greater price risk."

- question: "Government bonds (like U.S. Treasuries) are completely risk-free investments."
  type: true-false
  answer: false
  explanation: "False — government bonds have minimal credit (default) risk, but they still carry interest rate risk. If you hold a Treasury bond and prevailing rates rise, the market value of your bond falls. You can lose money if you sell before maturity. Bond funds holding Treasuries lost substantial value in 2022 when the Federal Reserve raised rates sharply. 'Safe' in bond context means low default risk, not freedom from price fluctuation. Duration determines how much interest rate risk a bond carries regardless of issuer."

- question: "When market interest rates fall, existing bond prices rise."
  type: true-false
  answer: true
  explanation: "True — this is the same inverse relationship from the other direction. If market rates fall to 1% and your bond pays 4%, your bond pays far more than newly issued alternatives. Investors will pay a premium above face value to acquire your higher-coupon bond, driving its price up. Mathematically, the bond's fixed cash flows are now discounted at a lower rate, increasing their present value. The bond-rate inverse relationship is perfectly symmetric: rates up → prices down, rates down → prices up."

- question: "Explain in your own words why bond prices and interest rates move in opposite directions."
  type: short-answer
  answer: "A bond is a promise to pay fixed future cash flows (coupons + face value at maturity). Its price is the present value of those cash flows. When interest rates rise, future cash flows are discounted more heavily, so their present value falls — the bond's price falls. Intuitively: if new bonds offer 6% and yours pays 3%, no one pays face value for yours. Its price drops until the effective yield (annual payment ÷ discounted price) matches 6%. The fixed cash flows don't change; only the rate at which they're valued does."
  explanation: "The inverse relationship is not a market quirk — it is a mathematical consequence of present-value discounting. Understanding it prevents the common mistake of thinking 'safe bonds' can't lose value. They can, if rates rise and you need to sell before maturity."
```

## Explainer

You already understand from your study of risk and return that higher potential reward comes with higher risk, and that the time value of money means a dollar today is worth more than a dollar in the future. Bonds apply both concepts directly. When a government or corporation needs to borrow money, it can issue a bond: a formal promise to pay you a fixed amount periodically (the **coupon**) and return your principal (the **face value** or **par value**) at a specified future date (the **maturity date**). In exchange for lending your money today, you receive a predictable income stream over time.

The most important principle in bond investing is the inverse relationship between bond prices and interest rates. Here is the intuition: suppose you hold a bond paying 3% annually and market rates rise to 5%. Your bond suddenly looks unattractive — new bonds pay more. For anyone to want your 3% bond, they would only buy it at a discount, so its price falls. The reverse is also true: if market rates fall to 1%, your 3% bond looks very attractive, and its price rises above par. This relationship is not optional or situational — it is an arithmetic identity. **Duration** measures how sensitive a bond's price is to rate changes; a bond with a 10-year duration loses roughly 10% of its price for each 1% rise in rates. Longer-maturity bonds have higher duration and therefore more interest rate risk.

Not all bonds carry the same **credit risk** — the chance the issuer defaults and fails to repay. U.S. Treasury bonds are considered essentially risk-free (the government can print currency); investment-grade corporate bonds carry modest credit risk; high-yield ("junk") bonds carry substantial default risk. The market compensates you for taking credit risk by offering higher yields. This is the same risk-return tradeoff you studied in investment fundamentals, applied to lending rather than owning. Ratings agencies (Moody's, S&P) provide letter grades to help investors assess credit risk, though these ratings have limitations.

Bonds serve a specific portfolio role: they tend to be less volatile than stocks and often move in the opposite direction during equity downturns, since investors flee to safer assets during market stress. This **negative correlation** is what makes bonds valuable as a portfolio stabilizer. A common rule of thumb is to hold a percentage of bonds roughly equal to your age, shifting gradually from growth-oriented stocks to income-oriented bonds as you approach retirement and can afford less volatility. Understanding the bond-rate inverse relationship is the key mental model — it explains why bond prices fell sharply in 2022 when interest rates rose rapidly, even though bonds are considered "safe."
