# coding: utf-8

"""
    katib

    swagger description for katib  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha3NasConfig(object):
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
        'graph_config': 'V1alpha3GraphConfig',
        'operations': 'list[V1alpha3Operation]'
    }

    attribute_map = {
        'graph_config': 'graphConfig',
        'operations': 'operations'
    }

    def __init__(self, graph_config=None, operations=None):  # noqa: E501
        """V1alpha3NasConfig - a model defined in Swagger"""  # noqa: E501

        self._graph_config = None
        self._operations = None
        self.discriminator = None

        if graph_config is not None:
            self.graph_config = graph_config
        if operations is not None:
            self.operations = operations

    @property
    def graph_config(self):
        """Gets the graph_config of this V1alpha3NasConfig.  # noqa: E501


        :return: The graph_config of this V1alpha3NasConfig.  # noqa: E501
        :rtype: V1alpha3GraphConfig
        """
        return self._graph_config

    @graph_config.setter
    def graph_config(self, graph_config):
        """Sets the graph_config of this V1alpha3NasConfig.


        :param graph_config: The graph_config of this V1alpha3NasConfig.  # noqa: E501
        :type: V1alpha3GraphConfig
        """

        self._graph_config = graph_config

    @property
    def operations(self):
        """Gets the operations of this V1alpha3NasConfig.  # noqa: E501


        :return: The operations of this V1alpha3NasConfig.  # noqa: E501
        :rtype: list[V1alpha3Operation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this V1alpha3NasConfig.


        :param operations: The operations of this V1alpha3NasConfig.  # noqa: E501
        :type: list[V1alpha3Operation]
        """

        self._operations = operations

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
        if issubclass(V1alpha3NasConfig, dict):
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
        if not isinstance(other, V1alpha3NasConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
