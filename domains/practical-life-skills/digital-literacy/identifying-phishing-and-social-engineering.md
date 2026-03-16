---
id: identifying-phishing-and-social-engineering
title: Identifying Phishing and Social Engineering Attempts
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: phishing-and-scams
  type: hard
- id: email-security-and-professional-tone
  type: soft
builds-toward:
- recognizing-online-scams-fraud
- keeping-yourself-safe-online
tags:
- security
- fraud
- social-engineering
stage: formal-systems
status: draft
---

# Identifying Phishing and Social Engineering Attempts

## Core Idea
Phishing emails impersonate trusted organizations to trick you into clicking malicious links or revealing credentials. Red flags include artificial urgency, mismatched sender addresses, generic greetings, spelling errors, and any requests for passwords or sensitive financial information.

## Explainer

You've already studied phishing as a category of online threat. Now the focus sharpens to recognition: what specific signals, in real messages, distinguish a legitimate communication from an attack? **Social engineering** is the broader discipline — manipulating people psychologically rather than technically to gain access or information. Phishing is social engineering delivered through electronic communication (email, SMS, voice calls, even social media messages). The attack works not by breaking cryptography but by exploiting human psychology: trust, urgency, fear, and authority.

The most reliable technical signal is the **sender address**. Email display names are trivially spoofed — any attacker can send an email that shows "PayPal Security Team" as the visible sender name. What matters is the actual address in the `From` field. Look past the display name: `PayPal Security Team <support@paypa1-alerts.com>` is not from PayPal. The domain part (after the @) must match the legitimate organization's actual domain. Closely inspect for the same typosquatting techniques as fake websites — one character substitution, added words like `-alerts` or `-secure`, or legitimate-looking subdomains. In SMS phishing (smishing) and social media messages, there is no sender address to inspect, which makes these vectors more dangerous and context more important.

**Urgency and fear** are the psychological levers that make phishing effective. A message claiming your account has been compromised, your package couldn't be delivered, or a charge is pending on your card exploits your desire to resolve the problem immediately. This urgency is manufactured specifically to prevent you from pausing to verify. The tell is that the urgency arrives unsolicited — you did not initiate a transaction, request a password reset, or contact support. Legitimate institutions also rarely demand action within hours, and they never ask you to provide your password, full credit card number, or Social Security number via email.

**Generic greetings** ("Dear Customer," "Dear User," "Hello Friend") indicate the attacker does not know your name — they are broadcasting to millions of addresses hoping some will respond. Legitimate communications from organizations you have accounts with almost always address you by name. Spelling and grammar errors, while less reliable than they once were (AI tools have improved attacker writing quality), are still diagnostic — a security alert from a major bank will be proofread. Finally, hover over any link before clicking it (on desktop, the destination appears in the browser status bar): the visible text may say `https://paypal.com` while the actual hyperlink leads somewhere entirely different. If any of these signals appear, verify through an independent channel — go directly to the organization's official website or call the number on the back of your card — never through the link or contact information provided in the suspicious message.
