# Alliance K9 Website — Master Codex Implementation Instructions

## How Codex Should Use This File

Read this file completely before editing code. Treat it as the primary implementation instruction set for the Alliance K9 MVP website.

Primary goals:

1. Replace filler copy with approved launch-ready copy.
2. Preserve the existing design and Heritage Luxury visual system.
3. Keep implementation staged and controlled.
4. Do not redesign components unless required for readability or functionality.
5. Prepare the site for production launch at `https://alliancek9dogs.com`.

---

# 1. Global Brand Direction

## Brand Positioning

**Working-Bred. Family-Raised. Purpose-Matched.**

Alliance K9 should feel like a premium, professional breeder/trainer brand. The site should communicate serious working genetics, thoughtful puppy placement, training knowledge, and emotional trust.

## Approved Visual Direction

**A2 — Heritage Luxury**

Visual tone:

- Dark cinematic backgrounds
- Midnight black and graphite panels
- Burnished gold accents
- Ivory text
- Editorial photography
- Premium spacing
- Elegant typography
- Warm but professional copy

## Color Palette

| Role | Color | Hex |
|---|---|---|
| Primary Background | Midnight Black | `#0D0D0D` |
| Secondary Background | Graphite | `#1B1B1B` |
| Accent | Burnished Gold | `#B08D57` |
| Main Text | Ivory | `#F2F2F2` |
| Secondary Text | Stone Gray | `#A3A3A3` |

## Typography

Recommended:

- Headings: `Cinzel`
- Body: `Inter`

Fallbacks:

- Heading fallback: Georgia, serif
- Body fallback: system-ui, sans-serif

## Marketing Philosophy

Use confidence-based marketing.

Use:

- Real scarcity
- Social proof
- Honest SOLD / Reserved labels
- Premium restraint
- Clear placement process
- Strong photography
- Professional evaluation language

Avoid:

- Fake urgency
- “ACT NOW” language
- Exaggerated guarantees
- Overstated working claims
- High-pressure sales tactics
- Tactical/military cosplay language

Preferred language:

- showing promise
- early observations suggest
- may be well suited for
- potential candidate
- appears to have
- recommended fit
- placement guidance

Avoid unsupported guarantees:

- guaranteed protection dog
- will be perfect for families
- will never be fearful
- fully trained
- certified
- police dog quality
- attack dog
- weaponized dog
- unstoppable protection

---

# 2. MVP Routes

The MVP includes these routes:

```text
/
/puppies/
/puppies/[slug]/
/parents/
/training/
/apply/
/gallery/
/contact/
```

Do not add blog, client portal, online payments, booking calendar, authentication, CRM, or complex backend unless explicitly instructed later.

---

# 3. Homepage Copy Implementation

## Route

```text
/
```

## Purpose

Set the site voice and brand identity. The homepage should create emotional trust, explain what Alliance K9 offers, and route users to puppies, application, parents, training, gallery, and contact pages.

## Hero Section

Eyebrow:

```text
Alliance K9 Puppies
```

Headline:

```text
Working-Bred. Family-Raised. Purpose-Matched.
```

Subheadline:

```text
Purpose-bred Dutch Shepherd and Belgian Malinois puppies raised with professional training insight, early socialization, and careful placement for working homes, active families, and devoted companions.
```

Primary CTA:

```text
View Available Puppies
```

Secondary CTA:

```text
Start an Application
```

## Trust Strip

```text
Professional K9 Background
Training experience guides every placement.
```

```text
Early Puppy Evaluation
Each puppy is observed for temperament, drive, confidence, and engagement.
```

```text
Working Bloodlines
Ranger × Mila combines serious working genetics with stable family integration.
```

```text
Placement-Focused
The right match matters more than rushing a sale.
```

## Intro / Brand Statement

Headline:

```text
Purpose-Bred Dogs, Raised With Intention
```

Body:

```text
At Alliance K9, puppies are raised with the same mindset that guides our training: clarity, structure, relationship, and long-term success. This litter is being carefully observed from birth through placement to help identify each puppy’s natural drives, temperament, confidence, and best-fit home.
```

```text
Whether you are looking for a family protection prospect, an active companion, or a serious working dog, our goal is to help place the right puppy with the right person.
```

## Current Litter Preview

Headline:

```text
Ranger × Mila Litter
```

Subheadline:

```text
Born March 21, 2026 — 12 puppies, 6 males and 6 females.
```

Body:

```text
This litter brings together Ranger’s KNPV Dutch Shepherd lineage and Mila’s strong Belgian Malinois working background. The puppies are showing a range of personalities, from affectionate family-oriented companions to high-drive working prospects.
```

```text
Each puppy profile includes individual notes on temperament, drive, affection, confidence, and recommended fit.
```

CTA:

```text
Meet the Puppies
```

## Puppy Preview Cards Section

Headline:

```text
Meet the Current Puppies
```

Intro:

```text
Every puppy is evaluated as an individual. Browse current profiles to learn more about each pup’s personality, strengths, and placement status.
```

Status language:

```text
Available
Reserved
SOLD — Found His Home
Pending Conversation
Evaluation Hold
```

Sold similar CTA:

```text
Looking for a similar prospect? View available puppies.
```

## Meet the Parents Preview

Headline:

```text
Built on Proven Foundations
```

Body:

```text
Ranger and Mila were selected for more than appearance alone. Their pairing reflects the traits Alliance K9 values most: confidence, drive, intelligence, nerve, affection, and the ability to live closely with people.
```

```text
Ranger brings strong Dutch Shepherd working heritage and a composed, capable presence. Mila contributes intensity, athleticism, obedience, and a deeply affectionate maternal temperament.
```

```text
Together, they have produced a litter with real range — from serious working candidates to loyal active companions.
```

CTA:

```text
Meet Ranger & Mila
```

## Training Preview

Headline:

```text
Training Support Beyond Placement
```

Body:

```text
Alliance K9 is built on professional training, not just breeding. Puppy buyers and training clients benefit from practical guidance rooted in structure, communication, and real-world dog handling.
```

```text
From puppy foundations and obedience to protection and working-dog development, training support is available for owners who want to build a reliable relationship with their dog from the start.
```

CTA:

```text
Explore Training
```

## Placement Philosophy

Headline:

```text
The Right Dog Matters
```

Body:

```text
These puppies are not placed on looks alone. Each one is observed for temperament, confidence, affection, drive, and overall suitability so we can help guide buyers toward a puppy that fits their lifestyle and goals.
```

```text
Some puppies are better suited for experienced working homes. Others may be ideal for active families seeking a loyal, trainable companion. The goal is not simply to sell a puppy — it is to create a successful long-term match.
```

CTA:

```text
Start the Placement Conversation
```

## Gallery Preview

Headline:

```text
Raised From Day One
```

Body:

```text
From newborn milestones to outdoor exploration, this litter has been documented throughout development. View the gallery for puppy portraits, group photos, parent images, and training moments from Alliance K9.
```

CTA:

```text
View Gallery
```

## Final CTA

Headline:

```text
Find Your Future Partner
```

Body:

```text
Whether you are seeking a working prospect, family protection candidate, or active companion, Alliance K9 is committed to honest evaluation, thoughtful placement, and long-term support.
```

Primary CTA:

```text
Apply for a Puppy
```

Secondary CTA:

```text
Contact Alliance K9
```

## Homepage Metadata

Title:

```text
Alliance K9 Puppies & Working Dogs
```

Meta description:

```text
Purpose-bred Dutch Shepherd and Belgian Malinois puppies from Alliance K9, raised with professional training insight, early evaluation, and intentional placement.
```

