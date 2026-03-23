---
id: capital-flows-equilibrium
title: International Capital Flows and Equilibrium
domain: economics
course: macroeconomics
prerequisites:
- id: current-account-definition-measurement
  type: hard
- id: international-capital-flows
  type: soft
builds-toward:
- mundell-fleming-extended
tags:
- capital-flows
- interest-rates
- international-investment
- equilibrium
stage: formal-systems
status: validated
---

# International Capital Flows and Equilibrium

## Core Idea
International capital flows are motivated by interest rate differentials and risk considerations. Capital flows adjust to equalize risk-adjusted returns across countries. Equilibrium requires expected return on domestic assets equals expected return on foreign assets (adjusted for exchange risk).

## How It's Best Learned
Set up uncovered interest rate parity: r_domestic ≈ r_foreign + expected depreciation. Show if US rate exceeds German, investors expect dollar depreciation. If not, capital flows to US until returns equalize.

## Common Misconceptions
- Assuming capital flows respond instantly.
- Treating interest rate parity as a law.
- Forgetting expectations matter.

## Questions

```yaml
- question: "The US Federal Reserve raises interest rates from 3% to 6%, while European rates stay at 3%. What happens in the short run and why doesn't the 3% interest rate gap permanently attract capital to the US?"
  type: multiple-choice
  options:
    - "Capital flows to the US indefinitely because higher rates always mean higher returns — the gap never closes"
    - "Capital flows to the US initially, appreciating the dollar, until the expected future depreciation of the now-overvalued dollar offsets the interest rate advantage"
    - "Capital flows out of the US because investors expect a recession when rates are high"
    - "Nothing happens — interest rate differentials don't affect capital flows in modern economies"
  answer: 1
  explanation: "When US rates rise, investors buy dollar assets, which appreciates the dollar immediately. The dollar is now above its long-run equilibrium value, so markets expect it to depreciate back toward fundamentals. That expected depreciation is precisely what offsets the interest rate advantage: if US rates are 3 percentage points higher but the dollar is expected to fall 3%, the total expected return on US and European assets is equalized. This is uncovered interest rate parity (UIP): r_domestic ≈ r_foreign + expected depreciation. The gap doesn't persist as a free lunch because the exchange rate itself adjusts."

- question: "Under uncovered interest rate parity (UIP), what does equilibrium actually mean?"
  type: multiple-choice
  options:
    - "The domestic and foreign interest rates are equal"
    - "Net capital flows are zero — no money moves between countries"
    - "The expected total return on domestic assets equals the expected total return on foreign assets, once exchange rate changes are accounted for"
    - "The exchange rate is fixed so that capital flows freely at stable rates"
  answer: 2
  explanation: "UIP equilibrium does NOT require equal interest rates — it requires equal expected total returns. A country with 6% interest rates and an expected 3% currency depreciation is equivalent to a country with 3% rates and a stable currency: the total expected return is 3% in both cases. Equilibrium is the state where no investor has an incentive to shift their portfolio between countries, which occurs when exchange rate expectations exactly offset interest rate differentials. Option B is wrong: capital still flows, but there's no net incentive for additional flows."

- question: "A country with significant political risk or default risk must offer higher interest rates than a stable country, even after accounting for expected currency depreciation, in order to attract foreign capital."
  type: true-false
  answer: true
  explanation: "This is the risk premium: investors require compensation for the additional risk of holding assets in a politically unstable or potentially defaulting country. Pure UIP assumes risk-neutral investors and identical risk environments — but in practice, a country with elevated risk must offer a premium above what currency-adjusted returns alone would predict. This is why emerging market interest rates are often dramatically higher than developed-market rates even when exchange rate depreciation accounts for part of the gap."

- question: "When the US interest rate rises above Germany's, US investors immediately earn a permanently higher return than German investors — the exchange rate adjustment is just a technicality that doesn't actually affect real returns."
  type: true-false
  answer: false
  explanation: "The exchange rate adjustment is not a technicality — it is the mechanism that eliminates the apparent return advantage. When US rates rise and capital flows in, the dollar appreciates. An investor who converts euros to dollars to earn the higher US rate will then face a depreciated dollar when they convert back to euros at the end of the period. If UIP holds, that depreciation exactly offsets the interest rate advantage, leaving the total return identical to what they would have earned in Germany. The rate differential and the exchange rate movement are not independent — they are two sides of the same adjustment."

- question: "Explain why higher interest rates in one country don't permanently attract more capital than lower-rate countries in a world of mobile capital."
  type: short-answer
  answer: "Because the exchange rate adjusts to eliminate the return advantage. When investors rush to a high-rate country, they buy its currency, which appreciates it immediately. The now-overvalued currency is expected to depreciate back toward fundamentals, and that expected depreciation offsets the interest rate advantage in terms of total expected return. Equilibrium (uncovered interest rate parity) is reached when r_domestic ≈ r_foreign + expected depreciation — meaning the interest rate gap equals the expected exchange rate loss, so investors are indifferent between the two countries."
  explanation: "The key insight is that capital flows are self-limiting through exchange rate feedback. The act of flowing capital to the high-rate country changes the exchange rate in a way that reduces the attractiveness of further flows. This is why interest rate differentials persist only alongside expected exchange rate movements — the two are linked by the arbitrage behavior of investors. A 'free lunch' from higher rates is competed away through currency appreciation."
```

## Explainer

From your work on the current account, you know that a country's external position reflects how much it's borrowing from or lending to the rest of the world. The **capital account** (or financial account) is the flip side: every dollar borrowed must have a corresponding capital inflow, and every dollar lent out corresponds to a capital outflow. What determines which direction capital flows? In a world of mobile capital, the answer is relative returns — adjusted for risk and expected exchange rate movements.

The fundamental equilibrium condition is **uncovered interest rate parity (UIP)**: in equilibrium, the expected return on domestic assets must equal the expected return on foreign assets, once you account for expected exchange rate changes. If the US interest rate is 5% and the German rate is 2%, the gap doesn't persist as a free lunch. Investors will rush to US assets, buying dollars and selling euros. This drives the dollar up — and because an appreciated dollar is expected to depreciate back toward fundamentals over time, that expected depreciation is exactly the 3% gap. Equilibrium is reached when: r_domestic ≈ r_foreign + expected depreciation of domestic currency.

The dynamics of adjustment are crucial to understand. When the US rate rises relative to Germany's, capital initially flows *to* the US — investors sell euros, buy dollars, and purchase US bonds. This flow appreciates the dollar immediately (the "overshooting" phenomenon). The dollar has now appreciated *past* its long-run equilibrium, so it's expected to depreciate going forward, which is precisely what makes US and German assets equally attractive again. The equilibrium isn't that capital flows stop — it's that the exchange rate has moved enough to make the expected returns equal, so there's no further incentive for net flows.

In practice, several things complicate this clean picture. **Capital flows are lumpy, not continuous**: institutional investors rebalance periodically, creating discrete adjustment episodes rather than smooth convergence. **Risk premiums** matter — a country with default risk or political instability must offer higher interest rates just to attract the same capital, even after adjusting for expected depreciation. **Capital controls** in emerging markets can sever the parity condition entirely for periods of time. And **expectations are endogenous**: if investors believe a currency will depreciate, they demand a premium that can make that belief self-fulfilling. Understanding capital flow equilibrium means holding all these moving parts together: interest rates, exchange rates, expectations, and the risk environment all interact simultaneously.

