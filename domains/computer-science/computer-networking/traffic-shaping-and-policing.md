---
id: traffic-shaping-and-policing
title: Traffic Shaping and Policing
domain: computer-science
course: computer-networking
prerequisites:
- id: qos-quality-of-service
  type: hard
tags:
- traffic-shaping
- policing
- rate-limiting
- qos
stage: advanced
status: draft
---

# Traffic Shaping and Policing

## Core Idea
Traffic shaping smooths bursty traffic to match a specified rate, buffering excess packets for later transmission without discarding them. Policing enforces a rate limit by discarding excess traffic, providing hard guarantees but risking packet loss. Both techniques use token bucket algorithms and are essential for implementing service-level agreements and preventing congestion.
