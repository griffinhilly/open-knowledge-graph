---
id: inflation-unemployment-tradeoff
title: Inflation-Unemployment Tradeoff and Modern Phillips Curve
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: phillips-curve-new-keynesian
  type: hard
- id: wage-setting-equilibrium
  type: soft
builds-toward:
- natural-rate-hypothesis
tags:
- phillips-curve
- inflation-unemployment
- tradeoff
stage: advanced
status: draft
---

# Inflation-Unemployment Tradeoff and Modern Phillips Curve

## Core Idea
The Phillips curve describes the relationship between inflation and unemployment. When unemployment falls below its natural rate, labor markets tighten, wage pressures rise, and inflation accelerates. The stability of this tradeoff depends on how inflation expectations form and respond to policy credibility.

## Questions

```yaml
- question: "A central bank commits to keeping unemployment permanently at 3%, which is below the natural rate of 5%, by running persistently expansionary monetary policy. According to the expectations-augmented Phillips curve, what is the long-run outcome?"
  type: multiple-choice
  options:
    - "Unemployment stays at 3% as long as the central bank maintains its policy stance — the tradeoff is permanent"
    - "Unemployment returns to 5% and inflation is permanently higher than before the policy began"
    - "Unemployment returns to 5% and inflation also returns to its original level, with no lasting effect"
    - "Unemployment stays at 3% but only if inflation is raised above some threshold level"
  answer: 1
  explanation: "The expectations-augmented Phillips curve predicts that the tradeoff is only temporary. Initially, expansionary policy surprises workers and firms, reducing unemployment. But as workers observe higher inflation, they revise expectations upward and demand higher nominal wages. Firms' cost advantages evaporate, employment falls back to the natural rate, and the economy is left with higher inflation but no lasting unemployment reduction. This is the long-run vertical Phillips curve: at the natural rate of unemployment, any inflation rate can be sustained depending on expectations. Option C is wrong — the inflation permanently rises (it does not self-reverse). Option A is the classic mistake Friedman and Phelps refuted."

- question: "What was the core insight that Friedman and Phelps added to the original Phillips curve analysis, explaining why the 1960s' stable tradeoff broke down in the 1970s stagflation?"
  type: multiple-choice
  options:
    - "The Phillips curve relationship depends on the level of the money supply, not the inflation rate, so monetarism can stabilize both inflation and unemployment simultaneously"
    - "The tradeoff is between unexpected inflation and unemployment, not between the level of inflation and the level of unemployment — only surprises can temporarily move unemployment"
    - "The tradeoff only works in downturns; during expansions, inflation and unemployment rise together regardless of policy"
    - "Fiscal policy, not monetary policy, is the correct tool for managing unemployment, so the Phillips curve breakdown reflects a policy instrument error"
  answer: 1
  explanation: "Friedman and Phelps showed that what appeared to be a stable menu of choices (choose any point on the Phillips curve) was actually an incomplete description. Workers and firms adjust their nominal wages and prices based on expected inflation; only unexpected inflation temporarily lowers real wages and boosts employment. Once inflation expectations adjust to match actual inflation, real wages return to equilibrium, unemployment returns to its natural rate, and the short-run curve shifts up. In the 1970s, expansionary policy that had 'worked' in the 1960s stopped working as agents learned to anticipate it — expectations adapted and the curve shifted, producing stagflation."

- question: "The original Phillips curve relationship, as estimated by A.W. Phillips in 1958, was so stable across nearly a century of UK data that it represented a reliable structural law for setting policy."
  type: true-false
  answer: false
  explanation: "False. The original relationship was an empirical regularity in historical data — not a structural law. The Lucas critique (made explicit in 1976) explains why: when policymakers exploit a statistical relationship by changing their behavior, agents in the economy change their behavior in response, and the original relationship breaks down. The Phillips curve is an equilibrium correlation between inflation and unemployment under particular policy regimes and expectation-formation processes. When the US tried to exploit the tradeoff in the 1960s and early 1970s, the relationship shifted — stagflation of the 1970s (high inflation AND high unemployment) violated the original curve entirely. An empirical regularity from a passive observation period cannot survive active exploitation."

- question: "If workers and firms form fully rational expectations and know the central bank's policy rule, the short-run inflation-unemployment tradeoff largely disappears because anticipated policy has no real effects."
  type: true-false
  answer: true
  explanation: "True. The expectations-augmented framework shows that only unexpected inflation temporarily reduces unemployment below the natural rate. If agents have rational expectations and can predict the central bank's actions, they incorporate anticipated inflation into wage and price contracts before the policy takes effect. Real wages are unchanged, employment is unchanged, and the only result is higher actual inflation. This 'policy neutrality' result under full rational expectations is why credibility matters so much in modern central banking: if markets believe the central bank will hit its inflation target, anticipated demand shocks will be pre-corrected and the real side of the economy is less disrupted."

- question: "Why does the stability of the inflation-unemployment tradeoff depend on how inflation expectations are formed? Contrast adaptive and rational expectations in your answer."
  type: short-answer
  answer: "The tradeoff works only when inflation is unexpected. If expectations are adaptive (backward-looking), agents base their predictions on recent inflation, so there is a lag before they catch up to new policy — giving the central bank a window to temporarily lower unemployment. But each round of inflation eventually enters expectations, shifting the short-run curve up. If expectations are rational (forward-looking, incorporating all available information including the policy rule itself), anticipated policy is already embedded in wage and price decisions before the policy takes effect, and no real effect on unemployment occurs. The more forward-looking and accurate the expectations, the shorter and weaker the tradeoff."
  explanation: "This is why central bank credibility is a crucial institutional feature. A credible inflation target anchors expectations near the target even when temporary supply shocks push inflation away. Workers and firms do not extrapolate short-run inflation deviations into long-run wage demands, so wage-price spiral dynamics are suppressed. By contrast, low-credibility central banks face expectations that amplify every inflationary shock, making the tradeoff worse — high inflation with high unemployment — because expectations themselves become destabilizing."
```

