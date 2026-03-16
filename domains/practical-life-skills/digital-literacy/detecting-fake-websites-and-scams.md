---
id: detecting-fake-websites-and-scams
title: Detecting Fake Websites and Online Scams
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: website-anatomy-and-links
  type: hard
- id: evaluating-source-credibility-online
  type: hard
builds-toward:
- keeping-yourself-safe-online
tags:
- security
- fraud
- credibility
stage: abstract-reasoning
status: draft
---

# Detecting Fake Websites and Online Scams

## Core Idea
Fake websites mimic legitimate ones to steal credentials or money. Red flags include subtle URL misspellings, missing HTTPS security indicators, poor design quality, unrealistic offers, and pressure to act immediately. Always navigate to official websites by typing the address directly.

## Explainer

From your study of website anatomy, you know that a URL has a specific structure — protocol, domain, path, and query parameters — and that every element carries meaning. From evaluating source credibility, you know that not all online content is equally trustworthy and that surface appearance (professional-looking design) does not equal legitimate authority. Detecting fake websites is the application of both skills under adversarial conditions: someone has deliberately designed a page to fool you, and the question is which signals survive the deception.

The **domain name** is the highest-value signal to check. Attackers use a technique called **typosquatting** — registering domains that look almost identical to legitimate ones but differ by one character: `paypa1.com` instead of `paypal.com`, `arnazon.com` instead of `amazon.com`, or `bankofamerica.com.support-login.net` (where the actual domain is `support-login.net`, not `bankofamerica.com`). That last pattern — a trusted brand name appearing as a subdomain of an attacker's real domain — is especially deceptive and extremely common. Always read the domain from right to left, stopping at the first slash: the real domain is the part immediately before the first `/`, and everything before it is a subdomain that anyone can create.

**HTTPS** (the padlock icon) tells you the connection is encrypted — nobody can intercept the data in transit. What it does not tell you is that the site on the other end is legitimate. Fake websites routinely use HTTPS. A padlock means your credentials are securely transmitted to the attacker; the encryption is working perfectly, just not in your favor. HTTPS is a necessary but not sufficient condition for trust. Its absence is a strong red flag; its presence is not a green light.

**Content and behavior signals** round out the detection toolkit. Fake sites often have inconsistent fonts, blurry logos, low-quality images, grammar errors, and links that go nowhere or loop back to the same page. **Urgency tactics** — "Your account will be suspended in 24 hours," "Only 2 left in stock at this price," "Claim your prize now" — are engineered to prevent you from pausing to think critically. Legitimate institutions do not demand immediate action that bypasses normal channels. The safest habit for high-stakes actions (banking, shopping, entering passwords) is to navigate directly by typing the known URL rather than clicking any link — from an email, search result, or ad — that claims to take you there.
