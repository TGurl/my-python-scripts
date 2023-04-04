#!/usr/bin/env python
from dataclasses import dataclass

@dataclass
class CONFIG:
    version = str
    title = str

@dataclass
class MC:
    age: int
    bank: int
    location: str
    job: str
