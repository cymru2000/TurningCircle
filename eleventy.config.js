module.exports = function (eleventyConfig) {
  // The repo README is for GitHub, not a site page
  eleventyConfig.ignores.add("README.md");

  // Every root-level article, newest first — drives the homepage
  // "Latest Articles" list. Any new .md file in the repo root is
  // picked up automatically; no per-article tags required.
  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("*.md")
      .filter((item) => item.url && item.url !== "/")
      .sort((a, b) => b.date - a.date);
  });
};
