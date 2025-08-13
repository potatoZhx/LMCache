# SPDX-License-Identifier: Apache-2.0
# Standard
from typing import Dict, Union

# First Party
from lmcache.logging import init_logger
from lmcache.v1.cache_controller.message import (
    GetP2PStatsMsg,
    GetP2PStatsRetMsg,
    P2PStatsUpdateMsg,
)

logger = init_logger(__name__)


class P2PStatsController:
    def __init__(self):
        self.p2p_stats: Dict[str, Dict[str, Dict[str, Union[int, float]]]] = {}

    async def update(self, msg: P2PStatsUpdateMsg) -> None:
        """
        Update p2p transfer infos for a given instance.
        """
        instance_id = msg.instance_id
        p2p_stats_to_update = msg.p2p_stats
        if instance_id not in self.p2p_stats:
            self.p2p_stats[instance_id] = {}
        for backend_name, p2p_stats_backend in p2p_stats_to_update.items():
            if p2p_stats_backend != {}:
                self.p2p_stats[instance_id][backend_name] = p2p_stats_backend

    async def get_p2p_stats(self, msg: GetP2PStatsMsg) -> GetP2PStatsRetMsg:
        """
        Get p2p transfer info for a given instance.
        """
        instance_id = msg.instance_id
        if instance_id not in self.p2p_stats:
            return GetP2PStatsRetMsg(p2p_stats={})
        return GetP2PStatsRetMsg(p2p_stats=self.p2p_stats[instance_id])
