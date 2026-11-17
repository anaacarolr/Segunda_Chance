import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, Card, Row, TextOverflow, Container, \
    IconButtonTheme, IconButton, CrossAxisAlignment
from flet.controls.core.canvas import color

from api_endpoints import get_produtos
from models import db_session


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_produtos():
        list_view.controls.clear()

    def montar_lista_planetas():
        list_view.controls.clear()

    def montar_lista_personagens():
        list_view.controls.clear()

        lista_dados = get_produtos()
        result_p = db_session.execute(lista_dados).scalars().all()


        for item in lista_dados["products"]:
            list_view.controls.append(
                Card(
                    content=Container(
                        content=Row([
                            Image(src=item["thumbnail"], width=150, height=150, fit="cover"),

                            Container(
                                content=Column([
                                    Text(item["title"], weight=FontWeight.BOLD, color=Colors.TEAL_100, max_lines=3,
                                         overflow=TextOverflow.ELLIPSIS, size=20),

                                    Text(item["category"].capitalize(), weight=FontWeight.BOLD, color=Colors.BROWN_300,
                                         size=15),
                                    Container(
                                        content=Row([
                                            Text(f" $ {item['price']} ", weight=FontWeight.BOLD,
                                                 color=Colors.PINK_100, size=20, ),
                                            Text(f" / ★ {item["rating"]}", weight=FontWeight.BOLD, size=15,
                                                 color=Colors.AMBER_ACCENT_200, )]),

                                    )
                                ], spacing=3),
                                expand=True
                            )
                        ], spacing=10),
                        padding=10
                    ),
                    margin=10,
                )
            )
        page.update()

        # Gerenciar as telas(routes)
        for produto in result_p:
            list_view.controls.append(
                Card(
                    content=Row([
                        Column([
                            Image(src=produto.imagem, width=150),
                            Text(produto.categoria, weight=FontWeight.BOLD, color=Colors.BLACK),
                        ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                        Row([
                            Column([
                                Text(produto.nome, weight=FontWeight.BOLD, color=Colors.BLACK, width=130),
                                Text(f"★{produto.avaliacao}", weight=FontWeight.BOLD, color=Colors.YELLOW_500),
                                Text(f"R$ {produto.preco} - {produto.estoque}", weight=FontWeight.BOLD,
                                     color=Colors.GREEN),
                            ],
                                margin=40,
                            ),
                        ]),
                    ]),
                )
            )

    def route_change():
        # carregar a primeira lista
        montar_lista_produtos()

        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Produtos", weight=FontWeight.BOLD, color=Colors.WHITE),
                        bgcolor=Colors.TEAL_100,
                    ),
                    list_view,
                ],
                padding=0
            )
        )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar telas
    def route_change():
        # Carrega a primeira lista
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Produtinhos", weight=FontWeight.BOLD, color=Colors.BROWN_500),
                        bgcolor=Colors.TEAL_100
                    ),
                    Column([
                        pagelet,
                        IconButton(icon=Icons.SHOPPING_CART, icon_color=Colors.PINK_100) if produto[
                                                                                                "id"] in ids_produtos_salvos() else IconButton(
                            icon=Icons.SHOPPING_CART, icon_color=Colors.GREY,
                            on_click=lambda e, prod=produto: salvar(prod))

                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.AUTO_AWESOME_ROUNDED, label="Produtos"),
                NavigationBarDestination(icon=Icons.SHOPPING_CART, label="Carrinho"),
            ],
            on_change=define_lista,
        ),
        content=Column([
            list_view,
        ],
            scroll=ScrollMode.HIDDEN,
            height=500,

        ),
        height=600,

    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
