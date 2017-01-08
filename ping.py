

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    if  platform.system().lower()=="windows":
        ping_str = "-n"
    else:
        ping_str = "-c"

    # Ping
    return os.system("ping " + ping_str + " 1 " + host) == 0


ping("192.168.1.142")
