---
id: collateral-haircut-valuation
title: Collateral Valuation and Haircuts in Repo Markets
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: leverage-and-margin-trading
  type: soft
builds-toward:
- financial-crisis-contagion
tags:
- repo
- collateral
- leverage
- valuation
stage: formal-systems
status: draft
---

# Collateral Valuation and Haircuts in Repo Markets

## Core Idea
In repo transactions, haircuts discount collateral value to protect the lender against price declines and liquidation costs. Haircuts vary by collateral type and market stress: safe government securities have low haircuts while illiquid assets have high haircuts. During crises, haircuts spike suddenly, forcing rapid deleveraging and asset fire sales, as seen in 2008 when repo haircuts increased sharply.

## Questions

```yaml
- question: "A bond worth $100 has a 5% repo haircut. How much cash can the borrower receive, and what leverage ratio does this create on the borrower's equity?"
  type: multiple-choice
  options:
    - "$105, creating 1:1 leverage — the haircut adds a safety premium to collateral value"
    - "$95, creating approximately 20:1 leverage on the $5 equity cushion"
    - "$50, creating 2:1 leverage — haircuts are symmetric around par value"
    - "$100, creating unlimited leverage — the haircut is a fee, not a principal discount"
  answer: 1
  explanation: "A 5% haircut means the lender advances 95% of collateral value: $95 on a $100 bond. The borrower posts $100 of collateral and receives $95 of cash, keeping a $5 equity stake. That $5 of equity controls $100 of assets — leverage of 20:1. This amplification is why haircuts are so consequential: a small change in collateral value wipes out equity entirely, and a small increase in the haircut dramatically reduces the cash available."

- question: "During a financial crisis, what happens to repo haircuts on risky assets, and why does this worsen the crisis rather than stabilize it?"
  type: multiple-choice
  options:
    - "Haircuts fall, making credit cheaper and stabilizing asset prices"
    - "Haircuts rise, forcing deleveraging that drives fire sales and further price declines"
    - "Haircuts stabilize automatically because central banks set them countercyclically"
    - "Haircuts rise but only affect new lending, leaving existing repo positions unchanged"
  answer: 1
  explanation: "Haircuts are procyclical: they rise sharply during crises precisely when lenders perceive higher price and liquidity risk. Borrowers who cannot post additional collateral are forced to sell assets immediately. When many levered institutions face higher haircuts simultaneously — because they all hold similar collateral — they all become forced sellers at once, depressing prices, which justifies still-higher haircuts: the haircut spiral. This is how localized credit stress becomes system-wide liquidity crisis."

- question: "A haircut primarily protects the lender from the risk that the borrower might default on the repurchase obligation."
  type: true-false
  answer: false
  explanation: "A haircut protects the lender from *collateral price risk* and *liquidation risk* — not directly from borrower default risk. If the borrower defaults, the lender already holds the collateral and sells it to recover the loan. The haircut ensures the sale proceeds will exceed the loan amount even after price declines during the liquidation period. Default risk per se is addressed by the right to seize and sell collateral; the haircut addresses whether that collateral will still be worth enough when it is sold."

- question: "In calm markets, low repo haircuts are a sign of healthy, efficiently functioning financial markets."
  type: true-false
  answer: false
  explanation: "Low haircuts in calm markets enable very high leverage, creating systemic fragility that is invisible until it unwinds. The conditions that make markets appear healthy — low volatility, liquid markets, stable prices — are exactly what allow haircuts to fall and leverage to build. When conditions reverse, this hidden leverage becomes the amplification mechanism for the crisis. Procyclically low haircuts are efficient at the micro level but dangerous at the macro level — this is a key reason the 2008 crisis was so severe."

- question: "Explain the 'haircut spiral' mechanism. Why do rising haircuts during a crisis cause further price declines rather than simply reducing new borrowing?"
  type: short-answer
  answer: "When haircuts rise, leveraged borrowers must post more collateral or repay part of the loan. Many cannot, so they sell assets to raise cash. When many institutions simultaneously face higher haircuts on similar collateral, they all become forced sellers at once. This drives asset prices down, which reduces collateral values and justifies still-higher haircuts, forcing more selling — a self-reinforcing cycle. The spiral transforms isolated credit stress into system-wide liquidity crisis through this feedback loop."
  explanation: "The spiral is self-reinforcing because haircuts respond endogenously to the prices they are causing to fall. Individual lenders acting rationally — demanding more protection as collateral becomes riskier — collectively produce an outcome that destroys the values they are trying to protect. In 2008, repo haircuts on mortgage-backed securities rose from 2–3% to 20–40% nearly overnight, forcing massive fire sales across asset classes as institutions sold their most liquid holdings to raise cash."
```

## Explainer

In a **repurchase agreement** (repo), one party sells a security to another with a promise to buy it back at a higher price on a specified date. Economically, this is a collateralized loan: the seller receives cash now, the buyer holds the security as collateral, and the price difference is the interest. If the seller defaults before the repurchase date, the buyer sells the collateral to recover the loan. From your bond pricing background, you know that bond prices fluctuate with yields, credit spreads, and market liquidity. The buyer therefore faces risk: collateral value might fall below the outstanding loan between default and liquidation, leaving the lender with a loss.

The **haircut** addresses this directly. If a bond is worth $100, the lender might advance only $95 — a 5% haircut — keeping a $5 cushion. The borrower receives only 95% of collateral value as cash, but posts 100% as security. The haircut compensates for two risks: (1) **price risk** — the collateral may decline in value before liquidation can be completed, and (2) **liquidation risk** — the collateral may be hard to sell quickly in stressed conditions without accepting a large discount. US Treasury bills have haircuts near zero because their prices are stable and markets are extremely deep. High-yield corporate bonds or structured credit products carry haircuts of 10–30% or more because their prices can gap down rapidly and thin markets may not absorb large sales without significant price concessions.

The danger lies in the **procyclicality** of haircuts. In calm markets, haircuts are low, enabling high leverage. Using your leverage knowledge: if a haircut is 5%, a borrower can post $100 of collateral and borrow $95, achieving roughly 20:1 leverage — small price moves on the underlying position are amplified enormously into equity. When a crisis hits and asset prices begin falling, lenders suddenly demand much higher haircuts on the same collateral — they perceive sharply higher price and liquidity risk. The borrower must now return cash or post additional collateral to meet the new margin requirement. If they cannot, they are forced to sell assets. When all leveraged institutions simultaneously face higher haircuts — because they all hold similar collateral — they all become forced sellers at once. This drives prices down further, which justifies still-higher haircuts, which forces more selling: the **haircut spiral**.

The 2008 financial crisis illustrated this mechanism in stark relief. Mortgage-backed securities and other structured products were widely used as repo collateral. As housing prices declined and underlying credit quality became uncertain, repo haircuts on these assets rose sharply — in some cases from 2–3% to 20–40% nearly overnight. Borrowers who had been leveraged 20:1 or 30:1 were forced to liquidate massive positions quickly. The cascade of fire sales depressed prices across asset classes as institutions sold their most liquid holdings (Treasuries, equities) to raise cash, transmitting stress far beyond the initial epicenter. This is why collateral haircut dynamics are central to understanding financial crisis contagion: they are the transmission mechanism through which localized credit concerns become system-wide liquidity crises.
