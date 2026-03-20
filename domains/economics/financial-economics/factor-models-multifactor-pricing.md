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
status: draft
---

# Factor Models and Multifactor Pricing (Fama-French)

## Core Idea
Multifactor models extend CAPM by adding risk factors beyond market return. The Fama-French 3-factor model adds size (SMB) and value (HML) factors; newer versions include profitability and investment factors. Each factor premium compensates systematic exposure; these models explain cross-sectional return variation better than single-factor CAPM.

## How It's Best Learned
Regress stock returns on Fama-French factors. Compare model R² and explanatory power to single-factor CAPM. Interpret factor exposures as systematic risks.

## Explainer

CAPM tells you that a stock's expected return depends on one thing: its beta with the market portfolio. But the CAPM prediction fails systematically in the data — small-cap stocks earn higher returns than their market beta predicts, and stocks with high book-to-market ratios ("value" stocks) outperform growth stocks even after controlling for market risk. These patterns are too persistent and too large to dismiss as noise. From your study of Arbitrage Pricing Theory, you know the theoretical framework that allows multiple factors: APT says that if multiple sources of systematic risk exist that cannot be arbitraged away, expected returns should be linear in exposure to each one. Fama-French turned this theory into an empirical program, asking: which factors actually matter in the data?

The **Fama-French 3-factor model** adds two long-short portfolio returns to the market excess return: **SMB** (Small Minus Big — the return of small-cap stocks minus large-cap stocks) and **HML** (High Minus Low — the return of value stocks minus growth stocks, where value/growth is measured by book-to-market ratio). A stock's expected return is then: E[Rᵢ] = Rf + βᵢ,mkt · (Rm - Rf) + βᵢ,SMB · E[SMB] + βᵢ,HML · E[HML]. Each β is estimated by regressing the stock's excess returns on the three factors. A small-cap value stock will have positive loadings on both SMB and HML, predicting a higher expected return than CAPM alone would assign. The model explains about 90% of cross-sectional return variation — dramatically better than single-factor CAPM's 70%.

The deeper question is *why* these factor premiums exist. Two interpretations compete. The **risk-based view** holds that small and value stocks are riskier in some dimension that CAPM's market beta misses — perhaps they're more distressed, more sensitive to economic downturns, or harder to hold during liquidity crises. Investors who bear this risk earn a premium as compensation. The **behavioral view** holds that size and value premiums reflect mispricing: investors systematically undervalue beaten-down value stocks and overpay for glamour growth stocks, and patient arbitrageurs earn returns by correcting these mispricings. The distinction matters for whether the premiums will persist (if risk-based, they should; if behavioral, smart money may eventually arbitrage them away) and for how to interpret a positive alpha (genuine outperformance, or just unpriced risk exposure?).

Later work extended the model. Fama and French's **5-factor model** adds **RMW** (Robust Minus Weak profitability) and **CMA** (Conservative Minus Aggressive investment), reflecting the empirical finding that profitable firms and firms that invest conservatively earn higher returns. Carhart added **momentum** (WML — Winners Minus Losers), capturing the tendency for recent winners to keep winning over 3–12 month horizons. The proliferation of factors — sometimes called the "factor zoo" — has led to methodological debates about data mining, multiple testing, and whether many discovered factors are spurious. The most theoretically grounded factors (market, size, value, profitability) are the most durable. Your eigenvalue background is relevant here: principal component analysis of asset returns often extracts 3–5 dominant components that map closely onto the leading empirical factors, suggesting these factors capture real, low-dimensional structure in the covariance matrix of returns.
