# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class AutoQuotaIncreaseOperations(object):
    """AutoQuotaIncreaseOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Api version. Constant value: "2019-07-19-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-07-19-preview"

        self.config = config

    def get_properties(
            self, subscription_id, custom_headers=None, raw=False, **operation_config):
        """For the specified subscription, gets the Auto Quota Increase enrollment
        status.

        Gets the Auto Quota Increase enrollment details for the specified
        subscription.

        :param subscription_id: Azure subscription id.
        :type subscription_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AutoQuotaIncreaseDetail or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.reservations.models.AutoQuotaIncreaseDetail or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.reservations.models.ExceptionResponseException>`
        """
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AutoQuotaIncreaseDetail', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_properties.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/autoQuotaIncrease'}

    def create(
            self, subscription_id, auto_quota_increase_request, custom_headers=None, raw=False, **operation_config):
        """For the specified subscription, sets the Auto Quota Increase enrollment
        properties.

        Sets the Auto Quota Increase enrollment properties for the specified
        subscription.

        :param subscription_id: Azure subscription id.
        :type subscription_id: str
        :param auto_quota_increase_request: Auto Quota increase request
         payload.
        :type auto_quota_increase_request:
         ~azure.mgmt.reservations.models.AutoQuotaIncreaseDetail
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AutoQuotaIncreaseDetail or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.reservations.models.AutoQuotaIncreaseDetail or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.reservations.models.ExceptionResponseException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(auto_quota_increase_request, 'AutoQuotaIncreaseDetail')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AutoQuotaIncreaseDetail', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/autoQuotaIncrease'}
