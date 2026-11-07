---
id: capital-structure-modigliani-miller
title: Capital Structure and the Modigliani-Miller Theorems
domain: economics
course: financial-economics
prerequisites:
- id: weighted-average-cost-of-capital
  type: hard
- id: cost-of-equity-capm
  type: soft
- id: net-present-value
  type: soft
builds-toward:
- dividend-policy-and-valuation
tags:
- corporate finance
- capital structure
- leverage
- Modigliani-Miller
- interest tax shield
- financial distress
- tradeoff theory
stage: advanced
status: validated
---

# Capital Structure and the Modigliani-Miller Theorems

## Core Idea
Capital structure is a firm's mix of debt and equity financing. Franco Modigliani and Merton Miller showed in 1958 that in perfect capital markets, with no taxes, transaction costs, or bankruptcy costs, a firm's total value does not depend on that mix (Proposition I). Debt is cheaper than equity, but adding debt makes equity riskier, so the cost of equity rises with leverage, r_E = r_U + (D/E)(r_U − r_D), and the weighted average cost of capital stays constant (Proposition II). Real-world capital structure choices therefore matter only because of the market imperfections the theorems assume away, chiefly the tax deductibility of interest and the costs of financial distress.

## How It's Best Learned
Work one firm through two financing plans, all equity and half debt, and compute the cash flows to investors in good and bad years. Show that an investor can recreate either plan's payoffs by borrowing or lending on personal account, which is the "homemade leverage" argument. Then add a corporate tax and compute the interest tax shield, so the departure from irrelevance is concrete.

## Common Misconceptions
- Because debt has a lower required return than equity, replacing equity with debt lowers a firm's cost of capital. (Without taxes, the cost of equity rises exactly enough to keep the weighted average cost of capital unchanged.)
- Leverage raises expected earnings per share, so it must raise the share price. (Leverage also raises the risk of those earnings, and in perfect markets the higher required return offsets the higher expected return.)
- The Modigliani-Miller theorems claim capital structure never matters in practice. (They state conditions under which it does not matter, which directs attention to the frictions, such as taxes and distress costs, that make it matter.)

## Questions

```yaml
- question: "An all-equity firm has a cost of capital r_U = 10%. It borrows half its value at r_D = 5% and uses the proceeds to buy back shares, so D/E = 1. With no taxes, what is the new cost of equity?"
  type: multiple-choice
  options: ["10%", "12.5%", "15%", "20%"]
  answer: 2
  explanation: "By MM Proposition II, r_E = r_U + (D/E)(r_U − r_D) = 10% + 1 × (10% − 5%) = 15%. The WACC is 0.5 × 15% + 0.5 × 5% = 10%, unchanged from the all-equity firm."
- question: "Under the Modigliani-Miller assumptions with no taxes, two firms with identical operating cash flows but different debt levels must have the same total market value."
  type: true-false
  answer: true
  explanation: "If the values differed, investors could buy the cheaper firm's securities and use personal borrowing or lending to replicate the other firm's payoffs, earning an arbitrage profit. Competition removes the gap, so total values are equal."
- question: "When interest payments are tax-deductible at corporate rate τ_c and the firm keeps permanent debt D, the 1963 Modigliani-Miller result states that firm value equals:"
  type: multiple-choice
  options: ["V_U", "V_U + τ_c D", "V_U − τ_c D", "V_U × (1 − τ_c)"]
  answer: 1
  explanation: "Each year the firm saves τ_c × r_D × D in taxes. Discounted at r_D as a perpetuity, the present value of these savings is τ_c D, so levered firm value is the unlevered value plus the value of the interest tax shield."
- question: "If debt creates a tax shield, why do most firms not finance themselves almost entirely with debt?"
  type: short-answer
  answer: "More debt raises the probability and expected cost of financial distress, including legal costs of bankruptcy, lost customers and suppliers, and distorted investment incentives. The tradeoff theory holds that firms choose leverage where the marginal tax benefit of debt equals the marginal expected cost of distress."
  explanation: "Agency costs between shareholders and creditors and the information problems behind pecking-order behavior also limit debt in practice."
```

## Explainer
From the weighted average cost of capital you know that a firm's financing mix appears in its discount rate. A natural question follows: can a firm raise its value just by changing that mix? Debt usually has a lower required return than equity, so it seems swapping equity for debt should lower the WACC and raise value.

Modigliani and Miller showed in 1958 that in perfect capital markets this reasoning fails. **Proposition I** says firm value depends only on the cash flows its assets generate, not on how those cash flows are divided between creditors and shareholders. The argument uses arbitrage. If a levered firm were worth more than an identical unlevered one, an investor could buy shares of the unlevered firm, borrow personally in the same proportion, and receive the same payoffs as a shareholder of the levered firm at lower cost. This **homemade leverage** keeps the two values equal.

**Proposition II** explains why cheap debt does not help. Debt holders have a prior claim, so adding debt shifts risk onto shareholders, who then demand a higher return. With no taxes, r_E = r_U + (D/E)(r_U − r_D). Take a firm with r_U = 10% that borrows half its value at 5%. The cost of equity rises to 15%, and the WACC stays at 0.5 × 15% + 0.5 × 5% = 10%.

The theorems matter because their assumptions point to the real reasons financing matters. The first is **taxes**. Interest is deductible from corporate income in many tax systems, so debt reduces taxes. In their 1963 paper, Modigliani and Miller showed that with permanent debt D and corporate tax rate τ_c, firm value becomes V_U + τ_c D. The second is **financial distress**. Heavy debt raises the risk of bankruptcy, with legal costs, lost customers, and poor investment decisions under pressure. The **tradeoff theory** says firms choose debt where the marginal tax benefit equals the marginal expected distress cost. The **pecking order theory** of Stewart Myers and Nicolas Majluf (1984) adds that managers know more than outside investors, so firms prefer internal funds, then debt, and issue equity last.

Modigliani received the Nobel Memorial Prize in Economic Sciences in 1985 and Miller in 1990, both partly for this work. The same no-arbitrage logic underlies the dividend irrelevance result.
