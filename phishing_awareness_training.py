#!/usr/bin/env python3
"""
Phishing Awareness Training Module
====================================
A self-contained, interactive command-line training program that teaches
users how to recognize phishing emails, fake websites, and social
engineering tactics — with real-world examples and scored quizzes.

Run with:  python3 phishing_awareness_training.py

No external dependencies. Works on Windows, macOS, and Linux.
"""

import sys
import time
import textwrap

WIDTH = 78


# ----------------------------------------------------------------------
# Display helpers
# ----------------------------------------------------------------------

def header(title):
    print("\n" + "=" * WIDTH)
    print(title.center(WIDTH))
    print("=" * WIDTH)


def subheader(title):
    print("\n" + "-" * WIDTH)
    print(" " + title)
    print("-" * WIDTH)


def wrap_print(text, indent=""):
    paragraphs = text.split("\n")
    for p in paragraphs:
        if p.strip() == "":
            print()
            continue
        wrapped = textwrap.fill(
            p, width=WIDTH - len(indent),
            initial_indent=indent, subsequent_indent=indent
        )
        print(wrapped)


def bullets(items):
    for item in items:
        wrap_print("  • " + item, indent="    ")


def pause():
    input("\n[Press Enter to continue] ")


def ask(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting training. Stay safe out there!")
        sys.exit(0)


# ----------------------------------------------------------------------
# Score tracker
# ----------------------------------------------------------------------

class ScoreTracker:
    def __init__(self):
        self.correct = 0
        self.total = 0
        self.module_scores = {}

    def record(self, module_name, correct, total):
        self.correct += correct
        self.total += total
        self.module_scores[module_name] = (correct, total)

    def percentage(self):
        if self.total == 0:
            return 0.0
        return round((self.correct / self.total) * 100, 1)

    def report(self):
        header("YOUR TRAINING REPORT")
        if not self.module_scores:
            wrap_print("You haven't completed any quizzes yet. "
                        "Go through the modules and try the quizzes!")
            return
        for module, (c, t) in self.module_scores.items():
            pct = round((c / t) * 100) if t else 0
            print(f"  {module:<35} {c}/{t}  ({pct}%)")
        print("-" * WIDTH)
        overall = self.percentage()
        print(f"  {'OVERALL SCORE':<35} {self.correct}/{self.total}  ({overall}%)")
        print()
        if overall >= 90:
            wrap_print("Excellent! You have a strong eye for phishing red flags. "
                        "Stay vigilant — attackers keep evolving their tactics.")
        elif overall >= 70:
            wrap_print("Good job! You understand most of the key concepts. "
                        "Review the sections you missed to sharpen your instincts.")
        elif overall >= 50:
            wrap_print("You're getting there. Phishing attacks rely on speed and "
                        "pressure — slow down, re-read the modules, and try again.")
        else:
            wrap_print("This is exactly why training matters. Go back through each "
                        "module carefully — recognizing these patterns could save "
                        "you or your organization from a real attack.")


TRACKER = ScoreTracker()


# ----------------------------------------------------------------------
# Quiz engine
# ----------------------------------------------------------------------

def run_quiz(module_name, questions):
    """
    questions: list of dicts:
        {
          "q": "question text",
          "options": ["a", "b", "c", "d"],
          "answer": index_of_correct_option,
          "explain": "why this is correct"
        }
    """
    subheader(f"QUIZ: {module_name}")
    wrap_print("Answer by typing the number of your choice, then press Enter.\n")

    correct_count = 0
    for i, item in enumerate(questions, 1):
        print(f"\nQ{i}. {item['q']}")
        for idx, opt in enumerate(item["options"], 1):
            print(f"   {idx}. {opt}")

        while True:
            raw = ask("Your answer: ")
            if raw.isdigit() and 1 <= int(raw) <= len(item["options"]):
                choice = int(raw) - 1
                break
            print("   Please enter a valid option number.")

        if choice == item["answer"]:
            print("   ✅ Correct!")
            correct_count += 1
        else:
            correct_letter = item["options"][item["answer"]]
            print(f"   ❌ Not quite. The correct answer was: {correct_letter}")
        wrap_print("   " + item["explain"], indent="   ")

    print(f"\nModule quiz result: {correct_count}/{len(questions)} correct.")
    TRACKER.record(module_name, correct_count, len(questions))
    pause()


# ----------------------------------------------------------------------
# MODULE 1: What is Phishing?
# ----------------------------------------------------------------------

def module_intro():
    header("MODULE 1: WHAT IS PHISHING?")
    wrap_print(
        "Phishing is a type of social engineering attack where criminals "
        "impersonate a trusted person, brand, or organization to trick you "
        "into handing over sensitive information (passwords, card numbers, "
        "company data) or into taking an action that helps the attacker "
        "(clicking a link, opening an attachment, approving a payment)."
    )

    subheader("Common types of phishing")
    bullets([
        "Email phishing: Mass emails sent to thousands of people, hoping a "
        "small percentage will fall for it.",
        "Spear phishing: A targeted attack aimed at a specific person or "
        "organization, using personal details to appear more convincing.",
        "Whaling: Spear phishing aimed at senior executives or high-value "
        "targets, often impersonating a CEO or CFO.",
        "Smishing: Phishing carried out via SMS/text messages, often with a "
        "fake delivery notice or bank alert link.",
        "Vishing: Voice phishing — a phone call where the attacker poses as "
        "tech support, a bank, or a government agency.",
        "Clone phishing: A near-identical copy of a legitimate email you've "
        "received before, resent with a malicious link swapped in.",
        "Business Email Compromise (BEC): Attackers impersonate an executive "
        "or vendor to trick an employee into wiring money or sharing data.",
    ])

    subheader("Why it works")
    wrap_print(
        "Phishing doesn't rely on breaking encryption or hacking software — "
        "it exploits human trust, urgency, and habit. Even highly trained "
        "professionals fall for well-crafted phishing attempts, which is "
        "why awareness training is one of the most effective defenses an "
        "organization can invest in."
    )
    pause()

    questions = [
        {
            "q": "What is the main thing phishing attacks exploit?",
            "options": [
                "Weaknesses in encryption algorithms",
                "Human trust, urgency, and habit",
                "Outdated antivirus software",
                "Slow internet connections",
            ],
            "answer": 1,
            "explain": "Phishing is fundamentally a social engineering "
                       "technique — it targets people, not just systems.",
        },
        {
            "q": "An attacker impersonating your company's CFO to trick an "
                 "employee into wiring money is an example of:",
            "options": ["Smishing", "Vishing", "Business Email Compromise", "Clone phishing"],
            "answer": 2,
            "explain": "BEC scams impersonate executives/vendors to "
                       "authorize fraudulent payments or data transfers.",
        },
        {
            "q": "A phishing attack carried out over a phone call is called:",
            "options": ["Whaling", "Vishing", "Smishing", "Spear phishing"],
            "answer": 1,
            "explain": "'Vishing' = voice + phishing, typically impersonating "
                       "support staff, banks, or officials over the phone.",
        },
        {
            "q": "Spear phishing differs from regular email phishing because it:",
            "options": [
                "Is sent to millions of random addresses",
                "Is highly targeted using personal/organizational details",
                "Only happens over text messages",
                "Never contains malicious links",
            ],
            "answer": 1,
            "explain": "Spear phishing is personalized and targeted, making "
                       "it harder to spot than generic mass phishing.",
        },
    ]
    run_quiz("Module 1: Intro to Phishing", questions)


# ----------------------------------------------------------------------
# MODULE 2: Recognizing Phishing Emails
# ----------------------------------------------------------------------

def module_email_recognition():
    header("MODULE 2: RECOGNIZING PHISHING EMAILS")

    subheader("Red flags to look for")
    bullets([
        "Mismatched or spoofed sender address: The display name looks "
        "legitimate, but the actual email address (hover or tap to reveal) "
        "is a slightly altered domain, e.g. 'support@paypa1.com'.",
        "Urgency or fear tactics: 'Your account will be suspended in 24 "
        "hours', 'Unusual sign-in attempt detected', 'Payment overdue'.",
        "Generic greetings: 'Dear Customer' instead of your actual name, "
        "especially from a service that normally personalizes emails.",
        "Suspicious links: The visible link text says one thing, but "
        "hovering over it reveals a completely different, unfamiliar URL.",
        "Unexpected attachments: Invoices, 'voicemails', or shipping labels "
        "you weren't expecting — especially .zip, .exe, or macro-enabled "
        "Office files.",
        "Requests for sensitive info: Legitimate companies almost never ask "
        "you to email or text your password, full card number, or OTP.",
        "Poor grammar or odd phrasing: Not always present (skilled "
        "attackers proofread), but still a common giveaway.",
        "Too-good-to-be-true offers: Lottery wins, unexpected refunds, or "
        "huge prizes you never entered to win.",
    ])

    subheader("Quick check before you click")
    bullets([
        "Hover over (don't click) any link to preview the real destination URL.",
        "Check the sender's full email address, not just the display name.",
        "Ask yourself: 'Was I expecting this email?'",
        "If it claims to be from a colleague or company, verify through a "
        "separate channel (call them, message them on Slack/Teams) before acting.",
        "Look at the email header/metadata if your client allows it — "
        "the 'Reply-To' address often differs from the 'From' address in fakes.",
    ])
    pause()

    questions = [
        {
            "q": "You receive an email from 'Amazon Support' but the address "
                 "is support@arnazon-secure.net. This is most likely:",
            "options": [
                "A normal Amazon subdomain",
                "A spoofed/lookalike domain used in phishing",
                "Proof the email is safe since it mentions Amazon",
                "An Amazon Prime renewal notice",
            ],
            "answer": 1,
            "explain": "Lookalike domains (swapped letters, extra words, "
                       "wrong TLDs) are a classic phishing technique.",
        },
        {
            "q": "Which of these is the strongest phishing red flag?",
            "options": [
                "The email was sent during business hours",
                "The email asks you to urgently verify your password via a link",
                "The email includes the company's logo",
                "The email was sent to multiple people",
            ],
            "answer": 1,
            "explain": "Urgent requests to 'verify' or 'confirm' credentials "
                       "via a link are one of the most common phishing patterns.",
        },
        {
            "q": "Before clicking a link in an email, you should:",
            "options": [
                "Click it quickly before the offer expires",
                "Forward it to a friend to check first",
                "Hover over it to preview the actual destination URL",
                "Reply to the sender asking if it's safe",
            ],
            "answer": 2,
            "explain": "Hovering (or long-pressing on mobile) reveals the "
                       "real URL without visiting the potentially dangerous site.",
        },
        {
            "q": "An email claims to be from your bank and asks you to reply "
                 "with your full card number and OTP to 'verify your account'. "
                 "You should:",
            "options": [
                "Reply with the details since it's your bank",
                "Never share this; contact your bank directly via their "
                "official number/app instead",
                "Forward the OTP only, not the card number",
                "Ignore it completely and delete without reporting",
            ],
            "answer": 1,
            "explain": "Legitimate banks never ask for full card numbers or "
                       "OTPs over email. Always verify through official channels.",
        },
    ]
    run_quiz("Module 2: Email Recognition", questions)


# ----------------------------------------------------------------------
# MODULE 3: Recognizing Fake Websites
# ----------------------------------------------------------------------

def module_fake_websites():
    header("MODULE 3: RECOGNIZING FAKE WEBSITES")

    subheader("How attackers build convincing fake sites")
    bullets([
        "Typosquatting: Registering domains that are common misspellings of "
        "real ones (e.g., 'goggle.com', 'facebok.com').",
        "Lookalike subdomains: 'secure-paypal.com.verify-login.info' — the "
        "real-looking word is buried inside a domain you don't actually own "
        "or control.",
        "Cloned design: Copying the exact HTML/CSS of a real login page so "
        "it looks pixel-perfect.",
        "Fake padlock confidence: HTTPS (the padlock icon) only means the "
        "connection is encrypted — it does NOT mean the site is legitimate. "
        "Attackers can get HTTPS certificates for fake sites too.",
        "URL shorteners: Hiding the real destination behind bit.ly or "
        "similar shortened links.",
        "Pop-up urgency: Fake virus warnings or 'account locked' banners "
        "designed to make you panic and act fast.",
    ])

    subheader("How to verify a website before entering credentials")
    bullets([
        "Read the full domain name carefully, right to left from the first "
        "single slash — that's the real owner (e.g. in "
        "'login.paypal.com.fake-domain.net/path', the real domain is "
        "'fake-domain.net', not paypal.com).",
        "Type the website address directly into the browser instead of "
        "clicking a link, especially for banking or login pages.",
        "Use a saved bookmark for sites where you log in regularly.",
        "Check for consistent branding, working internal links, and a real "
        "'Contact Us' or 'About' page — fake sites are often thin and rushed.",
        "If a password manager doesn't auto-fill credentials on a site "
        "where it normally would, that's a strong sign you're on a "
        "different (fake) domain.",
    ])
    pause()

    questions = [
        {
            "q": "The padlock icon (HTTPS) in your browser means:",
            "options": [
                "The website is definitely safe and legitimate",
                "The connection is encrypted, but the site could still be "
                "fake or malicious",
                "The website has been verified by the government",
                "The site cannot contain phishing forms",
            ],
            "answer": 1,
            "explain": "HTTPS only encrypts the connection — it says nothing "
                       "about whether the site itself is trustworthy.",
        },
        {
            "q": "In the URL 'login.bank.com.account-verify.ru/secure', the "
                 "real domain that owns this page is:",
            "options": ["bank.com", "login.bank.com", "account-verify.ru", "secure"],
            "answer": 2,
            "explain": "The actual registered domain is read from the part "
                       "right before the first single slash: 'account-verify.ru'.",
        },
        {
            "q": "The safest way to visit your bank's website is to:",
            "options": [
                "Click the link in an email claiming to be from the bank",
                "Search for it and click the first result",
                "Type the known address directly or use a saved bookmark",
                "Use a link shared in a text message",
            ],
            "answer": 2,
            "explain": "Typing the address yourself or using a trusted "
                       "bookmark avoids any tampering in links from emails/texts.",
        },
        {
            "q": "Registering 'amaz0n-deals.com' to trick users visually is "
                 "an example of:",
            "options": ["Whaling", "Typosquatting", "Vishing", "Tailgating"],
            "answer": 1,
            "explain": "Typosquatting relies on small visual swaps (0 for o, "
                       "extra letters) that are easy to miss at a glance.",
        },
    ]
    run_quiz("Module 3: Fake Websites", questions)


# ----------------------------------------------------------------------
# MODULE 4: Social Engineering Tactics
# ----------------------------------------------------------------------

def module_social_engineering():
    header("MODULE 4: SOCIAL ENGINEERING TACTICS")
    wrap_print(
        "Social engineering is the psychological manipulation behind "
        "phishing. Attackers lean on well-known human tendencies to lower "
        "your guard."
    )

    subheader("Common psychological levers")
    bullets([
        "Authority: Impersonating a boss, IT admin, police officer, or tax "
        "agency so the target feels they must comply.",
        "Urgency/Fear: 'Act now or lose access' — designed to make you skip "
        "your normal caution.",
        "Scarcity: 'Only 2 spots left' or 'Offer expires in 1 hour' to "
        "rush a decision.",
        "Reciprocity: Offering something small first (a 'free gift' or "
        "'refund') to make you feel obligated to respond.",
        "Trust/Familiarity: Pretending to be a known coworker, friend, or "
        "vendor — often using info gathered from social media.",
        "Curiosity: Subject lines like 'Is this you in this photo?' that "
        "are hard to resist clicking.",
        "Pretexting: Inventing a believable scenario (e.g., 'I'm from IT, "
        "I need your password to fix an issue') to extract information.",
        "Tailgating/Piggybacking: A physical-world tactic — following an "
        "employee through a secure door without their own access badge.",
        "Quid pro quo: Offering a service or favor in exchange for "
        "information or access.",
    ])

    subheader("Why these work even on careful people")
    wrap_print(
        "These tactics are designed to trigger fast, emotional decisions "
        "instead of slow, careful ones. Attackers often combine several at "
        "once — for example, an 'urgent' message from your 'boss' asking "
        "for a 'quick favor' before a meeting, layering authority, urgency, "
        "and familiarity together."
    )
    pause()

    questions = [
        {
            "q": "An email claiming to be from your IT department urgently "
                 "demanding your password to 'fix a server issue' is an "
                 "example of:",
            "options": ["Reciprocity", "Pretexting combined with authority", "Tailgating", "Quid pro quo"],
            "answer": 1,
            "explain": "It invents a believable scenario (pretexting) while "
                       "leaning on the authority of the IT department.",
        },
        {
            "q": "Following an employee through a badge-locked door without "
                 "swiping your own badge is called:",
            "options": ["Vishing", "Tailgating/Piggybacking", "Whaling", "Clone phishing"],
            "answer": 1,
            "explain": "Tailgating is a physical-world social engineering "
                       "tactic that bypasses access control technology entirely.",
        },
        {
            "q": "'Only 3 hours left to claim your refund!' is primarily "
                 "exploiting which tactic?",
            "options": ["Scarcity/urgency", "Reciprocity", "Curiosity", "Tailgating"],
            "answer": 0,
            "explain": "Artificial time pressure pushes people to act before "
                       "thinking it through carefully.",
        },
        {
            "q": "Why do social engineering tactics work even on careful, "
                 "intelligent people?",
            "options": [
                "They exploit technical vulnerabilities in software",
                "They trigger fast, emotional decision-making instead of "
                "careful thinking",
                "They only target people with no security training",
                "They require the victim to already be careless",
            ],
            "answer": 1,
            "explain": "The goal is to short-circuit deliberate thinking by "
                       "provoking fear, urgency, curiosity, or trust quickly.",
        },
    ]
    run_quiz("Module 4: Social Engineering", questions)


# ----------------------------------------------------------------------
# MODULE 5: Real-World Examples
# ----------------------------------------------------------------------

def module_real_world_examples():
    header("MODULE 5: REAL-WORLD EXAMPLES")
    wrap_print(
        "These well-documented incidents show how phishing and social "
        "engineering play out in practice — and why even large, "
        "well-resourced organizations can be affected."
    )

    subheader("1. Fake 'Google Docs' sharing invite (2017)")
    wrap_print(
        "A worm spread rapidly via emails that looked like a normal Google "
        "Docs sharing invitation. Clicking the link took users to a real "
        "Google sign-in page, but the action actually granted a malicious "
        "third-party app permission to access the victim's account and "
        "contacts — which let it auto-send itself to everyone in their "
        "address book within minutes."
    )

    subheader("2. Targeted spear-phishing of a political campaign (2016)")
    wrap_print(
        "A campaign staffer received what looked like a routine Google "
        "security alert asking them to change their password due to a "
        "suspicious login. The link led to a convincing fake Google login "
        "page. Entering credentials there handed the attacker direct access "
        "to the real account — illustrating how a single click on a "
        "well-crafted spear-phishing email can lead to a major data breach."
    )

    subheader("3. Vishing-driven corporate account takeover (2020)")
    wrap_print(
        "Attackers called employees at a major social media company while "
        "posing as internal IT staff, convincing some to share credentials "
        "or approve access through what looked like a legitimate internal "
        "tool. This gave the attackers access to internal administrative "
        "systems, which were then used to take over a number of "
        "high-profile verified accounts."
    )

    subheader("4. Business Email Compromise / fake invoice fraud")
    wrap_print(
        "A recurring pattern across many companies: attackers either "
        "compromise or spoof a vendor's or executive's email account, then "
        "send a finance employee a seemingly routine invoice or wire "
        "transfer request with slightly altered banking details. Because "
        "the email looks authentic and references real projects or "
        "vendors, large sums have been transferred before anyone notices "
        "the change in account details. Losses from this category of fraud "
        "are consistently among the highest of all cybercrime types "
        "reported to law enforcement each year."
    )

    subheader("5. Fake delivery/SMS phishing (smishing)")
    wrap_print(
        "Text messages claiming a package 'could not be delivered' or that "
        "a small customs fee is due, with a link to a fake courier-branded "
        "page asking for card details. These spike heavily around major "
        "shopping seasons when people are genuinely expecting deliveries."
    )

    subheader("Common thread across all examples")
    bullets([
        "The attack rarely required advanced technical hacking — it relied "
        "on a believable story and a moment of reduced caution.",
        "A single compromised account or click was often enough to cause "
        "large-scale damage.",
        "Verification through a second, independent channel (a phone call, "
        "an in-person check) would have stopped each of these.",
    ])
    pause()

    questions = [
        {
            "q": "In the 2017 fake 'Google Docs' worm, what made it spread "
                 "so fast?",
            "options": [
                "It exploited a software bug in Gmail's servers",
                "Clicking the link granted a malicious app permission to "
                "the victim's contacts, which it then auto-messaged",
                "It was sent by a government agency",
                "It required no user interaction at all",
            ],
            "answer": 1,
            "explain": "The worm abused OAuth permissions, not a software "
                       "vulnerability — a reminder to review third-party app "
                       "access permissions on your accounts.",
        },
        {
            "q": "What is the common thread across the real-world examples "
                 "in this module?",
            "options": [
                "They all required advanced hacking tools",
                "They all relied on a believable story and a moment of "
                "reduced caution rather than technical exploits",
                "They only affected small businesses",
                "None of them could have been prevented",
            ],
            "answer": 1,
            "explain": "Every example hinged on human trust and timing, not "
                       "on breaking through technical security controls.",
        },
        {
            "q": "What single habit would have stopped most of these "
                 "real-world incidents?",
            "options": [
                "Using a faster internet connection",
                "Verifying unusual requests through a separate, independent "
                "channel before acting",
                "Disabling email entirely",
                "Using a longer Wi-Fi password",
            ],
            "answer": 1,
            "explain": "A quick phone call or in-person check to confirm an "
                       "unusual request is one of the most effective phishing "
                       "defenses available.",
        },
    ]
    run_quiz("Module 5: Real-World Examples", questions)


# ----------------------------------------------------------------------
# MODULE 6: Best Practices
# ----------------------------------------------------------------------

def module_best_practices():
    header("MODULE 6: BEST PRACTICES & PREVENTION TIPS")

    subheader("Personal habits")
    bullets([
        "Pause before clicking. Urgency is a tactic — give yourself 30 "
        "seconds to think.",
        "Verify unusual requests (especially ones involving money or "
        "credentials) through a second channel: call the person, don't "
        "reply to the same email/text.",
        "Hover over links and check sender addresses before trusting an email.",
        "Never reuse passwords across sites — use a password manager.",
        "Enable Multi-Factor Authentication (MFA) on every account that "
        "supports it. Even if a password leaks, MFA can stop the takeover.",
        "Keep your browser, OS, and apps updated to patch known vulnerabilities.",
        "Type known website addresses directly rather than clicking links "
        "for sensitive logins (banking, email, work systems).",
    ])

    subheader("Organizational habits")
    bullets([
        "Run regular phishing simulations and awareness training (like "
        "this module) for all employees.",
        "Set up a simple, well-known way to report suspicious emails "
        "(e.g., a 'Report Phishing' button or a dedicated security inbox).",
        "Use email authentication standards (SPF, DKIM, DMARC) to make "
        "spoofing your domain harder.",
        "Require dual-approval for wire transfers or changes to vendor "
        "banking details above a certain amount.",
        "Maintain an incident response plan so people know what to do "
        "immediately after a suspected compromise (change passwords, "
        "notify IT/security, isolate the device).",
    ])

    subheader("If you think you've already clicked something suspicious")
    bullets([
        "Disconnect the device from the internet/network if possible.",
        "Change the password for the affected account immediately from a "
        "different, trusted device.",
        "Enable or check MFA settings on the account.",
        "Report it to your IT/security team or the impersonated "
        "organization right away — speed matters.",
        "Monitor accounts and statements for unusual activity afterward.",
    ])
    pause()

    questions = [
        {
            "q": "What is the single most effective technical control "
                 "against credential-based phishing, even if a password is stolen?",
            "options": [
                "A longer email signature",
                "Multi-Factor Authentication (MFA)",
                "Changing your email font",
                "Disabling spell-check",
            ],
            "answer": 1,
            "explain": "MFA adds a second proof of identity, which blocks "
                       "most account takeovers even after a password leak.",
        },
        {
            "q": "If you suspect you've clicked a phishing link and entered "
                 "your password, your FIRST step should be to:",
            "options": [
                "Wait a day to see if anything happens",
                "Immediately change the password from a different, trusted "
                "device and report it",
                "Reply to the sender asking them to undo it",
                "Delete the email and do nothing else",
            ],
            "answer": 1,
            "explain": "Fast action — changing credentials and reporting — "
                       "limits how much damage an attacker can do.",
        },
        {
            "q": "Why should organizations require dual-approval for large "
                 "wire transfers?",
            "options": [
                "It slows down legitimate business unnecessarily",
                "It adds a second check that can catch a fraudulent "
                "BEC-style request before money is sent",
                "It is a legal requirement everywhere",
                "It replaces the need for any other security measure",
            ],
            "answer": 1,
            "explain": "A second set of eyes is often enough to catch subtle "
                       "red flags in a fraudulent payment request.",
        },
        {
            "q": "Which habit best protects you against reused, leaked "
                 "passwords?",
            "options": [
                "Using the same strong password everywhere",
                "Using a password manager with unique passwords per site",
                "Writing passwords on a sticky note",
                "Changing your password once a year",
            ],
            "answer": 1,
            "explain": "Unique passwords per site mean a breach on one "
                       "service can't be used to access your other accounts.",
        },
    ]
    run_quiz("Module 6: Best Practices", questions)


# ----------------------------------------------------------------------
# Cheat sheet
# ----------------------------------------------------------------------

def cheat_sheet():
    header("QUICK-REFERENCE CHEAT SHEET")
    subheader("Before you click, ask yourself...")
    bullets([
        "Was I expecting this message?",
        "Does the sender's actual address match who they claim to be?",
        "Is this creating urgency, fear, or excitement to rush me?",
        "Does the link's real destination (hover/long-press) match what's "
        "claimed?",
        "Is this request for money, credentials, or sensitive data unusual "
        "for this sender?",
        "Could I verify this through a separate channel before acting?",
    ])
    wrap_print("\nIf you answer 'no' or 'unsure' to any of these — stop, "
               "verify independently, and don't click, reply, or pay.")
    pause()


# ----------------------------------------------------------------------
# Main menu
# ----------------------------------------------------------------------

def main_menu():
    while True:
        header("PHISHING AWARENESS TRAINING")
        wrap_print(
            "Welcome! This interactive module covers how to recognize "
            "phishing emails and fake websites, common social engineering "
            "tactics, real-world examples, and practical defense tips. "
            "Each module ends with a short quiz."
        )
        print()
        print("  1. Module 1 - What is Phishing?")
        print("  2. Module 2 - Recognizing Phishing Emails")
        print("  3. Module 3 - Recognizing Fake Websites")
        print("  4. Module 4 - Social Engineering Tactics")
        print("  5. Module 5 - Real-World Examples")
        print("  6. Module 6 - Best Practices & Prevention")
        print("  7. Quick-Reference Cheat Sheet")
        print("  8. View My Training Report (scores)")
        print("  0. Exit")

        choice = ask("\nSelect an option: ")

        if choice == "1":
            module_intro()
        elif choice == "2":
            module_email_recognition()
        elif choice == "3":
            module_fake_websites()
        elif choice == "4":
            module_social_engineering()
        elif choice == "5":
            module_real_world_examples()
        elif choice == "6":
            module_best_practices()
        elif choice == "7":
            cheat_sheet()
        elif choice == "8":
            TRACKER.report()
            pause()
        elif choice == "0":
            TRACKER.report()
            print("\nThanks for completing the training. Stay alert, and "
                  "when in doubt — verify before you click!\n")
            sys.exit(0)
        else:
            print("Invalid option, please try again.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nExiting training. Stay safe out there!")
        sys.exit(0)
