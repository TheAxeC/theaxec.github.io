---
layout: default
title : Publications
navbar_name: Publications
permalink: /publications/
body_attr: >-
  data-spy="scroll" data-target="#navbar-year" data-offset="100"
---

<div class="row">
    <div class="col-12 col-lg-10">
        {% for coll in site.data.publications %}
        {% if coll[0] != "title" and coll[0] != "secondary-title" %}
        <h2 class="pt-4" id="{{ coll[0] }}">{{ coll[1].title }}</h2>
        <div class="my-0 p-0 shadow-sm rounded-sm">
            {% for item in coll[1].papers %}
                {% if item.hide %}
                {% else %}
                    {% include widgets/publication_item.html item=item %}
                {% endif %}
            {% endfor %}
        </div>
        {% endif %}
        {% endfor %}
    </div>
    <div class="col-2 d-none d-lg-block">
        <div id="navbar-year" class="nav nav-pills flex-column sticky-top" style="top: 80px">
            {% for coll in site.data.publications %}
            {% if coll[0] != "title" %}
            <a class="nav-link d-block" href="#{{ coll[0] }}">{{ coll[1].title }}</a>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</div>
