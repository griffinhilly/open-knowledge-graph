---
id: understanding-urls-web-addresses
title: Understanding URLs and Web Addresses
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: web-browser-essentials
  type: hard
builds-toward:
- evaluating-source-credibility-online
- recognizing-online-scams-fraud
tags:
- url
- domain
- web-address
- http-https
stage: abstract-reasoning
status: draft
---

# Understanding URLs and Web Addresses

## Core Idea
A URL (Uniform Resource Locator) is the web address that tells your browser which page to load. URLs consist of a protocol (http or https), a domain name, and a path. The 'https' protocol with a padlock icon indicates a secure connection. Understanding URL structure helps you identify legitimate websites, spot phishing attempts, and navigate the web more effectively.

## How It's Best Learned
Visit several websites and examine the URLs in the address bar. Notice the difference between http and https. Try typing a URL directly instead of using search.

## Common Misconceptions
- The domain name is always the website owner's legal company name.
- http and https are interchangeable.
- A professional-looking domain guarantees legitimacy.

## Explainer

Now that you know how to navigate with a browser, it's worth understanding exactly what you're typing into the address bar and what each piece means. A **URL** (Uniform Resource Locator) is a structured address that tells your browser three things: what communication method to use, which server to contact, and where on that server the specific page lives. Breaking down a URL like `https://www.bbc.com/news/world` reveals: `https` is the **protocol**, `www.bbc.com` is the **domain**, and `/news/world` is the **path** to a specific page within that domain.

The **protocol** — `http` or `https` — specifies how your browser and the website communicate. The `s` in `https` stands for "secure": it means all data traveling between your browser and the website is encrypted, so no one watching the network connection can read it. Your browser signals this with a padlock icon in the address bar. This matters enormously when you're entering passwords, payment information, or any sensitive data — always verify the padlock is present before submitting a form. On an `http` site, that information travels as readable text.

The **domain name** is the most important piece for evaluating trust. Domains are hierarchical: reading from right to left, you move from general to specific. In `bbc.com`, `.com` is the **top-level domain** (TLD), and `bbc` is the registered name. The critical rule is that the real owner of a site is identified by the name directly to the left of the TLD. Scammers exploit this by creating addresses like `bbc.com.account-update.net` — where the actual domain is `account-update.net`, not `bbc.com`. The `bbc.com` part is just a subdirectory name designed to fool you. Always check what appears just before `.com`, `.org`, `.net`, or the country code at the end.

The **path** is everything after the domain — it tells the server which specific page, image, or file you want. Paths look like file folders on a computer because they work the same way: `/news/world` means "go into the `news` folder and find the `world` page." You rarely need to type paths manually; clicking links fills them in automatically. But reading a path can tell you a lot about a page's structure — a URL ending in `/login` or `/checkout` tells you exactly where you are in a website's flow, which is useful for catching redirects to unexpected locations.
