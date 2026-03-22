---
id: time-domain-response-first-order
title: First-Order System Time Response
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: first-order-transient-circuits
  type: soft
builds-toward:
- time-domain-response-second-order
- steady-state-error-analysis
tags:
- time-constant
- step-response
- first-order
- transient
- bandwidth
stage: advanced
status: validated
---

# First-Order System Time Response

## Core Idea
A first-order system has a transfer function G(s) = K/(τs + 1), where K is the DC gain and τ is the time constant. The step response rises exponentially as y(t) = K(1 − e^{−t/τ}), reaching 63.2% of its final value at t = τ and settling within 2% at t ≈ 4τ. First-order systems never overshoot — they approach the final value monotonically. The time constant τ characterizes both the speed of response and the system's bandwidth (ω₋₃dB = 1/τ rad/s), providing a direct link between time-domain and frequency-domain behavior.

## How It's Best Learned
Measure and fit τ from step response data on RC circuits or thermal systems, then verify by computing the Bode bandwidth. Simulate step responses with varying K and τ to build physical intuition before moving to higher-order systems.

## Common Misconceptions
- The time constant τ is not the settling time; the 2% settling time is approximately 4τ.
- A first-order system with an added zero is still first-order but can exhibit an initial positive spike or an initial undershoot depending on the zero location.
- Faster response (smaller τ) requires larger bandwidth, which amplifies measurement noise — speed always trades off against noise sensitivity.

## Questions

```yaml
- question: "A control engineer reduces a thermostat system's time constant τ from 10 seconds to 1 second to achieve faster response. A colleague warns this change will introduce a new problem. What is it?"
  type: multiple-choice
  options:
    - "The system will now overshoot the target temperature and oscillate"
    - "The system's bandwidth increases tenfold, causing it to pass significantly more high-frequency measurement noise"
    - "The DC gain K will decrease proportionally, making the steady-state temperature less accurate"
    - "A time constant below 5 seconds causes the step response to become non-exponential"
  answer: 1
  explanation: "Bandwidth equals 1/τ, so reducing τ from 10s to 1s increases bandwidth from 0.1 rad/s to 1 rad/s. A wider bandwidth means the system responds to — and amplifies — higher-frequency input variations, including sensor noise. First-order systems cannot overshoot (a common misconception); overshoot requires two poles, not one. The DC gain K is independent of τ and is unaffected by this change. The fundamental speed-versus-noise tradeoff is inherent to any dynamic system."

- question: "A first-order system has transfer function G(s) = 5/(2s + 1). A unit step input is applied. What is the output at t = 2 seconds?"
  type: multiple-choice
  options:
    - "Approximately 3.16, since t = 2s equals the time constant τ = 2 and the output reaches 63.2% of its final value K = 5"
    - "Approximately 4.90, since the 2% settling criterion is met at t = 2s"
    - "Exactly 2.50, since t/τ = 1 gives exactly half the final value"
    - "Exactly 5.00, since the system has had sufficient time to fully settle"
  answer: 0
  explanation: "The time constant τ = 2 (from the denominator 2s + 1). At t = τ, the step response y(t) = K(1 − e^{−t/τ}) = 5(1 − e^{−1}) ≈ 5 × 0.632 = 3.16. The 2% settling time is 4τ = 8 seconds — not 2 seconds. The step response never exactly reaches the final value of 5 in finite time; it approaches it asymptotically. The output at t = τ is always 63.2% of the final value, regardless of K or τ."

- question: "A first-order system's step response approaches its final value asymptotically and technically never reaches it in finite time, which is why engineers use the 2% settling time as a practical criterion for when the transient is complete."
  type: true-false
  answer: true
  explanation: "The exponential y(t) = K(1 − e^{−t/τ}) approaches K as t → ∞ but only equals K at t = ∞. At t = 4τ, the output is at 98.2% of the final value — within 2% — which engineers accept as 'settled.' This is a practical convention, not a mathematical endpoint. The exponential decay never reaches zero."

- question: "The time constant τ of a first-order system is the time at which the step response settles to within 2% of its final value."
  type: true-false
  answer: false
  explanation: "This is a common and consequential misconception. The time constant τ is the time at which the step response reaches 63.2% (= 1 − e^{−1}) of its final value — not 98%. The 2% settling time is approximately 4τ, not τ. Confusing these can lead to significant design errors: a system with τ = 1s does not settle in 1 second; it settles in approximately 4 seconds."

- question: "Explain why reducing a first-order system's time constant makes it both faster and more noise-sensitive, and why this represents a fundamental tradeoff rather than an engineering oversight."
  type: short-answer
  answer: "The time constant τ is directly linked to bandwidth by ω₋₃dB = 1/τ. A smaller τ means wider bandwidth — the system faithfully tracks faster input changes, which is what makes it 'faster.' But bandwidth does not distinguish between desired signals and noise: a system with wider bandwidth passes high-frequency noise just as readily as high-frequency signals. Since real sensor noise has significant high-frequency content, a faster system amplifies more noise. This tradeoff is fundamental because it is impossible to track fast signals without also responding to fast noise at similar frequencies — the two are physically indistinguishable to the filter. The engineering task is to choose τ to meet speed requirements while keeping noise amplification within acceptable limits."
  explanation: "This speed-versus-noise tradeoff reappears in every control and signal processing design. In higher-order systems it manifests in the gain-bandwidth product; in digital filters it appears as the transition band width. Understanding it at the level of first-order systems provides the conceptual foundation for all subsequent filter and controller design."
```

## Explainer

The first-order system is the simplest dynamical system — one energy storage element, one time constant, no oscillations. You already know transfer functions map inputs to outputs in the Laplace domain. When you apply a unit step input to G(s) = K/(τs + 1), the output in the time domain is y(t) = K(1 − e^{−t/τ}). This exponential rise follows directly from the system's internal feedback structure: the rate of change is proportional to how far the output still has to go. That is exactly what produces the decaying-error shape. The system is always "trying to catch up" to the target, and as it gets closer, it slows down.

The **time constant** τ is the single most important parameter. At t = τ, the output has reached 63.2% of its final value — this number is 1 − e^{−1} ≈ 0.632. At 2τ you are at 86%; at 4τ you are at 98%. Engineers use the **2% settling time** ≈ 4τ as the practical definition of when the transient is over. The system never literally reaches the final value (it approaches asymptotically), but 4τ is close enough for all practical purposes. Knowing τ from a step test immediately tells you how quickly the system responds and what bandwidth you will need to track time-varying inputs.

The time constant also links time-domain behavior to frequency-domain behavior. The **bandwidth** — the frequency at which output power drops to half its DC value — equals ω_{−3dB} = 1/τ exactly. Faster systems (smaller τ) have wider bandwidth, meaning they faithfully track higher-frequency input changes. But that wider bandwidth also passes more high-frequency noise through the system. A thermostat with a one-second time constant tracks fast temperature fluctuations precisely but is jittery; one with a ten-second time constant is smooth but sluggish. This speed-versus-noise tradeoff recurs in every real control and signal processing design — first-order systems make it explicit and quantitative.

One thing first-order systems never do is **overshoot**. With a single pole at s = −1/τ, the step response is purely real-exponential and rises monotonically. You can add a **zero** to a first-order system (by differentiating the input, for example), which may create an initial spike or undershoot depending on the zero location, but the underlying pole structure remains first-order and the response eventually settles without oscillation. This clean baseline — one pole, monotonic approach, settling at 4τ, bandwidth at 1/τ — is what you will use as a reference when second-order systems begin to overshoot and ring. The richer behavior there comes entirely from the second pole.