## Explainer

From the New Keynesian Phillips Curve, you know that inflation is driven by expected future inflation and the output gap — when the economy operates above potential, firms face rising marginal costs and raise prices. The inflation-unemployment tradeoff translates this output gap logic into labor market terms: when unemployment drops below its natural rate, labor becomes scarce, wages are bid up, firms pass those costs into prices, and inflation rises. The question at the heart of modern macroeconomics is whether this tradeoff is stable enough to exploit — can a central bank permanently buy lower unemployment by accepting higher inflation?

The original **Phillips curve**, estimated by A.W. Phillips in 1958, documented a remarkably stable negative relationship between wage inflation and unemployment in UK data spanning nearly a century. Policymakers in the 1960s interpreted this as a menu of choices: accept 2% unemployment at the cost of 5% inflation, or choose 4% unemployment with 2% inflation. This interpretation proved dangerously incomplete. When governments tried to exploit the tradeoff by running persistently expansionary policy, they discovered that the relationship shifted: the same unemployment rate was now associated with ever-higher inflation. By the 1970s, the US experienced stagflation — high inflation and high unemployment simultaneously — which the original stable Phillips curve could not explain.

The resolution came from **expectations augmentation**, introduced by Milton Friedman and Edmund Phelps. Their insight was that the tradeoff between inflation and unemployment is not between the level of inflation and the level of unemployment, but between *unexpected* inflation and unemployment. When a central bank stimulates the economy, firms see rising demand and hire more workers, temporarily pushing unemployment below its natural rate. But this only works as long as workers and firms are surprised by the higher inflation. Once they adjust their expectations upward — demanding higher nominal wages in anticipation of rising prices — the cost advantage to firms evaporates, employment returns to its natural level, and the economy is left with higher inflation but no lasting reduction in unemployment. The short-run Phillips curve shifts up with each round of inflationary policy.

This means the **short-run tradeoff** is real but temporary, and its slope depends on how quickly expectations adjust. If expectations are **adaptive** (backward-looking, based on recent inflation experience), the tradeoff can be exploited for a while before expectations catch up. If expectations are **rational** (forward-looking, incorporating all available information including knowledge of policy), the tradeoff is much shorter-lived — possibly nonexistent if policy is fully anticipated. Modern central banks take this seriously: by establishing credible inflation targets and communicating policy intentions transparently, they aim to anchor expectations so that temporary supply shocks do not spiral into persistent inflation through a wage-price feedback loop. The stability of the inflation-unemployment tradeoff is therefore not a fixed feature of the economy — it depends on the credibility of the institutions managing monetary policy.
