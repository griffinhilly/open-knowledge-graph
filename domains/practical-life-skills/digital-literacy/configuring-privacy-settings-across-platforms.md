---
id: configuring-privacy-settings-across-platforms
title: Configuring Privacy Settings Across Platforms
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: social-media-literacy
  type: hard
- id: managing-digital-identity-footprint
  type: soft
- id: private-browsing-and-incognito-mode
  type: soft
- id: form-filling-and-data-entry-safety
  type: soft
- id: app-permissions-and-privacy
  type: soft
builds-toward:
- digital-identity-management
tags:
- privacy
- settings
- social-media
stage: formal-systems
status: validated
---
# Configuring Privacy Settings Across Platforms

## Core Idea
Social media platforms, email providers, and search engines all have privacy settings that control who sees your information and what data is collected about you. Default settings typically share more data than users intend; reviewing and adjusting them gives you control.

## Questions

```yaml
- question: "A user carefully adjusts all their social media post visibility to 'Friends Only.' They then notice that ads on the platform suspiciously match items they searched for on a completely different website. Which setting did they most likely fail to adjust?"
  type: multiple-choice
  options:
    - "Visibility settings — they should have set profile visibility to private, not just posts"
    - "Data collection and ad personalization settings — cross-site tracking operates independently of who sees your posts"
    - "Notification settings — ads are triggered by notification preferences"
    - "Account security settings — two-factor authentication prevents ad tracking"
  answer: 1
  explanation: "Privacy settings operate on two distinct axes: visibility (who sees your content) and data collection (what the platform records about your behavior). Adjusting post visibility to 'Friends Only' only addresses the first axis. Cross-site tracking via embedded pixels or cookies is a data collection setting, typically buried under 'Ad Preferences' or 'Personalization.' Many users complete the visible settings and never realize a second category exists — which is exactly what the topic's key insight highlights."

- question: "After logging into a music app using 'Continue with Google,' you later revoke that app's access in Google's connected apps settings. What happens to data the music app already collected during your use?"
  type: multiple-choice
  options:
    - "It is automatically deleted because revoking access triggers a GDPR deletion request"
    - "Google notifies the app to purge your data within 30 days"
    - "The app retains all data it already collected; revoking access only prevents future data transfers from Google"
    - "Nothing changes — revoking access in Google has no effect on third-party apps"
  answer: 2
  explanation: "Revoking a connected app's access stops future data sharing from your Google account to that app, but the app retains whatever data it already received. This is a critical nuance: the damage from granting access happens at the moment of grant, not continuously. Apps often retain access indefinitely unless revoked, so the practical recommendation is to audit and revoke access to any connected apps you no longer actively use — and to review these periodically, not just once."

- question: "Social media platform privacy settings, once configured, remain in place permanently and do not need to be revisited."
  type: true-false
  answer: false
  explanation: "Platforms frequently update their terms of service, introduce new features, or reset certain settings to more permissive defaults after updates. A setting you configured two years ago may have been overridden by a platform change. Revisiting privacy settings periodically — at minimum once a year — is the only way to maintain ongoing control. This is distinct from a firewall you configure once; think of it more like a lease that needs periodic renewal."

- question: "Default privacy settings on most social media platforms tend to favor maximum data sharing because broad reach and data access serve the platform's business interests, not the user's."
  type: true-false
  answer: true
  explanation: "Platforms earn revenue through advertising, which depends on reach and detailed user data. Defaults that enable public posts, cross-site tracking, and third-party data sharing are rational from the platform's perspective: most users never change defaults, so these settings maximize the data available for targeting. Users who want more restrictive sharing must actively opt out — a design choice (not a technical necessity) that systematically tilts outcomes toward the platform."

- question: "Explain why adjusting visibility settings alone (controlling who can see your posts) may not adequately protect your privacy on a social media platform."
  type: short-answer
  answer: "Visibility settings control who sees your content, but data collection settings control what the platform records about your behavior — including activity on other websites, location, and browsing patterns used for ad targeting. A profile that's visible only to friends can still be connected to extensive behavioral tracking. Additionally, connected third-party apps may retain access to your account data indefinitely regardless of visibility settings. Full privacy protection requires addressing both axes independently."
  explanation: "The two-axis framework (visibility vs. data collection) is the central insight of this topic. Users often conflate them, assuming 'private profile' means 'limited data collection.' In practice, a user with a fully private profile and public-facing posts both feed the same advertising infrastructure if data collection settings are unrestricted. The distinction matters practically because the settings that control each axis are in completely different menus and require separate review."
```

## Explainer

From your study of social media literacy and digital identity, you know that platforms collect data about you and that your online presence extends well beyond what you consciously post. Privacy settings are the primary tool you have to limit and shape that presence. The key insight is that these settings exist on two distinct axes: **visibility** (who can see what you post) and **data collection** (what the platform records and uses about your behavior). Many users only think about the first and overlook the second entirely.

**Visibility settings** control the audience for your content. Most platforms offer gradations: public (anyone, including non-users), friends-of-friends or followers, friends or mutuals only, or private/close friends. The default on most platforms skews toward maximum visibility because broad reach serves the platform's interests (advertising reach, network growth) even when it doesn't serve yours. A common pattern: you create an account, accept defaults, and spend months with location data visible to strangers, or with posts indexed by search engines. Auditing visibility settings means going category by category — profile photo, biography, posts, tagged photos, stories — and asking for each one: "Who do I actually want to see this?"

**Data collection settings** are less visible but often more consequential. These include: whether the platform tracks your activity on other websites via embedded pixels or cookies; whether it uses your data for **targeted advertising**; whether it shares data with third-party "partners"; and whether it uses your location, camera, or microphone. On many platforms these settings are buried in "Security and Privacy" sub-menus or labeled in obscure ways ("Personalization and data" rather than "What we collect about you"). A useful mental model from your digital identity study: every toggle you enable here is a permission slip for data processing that happens invisibly in the background.

The practical process for configuring privacy across platforms is consistent, even though every platform's interface is different. Start with the privacy or security section of settings. Look for: audience controls for past and future posts, activity data and ad personalization settings, connected apps and permissions (apps you've logged into via a social account often retain access indefinitely unless revoked), and location settings. Do this on each platform separately, because there is no universal privacy switch. Revisit these settings periodically — platforms frequently update their defaults or introduce new data-sharing features that reset your preferences, and reviewing them once a year is a reasonable minimum for anyone who cares about their digital footprint.
