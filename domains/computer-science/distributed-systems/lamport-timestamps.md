---
id: lamport-timestamps
title: Lamport Timestamps
domain: computer-science
course: distributed-systems
prerequisites:
- id: logical-clocks
  type: hard
builds-toward:
- causal-ordering
- consensus-problem
tags:
- timestamps
- ordering
- lamport
stage: advanced
status: draft
---

# Lamport Timestamps

## Core Idea
Lamport timestamps assign scalar timestamps to events using a simple rule: each process maintains a counter that is incremented on local events and set to max(local, received) + 1 on message receipt. If event A causally precedes event B, then A's timestamp is strictly less than B's timestamp, enabling total ordering of events across the system.

## How It's Best Learned
Trace execution of multiple processes sending messages and track how timestamps evolve.

## Common Misconceptions
Lamport timestamps uniquely determine causality (they only order causally related events); they require synchronized physical clocks.
