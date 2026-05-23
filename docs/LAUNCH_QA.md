# Alliance K9 Phase 10 Launch QA

## Verification Run

- `npm.cmd install`
- `npm.cmd audit --omit=dev`
- `npm.cmd run check`
- `npm.cmd run build`
- Generated-site route, link, image, form, lightbox, mobile-navigation, puppy-status, and puppy-hero audit.

## Passed

- Astro check passes with 0 errors, 0 warnings, and 0 hints.
- Production build completes successfully.
- 20 static pages are generated.
- No missing internal links or referenced local assets were found in the generated HTML.
- Netlify form markup is present for:
  - Puppy application
  - Contact
  - Training inquiry
- Mobile navigation markup is present on every generated page.
- Gallery lightbox triggers are present on the generated gallery page.
- Git-index asset audit confirms the deploy-ready set includes 12 puppy hero images and 9 gallery images.
- Puppy profile statuses match the current known availability:
  - Iroh: Reserved
  - Toph: Reserved
  - All other listed puppies: Available
- Every puppy profile has a detected hero image in the local processed image folders.

## Launch Setup Notes

- Netlify form notifications still need to be configured in the Netlify dashboard after deployment.
- Set `PUBLIC_SITE_URL` in the deploy environment once the final production URL is known so canonical and social URLs use the live domain.
- A curated deploy-ready image set is committed for launch. The larger local working photo library remains untracked so new and alternate photos can keep moving quickly without bloating the repo.
- `npm audit --omit=dev` reports 5 moderate advisories from the `@astrojs/check` YAML language tooling dependency chain. The suggested automated fix requires a breaking change, so it was not applied during launch QA.

## Remaining Manual QA

- Verify final image selections visually on mobile and desktop after deployment.
- Submit one test entry for each Netlify form on the deployed site and confirm the submissions appear in Netlify Forms.
- Configure Netlify email notifications for the desired recipient.
- Confirm the final domain and DNS before public launch.
