from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((
            customer,
            order,
            day
        ))

    def get_most_ordered_dish_per_customer(self, customer):
        pedidos = [pedido[1] for pedido in self.orders
                   if pedido[0] == customer]
        if not pedidos:
            return None
        return Counter(pedidos).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        pedidos = {pedido[1] for pedido in self.orders
                   if pedido[0] == customer}
        cardapio = {pedido[1] for pedido in self.orders}
        return cardapio.difference(pedidos)

    def get_days_never_visited_per_customer(self, customer):
        pedidos = [pedido for pedido in self.orders if pedido[0] == customer]
        dias_visitados = {pedido[2] for pedido in pedidos}
        dias = {pedido[2] for pedido in self.orders}
        return dias.difference(dias_visitados)

    def get_busiest_day(self):
        dias = [pedido[2] for pedido in self.orders]
        return Counter(dias).most_common(1)[0][0]

    def get_least_busy_day(self):
        dias = [pedido[2] for pedido in self.orders]
        # o most_common sem parâmetro, retorna todos os dias
        # ordenado por frequência. Com o -1, pegamos o último
        # item dessa lista, sendo o dia menos movimentado
        return Counter(dias).most_common()[-1][0]
