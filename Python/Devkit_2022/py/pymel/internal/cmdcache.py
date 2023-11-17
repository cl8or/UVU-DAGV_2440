if False:
    from typing import Dict, List, Tuple, Union, Optional

from . import startup

class CmdCache(startup.SubItemCache):
    def build(self): pass
    def fromRawData(self, data): pass
    def rebuild(self):
        """
        Build and save to disk the list of Maya Python commands and their arguments
        
        WARNING: will unload existing plugins, then (re)load all maya-installed
        plugins, without making an attempt to return the loaded plugins to the
        state they were at before this command is run.  Also, the act of
        loading all the plugins may crash maya, especially if done from a
        non-GUI session
        """
        pass
    def toRawData(self, data): pass
    DESC = 'the list of Maya commands'
    
    
    ITEM_TYPES = {}
    
    
    NAME = 'mayaCmdsList'


class CmdExamplesCache(startup.PymelCache):
    DESC = 'the list of Maya command examples'
    
    
    NAME = 'mayaCmdsExamples'
    
    
    USE_VERSION = True


class CmdDocsCache(startup.PymelCache):
    DESC = 'the Maya command documentation'
    
    
    NAME = 'mayaCmdsDocs'


class CmdProcessedExamplesCache(CmdExamplesCache):
    USE_VERSION = False




def getCmdInfoBasic(command): pass
def cmdArgMakers(force='False'): pass
def getCmdInfo(command, version, python='True'):
    """
    Since many maya Python commands are builtins we can't get use getargspec on them.
    besides most use keyword args that we need the precise meaning of ( if they can be be used with
    edit or query flags, the shortnames of flags, etc) so we have to parse the maya docs
    """
    pass
def getModule(funcName, knownModuleCmds): pass
def nodeCreationCmd(func, nodeType): pass
def getCallbackFlags(cmdInfo):
    """
    used parsed data and naming convention to determine which flags are callbacks
    """
    pass
def _getNodeHierarchy(version='None'):
    """
    get node hierarchy as a list of 3-value tuples:
        ( nodeType, parents, children )
    """
    pass
def testNodeCmd(funcName, cmdInfo, nodeCmd='False', verbose='False'): pass
def fixCodeExamples(style="'maya'", force='False'):
    """
    cycle through all examples from the maya docs, replacing maya.cmds with pymel and inserting pymel output.
    
    NOTE: this can only be run from gui mode
    WARNING: back up your preferences before running
    
    TODO: auto backup and restore of maya prefs
    """
    pass
def getModuleCommandList(category, version='None'): pass


cmdlistOverrides = {}

nodeTypeToNodeCommand = {}

secondaryFlags = {}

_logger = None

UI_COMMANDS = []

moduleCommandAdditions = {}

_cmdArgMakers = {}

moduleNameShortToLong = {}


