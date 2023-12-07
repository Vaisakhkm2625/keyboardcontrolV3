
# Import statement
import sys,json
import logging
from time import process_time_ns, time
from PyQt6.QtCore import pyqtSignal

from PyQt6.QtWidgets import QApplication, QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QPushButton, QWidget, QMenu, QDialog
from PyQt6.QtGui import QAction, QIcon

from qt_material import QtStyleTools, apply_stylesheet,list_themes

from yapsy.PluginManager import PluginManager
from plugin_categories.action_plugin import Action 
from plugin_categories.event_plugin import Event

from ui.main_ui import Ui_MainWindow

from item import Item
from add_item_dialog import AddItemDialog
from add_event_dialog import AddEventDialog

### Global variables
PLUGIN_LOCATION = 'keyboardcontrolv3/plugins'

### Logging setup

#logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
log_format = '[%(asctime)s] %(levelname)s: %(message)s'

logging.basicConfig(format=log_format)
logger = logging.getLogger("keyboardcontrolv3_logger_inst")
#logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)




class Manager:

    item_list: list[Item]
    plugin_manager: PluginManager


    def __init__(self,ui):
        logger.info("Manager initiating....")

        self.ui = ui
        self.item_list=[]

        self.load_plugins()
        self.load_items()

        self.ui.item_list.currentRowChanged.connect(self.on_item_selected)
        self.ui.tryaction.clicked.connect(self.run_current_item_action)
        self.ui.apply.clicked.connect(self.apply_changes)
        self.ui.add_item.clicked.connect(self.on_add_item_pressed)
        self.ui.add_event.clicked.connect(self.on_add_event_pressed)

        self.run_events()

    def load_plugins(self):

        self.plugin_manager = PluginManager(categories_filter={"Action":Action,"Event":Event},plugin_info_ext="kb-plugin")
        self.plugin_manager.setPluginPlaces([PLUGIN_LOCATION])
        self.plugin_manager.collectPlugins()

        for action_plugin in self.plugin_manager.getPluginsOfCategory("Action"):
            logger.info(f"setting ui for action plugin {action_plugin.name}")

            ui_widget = action_plugin.plugin_object.get_ui_widget()
            action_plugin.ui_index = self.ui.actions_area.addWidget(ui_widget())


        #print("index me",self.plugin_manager.getPluginByName( "applications",category="Action")dd)

    #-------print("from action",action_plugin_manager.getPluginByName("applications", category='Action').plugin_object.data)
    #           plugin.plugin_object.set_data(data={"item":"item1","application_name":"easyeffects"})
    #           self.ui.sidebar.setLayout(a)
    #           self.action_plugin_list.append(plugin.name)
    #           self.ui.actions_area.setCurrentIndex(self.action_plugin_list.index(plugin.name))
    #           self.action_plugin_list[1].plugin_object.run_action()

    #           plugin.plugin_object.run_action()
    #           QListWidgetItem(plugin.name, self.ui.sidebar)

    def load_items(self):
        self.item_list = []

        items_data = self.read_config() 

        for item_data in items_data:
            item_instance = Item(**item_data)
            self.item_list.append(item_instance)

        self.update_side_bar()

        #select first item
        if self.item_list:
            self.ui.item_list.setCurrentRow(0)
            self.on_item_selected(0)

    def read_config(self):
        with open('config/config.json', 'r') as json_file:
            items_data = json.load(json_file)
            logger.info("Config file loaded")
            return items_data


    def save_config(self):
        pass
        #self.s.enter(int(seconds), 1, callback, (item))


    def on_item_selected(self,item_row):
        item = self.item_list[item_row]

        self.ui.item_name.setText(item.name)
        self.ui.description.setText(item.description)
        self.set_item_ui_action(item)
        self.set_item_ui_events(item)


    def set_item_ui_action(self,item: Item):
        action_plugin = self.plugin_manager.getPluginByName(item.action_type, category='Action')

        logger.debug(f"action {action_plugin} ui for {item.name}")

        try:
            self.ui.actions_area.widget(action_plugin.ui_index).set_ui_data(item.action_data)
        except Exception as e:
            logger.debug(f"unable to set data for action plugin data for item {item.name}")

        self.ui.actions_area.setCurrentIndex(action_plugin.ui_index)

        ## snippet - for running a plugin with item
        # need to handle this in try catch
        #name = self.item_list[item_row].action_type
        #action_data = self.item_list[item_row].action_data
        #self.plugin_manager.getPluginByName(name, category='Action').plugin_object.run_action(action_data)

    def get_current_ui_item(self):
        itemRow = self.ui.item_list.currentRow()
        item = self.item_list[itemRow]
        return item


    def set_item_ui_events(self,item: Item):

        self.ui.event_list.clear()

        for event in item.event_list:

            logger.debug(f"type -> { event['type'] }")
            ui_widget_class = self.plugin_manager.getPluginByName(event["type"], category='Event').plugin_object.get_ui_widget()
            ui_widget = ui_widget_class()
            ui_widget.set_ui_data(event["data"])
            #temp workaround - to get type when retriveing data
            ui_widget._event_type = event['type']


            event_list_item = QListWidgetItem()
            event_list_item.setSizeHint(ui_widget.sizeHint())  # Set the size hint for proper sizing
            self.ui.event_list.addItem(event_list_item)
            self.ui.event_list.setItemWidget(event_list_item,ui_widget)


    def apply_changes(self):
        logger.info("changes applying")
        item = self.get_current_ui_item()

        ## Action
        action_plugin = self.plugin_manager.getPluginByName(item.action_type, category='Action')
        item.action_data = self.ui.actions_area.widget(action_plugin.ui_index).get_ui_data()
        print(item.action_data)

        ## Event
        # i am dumb -> should have made a copy item
        event_list = []

        for i in range(self.ui.event_list.count()):
            event_list_item = self.ui.event_list.item(i)
            event_ui_widget= self.ui.event_list.itemWidget(event_list_item)
            data = event_ui_widget.get_ui_data()

            event = {"type":event_ui_widget._event_type,"data":data}
            print("event retrived data ->",event)
            event_list.append(event)

        item.event_list.clear()
        item.event_list=event_list

        #TODO: Not a good idea... atleast stop previous threads
        self.run_events()

    def on_add_item_pressed(self):

        action_list = []
        action_list = [ action_plugin.name for action_plugin in self.plugin_manager.getPluginsOfCategory("Action") ]

        add_item_dialog= AddItemDialog(action_list=action_list)
        add_item_dialog.data_passed_signal.connect(self.add_item_to_list)
        result = add_item_dialog.exec()
        self.update_side_bar()

    def add_item_to_list(self,item: Item):
        print("item: ",item.name," ",item.description)
        self.item_list.append(item)


    def on_add_event_pressed(self):
        logger.info("add_event_pressed")

        event_plugin_list = []
        event_plugin_list = [ event_plugin.name for event_plugin in self.plugin_manager.getPluginsOfCategory("Event") ]

        add_event_dialog = AddEventDialog(event_list=event_plugin_list) 
        add_event_dialog.data_passed_signal.connect(self.add_event_to_curr_item_list)
        result = add_event_dialog.exec()


    def add_event_to_curr_item_list(self,event):

        item = self.get_current_ui_item()
        logger.debug(f"event is adding to current item -> {item.name}")
        item.event_list.append(event)
        self.set_item_ui_events(item)


    def update_side_bar(self):
        self.ui.item_list.clear()

        for item in self.item_list:
            self.ui.item_list.addItem(QListWidgetItem(item.name))


    def run_action_by_item(self,item):
        action_plugin = self.plugin_manager.getPluginByName(item.action_type, category='Action')
        action_plugin.plugin_object.run_action(item.action_data)


    def run_current_item_action(self):
        self.run_action_by_item(self.get_current_ui_item())


        # TODO:[x] Now it's only for scheduler_event
        # make this loop through all event with getPluginByCatagory("Event")
    def run_events(self):

        #event_plugin = self.plugin_manager.getPluginByName("scheduler_event", category='Event')
        event_plugins = self.plugin_manager.getPluginsOfCategory('Event')


        #event_plugin.plugin_object.set_data_mappings(id_mappings = [{"item":"easyeffects","data":{"scheduled_time":"2023-12-04 07:39:15.276000"}}])

        for event_plugin in event_plugins:
            
            event_plugin.plugin_object.set_data_mappings(id_mappings = self.group_by_event(event_plugin.name) )
            event_plugin.plugin_object.start_event_listener(self.event_callback)
        #event_plugin.plugin_object.stop_event_listener()

    def event_callback(self,item_name):
        logger.info(f"running plugin action {item_name}")

        # TODO:optimize here
        for item in self.item_list:
            if item.name == item_name:
                break
        else:
            logger.warn(f"item id not found for callback -> {item_name}")
            item = None

        self.run_action_by_item(item)


    def group_by_event(self,event_name):

        return_list = []

        for item in self.item_list: 
            for event in item.event_list:
                if event["type"] == event_name:
                    #print(item.name,":",event["data"])
                    a = {}
                    a["item"]=item.name
                    a["data"] = event["data"]
                    return_list.append(a)

        return return_list



