from PyQt6.QtCore import QDateTime, QThread, pyqtSignal
from PyQt6.QtWidgets import QDateTimeEdit, QVBoxLayout, QWidget
from plugin_categories.event_plugin import Event
import sched,time
from datetime import datetime

class SchedulerWorker(QThread):

    run_function_signal = pyqtSignal()

    def __init__(self, scheduler):
        super().__init__()
        self.scheduler = scheduler

    def run(self):
        self.scheduler.run()


class SchedulerUiWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.data = {}

        self.date_time_edit = QDateTimeEdit(self)
        self.date_time_edit.setDateTime(QDateTime.currentDateTime())

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.date_time_edit)

        self.date_time_edit.dateTimeChanged.connect(self.datetime_changed)
        self.setLayout(self.vbox)

    def get_ui_data(self):
        self.data["scheduled_time"]= self.date_time_edit.dateTime().toPyDateTime().strftime("%Y-%m-%d %H:%M:%S.%f")
        return self.data

    def set_ui_data(self,data):
        self.data = data
        #self.date_time_edit.setDateTime(QDateTime.currentDateTime())
        try:
            self.date_time_edit.setDateTime(QDateTime.fromString(data["scheduled_time"],"%Y-%m-%d %H:%M:%S.%f"))
        except Exception as e:
            print("unable to get scheduled_time error:",e) 
            self.date_time_edit.setDateTime(QDateTime.currentDateTime())

    def datetime_changed(self):

        scheduled_time = self.date_time_edit.dateTime().toPyDateTime()
        current_time = QDateTime.currentDateTime().toPyDateTime()

        if scheduled_time <= current_time:
            print("Selected time should be in the future.")
            return

        self.data["scheduled_time"] = scheduled_time 



class SchedulerEventPlugin(Event):
    def __init__(self):
        super().__init__()

        self.schedule_mappings = []
        self.s = sched.scheduler(time.time, time.sleep)

        self.worker_thread = SchedulerWorker(self.s)

    def get_ui_widget(self):
        return SchedulerUiWidget

    # [
    #     {"item":"easyeffects","data":{"scheduled_time":"asfasdfasdf"}},
    #     {"item":"firefox","data":{"scheduled_time":"asfasdfasdf"}},
    # ]



    def set_data_mappings(self, id_mappings = []):
        self.schedule_mappings = id_mappings
        

    def start_event_listener(self,callback):
        # keyboard press ed > callback
        print("starting schduler event listenr")

        current_time = QDateTime.currentDateTime().toPyDateTime()

        for scheduled_map in self.schedule_mappings:
            item = scheduled_map["item"]

            try:
                scheduled_time = datetime.strptime(scheduled_map["data"]["scheduled_time"],"%Y-%m-%d %H:%M:%S.%f")
            except Exception as e:
                print(f"unable to convert datetime for item {item}")
                print("-------------------")
                print(e)
                print("-------------------")
                scheduled_time = ""

                continue


            if scheduled_time <= current_time:
                print("Selected time should be in the future.")
                continue

            time_difference = scheduled_time - current_time

            seconds = time_difference.total_seconds()

            self.s.enter(int(seconds), 1, callback, (item,))
            print(f"Function {item} scheduled to run at: {scheduled_time}")

        # Start the worker thread
        self.worker_thread.start()

    def run_function(self):
        print("Function is running!")

    def stop_event_listener(self):
        print("stoping keyboard listenr")




