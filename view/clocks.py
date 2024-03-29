from textual.app import ComposeResult
from textual.widgets import Static
from widgets.logo import Logo

from widgets.clock import Clock


class Clocks(Static):
    DEFAULT_CSS = """
        Clocks {
            layout: grid;
            grid-size: 4 1;
            grid-gutter: 15;
            height: 20%;
            min-height: 5;
            align: center top;
            padding: 0 0 0 0;
            border: none;
            background: $primary-darken-1;
        }
    """

    def compose(self) -> ComposeResult:
        yield Logo()
        yield Clock(label="America/New_York")
        yield Clock(label="UTC")
        yield Clock(label="Etc/GMT+12")
