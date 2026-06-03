---
layout: default
title : Publications
navbar_name: Publications
permalink: /publications/
description: "Research publications by Dr. Axel Faes - Journal articles, conference papers, and preprints on federated learning, brain-computer interfaces, and AI in healthcare."
keywords: "Axel Faes publications, research papers, federated learning, BCI, tensor regression, biomedical AI"
body_attr: >-
  data-spy="scroll" data-target="#navbar-year" data-offset="100"
---

{% include widgets/index_metrics.html %}

{% comment %} Explicit section order: published record first, papers under review below. {% endcomment %}
{% assign section_order = "journal,conference,papers-in-preparation,other-publications,thesis,abstracts,posters" | split: "," %}

{% assign i = 0 %}
<div class="row">
    <div class="col-12 col-lg-10">
        {% for seckey in section_order %}
        {% assign coll = site.data.publications[seckey] %}
        {% if coll %}
        <h2 class="pt-4" id="{{ seckey }}">{{ coll.title }}</h2>
        <div class="my-0 p-0 shadow-sm rounded-sm">
            {% for item in coll.papers %}
                {% if item.hide %}
                {% else %}
                    {% include widgets/publications_item.html i=i item=item %}
                {% endif %}
            {% endfor %}
        </div>
        {% endif %}
        {% endfor %}
    </div>
    <div class="col-2 d-none d-lg-block">
        <div id="navbar-year" class="nav nav-pills flex-column sticky-top" style="top: 80px">
            {% for seckey in section_order %}
            {% assign coll = site.data.publications[seckey] %}
            {% if coll %}
            <a class="nav-link d-block" href="#{{ seckey }}">{{ coll.title }}</a>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</div>
