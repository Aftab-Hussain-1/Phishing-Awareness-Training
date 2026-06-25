# Phishing Awareness Training — Summary

This document summarizes the content of the **Phishing Awareness Training** interactive course. The original file is an HTML-based e-learning module with 9 lessons plus a 15-question final quiz. Below is a written summary of everything covered.

## Module 1: What Is Phishing?

Phishing is a cyberattack where criminals impersonate a trusted person, brand, or organization to steal sensitive information (passwords, card numbers, bank logins) or install malware. It works because it targets people, not technical systems — no firewall stops a click.

**Common formats:**
- **Email phishing** — fake messages from "banks," "delivery services," or "IT support"
- **Spear phishing** — highly targeted attacks using personal details
- **Smishing** — phishing via SMS
- **Vishing** — phishing via phone calls/voicemail
- **Whaling** — attacks aimed at executives
- **Clone phishing** — a copy of a real email with a malicious link swapped in

## Module 2: Anatomy of a Phishing Email

Before reading an email's content, check: who it's really from, where links actually go, and whether you expected it.

**Red flags:**
- Sender address doesn't match the real domain (e.g. `support@paypa1-secure.com`)
- Urgent/threatening language ("account suspended in 24 hours")
- Generic greetings ("Dear Customer")
- Requests for payment, gift cards, or wire transfers
- Spelling/grammar mistakes
- Mismatched or shortened links
- Unexpected attachments (.zip, .exe, macros)

## Module 3: Spotting Fake Websites

Check the address bar before typing a password.

- **Domain name:** The real domain is the part right before the first single slash. `amazon.account-verify.com` is NOT Amazon.
- **HTTPS/padlock** only means the connection is encrypted — not that the site is legitimate.
- Watch for misspellings, odd formatting, unexpected pop-ups, and shortened URLs.
- **Safer habit:** type the company's known address yourself or use a saved bookmark instead of clicking email links.

## Module 4: Social Engineering Tactics

Phishing is psychology, not just technology. Common tactics:

- **Urgency & fear** — "Your account will be locked"
- **Authority** — impersonating a CEO, IT, or law enforcement
- **Curiosity** — "Someone tagged you in a photo"
- **Greed/reward** — fake prizes, refunds, investments
- **Trust exploitation (pretexting)** — posing as a coworker or vendor
- **Scarcity** — "Only 2 hours left"

**Real-world pattern:** Business Email Compromise (BEC) scams combine authority + urgency + secrecy to push finance staff into urgent wire transfers.

## Module 5: Spear Phishing & Targeted Attacks

Spear phishing is researched and personalized, using your name, job title, manager's name, or details scraped from social media/breached data. It's harder to spot because there may be no spelling errors or generic greetings.

**Defense:** If a request feels personal but unusual — especially involving money or credentials — verify through a separate channel (phone call, known chat tool) before acting.

## Module 6: Smishing & Vishing

- **Smishing (SMS phishing):** Fake delivery/bank texts with malicious links (e.g. fake "USPS fee" texts).
- **Vishing (voice phishing):** Callers impersonate banks or tech support, often with spoofed caller ID. A real bank never asks for your full card number or PIN over an inbound call.

**What to do:** Don't click links in unexpected texts; hang up and call the number on your card; never share one-time passcodes (OTPs) over the phone.

## Module 7: Business Email Compromise & QR Code Phishing

- **BEC:** Attackers compromise or spoof an executive's email to redirect wire transfers, change payroll details, or request gift cards. Pattern: secrecy + urgency + unusual request.
- **Quishing (QR code phishing):** Malicious QR codes in emails, flyers, or stickers (even over real codes on parking meters) lead to fake logins or malware — bypassing the "hover to check link" habit.

## Module 8: Best Practices — Email & Browsing Habits

**Email habits:**
- Pause before clicking anything urgent
- Hover over links to preview destinations
- Check the full sender address, not just display name
- Be cautious of attachments even from known contacts
- Never enter a password after clicking an email link

**Browsing habits:**
- Type known addresses directly or use bookmarks
- Check domains carefully before entering credentials
- Keep browser/OS updated
- Use a password manager (won't autofill on fake look-alike domains)

**Golden rule:** Pressure to act right now is itself a red flag.

## Module 9: Protecting Your Accounts

- **MFA (Multi-Factor Authentication):** Adds a second proof of identity beyond your password. Enable it everywhere possible.
- **MFA fatigue attacks:** Attackers spam push notifications hoping for an accidental approval — never approve a prompt you didn't trigger; deny and change your password.
- **Password hygiene:** Unique passwords per account, long passphrases, change immediately if compromised.
- **Reporting:** Use "Report Phishing" buttons; notify IT/security even if unsure; don't be embarrassed to report.

## Module 10: Real-World Case Studies

1. **Fake invoice scam:** Attackers impersonated a vendor with "updated" bank details; finance paid invoices into the attacker's account for months. *Lesson: verify any payment-detail change by phone using a previously known number.*
2. **Credential harvesting via cloned login pages:** Fake "document shared with you" emails led to near-identical login pages that captured passwords. *Lesson: scrutinize unexpected "shared document" login prompts.*
3. **Executive gift card scam:** A fake "CEO" email asked for a quick gift-card purchase favor. *Lesson: verify unusual money/gift-card requests through a separate channel.*

## Module 11: Putting It All Together — The 4-Step Check

1. **Were you expecting this?**
2. **Does the sender match?** (full address/number, not just display name)
3. **Where does the link or QR code actually go?**
4. **Is there pressure to act fast or keep it secret?**

**If in doubt:** Don't click, don't reply, don't scan. Verify independently and report to IT/security.

## Final Quiz

The course ends with a **15-question multiple-choice quiz** covering all topics above (e.g., spotting fake domains, what HTTPS does and doesn't guarantee, MFA fatigue, smishing/vishing/quishing, BEC patterns, and the safest way to access a bank's website). Scoring bands:

| Score | Result |
|---|---|
| 87%+ | Phishing Defense Expert |
| 60–86% | Solid awareness — review a few areas |
| Below 60% | Worth a second pass through the modules |

---

### About the file
The original `Phishing-Awareness-Training_.html` is a fully interactive, single-page web app (dark "case-file" themed UI) with:
- A module grid showing progress (completed modules tracked via `sessionStorage`)
- 9 expandable lesson modules with examples, mock phishing emails/texts, and color-coded callouts (tips/warnings/examples)
- A shuffled 15-question final quiz with instant feedback and a results screen
