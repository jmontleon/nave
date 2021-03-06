#!/usr/bin/env python
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

"""Controller

This script will interact with the Vessel and transfer events to the Vessel as
they happen.  It will be run when the container starts and serves as a daemon.
"""

import argparse
import json
import sys

from vessel import Vessel
from mariadb_vessel.mariadb_vessel import MariadbVessel


def parser():
    parser = argparse.ArgumentParser(description='Vessel Client.')

    parser.add_argument("vessel",
                        help='Input which vessel to spawn')
    return parser.parse_args()


def cluster_event():
    """ Cluster event

        Look for any events in the cluster and make the Vessel aware of them.
    """
    print "Looking for Cluster Events..."


def main():
    args = parser()
    service = args.vessel

    vessel_dict = {'mariadb': MariadbVessel()}
    service_ves = vessel_dict.get(service)
    service_ves.get_tpr_data()


if __name__ == '__main__':
    sys.exit(main())
