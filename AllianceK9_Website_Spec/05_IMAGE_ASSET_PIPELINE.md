# Alliance K9 Image Asset Pipeline

## Purpose

This document defines how puppy, parent, training, and gallery images should be handled for the Alliance K9 website.

The project contains many real iPhone photos, including many portrait-oriented puppy images. The website should embrace these images rather than forcing them into rigid square layouts.

## Core Rule

**Original images are protected source assets and must never be destructively edited.**

Codex may create optimized copies, cropped copies, resized copies, or converted copies, but must never overwrite, delete, or modify the originals.

## Non-Destructive Workflow

Required workflow:

```text
Original → Archive Copy → Processed Derivative → Website Use
```

Allowed operations on derivative copies:

- Crop
- Resize
- Compress
- Convert to WebP/AVIF
- Adjust orientation
- Generate thumbnails
- Generate responsive sizes

Forbidden operations on originals:

- Delete
- Overwrite
- Destructive crop
- Destructive compression
- Replace original with processed copy

## Recommended Folder Structure

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
└── mockups/
```

Dropbox/source organization may use:

```text
AllianceK9_Litter_2026/
├── 00_INBOX_UNSORTED/
├── 01_SORTED_BY_PUPPY/
├── 02_REVIEW_NOTES/
├── 03_WEBSITE_CANDIDATES/
├── 04_PROCESSED_WEB/
└── 99_ARCHIVE_ORIGINALS/
```

## Puppy Identification Key

| Puppy | Collar |
|---|---|
| Ty Lee | Orange |
| Kyoshi | Lime Green |
| Zuko | Black |
| Iroh | Grey |
| Aang | Red |
| Azula | Purple |
| Sokka | Light Blue |
| Hakoda | Dark Blue |
| Toph | Pink |
| Katara | White |
| Bumi | Dark Green |
| Mai | Yellow |

If collar color is unclear or hidden, do not guess. Mark as `Unknown_Review`.

## Image Classification Fields

Maintain an inventory CSV where practical.

Recommended columns:

```csv
original_filename,original_path,archive_path,suggested_puppy,collar_color_seen,confidence,photo_type,quality_tier,recommended_use,suggested_new_filename,destination_folder,is_duplicate,duplicate_of,notes
```

## Photo Type Options

- BABY
- HEADSHOT
- OUTDOOR
- MOVEMENT
- HANDLER
- SLEEPING
- GROUP
- SIDE_PROFILE
- PLAY
- STRUCTURE
- UNKNOWN

## Quality Tier Options

- S_PLUS — flagship/hero quality
- S — excellent website candidate
- A — strong gallery/social candidate
- B — usable/supporting story image
- ARCHIVE — keep but not preferred for website
- REJECT — blurry, poor crop, duplicate, or unsuitable

## Recommended Use Options

- PROFILE_HERO
- PROFILE_GALLERY
- WEBSITE_GENERAL
- SOCIAL_MEDIA
- DEVELOPMENT_TIMELINE
- GROUP_LITTER
- UNKNOWN_REVIEW
- ARCHIVE_ONLY

## Naming Convention

Use uppercase puppy names and clear tags.

Format:

```text
PUPPY_STAGE_TYPE_###.jpg
```

Examples:

```text
ZUKO_8W_HEADSHOT_001.jpg
IROH_8W_SIDE_PROFILE_001.jpg
AZULA_8W_HANDLER_001.jpg
AANG_8W_MOVEMENT_001.jpg
GROUP_6W_LITTER_001.jpg
UNKNOWN_REVIEW_001.jpg
```

Stage options:

- NEWBORN
- 3W
- 6W
- 8W
- 9W
- UNKNOWN_STAGE

## Hero Image Requirements

Hero images are used for page banners and major above-the-fold sections.

Recommended desktop derivative:

- 16:9 or 21:9
- 1800–2400px wide
- dark overlay support
- room for typography

Recommended mobile derivative:

- 4:5 or 9:16 portrait-safe crop
- preserve face, eyes, ears, muzzle, and posture

Hero crop rules:

- Do not cut off ears awkwardly.
- Do not crop through eyes or muzzle.
- Do not destroy body posture if posture is part of the image value.
- Preserve distinctive markings where possible.
- Use focal-point-aware `object-position` when using CSS cropping.

## Puppy Profile Image Requirements

Puppy profile pages should use:

- One strong hero or feature photo
- A puppy-specific gallery
- Portrait-friendly layout
- Masonry or mixed-grid presentation

Most iPhone portrait images should remain portrait-oriented when used in galleries.

Suggested sizes:

- Hero desktop: 1800–2400px wide
- Card image: 600–900px wide
- Gallery large: 1200–1600px wide
- Thumbnail: 400–600px wide

## Gallery Requirements

Use masonry or masonry-style layout.

Rules:

- Do not force all images into square crops.
- Preserve original orientation where practical.
- Support portrait, landscape, and group images.
- Use lazy loading.
- Use a lightbox viewer if practical.
- Keep image spacing premium and uncluttered.

## Parent Dog Images

Parent dog photos should be grouped by purpose:

- Primary portrait
- Structure/profile
- Working/training proof
- Personality/lifestyle

Ranger and Mila images should support the brand story:

- Ranger: composed power, stable working genetics, strong sire presence
- Mila: athletic femininity, maternal warmth, engagement, stable temperament

## SOLD / Placement Images

For sold puppies, family placement photos may be used as social proof when available.

Rules:

- Only use genuine placements.
- Keep tone tasteful.
- Do not use exploitative urgency.
- Pair with subtle copy such as: “Iroh has found his home.”

## Image Optimization Requirements

Codex should generate optimized formats where practical:

- WebP preferred
- AVIF optional
- JPEG fallback acceptable

Use responsive images where practical.

Include width/height attributes to reduce layout shift.

## Alt Text Rules

Alt text should be descriptive and useful.

Examples:

```text
Azula, a purple-collar female puppy, standing in grass and looking toward the camera.
Ranger, the Dutch Shepherd sire, posing near a lake.
Mila lying in grass with one of her puppies.
```

Avoid keyword stuffing.

## Acceptance Criteria

The image pipeline is acceptable when:

- Originals are preserved.
- Processed images are derivative copies.
- Puppy images are organized by puppy where possible.
- Unknown photos remain in review instead of being guessed.
- Galleries support portrait photography.
- Hero images have desktop and mobile-safe versions.
- Site images load quickly.
- No important subject features are awkwardly cropped.
