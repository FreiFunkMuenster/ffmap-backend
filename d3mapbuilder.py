import json
import datetime

class D3MapBuilder:
  def __init__(self, db):
    self._db = db

  def build(self):
    output = dict()

    now = datetime.datetime.utcnow().replace(microsecond=0)

    nodes = self._db.get_nodes()
    #remove invalid nodes (without name)
    #nodes = list(filter(lambda x: x.name != "", nodes))

    output['nodes'] = [{'name': x.name, 'id': x.id,
                        'macs': ', '.join(x.macs),
                        'geo': [float(x) for x in x.gps.split(" ")] if x.gps else None,
                        'firmware': x.firmware,
                        'flags': x.flags,
                        'clientcount': x.clientcount,
                        'uptime': x.uptime,
                        'tx_bytes': x.tx_bytes,
                        'rx_bytes': x.rx_bytes,
                        'loadavg': x.loadavg,
                        'autoupdater': x.autoupdater,
                        'branch': x.branch,
                        'hardware': x.hardware,
                        'gateway': x.gateway
                       } for x in nodes]

    links = self._db.get_links()

    #remove invalid links
    #nodes = list(filter(lambda x: x.name != "", nodes))
    output['links'] = [{'source': x.source.id, 'target': x.target.id,
                        'quality': x.quality,
                        'type': x.type,
                        'id': x.id
                       } for x in links]

    output['meta'] = {
                      'timestamp': now.isoformat()
                     }

    return json.dumps(output)

