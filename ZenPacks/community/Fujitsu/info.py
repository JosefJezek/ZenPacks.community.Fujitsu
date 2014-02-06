from ZenPacks.community.ConstructionKit.ClassHelper import *

def FujitsuLogicalDiskgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class FujitsuLogicalDiskInfo(ClassHelper.FujitsuLogicalDiskInfo):
    ''''''

def FujitsuHardDiskgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class FujitsuHardDiskInfo(ClassHelper.FujitsuHardDiskInfo):
    ''''''


