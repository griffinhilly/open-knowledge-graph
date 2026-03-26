---
id: data-privacy-personal-information
title: Data Privacy and Personal Information
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: digital-literacy-fundamentals
  type: hard
builds-toward:
- digital-privacy-fundamentals
- managing-digital-identity-footprint
tags:
- privacy
- personal-data
- information-sharing
- consent
stage: abstract-reasoning
status: validated
---

# Data Privacy and Personal Information

## Core Idea
Personal information includes anything that can identify you: name, address, phone, email, financial details, health records, and behavioral data. Companies collect data for marketing and analysis. Understanding what data you share, with whom, and how it's used enables you to make informed choices. Privacy is about maintaining control over your information, not about having something to hide.

## How It's Best Learned
Review the privacy policy of a website you use. Check what permissions an app requests on your phone. Search for what information is publicly available about you online.

## Questions

```yaml
- question: "A free flashlight app requests permission to access your contacts, location, and microphone. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The app needs these permissions to function correctly as a flashlight"
    - "The app is collecting data beyond its functional needs, likely to build user profiles for advertising revenue"
    - "This is standard practice — all apps require the same permissions"
    - "The permissions were added by mistake and can be safely ignored"
  answer: 1
  explanation: "A flashlight app has no functional need for contacts, location, or a microphone. When apps request disproportionate permissions, it strongly signals they are collecting data for advertising or third-party sale. This is the core business model: the app is 'free' because your data, not your payment, generates revenue. Granting unnecessary permissions hands over personal information with no corresponding benefit."

- question: "Researchers found that knowing a person's zip code, birthdate, and sex is sufficient to uniquely identify most Americans. Why does this matter for thinking about privacy?"
  type: multiple-choice
  options:
    - "Individually non-sensitive data points can combine to identify specific individuals, making seemingly harmless data a privacy risk"
    - "It shows that government databases are too accessible to outside researchers"
    - "It proves that zip codes should be treated as secret information like passwords"
    - "This only applies in rare cases where the person's name is already known"
  answer: 0
  explanation: "The combination problem is central to modern data privacy: no single piece of data needs to be sensitive for the combination to be identifying. Zip code, birthdate, and sex each seem innocuous, but together they narrow the population to a single individual in most cases. This is why privacy protection must extend beyond obvious data (SSN, passwords) to include behavioral data, location patterns, and other seemingly minor details."

- question: "If your personal data contains very little illegal or embarrassing, you have no meaningful reason to protect your digital privacy."
  type: true-false
  answer: false
  explanation: "Privacy is about control over your personal information, not about concealing wrongdoing. Even entirely innocent data can be used to manipulate purchasing decisions, enable price discrimination, expose you to targeted scams, or be exposed in a breach. The 'nothing to hide' framing conflates privacy with secrecy rather than recognizing it as a form of autonomy — the ability to control your own information regardless of its content."

- question: "When a digital service is offered for free, the company typically earns revenue by collecting user data and using it to enable targeted advertising."
  type: true-false
  answer: true
  explanation: "The dominant business model for free digital services is data monetization. Platforms collect detailed behavioral data (searches, clicks, viewing history, purchases) to build user profiles, then sell advertisers access to specific audience segments. The user is not the customer in this model — the advertiser is. Understanding this reframes 'free' services: you are exchanging your data, not money, for access."

- question: "Why is it important to think carefully about what personal data you share, even when you trust the company collecting it?"
  type: short-answer
  answer: "Even trustworthy companies can experience data breaches, be acquired by less trustworthy entities, change their privacy policies, or share data with third-party partners without your knowledge. Data shared today can persist and be used in ways you never anticipated. Additionally, data aggregated across many sources can reveal patterns you never intended to disclose."
  explanation: "Trust in a company at one moment doesn't guarantee your data will always be handled as you expect. Companies are sold, policies change, breaches happen, and third-party sharing extends your data beyond the original relationship. The practical implication: share the minimum necessary and review privacy settings regularly, rather than assuming that initial trust is permanent protection."
```

## Explainer

From digital literacy fundamentals, you know how to navigate devices, websites, and apps. What you may not have considered is that every interaction with a digital system leaves a trace. When you search for something, click a link, visit a page, use a map, or buy something online, that action is logged somewhere. Over time these logs accumulate into something surprisingly detailed: a record of your interests, location patterns, social connections, purchases, and habits. This is your **digital footprint**, and understanding it is the first step in understanding privacy.

**Personally identifiable information (PII)** is the formal term for data that can identify you. Some PII is obvious: your name, home address, phone number, email, Social Security number, financial account numbers, health records. But PII also includes things that seem less sensitive in isolation — your IP address, device ID, location data, and browsing history — because these can be combined with other data to identify you precisely. The combination problem is important: knowing someone's zip code, birthdate, and sex is enough to uniquely identify most people in the United States, even without a name.

The business model of most "free" digital services is data collection. A search engine, social media platform, or free app that doesn't charge money is typically earning revenue by collecting data about users and selling targeted advertising access to that data. Advertisers pay to reach specific audiences (people aged 25–34 who recently searched for hiking gear, for example). To make this targeting possible, the platform needs to build **user profiles** — records of what you've searched, clicked, watched, liked, and bought. You are not the customer; you are the product being refined and sold. Understanding this doesn't require paranoia, but it does inform decisions about which services to use and what to share.

Protecting privacy means exercising control over what you share and with whom. Practical habits include: checking app permissions and denying access that seems disproportionate to the app's function (a flashlight app has no need for your contacts or location); using strong, unique passwords and two-factor authentication to prevent unauthorized access; being selective about what you post publicly, since public posts can be archived and searched indefinitely; and reading privacy settings on platforms you use regularly. Privacy isn't a binary — you don't have to choose between full exposure and complete invisibility. It's a series of small decisions about tradeoffs between convenience and control, and making them consciously puts you in charge of your own information.
