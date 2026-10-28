// Keep the selected species and the relevant chapter when leaving a figure for its methods.
const METHODS_BASE =
  import.meta.env.VITE_EXPLORE_METHODS_URL || "https://raphaelnussbaumer.com/defile-explore/";

export function exploreMethodUrl(taxonId, topic, section) {
  const url = new URL(METHODS_BASE);
  url.searchParams.set("species", taxonId);
  url.hash = topic ? (section ? `${topic}-${section}` : topic) : "";
  return url.href;
}
