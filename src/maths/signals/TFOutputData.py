#  PyMODA, a Python implementation of MODA (Multiscale Oscillatory Dynamics Analysis).
#  Copyright (C) 2019 Lancaster University
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


class TFOutputData:
    """
    A class which contains the time-frequency output data required
    for plotting the appropriate transform.
    """

    def __init__(self,
                 times,
                 values,
                 ampl,
                 freq,
                 powers,
                 avg_ampl,
                 avg_pow,
                 transform="wt",
                 overall_coherence=None,
                 phase_coherence=None,
                 phase_diff=None,
                 tfsupp=None,
                 ):
        self.times = times
        self.transform = transform
        self.values = values

        self.ampl = ampl
        self.freq = freq
        self.powers = powers

        self.avg_ampl = avg_ampl
        self.avg_pow = avg_pow

        self.overall_coherence = overall_coherence
        self.phase_coherence = phase_coherence
        self.phase_diff = phase_diff
        self.surrogate_avg = None

        self.iamp = tfsupp
        self.valid = True

    def is_valid(self):
        """Returns whether the data is valid and should be plotted."""
        return self.valid and len(self.times) > 0 and len(self.freq) > 0 and len(self.ampl) > 0

    def invalidate(self):
        """
        Sets the data to None, which should free up memory when the
        garbage collector runs.
        """
        self.valid = False
        self.times = None
        self.values = None
        self.ampl = None
        self.freq = None
        self.powers = None
        self.avg_ampl = None
        self.avg_pow = None
        self.iamp = None
        self.re_transform = None

    def has_phase_coherence(self):
        return not (self.overall_coherence is None or len(self.freq) != len(self.overall_coherence))

    def has_surrogates(self):
        return self.surrogate_avg is not None

    def has_ridge_data(self) -> bool:
        return self.iamp is not None

    @staticmethod
    def empty():
        """
        Creates an instance of this class with only empty lists as data.
        """
        return TFOutputData(*[[] for _ in range(8)])