OG image:

```text
/assets/processed/homepage/mila-puppy-hero.webp
```

---

# 4. Available Puppies Page Copy Implementation

## Route

```text
/puppies/
```

## Purpose

Present the current Ranger × Mila litter clearly and professionally. Help visitors understand availability, individual puppy profiles, placement philosophy, and next steps.

## Hero Section

Eyebrow:

```text
Current Litter
```

Headline:

```text
Ranger × Mila Puppies
```

Subheadline:

```text
Purpose-bred Dutch Shepherd and Belgian Malinois puppies raised with early socialization, professional training insight, and careful placement for working homes, active families, and devoted companions.
```

Primary CTA:

```text
View Puppy Profiles
```

Secondary CTA:

```text
Start an Application
```

## Litter Snapshot Section

Headline:

```text
Born March 21, 2026
```

Body:

```text
The Ranger × Mila litter includes 12 puppies — 6 males and 6 females — each being individually observed for temperament, confidence, affection, prey drive, engagement, and overall placement suitability.
```

Stat cards:

```text
12 Puppies
6 Males
6 Females
Ranger × Mila
Applications Open
Born 03.21.2026
```

## Placement Philosophy Section

Headline:

```text
Each Puppy Is Evaluated as an Individual
```

Body:

```text
No two puppies in this litter are exactly alike. Some are showing stronger working potential, while others may be better suited for active companion homes or family protection roles. Alliance K9 evaluates each puppy’s natural drives, nerves, social engagement, affection, and ability to settle so buyers can make a more informed decision.
```

```text
The goal is not simply to place puppies quickly. The goal is to help each puppy land in the right home with the right expectations, support, and long-term fit.
```

## Puppy Grid Section

Headline:

```text
Meet the Puppies
```

Intro:

```text
Browse each puppy’s profile for photos, temperament notes, drive observations, recommended fit, and current placement status.
```

Each card should display:

- Puppy name
- Sex
- Collar color
- Status badge
- 2–4 trait chips
- Short description
- CTA button

Card CTA:

```text
View Profile
```

Status labels:

```text
Available
Reserved
SOLD — Found His Home
Pending Conversation
Evaluation Hold
```

Sold card subtext:

```text
Looking for a similar prospect? View available puppies.
```

Do not gray out sold puppies so heavily that they look broken. Sold puppies should remain attractive and useful as social proof while clearly unavailable.

## Scarcity / Social Proof Note

Approved subtle language:

```text
As puppies are matched and reserved, their status will be updated here. Serious buyers are encouraged to begin the conversation early so there is time to discuss goals, experience, and fit.
```

Do not use:

```text
Hurry!
Only a few left!
Act now!
Going fast!
```

## Recommended Fit Explainer Section

Headline:

```text
Working Prospects, Family Protection, and Active Companions
```

Body:

```text
This litter includes a range of temperaments and drive levels. Some puppies may be better suited for experienced working homes, sport, or personal protection development. Others may be excellent candidates for active families seeking a loyal, trainable companion with strong genetics and professional guidance behind them.
```

```text
If you are unsure which puppy may be the best fit, the application process is designed to help guide that conversation.
```

CTA:

```text
Start the Placement Conversation
```

## What Comes With Each Puppy

Headline:

```text
Raised With Intention
```

Items:

```text
Early handling and socialization
Individual temperament observations
Drive and engagement notes
Deworming schedule
Veterinary records
Buyer guidance and support
Training insight from Alliance K9
Pickup and transport options
```

Body:

```text
Each puppy is raised with close observation, regular handling, and age-appropriate exposure. Buyers receive available health records, developmental notes, and guidance to help support the transition into the new home.
```

## Deposit / Reservation Process Preview

Headline:

```text
How Placement Works
```

Steps:

```text
1. Review the puppies
2. Submit an application
3. Discuss your goals and experience
4. Place a deposit to reserve pick order or selected puppy
5. Prepare for pickup or transport
6. Continue with support after placement
```

Copy:

```text
Deposits help secure placement order and confirm serious interest. Final matches are guided by puppy temperament, buyer goals, and long-term suitability.
```

If accurate, include:

```text
A $500 deposit is required to reserve a puppy or hold placement position.
```

## Final CTA Section

Headline:

```text
Ready to Meet Your Future Partner?
```

Body:

```text
If one of the puppies catches your eye, the next step is to start the application process. Tell us about your goals, experience, and home environment so we can help guide you toward the right match.
```

Primary CTA:

```text
Start an Application
```

Secondary CTA:

```text
Contact Alliance K9
```

## Metadata

Title:

```text
Available Puppies | Alliance K9 Dogs
```

Meta description:

```text
View the current Ranger × Mila litter from Alliance K9, featuring purpose-bred Dutch Shepherd and Belgian Malinois puppies evaluated for temperament, drive, confidence, and placement fit.
```

OG Title:

```text
Available Puppies | Alliance K9 Dogs
```

OG Description:

```text
Meet the current Ranger × Mila litter and view individual puppy profiles, availability, temperament notes, and placement guidance from Alliance K9.
```

OG image recommendation:

Use best group/litter image if available. If not, use the strongest puppy hero image. Avoid using Aang as the default page-level OG image long-term unless intentionally chosen.

---

# 5. Puppy Profile Page Copy Implementation

## Route

```text
/puppies/[slug]/
```

Example:

```text
/puppies/aang/
```

## Purpose

Finalize the reusable individual puppy profile template. Each puppy page should convert interest in a specific puppy into an application or inquiry.

## Tone

Use:

- early observations
- showing promise
- appears well suited for
- may be a strong candidate for
- best matched with

Avoid:

- guaranteed adult behavior
- perfect for everyone
- excessive hype
- unsupported claims

## Hero Section

Dynamic eyebrow:

```text
Available Puppy
Reserved Puppy
SOLD — Found His Home
Pending Conversation
Evaluation Hold
```

Dynamic headline:

```text
Meet {name}
```

Dynamic subheadline should use 3 trait descriptors.

Examples:

```text
Curious • Compact • High Drive
Confident • Affectionate • People-Focused
Powerful • High Drive • Handler-Focused
```

Hero body:

```text
{name} is one of the Ranger × Mila puppies being raised and evaluated through Alliance K9. Each puppy is observed for temperament, confidence, drive, affection, social engagement, and placement suitability to help guide the right long-term match.
```

Primary CTA:

```text
Apply for {name}
```

Secondary CTA:

```text
Ask About {name}
```

## Status Badge Rules

Use only:

```text
Available
Reserved
SOLD — Found His Home
Pending Conversation
Evaluation Hold
```

## Quick Profile Section

Headline:

```text
Puppy Profile
```

Required fields:

```text
Name
Sex
Collar Color
Birth Date
Current Age
Current / Recent Weight
Status
Primary Traits
Best Fit
```

Optional fields:

```text
Go-Home Timing
Litter
Parents
Notes
```

## Personality / Evaluation Section

Headline:

```text
About {name}
```

Each puppy needs a 5–7 sentence profile based on real observations.

Include:

- Temperament
- Drive
- Social orientation
- Affection level
- Confidence / nerves
- Best-fit home
- Notable size/build details

### Aang Copy

```text
Aang may be one of the smaller pups, but he brings serious intensity and drive to the table. He shows strong prey, hunt, and bite drive, attacking toys and challenges with full commitment and purpose. Nothing holds him back when he engages — he is bold, determined, and highly motivated. Aang presents as socially neutral with new people, preferring to build a tight bond with his own handler or family. Once that connection is established, he is expected to be deeply loyal and engaged. His size makes him a great option for those wanting a high-drive working dog in a more compact package. Aang is well-suited for protection work, sport, or other demanding roles where drive and determination are key.
```

