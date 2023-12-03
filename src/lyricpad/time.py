import fractions
from typing import Optional

class TimeSig:
    num_beats:int
    beat_length:int


class Rhythm:
    def __init__(self) -> None:
        self.beats_per_bar = 4
        self.beat_length = 4
        self.bpm = 120

    @property
    def time_sig(self):
        return fractions.Fraction(self.beats_per_bar, self.beat_length)


class Beat:
    pass

class Bar:
    rhythm:Rhythm


class Timeline:
    pass

class TimeGrid:
    pass


def beats_to_seconds(num_beats:int, bpm:float|Rhythm):
    if isinstance(bpm,Rhythm):
        bpm = bpm.bpm
    return num_beats / bpm * 60

