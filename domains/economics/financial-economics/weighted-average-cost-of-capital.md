---
id: weighted-average-cost-of-capital
title: Weighted Average Cost of Capital (WACC)
domain: economics
course: financial-economics
prerequisites:
- id: cost-of-equity-capm
  type: hard
builds-toward:
- free-cash-flow-dcf-valuation
tags:
- corporate-finance
- discount-rate
- capital-structure
stage: advanced
status: draft
---

# Weighted Average Cost of Capital (WACC)

## Core Idea
WACC = (E/V)r_e + (D/V)r_d(1−T_c), where E and D are equity and debt market values, V = E + D, r_d is cost of debt, and T_c is tax rate. WACC is the appropriate discount rate for unlevered free cash flows in enterprise valuation.

## How It's Best Learned
Calculate WACC for a levered firm. Observe how increasing debt (while keeping business risk constant) initially lowers WACC due to tax deductibility of interest, but eventually raises it as financial distress risk increases.

## Questions

```yaml
- question: "A firm is financed 60% by equity (cost of equity = 12%) and 40% by debt (pretax cost of debt = 6%), with a corporate tax rate of 25%. What is its WACC?"
  type: multiple-choice
  options:
    - "9.0%"
    - "9.6%"
    - "10.2%"
    - "8.4%"
  answer: 0
  explanation: "WACC = (0.60)(0.12) + (0.40)(0.06)(1 − 0.25) = 0.072 + (0.40)(0.045) = 0.072 + 0.018 = 0.090 = 9.0%. The key step is applying the (1−T_c) tax shield to the debt cost. Option B (9.6%) is the common error of ignoring the tax shield: (0.60)(0.12) + (0.40)(0.06) = 0.072 + 0.024 = 0.096. The tax deductibility of interest is not optional — it is the reason debt is cheaper than equity on an after-tax basis."

- question: "Why is the debt cost in the WACC formula multiplied by (1 − T_c), but the equity cost is not?"
  type: multiple-choice
  options:
    - "Debt is riskier than equity, so it must be discounted by the tax factor"
    - "Interest payments on debt are tax-deductible, so the government effectively subsidizes part of the debt cost; equity dividends carry no such shield"
    - "Equity is already expressed as an after-tax return, while debt is expressed pretax"
    - "The formula convention is arbitrary — any consistent approach would give the same WACC"
  answer: 1
  explanation: "Interest expense reduces taxable income: a $100 interest payment at a 25% tax rate saves $25 in taxes, making the net cost to the firm only $75 (= $100 × (1 − 0.25)). Equity payouts (dividends, retained earnings) come from after-tax income — there is no analogous deduction. This asymmetry is real and significant: it gives debt an intrinsic cost advantage, which is why WACC falls as a firm initially levers up. The tax shield is not a convention — it reflects the actual cash cost of each financing source."

- question: "WACC is the appropriate discount rate to apply to a firm's levered equity cash flows (i.e., cash flows after interest and debt repayment) in a DCF model."
  type: true-false
  answer: false
  explanation: "WACC discounts *unlevered* (enterprise) free cash flows — operating cash flows available to all capital providers before any financing payments. Applying WACC to equity cash flows would double-count the tax shield (once in the rate, once by subtracting interest from cash flows). To value equity directly, you would use the levered cost of equity r_e as the discount rate on cash flows after debt service. WACC is specifically designed for the enterprise value approach, where financing is embedded in the rate rather than the cash flows."

- question: "As a firm takes on moderate amounts of debt (from an all-equity capital structure), its WACC initially falls because the after-tax cost of debt is lower than the cost of equity."
  type: true-false
  answer: true
  explanation: "This is the interest tax shield effect. Debt is cheaper than equity after tax (no double taxation of interest), so replacing equity with debt at first reduces the blended cost of capital. WACC falls as leverage increases — but only up to a point. At higher leverage, financial distress risk raises both the cost of equity (more volatile equity claims) and the effective cost of debt (higher default spreads), and WACC eventually rises. The optimal capital structure trades off tax benefits against distress costs."

- question: "Explain why using WACC as the discount rate in an enterprise DCF model correctly captures the value of the interest tax shield, even though the projected cash flows themselves are calculated before any interest payments."
  type: short-answer
  answer: "WACC uses the after-tax cost of debt r_d(1−T_c), which is lower than the pretax cost. This lower rate increases the present value of the discounted cash flows relative to discounting at the unlevered cost of capital. The difference in present values — the extra value from using the lower WACC — exactly equals (in the Miles-Ezzell and similar frameworks) the present value of the interest tax shield. By embedding the tax benefit in the discount rate, WACC allows the analyst to project simple, unleveraged operating cash flows and still arrive at the correct enterprise value for a leveraged firm."
  explanation: "This is the elegance of the WACC approach: you never explicitly model debt tax shields in the cash flows, yet the valuation implicitly includes them through the lower discount rate. The alternative (APV: Adjusted Present Value) makes this explicit — value the unlevered firm, then add the PV of tax shields separately. Both approaches should give the same answer under consistent assumptions. WACC's convenience is that it collapses two steps into one, but it requires a stable capital structure assumption."
```

## Explainer

From CAPM and the cost of equity, you know how to price a firm's equity: investors require a return equal to the risk-free rate plus beta times the market premium. But most firms are financed with a mix of equity and debt. When you discount a firm's future cash flows to value the whole enterprise, you need a discount rate that reflects the blended cost of *all* the capital the firm uses — not just equity. **WACC** is that blended rate: a weighted average of equity and debt costs, with weights proportional to how much of each financing source the firm uses at market value.

The formula WACC = (E/V)r_e + (D/V)r_d(1-T_c) contains a crucial asymmetry: the debt cost is multiplied by (1-T_c), the after-tax factor. This is because interest payments on debt are tax-deductible — if a firm pays $100 in interest and faces a 30% corporate tax rate, the government effectively subsidizes $30 of that interest, so the net cost to the firm is only $70. Equity dividends and retained earnings carry no such tax shield: they are paid from after-tax income. This **interest tax shield** makes debt an intrinsically cheaper source of capital, all else equal, which is why WACC falls as a firm initially takes on debt. The equity cost r_e comes from CAPM applied to the firm's levered equity beta; the debt cost r_d is typically the yield on the firm's bonds or bank debt, adjusted for default risk.

The practical use of WACC is as the discount rate in **enterprise DCF valuation**. You project the firm's free cash flows — operating cash flows available to all capital providers before any financing payments — and discount them at WACC. This approach is elegant because it separates the operating decision (what cash flows the business generates) from the financing decision (how those cash flows are split between debt and equity holders). WACC embeds the financing benefit of the tax shield in the discount rate itself, so you can value an unlevered free cash flow stream correctly for a levered firm just by discounting at WACC rather than the unlevered cost of capital.

The complication is that WACC is not stable. It depends on the capital structure weights E/V and D/V, which change as the firm's equity value changes. Using a constant WACC implicitly assumes the firm maintains a fixed debt-to-value ratio — not a fixed dollar amount of debt. It also assumes the firm's systematic risk (and thus the equity discount rate) is stable. In practice, WACC is highly sensitive to the equity beta estimate, the assumed market risk premium, and the target capital structure. Analysts typically compute a **WACC range** (e.g., 8%–12%) reflecting uncertainty across these inputs, and present a sensitivity table showing implied enterprise value across the WACC range. A 1-2 percentage point change in WACC can shift a DCF valuation by 30-50%, which is why the assumptions behind WACC deserve as much scrutiny as the cash flow projections themselves.
