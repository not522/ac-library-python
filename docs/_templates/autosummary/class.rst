{{ fullname }}
{{ underline }}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

{% block methods %}
   .. rubric:: Methods
{% for item in methods %}
   .. automethod:: {{ item }}
{%- endfor %}
{% endblock %}
