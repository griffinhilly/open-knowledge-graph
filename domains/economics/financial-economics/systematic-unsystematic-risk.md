---
id: systematic-unsystematic-risk
title: Systematic and Unsystematic Risk Decomposition
domain: economics
course: financial-economics
prerequisites:
- id: beta-and-systematic-risk
  type: hard
builds-toward:
- cost-of-equity-capm
tags:
- risk-measurement
- beta
- capm
stage: formal-systems
status: draft
---

# Systematic and Unsystematic Risk Decomposition

## Core Idea
Total risk = systematic risk (market-related, β) + unsystematic risk (firm-specific, diversifiable). Well-diversified portfolios eliminate unsystematic risk; only systematic risk remains and is priced in equilibrium, determining expected returns via CAPM.

## How It's Best Learned
Regress stock returns on market returns; the slope is beta (systematic risk exposure). Calculate R² to see what fraction of risk is systematic versus unsystematic.

## Questions

```yaml
- question: "Stock A has very high total variance, but most of it comes from firm-specific events uncorrelated with the market (low beta). Stock B has lower total variance but almost all of it is correlated with the market (high beta). According to CAPM, which stock should have the higher expected return?"
  type: multiple-choice
  options:
    - "Stock A, because higher total volatility means investors demand more compensation"
    - "Stock B, because its risk is systematic and cannot be diversified away — the market prices only this component"
    - "Stock A, because total variance always determines expected return under rational pricing"
    - "They should have the same expected return since both have the same total risk if properly measured"
  answer: 1
  explanation: "CAPM prices only systematic risk (beta), not total risk. Stock A's high variance is mostly idiosyncratic — a rational investor can eliminate it by diversifying. Since this risk is costlessly removable, the market does not reward bearing it. Stock B's variance is mostly market-correlated and cannot be diversified away, so investors require a risk premium. This is the central insight of CAPM: expected return depends on beta, not σ²."

- question: "An investor holds an equally weighted portfolio of 50 stocks from unrelated industries. Which statement best describes the effect of this diversification on portfolio risk?"
  type: multiple-choice
  options:
    - "Both systematic and unsystematic risk decrease as more uncorrelated stocks are added"
    - "Unsystematic risk decreases toward zero as idiosyncratic shocks cancel out; systematic risk (market exposure) cannot be eliminated this way"
    - "Systematic risk decreases because beta averages out across many different stocks"
    - "Total risk increases because holding more stocks exposes the investor to more potential losses"
  answer: 1
  explanation: "When you combine stocks whose idiosyncratic shocks are uncorrelated, the firm-specific variances cancel each other (one company's bad news is offset by another's good news). In the limit, the portfolio retains only systematic risk — the component that affects all stocks simultaneously. Systematic risk cannot be diversified away because market movements hit every stock in the portfolio at the same time. Beta of the portfolio is the weighted average of individual betas, which does not go to zero."

- question: "A stock with high total variance but low beta may have a lower expected return than a stock with low total variance but high beta."
  type: true-false
  answer: true
  explanation: "Expected return in CAPM is determined solely by beta (systematic risk), not total variance. A volatile stock whose variance is mostly idiosyncratic can have a low expected return if its beta is small. A less volatile stock that moves closely with the market can have a high expected return if its beta is large. This is counterintuitive but follows directly from the principle that only undiversifiable risk is priced."

- question: "Holding a highly concentrated position in a single volatile stock earns a higher expected return than a diversified portfolio with the same total variance, because the investor bears more risk."
  type: true-false
  answer: false
  explanation: "If the concentrated stock's high variance is mostly idiosyncratic (low beta), the market does not reward bearing it — the investor could have eliminated that variance costlessly through diversification. Expected return is not compensation for total risk; it is compensation for systematic risk. A concentrated position adds idiosyncratic risk that goes unpriced. The market only pays a premium for the component of risk that is impossible to diversify away."

- question: "Why does the market not compensate investors for bearing unsystematic risk? What would happen in equilibrium if it did?"
  type: short-answer
  answer: "Unsystematic risk is diversifiable at near-zero cost: adding more uncorrelated stocks eliminates idiosyncratic variance. If the market paid a premium for idiosyncratic risk, rational investors would immediately diversify it away and still capture the premium — a free lunch. Arbitrageurs would buy diversified portfolios of high-idiosyncratic-risk stocks, pocket the premium, and bear no net idiosyncratic risk. In equilibrium, this demand pressure would drive prices up and expected returns down until no premium remained for diversifiable risk."
  explanation: "The key is the word 'diversifiable.' Rational markets only price risks that someone must bear. Systematic risk must be held in aggregate by the market portfolio — it cannot be netted out. Unsystematic risk, however, can be netted out across investors, so no one needs to bear it. Competition among rational investors eliminates any premium for risk that can be avoided for free."
```

## Explainer

You already know that beta measures a stock's sensitivity to market movements — a stock with β = 1.5 tends to move 1.5% for every 1% move in the market. This topic makes that picture more precise by asking: what is the rest of the stock's movement doing? If beta explains the market-related part of a stock's return, something else must explain the departures from that pattern. The answer is **unsystematic risk** — variation driven by firm-specific events that have nothing to do with the broader market.

Think about the sources of stock price movements. When the Fed raises interest rates, nearly every stock falls — this is systematic risk, because the shock hits the whole market. When a pharmaceutical company announces that its flagship drug failed a clinical trial, that company's stock plummets while the rest of the market barely notices — this is unsystematic risk, also called **idiosyncratic risk** or **firm-specific risk**. The decomposition is: Total Risk = Systematic Risk + Unsystematic Risk, or in variance terms: σ²_i = β²_i·σ²_m + σ²_ε, where σ²_m is market variance and σ²_ε is the variance of the firm-specific residual.

The crucial insight is that these two components are treated very differently by the market's pricing mechanism. Unsystematic risk is **diversifiable**: if you hold a portfolio of 30 or more stocks, the firm-specific shocks tend to cancel out across positions. One company's drug failure is offset by another's surprise earnings beat. As you add more stocks, idiosyncratic variance approaches zero in a well-diversified portfolio. Systematic risk, by contrast, cannot be diversified away — when the whole market falls, every stock in your portfolio falls too.

Because rational investors can eliminate unsystematic risk cheaply through diversification, the market does not compensate them for bearing it. You receive no additional expected return for holding a concentrated position in a single volatile stock, because the idiosyncratic volatility could have been eliminated costlessly. What the market does price is **systematic risk** — the component measured by beta that cannot be escaped no matter how broadly you diversify. This is the foundation of CAPM: expected return is a function of beta alone, not total volatility. A stock with high total variance but low beta (because most of its variance is idiosyncratic) should have a low expected return. A stock with modest total variance but high beta should have a high expected return. The R² from regressing a stock's returns on the market tells you exactly what fraction of total risk is systematic — and therefore what fraction is being priced.
