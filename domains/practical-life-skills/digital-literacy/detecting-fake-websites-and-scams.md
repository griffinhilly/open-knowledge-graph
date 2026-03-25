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
- id: recognizing-online-scams-fraud
  type: soft
builds-toward:
- keeping-yourself-safe-online
tags:
- security
- fraud
- credibility
stage: abstract-reasoning
status: validated
---
# Detecting Fake Websites and Online Scams

## Core Idea
Fake websites mimic legitimate ones to steal credentials or money. Red flags include subtle URL misspellings, missing HTTPS security indicators, poor design quality, unrealistic offers, and pressure to act immediately. Always navigate to official websites by typing the address directly.

## Questions

```yaml
- question: "You receive an email from 'support@paypal.com.secure-verify.net' with a link to a site that has a padlock (HTTPS) and looks exactly like PayPal. Which statement is correct?"
  type: multiple-choice
  options:
    - "The site is likely legitimate — HTTPS confirms it is an official PayPal site"
    - "The site is likely a scam — the real domain is 'secure-verify.net,' not 'paypal.com,' even though paypal.com appears in the address"
    - "The email might be legitimate — companies often use third-party security subdomains like this"
    - "You cannot determine legitimacy from the URL alone; the padlock is the most reliable trust signal"
  answer: 1
  explanation: "Reading a domain correctly is critical: read from right to left, stopping at the first slash. The real domain is the part immediately before the first slash — here, 'secure-verify.net.' Everything before it is a subdomain that anyone can create freely. So 'paypal.com.secure-verify.net' is a subdomain of 'secure-verify.net,' not of 'paypal.com.' The padlock only confirms the connection to 'secure-verify.net' is encrypted — it says nothing about whether that site is trustworthy. This subdomain pattern (trusted brand as prefix of attacker's domain) is described as 'especially deceptive and extremely common.'"

- question: "A website selling electronics has HTTPS, an attractive professional design, and prices about 40% below retail. Which signal is the most actionable red flag?"
  type: multiple-choice
  options:
    - "The padlock — HTTPS is only used by verified legitimate businesses"
    - "The professional design — fake sites always look amateurish"
    - "The prices — unrealistically low prices are a common scam signal, and the padlock only confirms encryption, not legitimacy"
    - "The .com domain — legitimate businesses typically use .org or .net"
  answer: 2
  explanation: "Unrealistically low prices are a classic scam signal. The padlock and HTTPS tell you only that the connection is encrypted, not that the site is legitimate — fake sites routinely use HTTPS. Professional-looking design is not a reliable signal either; scammers invest in appearing credible. The combination of polished appearance with prices far below market value is a strong fraud pattern: the product either never arrives or is counterfeit. HTTPS is necessary but not sufficient for trust."

- question: "A website with HTTPS and a padlock icon is safe to enter your password on."
  type: true-false
  answer: false
  explanation: "HTTPS confirms that data between your browser and the server is encrypted and cannot be intercepted in transit. It says nothing about who controls the server. A phishing site can and routinely does use HTTPS, meaning your credentials are securely transmitted to the attacker — the encryption is working perfectly, just not in your favor. The padlock means 'this connection is private'; it does not mean 'this site is legitimate.' Its absence is a strong red flag; its presence is not a green light."

- question: "Urgency messages like 'Your account will be suspended in 24 hours' are a reliable indicator of a scam because legitimate institutions never communicate time-sensitive account issues."
  type: true-false
  answer: false
  explanation: "The claim that legitimate institutions never communicate urgently is an overclaim. Real institutions do sometimes send time-sensitive alerts — password breach notifications, genuine fraud alerts. The key insight is not that urgency is always fake, but that artificial urgency is a scammer's primary tool for preventing you from pausing to verify. The correct response is to slow down: navigate directly to the official site by typing its URL, call the institution's known phone number, or check through an app you already have installed — rather than clicking the link in the urgent message."

- question: "Why is typing a website's address directly into the browser safer than clicking a link in an email, even if the email looks legitimate and the link text shows the correct address?"
  type: short-answer
  answer: "Displayed link text can be completely different from the actual URL the link points to. An email can show 'www.paypal.com' as visible text while the underlying href points to 'paypa1-secure.com' or a subdomain of an attacker's domain. Even URLs that appear correct in email formatting may use Unicode lookalike characters or typosquatting that is hard to spot. When you type the address directly, you navigate to exactly what you type — no third party controls your destination. For high-stakes actions (banking, passwords, financial transactions), direct navigation eliminates the entire category of link-based phishing attacks in one habit."
  explanation: "The fundamental vulnerability of clicking links is that displayed text and actual destination are independent — the browser goes to the href, not the text. Hovering reveals the true URL in a browser, but email clients may not show this, and even visible URLs can use deceptive Unicode characters. Direct navigation bypasses typosquatting, subdomain attacks, and display-text deception simultaneously, which is why it is the single most effective defensive habit for high-stakes web interactions."
```

## Explainer

From your study of website anatomy, you know that a URL has a specific structure — protocol, domain, path, and query parameters — and that every element carries meaning. From evaluating source credibility, you know that not all online content is equally trustworthy and that surface appearance (professional-looking design) does not equal legitimate authority. Detecting fake websites is the application of both skills under adversarial conditions: someone has deliberately designed a page to fool you, and the question is which signals survive the deception.

The **domain name** is the highest-value signal to check. Attackers use a technique called **typosquatting** — registering domains that look almost identical to legitimate ones but differ by one character: `paypa1.com` instead of `paypal.com`, `arnazon.com` instead of `amazon.com`, or `bankofamerica.com.support-login.net` (where the actual domain is `support-login.net`, not `bankofamerica.com`). That last pattern — a trusted brand name appearing as a subdomain of an attacker's real domain — is especially deceptive and extremely common. Always read the domain from right to left, stopping at the first slash: the real domain is the part immediately before the first `/`, and everything before it is a subdomain that anyone can create.

**HTTPS** (the padlock icon) tells you the connection is encrypted — nobody can intercept the data in transit. What it does not tell you is that the site on the other end is legitimate. Fake websites routinely use HTTPS. A padlock means your credentials are securely transmitted to the attacker; the encryption is working perfectly, just not in your favor. HTTPS is a necessary but not sufficient condition for trust. Its absence is a strong red flag; its presence is not a green light.

**Content and behavior signals** round out the detection toolkit. Fake sites often have inconsistent fonts, blurry logos, low-quality images, grammar errors, and links that go nowhere or loop back to the same page. **Urgency tactics** — "Your account will be suspended in 24 hours," "Only 2 left in stock at this price," "Claim your prize now" — are engineered to prevent you from pausing to think critically. Legitimate institutions do not demand immediate action that bypasses normal channels. The safest habit for high-stakes actions (banking, shopping, entering passwords) is to navigate directly by typing the known URL rather than clicking any link — from an email, search result, or ad — that claims to take you there.
