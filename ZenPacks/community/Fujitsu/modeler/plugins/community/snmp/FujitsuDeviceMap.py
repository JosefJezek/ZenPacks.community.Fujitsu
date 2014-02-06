__doc__ = """FujitsuDeviceMap

Gather Fujitsu hardware model + serial number and OS information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap

class FujitsuDeviceMap(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.231.2.10.2.2.10.2.3.1.5.1': 'modelName',
        '.1.3.6.1.4.1.231.2.10.2.2.10.2.3.1.7.1': 'serialNumber',
        '.1.3.6.1.4.1.231.2.10.2.1.4.0': 'osVersion',
    })

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s", self.name(), device.id)

        manufacturer = 'Fujitsu'
        getdata, tabledata = results
        model = getdata.get('modelName', 'Unknown')
        serialNumber = getdata.get('serialNumber', 'Unknown')
        osVersion = getdata.get('osVersion', 'Unknown')

        hw_om = ObjectMap(compname='hw', data={
            'setProductKey': MultiArgs(model, manufacturer),
            'serialNumber': serialNumber,
        })

        osv = osVersion.lower()
        if 'centos' in osv or 'red hat' in osv or 'ubuntu' in osv or 'linux' in osv:
            manufacturer = 'Linux'
        else:
            manufacturer = 'Unknown'
        
        os_om = ObjectMap(compname='os', data={
            'setProductKey': MultiArgs(osVersion, manufacturer),
        })

        return [hw_om, os_om]