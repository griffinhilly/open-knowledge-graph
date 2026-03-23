---
id: factor-models-multifactor-pricing
title: Factor Models and Multifactor Pricing (Fama-French)
domain: economics
course: financial-economics
prerequisites:
- id: arbitrage-pricing-theory
  type: hard
- id: capital-asset-pricing-model
  type: hard
- id: eigenvalues-eigenvectors
  type: soft
tags:
- multifactor-models
- apt
- asset-pricing
stage: advanced
status: validated
---

# Factor Models and Multifactor Pricing (Fama-French)

## Core Idea
Multifactor models extend CAPM by adding risk factors beyond market return. The Fama-French 3-factor model adds size (SMB) and value (HML) factors; newer versions include profitability and investment factors. Each factor premium compensates systematic exposure; these models explain cross-sectional return variation better than single-factor CAPM.

## How It's Best Learned
Regress stock returns on Fama-French factors. Compare model R² and explanatory power to single-factor CAPM. Interpret factor exposures as systematic risks.

## Questions

```yaml
- question: "A small-cap stock with a high book-to-market ratio has CAPM beta = 0.9 — below the market average. CAPM predicts it should earn slightly below-market returns. What does the Fama-French 3-factor model predict for this stock's expected return compared to CAPM's prediction?"
  type: multiple-choice
  options:
    - "The same as CAPM — beta is the only relevant risk measure"
    - "Lower than CAPM — small-cap and value stocks are safer, so their required return is lower"
    - "Higher than CAPM — positive SMB and HML loadings add expected return beyond the market factor"
    - "Indeterminate — factor loadings only affect volatility, not expected returns"
  answer: 2
  explanation: "This stock has positive exposure to both the SMB (small minus big) and HML (high minus low book-to-market) factors. In the Fama-French model, expected return includes compensation for these factor exposures: E[Rᵢ] = Rf + βmkt(Rm−Rf) + βSMB·E[SMB] + βHML·E[HML]. Since both additional factor premiums are positive and this stock loads positively on both, its expected return is *higher* than CAPM alone would predict — despite its below-average market beta. CAPM systematically underpredicts returns for small-cap value stocks, which is exactly the empirical anomaly Fama-French was designed to explain."

- question: "A fund manager claims her portfolio generates positive alpha in the Fama-French 3-factor model, proving she has superior stock-picking skill. What is the key challenge to this interpretation?"
  type: multiple-choice
  options:
    - "Fama-French alpha is always zero by construction, so positive alpha is impossible"
    - "The positive alpha could reflect exposure to additional systematic risk factors (e.g., momentum, profitability) not included in the 3-factor model, rather than genuine skill"
    - "Alpha in the Fama-French model only measures trading costs, not skill"
    - "Factor models cannot be applied to managed portfolios, only to individual stocks"
  answer: 1
  explanation: "Alpha is measured relative to the factors included in the model. If the portfolio systematically loads on factors outside the model — like momentum (WML) or profitability (RMW) — those factor premiums appear as 'alpha' in the 3-factor regression but represent compensation for bearing systematic risk, not managerial skill. A manager who tilts toward past winners earns momentum premium but appears to have positive alpha in a model that doesn't include momentum. True alpha requires a model that fully controls for all priced risk factors, which remains an open empirical challenge."

- question: "The Fama-French 3-factor model explains a higher proportion of cross-sectional return variation than single-factor CAPM."
  type: true-false
  answer: true
  explanation: "Empirically, the Fama-French 3-factor model explains roughly 90% of cross-sectional return variation across diversified portfolios, compared to about 70% for CAPM. The addition of SMB and HML factors captures systematic return patterns — the size premium and value premium — that CAPM's single market factor cannot explain. This improvement motivated the entire multifactor empirical asset pricing research program."

- question: "SMB and HML are long-short portfolios with zero expected return under the null hypothesis that CAPM fully describes expected returns."
  type: true-false
  answer: false
  explanation: "Under CAPM, any portfolio's expected return is fully explained by its market beta. SMB and HML are constructed precisely to capture returns that CAPM *cannot* explain — their historical average returns (approximately 2–3% annually for SMB and 4–5% for HML) represent the size and value premiums that CAPM leaves unexplained. If CAPM fully described returns, these portfolios would have zero expected return after adjusting for market beta — but they don't, which is the empirical foundation of the Fama-French model."

- question: "Why does the interpretation of factor premiums — whether they represent compensation for risk or correction of mispricing — matter for whether the premiums will persist in the future?"
  type: short-answer
  answer: "If factor premiums (like the value premium) compensate for genuine systematic risk that investors cannot diversify away, they should persist as long as that risk exists — earning the premium is 'payment' for bearing unavoidable exposure. If instead premiums reflect behavioral mispricing (investors systematically undervaluing certain stocks), they are vulnerable to erosion as informed investors recognize and arbitrage the pattern, capital flows into strategies that exploit it, and prices correct. Risk-based premiums are equilibrium; behavioral premiums are potential arbitrage opportunities that smart money may eventually eliminate."
  explanation: "This debate is central to asset pricing. The risk-based view (Fama-French's preferred interpretation) predicts durable premiums. The behavioral view (e.g., Lakonishok, Shleifer, Vishny) predicts premiums may decay as awareness spreads. Empirically, value and size premiums have weakened since Fama-French published their 1993 paper, which some interpret as consistent with the behavioral story (publication led to trading that arbitraged the mispricing), though risk advocates dispute this."
```

