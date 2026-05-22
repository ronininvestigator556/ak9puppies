# Alliance K9 MVP Build Phases

## Build Strategy
This project should be built in tightly controlled phases.

Priority is launching a polished MVP quickly while preserving the approved design direction and avoiding unnecessary backend complexity.

## Phase 1 - Project Setup
### Goals
Create the technical foundation.

### Tasks
- Initialize Astro project.
- Add TypeScript.
- Add Tailwind CSS.
- Configure project structure.
- Add global styles.
- Add route structure.
- Add shared layout.
- Add SEO metadata defaults.
- Add favicon and base brand assets if available.

### Deliverables
- Working dev server.
- Base layout renders.
- Tailwind styles active.
- Navigation and footer shell present.

### Acceptance Criteria
- `npm install` succeeds.
- `npm run dev` succeeds.
- Homepage route loads.
- Tailwind classes render correctly.
- Project structure is clean and documented.

## Phase 2 - Design System Foundation
### Goals
Implement the core Heritage Luxury visual system.

### Tasks
- Add color tokens.
- Add typography setup.
- Add reusable spacing system.
- Add button variants.
- Add card styles.
- Add section container component.
- Add status badge component.
- Add image treatment classes.
- Add subtle hover/fade interactions.

### Required Style Tokens
Colors:
```text
midnight: #0D0D0D
graphite: #1B1B1B
gold: #B08D57
ivory: #F2F2F2
stone: #A3A3A3
```

Typography:
```text
heading: Cinzel
body: Inter
```

### Acceptance Criteria
- Site visually matches approved mockups.
- Buttons, cards, badges, sections, and typography are consistent.
- No page uses ad-hoc styling when a reusable component exists.

## Phase 3 - Content/Data System
### Goals
Create structured content for puppies, parents, training, and gallery.

### Tasks
- Create puppy content schema.
- Create dog/parent content schema.
- Create training service content schema.
- Create gallery content schema.
- Add initial content files.
- Add helper functions for status, related puppies, and image paths.

### Suggested Puppy Schema
```ts
type PuppyStatus = "Available" | "Reserved" | "Sold" | "Pending" | "Evaluation Hold";

type Puppy = {
  name: string;
  slug: string;
  sex: "Male" | "Female";
  collar: string;
  status: PuppyStatus;
  statusLabel?: string;
  birthDate: string;
  currentAge?: string;
  weightNotes?: string;
  traits: string[];
  bestFit: string[];
  shortDescription: string;
  fullDescription: string;
  heroImage: string;
  gallery: string[];
  developmentChecklist: string[];
  similarPuppies?: string[];
  soldMessage?: string;
};
```

### Required Puppy Records
- Aang
- Azula
- Bumi
- Hakoda
- Iroh
- Katara
- Kyoshi
- Mai
- Sokka
- Toph
- Ty Lee
- Zuko

### Acceptance Criteria
- Puppy listing page can render from content.
- Individual puppy pages can render from slug.
- Status badges render correctly.
- Sold puppies remain visible unless explicitly hidden.

## Phase 4 - Core Components
### Goals
Build reusable components required across all MVP pages.

### Components
- `SiteHeader`
- `SiteFooter`
- `HeroSection`
- `Section`
- `CTAButton`
- `PuppyCard`
- `StatusBadge`
- `TraitChip`
- `GalleryGrid`
- `Lightbox`
- `ProfileStats`
- `ProcessTimeline`
- `FAQAccordion`
- `ContactForm`
- `ApplicationForm`
- `TrainingServiceCard`
- `ParentDogProfile`
- `ImageWithOverlay`

### Acceptance Criteria
- Components are reusable.
- Components are responsive.
- Components use approved visual system.
- Components do not hardcode page-specific content unless intentional.

## Phase 5 - Priority Page Build
### Goal
Build launch-critical pages first.

### Priority Order
1. Homepage
2. Puppies listing page
3. Individual puppy profile template
4. Application page
5. Contact page

### Homepage Requirements
Route: `/`

Must include:
- Approved dark luxury hero style.
- Mila + puppy hero image if available.
- Brand statement.
- Primary CTAs: View Puppies; Apply / Inquire.
- Trust strip.
- Puppy preview.
- Parent/litter preview.
- Training preview.
- Final CTA.

### Puppies Page Requirements
Route: `/puppies`

Must include:
- Current litter overview.
- Born date.
- 12 puppies.
- 6 males / 6 females.
- Puppy grid.
- Availability labels.
- CTA to apply.
- SOLD puppies visible with tasteful badges.

### Puppy Profile Template Requirements
Route: `/puppies/[slug]`

Must include:
- Puppy hero image.
- Name.
- Status.
- Sex.
- Collar.
- Quick stats.
- Trait chips.
- Full description.
- Individual puppy gallery.
- Development checklist.
- Ranger x Mila parent link.
- Similar puppy recommendations.
- CTA to apply/contact.

### Application Page Requirements
Route: `/apply`

Must include:
- Process overview.
- Placement philosophy.
- Multi-section application form.
- Deposit explanation.
- FAQ / reassurance.
- CTA.

### Contact Page Requirements
Route: `/contact`

Must include:
- General inquiry form.
- Puppy inquiry routing.
- Training inquiry routing.
- Contact details.
- Social links if available.

