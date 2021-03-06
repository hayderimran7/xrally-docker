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

from xrally_docker.contexts import base


@base.configure("images", order=100, hidden=True)
class ImagesContext(base.BaseDockerContext):
    """Pull new images or load existing ones."""

    CONFIG_SCHEMA = {
        "type": "object",
        "properties": {
            "existing": {"description": "Load all existing images",
                         "type": "boolean"},
            "names": {"description": "Pull images from the list.",
                      "type": "array",
                      "items": {
                          "type": "string",
                          "description": "The image to pull. (if the tag of "
                                         "image is not specified, 'latest' "
                                         "will be used)."}}},
        "additionalProperties": False
    }

    DEFAULT_CONFIG = {"names": []}

    def setup(self):
        self.context["docker"]["images"] = []

        for name in self.config["names"]:
            if ":" not in name:
                name = "%s:latest" % name
            self.context["docker"]["images"].append(
                self.client().images.pull(name))

        if self.config.get("existing", bool(self.config["names"])):
            self.context["docker"]["images"].extend(
                self.client().images.list())

    def cleanup(self):
        # TODO(andreykurilin): remove uploaded images
        pass