### Azula Copy

```text
Azula is a confident, clear-headed female with exceptionally solid nerves — nothing in her environment seems to shake her. She is naturally curious and eager to explore, consistently engaging with new surroundings without hesitation. Her prey drive is already showing strong development, with a clear interest in toys and interactive play, along with early signs of possession when engaged. Azula is also highly people-oriented and thrives on attention, showing a strong desire to be held and connected with her handler. She is one of the more affectionate pups in the litter, which will translate into a deep, loyal bond with her future owner. This combination of confidence, drive, and handler focus makes her a strong candidate for both working roles and an engaged, active home. Azula will do best with someone who appreciates a dog that wants to be both a partner and a constant companion.
```

### Iroh Sold Copy

```text
Iroh is a well-balanced male who offers an excellent middle ground between drive and stability. He shows strong prey drive and engagement, but with a more measured approach compared to some of the higher-intensity pups in the litter. He is not one to start trouble, but he has the confidence and presence to step in when needed. Iroh is one of the larger pups in the litter, bringing both size and substance to match his temperament. Socially neutral at first, he forms strong, loyal bonds with his people and genuinely enjoys affection and close interaction. Notably, he demonstrates a better natural off switch than many at this age while still maintaining solid working potential. Iroh has found his home, but buyers interested in a similar profile may want to look closely at Zuko, Hakoda, or Bumi.
```

## Puppy Gallery

Headline:

```text
{name}'s Gallery
```

Body:

```text
A closer look at {name} from early development through current puppy evaluations.
```

Gallery requirements:

- Puppy-specific images only
- Portrait-oriented images supported
- Masonry or mixed-orientation grid
- No forced square crops
- Lightbox if implemented
- Hero image loads first
- Lazy-load gallery images

Ideal mix:

```text
Hero portrait
Standing / structure image
Movement image
Handler interaction
Personality image
Early baby photo
Group/litter image only if puppy is identifiable
```

## Early Development Section

Headline:

```text
Early Development
```

Body:

```text
Each puppy is raised with close observation, age-appropriate handling, and exposure designed to support confidence, engagement, and a smooth transition into the right home.
```

Checklist items:

```text
Early handling
Litter socialization
Outdoor exploration
Individual temperament observations
Drive and engagement notes
Veterinary records
Deworming schedule
Transition guidance
```

Do not claim completed items unless accurate.

## Best Fit Section

Headline:

```text
Best Fit for {name}
```

Template:

```text
Based on current observations, {name} appears best suited for {fit summary}. Final placement should consider handler experience, home environment, expectations, and willingness to continue training and structure.
```

Example fit categories:

```text
Active Family Companion
Family Protection Prospect
Working Home
Sport Prospect
Experienced Handler Preferred
Balanced Companion
High-Drive Compact Prospect
```

Aang example:

```text
Aang appears best suited for an active or experienced home that wants a compact, high-drive puppy with serious working potential. He may be a strong candidate for protection development, sport, or a structured family environment where drive and determination are appreciated.
```

## Parent Link Section

Headline:

```text
From Ranger × Mila
```

Body:

```text
{name} is part of the Ranger × Mila litter, combining Ranger’s KNPV Dutch Shepherd lineage with Mila’s strong Belgian Malinois working background.
```

CTA:

```text
Meet the Parents
```

## Similar Puppies Section

Headline:

```text
Looking for a Similar Puppy?
```

Body:

```text
If {name} is reserved or sold, these puppies may share similar traits or placement potential.
```

Iroh recommendations:

```text
Zuko
Hakoda
Bumi
```

Aang recommendations:

```text
Bumi
Zuko
Ty Lee
```

## Final CTA

Available version headline:

```text
Interested in {name}?
```

Available body:

```text
The next step is to start the application process so we can discuss your goals, experience, and whether {name} may be the right fit for your home.
```

Primary CTA:

```text
Apply for {name}
```

Secondary CTA:

```text
Contact Alliance K9
```

Sold version headline:

```text
{name} Has Found His Home
```

Sold body:

```text
{name} is no longer available, but several puppies from the same litter may offer similar traits, drive, or placement potential. View the available puppies or reach out for help identifying the right match.
```

Sold primary CTA:

```text
View Available Puppies
```

Sold secondary CTA:

```text
Contact Alliance K9
```

## Metadata

Dynamic title:

```text
{name} | {sex} {status} Puppy | Alliance K9 Dogs
```

Dynamic meta description:

```text
Meet {name}, a {sex} puppy from the Ranger × Mila litter at Alliance K9, evaluated for temperament, drive, confidence, affection, and placement fit.
```

Sold meta description:

```text
Meet {name}, a {sex} puppy from the Ranger × Mila litter at Alliance K9. {name} has found his home, but similar puppies may still be available.
```

OG image:

Use each puppy’s hero image.

## Required Puppy Content Fields

```text
name
slug
sex
collar
birthDate
currentAge
weightNotes
status
statusLabel
traits
bestFit
shortDescription
fullDescription
heroImage
gallery
developmentChecklist
similarPuppies
soldMessage
```

## CTA Logic

If status is Available:

```text
Apply for {name} -> /apply/?puppy={slug}
```

If query params are not implemented:

```text
Apply for {name} -> /apply/
```

If status is Reserved, Pending Conversation, or Evaluation Hold:

```text
Ask About {name} -> /contact/
```

If status is Sold:

```text
View Available Puppies -> /puppies/
```

---

# 6. Apply Page Copy Implementation

## Route

```text
/apply/
```

## Purpose

Guide serious buyers into a thoughtful puppy application. This page should feel like the beginning of a placement conversation, not a checkout page.

## Hero Section

Eyebrow:

```text
Puppy Application
```

Headline:

```text
Start the Placement Conversation
```

Subheadline:

```text
Every Alliance K9 puppy is placed with long-term fit in mind. This application helps us understand your experience, goals, lifestyle, and what kind of dog you are hoping to bring home.
```

Primary CTA:

```text
Begin Application
```

Secondary CTA:

```text
View Available Puppies
```

## Placement Philosophy Section

Headline:

```text
The Right Match Matters
```

Body:

```text
Working-line Dutch Shepherd and Belgian Malinois puppies are not one-size-fits-all dogs. Each puppy in the Ranger × Mila litter is being observed for temperament, confidence, affection, drive, engagement, and the ability to settle so we can better understand where each pup is most likely to thrive.
```

```text
The application process helps us compare your goals and home environment with what we are seeing in the puppies. Some pups may be better suited for experienced working homes, protection development, or sport. Others may be a better fit for active families wanting a loyal, trainable companion with strong genetics and support behind them.
```

```text
Our goal is not simply to place puppies quickly. Our goal is to help create successful long-term matches.
```

## Process Timeline Section

Headline:

```text
How the Placement Process Works
```

Steps:

```text
Submit an Application
Tell us about your experience, goals, home environment, and what kind of puppy you are looking for.
```

```text
Placement Conversation
We review your application and discuss which puppies may align with your needs, expectations, and handling experience.
```

```text
Deposit & Reservation
A deposit confirms serious interest and may secure placement order or a selected puppy depending on availability and fit.
```

```text
Puppy Matching
Puppy selection is guided by temperament observations, drive level, confidence, affection, and long-term suitability.
```

```text
Pickup or Transport
Once placement is confirmed, we coordinate pickup, travel, or available transport options.
```

