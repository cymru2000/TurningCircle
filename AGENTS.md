# Repository Guidelines

## Project Overview

TurningCircle (`turningcircle.co.uk`) is an independent UK automotive editorial publication covering the car market and the EV transition. Content is research-led and cites primary sources (SMMT registrations, GOV.UK policy, Zapmap).

It is a **static Eleventy v3 site**, not an application:

- Zero client-side JavaScript, no cookies, no analytics, no ads, no external CSS/JS/CDN requests.
- All CSS lives inline in a `<style>` block in `_includes/base.njk`; fonts are self-hosted variable WOFF2.
- Build output `_site/` is plain HTML/XML/text hosted on GitHub Pages. No backend, no database, no runtime env vars.

## Architecture & Data Flow

```
root *.md (articles + index/about/404)
   │  YAML frontmatter
   ▼
eleventy.config.mjs ── collections + filters ──► Nunjucks layouts (_includes/*.njk)
   ▲                                                  │
_data/*.json (site.json, topicBlurbs.json) ────────────┘
                                                       ▼
                                            _site/ (HTML, feed.xml, sitemap.xml, robots.txt, llms.txt)
```

Pipeline specifics:

1. Eleventy globs `*.md` **from the repository root** (`getFilteredByGlob("*.md")`). `README.md` and `AGENTS.md` are excluded via `eleventyConfig.ignores`.
2. The `posts` collection = all root markdown whose `url` exists and is not `/`, sorted newest-first. It drives the homepage, topic rails, archive, `feed.xml`, `sitemap.xml` and `llms.txt`. **Any new root `.md` file publishes automatically.**
3. Templates consume the collection plus JSON globals (`site.*`, `topicBlurbs.*`) and filters registered in `eleventy.config.mjs`.
4. Layout inheritance: `index.md`/`topic.njk` → `home.njk` → `base.njk`; articles → `article.njk` → `base.njk`; static pages → `page.njk`. Reusable markup comes from macros in `_includes/card.njk` (`photo`, `meta`, `leader`, `card`, `river`, `pager`).
5. `assets/` and `favicon.svg` are passthrough-copied verbatim; no asset bundling or minification step.
6. `tools/*.py` (Pillow) run **out of band before the build** to produce images in `assets/`; they are never invoked by Eleventy or CI.

Filters available in templates: `dateISO`, `dateHuman`, `dateShort`, `timeShort`, `readingTime` (220 wpm), `tagLabel`, `byTopic`, `notUrl`, `topicSlug`, `monthLabel`, `monthGroups`. Global `today` is captured at build start and used as the masthead build stamp.

## Key Directories

| Path | Purpose |
|---|---|
| `./*.md` | 56 flat articles + `index.md` (homepage/pagination), `about.md`, `404.md`. No `posts/` or `content/` folder exists. |
| `./*.njk` | Route templates: `topic.njk`, `archive.njk`, `feed.njk`, `sitemap.njk`, `robots.njk`, `llms.njk`. |
| `_includes/` | Nunjucks layouts and macros. `base.njk` (~240 lines) holds the entire design system. |
| `_data/` | Eleventy global data: `site.json` (title, url, topics list), `topicBlurbs.json` (per-topic copy). |
| `assets/` | `fonts/` (self-hosted WOFF2 + `src/` TTFs for the image tools), `img/` (icons, `stock/` photography), `og/` (1200×630 social cards). |
| `tools/` | Python image generators (see Development Commands). |
| `.github/workflows/deploy.yml` | CI: build on push to `main`, deploy `_site` to GitHub Pages. |

## Development Commands

No build, dev, lint or test npm scripts exist — invoke Eleventy directly.

```bash
npm install                      # install deps (npm only; package-lock.json v3)
npx @11ty/eleventy               # build to _site/
npx @11ty/eleventy --serve       # Eleventy's local server with rebuild-on-change
```

Image tooling (requires Python 3 + Pillow; not installed by npm):

```bash
python tools/make-photos.py <source-image> <slug|stock-name> [--credit "Credit Name"]
python tools/make-images.py      # regenerates all OG cards, favicon and apple-touch-icon
```

There is no linter, formatter, type checker, or bundler. Do not add tooling unless asked; verification is a successful `npx @11ty/eleventy` build plus inspecting `_site/`.

## Code Conventions & Common Patterns

**Content and frontmatter.** Root articles are kebab-case slugs matching their URL (`zev-mandate-review-halfway.md` → `/zev-mandate-review-halfway/`). Frontmatter contract:

```yaml
---
title: "Sentence case, no trailing period"
description: "Used for meta description, OG card and feed."
date: "2026-09-09"            # quoted ISO date; Eleventy special-cases this key
tags: ["UK-Cars", "EV", "Policy"]
author: "The TurningCircle Team"
layout: article.njk
ogType: article
topic: "Policy"               # MUST match a value in _data/site.json exactly
hero: "/assets/img/stock/westminster"   # no extension, no size suffix
heroCredit: "Unsplash"
---
```

