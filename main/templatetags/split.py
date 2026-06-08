from django import template
import re

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