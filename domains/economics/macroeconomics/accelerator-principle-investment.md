---
id: accelerator-principle-investment
title: The Accelerator Principle
domain: economics
course: macroeconomics
prerequisites:
- id: investment-demand-and-interest-rates
  type: hard
- id: business-cycles
  type: soft
builds-toward:
- business-cycles
tags:
- investment
- output
- acceleration
stage: formal-systems
status: draft
---

# The Accelerator Principle

## Core Idea
The accelerator principle states that investment depends on the change in output, not the level of output. Firms expand their capital stock when demand is rising (accelerating), but cut investment sharply during slowdowns. This creates an amplification mechanism: a small deceleration in output growth triggers a large drop in investment, magnifying the downturn.

## Explainer

From your study of investment demand, you know that investment is the flow of spending that adds to the capital stock. The accelerator principle provides the key insight into *why* firms invest: not because output is high, but because output is *growing*. The logic comes from a simple relationship — firms want to hold a capital stock roughly proportional to their output (to serve demand). If desired capital is K* = v·Y (where v is the capital-output ratio), then desired investment is the change in the capital stock: I = v·ΔY. Output growth requires new capital; stable output requires only replacement investment (to offset depreciation); and declining output means the existing capital stock is already more than sufficient, so firms cut new investment to near zero.

A numerical example makes the amplification vivid. Suppose a firm wants a capital-output ratio of 3 — $3 of capital to produce $1 of output per year. If output grows from $100 to $110, the firm needs $30 of new capital (to go from $300 to $330). This requires $30 of gross investment (plus depreciation). Now output slows from $110 to $115 — growth continues, but at half the previous rate. Desired capital rises from $330 to $345, requiring only $15 of new investment. Investment falls by half even though output is still rising. If output merely holds flat at $115, desired investment falls to zero (plus replacement only). A plateau in output growth — not a recession, just a slowdown — causes investment to collapse.

This is the **acceleration effect**: investment is highly volatile relative to output because it responds to the *change* in output, which is itself volatile. Business cycle fluctuations in GDP are modest (a few percent), but investment swings of 20–30% are common because the acceleration mechanism magnifies small output changes into large investment changes. Your prior study of business cycles is relevant here: the accelerator is one of the key internal propagation mechanisms that makes downturns self-reinforcing. When output slows, investment falls; the fall in investment reduces aggregate demand further, slowing output more; which further reduces investment. This **multiplier-accelerator interaction** (combined with the Keynesian multiplier that amplifies spending changes into output changes) was the basis for the first mathematical models of endogenous business cycles developed by Harrod, Samuelson, and Hicks in the 1930s–1950s.

The accelerator also explains why investment in long-lived capital goods — machinery, buildings, software — is the most cyclically volatile component of GDP. Consumer spending on non-durables is relatively stable because consumption tracks income. But firms facing uncertain demand become very cautious about locking in new capital commitments during downturns, since unused capital is costly and lumpy investments are hard to reverse. This **irreversibility** makes the accelerator asymmetric in practice: firms are quick to cut investment when growth slows, but cautious about ramping it back up until they are confident the recovery is sustained.
