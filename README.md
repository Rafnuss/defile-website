# defile-website

[![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen.svg)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-4.x-blueviolet.svg)](https://vitejs.dev/)
[![Plotly.js](https://img.shields.io/badge/Plotly.js-3.x-orange.svg)](https://plotly.com/javascript/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-blue.svg)](https://getbootstrap.com/)

A visualization tool for bird migration forecasts at Défilé de l'Ecluse, France. This app visualizes predictions made by the [defile-migration-forecast](https://github.com/AmedeeRoy/defile-migration-forecast) project, which models bird migration based on bird counts performed at Défilé de l'Ecluse.

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Explore methods

The illustrated technical guide lives in [defile-explore](https://raphaelnussbaumer.com/defile-explore/), alongside its QA viewer. Figure information links open the relevant chapter or section with the current species selected; there are no method modals in this app. A single illustrated-guide card replaces the old “How it’s made” flowchart and opens the guide with the selected species. Its title, description and English-language notice are translated in `src/i18n/explore.js`. The URL helper is `src/services/methods.js`. To test against a local documentation preview, set `VITE_EXPLORE_METHODS_URL=http://127.0.0.1:4174/` when starting Vite.

## Deployment

The website is published at https://raphaelnussbaumer.com/defile/. On pushes to `main`, GitHub Actions checks and builds the site, then publishes `dist/` as `site/` on the `defile-site` branch of `Rafnuss/rafnuss.github.io`. That branch calls the personal website’s deployment workflow, which includes the build under `/defile/`. Builds of the personal website also include the latest published Défilé build.

`PERSONAL_SITE_DEPLOY_KEY` is a write-enabled SSH deploy key for `Rafnuss/rafnuss.github.io`, stored as an Actions secret in this repository. It lets the build publish to that repository without a personal access token. The `defile-site` branch must exist before the first deployment.

The personal website serves redirects from `/defileViz/` and `/defileviz/`. This repository’s own Pages URL, `/defile-website/`, also redirects to `/defile/`. Redirects preserve query parameters and URL fragments, including language, species and tab selections. GitHub Pages serves these as HTML redirects, rather than HTTP 301 responses. Keep the old GitHub repository name unused so GitHub’s repository redirect continues to work.

### Publications

The `#publications` page shows two Nos Oiseaux cards (the two 1996 parts together, and the 2019–2020 syntheses together), followed by the future dataset section and all 21 available annual reports. Each article retains its full citation and link, maintained in `src/data/papers.js`. The data section distinguishes the data paper, the complete Zenodo deposit (DOI `10.5281/zenodo.23598005`) and the GBIF sampling-event representation, currently marked in preparation. A blank, unlinked card preserves the missing 2022 report in the annual sequence. Report links and first-page WebP thumbnails are generated from the sibling dataset repository's reference inventory; the 2015 report uses its recovered Migraction URL because the LPO archive links to 2016. The 1996 card links to the Nos Oiseaux archive (issues 443 and 444), since no public article PDF URL is recorded.

To regenerate covers and `src/data/reports.json`, install Poppler and WebP, restore the reference PDFs in `defile-dataset`, and run `python3 scripts/build-publication-covers.py ../defile-dataset`. Original PDFs remain with their publishers; only first-page thumbnails are stored here.
