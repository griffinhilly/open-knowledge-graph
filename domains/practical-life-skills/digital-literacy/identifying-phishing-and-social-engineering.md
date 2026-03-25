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
- id: detecting-fake-websites-and-scams
  type: soft
- id: recognizing-online-scams-fraud
  type: soft
- id: safe-downloads-and-source-verification
  type: soft
- id: operating-system-updates
  type: soft
- id: software-installation-management
  type: soft
builds-toward:
- recognizing-online-scams-fraud
- keeping-yourself-safe-online
tags:
- security
- fraud
- social-engineering
stage: formal-systems
status: validated
---
# Identifying Phishing and Social Engineering Attempts

## Core Idea
Phishing emails impersonate trusted organizations to trick you into clicking malicious links or revealing credentials. Red flags include artificial urgency, mismatched sender addresses, generic greetings, spelling errors, and any requests for passwords or sensitive financial information.

## Questions

```yaml
- question: "You receive an email with the display name 'PayPal Security Team' warning that your account has been locked. The From field shows: PayPal Security Team <support@paypa1-alerts.com>. Which signal is the most reliable indicator that this is phishing?"
  type: multiple-choice
  options:
    - "The urgent tone about your account being locked"
    - "The domain 'paypa1-alerts.com' does not match PayPal's actual domain"
    - "The email includes a link to click to restore access"
    - "The message arrived unsolicited without you contacting PayPal first"
  answer: 1
  explanation: "The domain is the most technically reliable indicator. Display names are trivially spoofed — any sender can put any name in that field. But the actual domain in the From address (paypa1-alerts.com — note the digit '1' replacing the letter 'l') is not PayPal's real domain. Urgency and unsolicited arrival are also warning signs, but they are psychological signals that could appear in legitimate communications (fraud alerts, for example). A mismatched or typosquatted domain is a nearly definitive technical signal."

- question: "You receive a suspicious email claiming your bank account was compromised. The email includes a toll-free phone number to call immediately. What is the safest response?"
  type: multiple-choice
  options:
    - "Call the number in the email — it is safer than clicking a link"
    - "Reply to the email asking for proof of identity before calling"
    - "Go directly to your bank's official website and find the support number there, then call that number"
    - "Forward the email to your bank's email address listed in the suspicious message"
  answer: 2
  explanation: "Attackers include fake phone numbers and email addresses in phishing messages — calling or replying via the contact info in the message connects you to the attacker, not your bank. The only safe verification path is through an independent channel you locate yourself: type your bank's URL directly into a browser, or call the number on the back of your physical bank card. Never use links, phone numbers, or email addresses provided in the suspicious message itself."

- question: "A phishing email that addresses you by your real name (e.g., 'Dear Griffin') is probably legitimate, since attackers only know your email address and use generic greetings."
  type: true-false
  answer: false
  explanation: "False. Data breaches regularly expose names, email addresses, and other personal information. Attackers can purchase or obtain breach databases and craft personalized messages using your real name — a technique called 'spear phishing.' A personalized greeting makes a message feel more trustworthy, but it is not evidence of legitimacy. Always evaluate the sender domain and any links independently, regardless of how personalized the greeting appears."

- question: "The artificial urgency in phishing messages — 'Your account will be suspended in 24 hours!' — is deliberately designed to prevent you from pausing to verify the message's legitimacy."
  type: true-false
  answer: true
  explanation: "True. This is the core psychological mechanism of social engineering. Urgency bypasses deliberate reasoning: when you feel you must act immediately, you are less likely to stop and verify independently. Legitimate institutions rarely demand action within hours on security matters, and they never ask for your password or full account credentials via email. Any message that creates extreme time pressure around sensitive information should be treated as a red flag, not as a reason to act faster."

- question: "Why does the display name in an email's 'From' field provide almost no security value, and what should you examine instead?"
  type: short-answer
  answer: "The display name is arbitrary — any sender can set it to any text, including 'PayPal Security Team' or 'Your Bank.' It requires no verification and can be changed trivially. What matters is the actual email address (specifically the domain after the @), which is harder to fake and must be inspected for typosquatting, extra words, or character substitutions. For SMS and social media messages where there is no visible domain to inspect, context and independent verification become even more critical."
  explanation: "Email protocols separate the display name (cosmetic) from the actual sending address (functional). Attackers exploit this separation: the envelope shows whatever name builds trust, while the actual origin domain reveals the deception. Checking the domain defeats the most common spoofing technique. When in doubt, verify through an independent channel — navigate to the organization's official site yourself rather than using any contact information in the suspicious message."
```

## Explainer

You've already studied phishing as a category of online threat. Now the focus sharpens to recognition: what specific signals, in real messages, distinguish a legitimate communication from an attack? **Social engineering** is the broader discipline — manipulating people psychologically rather than technically to gain access or information. Phishing is social engineering delivered through electronic communication (email, SMS, voice calls, even social media messages). The attack works not by breaking cryptography but by exploiting human psychology: trust, urgency, fear, and authority.

The most reliable technical signal is the **sender address**. Email display names are trivially spoofed — any attacker can send an email that shows "PayPal Security Team" as the visible sender name. What matters is the actual address in the `From` field. Look past the display name: `PayPal Security Team <support@paypa1-alerts.com>` is not from PayPal. The domain part (after the @) must match the legitimate organization's actual domain. Closely inspect for the same typosquatting techniques as fake websites — one character substitution, added words like `-alerts` or `-secure`, or legitimate-looking subdomains. In SMS phishing (smishing) and social media messages, there is no sender address to inspect, which makes these vectors more dangerous and context more important.

**Urgency and fear** are the psychological levers that make phishing effective. A message claiming your account has been compromised, your package couldn't be delivered, or a charge is pending on your card exploits your desire to resolve the problem immediately. This urgency is manufactured specifically to prevent you from pausing to verify. The tell is that the urgency arrives unsolicited — you did not initiate a transaction, request a password reset, or contact support. Legitimate institutions also rarely demand action within hours, and they never ask you to provide your password, full credit card number, or Social Security number via email.

**Generic greetings** ("Dear Customer," "Dear User," "Hello Friend") indicate the attacker does not know your name — they are broadcasting to millions of addresses hoping some will respond. Legitimate communications from organizations you have accounts with almost always address you by name. Spelling and grammar errors, while less reliable than they once were (AI tools have improved attacker writing quality), are still diagnostic — a security alert from a major bank will be proofread. Finally, hover over any link before clicking it (on desktop, the destination appears in the browser status bar): the visible text may say `https://paypal.com` while the actual hyperlink leads somewhere entirely different. If any of these signals appear, verify through an independent channel — go directly to the organization's official website or call the number on the back of your card — never through the link or contact information provided in the suspicious message.
