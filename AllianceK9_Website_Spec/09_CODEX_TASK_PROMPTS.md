# Alliance K9 Codex Task Prompts

## Prompt 1 — Project Setup

Build the Alliance K9 MVP website using Astro, TypeScript, and Tailwind CSS. Follow the project charter and MVP build phases exactly. Do not add out-of-scope features without approval. Implement the base layout, routes, header, footer, design tokens, and global styles first.

## Prompt 2 — Design System

Implement the Heritage Luxury design system using the approved color palette, typography, spacing, buttons, cards, badges, image overlays, and section containers. Use reusable components instead of ad-hoc styling.

## Prompt 3 — Puppy Content System

Create structured puppy content records for all 12 puppies using the provided schema. Build the `/puppies` listing page and `/puppies/[slug]` dynamic profile pages from content data. SOLD puppies must remain visible with tasteful badges.

## Prompt 4 — Forms

Implement Netlify-compatible forms for puppy application, contact, and training inquiry. Use accessible labels, required field validation, and a confirmation state. Do not implement payment processing.

## Prompt 5 — Image Pipeline

Implement a non-destructive image pipeline. Never edit originals. Create processed derivatives for web use in separate folders. Use responsive images, lazy loading, portrait-friendly gallery handling, and focal-point-aware object positioning.

## Prompt 6 — Gallery

Build a masonry-style gallery that preserves portrait and landscape images gracefully. Add category filters if practical. Implement lightbox behavior only if it does not delay MVP launch.

## Prompt 7 — Launch QA

Run through the QA checklist. Fix broken routes, broken forms, missing metadata, incorrect statuses, visual regressions, and image crop issues before deployment.

## Guardrails

- Do not build ecommerce.
- Do not build login/auth.
- Do not create a CMS unless explicitly asked.
- Do not overwrite original images.
- Do not use hard-sell urgency copy.
- Preserve the approved A2 Heritage Luxury visual identity.
