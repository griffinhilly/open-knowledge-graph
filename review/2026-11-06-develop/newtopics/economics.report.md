# New-topic report: economics

Status: complete. 17 new topics written, 21 proposed edges into existing topics. No existing files were edited.

The economics domain already has about 680 topics, many of them near-duplicates (for example several Hausman-test, NAIRU, and duality topics). Most standard units are covered. The gaps found are mostly units that textbooks treat as their own chapter or section but that appear in this graph only as a sentence inside another topic.

## 1. Syllabi compared against

| Course | Syllabus / text compared against |
|---|---|
| microeconomics | College Board AP Microeconomics Course and Exam Description (Units 1-6); Mankiw, *Principles of Economics* (micro chapters); Varian, *Intermediate Microeconomics* |
| macroeconomics | College Board AP Macroeconomics CED (Units 1-6); Mankiw, *Principles* (macro chapters) and *Macroeconomics* |
| advanced-macroeconomics | Romer, *Advanced Macroeconomics* (growth, RBC, nominal rigidity, consumption, investment, unemployment, monetary policy, deficits) |
| econometrics | Wooldridge, *Introductory Econometrics: A Modern Approach* (Parts 1-3) |
| advanced-microeconomics | Mas-Colell, Whinston and Green, *Microeconomic Theory*; Varian, *Microeconomic Analysis*; standard market-design material (Roth and Sotomayor, *Two-Sided Matching*) |
| financial-economics | Berk and DeMarzo, *Corporate Finance*; Bodie, Kane and Marcus, *Investments* |
| development-economics | Todaro and Smith, *Economic Development*; Ray, *Development Economics* |
| labor-economics | Borjas, *Labor Economics* |
| behavioral-economics | Standard undergraduate behavioral syllabus (heuristics and biases, prospect theory, time inconsistency, social preferences, nudges, experimental methods) |

## 2. New topics

