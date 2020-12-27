# from awesome_panel_extensions.frameworks.fast.site.menu import (
#     Menu,
#     MenuCategory,
#     MenuDivider,
#     MenuItem,
# )
# from awesome_panel_extensions.frameworks.fast.templates.fast_list_template import FastTemplate


# def test_menu_item():
#     # When
#     item = MenuItem(name="Awesome Panel", url="https://awesome-panel.org")
#     render = item.render()
#     # Then
#     assert item.name == "Awesome Panel"
#     assert item.url == "https://awesome-panel.org"
#     assert render == '<a href="https://awesome-panel.org">Awesome Panel</a>'


# def test_menu_divider():
#     # When
#     divider = MenuDivider()
#     render = divider.render()
#     # Then
#     assert render == "<fast-divider></fast-divider>"


# def test_menu_category_expanded():
#     # When
#     category = MenuCategory(name="Apps", expanded=False)
#     render = category.render()
#     # Then
#     assert category.name == "Apps"
#     assert (
#         render
#         == """\
# <fast-accordion-item slot="item">
#     <h3 slot="heading">Apps</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
# </fast-accordion-item>
# """
#     )


# def test_menu_category_expanded():
#     # When
#     category = MenuCategory(name="Apps", expanded=True)
#     render = category.render()
#     # Then
#     assert category.name == "Apps"
#     assert (
#         render
#         == """\
# <fast-accordion-item slot="item" expanded>
#     <h3 slot="heading">Apps</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
# </fast-accordion-item>
# """
#     )


# def test_menu_category_with_menu_item():
#     # Given
#     items = [
#         MenuItem(name="A", url="url-a"),
#         MenuItem(name="B", url="url-b"),
#     ]
#     # When
#     category = MenuCategory(name="Apps", items=items)
#     render = category.render()
#     # Then
#     assert (
#         render
#         == """\
# <fast-accordion-item slot="item">
#     <h3 slot="heading">Apps</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#     <ul>
#         <li><a href="url-a">A</a></li>
#         <li><a href="url-b">B</a></li>
#     </ul>
# </fast-accordion-item>
# """
#     )


# def test_menu_category_with_menu_divider():
#     # Given
#     items = [
#         MenuDivider(),
#     ]
#     # When
#     category = MenuCategory(name="Apps", items=items)
#     render = category.render()
#     # Then
#     assert (
#         render
#         == """\
# <fast-accordion-item slot="item">
#     <h3 slot="heading">Apps</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#     <ul>
#         <fast-divider></fast-divider>
#     </ul>
# </fast-accordion-item>
# """
#     )


# def test_menu_category_with_menu_category():
#     # Given
#     items = [
#         MenuCategory(name="Panel"),
#         MenuCategory(name="Bokeh"),
#     ]
#     # When
#     category = MenuCategory(name="Resources", items=items)
#     render = category.render()
#     # Then
#     assert (
#         render
#         == """\
# <fast-accordion-item slot="item">
#     <h3 slot="heading">Resources</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#     <fast-accordion>
#         <fast-accordion-item slot="item">
#             <h3 slot="heading">Panel</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#         </fast-accordion-item>
#         <fast-accordion-item slot="item">
#             <h3 slot="heading">Bokeh</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#         </fast-accordion-item>
#     </fast-accordion>
# </fast-accordion-item>
# """
#     )


# def test_menu():
#     # When
#     menu = Menu()
#     render = menu.render()
#     # Then
#     assert (
#         render
#         == """\
# <fast-accordion class="pn-menu">
# </fast-accordion>
# """
#     )


# def test_menu_with_menu_category():
#     items = [
#         MenuCategory(name="Panel"),
#         MenuCategory(name="Bokeh"),
#     ]
#     # When
#     menu = Menu(name="sidebar-menu", items=items)
#     render = menu.render()
#     # Then
#     assert (
#         render
#         == """\
# <fast-accordion class="pn-menu" id="sidebar-menu">
#     <fast-accordion-item slot="item">
#         <h3 slot="heading">Panel</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#     </fast-accordion-item>
#     <fast-accordion-item slot="item">
#         <h3 slot="heading">Bokeh</h3>{ COLLAPSED_ICON }{ EXPANDED_ICON }
#     </fast-accordion-item>
# </fast-accordion-item>
# """
#     )


# def test_menu_real_life_example():
#     # Given
#     items = [
#         MenuCategory(name="Home", expanded=True, items=[MenuItem(name="Home", url="/")]),
#         MenuCategory(
#             name="Apps",
#             expanded=False,
#             items=[
#                 MenuItem(name="App1", url="app1"),
#                 MenuDivider(),
#                 MenuItem(name="App2", url="app2"),
#             ],
#         ),
#         MenuCategory(
#             name="Resources",
#             items=[
#                 MenuCategory(
#                     name="Panel",
#                     items=[
#                         MenuItem(name="Panel1", url="panel1"),
#                         MenuItem(name="Panel2", url="panel2"),
#                     ],
#                 ),
#                 MenuCategory(
#                     name="Bokeh",
#                     items=[
#                         MenuItem(name="Bokeh1", url="bokeh1"),
#                         MenuItem(name="Bokeh2", url="bokeh2"),
#                     ],
#                 ),
#             ],
#         ),
#     ]

#     # When
#     menu = Menu(name="sidebar-menu", items=items)
#     render = menu.render()
#     # Then
#     assert (
#         render
#         == """\
# """
#     )

#     # Return an app for visual testing
#     template = FastTemplate(title="Test Menu")
#     menu = test_menu_real_life_example()
#     template.sidebar.append(menu)
#     return template


# if __name__.startswith("bokeh"):
#     # import webbrowser
#     # path="C:\\Program Files\\Google\\Chrome\\Application\chrome.exe".lower()
#     # webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(path))
#     test_menu_real_life_example().servable()
