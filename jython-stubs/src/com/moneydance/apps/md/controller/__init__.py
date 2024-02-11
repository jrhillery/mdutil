# encoding: utf-8
# module __init__.py
class FeatureModule:
    MONEYBOT_INVOKE_TARGET = None

    class ActionType:
        ACCOUNT_CONTEXT = None
        MENU = None
        MONEYBOT = None
        OTHER = None
        TXN_CONTEXT = None
    
        class EnumDesc:
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        @staticmethod
        def fromString(String=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    def cleanup(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getBuild(self, ):
        pass

    def getClass(self, ):
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