## Explainer

CAPM tells you that a stock's expected return depends on one thing: its beta with the market portfolio. But the CAPM prediction fails systematically in the data — small-cap stocks earn higher returns than their market beta predicts, and stocks with high book-to-market ratios ("value" stocks) outperform growth stocks even after controlling for market risk. These patterns are too persistent and too large to dismiss as noise. From your study of Arbitrage Pricing Theory, you know the theoretical framework that allows multiple factors: APT says that if multiple sources of systematic risk exist that cannot be arbitraged away, expected returns should be linear in exposure to each one. Fama-French turned this theory into an empirical program, asking: which factors actually matter in the data?

The **Fama-French 3-factor model** adds two long-short portfolio returns to the market excess return: **SMB** (Small Minus Big — the return of small-cap stocks minus large-cap stocks) and **HML** (High Minus Low — the return of value stocks minus growth stocks, where value/growth is measured by book-to-market ratio). A stock's expected return is then: E[Rᵢ] = Rf + βᵢ,mkt · (Rm - Rf) + βᵢ,SMB · E[SMB] + βᵢ,HML · E[HML]. Each β is estimated by regressing the stock's excess returns on the three factors. A small-cap value stock will have positive loadings on both SMB and HML, predicting a higher expected return than CAPM alone would assign. The model explains about 90% of cross-sectional return variation — dramatically better than single-factor CAPM's 70%.

The deeper question is *why* these factor premiums exist. Two interpretations compete. The **risk-based view** holds that small and value stocks are riskier in some dimension that CAPM's market beta misses — perhaps they're more distressed, more sensitive to economic downturns, or harder to hold during liquidity crises. Investors who bear this risk earn a premium as compensation. The **behavioral view** holds that size and value premiums reflect mispricing: investors systematically undervalue beaten-down value stocks and overpay for glamour growth stocks, and patient arbitrageurs earn returns by correcting these mispricings. The distinction matters for whether the premiums will persist (if risk-based, they should; if behavioral, smart money may eventually arbitrage them away) and for how to interpret a positive alpha (genuine outperformance, or just unpriced risk exposure?).

Later work extended the model. Fama and French's **5-factor model** adds **RMW** (Robust Minus Weak profitability) and **CMA** (Conservative Minus Aggressive investment), reflecting the empirical finding that profitable firms and firms that invest conservatively earn higher returns. Carhart added **momentum** (WML — Winners Minus Losers), capturing the tendency for recent winners to keep winning over 3–12 month horizons. The proliferation of factors — sometimes called the "factor zoo" — has led to methodological debates about data mining, multiple testing, and whether many discovered factors are spurious. The most theoretically grounded factors (market, size, value, profitability) are the most durable. Your eigenvalue background is relevant here: principal component analysis of asset returns often extracts 3–5 dominant components that map closely onto the leading empirical factors, suggesting these factors capture real, low-dimensional structure in the covariance matrix of returns.
