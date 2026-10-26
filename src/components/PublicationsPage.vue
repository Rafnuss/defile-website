<template>
  <div class="publications-page">
    <header class="publications-intro">
      <h1>{{ $t("publications.title") }}</h1>
      <p>{{ $t("publications.intro") }}</p>
    </header>

    <section aria-labelledby="papers-title">
      <div class="publication-section-head">
        <div>
          <h2 id="papers-title">{{ $t("publications.papers") }}</h2>
          <p>{{ $t("publications.papersIntro") }}</p>
        </div>
      </div>
      <div class="paper-grid">
        <article v-for="group in paperGroups" :key="group.id" class="publication-card">
          <div class="paper-covers paired">
            <a
              v-for="article in group.articles"
              :key="article.id"
              :href="article.url"
              target="_blank"
              rel="noopener"
              class="cover-link"
              :aria-label="article.title"
            >
              <img
                :src="`${base}publications/${article.cover}.webp`"
                alt=""
                width="566"
                height="800"
              />
            </a>
          </div>
          <div class="publication-body">
            <h3 lang="fr">{{ $t(`publications.group${group.id}`) }}</h3>
            <div class="paper-references">
              <div v-for="article in group.articles" :key="article.id" class="paper-reference">
                <p lang="fr" class="publication-citation">
                  {{ article.authors }} ({{ article.year }}). {{ article.title }}.
                  <cite>Nos Oiseaux</cite> <strong>{{ article.volume }}</strong
                  ><template v-if="article.number">({{ article.number }})</template>:
                  {{ article.pages }}.
                </p>
                <a
                  :href="article.url"
                  target="_blank"
                  rel="noopener"
                  class="publication-action"
                  :aria-label="`${$t(article.archive ? 'publications.issue' : 'publications.read', { n: article.issue })} — ${article.title}`"
                >
                  {{
                    $t(article.archive ? "publications.issue" : "publications.read", {
                      n: article.issue,
                    })
                  }}
                  <i class="bi bi-box-arrow-up-right" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section class="publication-data" aria-labelledby="data-title">
      <div class="publication-section-head">
        <div>
          <h2 id="data-title">{{ $t("publications.data") }}</h2>
          <p>{{ $t("publications.dataIntro") }}</p>
        </div>
      </div>
      <div class="data-grid">
        <article v-for="item in dataItems" :key="item.key" class="data-resource">
          <i :class="`bi bi-${item.icon}`" aria-hidden="true"></i>
          <h3>{{ $t(`publications.${item.key}`) }}</h3>
          <p>{{ $t(`publications.${item.key}Detail`) }}</p>
          <p v-if="item.key === 'dataPaper'" class="data-paper-title" lang="en">
            Six decades of visible bird migration counts at Défilé de l’Écluse, France, with
            documented survey effort
          </p>
          <a v-if="item.url" :href="item.url" target="_blank" rel="noopener" class="data-doi"
            >10.5281/zenodo.23598005 <i class="bi bi-box-arrow-up-right" aria-hidden="true"></i
          ></a>
          <span class="data-status">{{ $t("publications.soon") }}</span>
        </article>
      </div>
    </section>

    <section aria-labelledby="reports-title">
      <div class="publication-section-head">
        <div>
          <h2 id="reports-title">{{ $t("publications.reports") }}</h2>
          <p>{{ $t("publications.reportsIntro") }}</p>
        </div>
        <a :href="reportArchive" target="_blank" rel="noopener"
          >{{ $t("publications.archive") }}
          <i class="bi bi-box-arrow-up-right" aria-hidden="true"></i
        ></a>
      </div>
      <div class="report-grid">
        <component
          :is="report.url ? 'a' : 'article'"
          v-for="report in reportCards"
          :key="report.year"
          :href="report.url"
          :target="report.url ? '_blank' : null"
          :rel="report.url ? 'noopener' : null"
          :aria-label="
            report.url ? `${report.year}` : `${report.year} — ${$t('publications.unavailable')}`
          "
          class="publication-card report-card"
          :class="{ 'report-missing': !report.url }"
        >
          <div class="report-cover">
            <img
              v-if="report.cover"
              :src="`${base}publications/${report.cover}`"
              alt=""
              loading="lazy"
              width="566"
              height="800"
            />
            <div v-else class="empty-report-cover" aria-hidden="true"></div>
          </div>
          <div class="publication-body">
            <h3>{{ report.year }}</h3>
          </div>
        </component>
      </div>
    </section>
  </div>
</template>

<script setup>
import reports from "../data/reports.json";
import { paperGroups } from "../data/papers.js";

const base = import.meta.env.BASE_URL;
const reportArchive =
  "https://biblio.lpo-aura.org/documents/syntheses-annuelles-du-suivi-de-la-migration-postnuptiale-au-defile-de-lecluse-haute-savoie-et-ain-france/";