```text
Ongoing Support
Alliance K9 remains available for guidance as your puppy transitions into the home and begins the next stage of development.
```

## Deposit Explanation Section

Headline:

```text
Deposit & Reservation
```

Body:

```text
A $500 deposit is required to reserve a puppy or hold placement position. Deposits help confirm serious interest and allow us to plan placement conversations, pickup timing, and buyer support more effectively.
```

```text
Because puppy placement is based on fit, a deposit should not be viewed as an automatic “purchase button.” Alliance K9 reserves the right to guide placement based on the puppy’s temperament, the buyer’s goals, and the long-term suitability of the match.
```

Optional if accurate:

```text
Payment options may include cash, check, or Venmo by arrangement.
```

## Application Form Section

Headline:

```text
Puppy Application
```

Intro:

```text
Please complete the application below as thoroughly as possible. Honest answers help us better understand your goals and guide the placement process.
```

Recommended fields:

Applicant Information:

```text
Full Name
Email Address
Phone Number
City / State
Preferred Contact Method
```

Puppy Interest:

```text
Preferred Puppy
Preferred Sex
Are you open to recommendations?
Desired timeline
```

Preferred Puppy options:

```text
Aang
Azula
Bumi
Hakoda
Iroh
Katara
Kyoshi
Mai
Sokka
Toph
Ty Lee
Zuko
Unsure / Need Guidance
```

Intended Role:

```text
Active family companion
Family protection prospect
Personal protection development
Sport prospect
Working dog prospect
Training companion
Unsure / need guidance
```

Experience:

```text
Have you owned a Dutch Shepherd, Belgian Malinois, German Shepherd, or similar working breed before?
Describe your dog handling experience.
Have you worked with a professional trainer before?
Do you currently have dogs in the home?
```

Home Environment:

```text
Type of home
Do you have a fenced yard?
Children in the home?
Other pets?
General activity level of household
```

Training Plans:

```text
What are your training goals?
Do you plan to continue professional training?
Are you interested in Alliance K9 training support?
```

Additional Notes:

```text
Anything else we should know?
```

## Form Helper Text

Preferred Puppy:

```text
If you are unsure, select “Need Guidance.” Puppy recommendations can be discussed based on temperament, drive, and fit.
```

Working Breed Experience:

```text
Prior working-breed experience is helpful, but not always required. Honest answers help us guide placement responsibly.
```

Training Goals:

```text
This helps us understand whether you are looking for a companion, working prospect, protection candidate, or sport/performance dog.
```

Submit button:

```text
Submit Application
```

Secondary link:

```text
Questions? Contact Alliance K9
```

Success message:

```text
Thank you for taking the time to apply. We review each application with the goal of matching the right puppy to the right home. Alliance K9 will follow up soon to discuss availability, fit, and next steps.
```

## FAQ Section

Headline:

```text
Application Questions
```

FAQ:

```text
Do I need working-dog experience?
Working-breed experience is helpful, especially for higher-drive puppies, but it is not the only factor. Placement depends on goals, lifestyle, expectations, willingness to train, and which puppy may be the right fit.
```

```text
Does applying guarantee a puppy?
No. The application begins the placement conversation. Alliance K9 may recommend a specific puppy, suggest a different match, or advise waiting depending on fit and availability.
```

```text
How does the deposit work?
A $500 deposit confirms serious interest and may secure placement order or a selected puppy once fit and availability are discussed.
```

```text
Can I choose based on looks?
Appearance matters, but temperament and fit matter more. We encourage buyers to consider each puppy’s personality, drive level, affection, confidence, and recommended placement.
```

```text
Do you offer training support?
Yes. Alliance K9 offers training support and guidance for puppy foundations, obedience, behavior, and working-dog development.
```

## Final CTA

Headline:

```text
Ready to Begin?
```

Body:

```text
If you are serious about bringing home a Ranger × Mila puppy, the application is the best next step. Tell us what you are looking for, and we will help guide the conversation from there.
```

Primary CTA:

```text
Submit Application
```

Secondary CTA:

```text
View Available Puppies
```

## Metadata

Title:

```text
Apply for a Puppy | Alliance K9 Dogs
```

Meta description:

```text
Start the Alliance K9 puppy application for the current Ranger × Mila litter. Apply for purpose-bred Dutch Shepherd and Belgian Malinois puppies placed by temperament, drive, and long-term fit.
```

OG title:

```text
Apply for a Puppy | Alliance K9 Dogs
```

OG description:

```text
Begin the Alliance K9 placement conversation for the current Ranger × Mila litter and help us match the right puppy to the right home.
```

OG image:

```text
/assets/processed/homepage/mila-puppy-hero.webp
```

---

# 7. Meet the Parents Page Copy Implementation

## Route

```text
/parents/
```

## Purpose

Introduce Ranger and Mila as the foundation of the current litter. Build confidence by showing the quality, temperament, and working background behind the puppies.

## Hero Section

Eyebrow:

```text
The Foundation of the Litter
```

Headline:

```text
Meet Ranger & Mila
```

Subheadline:

```text
The Ranger × Mila litter brings together Dutch Shepherd working heritage and Belgian Malinois drive, producing puppies raised with purpose, observation, and long-term placement in mind.
```

Primary CTA:

```text
View Available Puppies
```

Secondary CTA:

```text
Start an Application
```

## Intro Section

Headline:

```text
Built on Proven Foundations
```

Body:

```text
A strong litter starts with more than appearance. Ranger and Mila were selected for the traits Alliance K9 values most: nerve, drive, intelligence, structure, handler engagement, and the ability to live closely with people.
```

```text
This pairing was chosen to produce puppies with real potential across working, sport, protection, and active companion roles. As each puppy develops, Alliance K9 observes temperament, prey drive, confidence, affection, engagement, and the ability to settle so buyers can make informed placement decisions.
```

## Ranger Section

Headline:

```text
Ranger
```

Subheadline:

```text
Dutch Shepherd • KNPV Lineage • Sire
```

Key facts:

```text
Breed: Dutch Shepherd
Role: Sire
Lineage: KNPV line
BRN: 40274
Known for: Structure, confidence, working heritage, stable presence
```

Body:

```text
Ranger is the sire of the current litter and brings strong Dutch Shepherd working heritage to the pairing. He represents the qualities Alliance K9 values in a serious working dog: confidence, athleticism, intelligence, drive, and a composed presence around people.
```

```text
His KNPV lineage offers a strong foundation for puppies with potential in protection, sport, working roles, and active homes that understand the needs of high-drive dogs. Ranger’s influence can be seen in the litter’s structure, intensity, confidence, and early working promise.
```

```text
Ranger’s BRN is 40274, providing traceable lineage for buyers interested in his background.
```

Trait chips:

```text
KNPV Lineage
Dutch Shepherd
Confident
Athletic
Working Heritage
Composed Presence
```

## Mila Section

Headline:

```text
Mila
```

Subheadline:

```text
Belgian Malinois • Working Background • Dam
```

Key facts:

```text
Breed: Belgian Malinois
Role: Dam
Known for: Drive, obedience, athleticism, maternal temperament, affection
Background: Strong working / police-line influence
```

Body:

```text
Mila is the dam of the current litter and contributes intensity, athleticism, intelligence, and a deeply affectionate temperament. She is a high-drive Belgian Malinois with strong working influence and a clear desire to engage with her people.
```

```text
Beyond drive, Mila brings an important quality to this pairing: connection. She is attentive, expressive, and closely bonded with her people, and she has shown a strong maternal side with the puppies. That combination of working energy and social connection is a major part of what makes this litter compelling.
```

