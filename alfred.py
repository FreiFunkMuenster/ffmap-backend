#!/usr/bin/env python3
import subprocess
import json

class alfred:
  def __init__(self,request_data_type = 158, request_statistics_data_type = 159):
    self.request_data_type = request_data_type
    self.request_statistics_data_type = request_statistics_data_type

  def aliases(self):
    output = subprocess.check_output(["alfred-json","-r",str(self.request_data_type),"-f","json","-z"])
    alfred_data = json.loads(output.decode("utf-8"))
    alias = {}
    for mac,node in alfred_data.items():
      node_alias = {}
      if 'location' in node:
        try:
          node_alias['gps'] = str(node['location']['latitude']) + ' ' + str(node['location']['longitude'])
        except:
          pass
      if 'statistics' in node:
        try:
          node_alias['uptime'] = node['statistics']['uptime']
        except:
          pass
        try:
          node_alias['tx_bytes'] = node['statistics']['traffic']['tx']['bytes']
          node_alias['rx_bytes'] = node['statistics']['traffic']['rx']['bytes']
        except:
          pass
        try:
          node_alias['loadavg'] = node['statistics']['loadavg']
        except:
          pass
      try:
        node_alias['firmware'] = node['software']['firmware']['release']
        node_alias['autoupdater'] = node['software']['autoupdater']['enabled']
        node_alias['branch'] = node['software']['autoupdater']['branch']
      except KeyError:
        pass
      try:
        node_alias['hardware'] = node['hardware']['model']
      except KeyError:
        pass
      try:
        node_alias['id'] = node['network']['mac']
      except KeyError:
        pass
      if 'hostname' in node:
        node_alias['name'] = node['hostname']
      elif 'name' in node:
        node_alias['name'] = node['name']
      if len(node_alias):
        alias[mac] = node_alias
    return alias

  def statistics(self):
    output = subprocess.check_output(["alfred-json","-r",str(self.request_statistics_data_type),"-f","json","-z"])
    alfred_data = json.loads(output.decode("utf-8"))
    alias = {}
    for mac,node in alfred_data.items():
      node_alias = {}
      try:
          node_alias['gateway'] = node['gateway']
      except:
          pass      
      try:
          node_alias['uptime'] = node['uptime']
      except:
          pass
      try:
          node_alias['tx_bytes'] = node['traffic']['tx']['bytes']
          node_alias['rx_bytes'] = node['traffic']['rx']['bytes']
      except:
          pass
      try:
          node_alias['loadavg'] = node['loadavg']
      except:
          pass
      if len(node_alias):
        alias[mac] = node_alias
    return alias

if __name__ == "__main__":
  ad = alfred()
  al = ad.aliases()
  print(al)
