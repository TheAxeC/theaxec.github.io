---
layout: default
title : Homepage
navbar_name: Home
num_selected: 10
permalink: /
---
{% include widgets/profile_card.html %}

{% include widgets/details.html %}

{% include widgets/updates.html %}

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