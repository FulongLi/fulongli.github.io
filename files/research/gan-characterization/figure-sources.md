# GaN characterisation figure sources

From Fulong Li's P3EP decks "Thermal resistance measurement_Fulong.pptx" and "Current capability test_Fulong.pptx" (CSA Catapult), extracted on 29 October 2026.

- `gan-package.jpg`: photograph of the packaged GaN device (thermal deck, slide 3), downscaled from 3647 × 4591 to 700 × 881 pixels with proportions kept.
- `cooling-plate.png`: CAD model of the six-seat base cooling plate (thermal deck, slide 3), downscaled from 2101 × 1364 to 1200 × 779.
- `test-bench.jpg`: photograph of the measurement bench (thermal deck, slides 4 and 6), downscaled from 3264 × 2448 to 1400 × 1050.
- `thermal-calibration.svg`: drawn for the website from the seven calibration points in the thermal deck's chart "Mapping of Temperature and Resistance" (slide 7). A least-squares fit gives T = 0.1073 R − 81.21 (R² = 0.998), matching the deck. The thermal resistance of about 0.2 K/W is the deck's stated result.
- `current-calibration.svg`: drawn from the current deck's calibration charts (slide 4): 21 gate-off points from two runs and 5 gate-on points, each with a least-squares linear fit (gate on: T = 116.3 R − 83.7, R in kΩ).
- `current-test-resistance.png`: the current deck's slide 5 trace of sensing resistance (an EMF figure), rendered with Inkscape at 300 dpi. The deck gives no axis labels; the y axis matches the calibration range of the sensing resistance in ohms. The ~25 °C and ~50 °C values on the page apply the gate-on fit to 940 Ω and 1150 Ω.
