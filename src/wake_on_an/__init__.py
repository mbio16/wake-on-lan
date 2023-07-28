import re
from wakeonlan import send_magic_packet
import logging


class WOL:
    def __init__(
        self,
        mac: str,
        ip: str | None,
        port: int | None,
    ) -> None:
        if self.__valid_mac(mac):
            logging.info("Mac is valid")
            self.mac = mac
            self.ip = self.__set_ip(ip)
            self.port = self.__set_port(port)
            logging.debug(
                "MAC: {}, IP: {}, PORT: {}".format(
                    str(self.mac), str(self.ip), str(self.port)
                )
            )
        else:
            logging.error("Mac address is not valid")
            raise Exception("Mac address is not valid")

    def __set_ip(self, ip: str | None) -> str:
        if ip is None:
            return "255.255.255.255"
        else:
            return ip

    def __set_port(self, port: int | None) -> int:
        if port is None:
            return 9
        else:
            return int(port)

    def __valid_mac(self, mac: str) -> bool:
        return re.match(
            "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()
        )

    def send_packet(self) -> None:
        logging.info(
            "Sending magic packet... to: {} and MAC: {} ...".format(
                str(self.ip), str(self.mac)
            )
        )
        send_magic_packet(
            self.mac,
            ip_address=self.ip,
            port=self.port,
        )
        logging.info("Packet sent")
