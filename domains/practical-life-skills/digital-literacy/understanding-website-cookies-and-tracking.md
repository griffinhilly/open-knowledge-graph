---
id: understanding-website-cookies-and-tracking
title: Understanding Website Cookies and Tracking
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: web-browser-basics
  type: hard
- id: digital-privacy-fundamentals
  type: soft
builds-toward:
- configuring-privacy-settings-across-platforms
tags:
- privacy
- tracking
- cookies
stage: formal-systems
status: draft
---

# Understanding Website Cookies and Tracking

## Core Idea
Cookies are small files that websites store on your browser to remember information about you—login details, preferences, or browsing behavior. While essential cookies enable website functionality, tracking cookies follow you across sites to build an advertising profile.

## Questions

```yaml
- question: "After reading about tracking cookies, a user opens private browsing mode before visiting a shoe store. They believe they will not be tracked since private mode clears cookies. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — private browsing mode prevents all forms of tracking"
    - "Private mode clears cookies after the session ends, but browser fingerprinting can still identify the browser during the session without using cookies at all"
    - "The user would only be tracked if they clicked on an advertisement"
    - "Private mode works for first-party cookies but not third-party cookies"
  answer: 1
  explanation: "Private browsing prevents cookies from persisting after the session, but fingerprinting — which identifies your browser by its unique combination of screen resolution, installed fonts, time zone, hardware, and other passive signals — requires no cookies at all. These signals are collected the moment the page loads, invisibly, without any storage on your device. Private mode addresses cookie-based tracking but leaves fingerprint-based tracking fully intact."

- question: "How does a third-party advertising network know which websites you've visited, even though you never created an account with that network?"
  type: multiple-choice
  options:
    - "The network intercepts your browser's DNS queries to reconstruct your browsing history"
    - "Websites you visit sell your browsing data to the network in real time"
    - "Code from the ad network is embedded in many different websites; when those pages load, your browser automatically sends the network's cookie back — allowing the network to track your activity across all those sites"
    - "The network can only see your activity if you have clicked at least one of its ads previously"
  answer: 2
  explanation: "Ad networks like Google or Meta place their tracking code on thousands of websites. When your browser loads a page containing that code, it contacts the ad network's servers and sends any existing cookies for that domain — just as it would for a first-party request. Because the same network's code appears across many sites, it accumulates a cross-site profile from these automatic browser requests, all without you ever visiting the ad network's own website or creating an account."

- question: "A first-party cookie and a third-party cookie can both be stored in your browser during a single page visit, even though they are set by different organizations."
  type: true-false
  answer: true
  explanation: "When you visit a website, the page may load resources from multiple sources: the site's own server (which may set first-party cookies) and embedded third-party scripts or images from ad networks, analytics providers, or social media buttons (each of which may set their own third-party cookies). Your browser stores all of them, tagged by the domain that set each one. The first-party cookie remembers your login; the third-party cookie logs the visit for the ad network. Both are written in the same browser session."

- question: "Blocking all cookies in your browser settings fully prevents advertising networks from tracking your browsing behavior."
  type: true-false
  answer: false
  explanation: "Cookies are only one layer of a multi-layer tracking system. Browser fingerprinting identifies your device by passively reading its configuration — screen resolution, installed fonts, browser plugins, GPU, time zone, language settings — and combining these into a near-unique identifier. This requires no storage on your device and cannot be blocked by cookie settings. Even with all cookies disabled, a fingerprinting script can recognize your browser on return visits. Full protection requires fingerprint-resistant browsers or extensions, not just cookie blocking."

- question: "Why does seeing the same advertisement follow you across multiple unrelated websites not require those websites to share data with each other directly?"
  type: short-answer
  answer: "Each of the unrelated websites has independently embedded code from the same third-party ad network. When your browser visits any of them, it automatically sends the ad network's cookie back to the network's servers — not to the other websites. The ad network is the common hub: it sees the visits from all participating sites because your browser communicates with it on each page load. The websites themselves never exchange data; they simply all load the same tracker, which does the aggregation centrally."
  explanation: "This is the key architectural insight: you don't need websites to collude with each other if they all independently include the same third-party code. The ad network becomes a passive aggregator — it collects cross-site data not by receiving reports from websites but by being a direct participant in every page load. Understanding this structure explains why blocking third-party cookies (or the tracker's domain via DNS blocking) is more effective than hoping websites will stop sharing data with each other."
```

## Explainer

You already know from your web browser basics how your browser requests pages from servers and how privacy fundamentals describe the data trail you leave online. Cookies are a specific mechanism at the center of that data trail — and understanding exactly how they work explains why the same pair of shoes can seem to follow you around the internet for a week after you looked at them once.

When you visit a website, the server can instruct your browser to store a small text file called a **cookie** on your device. The next time you visit, your browser automatically sends that cookie back to the server. This is how websites keep you logged in: the server issues you a session cookie containing a unique ID, and every subsequent request your browser sends includes that ID, so the server knows it's still you. **First-party cookies** — set by the website you're actually visiting — are largely benign and necessary. Without them, you'd have to log in to every page of a website separately.

**Third-party cookies** are different. These are cookies set not by the site you're visiting, but by code embedded in that site — typically from advertising networks like Google or Meta. When a page loads, it often pulls in tracking scripts from these external companies, and those companies set their own cookies in your browser. Because the same ad network's code appears on thousands of different websites, it can see which sites you've visited across the entire web. Each visit adds to a profile: you visited a shoe store, then read a travel article, then checked a news site. The ad network assembles these signals into a detailed behavioral profile and uses it to target ads. This is how you see ads for shoes after browsing for them — your browser revealed your visit by sending that third-party cookie on every subsequent page.

Modern browsers and privacy regulations have significantly restricted third-party cookies. Safari and Firefox block them by default; Chrome has been phasing them out. But the tracking industry has adapted with **fingerprinting** — identifying your browser by its unique combination of screen resolution, fonts installed, time zone, and other passive signals that require no cookie at all. This is why "private browsing" mode doesn't make you invisible: it clears cookies but leaves your fingerprint intact. Meaningfully protecting your privacy requires understanding that cookies are just one layer of a multi-layer tracking system. Managing cookies through browser settings is a useful first step; understanding why advertisers want them is what tells you which additional steps — like a privacy-focused browser extension or DNS-level blocking — are worth the tradeoff in convenience.
