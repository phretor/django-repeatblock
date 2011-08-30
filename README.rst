==================
Django-Repeatblock
==================

This is a simple template macro tag, that adds the ability of
repeating template blocks within a template file.

Use Case
========

Before
------

::
        <title>{% block site_title %}{{ title }} of this page{% endblock %}</title>

        <h1>{% block site_title_2 %}{{ title }} of this page{% endblock %}</h1>


After
-----

::
        {% load repeatblock %}
        <title>{% block site_title %}{{ title }} of this page{% endblock %}</title>

        <h1>{% repeatblock site_title %}</h1>


Installation
============
1. ``pip install -e pip install -e 'git+https://github.com/phretor/django-repeatblock.git#egg=django-repeatblock'``
2. Add ``'repeatblock'`` to your ``INSTALLED_APPS`` setting.

Docs
====
Check out the ``testapp/templates/`` folder.