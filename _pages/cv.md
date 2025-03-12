---
layout: cv
title : Resume
permalink: /cv
---

<div class="page">
    <header class="about-me">
        <img src="{{site.data.data.personal.portrait_url}}" alt="Avatar">
        <h1 class="about-me__name">{{site.data.data.personal.first-name}} <span class="about-me__last-name">{{site.data.data.personal.last-name}}</span></h1>
        <h6 class="about-me__position">
            {% assign title_post = 0 %}
            {{ site.data.data.personal.titles[0] }}
            {% for content in site.data.data.personal.titles %}
                {% if title_post > 0 %}
                - {{ content }}
                {% endif %}
                {% assign title_post = title_post | plus:1 %}
            {% endfor %}
        </h6>
        <span class="about-me__social">
            {% for content in site.data.website.references.content %}
            {% if content.platform != "Curriculum Vitae" %}
            <h6><a class="" target="_blank" href="{{content.url}}">
                <i class="{{content.name}}"></i> {{content.platform}}
            </a></h6>
            {% endif %}
            {% endfor %}
        </span>
    </header>
    <section class="experience">
        <div class="section__heading">
            <h1>{{site.data.data.experience.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.experience.content %}
        <div class="section__item">
            <div>
                <h4 class="education__institution section__subheading">{{item.title}}</h4>
                <h4 class="section__location">{{ item.location }}</h4>
            </div>
            <div>
                <h5 class="section__subsubheading"></h5>
                <h5 class="section__date-range">{{ item.duration }}</h5>
            </div>
            {% assign items = item.about | newline_to_br | split: '<br />'  %}
            <ul>
            {% for line in items %}
            {% assign changed = line | strip_newlines %}
            {% if line and changed != "" %}
            <li> {{line}}</li>
            {% endif %}
            {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </section>
    <section class="academic">
        <div class="section__heading">
            <h1>{{site.data.data.academic.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.academic.content %}
        <div class="section__item">
            <div>
                <h4 class="education__institution section__subheading">{{item.title}}</h4>
                <h4 class="education__institution section__subheading_second">{{item.location}}</h4>
                <h4 class="section__location">{{ item.duration }}</h4>
            </div>
        </div>
        {% endfor %}
    </section>
    <section class="education">
        <div class="section__heading">
            <h1>{{site.data.data.education.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.education.content %}
        <div class="section__item">
            <div>
                <h4 class="education__institution section__subheading">{{item.title}}</h4>
                <h4 class="section__location">{{ item.location }}</h4>
            </div>
            <div>
                <h5 class="section__subsubheading"></h5>
                <h5 class="section__date-range">{{ item.duration }}</h5>
            </div>
            {% assign items = item.about | newline_to_br | split: '<br />'  %}
            <ul>
            {% for line in items %}
            {% assign changed = line | strip_newlines %}
            {% if line and changed != "" %}
            <li> {{line}}</li>
            {% endif %}
            {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </section>
    <footer>
        <span class="footer__date">{{site.data.website.description.subtitle}}</span>
        <span class="footer__text">{{site.data.website.description.title}} · {{site.data.data.personal.footer}}</span>
        <!-- <span class="footer__pageNum">1</span> -->
    </footer>
</div>

<div class="page-break"></div>

{% assign i = 1 %}

<div class="page">
    <section class="awards">
        <div class="section__heading">
            <h1>{{site.data.data.awards.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        <table>
        {% for item in site.data.data.awards.content %}
        <tr>
            <td class="publications__date"> {{ item.date | date: "%b %Y" }} </td>
            <td class="section__award">
            <span class="section__subheading"> {{item.award}}, </span>
            <span class="section__element"> {{item.event}} </span>
            </td>
            <td class="section__location"> {{item.location}} </td>
        </tr>
        {% endfor %}
        </table>
    </section>
    <section class="extracurricular">
        <div class="section__heading">
            <h1>{{site.data.data.extracurricular.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.extracurricular.content %}
        <div class="section__item">
            <div>
                <h4 class="education__institution section__subheading">{{item.title}}</h4>
                <h4 class="education__institution section__subheading_second"> {{item.location}}</h4>
                <h4 class="section__location">{{ item.duration }}</h4>
            </div>
            <div>
                <h5 class="section__subsubheading"></h5>
                <h5 class="section__date-range"></h5>
            </div>
            {% assign items = item.about | newline_to_br | split: '<br />'  %}
            <ul>
            {% for line in items %}
            {% assign changed = line | strip_newlines %}
            {% if line and changed != "" %}
            <li> {{line}}</li>
            {% endif %}
            {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </section>
    <section class="projects">
        <div class="section__heading">
            <h1>{{site.data.data.projects.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.projects.content %}
        <div class="section__item">
            <div>
                <h4 class="education__institution section__subheading">{{item.title}}</h4>
                <h4 class="section__location">{{ item.role }}</h4>
            </div>
            <div>
                <h5 class="section__subsubheading"></h5>
                <h5 class="section__date-range">{{ item.duration }}</h5>
            </div>
            {% assign items = item.about | newline_to_br | split: '<br />'  %}
            <ul>
            {% for line in items %}
            {% assign changed = line | strip_newlines %}
            {% if line and changed != "" %}
            <li> {{line}}</li>
            {% endif %}
            {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </section>
    <footer>
        <span class="footer__date">{{site.data.website.description.subtitle}}</span>
        <span class="footer__text">{{site.data.website.description.title}} · {{site.data.data.personal.footer}}</span>
        <!-- <span class="footer__pageNum">2</span> -->
    </footer>
</div>

<div class="page-break"></div>

<div class="page">
    <section class="publications">
        <div class="section__heading">
            <h1>{{site.data.publications.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% include widgets/cv_item.html i=i
            title=site.data.publications.papers-in-preparation.title
            items=site.data.publications.papers-in-preparation.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.journal.title
            items=site.data.publications.journal.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.conference.title
            items=site.data.publications.conference.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.other-publications.title
            items=site.data.publications.other-publications.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.posters.title
            items=site.data.publications.posters.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.posters.title
            items=site.data.publications.posters.papers %}
        {% include widgets/cv_item.html i=i
            title=site.data.publications.abstracts.title
            items=site.data.publications.abstracts.papers %}
    </section>
    <footer>
        <span class="footer__date">{{site.data.website.description.subtitle}}</span>
        <span class="footer__text">{{site.data.website.description.title}} · {{site.data.data.personal.footer}}</span>
        <!-- <span class="footer__pageNum">3</span> -->
    </footer>
</div>

<div class="page-break"></div>

<div class="page">
    <section class="publications">
        <div class="section__heading">
            <h1>{{site.data.data.personal.secondary-title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% assign i = 1 %}
        {% include widgets/cv_item.html i=i
            title=site.data.data.students.title 
            items=site.data.data.students.content %}
        {% include widgets/cv_item.html i=0
            title=site.data.data.news.title 
            items=site.data.data.news.content %}
    </section>
    <footer>
        <span class="footer__date">{{site.data.website.description.subtitle}}</span>
        <span class="footer__text">{{site.data.website.description.title}} · {{site.data.data.personal.footer}}</span>
        <!-- <span class="footer__pageNum">4</span> -->
    </footer>
</div>