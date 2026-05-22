# Alliance K9 Component Specification

## Core Components

### SiteHeader
Responsive navigation with logo/wordmark, primary links, and mobile menu.

Links:
- Home
- Puppies
- Parents
- Training
- Gallery
- Apply
- Contact

### SiteFooter
Footer with brand statement, navigation, contact details, and social links.

### HeroSection
Reusable cinematic hero with background image, dark gradient overlay, heading, subheading, and one or two CTAs.

Requirements:
- Text must remain readable over photos.
- Support focal-point positioning.
- Support mobile portrait crops.

### CTAButton
Variants:
- Primary gold
- Secondary outline
- Text link

### PuppyCard
Used on `/puppies` and homepage preview.

Fields:
- Image
- Name
- Sex
- Collar
- Status badge
- Trait chips
- Short description
- Link to profile

### StatusBadge
Statuses:
- Available
- Pending
- Reserved
- Sold
- Evaluation Hold

SOLD/Reserved badges must be tasteful and visible without looking like pressure-sales graphics.

### TraitChip
Small tag for puppy traits such as High Drive, Affectionate, Protection Prospect, Balanced, Sport Prospect.

### GalleryGrid
Masonry or masonry-like layout. Must preserve portrait photos gracefully.

### Lightbox
Image expansion viewer with next/previous controls where practical.

### ProfileStats
Compact stat panel for puppy pages.

Fields may include:
- Sex
- Collar
- Birthdate
- Current age
- Weight notes
- Drive level
- Best fit
- Status

### ProcessTimeline
Reusable vertical/horizontal timeline used for application and training process.

### FAQAccordion
Accessible accordion for repeated questions.

### ContactForm
General contact form.

### ApplicationForm
Multi-section puppy application form.

### TrainingServiceCard
Training program/service display card.

### ParentDogProfile
Ranger/Mila profile component with portrait, details, traits, and gallery links.

### ImageWithOverlay
Image component with optional dark overlay and focal-point support.

## Accessibility Requirements

- Buttons and links must be keyboard accessible.
- Accordion must be keyboard accessible.
- Form fields must use labels.
- Images must include alt text.
- Text contrast must remain readable on dark backgrounds.
