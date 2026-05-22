# Alliance K9 Manual Image Selection Workflow

Use this when you want to manually choose photos while keeping the site easy to update.

## Source Photos

Keep originals in `AllianceK9_Litter_2026/`.

Do not edit, crop, compress, or overwrite originals in that folder.

## Website Images

Put web-ready copies in `public/assets/processed/`.

Recommended paths:

```text
public/assets/processed/homepage/mila-puppy-hero.webp
public/assets/processed/parents/ranger_hero.webp
public/assets/processed/parents/mila_hero.webp
public/assets/processed/puppies/zuko/zuko_hero.webp
public/assets/processed/puppies/zuko/zuko_gallery_001.webp
public/assets/processed/gallery/group_litter_001.webp
```

The site checks whether a processed image exists before rendering it. If a slot is empty, it shows an intentional pending media frame instead of a broken image.

## Puppy Folders

Each puppy already has a folder:

```text
public/assets/processed/puppies/aang/
public/assets/processed/puppies/azula/
public/assets/processed/puppies/bumi/
public/assets/processed/puppies/hakoda/
public/assets/processed/puppies/iroh/
public/assets/processed/puppies/katara/
public/assets/processed/puppies/kyoshi/
public/assets/processed/puppies/mai/
public/assets/processed/puppies/sokka/
public/assets/processed/puppies/toph/
public/assets/processed/puppies/ty-lee/
public/assets/processed/puppies/zuko/
```

Use each puppy's existing `*_hero.webp` filename for the main profile image. Add gallery files alongside it.

## Formats

Preferred:

- `.webp`
- `.avif`

Accepted:

- `.jpg`
- `.jpeg`
- `.png`

## Naming

Use descriptive lowercase names for processed website files:

```text
zuko_hero.webp
zuko_gallery_001.webp
zuko_gallery_002.webp
azula_hero.webp
group_litter_001.webp
```

## Practical Loop

1. Pick a strong original from `AllianceK9_Litter_2026/`.
2. Export or copy a web-ready derivative.
3. Put it in the matching `public/assets/processed/...` folder.
4. Refresh the local site.
5. If it looks good, keep going.

Originals stay protected. The public folder only contains website-ready derivatives.
