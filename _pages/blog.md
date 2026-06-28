---
layout: page
title: Blog
navbar_name: Blog
permalink: /blog
description: "Research diary of dr. ir. Axel Faes - notes on self-explaining AI, federated learning, block-term tensor methods, and AI in healthcare."
keywords: "Axel Faes blog, research diary, federated learning, self-explaining AI, block-term tensor, AI in healthcare"
---
<h1>{{ site.data.website.research.title }}</h1>

{{ site.data.website.research.content | newline_to_br | markdownify }}

{% assign sorted_blog = site.blog | sort: 'date' | reverse %}
{% assign published = sorted_blog | where: "publish", true %}
{% if published.size > 0 %}
<p class="blog-sub"><a href="{{ '/feed.xml' | relative_url }}">{% include site/icon.html name='rss' %} Subscribe via RSS</a></p>
<div class="postlist">
{% for post in published %}<a class="postrow" href="{{ post.url | relative_url }}"><span class="pdate">{{ post.date | date: "%b %Y" }}{% if post.category %} &middot; {{ post.category }}{% endif %}</span><span class="pmain"><span class="ptitle">{{ post.title }}</span><span class="pexcerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 130 }}</span></span></a>
{% endfor %}</div>
{% endif %}
