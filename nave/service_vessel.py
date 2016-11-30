# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Service Vessel class."""

from vessel import Vessel


class ServiceVessel(Vessel):

    def __init__(self, data):
        self.data = data
        super(ServiceVessel, self).__init__(data)

    def _database_action(self):
        """Register a service's user and password in the database"""

        pass

    def _keystone_action(self):
        """Register a service user and role in Keystone"""

        pass

    def _run_helm_package(self):
        """Execute a Helm package for a service"""

        pass
