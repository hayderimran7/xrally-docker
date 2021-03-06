# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally.task import scenario


def configure(name=None, context=None):
    return scenario.configure(name=name, namespace="docker", context=context)


class BaseDockerScenario(scenario.Scenario):
    def __init__(self, context=None):
        super(BaseDockerScenario, self).__init__(context)
        if "admin" in self.context:
            self.client = self.context["admin"]["credential"].clients()
        else:
            self.client = None
