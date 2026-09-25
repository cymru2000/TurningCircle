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

  // Stories in one topic, newest first - drives the topic landing pages,
  // the front page rails and the related-stories block on articles.
  eleventyConfig.addFilter("byTopic", (posts, topic) =>
    (posts || []).filter((p) => p.data.topic === topic)
  );

  // Everything except the given url - used for "related" on an article.
  eleventyConfig.addFilter("notUrl", (posts, url) =>
    (posts || []).filter((p) => p.url !== url)
  );

  // A topic's url slug, so /topic/used-market/ matches "Used market".
  eleventyConfig.addFilter("topicSlug", (t) =>
    String(t).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")
  );

  // Month label for the archive: "September 2026"
  eleventyConfig.addFilter("monthLabel", (d) =>
    new Date(d).toLocaleDateString("en-GB", { month: "long", year: "numeric" })
  );

  // Posts grouped into months for the archive page, newest month first.
  eleventyConfig.addFilter("monthGroups", (posts) => {
    const groups = new Map();
    for (const p of posts || []) {
      const key = new Date(p.date).toISOString().slice(0, 7);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(p);
    }
    return [...groups.entries()].map(([key, items]) => ({
      key,
      label: new Date(`${key}-01`).toLocaleDateString("en-GB", { month: "long", year: "numeric" }),
      items,
    }));
  });

  // Build stamp for the masthead - a static site is only as current as its last build.
  eleventyConfig.addGlobalData("today", () => new Date().toISOString());
  eleventyConfig.addFilter("timeShort", (d) =>
    new Date(d).toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" })
  );
  eleventyConfig.addFilter("dateShort", (d) =>
    new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short" })
  );
};