const reportCards = [...reports, { year: 2022 }].sort((a, b) => b.year - a.year);
const dataItems = [
  { key: "dataPaper", icon: "journal-text" },
  { key: "zenodo", icon: "database", url: "https://doi.org/10.5281/zenodo.23598005" },
  { key: "gbif", icon: "globe2" },
];
</script>

<style scoped>
.publications-page {
  padding-top: 2.5rem;
}
.publications-intro {
  max-width: 48rem;
  margin-bottom: 3rem;
}
h1 {
  font-size: clamp(1.8rem, 4vw, 2.5rem);
}
.publications-intro p {
  font-size: 1.1rem;
  color: var(--dv-muted);
}
section + section {
  margin-top: 3.5rem;
}
.publication-section-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.25rem;
}
.publication-section-head h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}
.publication-section-head p {
  margin: 0;
  color: var(--dv-muted);
  max-width: 44rem;
}
.publication-section-head > a {
  font-size: 0.85rem;
}
.paper-grid,
.report-grid,
.data-grid {
  display: grid;
  gap: 1.5rem;
}
.paper-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.data-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.report-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}
.publication-card {
  border: 1px solid var(--dv-line);
  border-radius: var(--dv-radius);
  overflow: hidden;
  background: var(--dv-surface);
}
.cover-link {
  display: block;
  height: 100%;
  max-width: 48%;
}
.paper-covers,
.report-cover {
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--dv-surface-2);
  padding: 1.25rem;
  overflow: hidden;
}
.paper-covers {
  height: 290px;
}
.paper-covers img,
.report-cover img {
  width: auto;
  max-width: 100%;
  height: 100%;
  object-fit: contain;
  box-shadow: 0 3px 12px var(--dv-line);
  transition: transform 0.2s;
}
.paired .cover-link {
  height: 90%;
}
.paired .cover-link:first-child {
  transform: rotate(-7deg) translateX(5%);
}
.paired .cover-link:last-child {
  transform: rotate(6deg) translateX(-5%);
}
.cover-link:hover img,
.report-card:hover img {
  transform: translateY(-4px);
}
.publication-body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 1.25rem;
  flex: 1;
}
.paper-grid .publication-card {
  display: flex;
  flex-direction: column;
}
.publication-citation {
  font-size: 0.85rem;
  color: var(--dv-muted);
}
h3 {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0.5rem 0;
}
.publication-body p {
  font-size: 0.85rem;
  color: var(--dv-muted);
}
.publication-action {
  font-size: 0.85rem;
  padding-top: 0.5rem;
}
.paper-references {
  margin: 1.25rem 0;
}
.paper-reference + .paper-reference {
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--dv-line);
}
.publication-body .publication-citation {
  margin-bottom: 0.5rem;
  line-height: 1.6;
  color: var(--dv-ink);
}
.publication-action i {
  margin-left: 0.35rem;
}
.report-card {
  text-decoration: none;
  color: var(--dv-ink);
  transition: border-color 0.2s;
}
.report-card[href]:hover {
  border-color: var(--dv-accent);
}
.report-cover {
  height: 245px;
}
.report-card h3 {
  font-size: 1.4rem;
  margin: 0;
}
.publication-data {
  background: var(--dv-accent-soft);
  padding: 2rem;
  border: 1px solid var(--dv-line);
  border-radius: var(--dv-radius);
}
.data-grid {
  margin-top: 1.5rem;
}
.data-grid p {
  font-size: 0.85rem;
  color: var(--dv-muted);
  margin: 0;
}
.data-resource {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.75rem;
}
.data-resource > i {
  color: var(--dv-accent);
  font-size: 1.4rem;
}
.data-resource h3 {
  font-size: 1.1rem;
  margin: 0;
}
.data-resource .data-paper-title {
  font-style: italic;
  font-size: 0.8rem;
}
.data-doi {
  overflow-wrap: anywhere;
  font-size: 0.8rem;
}
.data-status {
  font-size: 0.75rem;
  color: var(--dv-muted);
  margin-top: auto;
}
.empty-report-cover {
  height: 100%;
  aspect-ratio: 566 / 800;
  background: var(--dv-surface);
  border: 1px dashed var(--dv-line);
}
.report-missing {
  color: var(--dv-muted);
}
a:focus-visible {
  outline: 3px solid var(--dv-accent);
  outline-offset: 3px;
}
@media (max-width: 991.98px) {
  .report-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  .paper-covers {
    height: 230px;
  }
}
@media (max-width: 767.98px) {
  .paper-grid,
  .data-grid {
    grid-template-columns: 1fr;
  }
  .report-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .paper-covers {
    height: 300px;
  }
  .publication-data {
    padding: 1.25rem;
  }
}
@media (max-width: 399.98px) {
  .report-cover {
    height: 190px;
    padding: 0.75rem;
  }
  .report-card .publication-body {
    padding: 0.85rem;
  }
}
@media (prefers-reduced-motion: reduce) {
  .paper-covers img,
  .report-cover img,
  .report-card {
    transition: none;
  }
}
</style>
