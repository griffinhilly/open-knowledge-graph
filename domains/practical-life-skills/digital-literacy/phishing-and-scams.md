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
- id: keeping-yourself-safe-online
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

## Questions

```yaml
- question: "You receive an email that appears to come from your bank's official address, saying 'Your account will be suspended in 24 hours — click here immediately to verify your identity.' What is the best first response?"
  type: multiple-choice
  options:
    - "Click the link immediately — it came from the bank's official email address, so it must be legitimate"
    - "Reply to the email asking for more details before deciding"
    - "Do not click; hover over the link to inspect the actual destination URL, then call the bank directly using a number from their official website — not one in the email"
    - "Ignore it entirely — banks never send urgent emails"
  answer: 2
  explanation: "This message uses two classic phishing tactics: a spoofed sender identity and urgency ('24 hours'). Display names and even sender addresses can be faked. The correct defense is to not click any links, inspect the actual URL by hovering, and verify through a separate trusted channel (calling the bank's official number). Option A is the trap the attackers designed; option D is too dismissive since some urgent bank communications are legitimate."

- question: "A professional receives an email that correctly references their employer, their current project, and their manager's name, then urgently asks them to wire money. Why is this more dangerous than a generic phishing email?"
  type: multiple-choice
  options:
    - "It isn't — generic phishing is more dangerous because it reaches millions of people at once"
    - "Because it uses personal information to seem credible, making the psychological pressure to comply much harder to resist and the red flags much harder to spot"
    - "Because it arrived by email rather than text, which is a more trusted channel"
    - "Because it mentions money, which triggers security filters"
  answer: 1
  explanation: "This is a spear-phishing attack — targeted at a specific individual using harvested personal data. The personal details defeat the 'I'd recognize a scam' confidence, because the email seems to come from someone who already knows you. The urgency further suppresses skepticism. This is why 'I'm too smart to fall for phishing' is a dangerous belief — the most convincing attacks are designed to fool exactly that person."

- question: "Phishing emails are easy to spot because they typically contain obvious spelling errors and come from clearly suspicious email addresses."
  type: true-false
  answer: false
  explanation: "This describes generic, mass-sent phishing — but sophisticated attacks, especially spear-phishing targeted at specific individuals, may have flawless grammar, no spelling errors, and spoofed sender addresses that look identical to legitimate ones. Relying on spelling errors as your filter will cause you to miss the most dangerous attacks."

- question: "The urgency tactics in phishing messages — such as 'your account will be locked in 24 hours' — are deliberately designed to suppress your skepticism and push you into acting without careful thought."
  type: true-false
  answer: true
  explanation: "Urgency is the most powerful psychological lever in social engineering. When people feel rushed or threatened, they bypass careful evaluation and focus on taking the prescribed action. Phishers engineer this state intentionally. Recognizing urgency as a manipulation tactic — and treating it as a reason to slow down rather than speed up — is one of the most important defensive habits."

- question: "Why does phishing work on intelligent, tech-savvy people, not just those who are new to technology? What does this tell you about the right defense strategy?"
  type: short-answer
  answer: "Phishing exploits human psychology — trust, urgency, fear — not technical ignorance. Even experts can be rushed or deceived by a well-crafted, personalized message that looks exactly like a communication they would normally receive. The right defense is behavioral, not just technical: slow down when you feel pressured, verify through a separate trusted channel (call the institution directly using a number you find independently), and remember that any legitimate organization will wait for you to verify before taking action."
  explanation: "The common assumption that 'smart people don't fall for scams' is exactly the confidence phishers count on. Spear-phishing attacks are designed with research — they reference real people, real projects, real relationships. No amount of general intelligence fully protects against a message specifically crafted to seem legitimate to you. The defense must be habitual and procedural, not IQ-dependent."
```

## Explainer

Phishing works because it exploits trust, not technical ignorance. You already know from internet safety basics that not every website or email is what it claims to be. Phishing is the systematic exploitation of that gap — attackers craft messages that look exactly like ones from your bank, your employer, or a government agency, then use psychological pressure to make you act before you think. The attack doesn't need to bypass your antivirus; it needs to bypass you.

The core mechanism is **social engineering**: manipulating human behavior rather than breaking technical systems. The most effective phishing messages share a common structure — they establish a credible sender identity, create urgency or fear ("Your account will be suspended in 24 hours"), and offer a clear action that feels safe but isn't (clicking a link that leads to a fake login page). Each element is designed to suppress your skepticism. Urgency is the most powerful lever: when you feel rushed, you're less likely to pause and inspect the details.

The technical tells are learnable with practice. **URL inspection** is your most reliable tool: hover over any link before clicking and read the actual destination, not the display text. Phishers use tricks like `paypal.com.attacker.net` (where `attacker.net` is the actual domain), character substitutions like `paypa1.com`, or long URLs designed to bury the real domain at the end. **Email headers** can reveal spoofed senders — a message may display as "Bank of America Support" but originate from `support@totally-not-bank.ru`. And while spelling errors are a classic tell, sophisticated spear-phishing attacks — those targeted at specific individuals using personal information — may have none.

**Spear-phishing** represents the evolution beyond mass phishing. Where a generic phishing email goes to millions of people hoping a few will bite, spear-phishing is tailored to you: it may reference your employer, your recent purchase, or your colleague's name (harvested from LinkedIn or a data breach). This is why the "I'd recognize a scam" confidence is dangerous — the most convincing attacks are designed for you specifically. The defense is behavioral: slow down, verify through a separate channel (call the bank directly using a number from their official website, not one in the email), and remember that any legitimate organization will wait for you to verify before taking action.
