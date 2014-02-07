__doc__ = """FujitsuLogicalDiskMap

Gather Fujitsu RAID information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.Fujitsu.Definition import *

class FujitsuLogicalDiskMap(SnmpPlugin):
    """
    Map Fujitsu RAID table to model.
    """

    compname = 'os'
    constr = Construct(FujitsuLogicalDiskDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpEntryName = 'svrLogicalDriveTable'
    snmpEntryOID = '.1.3.6.1.4.1.231.2.49.1.6.2.1'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.3': 'arraySize', # svrLogicalDriveArraySize
            '.4': 'totalSize', # svrLogicalDriveTotalSize
            '.6': 'raidLevel', # svrLogicalDriveRaidLevelStr
            '.7': 'stripeSize', # svrLogicalDriveStripeSize
            '.14': 'osName', # svrLogicalDriveOSDeviceName
            '.15': 'readMode', # svrLogicalDriveReadMode
            '.17': 'cacheMode', # svrLogicalDriveDiskCacheMode
            '.20': 'title', # svrLogicalDriveDisplayName
        }),
    )

    readModeMap = {
        1: 'Unknown',
        2: 'Read Ahead',
        3: 'No Read Ahead',
        4: 'Adaptive',
    }

    cacheModeMap = {
        1: 'Unknown',
        2: 'Enabled',
        3: 'Disabled',
        4: 'Unchanged',
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
            om.stripeSize = om.stripeSize / 1024
            om.readMode = self.readModeMap.get(getattr(om, 'readMode', 1),
                                                    'Unknown (%d)'%om.readMode)
            om.cacheMode = self.cacheModeMap.get(getattr(om, 'cacheMode', 1),
                                                    'Unknown (%d)'%om.cacheMode)
            om.snmpindex = snmpindex
            rm.append(om)
            log.debug('om: %s' % om)
        
        maps.append(rm)

        return maps
