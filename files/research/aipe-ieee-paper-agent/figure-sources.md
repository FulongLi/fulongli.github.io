# AIPE IEEE Paper Agent figure sources

## Drawn diagram

`/images/research/aipe-ieee-paper-agent/agent-architecture.svg` was drawn for the website on 29 October 2026 in the shared site palette. It summarises the [repository README](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/README.md), [aipe.yaml](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/aipe.yaml), [architecture](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/docs/architecture.md) and [core/SKILL.md](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/core/SKILL.md) at commit `5192c62`, and contains no measured data. The page also uses the shared framework diagram in `_includes/aipe-framework.html` with `agent="paper"`, which adds the IEEE Paper Agent below the review package.

## Example

The paper plan and evidence matrix (`dab-10kw-paper-plan.md`, `dab-10kw-evidence-matrix.md` in this folder) were produced on 29 October 2026 by following the repository's `core/workflows/idea-to-paper.md` and `core/policies/scientific-integrity.md` at commit `5192c62`, with Claude Code as the host agent. Every number in them is copied from the [AIPE-Workflows DAB reference run](https://github.com/FulongLi/AIPE-Workflows/blob/main/examples/dab-10kw/README.md) at commit `6284f18`.

The workspace and audit results on the page come from these commands, run with Python 3.11 on macOS:

```sh
python -m unittest discover -s tests
python scripts/create-manuscript.py dab-10kw-aipe --venue ieee-ojpel --domain power-electronics --title "Agent-Coordinated Design of a 10 kW SiC Dual-Active-Bridge Converter"
python scripts/check-latex.py manuscripts/dab-10kw-aipe
python scripts/check-citations.py manuscripts/dab-10kw-aipe --write-audit
python scripts/build-reference-index.py
```

No TeX distribution was installed, so `main.tex` was not compiled.