class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        #apply_stylesheet(self, theme='dark_teal.xml')
        apply_stylesheet(self, theme='light_green.xml')


        self.window = MainWindow()
        self.window.themeSignal.connect(self.apply_theme)
        self.window.show()

        self.extra = { # Font
            'font_family': 'monoespace',
            'font_size': '20px',
            'color': 'white',
        }

        apply_stylesheet(self, theme="dark_teal.xml")

    def apply_theme(self,theme):

        apply_stylesheet(self, theme=theme,invert_secondary=True,extra=self.extra)
        


class MainWindow(QMainWindow):

    themeSignal = pyqtSignal(str)




    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        #self.ui.apply.clicked.connect(self.run_some)
        self.manager = Manager(self.ui)
        self.add_style_menu()


    def add_style_menu(self):
        # Create the main menu bar
        menubar = self.menuBar()

        # Create a menu for colors
        color_menu = QMenu('Select Color', self)

        # List of colors
        #colors = ["red", "green", "blue", "black", "white", "red"]

        colors = list_themes()

        # Create actions for each color
        color_actions = [QAction(color.replace("_","-").replace(".xml",""), self) for color in colors]

        # Add color actions to the color menu
        color_menu.addActions(color_actions)

        # Connect each color action to the colorSelected method
        for action in color_actions:
            action.triggered.connect(self.colorSelected)

        # Add the color menu to the main menu bar
        menubar.addMenu(color_menu)

    def colorSelected(self):
        # Get the text of the triggered action (color)
        selected_color = self.sender().text().replace("-","_")+".xml"
        print(f'Selected color: {selected_color}')
        self.themeSignal.emit(selected_color)



if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
