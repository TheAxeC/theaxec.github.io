---
layout: default
title : Blog
num_selected: 10
permalink: /blog
description: "Research projects by Dr. Axel Faes - AI in healthcare, federated learning for heart disease prediction, brain-computer interfaces, and open-source contributions."
keywords: "AI research, federated learning projects, BCI research, GitHub repositories, biomedical AI applications"
---

<div class="row">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <div class="col">
                        <p class="h1 font-weight-normal">{{ site.data.website.research.title }}</p>
                        <p class="text-profile-bio">
                            {{ site.data.website.research.content | newline_to_br | markdownify }}
                        </p>
                    </div>
                </div>
                {% assign blog_len = site.blog | where_exp: "page","page.publish" | size %}
                {% if blog_len > 0 %}
                <div class="row">
                    <!-- <div class="owl-carousel owl-theme"> -->
                        {% assign sorted_blog = site.blog | sort: 'date' | reverse %}
                        {% for update in sorted_blog %}
                        {% if update.publish %}
                        <div class="col-12 col-md-6 col-lg-3 col-xl-2 col-sm-12 p-0">
                            <div class="card ml-2 mr-2 mb-3 news-card" > <a href="{{ update.url }}">
                                <img src="{{ update.picture }}" class="figure-img img-fluid img-thumbnail w-full rounded-lg">
                                <div class="news-desc">{{ update.title }}</div>
                                <div class="news-time">{{ update.category }}</div>
                            </a></div>
                        </div>
                        {% endif %}
                        {% endfor %}
                    <!-- </div> -->
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>