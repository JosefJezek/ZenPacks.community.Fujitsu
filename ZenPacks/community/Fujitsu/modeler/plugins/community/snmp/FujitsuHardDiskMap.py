__doc__ = """FujitsuHardDiskMap

Gather Fujitsu Hard Disk information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.Fujitsu.Definition import *

class FujitsuHardDiskMap(SnmpPlugin):
    """
    Map Fujitsu Hard Disk table to model.
    """

    compname = 'os'
    constr = Construct(FujitsuHardDiskDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpEntryName = 'svrPhysicalDeviceTable'
    snmpEntryOID = '.1.3.6.1.4.1.231.2.49.1.5.2.1'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.5': 'model', # svrPhysicalDeviceModelName
            '.6': 'manufacturer', # svrPhysicalDeviceVendorName
            '.11': 'interface', # svrPhysicalDeviceInterface
            '.12': 'errors', # svrPhysicalDeviceErrors
            '.13': 'badBlocks', # svrPhysicalDeviceNrBadBlocks
            '.14': 'smartStatus', # svrPhysicalDeviceSmartStatus
            '.16': 'firmware', # svrPhysicalDeviceFirmwareRevision
            '.17': 'serialNumber', # svrPhysicalDeviceSerialNumber
            '.21': 'capacity', # svrPhysicalDeviceCapacityMB
            '.22': 'bay', # svrPhysicalDeviceEnclosureNumber
            '.23': '_svrPhysicalDeviceSlot',
            '.24': 'title', # svrPhysicalDeviceDisplayName
        }),
    )

    interfaceMap = {
        1: 'Other',
        2: 'SCSI',
        3: 'IDE',
        4: 'IEEE1394',
        5: 'SATA',
        6: 'SAS',
        7: 'FC',
    }

    smartStatusMap = {
        1: 'Ok',
        2: 'Failure Predicted',
        3: 'Not Available',
        4: 'Monitoring Disabled',
    }

    def process(self, device, results, log):
        log.info('Modeler %s processing data for device %s', self.name(), device.id)

        getdata, tabledata = results
        maps = []
        rm = self.relMap()

        for snmpindex, row in tabledata.get(self.snmpEntryName, {}).items():
            om = self.objectMap(row)
            om.title = getattr(om, 'title', 'Unknown').replace(' ', '_') or 'Unknown'
            om.id = self.prepId(om.title)
            om.snmpindex = snmpindex
            om.model = getattr(om, 'model', 'Unknown') or 'Unknown'
            om.manufacturer = getattr(om, 'manufacturer', 'Unknown').title() or 'Unknown'
#            om.setProductKey = MultiArgs(om.model, om.manufacturer)
            om.interface = self.interfaceMap.get(getattr(om, 'interface', 1),
                                                    'Unknown (%d)'%om.interface)
            om.smartStatus = self.smartStatusMap.get(getattr(om, 'smartStatus', 3),
                                                    'Unknown (%d)'%om.smartStatus)
            om.capacity = round((float(getattr(om, 'capacity', 0) or 0) * 1048576) / 10**9, 1)
            om.bay = '%s:%s' % (om.bay, om._svrPhysicalDeviceSlot)
            rm.append(om)
            log.debug('om: %s' % om)
        
        maps.append(rm)

        return maps
