---
layout: home.njk
title: "TurningCircle"
description: "Independent coverage of the UK car market and the switch to electric, built on registration data, policy documents and named sources."
templateEngineOverride: njk,md
eleventyExcludeFromCollections: true
pagination:
  data: collections.posts
  size: 22
  alias: posts
permalink: "{% if pagination.pageNumber > 0 %}page/{{ pagination.pageNumber | plus: 1 }}/{% else %}/{% endif %}"
---
