---
id: supply-side-shocks-and-stagflation
title: Supply-Side Shocks and Stagflation
domain: economics
course: macroeconomics
prerequisites:
- id: aggregate-supply-short-run
  type: hard
- id: inflation-and-price-level
  type: hard
builds-toward:
- stagflation-and-conflicting-policy
tags:
- shocks
- inflation
- unemployment
stage: formal-systems
status: validated
---

# Supply-Side Shocks and Stagflation

## Core Idea
Supply shocks (oil price spikes, crop failures, productivity declines) shift aggregate supply leftward, raising prices and reducing output simultaneously—stagflation. Unlike demand shocks, which produce a tradeoff between inflation and unemployment, supply shocks worsen both. Supply shocks are particularly difficult for policymakers: stimulating demand alleviates unemployment but worsens inflation, while restricting demand reduces inflation but increases unemployment.

## Questions

```yaml
- question: "After a major oil supply disruption, a central bank expands the money supply to combat the resulting recession. What happens to inflation?"
  type: multiple-choice
  options:
    - "Inflation falls — stimulus restores output, which lowers costs through economies of scale"
    - "Inflation worsens — expanding AD shifts the demand curve rightward against the already-shifted AS curve, raising the price level further"
    - "Inflation is unaffected — supply shocks isolate inflation from monetary policy entirely"
    - "Inflation and unemployment both fall because stimulus reverses the supply shock's effects"
  answer: 1
  explanation: "Expanding the money supply shifts AD rightward. But the AS curve has already shifted leftward from the supply shock. The new intersection of rightward-shifted AD and leftward-shifted AS sits at higher output than without stimulus (reducing unemployment) but at an even higher price level (worsening inflation). This is the policy trap: the standard tool for fighting recession exacerbates the inflation component of stagflation."

- question: "Which best explains why stagflation is harder to address than a pure demand-driven recession?"
  type: multiple-choice
  options:
    - "Stagflation always persists longer, so standard tools run out of effectiveness over time"
    - "Central banks have no policy tools that affect supply-side conditions at all"
    - "Any demand-management policy that alleviates unemployment worsens inflation, and vice versa — leaving no clean solution"
    - "Supply shocks always produce more severe downturns than demand shocks of equivalent size"
  answer: 2
  explanation: "The defining difficulty of stagflation is the policy trap. Demand-management tools shift AD. Shifting it right helps unemployment but worsens inflation. Shifting it left reduces inflation but deepens the recession. With a pure demand shock, the problem and the solution involve the same direction of AD movement. With a supply shock, both problems exist simultaneously and any AD movement trades one problem for the other. The only genuine cure is restoring supply."

- question: "A negative supply shock raises prices while simultaneously boosting output, creating a tradeoff policymakers can exploit."
  type: true-false
  answer: false
  explanation: "A negative supply shock shifts AS leftward — firms can produce less at every price level. The new AS-AD intersection has a higher price level AND lower output simultaneously. This is stagflation, not a tradeoff to exploit. Tradeoffs between inflation and output arise from demand shocks (which move the economy along the AS curve). Supply shocks move the AS curve itself, producing the worst of both worlds."

- question: "A positive supply shock — such as a major fall in commodity prices — simultaneously reduces inflation and increases output."
  type: true-false
  answer: true
  explanation: "A positive supply shock shifts AS rightward. The new equilibrium has higher output AND a lower price level — the mirror image of stagflation. Both macroeconomic indicators improve at once. This is why productivity gains from technology are so valuable: they deliver the output expansion of stimulus without the inflationary cost."

- question: "Why is a supply shock fundamentally different from a demand shock in terms of the policy response it requires?"
  type: short-answer
  answer: "A demand shock moves the economy along the existing AS curve: a recession (leftward AD shift) can be countered by rightward AD stimulus, and vice versa — the problem and solution involve the same tool in opposite directions. A supply shock moves the AS curve itself, creating stagflation where output falls and prices rise simultaneously. Any demand-side response that fixes one variable worsens the other. The correct response requires restoring the supply side — reducing input costs, improving productivity, removing bottlenecks — not manipulating aggregate demand."
  explanation: "This asymmetry is why supply shocks historically caused so much policy confusion. Standard Keynesian or monetarist tools are demand-side instruments. When the 1970s oil shocks hit, policymakers tried both stimulus (which worsened inflation) and contraction (which worsened unemployment) before recognizing that demand management cannot cure a supply-side problem. Recognition of shock type is the first analytical step."
```

## Explainer

Supply shocks are disruptions to the economy's productive capacity rather than to spending. From your study of aggregate supply, you know the short-run AS curve reflects the costs of production—when those costs rise suddenly (an oil price spike, a war disrupting supply chains, a poor harvest), firms can produce less at every price level. The AS curve shifts leftward, and the new intersection with the AD curve sits at a higher price level *and* lower real output simultaneously. This combination—inflation plus recession—is **stagflation**, and it is what made the 1970s oil crises so economically painful.

What makes stagflation uniquely difficult is the **policy trap** it creates. You already know that inflation arises when output exceeds potential (demand-pull) or costs rise (cost-push), and that unemployment rises when output falls below potential. Normally these problems appear separately: recession → stimulate demand; inflation → restrict demand. A supply shock destroys this separation. Both problems appear at once, and any policy response that addresses one aggravates the other.

Consider the policymaker's choices after an adverse supply shock. If they expand fiscal or monetary policy to fight the recession (moving along the new, higher-cost AS curve toward higher output), they accept even higher inflation—the AD curve shifts right, raising the price level further. If they tighten policy to fight inflation—restricting demand—they push output down further, deepening the recession. There is no clean medicine for stagflation within the standard demand-management toolkit. The only true cure is a positive supply shock that reverses the original disruption (e.g., energy prices falling back), or long-run supply-side policies that improve productivity.

**Positive supply shocks** work in reverse: a technological breakthrough, a fall in commodity prices, or increased labor force participation shifts AS rightward—lower prices and higher output simultaneously. These combine the benefits of both anti-inflation and anti-recession policies at once. Recognizing whether a shock is supply-side or demand-side is therefore the first analytical task in any macroeconomic diagnosis, because the policy response must be matched to the shock type.
