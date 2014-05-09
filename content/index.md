Title: Building Static Blog
Date: 2014-05-08 10:20
Modified: 2014-05-08 10:20
Category: Blog
Tags: Pelican, GitHub, Blog
Authors: Susheng Shi
Summary: Let's learn to how build a customized static blog:D

In this my first post, let me go through how to build a static Blog using [**Pelican**](https://github.com/getpelican/pelican) + [**Github**](https://github.com/) like this.

Why writing this?
-----------------
There are plenty of tutorials on building up static blog, but most of them contain some errors or miss some very important tips.

[Chinese](http://www.lizherui.com/pages/2013/08/17/build_blog.html)
[English](http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/)

Theme
-----------------
There are quite a lot of themes for options, however I really like this one. [**pelican-svbhack**](https://github.com/giulivo/pelican-svbhack) is a very neat theme for Pelican. However, one big annoying thing is that it opens a new tab or window for links on the left side. I don't know why the author does this, but according to this article ["New Window for a New Link?"](http://www.problogdesign.com/blog-usability/new-window-for-a-new-link/), please give the right back to the user. So simply edit two lines in **pelican-svbhack/templates/base.html**.

```html
        {% for name, link in LINKS %}
        <li><a href="{{ link }}">{{ name }}</a></li>
        {% endfor %}
        {% for name, link in SOCIAL %}
        <li><a href="{{ link }}">{{ name }}</a></li>
        {% endfor %}
```

GitHub
-----------------
```
进入output把自己刚刚建好的username.github.io版本库clone下来：
cd output
git clone git@github.com:username/username.github.io.git
```
This is not corret, which will create a new directory in your __output__ folder. And when you run **make html**, the git repository will be cleared. The correct way is:
```
git init
git remote add origin YourGitRepo
git push origin master
```
Of course, the assumption is that your SSH is set correctly.