```text
Mila’s influence is especially valuable for buyers seeking a puppy with both capability and relationship — a dog that can work, train, bond, and live as part of a structured home.
```

Trait chips:

```text
Belgian Malinois
High Drive
Athletic
Affectionate
Maternal
Handler-Oriented
```

## Why This Pairing Section

Headline:

```text
Why Ranger × Mila?
```

Body:

```text
This pairing was chosen to balance working potential with temperament and handler connection. Ranger contributes Dutch Shepherd structure, working heritage, and composed confidence. Mila contributes Malinois intensity, athleticism, obedience, and social engagement.
```

```text
Together, they have produced a litter with meaningful range. Some puppies are showing strong potential for protection, sport, or working homes. Others may be excellent matches for active families seeking a loyal, trainable companion with professional guidance behind the placement.
```

```text
Because working-line puppies can vary significantly even within the same litter, Alliance K9 evaluates each puppy as an individual rather than assuming one-size-fits-all placement.
```

## Traits We Are Watching

Headline:

```text
Traits We Are Watching
```

Intro:

```text
As the litter develops, each puppy is observed for traits that matter in both working and companion homes.
```

Items:

```text
Nerve and environmental confidence
Prey drive and toy engagement
Hunt drive and curiosity
Social engagement with people
Affection and handler focus
Possession and grip tendencies
Ability to settle and recover
Overall placement suitability
```

Body:

```text
These observations help guide recommendations for each puppy. A high-drive sport prospect may not be the right match for every family, while a balanced, affectionate puppy may be ideal for an active home that values structure and training.
```

## Working Heritage Section

Headline:

```text
Working Heritage, Raised for Real Life
```

Body:

```text
The goal of this litter is not simply to produce intense dogs. The goal is to produce capable, stable, trainable dogs with the potential to succeed in the right homes. Working heritage matters, but so does daily life, relationship, structure, and responsible ownership.
```

```text
Alliance K9 approaches this litter with both a trainer’s eye and a breeder’s responsibility. The puppies are observed not only for drive and confidence, but also for how they engage with people, recover from stimulation, interact with littermates, and settle after activity.
```

## Image Guidance

Ranger primary image options:

```text
Picnic table / lake portrait
Tree + lake sitting portrait
Golden-hour walking with ball
Lake side-profile
```

Ranger bitework images should be secondary support only.

Mila primary image options:

```text
Mila with puppy
Standing structure shot
Snow standing portrait
```

Mila couch/snuggle can be secondary personality support. Bunny ears image is social/personality use only, not formal parent hero.

Do not lead this page with bitework imagery. Tone should be composed capability, not intimidation.

## Final CTA Section

Headline:

```text
Interested in the Ranger × Mila Litter?
```

Body:

```text
If you are considering one of these puppies, the next step is to review the available profiles and start the placement conversation. Alliance K9 can help guide you toward the puppy whose temperament, drive, and personality best align with your goals.
```

Primary CTA:

```text
View Available Puppies
```

Secondary CTA:

```text
Start an Application
```

## Metadata

Title:

```text
Meet Ranger & Mila | Alliance K9 Dogs
```

Meta description:

```text
Meet Ranger and Mila, the Dutch Shepherd and Belgian Malinois parents behind the current Alliance K9 litter, selected for working heritage, drive, temperament, and handler connection.
```

OG title:

```text
Meet Ranger & Mila | Alliance K9 Dogs
```

OG description:

```text
Learn about the Ranger × Mila pairing behind the current Alliance K9 litter and the traits guiding each puppy’s placement.
```

OG image recommendation:

Best option: Mila with puppy. Alternative: Ranger lake / picnic table portrait.

---

# 8. Training Page Copy Implementation

## Route

```text
/training/
```

## Purpose

Present Alliance K9 training services clearly and professionally. Support puppy buyers, local obedience clients, behavior modification inquiries, protection/working dog prospects, and owners of high-drive breeds.

## Hero Section

Eyebrow:

```text
Alliance K9 Training
```

Headline:

```text
Training With Purpose
```

Subheadline:

```text
Professional dog training built on clear communication, structure, relationship, and practical results for puppies, family companions, behavior cases, and working dogs.
```

Primary CTA:

```text
Start a Training Inquiry
```

Secondary CTA:

```text
View Puppy Program
```

## Intro / Philosophy Section

Headline:

```text
Clear Communication. Real Structure. Better Dogs.
```

Body:

```text
Alliance K9 training is built around helping dogs and handlers understand each other more clearly. Whether the goal is puppy foundations, reliable obedience, behavior improvement, or working-dog development, the foundation is the same: communication, consistency, structure, and a relationship that can hold up in real life.
```

```text
Training is not about tricks or shortcuts. It is about creating a dog that understands expectations, responds to guidance, and can function with more confidence and reliability in the home, in public, and around distractions.
```

## Training Programs Section

Headline:

```text
Training Programs
```

Intro:

```text
Every dog is different. Training recommendations are based on the dog’s temperament, age, behavior, drives, owner goals, and the level of structure needed for long-term success.
```

### Puppy Foundations

```text
Start young with structure, confidence, and clear communication. Puppy foundation work may include crate training, leash skills, engagement, confidence building, early obedience, household manners, and owner coaching.
```

Best for:

```text
Young puppies, new puppy owners, working-breed puppies, and families wanting to start correctly from day one.
```

### Obedience Training

```text
Obedience training focuses on practical, reliable skills that make daily life easier. Depending on the dog and owner goals, this may include leash manners, recall, place work, impulse control, neutrality, public manners, and handler communication.
```

Best for:

```text
Family dogs, active companions, working breeds, and owners wanting better reliability and control.
```

### Behavior Modification

```text
Behavior work addresses issues such as reactivity, poor impulse control, confidence concerns, household conflict, leash problems, and unwanted patterns that have become difficult to manage. The goal is to create more structure, better communication, and a realistic plan for improvement.
```

Best for:

```text
Dogs struggling with reactivity, anxiety, over-arousal, confidence issues, or behavior patterns that need structured intervention.
```

### Protection & Working Dog Development

```text
Working and protection development begins with honest evaluation. Not every dog is suited for this type of work. For appropriate dogs, training may focus on drive development, obedience under stimulation, handler control, confidence, engagement, and responsible progression.
```

Best for:

```text
Suitable working-breed dogs, sport prospects, personal protection candidates, and experienced handlers seeking structured development.
```

### Board & Train / Intensive Training

Only include if currently offered. If not, remove or mark availability-dependent.

```text
For dogs needing a more immersive training structure, intensive programs may be available depending on schedule, suitability, and training goals. These programs are designed to build foundation, address specific issues, and transfer skills back to the owner.
```

Best for:

```text
Owners needing more concentrated training support and dogs that are appropriate for structured handling away from home.
```

## Training Process Section

Headline:

```text
How Training Works
```

Steps:

```text
Consultation
We start by discussing your dog, your concerns, your goals, and what you want life with your dog to look like.
```

```text
Evaluation
Your dog is evaluated for temperament, behavior, drives, confidence, engagement, and handling needs.
```

```text
Training Plan
A realistic plan is built around the dog in front of us, the owner’s goals, and the level of structure needed.
```

```text
Training Work
Training focuses on clear communication, repetition, consistency, and practical application in real-world situations.
```

```text
Owner Transfer
Owners are coached on how to maintain the work, communicate clearly, and continue building progress after training.
```

```text
Long-Term Support
Training does not end when a session does. Alliance K9 focuses on helping owners understand how to keep moving forward.
```

## Training Philosophy Banner

Headline:

