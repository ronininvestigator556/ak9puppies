# Alliance K9 Content Model and Data Schema

## Puppy Data Model

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

## Required Puppy Records

- Aang — red collar
- Azula — purple collar
- Bumi — dark green collar
- Hakoda — dark blue collar
- Iroh — grey collar
- Katara — white collar
- Kyoshi — lime green collar
- Mai — yellow collar
- Sokka — light blue collar
- Toph — pink collar
- Ty Lee — orange collar
- Zuko — black collar

## Example Puppy Record

```json
{
  "name": "Zuko",
  "slug": "zuko",
  "sex": "Male",
  "collar": "Black",
  "status": "Available",
  "birthDate": "2026-03-21",
  "weightNotes": "11.4 lbs at 6 weeks; second largest pup in the litter.",
  "traits": ["High Drive", "Protection Prospect", "Handler-Focused", "Sport Prospect"],
  "bestFit": ["Working Home", "Protection", "Sport"],
  "shortDescription": "Powerful, intense, and highly handler-focused.",
  "fullDescription": "Zuko is a powerful, high-drive male who strongly mirrors his father in both structure and temperament.",
  "heroImage": "/assets/processed/puppies/zuko/zuko_hero.webp",
  "gallery": [],
  "developmentChecklist": ["Early handling", "Socialization exposure", "Vet checked", "Dewormed"],
  "similarPuppies": ["iroh", "bumi", "hakoda"]
}
```

## Parent Dog Model

```ts
type ParentDog = {
  name: string;
  role: "Sire" | "Dam";
  breed: string;
  registryNotes?: string;
  temperamentSummary: string;
  workingNotes: string;
  heroImage: string;
  gallery: string[];
};
```

## Training Service Model

```ts
type TrainingService = {
  title: string;
  slug: string;
  summary: string;
  bullets: string[];
  image?: string;
};
```

## Gallery Item Model

```ts
type GalleryItem = {
  src: string;
  alt: string;
  category: "puppies" | "parents" | "training" | "group";
  puppySlug?: string;
  featured?: boolean;
};
```
