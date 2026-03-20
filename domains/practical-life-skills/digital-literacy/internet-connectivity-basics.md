---
id: internet-connectivity-basics
title: Internet Connectivity Basics
domain: practical-life-skills
course: digital-literacy
prerequisites: []
builds-toward:
- web-browser-essentials
- wifi-and-network-basics
tags:
- internet
- connectivity
- networks
- wifi
- broadband
stage: concrete-operations
status: draft
---

# Internet Connectivity Basics

## Core Idea
The internet is a global network of computers that communicate through standardized protocols. To access it, you need a device, a connection method (broadband, WiFi, mobile data), and an Internet Service Provider (ISP). Understanding how you connect, connection types, and basic network security helps you troubleshoot issues and protect your information.

## How It's Best Learned
Check your own internet connection settings and identify your provider, connection type, and signal strength. Test your connection speed and learn what factors affect it.

## Common Misconceptions
- WiFi and the internet are the same thing—WiFi is just one way to connect.
- A faster internet speed always makes websites load faster.
- You're completely safe if your WiFi is password-protected.

## Questions

```yaml
- question: "Your laptop shows 'Connected to WiFi' but no websites will load. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "WiFi and the internet are the same, so if WiFi is connected, the internet must be working"
    - "Your WiFi password is wrong — reconnect with the correct credentials"
    - "WiFi connects your device to the local router, but the router has lost its path to the internet beyond it"
    - "Your browser must be broken — try restarting it"
  answer: 2
  explanation: "WiFi only covers the link between your device and your local router — nothing more. 'Connected to WiFi' means your device successfully reached the router. Whether the router has a working internet connection is a separate question. The router could have lost contact with the ISP (modem issue, service outage, unpaid bill), leaving you connected locally but cut off from the internet. This is one of the most common troubleshooting situations, and understanding the chain (device → router → modem → ISP → internet) tells you where to look."

- question: "Which home internet connection type typically provides the highest speeds and most reliable signal?"
  type: multiple-choice
  options:
    - "DSL — it uses the existing telephone network, which is extremely reliable"
    - "Cable — coaxial TV cables always outperform every other technology"
    - "Mobile data (5G) — cellular towers are the most modern infrastructure"
    - "Fiber — light pulses through glass cables offer the highest bandwidth and most stable signal"
  answer: 3
  explanation: "Fiber-optic connections transmit data as light through glass cables, with far greater bandwidth potential and signal stability than copper-based alternatives (DSL, cable). DSL uses phone lines and is the slowest, often relegated to rural areas. Cable is fast and widely available but shares bandwidth with neighbors, causing congestion. 5G mobile data can be fast but fluctuates with tower load and physical obstacles. Fiber is currently the gold standard for home internet, though availability varies by region."

- question: "A WiFi password using WPA2 encryption prevents unauthorized devices from joining your local network, which means your internet connection is secure from all outside threats."
  type: true-false
  answer: false
  explanation: "A WiFi password only controls who can join your local network — it prevents strangers from connecting to your router and using your bandwidth or seeing local traffic. It does nothing against threats that operate at higher levels: a phishing email, a malicious website, or malware you download all bypass WiFi security entirely because they reach you through the internet connection itself, which your password-protected WiFi happily carries. Think of the WiFi password as locking the front door — necessary, but not a substitute for security inside the house."

- question: "Your router can show all devices as 'connected' while you have no internet access, because WiFi connectivity and internet connectivity are two separate things."
  type: true-false
  answer: true
  explanation: "WiFi is just the wireless link between devices and the router — the local network. The router connects to the internet through a modem and your ISP. If the modem loses connection, or the ISP has an outage, or the router's WAN port fails, all your devices can still connect to each other over WiFi but none can reach the internet. The status 'connected to WiFi' means the device-to-router link works; it says nothing about the router-to-internet link."

- question: "Explain the difference between WiFi and the internet. Why can you be 'connected to WiFi' but still have no internet access?"
  type: short-answer
  answer: "WiFi is the wireless technology that connects your device to your local router — it's the on-ramp to your home network. The internet is the global network that exists beyond your router, accessed through your modem and ISP. A 'Connected to WiFi' status only means your device reached the router. If the router has no working path to the internet (ISP outage, modem failure, etc.), you have local network access but no internet access."
  explanation: "The device → router → modem → ISP → internet chain has multiple independent links, each of which can fail. WiFi status only confirms the first link. Knowing this lets you troubleshoot: if WiFi is connected but internet is down, the problem is downstream of the router — check the modem, call the ISP, or power-cycle the router. If WiFi itself is failing, the problem is between your device and the router."
```

## Explainer

The internet is a system of interconnected networks, and connecting to it always involves a chain of distinct steps. Your device (phone, laptop) connects to a **local network** — either by WiFi (wireless) or ethernet (wired cable). That local network connects through a **router** to a **modem**, which connects to your **Internet Service Provider (ISP)** — a company like Comcast, AT&T, or a local cable provider. Your ISP connects to the broader internet, a global web of routers and fiber-optic cables linking millions of networks worldwide. Understanding this chain matters because each link can fail independently, and knowing which link failed is the key to fixing it.

**WiFi** is specifically the technology for the wireless connection between your device and your local router — nothing more. Your router could be connected to an internet service, or it might not be. This is why your laptop can show "Connected to WiFi" while still having no internet access: your device reached the router successfully, but the router has no path to the internet. The internet is what lives beyond your router; WiFi is just the on-ramp to your local network.

**Connection types** vary in how they deliver your connection from the ISP to your home. **Broadband** is the general term for high-speed connections. **Cable internet** (most common in the US) sends data over coaxial TV cables — fast and widely available. **Fiber** uses light pulses through glass cables — the fastest and most reliable. **DSL** uses telephone lines — slower, often in rural areas. **Mobile data** (4G/5G) uses cell towers — convenient but shared bandwidth means it slows when towers are congested. Each has different speed limits and reliability characteristics. Your ISP plan specifies a maximum speed (e.g., 200 Mbps download), but actual speed depends on network congestion, distance to the ISP's equipment, and your hardware.

**Network security** is a layered problem, not a switch you can flip. A password on your WiFi network (using WPA2 or WPA3 encryption) prevents unauthorized devices from joining your network — this is the basic minimum. But it does not protect you from threats that operate at higher levels: malicious websites, phishing emails, or software you install. Password protection means "strangers on the street can't see your network traffic or use your bandwidth"; it does not mean your device is secure from everything. Think of it as locking the front door of your house — necessary, but not a substitute for locking your valuables or being careful about who you let in.
