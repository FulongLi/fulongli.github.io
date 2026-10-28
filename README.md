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

## Research Content and Assets

Research pages use a concise technical narrative: the question, modelling or experimental method, representative results and implications. Keep enough detail to explain model inputs and outputs, network structure or control method, and the basis of validation. Technical articles retain their contents navigation; avoid emphasising partner names in the narrative. Keep original figure colours and proportions, and use the shared site theme. Figure-source manifests under `files/research/` record the provenance of the published figures.

Keep only assets used by the site and its public downloads. Experimental scripts, regenerated simulation bundles and intermediate exports belong in their dedicated research repositories, linked from the relevant page.

Agent project introductions follow one structure, in this order:

1. **The AIPE Framework** — `{% include aipe-framework.html agent="<stage>" %}` inserts the shared AIPE introduction and workflow diagram with the agent's stage highlighted (`spec`, `electrical`, `simulation`, `components`, `field`, `cad`, `pcb` or `review`).
2. **Role of the agent** — where it sits in that workflow, with its inputs, outputs and hand-offs.
3. **How the agent is organised** — a flow chart of the agent's internal parts, drawn in the site palette, followed by a short table of their responsibilities.
4. **Example** — one task the agent has run, from its requirements to the resulting artifacts, stating what has and has not been verified.

Section titles can vary slightly, but keep this order and connect each example to the workflow that produced it.

## Local Development

```bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.

---

Last updated: October 2026
