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

## Questions

```yaml
- question: "An IPS blocks a legitimate database query because it matches a SQL injection signature. What fundamental tradeoff does this illustrate about IPS deployment?"
  type: multiple-choice
  options:
    - "Signature-based detection cannot identify novel zero-day attacks"
    - "Inline placement makes the IPS a network bottleneck under heavy traffic"
    - "IPS false positives actively block legitimate traffic, whereas IDS false positives generate alerts without disruption — the inline position turns detection errors into operational outages"
    - "Anomaly-based detection has higher false positive rates than signature-based detection"
  answer: 2
  explanation: "The critical difference between IDS and IPS is what happens on a false positive. An IDS monitors a copy of traffic and generates alerts — a false positive wastes analyst time but causes no operational harm. An IPS sits inline; when it misidentifies legitimate traffic as malicious, it actively drops or blocks that traffic, potentially halting business operations. This asymmetry means IPS systems require careful tuning before being placed in blocking mode, and operators often run IPS in 'detection only' mode first to characterize the false positive rate."

- question: "A web server allows HTTP traffic on port 80. A properly configured firewall permits this traffic. Why does the organization still need an IDS/IPS?"
  type: multiple-choice
  options:
    - "Firewalls are hardware devices and cannot be updated with new security rules quickly enough"
    - "Firewalls enforce policies about who can communicate with whom, but cannot inspect payload content — a SQL injection attack embedded in a valid HTTP request passes freely through a firewall"
    - "IDS/IPS monitors network traffic for performance degradation that firewalls ignore"
    - "Firewalls only work at the network perimeter, while IDS/IPS also monitor internal traffic"
  answer: 1
  explanation: "Firewalls operate at the network/transport layer, filtering by IP address, port, and protocol. They are blind to the content of permitted traffic. A SQL injection attack, a cross-site scripting payload, or malware download embedded in an HTTP request is invisible to a firewall that allows HTTP on port 80. IDS/IPS perform deep packet inspection, analyzing payload content and behavioral patterns to detect malicious activity within otherwise permitted sessions. Firewalls and IDS/IPS are complementary controls, not substitutes."

- question: "Anomaly-based IDS is strictly superior to signature-based IDS because it can detect novel attacks that have no known signature."
  type: true-false
  answer: false
  explanation: "Anomaly-based detection has a critical weakness: it generates many false positives. Any legitimate but unusual activity — a backup job at an unexpected time, a software update causing a traffic spike, a new application deployment — can look anomalous against the learned baseline. Signature-based detection is highly accurate for known attack patterns (low false positives) but blind to new ones. Neither approach dominates the other; they address different threat classes. Production security systems deploy both, feeding alerts into a SIEM for correlation."

- question: "A network-based IDS (NIDS) can detect attacks concealed within TLS-encrypted HTTPS traffic by performing signature matching on the packet payloads."
  type: true-false
  answer: false
  explanation: "Encrypted traffic is opaque to NIDS payload inspection. TLS encrypts the application-layer content so that only the endpoints (client and server) can read it. A NIDS sees only ciphertext in the payload and cannot apply signature-based rules to it. NIDS can still analyze metadata — connection timing, volume, source/destination patterns — but payload signatures are ineffective against encrypted traffic. Host-based IDS (HIDS), running on the server, can inspect traffic after decryption at the application layer and is not subject to this limitation."

- question: "Explain the difference between IDS and IPS in terms of network placement and what this means for both their defensive capability and operational risk."
  type: short-answer
  answer: "An IDS monitors a *copy* of network traffic — delivered via a network tap or switch port mirror — and operates out-of-band. It can generate alerts but cannot block anything. An IPS sits *inline* on the network path, meaning all traffic physically flows through it. When the IPS identifies malicious traffic, it can drop the packets, reset the connection, or block the source in real time before the attack reaches its target. The placement difference creates an asymmetric risk profile: the IDS's out-of-band position means failures and false positives have no operational impact, but it cannot stop attacks in progress. The IPS's inline position enables active defense but makes false positives operationally damaging (legitimate traffic is blocked) and introduces a potential single point of failure — if the IPS goes down or becomes a bottleneck, it can disrupt the entire network."
  explanation: "This tradeoff explains why organizations often deploy IDS first, tune the detection rules, and only switch to IPS blocking mode after validating that the false positive rate is acceptably low. The inline position converts detection errors into disruptions, so operational risk must be managed before enabling blocking."
```

## Explainer

From network security fundamentals, you understand that firewalls filter traffic based on rules about addresses, ports, and protocols. But firewalls are blunt instruments — they enforce policies about *who* can talk to *whom*, not about *what* is being said. A firewall that allows HTTP traffic on port 80 will happily pass through a SQL injection attack embedded in a valid HTTP request. **Intrusion Detection Systems** (IDS) and **Intrusion Prevention Systems** (IPS) fill this gap by inspecting the *content* and *behavior* of network traffic to identify malicious activity.

An **IDS** monitors network traffic (or host activity) and generates alerts when it detects something suspicious. It operates in two fundamental modes. **Signature-based detection** maintains a database of known attack patterns — specific byte sequences, packet structures, or protocol anomalies that correspond to known exploits. When traffic matches a signature, the IDS flags it. This is analogous to antivirus scanning: it is highly accurate for known threats (low false positives) but completely blind to novel attacks not yet in the database (high false negatives). **Anomaly-based detection** instead builds a model of "normal" traffic — typical bandwidth usage, protocol distributions, connection patterns — and flags deviations from that baseline. This can catch zero-day attacks and insider threats that have no known signature, but it generates more false positives because legitimate but unusual activity (a backup job, a software update, a traffic spike) can look anomalous.

The critical distinction between IDS and **IPS** is *placement* and *action*. An IDS typically operates passively — it monitors a copy of the traffic (via a network tap or port mirror) and alerts administrators, but it does not block anything. An IPS sits **inline** on the network path, meaning all traffic flows through it. When the IPS detects an attack, it can actively **drop the malicious packets**, reset the connection, or block the source IP — in real time, before the attack reaches its target. This inline position gives the IPS defensive power but also introduces risk: false positives cause legitimate traffic to be blocked, and the IPS itself becomes a potential bottleneck and single point of failure.

Deployment comes in two forms. A **network-based** IDS/IPS (NIDS/NIPS) monitors traffic at a network chokepoint — typically at the perimeter or between network segments. A **host-based** IDS/IPS (HIDS/HIPS) runs on individual servers, monitoring system calls, file changes, log entries, and local network connections. The two approaches are complementary: NIDS catches attacks traversing the network, while HIDS catches attacks that originate locally or that encrypted network traffic conceals from NIDS. Modern security operations typically deploy both, feeding alerts into a centralized **SIEM** (Security Information and Event Management) system for correlation and response.
