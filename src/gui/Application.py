#  PyMODA, a Python implementation of MODA (Multiscale Oscillatory Dynamics Analysis).
#  Copyright (C) 2019  Lancaster University
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
from typing import Type

from PyQt5.QtWidgets import QApplication

from gui.windows.base.BaseWindow import BaseWindow
from gui.windows.bispectrum.BAWindow import BAWindow
from gui.windows.phasecoherence.PCWindow import PCWindow
from gui.windows.ridgeextraction.REWindow import REWindow
from gui.windows.timefrequency.TFWindow import TFWindow
from gui.windows.LauncherWindow import LauncherWindow
from utils import cache


class Application(QApplication):
    """The base application."""

    launcher_window = None
    windows = []

    def __init__(self, args):
        super(Application, self).__init__(args)
        self.start_launcher()

    def start_launcher(self):
        """Opens the launcher window."""
        self.launcher_window = LauncherWindow(self)
        self.launcher_window.show()

    def start_time_frequency(self):
        """Opens the time-frequency window."""
        self.open_window(TFWindow)

    def start_phase_coherence(self):
        """Opens the phase coherence window."""
        self.open_window(PCWindow)

    def start_ridge_extraction(self):
        """Opens the phase coherence window."""
        self.open_window(REWindow)

    def start_bispectrum(self):
        """Opens the wavelet bispectrum analysis window."""
        self.open_window(BAWindow)

    def start_bayesian(self):
        """Opens the Bayesian inference window."""
        raise Exception("Dynamical Bayesian inference is not implemented yet.")
        # self.open_window(DBIWindow)

    def open_window(self, WindowType: Type[BaseWindow]):
        w = WindowType(self)
        self.windows.append(w)
        w.show()

    def notify_close_event(self, window: BaseWindow):
        try:
            self.windows.remove(window)
        except ValueError:
            pass

        if len(self.windows) == 0:
            cache.clear()
