import pluginRss from "@11ty/eleventy-plugin-rss";

export default function (eleventyConfig) {
  eleventyConfig.addPlugin(pluginRss);

  // The repo README is for GitHub, not a site page
  eleventyConfig.ignores.add("README.md");

  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("favicon.svg");

  // Every root-level article, newest first - drives the homepage list,
  // the RSS feed, the sitemap and llms.txt. Any new .md file in the repo
  // root is picked up automatically.
  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("*.md")
      .filter((item) => item.url && item.url !== "/")
      .sort((a, b) => b.date - a.date);
  });

  eleventyConfig.addFilter("dateISO", (d) => new Date(d).toISOString().slice(0, 10));

  eleventyConfig.addFilter("dateHuman", (d) =>
    new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" })
  );

  eleventyConfig.addFilter("readingTime", (content) => {
    const words = String(content)
      .replace(/<[^>]*>/g, " ")
      .split(/\s+/)
      .filter(Boolean).length;
    return Math.max(1, Math.round(words / 220));
  });

  eleventyConfig.addFilter("tagLabel", (t) => String(t).replace(/-/g, " "));
};
