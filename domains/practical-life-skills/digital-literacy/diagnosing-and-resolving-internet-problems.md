---
id: diagnosing-and-resolving-internet-problems
title: Diagnosing and Resolving Internet Connection Problems
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: internet-connectivity-basics
  type: hard
- id: basic-computer-troubleshooting
  type: hard
builds-toward:
- getting-help-troubleshooting
tags:
- troubleshooting
- networking
- connectivity
stage: abstract-reasoning
status: validated
---

# Diagnosing and Resolving Internet Connection Problems

## Core Idea
Internet problems can originate from your device, your router, your Internet Service Provider, or the website you're accessing. Methodical troubleshooting—checking connection status, restarting devices, testing different networks—helps identify the root cause and solution.

## Questions

```yaml
- question: "Your laptop cannot reach the internet. Your phone on the same WiFi network works fine. What should you investigate FIRST?"
  type: multiple-choice
  options:
    - "Restart your modem and router in the correct sequence"
    - "Contact your ISP to report an outage"
    - "Check your laptop's WiFi settings and network connection — the problem is specific to that device"
    - "Check downdetector.com to see if the website you're visiting is down"
  answer: 2
  explanation: "When one device fails but others on the same network work, the failure is isolated to the device — not the router, modem, or ISP. Those shared components serve all devices equally; if they were broken, all devices would fail. Investigating the laptop's WiFi settings, network adapter, and connection status is the correct first step. Restarting the router (option A) would be appropriate if no devices could connect."

- question: "You've restarted your modem and router in the correct sequence. Internet still doesn't work. Downdetector.com shows no widespread outages for any site you try. A speed test shows near-zero speed despite your router showing a successful connection status. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "Your WiFi password has changed and your devices are connecting to an unauthenticated network"
    - "Your DNS server is misconfigured, preventing name resolution"
    - "Your ISP connection itself may be disrupted — contact your provider with the speed test result as evidence"
    - "Your router needs to be replaced"
  answer: 2
  explanation: "Near-zero speed despite a successful connection status means traffic is not actually flowing through the ISP link. This is distinct from DNS problems (option B), which would cause name resolution failures but normal speeds when connecting by IP address. A speed test near zero with the router showing 'connected' points to the ISP layer — the link is reported up but data isn't moving. Contacting the ISP with specific evidence (speed test numbers) is more productive than vague complaints."

- question: "If all devices on a home network lose internet access simultaneously, the problem is upstream of the devices — in the router, modem, or ISP — rather than in any individual device."
  type: true-false
  answer: true
  explanation: "This is the core logic of chain-of-failure isolation. Each device connects to the network independently, so a problem affecting all devices simultaneously cannot be in any individual device. The failure must be at a shared component: the WiFi access point, the router, the modem, or the ISP link. Knowing this immediately narrows where to look and what to test next — hardware restart rather than device-specific settings."

- question: "When restarting network equipment, it is fine to restart the modem and router simultaneously because the order in which they come back online does not affect the result."
  type: true-false
  answer: false
  explanation: "The restart sequence matters. The modem must come up first and fully establish its connection to the ISP before the router is powered on, because the router needs to acquire a valid IP address and configuration from the modem (or ISP) at startup. If the router comes up before the modem is ready, it may acquire a stale or invalid configuration and continue to fail even though the hardware is physically running. The correct sequence: modem on → wait 1-2 minutes → router on → wait → reconnect devices."

- question: "Why is asking 'can multiple devices access the internet?' the best first diagnostic step when troubleshooting a connection problem?"
  type: short-answer
  answer: "It immediately isolates which segment of the chain has failed. If only one device can't connect, the problem is in that device — not the shared network infrastructure. If no devices can connect, the problem is upstream in the router, modem, or ISP. This single question rules out half the possible failure points before touching any hardware or settings, making every subsequent step more targeted and efficient."
  explanation: "Good troubleshooting is about narrowing the problem space as quickly as possible. The device-vs-network question is the single most efficient branch point because it divides the entire chain into two distinct halves. Starting here prevents the common mistake of restarting routers and modems when the actual problem is a disabled WiFi adapter on a single laptop — or vice versa, spending time on device settings when the ISP is down."
```

## Explainer

From your understanding of how internet connectivity works — device, router, modem, ISP, and the wider internet — you already know the chain of systems your data travels through. When something breaks, the key insight is that this chain has distinct segments, and each segment can fail independently. **Diagnostic thinking** means isolating which segment is the problem, rather than randomly restarting things and hoping one restart fixes it.

Start with the simplest test: **can multiple devices access the internet?** If your phone works fine but your laptop cannot connect, the problem is in your device — not your router, not your ISP. Check whether WiFi is enabled, whether you are connected to the right network, and whether your device's network settings have been changed. If no devices can connect, the problem is upstream of all of them. The next question: can you reach your router? Disconnect from WiFi and use an ethernet cable directly from the router to your laptop — if this works, your WiFi is the issue (restart the router). If ethernet also fails, the router itself or your ISP connection is broken.

The **restart sequence** exists because network devices accumulate state — IP address leases expire, firmware gets into inconsistent states, memory fills up — and powering off clears all of that. The correct sequence matters: turn off your modem first, then router, then devices. Wait 30 seconds for the modem to fully clear. Power on modem first, wait for it to connect to the ISP (usually 1–2 minutes), then power on the router, then reconnect your devices. Restarting in the wrong order, or not waiting between steps, can result in the router acquiring a stale configuration.

When the hardware restart does not help, **narrow the problem geographically**. Visit a website like downdetector.com (or simply search "[website name] down") to check if the site you're trying to reach is having widespread problems — if so, this is not your issue to fix. Run a speed test to confirm your connection is actually reaching the internet. If speed is near zero despite a successful connection status, your ISP link may be throttled or disrupted — contact your provider with this evidence. If speed is normal but specific sites fail, the problem may be DNS (your device's ability to translate names like "google.com" into IP addresses); switching to a public DNS server (such as 8.8.8.8) is a quick diagnostic test. Each of these steps rules out one layer of the chain, systematically converging on the true cause.
