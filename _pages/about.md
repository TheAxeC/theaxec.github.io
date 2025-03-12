---
layout: default
title : About
navbar_name: About
num_selected: 10
permalink: /about
---


<div class="row">
    <div class="col-12 col-lg-10">
        {% for coll in site.data.data %}
        {% if coll[0] != "personal" %}
        <h2 class="pt-4" id="{{ coll[0] }}">{{ coll[1].title }}</h2>
        <div class="my-0 p-0 shadow-sm rounded-sm">
            {% for item in coll[1].content %}
                {% if item.hide %}
                {% else %}
                    {% include widgets/about_item.html item=item %}
                {% endif %}
            {% endfor %}
        </div>
        {% endif %}
        {% endfor %}
    </div>
    <div class="col-2 d-none d-lg-block">
        <div id="navbar-year" class="nav nav-pills flex-column sticky-top" style="top: 80px">
            {% for coll in site.data.data %}
            {% if coll[0] != "personal" %}
            <a class="nav-link d-block" href="#{{ coll[0] }}">{{ coll[1].title }}</a>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</div>



