#!/usr/bin/python3
"""Module that defines MyInt class"""


class MyInt(int):
    """Class MyInt that inherits from int class"""

    def __eq__(self, num):
        """
            Overrides the '==' and '!=' operators.

            Args:
                num (int): number
        """
        return (not super().__eq__(num))

    def __ne__(self, num):
        """
            Overrides the '==' and '!=' operators.

            Args:
                num (int): number.
        """
        return (super().__eq__(num))
