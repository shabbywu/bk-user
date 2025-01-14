# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Department(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'has_children': 'bool',
        'full_name': 'str',
        'order': 'int',
        'extras': 'object',
        'enabled': 'bool',
        'code': 'str',
        'category_id': 'int',
        'lft': 'int',
        'rght': 'int',
        'tree_id': 'int',
        'level': 'int',
        'parent': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'has_children': 'has_children',
        'full_name': 'full_name',
        'order': 'order',
        'extras': 'extras',
        'enabled': 'enabled',
        'code': 'code',
        'category_id': 'category_id',
        'lft': 'lft',
        'rght': 'rght',
        'tree_id': 'tree_id',
        'level': 'level',
        'parent': 'parent'
    }

    def __init__(self, id=None, name=None, has_children=None, full_name=None, order=None, extras=None, enabled=True, code=None, category_id=None, lft=None, rght=None, tree_id=None, level=None, parent=None):  # noqa: E501
        """Department - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._has_children = None
        self._full_name = None
        self._order = None
        self._extras = None
        self._enabled = None
        self._code = None
        self._category_id = None
        self._lft = None
        self._rght = None
        self._tree_id = None
        self._level = None
        self._parent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if has_children is not None:
            self.has_children = has_children
        if full_name is not None:
            self.full_name = full_name
        if order is not None:
            self.order = order
        if extras is not None:
            self.extras = extras
        if enabled is not None:
            self.enabled = enabled
        if code is not None:
            self.code = code
        if category_id is not None:
            self.category_id = category_id
        if lft is not None:
            self.lft = lft
        if rght is not None:
            self.rght = rght
        if tree_id is not None:
            self.tree_id = tree_id
        if level is not None:
            self.level = level
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this Department.  # noqa: E501


        :return: The id of this Department.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Department.


        :param id: The id of this Department.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Department.  # noqa: E501


        :return: The name of this Department.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Department.


        :param name: The name of this Department.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def has_children(self):
        """Gets the has_children of this Department.  # noqa: E501


        :return: The has_children of this Department.  # noqa: E501
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """Sets the has_children of this Department.


        :param has_children: The has_children of this Department.  # noqa: E501
        :type: bool
        """

        self._has_children = has_children

    @property
    def full_name(self):
        """Gets the full_name of this Department.  # noqa: E501


        :return: The full_name of this Department.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Department.


        :param full_name: The full_name of this Department.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def order(self):
        """Gets the order of this Department.  # noqa: E501


        :return: The order of this Department.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Department.


        :param order: The order of this Department.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def extras(self):
        """Gets the extras of this Department.  # noqa: E501


        :return: The extras of this Department.  # noqa: E501
        :rtype: object
        """
        return self._extras

    @extras.setter
    def extras(self, extras):
        """Sets the extras of this Department.


        :param extras: The extras of this Department.  # noqa: E501
        :type: object
        """

        self._extras = extras

    @property
    def enabled(self):
        """Gets the enabled of this Department.  # noqa: E501


        :return: The enabled of this Department.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Department.


        :param enabled: The enabled of this Department.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def code(self):
        """Gets the code of this Department.  # noqa: E501


        :return: The code of this Department.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Department.


        :param code: The code of this Department.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def category_id(self):
        """Gets the category_id of this Department.  # noqa: E501


        :return: The category_id of this Department.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Department.


        :param category_id: The category_id of this Department.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def lft(self):
        """Gets the lft of this Department.  # noqa: E501


        :return: The lft of this Department.  # noqa: E501
        :rtype: int
        """
        return self._lft

    @lft.setter
    def lft(self, lft):
        """Sets the lft of this Department.


        :param lft: The lft of this Department.  # noqa: E501
        :type: int
        """

        self._lft = lft

    @property
    def rght(self):
        """Gets the rght of this Department.  # noqa: E501


        :return: The rght of this Department.  # noqa: E501
        :rtype: int
        """
        return self._rght

    @rght.setter
    def rght(self, rght):
        """Sets the rght of this Department.


        :param rght: The rght of this Department.  # noqa: E501
        :type: int
        """

        self._rght = rght

    @property
    def tree_id(self):
        """Gets the tree_id of this Department.  # noqa: E501


        :return: The tree_id of this Department.  # noqa: E501
        :rtype: int
        """
        return self._tree_id

    @tree_id.setter
    def tree_id(self, tree_id):
        """Sets the tree_id of this Department.


        :param tree_id: The tree_id of this Department.  # noqa: E501
        :type: int
        """

        self._tree_id = tree_id

    @property
    def level(self):
        """Gets the level of this Department.  # noqa: E501


        :return: The level of this Department.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Department.


        :param level: The level of this Department.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def parent(self):
        """Gets the parent of this Department.  # noqa: E501


        :return: The parent of this Department.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Department.


        :param parent: The parent of this Department.  # noqa: E501
        :type: int
        """

        self._parent = parent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Department, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Department):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
