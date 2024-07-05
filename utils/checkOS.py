import platform


def detect_os() -> str:
    return(platform.system())