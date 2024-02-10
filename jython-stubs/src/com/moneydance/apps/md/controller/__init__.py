# encoding: utf-8
# module __init__.py
class FeatureModule:
    MONEYBOT_INVOKE_TARGET = None

    def cleanup(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getBuild(self, ):
        pass

    def getDescription(self, ):
        pass

    def getDisplayName(self, ):
        pass

    def getIDStr(self, ):
        pass

    def getIconImage(self, ):
        pass

    def getName(self, ):
        pass

    def getSourceFile(self, ):
        pass

    def getVendor(self, ):
        pass

    def getVendorURL(self, ):
        pass

    def handleEvent(self, String=None):
        pass

    def init(self, ):
        pass

    def invoke(self, String=None):
        pass

    def isBundled(self, ):
        pass

    def toString(self, ):
        pass

    def unload(self, ):
        pass

class FeatureModuleContext:

    def getBuild(self, ):
        pass

    def getCurrentAccountBook(self, ):
        pass

    def getRootAccount(self, ):
        pass

    def getVersion(self, ):
        pass

    def registerAccountEditor(self, FeatureModule=None, int1=None, AccountEditor2=None):
        pass

    def registerFeature(self, FeatureModule=None, String1=None, Image2=None, String3=None):
        pass

    def registerHomePageView(self, FeatureModule=None, HomePageView1=None):
        pass

    def showURL(self, String=None):
        pass

