# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: PromoPlanner
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


def add_tag(tags, tag_name):
    """Добавить тег в список (возвращает новый список)."""
    tags = list(tags) if not isinstance(tags, list) else tags
    for t in tags:
        if t is not None and getattr(t, 'name', '') == tag_name:
            return tags
    tags.append(Tag(tag_name))
    return tags


def remove_tag(tags, tag_name):
    """Удалить тег из списка (возвращает новый список)."""
    tags = list(tags) if not isinstance(tags, list) else tags
    return [t for t in tags if t is None or getattr(t, 'name', '') != tag_name]


def set_tags(tags, new_tags):
    """Заменить набор тегов (возвращает новый список)."""
    result = []
    if isinstance(new_tags, list):
        for nt in new_tags:
            name = nt.name if hasattr(nt, 'name') else str(nt)
            result.extend(add_tag(result, name))
    return result
