# Converter design optimisation figure sources

- `/images/research/converter-optimization/design-process.svg` was drawn for the website on 29 October 2026 in the shared site palette. It summarises the general multi-objective design process and contains no data.
- `/images/research/converter-optimization/proposed-design-framework.png` is Fulong Li's framework diagram, unchanged.
- `/images/research/converter-optimization/pareto-front.svg` and `design-tradeoff-radar.svg` were generated on 29 October 2026 from the loss and volume models in [AIPE-Converter-Optimisation-Agent](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) at commit `3b68298` (`physics.py`, `parameters.py`, default `DesignParameters`).
  - 60,000 designs were sampled uniformly (NumPy `default_rng(1)`) over die area 0.35–4.5 × the reference area, switching frequency 50–300 kHz, inductor ripple 10–50% of the output current and junction temperature rise 1–75 K. Efficiency and power density follow `efficiency_and_power_density`.
  - The Pareto front is the set of non-dominated designs in total loss and total volume (146 designs). The scatter shows a random 3,000 of the samples.
  - Design A is the front design nearest 2.2 kW/dm³, design C the one nearest 8.8 kW/dm³, and design B the knee: the front design closest to the ideal point after normalising both objectives across the front.
  - Radar axes are scaled to 0.15–1 across the front, inverted for loss and volume so that outward is better.
  - Chart colours `#2a78d6`, `#eb6834` and `#1baf7a` passed the categorical palette checks (lightness, chroma, colour-vision-deficiency separation); the third is below 3:1 contrast, so every design is labelled directly and listed in the table.
- The repository's own weighted-sum SLSQP sweep was not used for the front: in that implementation the switching frequency stays at its 175 kHz starting value, which appears to be a scaling issue between the frequency (in hertz) and the other variables.
