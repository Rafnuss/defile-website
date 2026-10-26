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

## Deployment

The website is published at https://raphaelnussbaumer.com/defile/. On pushes to `main`, GitHub Actions checks and builds the site, then publishes `dist/` as `site/` on the `defile-site` branch of `Rafnuss/rafnuss.github.io`. That branch calls the personal website’s deployment workflow, which includes the build under `/defile/`. Builds of the personal website also include the latest published Défilé build.

`PERSONAL_SITE_DEPLOY_KEY` is a write-enabled SSH deploy key for `Rafnuss/rafnuss.github.io`, stored as an Actions secret in this repository. It lets the build publish to that repository without a personal access token. The `defile-site` branch must exist before the first deployment.

The personal website serves redirects from `/defileViz/` and `/defileviz/`. This repository’s own Pages URL, `/defile-website/`, also redirects to `/defile/`. Redirects preserve query parameters and URL fragments, including language, species and tab selections. GitHub Pages serves these as HTML redirects, rather than HTTP 301 responses. Keep the old GitHub repository name unused so GitHub’s repository redirect continues to work.
