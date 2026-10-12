"""Валидация IP адресов"""

def is_valid_ipv4(ip: str) -> bool:
    
    if not isinstance(ip, str):
        return False

    octets = ip.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        if len(octet) > 1 and octet.startswith("0"):
            return False
        if not (0 <= int(octet) <= 255):
            return False
    
    return True


if __name__ == "__main__":
    print(is_valid_ipv4("1.1.1.1"))