```text
Training the Dog in Front of Us
```

Body:

```text
No two dogs are exactly the same. A young puppy, a high-drive Malinois, a reactive family dog, and a personal protection prospect all require different handling, expectations, and progression. Alliance K9 approaches training with a practical eye toward temperament, behavior, and the owner’s real-life needs.
```

```text
The goal is not to force every dog into the same mold. The goal is to build the clearest path forward for that dog and that handler.
```

## Results / Social Proof Section

Headline:

```text
Real Dogs. Real Progress.
```

Body:

```text
Training progress comes from consistency, structure, and owner follow-through. Alliance K9 works to create practical improvements that matter in daily life — calmer handling, clearer communication, better obedience, improved confidence, and stronger relationships between dogs and their people.
```

Optional result categories:

```text
Better leash manners
Improved recall
More reliable obedience
Reduced reactivity
Improved confidence
Clearer handler communication
Stronger puppy foundations
Working-dog development
```

If testimonials are not available, use “Training Focus Areas” instead of fake testimonials. Do not fabricate client quotes.

## Puppy Buyer Training Support Section

Headline:

```text
Support for Alliance K9 Puppy Buyers
```

Body:

```text
Puppy buyers are encouraged to continue training after placement. These puppies come from working lines and benefit from structure, engagement, consistency, and clear expectations from the beginning.
```

```text
Alliance K9 can provide guidance for puppy foundations, obedience, socialization, confidence building, crate routines, leash work, and early working-dog development where appropriate.
```

CTA:

```text
Ask About Puppy Training
```

## FAQ Section

Headline:

```text
Training Questions
```

FAQ:

```text
What age should training start?
Training can begin as soon as a puppy comes home. Early work should be age-appropriate and focused on confidence, engagement, structure, crate routines, leash introduction, and basic communication.
```

```text
Do you work with behavior issues?
Yes. Behavior modification may be available depending on the dog, the issue, and safety considerations. Reactivity, over-arousal, confidence issues, leash problems, and household structure concerns can often be addressed with the right plan.
```

```text
Do you train protection dogs?
Protection and working-dog development begins with evaluation. Not every dog is suited for protection work, and responsible training requires the right temperament, drives, control, handler commitment, and long-term management.
```

```text
Do owners need to participate?
Yes. Owner involvement is essential. Training progress depends heavily on consistency, handling, expectations, and follow-through after sessions or programs are complete.
```

```text
Do you offer board and train?
Board and train or intensive options may be available depending on schedule, dog suitability, and training goals. Contact Alliance K9 to discuss current availability.
```

## Final CTA

Headline:

```text
Ready to Build a Better Relationship With Your Dog?
```

Body:

```text
Whether you are starting with a new puppy, improving obedience, addressing behavior concerns, or developing a serious working prospect, Alliance K9 can help create a practical path forward.
```

Primary CTA:

```text
Start a Training Inquiry
```

Secondary CTA:

```text
Contact Alliance K9
```

## Metadata

Title:

```text
Dog Training | Alliance K9 Dogs
```

Meta description:

```text
Professional dog training from Alliance K9 for puppies, obedience, behavior modification, protection development, and working dogs in Alabama.
```

OG title:

```text
Dog Training | Alliance K9 Dogs
```

OG description:

```text
Training built on communication, structure, and real-world results for puppies, family companions, behavior cases, and working dogs.
```

OG image recommendation:

Use Ranger walking with ball / field image, composed Ranger portrait, or strong training image. Avoid overly intense bitework as default OG image unless intentionally targeting working/protection buyers.

---

# 9. Gallery Page Copy Implementation

## Route

```text
/gallery/
```

## Purpose

Showcase the visual story behind Alliance K9: puppies, parent dogs, training moments, group/litter photos, handler interaction, socialization, and outdoor exploration.

## Hero Section

Eyebrow:

```text
Alliance K9 Media
```

Headline:

```text
The Story in Photos
```

Subheadline:

```text
A visual look at the Ranger × Mila litter, parent dogs, training moments, and the everyday handling that shapes each Alliance K9 puppy.
```

Primary CTA:

```text
View Available Puppies
```

Secondary CTA:

```text
Start an Application
```

## Intro Section

Headline:

```text
Raised, Handled, and Documented
```

Body:

```text
The Alliance K9 gallery is more than a collection of puppy pictures. It shows the development, handling, socialization, and daily life behind the dogs we raise and train.
```

```text
From newborn milestones and early handling to outdoor exploration, parent portraits, and training moments, these images help tell the story of the Ranger × Mila litter and the Alliance K9 program.
```

## Browse Gallery Section

Headline:

```text
Browse the Gallery
```

Intro:

```text
Explore photos by category to see the puppies, parents, litter development, and training work behind Alliance K9.
```

Recommended filters:

```text
All
Puppies
Group / Litter
Parents
Training
Outdoor Exploration
Handler Interaction
Development Timeline
```

Filters are optional for MVP. If not implemented, use category headings instead.

## Gallery Layout Requirements

Use masonry or mixed-orientation layout.

Requirements:

```text
Use masonry or mixed aspect-ratio layout.
Preserve portrait orientation where practical.
Do not force all images into square crops.
Use lazy loading.
Use responsive image sizes.
Use lightbox expansion if implemented.
Maintain premium spacing and dark/gold visual system.
```

Avoid:

```text
Rigid square-only grid
Aggressive center cropping
Cropping ears, eyes, muzzles, tails, or important markings
Overcrowded layout
Tiny thumbnails with no emotional impact
```

## Category Descriptions

Puppies:

```text
Individual puppy portraits, profile images, personality moments, and early development photos from the current Ranger × Mila litter.
```

Group / Litter:

```text
Group photos showing the litter together, social interaction, play, rest, and shared developmental moments.
```

Parents:

```text
Images of Ranger and Mila, the sire and dam of the current litter, including portraits, structure photos, and selected working or lifestyle images.
```

Training:

```text
Training and working-dog images that show the experience, structure, and handling behind Alliance K9.
```

Use bitework or intense working images thoughtfully. They should support credibility without making the brand feel overly aggressive or performative.

Handler Interaction:

```text
Photos showing puppies and dogs engaging with people through handling, affection, training, and everyday interaction.
```

Development Timeline:

```text
Photos showing puppies from birth through current evaluation age, including neonatal photos, early handling, outdoor exposure, and personality emergence.
```

## Caption Guidance

Good caption examples:

```text
Azula during outdoor exploration.
Ranger at the lake.
Mila with one of the Ranger × Mila puppies.
Early handling from the current litter.
Aang showing confidence during yard time.
```

Avoid:

```text
CUTEST PUPPY EVER!!!
This baby is perfect!!!
Future ultimate protection beast!!!
You need this dog now!!!
```

## Alt Text Guidance

Good alt text examples:

```text
Brindle Dutch Shepherd puppy standing in grass during outdoor evaluation.
Mila lying in grass with one of her puppies.
Ranger sitting beside a lake.
Group of Ranger × Mila puppies resting together.
Belgian Malinois puppy looking up at handler.
```

Avoid:

```text
dog image
puppy photo
image 1
gallery pic
```

## Featured Gallery Section

Headline:

```text
Featured Moments
```

Body:

```text
A few selected images that capture the heart of the Alliance K9 program — thoughtful breeding, real handling, working potential, and strong human connection.
```

Recommended images:

```text
Mila with puppy
Strong Ranger portrait
Best group/litter photo
One training image
One outdoor puppy exploration image
```

## Gallery CTA Section

Headline:

```text
See a Puppy That Stands Out?
```

Body:

