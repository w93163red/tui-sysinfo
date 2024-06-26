from datetime import datetime

import pytz
from textual.reactive import reactive
from textual.widgets import Static, Digits


class Clock(Static):
    currentTime = reactive(datetime.now().strftime("%H:%M:%S"))
    currentDate = reactive(datetime.now().strftime("%m-%d-%Y"))
    blink = reactive(False)

    DEFAULT_CSS = """
        Clock {
            align-horizontal: center;
            box-sizing: content-box;
            border: round white;
            max-width: 30;
            width: auto;
            align: center middle;
            border-title-style: italic;
            border-title-align: center;
        }
      
        Digits {
            text-align: center;
        }
    
        .clock-time {
            text-align: center;
        }
    """

    def __init__(self, label,
                 name: str | None = None,
                 id: str | None = None,
                 classes: str | None = None,
                 disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.label = label
        if label == 'Etc/GMT+12':
            self.border_title = "Anywhere on Earth"
        else:
            self.border_title = label

    def on_mount(self):
        self.set_interval(1, self.update_time)

    def compose(self):
        yield Digits(self.currentDate, id="clock-date")
        yield Digits(self.currentTime, id="clock-time")

    def update_time(self):
        self.currentTime = self.get_time()
        self.currentDate = self.get_date()
        self.blink = not self.blink

    def get_time(self):
        return datetime.now(pytz.timezone(self.label)).strftime("%H:%M:%S")

    def get_date(self):
        return datetime.now(pytz.timezone(self.label)).strftime("%m-%d-%Y")

    def watch_currentTime(self):
        try:
            self.query_one("#clock-time").update(self.currentTime)
            self.query_one("#clock-date").update(self.currentDate)
            if self.blink:
                self.styles.border = ("blank", "white")
            else:
                self.styles.border = ("round", "white")
        except Exception as e:
            print(e)
