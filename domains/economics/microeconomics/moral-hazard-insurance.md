---
id: moral-hazard-insurance
title: Moral Hazard in Insurance and Contracting
domain: economics
course: microeconomics
prerequisites:
- id: moral-hazard
  type: hard
tags:
- moral-hazard
- incentives
- insurance
stage: advanced
status: validated
---

# Moral Hazard in Insurance and Contracting

## Core Idea
Moral hazard arises when one party's effort or behavior is hidden (not observed) after a contract is signed. Example: once insured, a person has less incentive to prevent loss. Insurers respond by deductibles, coinsurance, and monitoring—making the insured share risk to align incentives. Moral hazard explains why insurance is incomplete (full coverage isn't offered) and why contracts include incentive clauses.

## How It's Best Learned
Compare full vs. partial insurance coverage. Understand why full insurance reduces effort to prevent loss. See how deductibles solve the problem.

## Common Misconceptions
- Moral hazard is unethical behavior (it's a rational response to incentives; the problem is aligning incentives, not morality).
- Moral hazard and adverse selection are the same (one is pre-contract information, the other is post-contract behavior).

## Questions

```yaml
- question: "A homeowner purchases comprehensive flood insurance with full coverage and zero deductible. How does standard moral hazard theory predict their behavior will change?"
  type: multiple-choice
  options:
    - "They will invest more in flood prevention because they now have more financial security"
    - "They will reduce investment in flood prevention because the insurer bears the full cost of any loss"
    - "Their behavior will not change because moral hazard only applies to car insurance"
    - "They will invest the same amount in prevention because floods are uncontrollable anyway"
  answer: 1
  explanation: "Full coverage with zero deductible means the homeowner bears none of the financial cost of a flood loss. Any prevention effort (raised foundations, sump pumps, flood barriers) now has zero personal financial benefit — the insurer pays regardless. Moral hazard predicts that rational agents reduce effort when they do not bear the consequences of inaction. This is not dishonesty; it is the logical response to changed incentives. The insurer priced the policy assuming pre-insurance prevention levels, but behavior changes post-contract."

- question: "What is the primary economic purpose of requiring insured parties to pay a deductible?"
  type: multiple-choice
  options:
    - "To reduce administrative costs by discouraging small claims"
    - "To penalize policyholders who file claims too frequently"
    - "To preserve the insured's incentive to prevent losses by ensuring they bear some financial cost"
    - "To allow insurers to offer lower premiums by transferring risk back to policyholders"
  answer: 2
  explanation: "Deductibles are incentive alignment tools, not punishments. By making the insured pay the first $X of any loss, the deductible ensures that prevention efforts have personal financial value — you still benefit from avoiding the first $X. Without any deductible, the full financial benefit of prevention accrues to the insurer, destroying the insured's motivation to take precautions. Reduced administrative costs (option A) are a secondary effect, but the primary function is preserving the insured's skin in the game."

- question: "A deductible partially restores the insured's incentive to prevent loss by ensuring they bear the cost of small claims."
  type: true-false
  answer: true
  explanation: "Yes — a deductible makes the insured the residual claimant on small losses. If you must pay the first $500 of any damage, you have a direct financial incentive to prevent incidents that would cost less than $500 (or even somewhat more). This is precisely why deductibles exist from an incentive standpoint: they keep some 'skin in the game' so the insured's interests partially align with the insurer's interests in preventing the loss."

- question: "Full insurance with zero deductible is optimal for a risk-averse individual because it completely eliminates financial risk, which is the goal of insurance."
  type: true-false
  answer: false
  explanation: "This ignores the incentive effect — the key insight of moral hazard. While full insurance maximizes risk-sharing (good for the risk-averse individual), it eliminates all incentive to prevent the insured event. The optimal contract under unobservable effort trades off risk-bearing against incentive provision: some risk must be left with the insured to maintain prevention motivation. Full coverage is only optimal if effort is observable (and can be contractually required) or if the insured event is entirely unpreventable."

- question: "Why is complete insurance — full coverage with zero deductible — never optimal when the insured's effort is unobservable?"
  type: short-answer
  answer: "Complete insurance removes all personal financial consequences of the insured event, which eliminates any incentive to take preventive action. Since the insurer cannot observe whether the insured is taking precautions, it cannot condition the contract on effort. Rational agents then reduce prevention to zero, increasing the probability of loss — at the insurer's full expense. The optimal contract balances the benefits of risk transfer (which argues for more coverage) against the need to maintain prevention incentives (which argues for deductibles and coinsurance). Some risk retention is always efficient when effort is hidden."
  explanation: "This is the core moral hazard result: information asymmetry about effort makes full insurance non-optimal even for genuinely risk-averse individuals. The insurer must make the insured a partial residual claimant to align incentives. The result has broad applications beyond insurance: employment contracts include bonuses and profit-sharing for the same reason — if employees bore no cost of poor performance, they would underinvest in effort."
```

## Explainer

You already understand moral hazard as a general phenomenon — the idea that having protection changes how people behave. Insurance is the canonical setting where this plays out, and it reveals both why the problem is inescapable and why markets have developed specific tools to manage it.

Imagine you own a car and have no insurance. You park carefully, keep a steering lock, and use well-lit spaces at night. Every precaution has a personal benefit: it reduces the probability you pay for a repair out of pocket. Now suppose you get comprehensive insurance with full coverage and zero deductible. The precaution is now less personally valuable — the insurer bears the loss, not you. Rationally, your investment in prevention falls. This is **moral hazard**: the insurance contract itself changed the incentives that made the insured event less likely. The insurer is pricing coverage based on your pre-insurance behavior, but after the contract is signed, your behavior changes. The insurer cannot directly observe whether you left your car unlocked or parked in a risky location; your effort is the **hidden action**.

The insurer's response is to make you share the risk — via **deductibles** (you pay the first $X, so your incentive to prevent small losses is preserved), **coinsurance** (you pay a percentage of every loss, so your marginal cost of carelessness is never zero), and **policy limits** (you bear the tail risk, so very large losses still hurt you). These are not punishments; they are incentive alignment tools. By keeping some skin in the game, the insurer restores at least partial motivation to reduce risk. The optimal contract trades off risk-bearing (the insured should bear less risk because insurers diversify better) against incentives (the insured needs enough exposure to maintain prevention effort).

Moral hazard is distinct from **adverse selection**, which happens *before* a contract is signed: high-risk types disproportionately seek coverage, biasing the insured pool. Moral hazard is a post-contract behavioral change. Both arise from information asymmetry — the insurer cannot observe everything — but at different stages of the relationship. In practice, the same contract features (deductibles, coinsurance, monitoring) can address both problems simultaneously, which is why insurance contracts are structured the way they are. The key insight is that complete insurance — full coverage with no deductible — is never optimal when effort is unobservable, because it fully removes the incentive to prevent the loss the insurance is covering.
