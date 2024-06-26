from textual.app import ComposeResult
from textual.widgets import Static

from widgets.clock import Clock


class Clocks(Static):
    DEFAULT_CSS = """
        Clocks {
            layout: grid;
            grid-size: 3 1;
            grid-gutter: 15;
            height: 100%;
            min-height: 5;
            align: center top;
            padding: 0 0 0 0;
            border: none;
        }
    """

    def compose(self) -> ComposeResult:
        yield Clock(label="America/New_York")
        yield Clock(label="UTC")
        yield Clock(label="Etc/GMT+12")
