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

from rally.task import context

from xrally_docker import client


def configure(name, order, hidden=False):
    return context.configure(name, namespace="docker", order=order,
                             hidden=hidden)


@context.configure("users", namespace="docker", order=1)
class UsersContext(context.Context):
    """A dummy context for Docker."""

    CONFIG_SCHEMA = {"type": "object", "additionalProperties": False}

    def setup(self):
        self.context["users"] = []
        self.context["docker"] = {}

    def cleanup(self):
        pass


class BaseDockerContext(context.Context):
    CONFIG_SCHEMA = {"type": "object", "additionalProperties": False}

    def __init__(self, ctx):
        super(BaseDockerContext, self).__init__(ctx)
        self.client = client.DockerClient(self.context["admin"]["credential"])
