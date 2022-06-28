# -*- coding:utf-8 -*-

class No:
    def __init__(self, value, priority):
        self._value = value
        self._priority = priority
        self.next = None

    def __str__(self):
        return str(f"{self._value} - {self._priority}")

    def __repr__(self):
        return repr(f"{self._value} - {self._priority}")

    def priority(self):
        return self._priority