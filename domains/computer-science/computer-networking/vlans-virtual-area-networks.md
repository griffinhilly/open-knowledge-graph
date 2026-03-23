---
id: vlans-virtual-area-networks
title: VLANs (Virtual Local Area Networks)
domain: computer-science
course: computer-networking
prerequisites:
- id: switching-basics
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- vlan
- segmentation
- layer-2
- traffic-isolation
stage: advanced
status: validated
---

# VLANs (Virtual Local Area Networks)

## Core Idea
A VLAN is a logical subdivision of a physical network that isolates traffic at Layer 2, allowing multiple broadcast domains to coexist on one switch. VLANs are identified by VLAN IDs (1–4094) and enable traffic segregation for security, performance, and administrative purposes without requiring separate physical switches.

## How It's Best Learned
Configure VLANs on a managed switch or in a network simulator; test that frames in different VLANs cannot communicate directly at Layer 2, and observe how a router enables inter-VLAN routing.

## Common Misconceptions
- VLANs provide security; they only segment Layer 2 traffic and can be bypassed by a determined attacker—security requires Layer 3 firewalls.
- VLANs eliminate the need for routers; they require routers or multi-layer switches to route between VLANs.

## Questions

```yaml
- question: "A university puts student devices on VLAN 200 and a file server on VLAN 300. Students report they cannot access the file server. What is most likely needed?"
  type: multiple-choice
  options:
    - "The file server's VLAN ID must be changed to 200 to match the student VLAN"
    - "A router or Layer 3 switch must be configured to route traffic between VLAN 200 and VLAN 300"
    - "The trunk port connecting the switches must be reconfigured as an access port"
    - "Students' devices must have statically assigned IP addresses within the VLAN 300 subnet"
  answer: 1
  explanation: "VLANs are separate Layer 2 broadcast domains — devices in different VLANs cannot communicate at Layer 2 even if they share the same physical switch. Just as traffic between two physically separate networks requires a router, traffic between VLANs requires inter-VLAN routing: a router or Layer 3 switch must have an interface in both VLANs and forward packets between them. Changing VLAN IDs (option A) would break other things; trunk ports carry multiple VLANs but do not route between them; IP addressing alone (option D) does not enable routing."

- question: "A network administrator says 'We put our accounting department on its own VLAN to keep their financial data secure from other users.' What is the most significant gap in this security model?"
  type: multiple-choice
  options:
    - "VLANs are only available on expensive enterprise switches, making cost-effective implementations impractical"
    - "VLAN segmentation is a Layer 2 control — a determined attacker with switch access could use VLAN-hopping techniques, and any inter-VLAN traffic is fully visible at the router where policy enforcement is needed anyway"
    - "VLANs cannot be used for security because 802.1Q tags can be stripped in transit by any device"
    - "The accounting VLAN will have degraded performance because all traffic must traverse extra switches"
  answer: 1
  explanation: "VLANs provide Layer 2 isolation but not true security. VLAN-hopping attacks (exploiting misconfigured trunk ports) can let an attacker reach other VLANs. More fundamentally, any traffic that crosses between the accounting VLAN and other systems must pass through a router, which must apply access control lists and firewall rules to enforce security policy. Real security requires Layer 3 controls, not just VLAN assignment. VLANs are a segmentation and performance tool that complements security — they are not themselves a security boundary."

- question: "A trunk port connecting two managed switches carries traffic for only the VLAN assigned to that port."
  type: true-false
  answer: false
  explanation: "This describes an *access* port, not a trunk port. An access port belongs to exactly one VLAN and connects to end devices. A *trunk* port carries traffic for multiple VLANs simultaneously between switches, using 802.1Q VLAN tagging — each frame gets a header inserted that identifies its VLAN ID, allowing the receiving switch to correctly forward or filter it. Trunk ports are what make it possible to span a single VLAN across multiple physical switches and carry many VLANs over one physical link."

- question: "Two computers assigned to the same VLAN but connected to different physical switches can communicate at Layer 2, provided a trunk port links the switches."
  type: true-false
  answer: true
  explanation: "VLANs are logical, not physical. The trunk port carries 802.1Q-tagged frames for all configured VLANs. When a frame arrives at the second switch with the VLAN tag of the shared VLAN, the switch forwards it to ports belonging to that VLAN. This allows a single logical broadcast domain to span an entire campus network. The VLAN ID in the tag maintains isolation — frames tagged for VLAN 10 are never forwarded to ports assigned to VLAN 20."

- question: "Why do VLANs reduce broadcast traffic in large networks, and why does this matter for performance?"
  type: short-answer
  answer: "A broadcast frame (such as an ARP request) is forwarded to every port in the same broadcast domain. Without VLANs, a single large switch places all ports in one broadcast domain — every broadcast reaches every device, which must process and discard it. VLANs partition the switch into smaller broadcast domains, so a broadcast from a device on VLAN 10 reaches only other VLAN 10 devices. In large networks with hundreds of devices, unconstrained broadcasts consume significant bandwidth and CPU time on every endpoint. VLANs limit this blast radius, reducing unnecessary traffic and processing overhead."
  explanation: "Broadcast reduction was one of the original motivations for VLANs. Protocols like ARP, DHCP, and NetBIOS generate substantial broadcast traffic; containing them to logically relevant groups (one VLAN per subnet) is essential for network scalability at enterprise scale."
```

## Explainer

From your study of switching basics, you know that a switch learns which MAC addresses are reachable on which ports and forwards frames accordingly. By default, every port on a switch belongs to the same **broadcast domain** — when any device sends a broadcast frame (like an ARP request), every other device on the switch receives it. In a small network this is fine, but in a building with hundreds of devices, broadcast storms can saturate the network and every device wastes CPU processing irrelevant broadcasts. **VLANs** solve this by letting you partition a single physical switch into multiple independent broadcast domains.

Think of a VLAN as a virtual wall inside the switch. Ports assigned to VLAN 10 can only communicate at Layer 2 with other ports on VLAN 10 — they cannot see or be seen by ports on VLAN 20, even though they share the same physical hardware. Each VLAN gets a numeric **VLAN ID** (1–4094), and you assign switch ports to VLANs through configuration. An **access port** belongs to exactly one VLAN and connects to end devices (computers, printers). A **trunk port** carries traffic for multiple VLANs simultaneously between switches, using 802.1Q tagging — each frame on the trunk gets a small header inserted that identifies which VLAN it belongs to, so the receiving switch knows where to deliver it.

The practical benefits are immediate. A university can put all faculty devices on VLAN 100 and all student devices on VLAN 200, even if faculty and student offices are on the same floor and plugged into the same switch. The two groups are completely isolated at Layer 2 — a broadcast from a student's laptop never reaches faculty machines. This reduces broadcast traffic, improves performance, and limits the blast radius of network problems. If a student's machine gets infected with malware that floods the network, only VLAN 200 is affected.

Critically, VLANs alone do not allow communication between groups — that requires **inter-VLAN routing**. Since VLANs are separate broadcast domains, traffic from VLAN 100 to VLAN 200 must pass through a router or a Layer 3 switch, just as traffic between two physically separate networks would. This is often done with a "router on a stick" configuration, where a single router interface uses 802.1Q sub-interfaces to route between VLANs. The router becomes the policy enforcement point where you can apply access control lists and firewall rules, giving you both segmentation and controlled inter-segment communication.
