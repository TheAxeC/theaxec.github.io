---
layout: default
title : Research
num_selected: 10
permalink: /research
---

{% include widgets/profile_card.html %}

<div class="row mt-3">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <h2 clss="mb-5">Projects</h2>
                </div>
                <div class="row">
                    <div class="owl-carousel owl-theme">
                        {% for update in site.projects %}
                        <div class="news-card"><a href="{{ update.url }}">
                            <img src="{{ update.picture }}" class="w-full rounded-lg">
                            <div class="news-desc">{{ update.title }}</div>
                            <div class="news-time">{{ update.role }}</div>
                            <div class="news-time">{{ update.duration }}</div>
                        
                        </a></div>
                        {% endfor %}
                    </div>
                    
                </div>
            </div>
        </div>        
    </div>
</div>

<div class="row mt-3">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-5">
                <div class="row">
                    <h2 clss="mb-5">Blog</h2>
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

{% for item in site.data.publications %}
{% if item[0] != "title" %}
{% assign pubs_all = pubs_all | concat: item[1].papers %}
{% endif %}
{% endfor %}
{% assign pubs = pubs_all
    | sort: "pub_date" | reverse | where: "selected", true %}
{% 
    include widgets/publication_card.html 
    publications=pubs 
    title='<i class="fas fa-star"></i> Selected Publications'
%}