```text
If one of the puppies catches your attention, visit the available puppy profiles to learn more about temperament, drive, affection, confidence, and current placement status.
```

Primary CTA:

```text
View Available Puppies
```

Secondary CTA:

```text
Start an Application
```

Optional training CTA:

Headline:

```text
Interested in Training?
```

Body:

```text
Alliance K9 also offers training support for puppies, obedience, behavior concerns, and working-dog development.
```

CTA:

```text
Explore Training
```

## Gallery Data Model

Recommended:

```ts
type GalleryCategory =
  | "puppies"
  | "group-litter"
  | "parents"
  | "training"
  | "outdoor"
  | "handler-interaction"
  | "development";

type GalleryImage = {
  src: string;
  alt: string;
  caption?: string;
  category: GalleryCategory;
  puppySlug?: string;
  featured?: boolean;
  orientation?: "portrait" | "landscape" | "square";
};
```

## Metadata

Title:

```text
Gallery | Alliance K9 Dogs
```

Meta description:

```text
View the Alliance K9 gallery featuring Ranger × Mila puppies, parent dogs, training moments, outdoor exploration, and working-dog development.
```

OG title:

```text
Gallery | Alliance K9 Dogs
```

OG description:

```text
Explore photos from Alliance K9, including the current Ranger × Mila litter, parent dogs, puppy development, and training work.
```

OG image recommendation:

Use Mila with puppy, best group/litter photo, or strong outdoor puppy exploration image. Confirm current `gallery-001.webp` is one of the strongest emotional images before public launch.

---

# 10. Contact Page Copy Implementation

## Route

```text
/contact/
```

## Purpose

Route visitors into the correct inquiry path: puppy placement, training, working/protection dog, future litter, or general question.

## Hero Section

Eyebrow:

```text
Contact Alliance K9
```

Headline:

```text
Start the Conversation
```

Subheadline:

```text
Have questions about the Ranger × Mila litter, puppy placement, training support, or working-dog development? Send a message and include as much detail as possible so we can point you in the right direction.
```

Primary CTA:

```text
Send a Message
```

Secondary CTA:

```text
View Available Puppies
```

## Contact Intro Section

Headline:

```text
How Can We Help?
```

Body:

```text
Alliance K9 works with puppy buyers, training clients, and owners seeking practical guidance for high-drive dogs. Whether you are ready to apply, interested in training, or still figuring out which puppy may be the right fit, the best next step is to reach out with clear information about your goals.
```

```text
For puppy placement questions, include which puppy or type of puppy you are interested in, your intended role, and your experience with working breeds. For training inquiries, include your dog’s age, breed, current behavior concerns, and what you want to accomplish.
```

## Inquiry Type Section

Headline:

```text
Choose the Right Inquiry Type
```

Intro:

```text
Selecting the right inquiry type helps us understand what you need and respond more efficiently.
```

Options:

Puppy Placement:

```text
Questions about the current Ranger × Mila litter, availability, temperament, application process, deposits, pickup, or transport.
```

Training:

```text
Questions about puppy foundations, obedience, behavior modification, protection development, working-dog evaluation, or ongoing support.
```

General:

```text
General questions about Alliance K9, future litters, media, referrals, or anything that does not fit the other categories.
```

## Contact Form Section

Headline:

```text
Send a Message
```

Intro:

```text
Complete the form below and include enough detail for us to understand your situation. Short messages are welcome, but thoughtful context helps us give a better answer.
```

Required fields:

```text
Full Name
Email Address
Phone Number
Inquiry Type
Message
```

Inquiry Type options:

```text
Puppy Placement
Training
Working / Protection Dog
Future Litter
General Question
```

Optional fields:

```text
Preferred Puppy
Dog Name
Dog Breed
Dog Age
Location
Preferred Contact Method
```

Helper text:

Inquiry Type:

```text
Choose the option that best fits your question. If you are unsure, select General Question.
```

Preferred Puppy:

```text
If you are asking about a specific puppy, include the puppy’s name here.
```

Training:

```text
For training inquiries, include your dog’s breed, age, behavior concerns, and training goals in the message.
```

Message:

```text
Helpful details include your goals, experience level, household environment, timeline, and any specific questions.
```

Submit button:

```text
Send Message
```

Success message:

```text
Thank you for reaching out. Your message has been received. Alliance K9 will review your inquiry and follow up with the next best step based on your goals, questions, and current availability.
```

## Direct Contact Section

Headline:

```text
Contact Details
```

Body:

```text
Use the contact form for the most complete response. If direct contact information is listed here, please include your name, inquiry type, and the best way to reach you.
```

Fields to support:

```text
Phone
Email
Location / Service Area
Facebook
Instagram
Good Dog profile if still used
```

Location copy:

```text
Based in the Birmingham, Alabama area.
```

Optional if desired:

```text
Serving Chelsea, Birmingham, and surrounding Alabama communities.
```

## What to Include Section

Headline:

```text
What to Include
```

Body:

```text
The best inquiries include context. For puppy questions, tell us what kind of dog you are looking for and what your goals are. For training questions, describe the dog in front of us and what you want to improve.
```

Helpful details:

```text
Your name and location
Which puppy or service you are interested in
Your experience with dogs or working breeds
Your goals for the dog
Current behavior or training concerns
Household environment
Timeline
Best contact method
```

## Puppy Inquiry CTA

Headline:

```text
Interested in a Puppy?
```

Body:

```text
If you are serious about the current Ranger × Mila litter, the puppy application is the best next step. The application gives Alliance K9 the context needed to discuss fit, availability, and placement.
```

CTA:

```text
Start Puppy Application
```

Link:

```text
/apply/
```

## Training Inquiry CTA

Headline:

```text
Interested in Training?
```

Body:

```text
For training support, include your dog’s age, breed, behavior concerns, and training goals. Alliance K9 can help determine whether puppy foundations, obedience, behavior work, or working-dog development may be appropriate.
```

CTA:

```text
Explore Training
```

Link:

```text
/training/
```

## Final CTA

Headline:

```text
Let’s Find the Right Next Step
```

Body:

```text
Whether you are looking for a puppy, training support, or guidance on a working-breed dog, Alliance K9 is here to help you move forward with clarity.
```

Primary CTA:

```text
Send a Message
```

Secondary CTA:

```text
View Available Puppies
```

## Metadata

Title:

```text
Contact | Alliance K9 Dogs
```

Meta description:

```text
Contact Alliance K9 for puppy placement, training inquiries, working-dog development, and questions about the current Ranger × Mila litter in Alabama.
```

OG title:

```text
Contact | Alliance K9 Dogs
```

OG description:

```text
Reach out to Alliance K9 about available puppies, puppy placement, training support, and working-dog development.
```

OG image recommendation:

Use Mila with puppy, strong puppy/handler interaction image, or strongest Alliance K9 branded image.

---

# 11. Sitewide Production Cleanup and Launch

## Production Domain

Final domain:

```text
https://alliancek9dogs.com
```

Testing domain:

```text
https://alliancek9.netlify.app
```

Before production launch, replace production-facing references from:

```text
https://alliancek9.netlify.app
```

to:

```text
https://alliancek9dogs.com
```

This applies to canonical URLs, OG URLs, Twitter URLs, sitemap, robots, and absolute social image URLs.

Netlify references may remain only in internal docs or testing notes if they do not render in production metadata.

## Required Metadata Per Page

Each public page should include:

```text
title
meta description
canonical URL
og:type
og:title
og:description
og:url
og:site_name
og:image
og:image:alt
twitter:card
twitter:title
twitter:description
twitter:image
```

