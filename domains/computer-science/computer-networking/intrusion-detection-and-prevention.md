---
id: intrusion-detection-and-prevention
title: Intrusion Detection and Prevention Systems
domain: computer-science
course: computer-networking
prerequisites:
- id: network-security-fundamentals
  type: hard
tags:
- ids
- ips
- intrusion-detection
- anomaly-detection
stage: advanced
status: draft
---

# Intrusion Detection and Prevention Systems

## Core Idea
IDS systems detect suspicious network traffic patterns using signature matching or anomaly detection; IPS systems extend IDS by actively blocking detected attacks. Both monitor traffic at network or host level for signs of compromise or attacks. Machine learning techniques increasingly supplement signature-based detection to identify novel attack patterns.

## Explainer

From network security fundamentals, you understand that firewalls filter traffic based on rules about addresses, ports, and protocols. But firewalls are blunt instruments — they enforce policies about *who* can talk to *whom*, not about *what* is being said. A firewall that allows HTTP traffic on port 80 will happily pass through a SQL injection attack embedded in a valid HTTP request. **Intrusion Detection Systems** (IDS) and **Intrusion Prevention Systems** (IPS) fill this gap by inspecting the *content* and *behavior* of network traffic to identify malicious activity.

An **IDS** monitors network traffic (or host activity) and generates alerts when it detects something suspicious. It operates in two fundamental modes. **Signature-based detection** maintains a database of known attack patterns — specific byte sequences, packet structures, or protocol anomalies that correspond to known exploits. When traffic matches a signature, the IDS flags it. This is analogous to antivirus scanning: it is highly accurate for known threats (low false positives) but completely blind to novel attacks not yet in the database (high false negatives). **Anomaly-based detection** instead builds a model of "normal" traffic — typical bandwidth usage, protocol distributions, connection patterns — and flags deviations from that baseline. This can catch zero-day attacks and insider threats that have no known signature, but it generates more false positives because legitimate but unusual activity (a backup job, a software update, a traffic spike) can look anomalous.

The critical distinction between IDS and **IPS** is *placement* and *action*. An IDS typically operates passively — it monitors a copy of the traffic (via a network tap or port mirror) and alerts administrators, but it does not block anything. An IPS sits **inline** on the network path, meaning all traffic flows through it. When the IPS detects an attack, it can actively **drop the malicious packets**, reset the connection, or block the source IP — in real time, before the attack reaches its target. This inline position gives the IPS defensive power but also introduces risk: false positives cause legitimate traffic to be blocked, and the IPS itself becomes a potential bottleneck and single point of failure.

Deployment comes in two forms. A **network-based** IDS/IPS (NIDS/NIPS) monitors traffic at a network chokepoint — typically at the perimeter or between network segments. A **host-based** IDS/IPS (HIDS/HIPS) runs on individual servers, monitoring system calls, file changes, log entries, and local network connections. The two approaches are complementary: NIDS catches attacks traversing the network, while HIDS catches attacks that originate locally or that encrypted network traffic conceals from NIDS. Modern security operations typically deploy both, feeding alerts into a centralized **SIEM** (Security Information and Event Management) system for correlation and response.
