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

## Explainer

From CAPM and the cost of equity, you know how to price a firm's equity: investors require a return equal to the risk-free rate plus beta times the market premium. But most firms are financed with a mix of equity and debt. When you discount a firm's future cash flows to value the whole enterprise, you need a discount rate that reflects the blended cost of *all* the capital the firm uses — not just equity. **WACC** is that blended rate: a weighted average of equity and debt costs, with weights proportional to how much of each financing source the firm uses at market value.

The formula WACC = (E/V)r_e + (D/V)r_d(1-T_c) contains a crucial asymmetry: the debt cost is multiplied by (1-T_c), the after-tax factor. This is because interest payments on debt are tax-deductible — if a firm pays $100 in interest and faces a 30% corporate tax rate, the government effectively subsidizes $30 of that interest, so the net cost to the firm is only $70. Equity dividends and retained earnings carry no such tax shield: they are paid from after-tax income. This **interest tax shield** makes debt an intrinsically cheaper source of capital, all else equal, which is why WACC falls as a firm initially takes on debt. The equity cost r_e comes from CAPM applied to the firm's levered equity beta; the debt cost r_d is typically the yield on the firm's bonds or bank debt, adjusted for default risk.

The practical use of WACC is as the discount rate in **enterprise DCF valuation**. You project the firm's free cash flows — operating cash flows available to all capital providers before any financing payments — and discount them at WACC. This approach is elegant because it separates the operating decision (what cash flows the business generates) from the financing decision (how those cash flows are split between debt and equity holders). WACC embeds the financing benefit of the tax shield in the discount rate itself, so you can value an unlevered free cash flow stream correctly for a levered firm just by discounting at WACC rather than the unlevered cost of capital.

The complication is that WACC is not stable. It depends on the capital structure weights E/V and D/V, which change as the firm's equity value changes. Using a constant WACC implicitly assumes the firm maintains a fixed debt-to-value ratio — not a fixed dollar amount of debt. It also assumes the firm's systematic risk (and thus the equity discount rate) is stable. In practice, WACC is highly sensitive to the equity beta estimate, the assumed market risk premium, and the target capital structure. Analysts typically compute a **WACC range** (e.g., 8%–12%) reflecting uncertainty across these inputs, and present a sensitivity table showing implied enterprise value across the WACC range. A 1-2 percentage point change in WACC can shift a DCF valuation by 30-50%, which is why the assumptions behind WACC deserve as much scrutiny as the cash flow projections themselves.
