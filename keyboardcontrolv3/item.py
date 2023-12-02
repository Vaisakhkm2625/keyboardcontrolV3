

class Item:

    def __init__(self,name: str,description: str = "", action_type: str = "",action_data: dict = {},trigger_list: list =[]):
        self.name= name
        self.description = description
        self.action_type = action_type
        self.action_data = action_data

        self.trigger_list = trigger_list
