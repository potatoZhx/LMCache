# SPDX-License-Identifier: Apache-2.0
# Standard
from typing import Dict, Union

# First Party
from lmcache.logging import init_logger
from lmcache.v1.cache_controller.message import (
    GetP2PInfoMsg,
    GetP2PInfoRetMsg,
    P2PInfoUpdateMsg,
)

logger = init_logger(__name__)


class P2PInfoController:
    def __init__(self):
        self.p2p_info: Dict[str, Dict[str, Dict[str, Union[int, float]]]] = {}

    async def update(self, msg: P2PInfoUpdateMsg) -> None:
        """
        Update p2p transfer infos for a given instance.
        """
        logger.info(f"update p2p info: {msg.p2p_info}")
        instance_id = msg.instance_id
        p2p_info_to_update = msg.p2p_info
        if instance_id not in self.p2p_info:
            self.p2p_info[instance_id] = {}
        for backend_name, p2p_info_backend in p2p_info_to_update.items():
            if p2p_info_backend != {}:
                self.p2p_info[instance_id][backend_name] = p2p_info_backend

    async def get_p2p_info(self, msg: GetP2PInfoMsg) -> GetP2PInfoRetMsg:
        """
        Get p2p transfer info for a given instance.
        """
        instance_id = msg.instance_id
        if instance_id not in self.p2p_info:
            return GetP2PInfoRetMsg(p2p_info={})
        return GetP2PInfoRetMsg(p2p_info=self.p2p_info[instance_id])
