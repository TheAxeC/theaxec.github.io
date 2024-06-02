---
layout: default
title : Research
num_selected: 10
permalink: /research
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
                    <div class="col-md-auto d-none d-md-block">
                        <figure class="figure">
                            <img 
                                src="{{ site.data.website.research.image }}" 
                                class="figure-img img-fluid img-thumbnail" 
                                style="height: 300px;"
                                data-toggle="tooltip" 
                                data-placement="top" 
                                title="{{ site.data.website.description.subtitle }}"
                            >
                            <figcaption class="figure-caption text-right"></figcaption>
                        </figure>
                    </div>
                </div>
            </div>
        </div>        
    </div>
</div>



{% assign project_len = site.projects | where_exp: "page","page.publish" | size %}
{% if project_len > 0 %}
<div class="row mt-3">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <h2 class="mb-2">Project Blogs</h2>
                </div>
                <div class="row">
                    <div class="owl-carousel owl-theme">
                        {% for update in site.projects %}
                        {% if update.publish %}
                        <div class="news-card"><a href="{{ update.url }}">
                            <img src="{{ update.picture }}" class="w-full rounded-lg">
                            <div class="news-desc">{{ update.title }}</div>
                            <div class="news-time">{{ update.role }}</div>
                            <div class="news-time">{{ update.duration }}</div>
                        
                        </a></div>
                        {% endif %}
                        {% endfor %}
                    </div>
                    
                </div>
            </div>
        </div>        
    </div>
</div>
{% endif %}

{% assign blog_len = site.blog | where_exp: "page","page.publish" | size %}
{% if blog_len > 0 %}
<div class="row mt-3">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <h2 class="mb-2">Blog</h2>
                </div>
                <div class="row">
                    <div class="owl-carousel owl-theme">
                        {% for update in site.blog %}
                        {% if update.publish %}
                        <div class="news-card"><a href="{{ update.url }}">
                            <img src="{{ update.picture }}" class="w-full rounded-lg">
                            <div class="news-desc">{{ update.title }}</div>
                            <div class="news-time">{{ update.category }}</div>
                        
                        </a></div>
                        {% endif %}
                        {% endfor %}
                    </div>
                    
                </div>
            </div>
        </div>        
    </div>
</div>
{% endif %}