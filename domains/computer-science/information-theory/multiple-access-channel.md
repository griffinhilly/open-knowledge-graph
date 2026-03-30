---
id: multiple-access-channel
title: Multiple Access Channel
domain: computer-science
course: information-theory
prerequisites:
- id: channel-capacity
  type: hard
- id: network-information-theory
  type: hard
- id: mutual-information
  type: hard
tags:
- multiple access
- MAC
- multi-user
- successive decoding
- capacity region
stage: expert
status: validated
---

# Multiple Access Channel

## Core Idea
The multiple access channel (MAC) models K independent senders transmitting to a single receiver over a shared medium. The capacity region — the set of simultaneously achievable rate tuples (R_1, ..., R_K) — is characterized by sum_{i in S} R_i <= I(X_S; Y | X_{S^c}) for all subsets S of senders, where X_S denotes the inputs from senders in S. For two users: R_1 <= I(X_1;Y|X_2), R_2 <= I(X_2;Y|X_1), R_1+R_2 <= I(X_1,X_2;Y). The capacity region is achieved by joint typicality decoding or successive interference cancellation (SIC), where the receiver decodes one user at a time, subtracting each decoded signal. The MAC was the first multi-user channel whose capacity region was fully characterized.

## Questions

```yaml
- question: "Two users share a Gaussian MAC with power constraints P_1 and P_2 and noise power N. The sum capacity is log2(1 + (P_1+P_2)/N). How does this compare to giving each user a separate channel with half the bandwidth?"
  type: multiple-choice
  options:
    - "The MAC sum rate is always lower because of interference"
    - "They are always equal because the total power and noise are the same"
    - "The MAC sum rate is higher — treating interference as part of the signal (via SIC) is more efficient than splitting the channel"
    - "The comparison depends on which user has more power"
  answer: 2
  explanation: "With orthogonal access (each user gets half the bandwidth), the sum rate is (1/2)log(1+2P_1/N) + (1/2)log(1+2P_2/N), which is strictly less than log(1+(P_1+P_2)/N) by the concavity of the log function. The MAC allows both users to transmit simultaneously across the full bandwidth, and SIC at the receiver separates them — this is more efficient than dividing the channel. Orthogonal multiple access (TDMA, FDMA) is suboptimal from an information-theoretic perspective."

- question: "In successive interference cancellation, the decoding order affects the individual rates R_1 and R_2 but not the sum rate R_1 + R_2."
  type: true-false
  answer: true
  explanation: "Decoding user 1 first (treating user 2 as noise) gives R_1 <= log(1 + P_1/(P_2+N)), then subtracting user 1 and decoding user 2 gives R_2 <= log(1 + P_2/N). Reversing the order gives R_1 <= log(1 + P_1/N) and R_2 <= log(1 + P_2/(P_1+N)). In both cases, R_1 + R_2 <= log(1 + (P_1+P_2)/N). The sum rate boundary is the same; the decoding order just selects different corner points of the capacity region. Time-sharing between decoding orders traces out the full dominant face."

- question: "Explain why the MAC capacity region is a polygon (for two users) and how its corner points correspond to different decoding strategies."
  type: short-answer
  answer: "The two-user MAC capacity region is defined by R_1 <= I(X_1;Y|X_2), R_2 <= I(X_2;Y|X_1), and R_1+R_2 <= I(X_1,X_2;Y). The first constraint is the rate if user 2's signal were removed (decoded first); the second is the rate if user 1's signal were removed. The sum constraint bounds the total throughput. The resulting region is a pentagon. The two corner points on the dominant face correspond to the two SIC decoding orders: (I(X_1;Y|X_2), I(X_1,X_2;Y) - I(X_1;Y|X_2)) and (I(X_1,X_2;Y) - I(X_2;Y|X_1), I(X_2;Y|X_1)). Time-sharing between corners achieves any point on the dominant face. Each corner point gives one user the best possible rate while the other user gets whatever remains."
  explanation: "This pentagon structure generalizes to K users as a polymatroidal region. The number of constraints grows exponentially (2^K - 1 subset constraints), but the structure remains clean. The fact that the full region is achievable — not just corner points — is a remarkable result that relies on the flexibility of random coding."
```

## Explainer

The multiple access channel is the canonical uplink model: think of multiple cell phones transmitting to a single base station, or multiple IoT devices sending data to a gateway. Each sender has an independent message and a power constraint. The shared medium means the receiver sees a superposition of all transmitted signals plus noise. The fundamental question is: what rates can all users simultaneously achieve?

For two Gaussian users, Y = X_1 + X_2 + Z. Decoding user 1 first (treating X_2 as additional noise of power P_2): R_1 <= (1/2) log(1 + P_1/(P_2 + N)). After subtracting the decoded X_1, decode user 2 with no interference: R_2 <= (1/2) log(1 + P_2/N). Reversing the order swaps the rates. Time-sharing between the two orders traces the dominant face of the capacity region. The sum-rate boundary R_1 + R_2 <= (1/2) log(1 + (P_1+P_2)/N) is achieved by both orderings.

The key insight is that **treating all other users as noise and decoding sequentially (SIC) is optimal** — you do not need more sophisticated joint decoding. This is because the MAC is "informationally friendly": each user's signal adds information, not just interference. The receiver decodes one user, removes their contribution from the received signal (since it now knows what they sent), and faces a cleaner signal for the remaining users. This is unlike the interference channel, where each receiver wants only its own message and the other signals are pure interference.

The MAC has direct engineering implications. In 4G/5G uplink, non-orthogonal multiple access (NOMA) schemes use SIC-like receivers to allow users to transmit simultaneously, approaching the MAC capacity region. Traditional orthogonal schemes (TDMA, FDMA, OFDMA) divide the channel among users, which is simple but suboptimal — the capacity region of orthogonal access is strictly inside the MAC capacity region. The information-theoretic result motivates the engineering move toward non-orthogonal schemes that let users "collide" and rely on receiver intelligence to separate them.
