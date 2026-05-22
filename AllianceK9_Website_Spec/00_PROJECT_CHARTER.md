# Alliance K9 Website Project Charter

## Project Name
Alliance K9 Puppies / Working Dogs Website

## Project Owner
Alliance K9

## Primary Objective
Build and launch a lean, premium marketing website for the current Ranger x Mila litter before the puppies age out of peak placement timing.

The website must help convert interested visitors into qualified puppy inquiries while reinforcing Alliance K9 as a professional breeder/trainer brand.

## Secondary Objective
Support Alliance K9 training services as a secondary revenue stream by presenting training programs, process, credibility, and contact pathways.

## Brand Positioning
**Working-Bred. Family-Raised. Purpose-Matched.**

The site should communicate:
- Serious working genetics
- Professional training knowledge
- Intentional puppy placement
- Emotional connection
- Trustworthy breeder practices
- Premium presentation without flashy pressure tactics

## Brand Tone
The site should feel:
- Premium
- Refined
- Cinematic
- Professional
- Confident
- Warm
- Trustworthy
- Working-dog credible

The site should not feel:
- Tactical cosplay
- Military-themed
- Cheap classified ad
- Generic breeder template
- Pet-store style
- Hard-sell or pressure-based

## Visual Direction
Approved visual direction: **A2 - Heritage Luxury**

Core aesthetic:
- Dark cinematic backgrounds
- Midnight black and graphite panels
- Burnished gold accents
- Ivory text
- Editorial photography
- Premium spacing
- Subtle motion
- Elegant typography

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

The site should rely on:
- Real scarcity
- Social proof
- Honest SOLD / Reserved labels
- Premium restraint
- Clear placement process
- Strong photography
- Professional evaluation language

Avoid:
- Fake urgency
- "ACT NOW" language
- Exaggerated guarantees
- Overstated working claims
- High-pressure sales tactics

## SOLD / Reserved Strategy
Sold puppies should remain visible on the site when appropriate.

Purpose:
- Demonstrate genuine demand
- Provide social proof
- Create subtle scarcity
- Redirect attention to similar available puppies

Rules:
- Only use SOLD / Reserved labels when true.
- Use tasteful badges.
- Avoid manipulative copy.
- Include "Looking for a similar puppy?" recommendations where useful.

Example:
> Iroh has found his home. Looking for a similar prospect? View Zuko, Bumi, or Hakoda.

## MVP Scope
The MVP includes the following pages:

```text
/
Homepage

/parents
Ranger x Mila / Meet the Parents

/puppies
Available Puppies / Current Litter

/puppies/[slug]
Individual Puppy Profile Template

/training
Training Overview

/apply
Puppy Application / Reserve

/gallery
Gallery / Media

/contact
Contact / Inquiry
```

## Out of Scope for MVP
Do not build these unless explicitly approved later:
- Blog
- Client portal
- E-commerce checkout
- Online deposit payments
- Booking calendar
- Full CRM
- Login/authentication
- Training package checkout
- Complex backend dashboard
- Automated puppy matching engine
- Long-form knowledge base
- Full legal contract system

## Payment Handling
The site does not need payment processing.

Payments may be handled offline through:
- Cash
- Check
- Venmo

The website should direct users to inquire/apply rather than purchase online.

## Forms Required
MVP forms:
1. Puppy Application Form
2. Training Inquiry Form
3. General Contact Form

Preferred handling:
- Netlify Forms for MVP
- Email notification to Alliance K9
- Optional success/thank-you page or inline confirmation

## Technical Recommendation
Preferred stack:
- Astro
- TypeScript
- Tailwind CSS
- Static content files
- Netlify deployment

Reason:
- Fast MVP development
- Excellent performance
- Simple hosting
- Static marketing pages
- Easy image optimization
- Forms supported without custom backend

## Content Model
Use local structured content rather than a database for MVP.

Suggested structure:
```text
src/content/puppies/
src/content/dogs/
src/content/training/
src/content/gallery/
```

Each puppy should be represented as structured content with status, description, traits, images, and related puppy recommendations.

## Image Policy
Original images are protected source assets.

Codex may:
- Copy images
- Crop copies
- Resize copies
- Compress copies
- Convert copies to WebP/AVIF
- Create web-ready derivatives

Codex must not:
- Delete originals
- Overwrite originals
- Destructively edit originals
- Replace source photos with cropped versions

All crops and processed versions must be derivative files.

## Image Design Requirements
Because many source images are iPhone portrait photos:
- Use portrait-friendly layouts.
- Use masonry galleries.
- Avoid forcing all images into square crops.
- Use focal-point-aware object positioning.
- Avoid cropping ears, eyes, muzzle, distinctive markings, or posture.
- Preserve original composition where practical.
- Crop copies only when beneficial.

## Approved Mockup Reference Set
| Mockup ID | Page / Section |
|---|---|
| 01 | Homepage |
| 02 | Ranger x Mila / Parents |
| 03 | Puppies / Available Litters |
| 04A | Training Overview / Programs |
| 04B | Training Process / FAQ |
| 04C | Training Results / Social Proof |
| 05A | Application Intro / Process |
| 05B | Application Form UI |
| 05C | Application FAQ / CTA |
| 06 | Gallery |
| 07 | Contact |
| 08A | Puppy Profile Template |

## Success Criteria
The MVP is successful when:
- Site is live and mobile-responsive.
- Homepage clearly communicates Alliance K9 brand.
- Visitors can view current puppies.
- Each puppy has an individual profile page.
- SOLD / Reserved status is clearly displayed.
- Visitors can apply for a puppy.
- Visitors can inquire about training.
- Visitors can contact Alliance K9.
- Images load quickly and look premium.
- Forms submit successfully.
- Site reflects the approved Heritage Luxury design direction.

## Launch Priority
Speed matters.

The current litter is approaching 9 weeks old, so launch should prioritize:
1. Homepage
2. Puppies page
3. Individual puppy profiles
4. Application form
5. Contact form

Other pages may follow immediately after if time allows.
