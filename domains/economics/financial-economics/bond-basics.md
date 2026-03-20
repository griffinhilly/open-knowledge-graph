---
id: bond-basics
title: Bonds and Fixed Income Instruments
domain: economics
course: financial-economics
prerequisites:
- id: interest-rates-and-loanable-funds
  type: hard
- id: time-value-of-money
  type: soft
builds-toward:
- bond-pricing
- yield-to-maturity
- term-structure-of-interest-rates
tags:
- bonds
- fixed-income
- coupon
- face-value
- debt-securities
stage: formal-systems
status: validated
---

# Bonds and Fixed Income Instruments

## Core Idea
A bond is a debt security in which the issuer borrows from investors and commits to pay periodic interest (coupon payments) plus return the principal (face value) at maturity. Bonds are characterized by their face value, coupon rate, maturity date, and credit quality. Government bonds (Treasuries) carry essentially no default risk in nominal terms, while corporate bonds bear default risk and pay a credit spread above Treasuries. The bond market globally exceeds the equity market in total value and is central to monetary policy transmission, government financing, and portfolio construction.

## How It's Best Learned
Study a real Treasury bond prospectus to connect terminology to actual instruments. Distinguish between zero-coupon bonds (no interim payments), coupon bonds, and callable bonds (where the issuer may redeem early). Compare bonds across different credit ratings and maturities side by side.

## Common Misconceptions
- The coupon rate is fixed at issuance; the current yield and yield to maturity change daily as the market price moves.
- Government bonds have no default risk but carry substantial interest rate risk — their prices fall when rates rise.

## Explainer

A bond is simply a loan that has been packaged into a tradeable security. When you lend money by buying a bond, the borrower (the **issuer**) promises to pay you a series of fixed cash flows: periodic **coupon payments** (typically semiannual) equal to the coupon rate times the **face value** (also called par value), plus the face value itself returned at **maturity**. Your prerequisite on the time value of money is the key to understanding everything that follows: each of these future cash flows is worth less than its face amount today, and the bond's market price is exactly the present value of all those future payments.

The relationship between bond prices and interest rates is the most important thing to internalize. Suppose you hold a bond paying 5% coupons on $1,000 face value — that's $50 per year. Now imagine market interest rates rise to 7%. New bonds are being issued paying $70 per year on a $1,000 face value. Nobody will pay $1,000 for your old 5% bond when they can get a 7% bond instead. The price of your bond must fall until the $50 coupon represents a 7% return on the lower price. This inverse relationship — **when rates rise, bond prices fall; when rates fall, bond prices rise** — is mechanical, not incidental. It follows directly from the present-value formula you already know.

This is why the common misconception in the notes deserves emphasis: the **coupon rate** is a fixed contractual feature set at issuance, like a printed label. The **yield to maturity (YTM)** is the actual return you earn by buying the bond at today's market price and holding it to maturity — it changes every day as the price changes. When the bond trades at face value, coupon rate equals YTM. When it trades below par (a **discount bond**), YTM > coupon rate. When it trades above par (a **premium bond**), YTM < coupon rate. The market price adjusts until the YTM matches what investors demand for the bond's risk.

Credit quality introduces the second dimension. A **Treasury bond** backed by the US government carries essentially no **default risk** — the government can always print dollars. But as noted, it carries substantial **interest rate risk**. A **corporate bond** adds **default risk**: the issuer might fail to make payments. Investors demand a **credit spread** — extra yield above the Treasury rate — as compensation. This spread widens when the issuer's finances deteriorate and narrows when they improve. Investment-grade bonds carry lower spreads; high-yield (junk) bonds carry higher spreads, compensating investors for the higher probability of default. The bond's price encodes all of this: it is whatever price makes the YTM (including the credit spread) match what the market demands given the issuer's risk profile and the current level of interest rates. Mastering this interplay between price, yield, maturity, and credit quality is the foundation of all fixed-income analysis.
