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

import collections

from tuskar_ui import api

from openstack_dashboard.test.test_data import utils as test_data_utils

from novaclient.v1_1.contrib import baremetal
from tuskarclient.v1 import flavors
from tuskarclient.v1 import racks
from tuskarclient.v1 import resource_classes


def data(TEST):
    FlavorTemplateStruct = collections.namedtuple('FlavorStruct',
                                                  'id name capacities')
    CapacityStruct = collections.namedtuple('CapacityStruct',
                                            'name value unit')
    TEST.tuskar_flavor_templates = test_data_utils.TestDataContainer()
    flavor_template_1 = api.FlavorTemplate(
        FlavorTemplateStruct(
            id="1",
            name='nano',
            capacities=[
                api.Capacity(CapacityStruct(
                    name='cpu',
                    unit='',
                    value='1')),
                api.Capacity(CapacityStruct(
                    name='memory',
                    unit='MB',
                    value='64')),
                api.Capacity(CapacityStruct(
                    name='storage',
                    unit='MB',
                    value='128')),
                api.Capacity(CapacityStruct(
                    name='ephemeral_disk',
                    unit='GB',
                    value='0')),
                api.Capacity(CapacityStruct(
                    name='swap_disk',
                    unit='GB',
                    value='0'))]))
    flavor_template_2 = api.FlavorTemplate(
        FlavorTemplateStruct(
            id="2",
            name='large',
            capacities=[]))
    TEST.tuskar_flavor_templates.add(flavor_template_1, flavor_template_2)

    # Flavors
    TEST.tuskarclient_flavors = test_data_utils.TestDataContainer()
    TEST.tuskar_flavors = test_data_utils.TestDataContainer()
    flavor_1 = flavors.Flavor(flavors.FlavorManager(None),
                              {'id': '1',
                               'name': 'nano',
                               'max_vms': 100,
                               'capacities':
                                   [{"name": "cpu",
                                     "value": 64,
                                     "unit": "CPU"},
                                    {"name": "memory",
                                     "value": 1024,
                                     "unit": "MB"},
                                    {"name": "storage",
                                     "value": 1,
                                     "unit": "GB"},
                                    {"name": "ephemeral_disk",
                                     "value": 0,
                                     "unit": "GB"},
                                    {"name": "swap_disk",
                                     "value": 2,
                                     "unit": "GB"}]})
    flavor_2 = flavors.Flavor(flavors.FlavorManager(None),
                              {'id': '2',
                               'name': 'large',
                               'max_vms': 10,
                               'capacities': []})
    TEST.tuskarclient_flavors.add(flavor_1, flavor_2)
    TEST.tuskar_flavors.add(api.Flavor(flavor_1), api.Flavor(flavor_2))

    # Resource Classes
    TEST.tuskarclient_resource_classes = test_data_utils.TestDataContainer()
    TEST.tuskar_resource_classes = test_data_utils.TestDataContainer()
    resource_class_1 = resource_classes.ResourceClass(
        resource_classes.ResourceClassManager(None),
        {'id': '1',
         'service_type': 'compute',
         'racks': [{'id': 1}, {'id': 2}],
         'name': 'rclass1'})
    resource_class_2 = resource_classes.ResourceClass(
        resource_classes.ResourceClassManager(None),
        {'id': '2',
         'service_type': 'compute',
         'racks': [],
         'name': 'rclass2'})
    TEST.tuskarclient_resource_classes.add(resource_class_1, resource_class_2)
    TEST.tuskar_resource_classes.add(api.ResourceClass(resource_class_1),
                                     api.ResourceClass(resource_class_2))

    #Racks
    TEST.tuskarclient_racks = test_data_utils.TestDataContainer()
    TEST.tuskar_racks = test_data_utils.TestDataContainer()
    rack_1 = racks.Rack(racks.RackManager(None),
                        {'id': '1',
                         'name': 'rack1',
                         'location': 'location',
                         'subnet': '192.168.1.0/24',
                         'state': 'active',
                         'nodes':
                             [{'id': '1'},
                              {'id': '2'},
                              {'id': '3'},
                              {'id': '4'}],
                         'capacities':
                             [{"name": "total_cpu",
                               "value": "64",
                               "unit": "CPU"},
                              {"name": "total_memory",
                               "value": "1024",
                               "unit": "MB"}],
                         'resource_class': {'id': '1'}})
    rack_2 = racks.Rack(racks.RackManager(None),
                        {'id': '2',
                         'name': 'rack2',
                         'location': 'location',
                         'subnet': '192.168.1.0/25',
                         'state': 'provisioning',
                         'nodes': [],
                         'capacities':
                             [{"name": "total_cpu",
                               "value": "1",
                               "unit": "CPU"},
                              {"name": "total_memory",
                               "value": "4",
                               "unit": "MB"}],
                         'resource_class': {'id': '1'}})
    rack_3 = racks.Rack(racks.RackManager(None),
                        {'id': '3',
                         'name': 'rack3',
                         'location': 'location',
                         'subnet': '192.168.1.0/26',
                         'state': 'inactive',
                         'nodes': [],
                         'capacities':
                             [{"name": "total_cpu",
                               "value": "1",
                               "unit": "CPU"},
                              {"name": "total_memory",
                               "value": "2",
                               "unit": "MB"}],
                         'resource_class': None})
    TEST.tuskarclient_racks.add(rack_1, rack_2, rack_3)
    TEST.tuskar_racks.add(api.Rack(rack_1), api.Rack(rack_2), api.Rack(rack_3))

    # Nodes
    TEST.baremetalclient_nodes = test_data_utils.TestDataContainer()
    TEST.baremetal_nodes = test_data_utils.TestDataContainer()
    TEST.baremetalclient_unracked_nodes = test_data_utils.TestDataContainer()
    TEST.baremetal_unracked_nodes = test_data_utils.TestDataContainer()
    TEST.baremetalclient_nodes_all = test_data_utils.TestDataContainer()
    TEST.baremetal_nodes_all = test_data_utils.TestDataContainer()

    node_1 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '1',
         'name': 'node1',
         'prov_mac_address': '00-B0-D0-86-AB-F7'})
    node_2 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '2',
         'name': 'node2',
         'prov_mac_address': '00-B0-D0-86-AB-F8'})
    node_3 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '3',
         'name': 'node3',
         'prov_mac_address': '00-B0-D0-86-AB-F9'})
    node_4 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '4',
         'name': 'node4',
         'prov_mac_address': '00-B0-D0-86-AB-F0'})
    node_5 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '5',
         'name': 'node5',
         'prov_mac_address': '00-B0-D0-86-AB-F1'})

    TEST.baremetalclient_nodes.add(node_1, node_2, node_3, node_4)
    TEST.baremetal_nodes.add(api.Node(node_1),
                             api.Node(node_2),
                             api.Node(node_3),
                             api.Node(node_4))
    TEST.baremetalclient_unracked_nodes.add(node_5)
    TEST.baremetal_unracked_nodes.add(api.Node(node_5))
    TEST.baremetalclient_nodes_all.add(node_1, node_2, node_3, node_4, node_5)
    TEST.baremetal_nodes_all.add(api.Node(node_1),
                             api.Node(node_2),
                             api.Node(node_3),
                             api.Node(node_4),
                             api.Node(node_5))
