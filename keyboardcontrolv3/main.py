
# Import statement
import sys,json

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
    item_list: list[Item]

    plugin_manager: PluginManager


    def __init__(self,ui):
        logger.info("Manager initiating....")

        self.ui = ui
        self.item_list=[]

        self.load_plugins()
        self.load_items()

        self.ui.item_list.currentRowChanged.connect(self.show_item_ui)


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

    #def add_action_plugin(self):


    def load_items(self):
        self.item_list = []

        with open('config/config.json', 'r') as json_file:
            items_data = json.load(json_file)
            print(items_data)

        for item_data in items_data:
            item_instance = Item(**item_data)
            self.item_list.append(item_instance)

        self.update_side_bar()


    def show_item_ui(self,itemid = 0):
        item = self.item_list[itemid]
        action_plugin = self.plugin_manager.getPluginByName(item.action_type, category='Action')

        logger.debug(f"action ui for {item.name}")

        self.ui.actions_area.widget(action_plugin.ui_index).set_ui_data(item.action_data)
        self.ui.actions_area.setCurrentIndex(action_plugin.ui_index)

        ## snippet - for running a plugin with item
        # need to handle this in try catch
        #name = self.item_list[itemid].action_type
        #action_data = self.item_list[itemid].action_data
        #self.plugin_manager.getPluginByName(name, category='Action').plugin_object.run_action(action_data)


    def update_side_bar(self):
        self.ui.item_list.clear()

        for item in self.item_list:
            self.ui.item_list.addItem(QListWidgetItem(item.name))

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

        #self.ui.apply.clicked.connect(self.run_some)
        self.manager = Manager(self.ui)



    def run_some(self):
            self.action_plugin_list[0].plugin_object.run_action()
            self.action_plugin_list[0].plugin_object.set_data(data={"item":"item1","application_name":"easyeffects"})


if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
