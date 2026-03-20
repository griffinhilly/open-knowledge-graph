---
id: pump-system-matching-operating-point
title: 'Pump-System Matching: Operating Point and System Curves'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: centrifugal-pump-curves-selection
  type: hard
- id: pipe-network-solutions-hardy-cross
  type: soft
tags:
- pump-selection
- system-curve
- operating-point
stage: advanced
status: draft
---

# Pump-System Matching: Operating Point and System Curves

## Core Idea
A system curve represents the head required to deliver each flow rate: H_system = ΔZ + H_loss, where H_loss increases with Q². The pump-system operating point is where the pump curve intersects the system curve. Changing pipe sizes, adding resistance, or altering elevation shifts the system curve; changes in pump speed shift the pump curve, allowing flow control without replacing the pump.

## Explainer

From your work with centrifugal pump curves, you know that a pump has a characteristic H–Q curve: at zero flow it produces maximum head; as flow increases, head falls. The pump doesn't "know" what flow rate it will deliver — it simply responds to whatever resistance the connected system presents. The **system curve** captures that resistance: H_system(Q) = ΔZ + K·Q², where ΔZ is the static head the pump must overcome (elevation change plus any constant pressure difference) and K·Q² is the friction head, which grows with the square of flow because pipe losses scale with V² and V is proportional to Q. The **operating point** — the actual flow and head delivered — is where these two curves cross. At that point, the head the pump supplies exactly matches the head the system demands.

Visualizing the intersection makes flow control intuitive. If you throttle a downstream valve, you increase K — the system curve steepens, the intersection moves up and to the left, and flow decreases. You haven't changed the pump at all; you've changed the system. Conversely, if you reduce static head (e.g., lower the discharge reservoir level), the system curve drops, the intersection moves right, and flow increases. This is why the system curve is just as important as the pump curve when sizing a pump: a pump that performs well in one system can be dramatically over- or under-loaded in a system with different pipe sizes or elevation.

The most powerful flow control technique is **variable speed drive (VSD)**: changing pump rotational speed N shifts the entire pump curve according to the **affinity laws** — flow scales with N, head scales with N², and power scales with N³. If you halve the speed, flow halves but power drops to one-eighth of its original value. This is far more efficient than throttling (which wastes energy across the valve) and explains why VSD motors are standard in modern HVAC and water systems. On the pump curve, increasing speed moves the curve up and to the right; decreasing speed moves it down and left.

**Multiple pumps** expand the operating envelope. Two identical pumps in **parallel** add their flows at the same head — the combined pump curve has double the Q at each H value, useful when you need high flow but the system head doesn't require it. Two pumps in **series** add heads at the same flow — the combined curve has double the H at each Q, useful for high-head systems like multi-story buildings or deep wells. The operating point shifts accordingly in both cases, but it remains at the intersection of the combined pump curve with the (unchanged) system curve. A common design mistake is to assume two parallel pumps always deliver twice the flow of one — they don't, because the operating point moves up the steepening system curve and each pump delivers less than its solo flow.


