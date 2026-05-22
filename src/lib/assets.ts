import { existsSync, readdirSync, type Dirent } from "node:fs";
import { join, posix } from "node:path";

const imageExtensions = new Set([".avif", ".jpg", ".jpeg", ".png", ".webp"]);
const publicRoot = join(process.cwd(), "public");

function normalizePublicPath(path: string) {
  return path.startsWith("/") ? path : `/${path}`;
}

function publicPathToFilePath(path: string) {
  const publicPath = normalizePublicPath(path).replace(/^\/+/, "");
  return join(publicRoot, publicPath);
}

function hasImageExtension(filename: string) {
  const extension = filename.slice(filename.lastIndexOf(".")).toLowerCase();
  return imageExtensions.has(extension);
}

export function publicAsset(path?: string) {
  if (!path) {
    return undefined;
  }

  const normalizedPath = normalizePublicPath(path);
  return existsSync(publicPathToFilePath(normalizedPath)) ? normalizedPath : undefined;
}

export function listPublicImages(directory: string) {
  const normalizedDirectory = normalizePublicPath(directory);
  const filePath = publicPathToFilePath(normalizedDirectory);

  if (!existsSync(filePath)) {
    return [];
  }

  return readdirSync(filePath, { withFileTypes: true })
    .filter((entry: Dirent) => entry.isFile() && hasImageExtension(entry.name))
    .map((entry: Dirent) => posix.join(normalizedDirectory, entry.name))
    .sort((a: string, b: string) => a.localeCompare(b));
}

export function listPuppyImages(slug: string) {
  return listPublicImages(`/assets/processed/puppies/${slug}`);
}

export function firstPublicImage(directory: string) {
  return listPublicImages(directory)[0];
}

export function firstHeroImage(directory: string) {
  return listPublicImages(directory).find((image) =>
    image.toLowerCase().includes("hero"),
  );
}

export function puppyHeroImage(slug: string, preferredPath?: string) {
  return (
    publicAsset(preferredPath) ??
    firstHeroImage(`/assets/processed/puppies/${slug}`) ??
    firstPublicImage(`/assets/processed/puppies/${slug}`)
  );
}
