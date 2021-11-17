"""Custom class code"""

import numpy as np
from magpylib._src.obj_classes.class_BaseGeo import BaseGeo
from magpylib._src.obj_classes.class_BaseDisplayRepr import BaseDisplayRepr
from magpylib._src.obj_classes.class_BaseGetBH import BaseGetBH
from magpylib._src.default_classes import default_settings as Config
from magpylib._src.input_checks import check_vector_format, check_vector_type


# ON INTERFACE
class Custom(BaseGeo, BaseDisplayRepr, BaseGetBH):
    """
    Custom Source class

    Parameters
    ----------
    field_B_lambda: function
        field function for B-field, should accept (n,3) position array and return
        B-field array of same shape. 

    field_H_lambda: function
        field function for H-field, should accept (n,3) position array and return
        H-field array of same shape. 

    position: array_like, shape (3,) or (M,3), default=(0,0,0)
        Object position (local CS origin) in the global CS in units of [mm].
        For M>1, the position represents a path. The position and orientation
        parameters must always be of the same length.

    orientation: scipy Rotation object with length 1 or M, default=unit rotation
        Object orientation (local CS orientation) in the global CS. For M>1
        orientation represents different values along a path. The position and
        orientation parameters must always be of the same length.

    Returns
    -------
    Custom object: Custom

    Examples
    --------
    By default a Dipole is initialized at position (0,0,0), with unit rotation:

    """

    def __init__(
        self,
        field_B_lambda=None,
        field_H_lambda=None,
        position=(0, 0, 0),
        orientation=None,
        style=None,
    ):
        # instance attributes
        self.field_B_lambda = field_B_lambda
        self.field_H_lambda = field_H_lambda
        self._object_type = "Custom"

        # init inheritance
        BaseGeo.__init__(self, position, orientation, style=style)
        BaseDisplayRepr.__init__(self)

