"""Provides the MENU html string appended to all templates

If you need some sort of custom MENU html string feel free to customize this code.

Please note that the default MENU only works in [Fast](https://www.fast.design/) based templates.
"""
from typing import List, Optional

from awesome_panel_extensions.site.resource import Resource

_ACCENT_COLOR = "#A01346"
_EXPAND = ["Main"]


def _get_collapsed_icon(accent_color: str = _ACCENT_COLOR):
    return f"""
    <svg style="stroke: {accent_color}" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="collapsed-icon">
                <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
                <path d="M9 5.44446V12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
                <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>
    """.replace(
        "\n", ""
    )


def _get_expanded_icon(accent_color: str = _ACCENT_COLOR):
    return f"""
<svg style="stroke: {accent_color}" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="expanded-icon">
    <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
""".replace(
        "\n", ""
    )


MENU_PRE = """
<fast-accordion id="menu">
"""

MENU_POST = """
</fast-accordion>
"""

MENU_GROUP_PRE = """
    <fast-accordion-item slot="item">
        <h3 slot="heading">Group</h3>{collapsed_icon}{expanded_icon}
        <ul>
"""

MENU_GROUP_POST = """
        </ul>
    </fast-accordion-item>
"""


def _category_sort_key(value):
    if value == "Main":
        return "."
    return value


def _name_sort_key(value):
    if value.name == "Home":
        return "."
    return value.name


def _sort_applications(applications):
    return sorted(applications, key=_name_sort_key)


def _sort_categories(categories):
    return sorted(categories, key=_category_sort_key)


def _group_and_sort(resources):
    result = {}
    for resource in resources:
        if resource.category not in result:
            result[resource.category] = [resource]
        else:
            result[resource.category].append(resource)

    sorted_result = {key: _sort_applications(result[key]) for key in _sort_categories(result)}
    return sorted_result


def to_menu_item(resource: Resource) -> str:
    """Converts a Resource to a Menuitem"""
    return f'<li><a href="{resource.url}">{resource.name}</a></li>'


def to_menu(
    resources: List[Resource], accent_color: str = _ACCENT_COLOR, expand: Optional[List[str]] = None
) -> str:
    """Converts a list of Resources to a Menu

    Args:
        resources (List[Resource]): The list of Resources
        accent_color (List[Resource]): The color of the collapsed and expanded icon
        expand (List[str]): The list of categories to expand. Defaults to ["Main"]

    Returns:
        [str]: The Menu as a HTML string
    """
    if expand is None:
        expand = _EXPAND
    groups = _group_and_sort(resources)
    menu = MENU_PRE
    collapsed_icon = _get_collapsed_icon(accent_color=accent_color)
    expanded_icon = _get_expanded_icon(accent_color=accent_color)
    menu_group_pre = MENU_GROUP_PRE.replace("{collapsed_icon}", collapsed_icon).replace(
        "{expanded_icon}", expanded_icon
    )
    for group, group_resources in groups.items():
        pre = menu_group_pre.replace("Group", group)
        if group in expand:
            pre = pre.replace('slot="item">', 'slot="item" expanded>')
        menu += pre

        menu_items = [to_menu_item(resource) for resource in group_resources]
        menu += "\n".join(menu_items)

        menu += MENU_GROUP_POST
    menu += MENU_POST
    return menu
