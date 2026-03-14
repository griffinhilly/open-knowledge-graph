---
id: network-function-virtualization-nfv
title: Network Function Virtualization (NFV)
domain: computer-science
course: computer-networking
prerequisites:
- id: software-defined-networking
  type: hard
- id: network-virtualization-network-slicing
  type: hard
builds-toward:
- network-management-and-monitoring
- qos-quality-of-service
tags:
- sdn
- nfv
- virtualization
- cloud-networking
stage: advanced
status: draft
---

# Network Function Virtualization (NFV)

## Core Idea
Network Function Virtualization (NFV) runs network functions (firewalls, load balancers, NAT, DPI) as software on general-purpose compute infrastructure instead of dedicated hardware appliances. NFV reduces capital expenditure and deployment time, enabling rapid scaling and service chaining. Service Function Chaining (SFC) defines how packets traverse a sequence of VNFs.

## How It's Best Learned
Deploy VNFs (e.g., open vSwitch, VyOS) on KVM or Docker. Configure service chaining using segment routing or encapsulation. Monitor VNF resource consumption and scaling behavior. Test failure recovery and traffic rerouting.

## Common Misconceptions
NFV is not the same as SDN; NFV virtualizes network functions while SDN virtualizes control. VNFs require careful resource provisioning; they are not infinitely scalable. Service chaining adds latency; performance tuning is essential.
