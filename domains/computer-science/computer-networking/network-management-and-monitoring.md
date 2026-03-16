---
id: network-management-and-monitoring
title: Network Management and Monitoring
domain: computer-science
course: computer-networking
prerequisites:
- id: osi-model-layers
  type: hard
- id: network-standards-and-ietf
  type: hard
tags:
- snmp
- monitoring
- management
- alerting
stage: advanced
status: draft
---

# Network Management and Monitoring

## Core Idea
Network management involves monitoring device health, link usage, and service quality; collecting metrics via SNMP agents on devices; and configuring devices from a central management station. Monitoring tools collect metrics like CPU, memory, interface statistics, and application-level metrics to detect problems before they impact users. Real-time alerting on threshold violations enables rapid response.

## Explainer

From your study of the OSI model, you know that networks are built in layers — physical links, data frames, IP packets, transport sessions, and applications. Network management operates across all of these layers simultaneously, giving administrators a unified view of what is happening at every level of the stack. The core challenge is that a modern network may contain hundreds or thousands of devices, each generating its own local view of the world. Without centralized management, diagnosing a slow application might require logging into dozens of routers and switches individually. Network management tools solve this by collecting data from every device and presenting it in one place.

The dominant protocol for this collection is **SNMP (Simple Network Management Protocol)**, which you encountered through network standards and the IETF. SNMP works on an agent-manager model: each network device runs a small software agent that exposes a structured database of variables called a **MIB (Management Information Base)**. The MIB organizes everything the device knows — interface counters, CPU utilization, error rates, routing table size — into a tree of named, numbered objects. The management station periodically polls agents for these values (GET requests), and agents can also send unsolicited **traps** when something noteworthy happens, like an interface going down. Think of it as each device maintaining a standardized dashboard, and the management station reading all the dashboards from a central console.

Monitoring becomes powerful when raw metrics are combined with **baselines and thresholds**. A baseline captures normal behavior — say, a WAN link that typically runs at 40% utilization during business hours. An alert fires when utilization crosses 85%, not because 85% is universally bad, but because it deviates significantly from this network's normal pattern. Good monitoring systems distinguish between a brief spike (often harmless) and a sustained threshold violation (likely a real problem) by using dampening — requiring the condition to persist for some interval before firing. This prevents alert fatigue, where administrators are buried under thousands of transient notifications and start ignoring them all.

Beyond reactive alerting, modern network management includes **configuration management** and **performance trending**. Configuration management tracks the running configuration of every device, detects unauthorized changes, and can push standardized configurations across the network. Performance trending stores historical metrics so administrators can identify slow degradation — a link whose utilization has grown 5% per month will saturate in six months, and capacity planning catches this before users notice. Together, these capabilities — fault detection, performance monitoring, configuration control, and capacity planning — form the FCAPS framework (Fault, Configuration, Accounting, Performance, Security) that defines the scope of network management as a discipline.