Site name:

```text
Alliance K9
```

Twitter card type:

```text
summary_large_image
```

Global default OG image:

```text
/assets/processed/homepage/mila-puppy-hero.webp
```

## URL / Canonical Cleanup

Search entire codebase for:

```text
alliancek9.netlify.app
```

Replace production-facing references with:

```text
alliancek9dogs.com
```

Check:

```text
SEO component
Astro layout
site config
sitemap config
canonical URL logic
Open Graph URL logic
Twitter image URL logic
robots.txt
manifest file if present
README launch instructions
hardcoded page metadata
```

## Sitemap and Robots

If sitemap generation exists, confirm it uses:

```text
https://alliancek9dogs.com
```

Public routes:

```text
/
/puppies/
/puppies/aang/
/puppies/azula/
/puppies/bumi/
/puppies/hakoda/
/puppies/iroh/
/puppies/katara/
/puppies/kyoshi/
/puppies/mai/
/puppies/sokka/
/puppies/toph/
/puppies/ty-lee/
/puppies/zuko/
/parents/
/training/
/apply/
/gallery/
/contact/
```

Robots when production-ready:

```text
User-agent: *
Allow: /
Sitemap: https://alliancek9dogs.com/sitemap.xml
```

Use sitemap-index.xml instead if that is the generated path.

## Filler Copy Cleanup

Search terms:

```text
lorem
ipsum
placeholder
TODO
TBD
coming soon
sample
example
dummy
filler
test copy
replace me
```

No public page should contain filler copy before launch.

## CTA Link Audit

Confirm all buttons/links resolve correctly:

```text
View Available Puppies -> /puppies/
Meet the Puppies -> /puppies/
Start an Application -> /apply/
Apply for a Puppy -> /apply/
Contact Alliance K9 -> /contact/
Send a Message -> /contact/ or contact form anchor
Explore Training -> /training/
Meet Ranger & Mila -> /parents/
View Gallery -> /gallery/
```

## Puppy Status Audit

Use only these status values:

```text
Available
Reserved
Sold
Pending Conversation
Evaluation Hold
```

Display labels:

```text
Available
Reserved
SOLD — Found His Home
Pending Conversation
Evaluation Hold
```

Rules:

- Sold puppies remain visible unless explicitly hidden.
- SOLD badges must only be used for genuinely sold puppies.
- Reserved means serious hold/deposit/reservation.
- Pending Conversation means active buyer discussion, not final.
- Evaluation Hold means intentionally held back for further assessment.

Manual status review before launch:

```text
Aang
Azula
Bumi
Hakoda
Iroh
Katara
Kyoshi
Mai
Sokka
Toph
Ty Lee
Zuko
```

## Collar Reference

```text
Ty Lee = Orange
Kyoshi = Lime Green
Zuko = Black
Iroh = Grey
Aang = Red
Azula = Purple
Sokka = Light Blue
Hakoda = Dark Blue
Toph = Pink
Katara = White
Bumi = Dark Green
Mai = Yellow
```

## Image Audit

Confirm every public image:

```text
exists
loads correctly
has meaningful alt text
is web-optimized
does not awkwardly crop critical features
works on mobile
```

Avoid cropping:

```text
eyes
ears
muzzle
tail if important to posture
distinctive markings
handler interaction context
```

Gallery rules:

```text
masonry or mixed-orientation layout is active
portrait iPhone photos display well
not all images are forced into squares
lightbox works if implemented
images lazy-load
```

## Original Asset Rule

Confirm code/process does not overwrite original photos. Originals should remain untouched. Processed images should be derivatives.

## Form Audit

Required forms:

```text
Puppy Application
Contact Form
Training Inquiry or Contact inquiry type
```

If using Netlify Forms, confirm each form has:

```html
data-netlify="true"
name="..."
method="POST"
```

For Netlify, rendered HTML may need:

```html
<input type="hidden" name="form-name" value="puppy-application" />
```

Recommended form names:

```text
puppy-application
contact-inquiry
training-inquiry
```

Test each form after deployment and confirm submissions appear in Netlify.

Success messages:

Puppy Application:

```text
Thank you for taking the time to apply. We review each application with the goal of matching the right puppy to the right home. Alliance K9 will follow up soon to discuss availability, fit, and next steps.
```

Contact:

```text
Thank you for reaching out. Your message has been received. Alliance K9 will review your inquiry and follow up with the next best step based on your goals, questions, and current availability.
```

Training Inquiry:

```text
Thank you for your training inquiry. Alliance K9 will review your message and follow up to discuss your dog, your goals, and possible next steps.
```

## Mobile QA

Test at minimum:

```text
iPhone SE / narrow mobile
iPhone standard
large mobile
tablet
desktop
wide desktop
```

Check:

```text
navigation menu works
hero text is readable
buttons are tappable
puppy cards stack cleanly
forms are easy to complete
galleries do not overflow
images are not awkwardly cropped
footer links are readable
no horizontal scrolling
```

## Accessibility QA

Check:

```text
All images have alt text.
Buttons have clear labels.
Form fields have labels.
Color contrast is readable.
Keyboard navigation works for forms and menus.
Focus states are visible.
Links are distinguishable.
Headings are hierarchical.
```

Avoid:

```text
Icon-only buttons without labels
Placeholder-only form labels
Low-contrast gray text
Text embedded in images without HTML equivalent
```

## Performance QA

Photo-heavy site performance matters.

Check:

```text
Images are optimized.
Large images are not served unnecessarily.
Lazy loading is active where appropriate.
Hero image is prioritized.
Gallery images are lazy-loaded.
No unused massive image files are loaded on initial page.
Fonts are not excessively heavy.
Build output is clean.
```

Recommended commands:

```bash
npm run build
npm run preview
```

Optional if configured:

```bash
npm run lint
npm run check
```

## Browser QA

Test at minimum:

```text
Chrome desktop
iPhone Safari or mobile browser
```

If available:

```text
Safari
Firefox
```

## Navigation QA

Header/footer links:

```text
Home -> /
Puppies -> /puppies/
Parents -> /parents/
Training -> /training/
Gallery -> /gallery/
Apply -> /apply/
Contact -> /contact/
```

Logo should link to:

```text
/
```

## Footer QA

Footer should include:

```text
Alliance K9
Short brand statement
Navigation links
Contact link
Location/service area if desired
Copyright
```

Recommended footer line:

```text
Purpose-bred working dogs and training support based in the Birmingham, Alabama area.
```

Copyright:

```text
© 2026 Alliance K9. All rights reserved.
```

## Final Pre-Launch Checklist

```text
[ ] Production domain connected
[ ] SSL active
[ ] Canonical URLs use alliancek9dogs.com
[ ] OG URLs use alliancek9dogs.com
[ ] Sitemap uses alliancek9dogs.com
[ ] Robots allows indexing
[ ] Homepage copy finalized
[ ] Puppies page copy finalized
[ ] Puppy profiles finalized enough for launch
[ ] Apply page finalized
[ ] Parents page finalized
[ ] Training page finalized
[ ] Gallery page finalized
[ ] Contact page finalized
[ ] No filler copy remains
[ ] All puppy statuses verified
[ ] All forms tested
[ ] All CTA links tested
[ ] All images load
[ ] Mobile checked
[ ] Basic accessibility checked
[ ] Build succeeds
[ ] Netlify deploy succeeds
```

## Codex Final Report Requirement

After cleanup, report:

```text
Files changed
Metadata updates completed
Routes checked
Forms checked
Image issues found/fixed
Remaining manual checks
Deployment readiness status
```