| new id | course | why it is a gap (syllabus unit) | prerequisites |
|---|---|---|---|
| economic-systems-resource-allocation | microeconomics | AP Micro Unit 1, "Resource Allocation and Economic Systems"; Mankiw ch. 1. No economics topic covers traditional / command / market / mixed systems; only history and sociology topics touch capitalism and socialism. | scarcity-and-opportunity-cost (hard), scarcity-choice-production-tradeoff (soft), production-possibilities-frontier (soft) |
| marginal-analysis-cost-benefit | microeconomics | AP Micro Unit 1, "Cost-Benefit Analysis" and "Marginal Analysis"; Mankiw's "rational people think at the margin". Marginal reasoning appears only inside firm and consumer topics; there is no general MB = MC decision-rule topic. | opportunity-cost-concept (hard), scarcity-and-opportunity-cost (soft) |
| tariffs-and-import-quotas | microeconomics | AP Micro Unit 2, "International Trade and Public Policy"; Mankiw ch. 9 "Application: International Trade". Comparative advantage exists, but no topic does the world-price / tariff / quota welfare analysis. | comparative-advantage-and-trade (hard), consumer-surplus-deadweight-loss-policy (hard), market-equilibrium (hard), tax-incidence-and-elasticity (soft) |
| tax-system-design-efficiency-equity | microeconomics | Mankiw ch. 12 "The Design of the Tax System". Progressive taxes appear only inside automatic stabilizers. No topic covers average vs marginal rates, lump-sum taxes, benefits vs ability-to-pay principles, or vertical and horizontal equity. | tax-incidence-and-elasticity (hard), consumer-surplus-deadweight-loss-policy (hard), price-elasticity-of-demand (soft), tax-brackets-marginal-rates (soft, practical-life-skills) |
| expected-utility-and-risk-aversion | microeconomics | Varian ch. 12 "Uncertainty"; MWG ch. 6 "Choice Under Uncertainty". Behavioral and finance topics mention expected utility, and philosophy has expected-value-decision-making, but no economics topic teaches EU, concavity, certainty equivalent, or risk premium. | utility-function-representation (hard), expected-value (hard, mathematics), marginal-utility-diminishing-marginal (soft) |
| bank-runs-and-deposit-insurance | macroeconomics | Mankiw *Macroeconomics*, chapter on the financial system and financial crises; AP Macro Unit 4 banking. Only one-line mentions exist (banking-services-and-development, financial-accelerator-mechanism); no topic covers runs, Diamond-Dybvig, deposit insurance, or the lender of last resort. | money-supply-and-money-creation (hard), central-banking-and-the-fed (soft), nash-equilibrium-microeconomics (soft) |
| hall-random-walk-consumption | advanced-macroeconomics | Romer, Consumption chapter, section on the random-walk hypothesis and its tests. consumption-smoothing-intertemporal covers the PIH but not Hall's martingale result or excess sensitivity. | euler-equation-consumption (hard), consumption-smoothing-intertemporal (hard), rational-expectations-macro (soft), martingales-introduction (soft, mathematics) |
| precautionary-saving | advanced-macroeconomics | Romer, Consumption chapter, section on precautionary saving. No topic covers prudence (u‴ > 0), certainty equivalence, or buffer-stock saving. | euler-equation-consumption (hard), expected-utility-and-risk-aversion (hard, new), hall-random-walk-consumption (soft, new), consumption-smoothing-intertemporal (soft) |
| cointegration-and-error-correction | econometrics | Wooldridge ch. 18 (cointegration and error correction models). Cointegration is named only inside stationarity topics as a diagnostic; no topic teaches Engle-Granger testing or the ECM. | stationarity-and-unit-roots (hard), unit-roots-stationarity (soft), simple-linear-regression-estimation (soft), vector-autoregression-models (soft) |
| simultaneous-equations-models | econometrics | Wooldridge ch. 16 "Simultaneous Equations Models". Simultaneity appears as a source of endogeneity and 2SLS exists, but no topic covers structural systems or the order and rank conditions for identification. | endogeneity (hard), instrumental-variables (hard), two-stage-least-squares (hard), reduced-form-equations (soft) |
| tobit-censored-regression | econometrics | Wooldridge ch. 17, Tobit model for corner solution responses (and censored regression). Survival analysis covers censoring of durations only; no Tobit topic exists. | maximum-likelihood-econometrics (hard), logit-probit-models (hard), multiple-regression-model (soft), nonlinear-models-interpretation (soft) |
| heckman-sample-selection-correction | econometrics | Wooldridge ch. 17, sample selection corrections. selection-bias-econometrics names Heckman in one sentence; labor topics invoke the correction without a topic that teaches it. | selection-bias-econometrics (hard), logit-probit-models (hard), maximum-likelihood-econometrics (soft), tobit-censored-regression (soft, new) |
| finite-distributed-lag-models | econometrics | Wooldridge ch. 10, static and finite distributed lag models (impact propensity, long-run propensity). Distributed lags appear only in serial-correlation tests. | time-series-basics-econometrics (hard), multiple-regression-model (hard), multicollinearity (soft), serial-correlation (soft) |
| capital-structure-modigliani-miller | financial-economics | Berk and DeMarzo, capital structure chapters (MM I and II, taxes, distress costs, tradeoff and pecking order). Only dividend irrelevance is covered (dividend-policy-and-valuation); WACC exists without the leverage theory behind it. | weighted-average-cost-of-capital (hard), cost-of-equity-capm (soft), net-present-value (soft) |
| two-sided-matching-deferred-acceptance | advanced-microeconomics | Market design / matching (Gale-Shapley 1962; Roth and Sotomayor). Grep for stable matching, Gale-Shapley, and deferred acceptance across economics, mathematics, and computer-science found nothing. | pareto-efficiency-and-optimality (soft), core-of-an-economy (soft), mechanism-design-basics (soft), incentive-compatibility (soft) |
| samuelson-condition-public-goods | advanced-microeconomics | MWG ch. 11 public goods (Samuelson condition, voluntary provision, Lindahl equilibrium). public-goods-and-common-resources covers classification and free riding but not the efficiency condition or Lindahl prices. | public-goods-and-common-resources (hard), pareto-efficiency-and-optimality (hard), marginal-rate-substitution-indifference (soft), nash-equilibrium-microeconomics (soft) |
| harrod-domar-growth-model | development-economics | Todaro and Smith ch. 3, classic theories (linear stages, Harrod-Domar, financing gap). No topic covers Harrod-Domar; foreign-aid-effectiveness and savings-constraints-development rely on its logic. | savings-investment-identity (hard), production-function-macroeconomics (soft) |

All 17 ids were checked with Glob as unused. All prerequisite and builds-toward ids were checked with Glob as existing. Stages are at or above the stage of each topic's hard prerequisites.

## Proposed edges into existing topics

