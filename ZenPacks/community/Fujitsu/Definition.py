from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "Fujitsu"
VERSION = Version(1, 0, 0)

def getMapValue(ob, datapoint, map):
    '''Attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'Unknown'
    
def getValue(ob, datapoint):
    '''Attempt to get RRD value'''
    try:
        return int(ob.getRRDValue(datapoint))
    except:
        return 'Unknown'


def getDiskStatus(ob): return ob.getMapValue('diskStatus_diskStatus', ob.diskStatusMap)

diskStatusMap = {
    1: 'Unknown',
    2: 'No Disk',
    3: 'Available - unconfigured',
    4: 'Operational',
    5: 'Failed',
    6: 'Rebuilding',
    7: 'Global Hot Spare - for use in any array',
    8: 'Dedicated Hot Spare - for use in a dedicated array',
    9: 'Offline',
    10: 'Unconfigured Failed',
    11: 'Failed Missing',
    12: 'Copy Back',
    13: 'Redundant Copy',
    14: 'Waiting for copyback to start',
    15: 'Preparing to start up',
    16: 'Migrating',
    17: 'Jbod - exposed to operating system',
    18: 'Shielded - under diagnostic test',
    19: 'Clearing',
    20: 'Erasing',
}

DATA = {
    'version': VERSION,
    'zenpackbase': BASE,
    'component': 'FujitsuHardDisk',
    'componentData': {
        'singular': 'Hard Disk',
        'plural': 'Hard Disks',
        'properties': {
            'badBlocks': addProperty('Bad Blocks', optional=False),
            'bay': addProperty('Bay'),
            'capacity': addProperty('Capacity GB', optional=False),
            'errors': addProperty('Errors All', optional=False),
            'firmware': addProperty('Firmware'),
            'interface': addProperty('Interface'),
            'manufacturer': addProperty('Manufacturer'),
            'model': addProperty('Model'),
            'serialNumber': addProperty('Serial #'),
            'smartStatus': addProperty('SMART Status', optional=False),
            'getDiskStatus': getReferredMethod('Disk Status', 'getDiskStatus'),
            'alias': addProperty('Alias (offline)'),
            'cache': addProperty('Cache (offline)'),
            'formFactor': addProperty('Form Factor (offline)', default='3.5"'),
            'rpm': addProperty('RPM (offline)'),
            'storageType': addProperty('Storage Type (offline)', default='HDD'),
            'description': addProperty('Description (offline)'),
            'date': addProperty('Date of Purchase (offline)'),
            'eventClass': getEventClass('/Status/HardDisk'),
        },
    },
    'componentAttributes': {'diskStatusMap': diskStatusMap },
    'componentMethods': [getMapValue, getDiskStatus],
}

FujitsuHardDiskDefinition = type('FujitsuHardDiskDefinition', (BasicDefinition,), DATA)


def getRaidStatus(ob): return ob.getMapValue('raidStatus_raidStatus', ob.raidStatusMap)

raidStatusMap = {
    1: 'Unknown',
    2: 'Operational',
    3: 'Partially Degraded - reduced redundancy still available',
    4: 'Degraded - redundancy lost',
    5: 'Failed - too many disks failed',
    6: 'Rebuilding',
    7: 'Checking',
    8: 'Mdcing - fixes inconsistencies',
    9: 'Initializing',
    10: 'Background Initializing',
    11: 'Migrating',
    12: 'Copying - copyback or redundant copy',
    13: 'Offline',
    14: 'Hot Spare In Use',
    15: 'Erasing',
}

DATA = {
    'version': VERSION,
    'zenpackbase': BASE,
    'component': 'FujitsuLogicalDisk',
    'componentData': {
        'singular': 'Logical Disk',
        'plural': 'Logical Disks',
        'properties': {
            'arraySize': addProperty('Array Size GB', optional=False),
            'cacheMode': addProperty('Cache Mode', optional=False),
            'osName': addProperty('OS Name', optional=False),
            'raidLevel': addProperty('RAID Level', optional=False),
            'readMode': addProperty('Read Mode'),
            'stripeSize': addProperty('Stripe Size KB'),
            'totalSize': addProperty('Total Size GB'),
            'getRaidStatus': getReferredMethod('RAID Status', 'getRaidStatus'),
            'alias': addProperty('Alias (offline)'),
            'description': addProperty('Description (offline)'),
            'eventClass': getEventClass('/Status/RAID'),
        },
    },
    'componentAttributes': {'raidStatusMap': raidStatusMap },
    'componentMethods': [getMapValue, getRaidStatus],
}

FujitsuLogicalDiskDefinition = type('FujitsuLogicalDiskDefinition', (BasicDefinition,), DATA)