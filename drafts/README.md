# Banked evergreen drafts

Articles held ready but not published. Eleventy only globs `*.md` from the repo
root, and `eleventy.config.mjs` ignores `drafts/**`, so nothing here is built or
deployed.

## Publishing one

    git mv drafts/<slug>.md ./<slug>.md

Then, in the moved file:

1. Set `date:` to the day it actually goes live (not the planned date, if late).
2. Leave `title`, `description`, `topic`, `hero`, `heroCredit` as they are —
   the `topic` values already match `_data/site.json` and the `hero` paths point
   at existing stock images.
3. Build and check: `npx @11ty/eleventy`, then confirm the article appears in
   `_site/index.html`, `_site/<slug>/index.html`, its topic hub and
   `_site/sitemap.xml`.

Commit message convention used on this repo:

    Publish: <slug> (YYYY-MM-DD)

## Current stock

| Planned date | Slug | Topic |
|---|---|---|
| 2026-11-10 | kw-and-kwh-explained | Charging |
| 2026-11-17 | towing-with-an-electric-car | Guides |
| 2026-11-24 | end-of-ev-lease-options | Guides |
| 2026-11-30 | ev-tyres-wear-and-cost | Guides |

The dates are a suggested ladder only; they carry no scheduling mechanism. A
file moved to the root publishes on the next build regardless of its `date`.