```
ADD	economic-systems-resource-allocation	supply-and-demand-basics	soft	Price-guided allocation is the setting supply and demand formalizes
ADD	marginal-analysis-cost-benefit	profit-maximization-output-level	soft	MR = MC is the firm's case of the general MB = MC rule
ADD	marginal-analysis-cost-benefit	marginal-utility-and-consumer-choice	soft	Consumer choice applies the marginal rule per dollar spent
ADD	marginal-analysis-cost-benefit	externalities-and-market-failure	soft	Social optimum is defined by marginal social benefit = marginal social cost
ADD	marginal-analysis-cost-benefit	sunk-cost-fallacy	soft	The fallacy is defined against the rule that sunk costs drop out of marginal comparisons
ADD	tariffs-and-import-quotas	trade-and-development	soft	Protection and infant-industry debates use the tariff welfare analysis
ADD	tax-system-design-efficiency-equity	social-welfare-optimization	soft	Optimal taxation formalizes the efficiency-equity tradeoff
ADD	tax-system-design-efficiency-equity	automatic-stabilizers-fiscal-tools	soft	Stabilizer effect of progressive taxes relies on average vs marginal rates
ADD	expected-utility-and-risk-aversion	risk-and-return-tradeoff	soft	Risk premia rest on investor risk aversion
ADD	expected-utility-and-risk-aversion	insurance-markets-and-selection	hard	Insurance demand and screening models assume expected-utility, risk-averse buyers
ADD	expected-utility-and-risk-aversion	moral-hazard-insurance	soft	Insurance contracting assumes risk-averse insured parties
ADD	expected-utility-and-risk-aversion	prospect-theory-behavioral	hard	Prospect theory is defined by its departures from expected utility
ADD	bank-runs-and-deposit-insurance	financial-frictions-amplification	soft	Runs and fire sales are a core amplification channel
ADD	bank-runs-and-deposit-insurance	financial-system-interconnectedness	soft	Contagion between banks extends the single-bank run
ADD	heckman-sample-selection-correction	lifecycle-labor-supply	soft	Topic invokes Heckman's correction for women's wage selection
ADD	heckman-sample-selection-correction	occupational-choice	soft	Topic motivates Heckman-style corrections for self-selection
ADD	finite-distributed-lag-models	lagged-dependent-variable-regression	soft	Models with lagged y extend distributed lag models
ADD	capital-structure-modigliani-miller	dividend-policy-and-valuation	soft	Dividend irrelevance is the payout-policy version of the MM argument
ADD	samuelson-condition-public-goods	vcg-auction-mechanism	soft	Clarke-Groves mechanisms address the preference-revelation problem in public-good provision
ADD	harrod-domar-growth-model	savings-constraints-development	soft	Saving-led capital accumulation argument originates in Harrod-Domar
ADD	harrod-domar-growth-model	foreign-aid-effectiveness	soft	The financing-gap model behind aid targets is Harrod-Domar
```

Prerequisite chains for these edges were checked for cycles by reading the prerequisite lists of the target topics; none of the targets is an ancestor of the new topic that points to it.

## 4. Gaps considered and rejected

| Candidate | Already covered by |
|---|---|
| Coase theorem, Pigouvian taxes, cap-and-trade | externalities-and-market-failure |
| Subsidies and their deadweight loss | consumer-surplus-deadweight-loss-policy |
| Market demand as horizontal sum | demand-curve-derivation, demand-curve-individual-consumer |
| Antitrust and merger policy | monopoly-sources-barriers, monopoly-output-and-pricing, cartel-and-collusion |
| Inequality measurement (Lorenz, Gini) | income-inequality-measurement |
| Network externalities | monopoly-market-power-barriers (mentioned); not a separate unit in AP Micro or Mankiw, so not a clear gap |
| Public choice, median voter | social-sciences spatial-models-political-ideology; not a unit in the economics comparators |
| Keynesian cross, spending multiplier | aggregate-demand-expenditure-approach, fiscal-multiplier, demand-shocks-and-multipliers |
| Fractional-reserve banking, reserve requirements | money-supply-and-money-creation, money-multiplier-dynamics, monetary-base-and-money-creation |
| Costs of inflation (shoe-leather, menu costs, inflation tax, seigniorage) | inflation-and-price-level, hyperinflation-and-money-dynamics |
| Money market | liquidity-preference-theory-keynes |
| Real exchange rate, overshooting | exchange-rates-macroeconomics, exchange-rate-dynamics |
| Policy trilemma | open-economy-macroeconomics, exchange-rate-regimes-and-monetary-policy |
| Currency crises, sudden stops | capital-flows-and-financial-account (partial); not a separate unit in the comparators |
| Lucas critique | rational-expectations-macro, dsge-models |
| Inflation targeting | central-bank-credibility-expectations, inflation-dynamics-and-persistence |
| Efficiency wages | wage-determination, unemployment-theory, labor-market-equilibrium |
| Nash bargaining over wages | wage-setting-equilibrium, search-and-matching-models |
| Hotelling linear city | product-differentiation |
| Spurious regression | time-series-basics-econometrics, stationarity-and-unit-roots |
| Granger causality | vector-autoregression-models |
| Linear probability model | logit-probit-models |
| Log functional forms | coefficient-interpretation-regression |
| HAC / Newey-West standard errors | serial-correlation, generalized-least-squares |
| Internal rate of return | net-present-value (NPV vs IRR), yield-to-maturity |
| Dividend irrelevance | dividend-policy-and-valuation |
| Harris-Todaro migration | migration-and-development, labor-migration-development |
| Import substitution vs export-led growth | trade-and-development, learning-by-doing-and-development, industrial-catch-up-growth |
| Poverty lines and headcounts | multidimensional-poverty-measurement, development-definition-and-measurement |
| Labor economics (Borjas chapters) | All covered: labor-supply-theory, labor-demand-theory, labor-market-equilibrium, compensating-wage-differentials, human-capital-theory, returns-to-education, immigration-economics, discrimination-economics, labor-unions, incentive-design-personnel-economics, unemployment-theory, search-and-matching-models |
| Behavioral economics syllabus | All covered: heuristics-and-biases, prospect-theory-behavioral, loss-aversion, endowment-effect, mental-accounting, present-bias, hyperbolic-discounting, social-preferences, nudge-theory, experimental-economics-methods, and others |
