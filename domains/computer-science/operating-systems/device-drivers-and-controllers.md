---
id: device-drivers-and-controllers
title: Device Drivers and I/O Controllers
domain: computer-science
course: operating-systems
prerequisites:
- id: io-systems-overview
  type: hard
- id: interrupt-exception-handling
  type: soft
tags:
- drivers
- hardware
- io
stage: formal-systems
status: draft
---

# Device Drivers and I/O Controllers

## Core Idea
Device drivers are kernel code modules that manage hardware devices, translating high-level I/O operations into device-specific commands and protocols. Hardware controllers execute these commands and signal completion via interrupts. Device drivers abstract hardware differences and provide a uniform interface to user programs, isolating applications from hardware details.
