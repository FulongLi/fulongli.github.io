# AIPE PCB Agent figure sources

The two images were supplied by Fulong Li on 28 October 2026 for the project introduction. They are KiCad 3D screenshots and are reproduced without cropping, recolouring or resizing the source files. Both are 1040 × 592 pixels.

| Published asset | Supplied file | Content |
| --- | --- | --- |
| `/images/research/aipe-pcb-agent/control-board-3d.png` | `codex-clipboard-762e5d75-5eeb-4f53-b5aa-d43b33c979e3.png` | DSP control board |
| `/images/research/aipe-pcb-agent/power-board-3d.png` | `codex-clipboard-a6fcfca1-d2c8-402f-8122-7f22aa64457b.png` | SiC buck power board |

The control-board silkscreen identifies these as V2-generation boards (two-board architecture with a 2 × 25 mezzanine), so the page describes the example with the V2 dimensions and parts from [the V2 design report](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw/review/design_report.md) and [example history](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/history.md).

## Drawn diagrams

The two diagrams were drawn for the website on 28 October 2026 in the shared site palette. They summarise repository documentation and contain no measured data.

| Published asset | Content | Sources |
| --- | --- | --- |
| `_includes/aipe-framework.html` (inline SVG) | AIPE design workflow and coordination layer, shared by agent pages | [GitHub profile README](https://github.com/FulongLi), [AIPE-Workflows README](https://github.com/FulongLi/AIPE-Workflows/blob/main/README.md) and [architecture](https://github.com/FulongLi/AIPE-Workflows/blob/main/docs/architecture.md) |
| `/images/research/aipe-pcb-agent/agent-architecture.svg` | Internal organisation of AIPE PCB Agent | [Repository README](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/README.md), [aipe.yaml](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/aipe.yaml), [automation architecture](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/architecture.md) |

The user confirmed that the example should use the repository's 5 kW rating. Electrical design values are taken from [the SiC buck requirements](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw/input/requirements.yaml). Framework descriptions are based on [the repository README](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/README.md) and [automation architecture](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/architecture.md), accessed on 28 October 2026.
