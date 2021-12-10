"""Employee Model."""

from masoniteorm.models import Model


class Employee(Model):
    __table__="employees"