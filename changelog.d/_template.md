# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- towncrier release notes start -->
{% for section, _ in sections.items() %}
{% set underline = underlines[0] %}{% if section %}{{section}}{% set underline = underlines[1] %}{% endif %}
{% if underline %}{{ underline * ((section)|length)}}{% endif %}
{% if sections[section] %}
{% for category, val in definitions.items() if category in sections[section]%}

### {{ definitions[category]['name'] }}

{% if definitions[category]['showcontent'] %}
{% for text, values in sections[section][category].items() %}
- {{ text }}{% for issue in values %} ([#{{ issue }}]({{ issue_format.format(issue=issue) }})){% endfor %}
{% endfor %}
{% else %}
{% set issue_joiner = joiner(', ') %}
- {% for text, values in sections[section][category].items() %}{{ issue_joiner() }}{% for issue in values %}{{ issue_joiner() }}[#{{ issue }}]({{ issue_format.format(issue=issue) }}){% endfor %}{% endfor %}

{% endif %}
{% endfor %}
{% else %}
No significant changes.
{% endif %}
{% endfor %}