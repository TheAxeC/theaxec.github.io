---
layout: post
title:  "Making ical-kuleuven"
category: projects
tags: javascript
---

I enjoy using google calender. However, KULeuven does not support exporting your schedule to google calender. So I decided to create a small application to do that for me. 

There were several steps involved.

* Finding a schedule in html
* Parsing the schedule
* Serving the schedule

Finding the url I needed wasn't difficult. The url requires query parameters:

* SEL_JAAR => current academic year
* STUDIEJAAR => 1 for first year of masters, 2 for the second year
* OBJID_SC => ID of the masters (or bachelors) program

Now I needed to request these pages. This was quite a lot more difficult than it should have been. Before the actual page (with course information) is loaded, an empty page is loaded that executes some javascript which waits for a timeout. I didn't just need to request a page, I needed to emulate a browser. PhantomJS and node-horseman are excellent for this. Horseman allows you to easily traverse pages:

{% highlight js %}
horseman
    .open(url)
    ...
    .waitForNextPage()
    .click('a[href="javascript:semester()"]')
    ...
    .html()
    .then(function (page) {
        ...
    }).close();
{% endhighlight %}

Parsing the html is done by using jsdom. jsdom loads html and can also load JQuery. This allows you to parse the html file using JQuery which makes your life so much easier. Finding a course can be as easy as doing: 
{% highlight js %}
var courseIDList = window.$('a:containsi("' + c + '")');
{% endhighlight %}

Afterwards, I extract the necessary data from the html and pass it to an ical generator (ical-generator). 

In about 250 lines of code, I could request and traverse webpages, parse them and construct an iCalendar.


