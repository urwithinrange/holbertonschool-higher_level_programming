#!/usr/bin/python3
"""Class LockedClass"""


class LockedClass:
    """Prevents the user from dynamically \
    from creating new instance attributes
    """
    __slots__ = ["first_name"]
