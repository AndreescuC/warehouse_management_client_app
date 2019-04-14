import json


class Storage:
    def __init__(self):
        self.current_shipment_id = None
        self.orders_info = {}

    def set_shipment_id(self, id):
        self.current_shipment_id = id

    def set_shipment_info(self, info):
        self.orders_info = json.loads(info.decode("utf-8"))['content']['orders']
        self.orders_info = {order['id']: order for order in self.orders_info}

    def remove_order_info(self, order_id):
        if order_id not in self.orders_info:
            return False
        del self.orders_info[order_id]
        return True
