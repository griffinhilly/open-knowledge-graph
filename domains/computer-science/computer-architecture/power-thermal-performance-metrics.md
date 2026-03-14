---
id: power-thermal-performance-metrics
title: Performance Metrics, Power, and Thermal Management
domain: computer-science
course: computer-architecture
prerequisites:
- id: pipelining-fundamentals
  type: soft
- id: cache-design-principles
  type: soft
tags:
- performance
- power
- thermal
- metrics
stage: formal-systems
status: draft
---

# Performance Metrics, Power, and Thermal Management

## Core Idea
CPU performance is measured by clock speed, IPC (instructions per cycle), and latency. Power consumption is proportional to voltage, frequency, and switching activity; thermal dissipation must be managed via cooling. Trade-offs between performance and power are fundamental to processor design.

## How It's Best Learned
Compare performance (cycles per instruction), power (watts), and thermal design power (TDP) across generations; understand Dennard scaling limits.

## Common Misconceptions
Higher clock speed does not always mean better performance—IPC matters equally. Power consumption scales superlinearly with voltage; thermal limits often constrain clock speed.
