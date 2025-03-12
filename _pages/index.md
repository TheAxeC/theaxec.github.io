---
layout: default
title : Homepage
navbar_name: Home
num_selected: 10
permalink: /
---
{% include widgets/index_profile_card.html %}

{% include widgets/index_details.html %}

<!-- {% include widgets/index_updates.html %} -->

{% for item in site.data.publications %}
{% if item[0] != "title" and item[0] != "secondary-title" %}
{% assign pubs_all = pubs_all | concat: item[1].papers %}
{% endif %}
{% endfor %}

{% assign pubs = pubs_all
    | sort: "pub_date" | reverse | where: "selected", true %}
{% 
    include widgets/index_publication_card.html 
    publications=pubs 
    title='<i class="fas fa-star"></i> Selected Publications'
%}
