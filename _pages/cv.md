---
layout: cv
title : Resume
permalink: /cv
---

<div class="page">
    <header class="about-me">
    <img src="{{site.data.data.personal.portrait_url}}" alt="Avatar">
    <h1 class="about-me__name">{{site.data.data.personal.first-name}} <span class="about-me__last-name">{{site.data.data.personal.last-name}}</span></h1>
    <h6 class="about-me__position">{{site.data.data.personal.background}} - {{site.data.data.personal.expert}} - {{site.data.data.personal.ai}}</h6>
    <span class="about-me__social">
        {% for content in site.data.website.references.content %}
        <h6><a class="" target="_blank" href="{{content.url}}">
            <i class="{{content.name}}"></i> {{content.platform}}
        </a></h6>
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
    <section class="projects">
    <div class="section__heading">
        <h1>{{site.data.data.projects.title}}</h1>
        <span class="section__heading-underline"></span>
    </div>
    {% for item in site.data.data.projects.content %}
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
    <section class="skills">
        <div class="section__heading">
            <h1>{{site.data.data.awards.title}}</h1>
            <span class="section__heading-underline"></span>
        </div>
        {% for item in site.data.data.awards.content %}
            <div class="section__item">
                <div>
                    <h4 class="education__institution section__subheading">{{item.award}}</h4>
                    <h4 class="education__institution section__element">{{item.event}}</h4>
                    <h4 class="section__location">{{ item.location }}</h4>
                </div>
                <!-- <div>
                    <h5 class="section__subsubheading">{{item.event}}</h5>
                    <h5 class="section__date-range">{{ item.date }}</h5>
                </div> -->
            </div>
        {% endfor %}
    </section>
</div>

<div class="page-break"></div>

{% assign i = 1 %}

<div class="page">
    <section class="extracurricular">
    <div class="section__heading">
        <h1>{{site.data.data.extracurricular.title}}</h1>
        <span class="section__heading-underline"></span>
    </div>
    {% for item in site.data.data.extracurricular.content %}
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
    <section class="publications">
    <div class="section__heading">
        <h1>{{site.data.publications.title}}</h1>
        <span class="section__heading-underline"></span>
    </div>
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.papers-in-preparation %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.journal %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.conference %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.other-publications %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.thesis %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.posters %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.other %}
    </section>
</div>

<div class="page-break"></div>

<div class="page">
    <section class="publications">
    <div class="section__heading">
        <h1>{{site.data.publications.title}}</h1>
        <span class="section__heading-underline"></span>
    </div>
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.abstracts %}
    {% include widgets/pub_cv.html i=i
        publications=site.data.publications.students %}
    {% include widgets/pub_cv.html i=0
        publications=site.data.publications.news %}
    </section>
</div>
