import connexion
import json
from pprint import pprint
import os

from napps.snlab.unicorn_resource_discovery.models.error_response import ErrorResponse
from napps.snlab.unicorn_resource_discovery.models.path_query_response import PathQueryResponse
from napps.snlab.unicorn_resource_discovery.models.query_requests import QueryRequests
from napps.snlab.unicorn_resource_discovery.models.resource_query_response import ResourceQueryResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

#from kytos.core import log
from kytos.core import KytosEvent, log
from kytos.core.helpers import listen_to
from pyof.foundation.network_types import Ethernet
from pyof.v0x01.asynchronous.packet_in import PacketInReason
from pyof.v0x01.common.action import ActionOutput
from pyof.v0x01.common.flow_match import Match
from pyof.v0x01.common.phy_port import Port
from pyof.v0x01.controller2switch.flow_mod import FlowMod, FlowModCommand
from pyof.v0x01.controller2switch.packet_out import PacketOut


def query_path_post(query_set):
    """
    query_path_post
    query the ingress point of the next domain
    :param query_set: a set of path queries
    :type query_set: dict | bytes

    :rtype: PathQueryResponse
    """
    if connexion.request.is_json:
        query_set = QueryRequests.from_dict(connexion.request.get_json())
        log.info(query_set[0])
        log.info(len(query_set))

        """
        open the egress2ingress mapping file
        """
#        pprint(json.loads(connexion.request.get_json()))
        with open(os.path.dirname(__file__) + '/../egress2ingress-config.json') as data_file:
            egress2ingress = json.load(data_file)
        pprint(egress2ingress)

        next_ingress_array = []

        for query in query_set:

            """
            get the egress point of each flow
            """
            egress = get_egress_point(query)

            """
            get the next ingress point of each flow from pre-configured e2i mapping
            """
#            print(egress2ingress[egress[0]][egress[1]])
            next_ingress_array.append("{0}".format(egress2ingress[egress[0]][egress[1]]))
#    print(next_ingress_array)
    return next_ingress_array
#    return json.dumps(["1.2.3.4", "3.4.5.6"])
#    return json.dumps(next_ingress_array)    
#    return connexion.request.get_json()
    #return 'do some magic!'


def query_resource_post(query_set):
    """
    query_resource_post
    query the resource availability of the current domain for a given set of flows
    :param query_set: a set of resource queries
    :type query_set: dict | bytes

    :rtype: ResourceQueryResponse
    """
    if connexion.request.is_json:
        query_set = QueryRequests.from_dict(connexion.request.get_json())
    return 'do some magic!'

def get_egress_point(query):
    return ('192.151.1.102', '2')



#@listen_to('kytos/of_core.v0x01.messages.in.ofpt_packet_in')
#def handle_packet_in(self, event):
#    log.info("packet is in")
#    packet_in = event.content['message']
#
#    ethernet = Ethernet()
#    ethernet.unpack(packet_in.data.value)
#
#    in_port = packet_in.in_port.value
#    switch = event.source.switch
#    switch.update_mac_table(ethernet.source, in_port)
#    log.info('Packet received from %s to %s.', ethernet.source.value,\
#         ethernet.destination.value)
#

#@listen_to('tutorial/ping.periodic_ping')
#def pong(self, event):
#    message = 'Hi, here is the Pong NApp answering a ping.'
#    message += 'The current time is {}, and the ping was dispatched '
#    message += 'at {}.'
#    log.info(message.format(datetime.now(), event.content['message']))
#