- `topic` must be one of the exact strings in `_data/site.json` — currently `New cars`, `Policy`, `Charging`, `Used market`, `Guides`. A near-miss silently drops the article from topic hubs, rails and related-stories blocks.
- Every significant number must appear in prose with a linked primary source; unsourced claims are labelled as such (see `about.md` for the editorial standard).

**Templates.** Nunjucks, 2-space indent. Layouts set in frontmatter (`layout: article.njk`); macros imported explicitly with context:

```njk
{% from "card.njk" import photo, card with context %}
```

`index.md` sets `templateEngineOverride: njk,md`, so both Nunjucks and Markdown semantics apply there (note the Liquid-style `| plus: 1` filter usage) — mirror that pattern if editing it.

**Images.** When `hero` points at `/assets/img/stock/<name>`, the `photo` macro expects all of `<name>-400|800|1600.jpg`, the matching `.webp` set, and `<name>-og.jpg`. When `hero` is absent, `base.njk` falls back to `/assets/og/<slug>.png`. Missing assets render broken, not substituted — run the matching Python tool.

**Error handling and state.** Build-time only. There is no runtime error handling, no DI container, no logging library, and no persisted state; broken frontmatter or a missing template fails the Eleventy build. Python tools `print()` progress and `sys.exit` on missing inputs; `make-images.py` can fetch TTFs from Google Fonts but falls back to `C:/Windows/Fonts/*` paths.

**Styling.** Pure CSS inside `base.njk` using custom properties (`--paper`, `--ink`, `--amber`, `--rule`, `--display`, `--text`, `--ui`, …). Do not introduce a stylesheet file, utility framework, or a `<script>` tag.

## Important Files

- `eleventy.config.mjs` — build config: plugin registration, ignores, passthrough copies, `posts` collection, all filters, `today` global.
- `_includes/base.njk` — HTML shell, head metadata, OpenGraph/Twitter cards, inline CSS, masthead, footer.
- `_includes/card.njk` — responsive `<picture>` markup and all card/river/pager components.
- `_includes/article.njk` / `home.njk` / `page.njk` — article, front-page, static-page layouts.
- `index.md` — homepage pagination (`size: 22`) and permalink scheme.
- `topic.njk`, `archive.njk`, `feed.njk`, `sitemap.njk`, `robots.njk`, `llms.njk` — generated routes.
- `_data/site.json` — site metadata and the authoritative topic enumerations.
- `package.json` — only `@11ty/eleventy` (dev) and `@11ty/eleventy-plugin-rss`; `type: commonjs` while config is ESM `.mjs`.

## Runtime/Tooling Preferences

- **Node 20** (pinned in CI via `actions/setup-node`; no `engines` field or `.nvmrc`).
- **npm** with `package-lock.json` (lockfileVersion 3). Use `npm install`, not pnpm/yarn/bun.
- Eleventy **v3**; config must stay ESM (`eleventy.config.mjs`).
- Python 3 + Pillow, needed only for `tools/`. Pillow is not pinned anywhere — note it in PRs that touch the tools.
- No TypeScript, no transpiler, no bundler, no `.env` files, no secrets required.
- Deployment is GitHub Actions only: push to `main` builds and publishes; PRs run no checks at all.

## Testing & QA

There is **no test infrastructure** — no framework, no test files, no coverage tooling, and no CI test step. `npm test` is the unconfigured npm stub and exits 1.

Verification expectations for changes here:

1. Run `npx @11ty/eleventy` and require a clean build (warnings about missing layouts/frontmatter matter).
2. Inspect the generated page in `_site/` — e.g. `_site/index.html`, `_site/<slug>/index.html`, `_site/feed.xml` — confirming the article appears on the homepage, its topic hub, the archive, the sitemap and `llms.txt`.
3. For image work, regenerate with the relevant `tools/*.py` script and confirm the file naming contract above resolves.
4. Do not add a test runner as part of an unrelated change; if tests are genuinely required, ask first.

## Gotchas

- **Flat root content model**: articles live in `./`, not a content directory. Moving them into one breaks the `posts` collection glob.
- **Pagination coupling**: `sitemap.njk` computes page counts from the hardcoded tile size `22`. Changing `size` in `index.md` requires the matching edit in `sitemap.njk`.
- **Topic strings are load-bearing**: `topicSlug` lowercases and dashes them, so `Used market` → `/topic/used-market/`.
- **Avoid creating extra root `.md` files** (notes, drafts, plan docs) unless intended to publish; a new root markdown file goes live on the next build. Non-publishing files (like this one) must be added to `eleventyConfig.ignores` in `eleventy.config.mjs`.
- `tools/make-photos.py` writes to `assets/img/`, while shipped photography is organised under `assets/img/stock/`; place generated files deliberately.
- Articles are dated across Jul–Sep 2026 (future-dated editorial calendar) with matching `hero` assets; keep new pieces consistent with that scheme rather than "today".
