"""Generate template reference."""

import os

import jinja2

import websauna.system
import websauna.utils
import websauna.tests
import websauna.system.user
import websauna.system.crud
import websauna.system.admin

TEMPLATE="""
=========
Templates
=========

.. contents:: :local:

Introduction
============

:doc:`See templating documentation <../narrative/frontend/templates>`.

Default site
============

{% for name, intro, ref, heading in modules.core %}

{{ name }}
{{ heading }}

{{ intro }}

.. literalinclude:: {{ ref }}
    :language: html+jinja
    :linenos:
    :name: {{ name }}

{% endfor %}

Admin
=====

{% for name, intro, ref, heading in modules.admin %}

{{ name }}
{{ heading }}

{{ intro }}

.. literalinclude:: {{ ref }}
    :language: html+jinja
    :linenos:
    :name: {{ name }}

{% endfor %}


CRUD
====

{% for name, intro, ref, heading in modules.crud %}

{{ name }}
{{ heading }}

{{ intro }}

.. literalinclude:: {{ ref }}
    :language: html+jinja
    :linenos:
    :name: {{ name }}

{% endfor %}

User
====

{% for name, intro, ref, heading in modules.user %}

{{ name }}
{{ heading }}

{{ intro }}

.. literalinclude:: {{ ref }}
    :language: html+jinja
    :linenos:
    :name: {{ name }}

{% endfor %}
"""


template = jinja2.Template(TEMPLATE)
env = jinja2.Environment()

def find_package_templates(pkg):
    path = pkg.__file__
    templates = os.path.join(os.path.dirname(path), "templates")

    ref_path = os.path.abspath(os.path.join(os.getcwd(), "source", "reference"))

    for root, dirs, files in os.walk(templates, topdown=False):
        for name in files:
            full = os.path.join(root, name)
            rel_path = os.path.relpath(full, templates)
            if name.endswith(".html") or name.endswith(".txt") or name.endswith(".xml"):

                template_source = open(full, "rt").read()
                lexed = env.lex(template_source)
                lexed = list(lexed)

                if lexed[0][1] == "comment_begin":
                    description = lexed[1][2].strip()
                else:
                    description = "--- description missing ---"

                literal_include_path = os.path.relpath(full, ref_path)

                heading = "-" * len(rel_path)

                yield rel_path, description, literal_include_path, heading

modules = {}
modules["core"] = list(find_package_templates(websauna.system.core))
modules["admin"] = list(find_package_templates(websauna.system.admin))
modules["crud"] = list(find_package_templates(websauna.system.crud))
modules["user"] = list(find_package_templates(websauna.system.user))

print(template.render(dict(modules=modules)))