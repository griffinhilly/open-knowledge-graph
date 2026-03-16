---
id: investment-risk-and-return
title: Investment Risk and Return
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: compound-interest
  type: hard
- id: time-value-of-money-personal
  type: hard
- id: percent-concept
  type: soft
- id: mean-median-mode
  type: soft
- id: simple-probability
  type: soft
- id: inflation-and-purchasing-power
  type: soft
- id: expected-value
  type: soft
- id: variance-of-random-variables
  type: soft
- id: variance-standard-deviation
  type: soft
- id: probability-with-combinatorics
  type: soft
builds-toward:
- stock-market-fundamentals
- bonds-and-fixed-income
- index-fund-investing
tags:
- risk
- return
- volatility
- diversification
- asset-classes
stage: abstract-reasoning
status: validated
---
# Investment Risk and Return

## Core Idea
Expected return and risk (measured as volatility or potential loss) are positively correlated across asset classes: higher potential returns require accepting higher potential losses. Diversification across uncorrelated assets reduces portfolio volatility without proportionally reducing expected returns, because individual asset risks partially cancel out. The appropriate risk level depends on investment horizon — longer horizons allow time to recover from downturns — and personal risk tolerance. Understanding this tradeoff prevents both reckless speculation and overly conservative choices that fail to outpace inflation.

## How It's Best Learned
Examine historical annual return distributions for stocks (e.g., S&P 500), bonds, and cash over 50+ years. Note not just average returns but the range and worst years. Then model how portfolio allocation shifts the distribution of 30-year wealth outcomes.

## Common Misconceptions
- High past returns guarantee future returns for a specific investment; past performance reflects historical conditions, not future prospects.
- Diversification means owning many funds; five highly correlated large-cap U.S. equity funds provide almost no diversification benefit.

## Questions

```yaml
- question: "An investor can choose between Asset A (expected return 4%, low volatility) and Asset B (expected return 10%, high volatility). Which statement best describes the risk-return tradeoff?"
  type: multiple-choice
  options: ["Asset B is strictly better because it has a higher expected return", "Asset A is strictly better because it avoids the risk of loss", "Asset B's higher expected return compensates for the possibility of larger losses; the right choice depends on the investor's time horizon and risk tolerance", "The two assets are equivalent because diversifying between them averages out to 7%"]
  answer: 2
  explanation: "The risk-return tradeoff means neither asset is universally 'better.' Asset B's higher expected return is compensation for accepting the possibility of larger losses. An investor with a long time horizon can weather downturns; one needing funds soon cannot. Option D conflates the concept of diversification with expected return averaging — blending assets changes the volatility profile, not just the midpoint return."

- question: "Owning five different mutual funds automatically provides meaningful diversification."
  type: true-false
  answer: false
  explanation: "Diversification benefit comes from holding assets whose returns are not perfectly correlated — when one falls, others don't fall equally. Five large-cap U.S. equity funds from different providers may hold many of the same underlying stocks and move nearly in lockstep. True diversification requires assets that respond differently to the same economic events (e.g., combining equities with bonds, international stocks, or real assets)."

- question: "Why does a longer investment time horizon generally allow an investor to accept more risk?"
  type: short-answer
  answer: "A longer horizon gives the portfolio time to recover from downturns. Short-term volatility becomes less relevant when the investor won't need to liquidate assets for decades; historically, diversified equity portfolios have recovered from all major crashes given enough time."
  explanation: "Risk in investments shows up as volatility — short-term prices can swing dramatically. But if an investor has 30 years before needing the money, they can ride out a 40% crash and benefit from the subsequent recovery. An investor who needs money in two years cannot afford to wait for a recovery, so they must hold lower-volatility assets even if expected returns are lower."
```

## Explainer

You already know from compound interest that money grows faster when returns are reinvested over time, and from time-value-of-money that a dollar today is worth more than a dollar tomorrow. Investment risk and return extends those ideas: the rate at which your money grows is not guaranteed — it depends on what you invest in, and higher potential growth comes with higher potential loss.

The core relationship is that risk and expected return move together across asset classes. Cash held in a savings account is nearly risk-free but earns little. Government bonds earn somewhat more but can lose value when interest rates rise. Stocks of large established companies ("equities") have historically returned around 7–10% per year on average, but individual years have ranged from -50% to +50%. Stocks of small or emerging-market companies are even more volatile with even higher long-run averages. This isn't random — the higher return is the market's way of compensating investors for tolerating uncertainty. Nobody would hold volatile stocks if they didn't expect better returns than a savings account.

Diversification is how you reduce the penalty for accepting risk. When you hold many assets whose returns are not perfectly correlated, losses in one are partially offset by gains in another. A portfolio of 500 stocks weathers a single company's bankruptcy far better than a portfolio of 5 stocks. But here's the misconception: holding five different funds that all own the same 500 U.S. companies gives you almost no diversification. True diversification means combining assets that react differently to the same economic events — equities and bonds, domestic and international, different sectors. The mathematics here connects to variance: the variance of a portfolio depends not just on individual variances but on the covariances between assets. Low or negative covariance is what actually reduces portfolio volatility.

Your appropriate risk level isn't fixed — it depends on your time horizon and your personal capacity to tolerate losses without panic-selling. A 25-year-old saving for retirement has 40 years for a portfolio to recover from crashes; they can rationally hold mostly equities. A 65-year-old who will start withdrawing funds in five years cannot afford a 40% drawdown and should hold more bonds. This is why "invest aggressively when young, shift conservative near retirement" is standard advice — it's not a rule of thumb but a direct consequence of the risk-return tradeoff and time horizon logic.

Finally, the most dangerous trap in investing is using past returns to predict future returns for specific investments. An asset that returned 25% last year may have simply been in favorable conditions that no longer exist. What persists over time is the general relationship — riskier asset classes tend to outperform safer ones over long periods — not the specific performance of any individual stock or fund. This is why diversified index funds (which we'll explore next) are the practical implementation of these principles for most investors.

