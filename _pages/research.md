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
                    <div class="col-md-7 d-none d-md-block align-self-center">
                        <figure class="figure align-self-center">
                        <a href="{{site.data.website.description.github.url}}">
                            <img 
                                src="{{site.data.website.description.github.overview}}"
                                alt="{{site.data.website.description.github.overview-alt}}"
                                class="figure-img img-fluid img-thumbnail github_light" 
                                data-toggle="tooltip" 
                                data-placement="center" 
                                title="{{ site.data.website.description.subtitle }}"
                            >
                            <img 
                                src="{{site.data.website.description.github.overview-dark}}"
                                alt="{{site.data.website.description.github.overview-alt}}"
                                class="figure-img img-fluid img-thumbnail github_dark" 
                                data-toggle="tooltip" 
                                data-placement="center" 
                                title="{{ site.data.website.description.subtitle }}"
                            >
                            <figcaption class="figure-caption text-right"></figcaption>
                        </a>
                        </figure>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 col-md-6 col-sm-12 text-center">
                        <a href="{{site.data.website.description.github.url}}">
                            <img class="figure-img img-fluid img-thumbnail github_light" src="{{site.data.website.description.github.stats}}" alt="{{site.data.website.description.github.stats-alt}}"/>
                            <img class="figure-img img-fluid img-thumbnail github_dark" src="{{site.data.website.description.github.stats-dark}}" alt="{{site.data.website.description.github.stats-alt}}"/>
                        </a>
                    </div>
                    <div class="col-12 col-md-6 col-sm-12 text-center">
                        <a href="{{site.data.website.description.github.url}}">
                            <img class="figure-img img-fluid img-thumbnail github_light" src="{{site.data.website.description.github.languages}}" alt="{{site.data.website.description.github.languages-alt}}"/>
                            <img class="figure-img img-fluid img-thumbnail github_dark" src="{{site.data.website.description.github.languages-dark}}" alt="{{site.data.website.description.github.languages-alt}}"/>
                        </a>
                    </div>
                </div>
            </div>
        </div>        
    </div>
</div>

{% assign project_len = site.data.website.description.github.pins | size %}
{% if project_len > 0 %}
<div class="row mt-3">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <h2 class="mb-2">Pinned Github Repositories</h2>
                </div>
                <div class="row">
                    {% for item in site.data.website.description.github.pins %}
                    <div class="col-12 col-md-6 col-sm-12 text-center">
                        <a href="{{item.url}}">
                            <img class="figure-img img-fluid img-thumbnail github_light" src="{{item.img}}" alt="{{item.url}}"/>
                            <img class="figure-img img-fluid img-thumbnail github_dark" src="{{item.img-dark}}" alt="{{item.url}}"/>
                        </a>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>        
    </div>
</div>
{% endif %}

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