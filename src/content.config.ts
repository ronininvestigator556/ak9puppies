import { glob } from "astro/loaders";
import { defineCollection } from "astro:content";
import { z } from "astro/zod";

const puppyStatus = z.enum([
  "Available",
  "Reserved",
  "Sold",
  "Pending Conversation",
  "Evaluation Hold",
]);

const puppySchema = z.object({
  name: z.string(),
  slug: z.string(),
  sex: z.enum(["Male", "Female"]),
  collar: z.string(),
  status: puppyStatus,
  statusLabel: z.string().optional(),
  birthDate: z.string(),
  currentAge: z.string().optional(),
  weightNotes: z.string().optional(),
  traits: z.array(z.string()),
  bestFit: z.array(z.string()),
  shortDescription: z.string(),
  fullDescription: z.string(),
  heroImage: z.string(),
  gallery: z.array(z.string()),
  developmentChecklist: z.array(z.string()),
  similarPuppies: z.array(z.string()).optional(),
  soldMessage: z.string().optional(),
});

const parentDogSchema = z.object({
  name: z.string(),
  role: z.enum(["Sire", "Dam"]),
  breed: z.string(),
  registryNotes: z.string().optional(),
  temperamentSummary: z.string(),
  workingNotes: z.string(),
  heroImage: z.string(),
  gallery: z.array(z.string()),
});

const trainingServiceSchema = z.object({
  title: z.string(),
  slug: z.string(),
  summary: z.string(),
  bullets: z.array(z.string()),
  image: z.string().optional(),
});

const galleryItemSchema = z.object({
  src: z.string(),
  alt: z.string(),
  category: z.enum(["puppies", "group-litter", "parents", "training", "outdoor", "handler-interaction", "development", "group"]),
  puppySlug: z.string().optional(),
  featured: z.boolean().optional(),
  caption: z.string().optional(),
  orientation: z.enum(["portrait", "landscape", "square"]).optional(),
});

export const collections = {
  puppies: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/puppies" }),
    schema: puppySchema,
  }),
  dogs: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/dogs" }),
    schema: parentDogSchema,
  }),
  training: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/training" }),
    schema: trainingServiceSchema,
  }),
  gallery: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/gallery" }),
    schema: galleryItemSchema,
  }),
};
