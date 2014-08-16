class Node():
  def __init__(self):
    self.name = ""
    self.id = ""
    self.macs = set()
    self.interfaces = dict()
    self.flags = dict({
      "online": False,
      "gateway": False,
      "client": False
    })
    self.gps = None
    self.firmware = None
    self.clientcount = 0
    self.lastseen = 0
    self.uptime = 0.0
    self.tx_bytes = 0
    self.rx_bytes = 0
    self.loadavg = 0.0
    self.autoupdater = False
    self.branch = ""
    self.hardware = ""
    self.gateway = ""

  def add_mac(self, mac):
    mac = mac.lower()
    if len(self.macs) == 0:
      self.id = mac

    self.macs.add(mac)

    self.interfaces[mac] = Interface()

  def __repr__(self):
    return self.macs.__repr__()

class Interface():
  def __init__(self):
    self.vpn = False

