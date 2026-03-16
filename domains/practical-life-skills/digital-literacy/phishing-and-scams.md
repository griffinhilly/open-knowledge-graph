---
id: phishing-and-scams
title: Phishing and Online Scams
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: internet-safety-basics
  type: hard
- id: email-fundamentals
  type: soft
builds-toward:
- digital-privacy-fundamentals
tags:
- phishing
- scams
- fraud
- social-engineering
stage: concrete-operations
status: validated
---

# Phishing and Online Scams

## Core Idea
Phishing is a social engineering attack where an attacker impersonates a trusted entity — a bank, employer, or government agency — to trick you into revealing credentials, clicking malware links, or transferring money. Attacks arrive via email, text (smishing), phone (vishing), and social media. The tell-tale signs are urgency, mismatched URLs, spelling errors, and requests for sensitive information that legitimate organizations never make.

## How It's Best Learned
Walk through real phishing email examples and identify the specific red flags in each. Practice hovering over links to inspect the real URL before clicking.

## Common Misconceptions
- Phishing can target anyone, not just the technologically naive — highly convincing spear-phishing targets executives and professionals.
- A familiar-looking email address does not mean the sender is legitimate; display names are trivially spoofed.
- Banks and government agencies will never ask for your password or full Social Security number via email.

## Explainer

Phishing works because it exploits trust, not technical ignorance. You already know from internet safety basics that not every website or email is what it claims to be. Phishing is the systematic exploitation of that gap — attackers craft messages that look exactly like ones from your bank, your employer, or a government agency, then use psychological pressure to make you act before you think. The attack doesn't need to bypass your antivirus; it needs to bypass you.

The core mechanism is **social engineering**: manipulating human behavior rather than breaking technical systems. The most effective phishing messages share a common structure — they establish a credible sender identity, create urgency or fear ("Your account will be suspended in 24 hours"), and offer a clear action that feels safe but isn't (clicking a link that leads to a fake login page). Each element is designed to suppress your skepticism. Urgency is the most powerful lever: when you feel rushed, you're less likely to pause and inspect the details.

The technical tells are learnable with practice. **URL inspection** is your most reliable tool: hover over any link before clicking and read the actual destination, not the display text. Phishers use tricks like `paypal.com.attacker.net` (where `attacker.net` is the actual domain), character substitutions like `paypa1.com`, or long URLs designed to bury the real domain at the end. **Email headers** can reveal spoofed senders — a message may display as "Bank of America Support" but originate from `support@totally-not-bank.ru`. And while spelling errors are a classic tell, sophisticated spear-phishing attacks — those targeted at specific individuals using personal information — may have none.

**Spear-phishing** represents the evolution beyond mass phishing. Where a generic phishing email goes to millions of people hoping a few will bite, spear-phishing is tailored to you: it may reference your employer, your recent purchase, or your colleague's name (harvested from LinkedIn or a data breach). This is why the "I'd recognize a scam" confidence is dangerous — the most convincing attacks are designed for you specifically. The defense is behavioral: slow down, verify through a separate channel (call the bank directly using a number from their official website, not one in the email), and remember that any legitimate organization will wait for you to verify before taking action.
