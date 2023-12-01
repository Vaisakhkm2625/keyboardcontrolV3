

# Import statement
import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QIcon

from yapsy.PluginManager import PluginManager
from plugin_categories.action_plugin import Action 
from plugin_categories.event_plugin import Event

from ui.main_ui import Ui_MainWindow

import logging
from item import Item



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
    item_list: list[dict]

    action_plugin_list: list[object]
    event_plugin_list: list[object]

    def __init__(self,ui):
        logger.info("Manager initiating....")

        self.ui = ui
        self.action_plugin_list =[]
        self.event_plugin_list =[]
        self.item_list=[]

        self.load_action_plugins()
        self.load_event_plugins()
        self.load_items()

    def load_action_plugins(self):

        action_plugin_manager = PluginManager(categories_filter={"Action":Action},plugin_info_ext="kb-plugin")
        action_plugin_manager.setPluginPlaces([PLUGIN_LOCATION])
        action_plugin_manager.collectPlugins()

        for action_plugin in action_plugin_manager.getAllPlugins():

            logger.info(f"Plugin {action_plugin.name} loading")
            self.action_plugin_list.append(action_plugin)

            ui_widget = action_plugin.plugin_object.get_ui_widget()
            action_plugin.ui_index = self.ui.actions_area.addWidget(ui_widget())


        #testing of loading
        print(self.action_plugin_list)
        self.action_plugin_list[0].plugin_object.set_data(data = {"hello":"hi"})
        print("from action",action_plugin_manager.getPluginByName("applications", category='Action').plugin_object.data)
        print("action plugins -> ",action_plugin_manager.getPluginsOfCategory("Action"))



    def load_event_plugins(self):

        event_plugin_manager = PluginManager(categories_filter={"Event":Event},plugin_info_ext="kb-plugin")
        event_plugin_manager.setPluginPlaces([PLUGIN_LOCATION])
        event_plugin_manager.collectPlugins()

        for event_plugin in event_plugin_manager.getAllPlugins():

            logger.info(f"Plugin {event_plugin.name} loading")
            self.event_plugin_list.append(event_plugin)

            #plugin.plugin_object.set_data(data={"item":"item1","application_name":"easyeffects"})
            #self.ui.sidebar.setLayout(a)
            #self.action_plugin_list.append(plugin.name)
            #self.ui.actions_area.setCurrentIndex(self.action_plugin_list.index(plugin.name))
            #self.action_plugin_list[1].plugin_object.run_action()

            #plugin.plugin_object.run_action()
            #QListWidgetItem(plugin.name, self.ui.sidebar)

    #def add_action_plugin(self):


    def load_items(self):
        self.item_list = []


        a = Item()
        a.action_type = "application"


    def read_data(self):
        pass

    def save_data(self):
        pass



class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        #apply_stylesheet(self, theme='dark_teal.xml')

        self.window = MainWindow()
        self.window.show()

class MainWindow(QMainWindow):

    action_plugin_list = []

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.apply.clicked.connect(self.run_some)
        self.manager = Manager(self.ui)



    def run_some(self):
            self.action_plugin_list[0].plugin_object.run_action()
            self.action_plugin_list[0].plugin_object.set_data(data={"item":"item1","application_name":"easyeffects"})



if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
