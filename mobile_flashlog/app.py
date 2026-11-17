import flet as ft
from flet import ThemeMode, Text, TextField, Column, Container, Colors, FontWeight, ElevatedButton, Row, View

# Correção 1: Ajustado o nome da importação para bater com a chamada da linha 27
from models import get_encomenda_por_codigo, get_movimentacoes_por_pacote


def main(page: ft.Page):
    page.title = "Primeira tela"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 800
    page.bgcolor = "#F5F5F5"  # Fundo cinza claro como na imagem

    dados_rastreio = {"pacote": None, "movimentacoes": []}

    def navegar(route):
        page.route = route
        route_change()

    def buscar_e_rastrear(e):
        codigo = input_codigo.value.strip()
        print(f"[DEBUG] Buscando o código: {codigo}")  # <-- ADICIONE
        if not codigo:
            input_codigo.error_text = "Insira um código válido"
            page.update()
            return

        pacote = get_encomenda_por_codigo(codigo)
        print(f"[DEBUG] Resposta do pacote: {pacote}")  # <-- ADICIONE

        if not pacote:
            input_codigo.error_text = "Encomenda não encontrada"
            page.update()
            return

        print("[DEBUG] Pacote encontrado! Buscando movimentações...")  # <-- ADICIONE
        movs = get_movimentacoes_por_pacote(pacote["id"])
        print(f"[DEBUG] Movimentações encontradas: {len(movs)}")  # <-- ADICIONE

        dados_rastreio["pacote"] = pacote
        dados_rastreio["movimentacoes"] = movs
        input_codigo.error_text = None

        print("[DEBUG] Chamando navegação para /rastrear_encomenda")  # <-- ADICIONE
        navegar("/rastrear_encomenda")

        # Busca os dados na API
        pacote = get_encomenda_por_codigo(codigo)
        if not pacote:
            input_codigo.error_text = "Encomenda não encontrada"
            page.update()
            return
            # Se achou o pacote, busca o histórico de movimentações dele
        movs = get_movimentacoes_por_pacote(pacote["id"])

            # Salva no estado local e muda de tela
        dados_rastreio["pacote"] = pacote
        dados_rastreio["movimentacoes"] = movs
        input_codigo.error_text = None
        navegar("/rastrear_encomenda")

    # --- COMPONENTES ---
    text = Text()

    input_codigo = TextField(
        label="Insira o Número de Rastreamento",
        border_radius=15,
        bgcolor=Colors.WHITE,
        border_color=Colors.TRANSPARENT,
        filled=True
    )

    btn_acompanhar = ElevatedButton(
        "Rastrear envio  →",
        bgcolor=Colors.PINK,
        color=Colors.BLACK,
        width=400,
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
        on_click=buscar_e_rastrear,
    )

    # --- ESTRUTURA DA TELA ---
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    # Área de Input
                    Container(
                        Column([Text("FlashLog Transportes", weight=FontWeight.BOLD, size=36,
                                     color=Colors.PINK, ),
                                Text("Orquestre sua cadeia de suprimentos",
                                     weight=FontWeight.BOLD, ), input_codigo, btn_acompanhar], spacing=15)
                        ,padding=20


                    ),

                    # Seção de Últimas Pesquisas
                    Container(
                        Column([
                            Row([
                                Text("Últimas Pesquisas", weight=FontWeight.BOLD, size=20),
                                Text("Limpar tudo", color=Colors.PINK_300, size=12, weight=FontWeight.BOLD),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                        ]),
                        padding=20
                    ),
                ],
                expand=True

            )
        )
        # TELA 2: Detalhes do Rastreamento
        if page.route == "/rastrear_encomenda" and dados_rastreio["pacote"]:
            p = dados_rastreio["pacote"]
            movs = dados_rastreio["movimentacoes"]

            # =========================================================
            # A PARTE QUE VOCÊ MOSTROU FICA EXATAMENTE AQUI:
            # =========================================================
            lista_mov_widgets = []
            if not movs:
                lista_mov_widgets.append(Text("Nenhuma movimentação registrada ainda.", color=Colors.GREY_600))
            for m in movs:
                cidade_atual = m.get('cidade', 'Não informada')
                icone_status = ft.Icons.CHECK_CIRCLE if "Entregue" in m['tipo'] else ft.Icons.LOCATION_ON

                lista_mov_widgets.append(
                    Container(
                        content=Row([
                            ft.Icon(icone_status, color=Colors.PINK_400, size=24),
                            Column([
                                Text(cidade_atual, weight=FontWeight.BOLD, size=16, color=Colors.BLACK),
                                Text(f"{m['tipo']}", size=13, color=Colors.GREY_700),
                                Text(f"Data: {m['data_movimentacao']}", size=11, color=Colors.GREY_500)
                            ], spacing=2)
                        ]),
                        padding=8,
                        border=ft.Border(left=ft.BorderSide(2, Colors.PINK_100))
                    )
                )
            # =========================================================
            page.views.append(
                View(
                    route="/rastrear_encomenda",
                    controls=[
                        # Botão voltar inserido no topo para melhorar a usabilidade
                        Row([
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=view_pop,
                                icon_color=Colors.PINK
                            ),
                            Text("Detalhes do Rastreio", size=20, weight=FontWeight.BOLD)
                        ]),

                        # Card Principal de Informações do Pacote
                        Container(
                            Column([
                                Text("Código de rastreamento", size=12, weight=FontWeight.W_100),
                                Text(p["codigo_rastreio"], size=22, color=Colors.PINK_300, weight=FontWeight.BOLD),
                                Row([
                                    Container(
                                        Column([
                                            Text("Status Atual:", size=11),
                                            Text(p["status_atual"], weight=FontWeight.BOLD, size=14),
                                        ]),
                                        bgcolor=Colors.PINK, border_radius=11, padding=8, expand=True
                                    ),
                                    Container(
                                        Column([
                                            Text("Remetente:", size=11),
                                            Text(p["remetente"] if p["remetente"] else "Não informado",
                                                 weight=FontWeight.BOLD, size=14),
                                        ]),
                                        bgcolor=Colors.PINK, border_radius=11, padding=8, expand=True
                                    )
                                ], spacing=10),
                            ], spacing=10),
                            border_radius=10, bgcolor=Colors.GREY_300, width=360, padding=15, margin=10,
                        ),

                        # Grid de Informações Secundárias Fixas/Ajustadas
                        Container(
                            Row([
                                Container(
                                    Column([
                                        ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.PINK_400, size=24),
                                        Text("Peso do Envio", size=12, weight=FontWeight.W_300),
                                        Text(f"{p['peso']} ", size=16, weight=FontWeight.BOLD),
                                    ]),
                                    bgcolor=Colors.GREY_300, width=170, height=100, padding=10, border_radius=15,
                                ),
                                Container(
                                    Column([
                                        ft.Icon(ft.Icons.SPEED, color=ft.Colors.PINK_400, size=24),
                                        Text("Dimensões", size=12, weight=FontWeight.W_300),
                                        Text(f"{p['largura']}x{p['altura']} ", size=15, weight=FontWeight.BOLD),
                                    ]),
                                    bgcolor=Colors.GREY_300, width=170, height=100, padding=10, border_radius=15,
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            width=360, margin=10
                        ),

                        # Seção de Histórico de Movimentações
                        Container(
                            Column([
                                Text("Histórico de Movimentações", weight=FontWeight.BOLD, size=18),
                                Column(lista_mov_widgets, spacing=10)
                            ]),
                            padding=15, margin=10, bgcolor=Colors.WHITE, border_radius=15, width=360
                        )
                    ]
                )
            )
        page.update()

    def view_pop(e=None):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.route = top_view.route
            page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()


ft.run(main)
