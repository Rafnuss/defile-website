import { describe, expect, it } from "vitest";
import { exploreMethodUrl } from "../src/services/methods.js";

describe("links to the Explore documentation", () => {
  it("opens the guide card at the beginning with the selected species", () => {
    const url = new URL(exploreMethodUrl("avibase-451D6FC8"));
    expect(url.searchParams.get("species")).toBe("avibase-451D6FC8");
    expect(url.hash).toBe("");
  });
  it("keeps the selected taxon when opening a chapter", () => {
    const url = new URL(exploreMethodUrl("avibase-451D6FC8", "phenology"));
    expect(url.pathname).toBe("/defile-explore/");
    expect(url.searchParams.get("species")).toBe("avibase-451D6FC8");
    expect(url.hash).toBe("#phenology");
  });
  it("namespaces section anchors that repeat between chapters", () => {
    expect(new URL(exploreMethodUrl("taxon", "coverage", "m-rate")).hash).toBe("#coverage-m-rate");
    expect(new URL(exploreMethodUrl("taxon", "shown", "m-rate")).hash).toBe("#shown-m-rate");
  });
});
