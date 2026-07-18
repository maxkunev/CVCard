from django import template
import re
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()


@register.filter
def parse_stack(value):
    if not isinstance(value, str):
        return []

    if "•" in value:
        items = re.split(r"[•]", value)

    if "," in value:
        items = re.split(r"[\n,]", value)

    result = []

    for item in items:
        item = item.strip()
        if not item:
            continue

        if ":" in item:
            item = item.split(":", 1)[1].strip()
        if "•" in item:
            item = item.split("•", 1)[1].strip()

        result.append(item)

    return result

@register.filter
def split(value):
    if not value:
        return []

    items = re.split(r"•", value)

    return [item.strip() for item in items if item.strip()]

@register.filter
def before_pipe(value):
    return value.split('|')[0].strip()

@register.filter
def render_bullets(text):
    if not text:
        return ''
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    html_parts = []
    in_list = False

    for line in lines:
        is_bullet = line.startswith(('•', '-', '*'))
        content = line.lstrip('•-* ').strip()

        if is_bullet:
            if not in_list:
                html_parts.append('<ul class="mb-3">')
                in_list = True
            html_parts.append(f'<li>{escape(content)}</li>')
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(f'<p class="mb-3">{escape(content)}</p>')

    if in_list:
        html_parts.append('</ul>')

    return mark_safe(''.join(html_parts))