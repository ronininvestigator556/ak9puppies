import type { CollectionEntry } from "astro:content";

export type PuppyEntry = CollectionEntry<"puppies">;

const statusRank: Record<PuppyEntry["data"]["status"], number> = {
  Available: 1,
  Pending: 2,
  "Evaluation Hold": 3,
  Reserved: 4,
  Sold: 5,
};

export function sortPuppies(puppies: PuppyEntry[]) {
  return [...puppies].sort((a, b) => {
    const statusDelta = statusRank[a.data.status] - statusRank[b.data.status];

    if (statusDelta !== 0) {
      return statusDelta;
    }

    return a.data.name.localeCompare(b.data.name);
  });
}

export function getPuppyUrl(puppy: PuppyEntry) {
  return `/puppies/${puppy.data.slug}`;
}

export function getSimilarPuppies(
  puppy: PuppyEntry,
  puppies: PuppyEntry[],
): PuppyEntry[] {
  const slugs = puppy.data.similarPuppies ?? [];
  return slugs
    .map((slug) => puppies.find((candidate) => candidate.data.slug === slug))
    .filter((candidate): candidate is PuppyEntry => Boolean(candidate));
}

export function getPuppyImagePath(puppy: PuppyEntry, filename: string) {
  return `/assets/processed/puppies/${puppy.data.slug}/${filename}`;
}
