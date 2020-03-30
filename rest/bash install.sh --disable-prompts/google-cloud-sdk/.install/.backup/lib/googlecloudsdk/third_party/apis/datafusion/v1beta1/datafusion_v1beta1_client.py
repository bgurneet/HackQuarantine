"""Generated client library for datafusion version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datafusion.v1beta1 import datafusion_v1beta1_messages as messages


class DatafusionV1beta1(base_api.BaseApiClient):
  """Generated client library for service datafusion version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://datafusion.googleapis.com/'
  MTLS_BASE_URL = u'https://datafusion.mtls.googleapis.com/'

  _PACKAGE = u'datafusion'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DatafusionV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new datafusion handle."""
    url = url or self.BASE_URL
    super(DatafusionV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = u'projects_locations_instances'

    def __init__(self, client):
      super(DatafusionV1beta1.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Data Fusion instance in the specified project and location.

      Args:
        request: (DatafusionProjectsLocationsInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.instances.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'instanceId'],
        relative_path=u'v1beta1/{+parent}/instances',
        request_field=u'instance',
        request_type_name=u'DatafusionProjectsLocationsInstancesCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Date Fusion instance.

      Args:
        request: (DatafusionProjectsLocationsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method=u'DELETE',
        method_id=u'datafusion.projects.locations.instances.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsInstancesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Data Fusion instance.

      Args:
        request: (DatafusionProjectsLocationsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.instances.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsInstancesGetRequest',
        response_type_name=u'Instance',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (DatafusionProjectsLocationsInstancesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.instances.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsInstancesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Data Fusion instances in the specified project and location.

      Args:
        request: (DatafusionProjectsLocationsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.instances.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'orderBy', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/instances',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsInstancesListRequest',
        response_type_name=u'ListInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a single Data Fusion instance.

      Args:
        request: (DatafusionProjectsLocationsInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method=u'PATCH',
        method_id=u'datafusion.projects.locations.instances.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta1/{+name}',
        request_field=u'instance',
        request_type_name=u'DatafusionProjectsLocationsInstancesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Restart(self, request, global_params=None):
      r"""Restart a single Data Fusion instance.
At the end of an operation instance is fully restarted.

      Args:
        request: (DatafusionProjectsLocationsInstancesRestartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Restart')
      return self._RunMethod(
          config, request, global_params=global_params)

    Restart.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:restart',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.instances.restart',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:restart',
        request_field=u'restartInstanceRequest',
        request_type_name=u'DatafusionProjectsLocationsInstancesRestartRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (DatafusionProjectsLocationsInstancesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.instances.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'DatafusionProjectsLocationsInstancesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (DatafusionProjectsLocationsInstancesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.instances.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'DatafusionProjectsLocationsInstancesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Upgrade(self, request, global_params=None):
      r"""Upgrade a single Data Fusion instance.
At the end of an operation instance is fully upgraded.

      Args:
        request: (DatafusionProjectsLocationsInstancesUpgradeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Upgrade')
      return self._RunMethod(
          config, request, global_params=global_params)

    Upgrade.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:upgrade',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.instances.upgrade',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:upgrade',
        request_field=u'upgradeInstanceRequest',
        request_type_name=u'DatafusionProjectsLocationsInstancesUpgradeRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = u'projects_locations_operations'

    def __init__(self, client):
      super(DatafusionV1beta1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (DatafusionProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'datafusion.projects.locations.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'DatafusionProjectsLocationsOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatafusionProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'datafusion.projects.locations.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (DatafusionProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (DatafusionProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/operations',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(DatafusionV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (DatafusionProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (DatafusionProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'datafusion.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'includeUnrevealedLocations', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/locations',
        request_field='',
        request_type_name=u'DatafusionProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DatafusionV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
