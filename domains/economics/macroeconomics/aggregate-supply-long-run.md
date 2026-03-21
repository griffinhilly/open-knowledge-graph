---
id: aggregate-supply-long-run
title: Long-Run Aggregate Supply and Potential Output
domain: economics
course: macroeconomics
prerequisites:
- id: aggregate-supply-short-run
  type: hard
- id: types-of-unemployment
  type: soft
builds-toward:
- as-ad-model
- economic-growth-theory
tags:
- LRAS
- potential-output
- full-employment
- long-run
- self-correction
stage: formal-systems
status: validated
---

# Long-Run Aggregate Supply and Potential Output

## Core Idea
The long-run aggregate supply (LRAS) curve is vertical at the economy's potential output — the level of real GDP consistent with the natural rate of unemployment when all prices are fully flexible. In the long run, output is determined by real factors (capital, labor, technology), not by the price level. If actual GDP exceeds potential (inflationary gap), wages and prices rise until the economy returns to LRAS. If GDP falls short (recessionary gap), wages and prices fall — though this self-correction can be slow and painful.

## How It's Best Learned
Use the AS-AD diagram to trace the self-correction mechanism: start from an inflationary gap, then show how rising wages shift SRAS left over time until equilibrium is restored at LRAS. Ask: why might this take years?

## Common Misconceptions
- The LRAS is vertical because all wages and prices are flexible in the long run, not because supply is inelastic.
- Potential output is not the maximum possible output — it is the sustainable full-employment level.
- Keynesians and classicals disagree on how fast the self-correction operates, not on the long-run result.

## Questions

```yaml
- question: "A positive demand shock temporarily pushes GDP above potential. What happens in the long run if no policy intervention occurs?"
  type: multiple-choice
  options:
    - "GDP stays above potential permanently because the new demand level supports it"
    - "The SRAS shifts leftward as wages rise, returning GDP to potential at a higher price level"
    - "The LRAS shifts rightward to accommodate the higher level of output"
    - "The SRAS shifts rightward as firms expand capacity, locking in the higher GDP"
  answer: 1
  explanation: "When GDP exceeds potential, labor markets are tight: workers push for higher wages and firms raise prices. Rising wages increase production costs, shifting SRAS leftward. This continues until the economy returns to the LRAS at potential output — but at a higher price level than before the shock. The real output gain is temporary; the only permanent effect is inflation. Option C is a key misconception: the LRAS doesn't shift to meet actual output; actual output is pulled back to LRAS."

- question: "What ultimately determines the level of potential output (the position of the LRAS curve)?"
  type: multiple-choice
  options:
    - "The price level — higher prices incentivize more production"
    - "Aggregate demand — more spending shifts LRAS rightward over time"
    - "Real supply-side factors: the capital stock, labor force size and skills, and technology"
    - "The natural rate of interest set by the central bank"
  answer: 2
  explanation: "The LRAS is vertical because the price level does not affect real output in the long run. What determines where the LRAS sits are the real factors of production: how much physical capital exists, how large and skilled the workforce is, and how productive technology is. A higher price level doesn't give workers better tools or more training — it just raises all nominal prices together. This is why the LRAS is about the supply side of the economy, not about nominal variables like prices or interest rates."

- question: "An economy at potential output has zero unemployment."
  type: true-false
  answer: false
  explanation: "Potential output corresponds to the natural rate of unemployment, which is greater than zero. Even at potential, frictional unemployment (people between jobs) and structural unemployment (skills mismatch) exist. Cyclical unemployment — caused by insufficient demand — is zero at potential, but total unemployment is not. Treating 'potential output' as 'maximum possible output with everyone employed' is a common error; it is better understood as 'sustainable full-employment output consistent with stable inflation.'"

- question: "The self-correction mechanism that eliminates a recessionary gap (GDP below potential) tends to operate more slowly than the correction of an inflationary gap (GDP above potential)."
  type: true-false
  answer: true
  explanation: "When GDP exceeds potential, tight labor markets push wages upward relatively quickly — workers and unions press for raises, and firms competing for scarce labor bid wages up. But when GDP is below potential and unemployment is high, wages are downwardly rigid: workers resist nominal pay cuts, employers worry about morale and productivity, and wage floors (including minimum wage laws) create barriers. This asymmetry — wages rise faster than they fall — means the self-correction of recessions is slow and potentially incomplete without policy intervention."

- question: "Why might a Keynesian economist argue for active fiscal or monetary policy to address a recession rather than waiting for the self-correction mechanism to work?"
  type: short-answer
  answer: "Because the self-correction of a recessionary gap relies on wages and prices falling, but wages are downwardly rigid — workers resist nominal cuts and contracts prevent rapid adjustment. This means the return to potential output could take years or even decades, during which unemployment remains high, human capital erodes, and long-term output potential is damaged. The social costs of waiting (sustained unemployment, poverty, lost skills) may far exceed the costs of intervention. As Keynes famously put it, 'in the long run, we are all dead.'"
  explanation: "This is the central policy debate of macroeconomics. Classical economists trust the self-correction mechanism and worry about government intervention creating distortions. Keynesians emphasize the slow and painful nature of the downward adjustment, especially in deep recessions like the Great Depression. Both schools agree the economy eventually returns to potential — the disagreement is about how long it takes and what the costs of waiting are."
```

## Explainer

You already understand the short-run aggregate supply (SRAS) curve: it slopes upward because in the short run, some prices and wages are sticky, so higher price levels can temporarily boost output. The **long-run aggregate supply (LRAS)** curve is what happens when all those stickiness frictions have worked themselves out — when workers renegotiate wage contracts, firms adjust prices, and the economy arrives at its new steady state. At that point, the price level does not affect output. The LRAS is vertical.

Why vertical? In the long run, the economy's output is determined entirely by real factors: the stock of capital, the size and skills of the labor force, and the level of technology. These are the supply-side fundamentals. A higher price level does not give workers more machines or better skills — it just means all nominal prices are higher together. Output pins at **potential output**: the level of real GDP consistent with the **natural rate of unemployment**, where frictional and structural unemployment exist but there is no cyclical unemployment. This is not maximum possible output — it is sustainable full-employment output.

The self-correction mechanism explains how the economy returns to LRAS after shocks. Suppose a positive demand shock (say, a burst of government spending) pushes actual GDP above potential — an **inflationary gap**. The economy is operating beyond its sustainable capacity: workers are overtime, and businesses are operating at above-normal intensity. With labor markets tight, workers push for higher wages, and firms raise prices. As wages and prices rise, the SRAS curve shifts leftward (higher input costs reduce short-run supply). This process continues until the SRAS has shifted left enough that the new equilibrium occurs right on the LRAS — at potential output but at a higher price level. The demand shock has been neutralized in real terms but has produced permanent inflation.

The symmetric case is a **recessionary gap**: actual GDP below potential, unemployment above the natural rate. In principle, excess labor supply should push wages down, lowering costs, shifting SRAS right, and returning GDP to potential at a lower price level. In practice, this is where the famous Keynesian critique bites: wages are **downwardly rigid** — workers resist nominal wage cuts, unions enforce wage floors, and morale effects make employers reluctant to cut pay. The self-correction mechanism operates very slowly on the downside. This asymmetry — fast correction upward, slow correction downward — is the core argument for activist macroeconomic policy: if self-correction would take years or decades, the social costs of waiting (sustained unemployment, lost output, eroded human capital) may justify policy intervention to speed the return to potential.
