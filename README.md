# Fulong Li's Personal Website

Source code for [fulongli.github.io](https://fulongli.github.io) — a personal academic and professional website built with **Jekyll** and the **Minimal Mistakes** theme, hosted on **GitHub Pages**.

**Live site:** [https://fulongli.github.io](https://fulongli.github.io)

---

## Site Structure

| Section | Path | Description |
|---------|------|-------------|
| **Timeline** | `_posts/` | Chronological milestones — conferences, secondments, career events |
| **Research** | `_pages/research/` | Technical research areas: switching devices, converters, microgrids, passive components, sensing devices, etc. |
| **Publications** | `_pages/publications.md` | Journal articles, conference papers, and thesis |
| **Novels** | `_pages/Novels.md` | Redirects to the Spirit Connect Fantasy worldbuilding site |
| **Spirit Connect Group** | `_pages/spiritconnectltd.md` | Links to the Spirit Connect landing page, AIPE Labs, and related resources |
| **Notes** | `_notes/` | Essays and reflections on AI, civilisation, and life |
| **Support** | `_pages/support.md` | Ways to support the project |

## Repository Layout

```
.
├── _config.yml          # Jekyll site configuration
├── _data/               # Navigation and UI text
├── _includes/           # Reusable HTML partials
├── _layouts/            # Page layout templates
├── _pages/              # Static pages (research, CV, novels, etc.)
├── _posts/              # Blog / timeline posts
├── _notes/              # Life notes collection
├── _publications/       # Publication entries
├── _sass/               # Stylesheets
├── assets/              # CSS, JS, fonts
├── files/               # Downloadable PDFs (slides, posters, CV)
└── images/              # Site images (research, novels, timeline)
```

## Local Development

```bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.

---

Last updated: June 2026