### Acceptance Criteria
- Launch-critical pages are usable on mobile and desktop.
- All primary CTAs work.
- Forms submit or show appropriate success state.
- Puppy profiles render dynamically.

## Phase 6 - Secondary Page Build
### Goal
Complete remaining MVP pages.

### Pages
1. Parents page
2. Training page
3. Gallery page

### Parents Page Requirements
Route: `/parents`

Must include:
- Ranger section.
- Mila section.
- Pairing rationale.
- Working lineage / temperament notes.
- Parent gallery.
- CTA to puppies.

### Training Page Requirements
Route: `/training`

Must include:
- Training hero.
- Program/service cards.
- Training philosophy.
- Training process.
- Results / testimonials area.
- Training FAQ.
- CTA to contact.

### Gallery Page Requirements
Route: `/gallery`

Must include:
- Masonry image layout.
- Category filters if practical: Puppies, Parents, Training, Group / Litter.
- Lightbox viewer.
- Lazy-loaded images.
- Portrait-friendly handling.

### Acceptance Criteria
- Pages match approved mockups.
- Gallery does not force images into square crops.
- Training page clearly supports service inquiries.
- Parent page supports litter credibility.

## Phase 7 - Forms
### Goal
Enable lead capture.

### Preferred MVP Method
Netlify Forms.

### Required Forms
1. Puppy Application
2. Contact Form
3. Training Inquiry

### Application Form Fields
Suggested fields:
- Name
- Email
- Phone
- Location
- Preferred puppy
- Preferred sex
- Intended role
- Working breed experience
- Home environment
- Children/other pets
- Training goals
- Timeline
- Additional notes

### Training Inquiry Fields
Suggested fields:
- Name
- Email
- Phone
- Dog name
- Dog age
- Breed
- Training goals
- Behavior concerns
- Preferred service
- Additional notes

### Acceptance Criteria
- Forms submit successfully.
- Required fields validate.
- Confirmation state displays.
- Submissions are recoverable through Netlify or configured endpoint.

## Phase 8 - Image Asset Processing
### Goal
Prepare selected images for web use without modifying originals.

### Rules
- Never edit originals.
- Copy originals before processing.
- Create derivatives for web use.
- Use WebP or AVIF where practical.
- Preserve JPEG fallback if needed.
- Use responsive image sizes.

### Suggested Structure
```text
public/assets/
├── originals/
├── processed/
│   ├── homepage/
│   ├── parents/
│   ├── puppies/
│   │   ├── aang/
│   │   ├── azula/
│   │   ├── bumi/
│   │   ├── hakoda/
│   │   ├── iroh/
│   │   ├── katara/
│   │   ├── kyoshi/
│   │   ├── mai/
│   │   ├── sokka/
│   │   ├── toph/
│   │   ├── ty-lee/
│   │   └── zuko/
│   ├── training/
│   └── gallery/
```

### Hero Image Requirements
- Desktop derivative: 1800-2400px wide.
- Mobile derivative: portrait-safe crop.
- Preserve subject face, ears, eyes, and posture.
- Use dark overlay for text legibility.

### Gallery Requirements
- Preserve original orientation where practical.
- Use masonry layout.
- Lazy load images.
- Do not crop everything into squares.

### Acceptance Criteria
- Images load quickly.
- No major subject crops are awkward.
- Mobile crops are acceptable.
- Original files are preserved.

## Phase 9 - SEO / Social Metadata
### Goals
Make pages discoverable and shareable.

### Tasks
- Add title tags.
- Add meta descriptions.
- Add Open Graph images.
- Add canonical URLs if needed.
- Add structured content where practical.
- Add alt text for images.

### Required Page Metadata
Each puppy profile should have:
- Unique title
- Unique description
- Puppy hero image as social share image
- Status included if useful

Example:
```text
Zuko | Male Working Prospect | Alliance K9 Puppies
```

### Acceptance Criteria
- Social previews work.
- Puppy pages have unique metadata.
- Images have meaningful alt text.
- No obvious SEO metadata omissions.

## Phase 10 - QA / Launch
### QA Checklist
- Homepage loads on mobile and desktop.
- Navigation works.
- All routes work.
- Puppy cards link to correct puppy profiles.
- SOLD / Reserved badges are accurate.
- Application form works.
- Contact form works.
- Training inquiry form works.
- Gallery lightbox works.
- Images are optimized.
- No broken image paths.
- No placeholder copy remains unless approved.
- No lorem ipsum remains.
- Mobile menu works.
- Footer links work.
- Site performance is acceptable.
- Site deploys successfully.

### Launch Criteria
The site may launch when:
- Homepage, Puppies, Puppy Profiles, Apply, and Contact are complete.
- Forms are functional.
- Current puppy statuses are accurate.
- At least one strong image is assigned per available puppy.
- Site is responsive.
- No major visual defects exist.

## Phase 11 - Post-Launch Enhancements
Do not block MVP launch for these.

Possible future work:
- Blog / education hub
- Training package pages
- Online booking
- Automated puppy matching
- Email marketing integration
- CRM integration
- Deposit payment integration
- Client testimonials database
- Upcoming litters page
- Health guarantee / policies page
- Long-term breeder archive
