---
id: switching-basics
title: Network Switching and Switching Tables
domain: computer-science
course: computer-networking
prerequisites:
- id: mac-addressing
  type: hard
builds-toward:
- vlans-virtual-area-networks
- spanning-tree-protocol
tags:
- switch
- forwarding
- mac-table
- layer-2-forwarding
stage: advanced
status: draft
---

# Network Switching and Switching Tables

## Core Idea
A network switch is a Layer 2 device that forwards frames based on destination MAC addresses using a MAC address table. Switches learn MAC addresses by observing source addresses in arriving frames, then forward frames destined for known addresses directly to the appropriate port, reducing collision domains and improving bandwidth utilization.
