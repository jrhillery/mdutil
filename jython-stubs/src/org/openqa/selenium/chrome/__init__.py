# encoding: utf-8
# module __init__.py
class ChromeDriver:
    IS_CHROMIUM_BROWSER = None

    class When:
        AFTER = None
        BEFORE = None
        EXCEPTION = None
    
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

    def addVirtualAuthenticator(self, VirtualAuthenticatorOptions=None):
        pass

    @staticmethod
    def builder():
        pass

    def close(self, ):
        pass

    def deleteDownloadableFiles(self, ):
        pass

    def deleteNetworkConditions(self, ):
        pass

    def downloadFile(self, String=None, Path1=None):
        pass

    def equals(self, Object=None):
        pass

    def executeAsyncScript(self, String=None, Object1=None):
        pass

    def executeCdpCommand(self, String=None, Map1=None):
        pass

    def executeScript(self, ScriptKey=None, Object1=None):
        pass

    def findElement(self, By=None):
        pass

    def findElements(self, SearchContext=None, BiFunction1=None, By2=None):
        pass

    def get(self, String=None):
        pass

    def getBiDi(self, ):
        pass

    def getCapabilities(self, ):
        pass

    def getCastIssueMessage(self, ):
        pass

    def getCastSinks(self, ):
        pass

    def getCommandExecutor(self, ):
        pass

    def getCurrentUrl(self, ):
        pass

    def getDevTools(self, ):
        pass

    def getDownloadableFiles(self, ):
        pass

    def getErrorHandler(self, ):
        pass

    def getFederatedCredentialManagementDialog(self, ):
        pass

    def getFileDetector(self, ):
        pass

    def getLocalStorage(self, ):
        pass

    def getNetworkConditions(self, ):
        pass

    def getNetworkConnection(self, ):
        pass

    def getPageSource(self, ):
        pass

    def getPinnedScripts(self, ):
        pass

    def getScreenshotAs(self, OutputType=None):
        pass

    def getSessionId(self, ):
        pass

    def getSessionStorage(self, ):
        pass

    def getTitle(self, ):
        pass

    def getWindowHandle(self, ):
        pass

    def getWindowHandles(self, ):
        pass

    def launchApp(self, String=None):
        pass

    def location(self, ):
        pass

    def manage(self, ):
        pass

    def maybeGetBiDi(self, ):
        pass

    def maybeGetDevTools(self, ):
        pass

    def navigate(self, ):
        pass

    def onLogEvent(self, EventType=None):
        pass

    def perform(self, Collection=None):
        pass

    def pin(self, String=None):
        pass

    def quit(self, ):
        pass

    def register(self, Predicate=None, Supplier1=None):
        pass

    def removeVirtualAuthenticator(self, VirtualAuthenticator=None):
        pass

    def requireDownloadsEnabled(self, Capabilities=None):
        pass

    def resetCooldown(self, ):
        pass

    def resetInputState(self, ):
        pass

    def selectCastSink(self, String=None):
        pass

    def setDelayEnabled(self, boolean=None):
        pass

    def setErrorHandler(self, ErrorHandler=None):
        pass

    def setFileDetector(self, FileDetector=None):
        pass

    def setLocation(self, Location=None):
        pass

    def setLogLevel(self, Level=None):
        pass

    def setNetworkConditions(self, ChromiumNetworkConditions=None):
        pass

    def setNetworkConnection(self, ConnectionType=None):
        pass

    def setPermission(self, String=None, String1=None):
        pass

    def startDesktopMirroring(self, String=None):
        pass

    def startTabMirroring(self, String=None):
        pass

    def stopCasting(self, String=None):
        pass

    def switchTo(self, ):
        pass

    def toString(self, ):
        pass

    def unpin(self, ScriptKey=None):
        pass

class ChromeDriverService:
    CHROME_DRIVER_ALLOWED_IPS_PROPERTY = None
    CHROME_DRIVER_APPEND_LOG_PROPERTY = None
    CHROME_DRIVER_DISABLE_BUILD_CHECK = None
    CHROME_DRIVER_EXE_PROPERTY = None
    CHROME_DRIVER_LOG_LEVEL_PROPERTY = None
    CHROME_DRIVER_LOG_PROPERTY = None
    CHROME_DRIVER_NAME = None
    CHROME_DRIVER_READABLE_TIMESTAMP = None
    CHROME_DRIVER_SILENT_OUTPUT_PROPERTY = None
    CHROME_DRIVER_VERBOSE_LOG_PROPERTY = None
    LOG_NULL = None
    LOG_STDERR = None
    LOG_STDOUT = None

    class Builder:
    
        def build(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def score(self, Capabilities=None):
            pass
    
        def toString(self, ):
            pass
    
        def usingAnyFreePort(self, ):
            pass
    
        def usingDriverExecutable(self, File=None):
            pass
    
        def usingPort(self, int=None):
            pass
    
        def withAllowedListIps(self, String=None):
            pass
    
        def withAppendLog(self, boolean=None):
            pass
    
        def withBuildCheckDisabled(self, boolean=None):
            pass
    
        def withEnvironment(self, Map=None):
            pass
    
        def withLogFile(self, File=None):
            pass
    
        def withLogLevel(self, ChromiumDriverLogLevel=None):
            pass
    
        def withLogOutput(self, OutputStream=None):
            pass
    
        def withReadableTimestamp(self, Boolean=None):
            pass
    
        def withSilent(self, boolean=None):
            pass
    
        def withTimeout(self, Duration=None):
            pass
    
        def withVerbose(self, boolean=None):
            pass

    class Builder:
    
        def build(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def score(self, Capabilities=None):
            pass
    
        def toString(self, ):
            pass
    
        def usingAnyFreePort(self, ):
            pass
    
        def usingDriverExecutable(self, File=None):
            pass
    
        def usingPort(self, int=None):
            pass
    
        def withEnvironment(self, Map=None):
            pass
    
        def withLogFile(self, File=None):
            pass
    
        def withLogOutput(self, OutputStream=None):
            pass
    
        def withTimeout(self, Duration=None):
            pass

    def close(self, ):
        pass

    @staticmethod
    def createDefaultService():
        pass

    def equals(self, Object=None):
        pass

    def getDefaultDriverOptions(self, ):
        pass

    def getDriverName(self, ):
        pass

    def getDriverProperty(self, ):
        pass

    def getExecutable(self, ):
        pass

    def getUrl(self, ):
        pass

    def isRunning(self, ):
        pass

    def sendOutputTo(self, OutputStream=None):
        pass

    def setExecutable(self, String=None):
        pass

    def start(self, ):
        pass

    def stop(self, ):
        pass

    def toString(self, ):
        pass

class ChromeOptions:
    CAPABILITY = None
    LOGGING_PREFS = None

    def addArguments(self, String=None):
        pass

    def addEncodedExtensions(self, String=None):
        pass

    def addExtensions(self, File=None):
        pass

    def asMap(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getBrowserName(self, ):
        pass

    def getBrowserVersion(self, ):
        pass

    def getCapability(self, String=None):
        pass

    def getCapabilityNames(self, ):
        pass

    def getPlatformName(self, ):
        pass

    def merge(self, Capabilities=None):
        pass

    def setAcceptInsecureCerts(self, boolean=None):
        pass

    def setAndroidActivity(self, String=None):
        pass

    def setAndroidDeviceSerialNumber(self, String=None):
        pass

    def setAndroidPackage(self, String=None):
        pass

    def setAndroidProcess(self, String=None):
        pass

    def setBinary(self, File=None):
        pass

    def setBrowserVersion(self, String=None):
        pass

    def setCapability(self, String=None, boolean1=None):
        pass

    def setEnableDownloads(self, boolean=None):
        pass

    def setExperimentalOption(self, String=None, Object1=None):
        pass

    def setImplicitWaitTimeout(self, Duration=None):
        pass

    def setPageLoadStrategy(self, PageLoadStrategy=None):
        pass

    def setPageLoadTimeout(self, Duration=None):
        pass

    def setPlatformName(self, String=None):
        pass

    def setProxy(self, Proxy=None):
        pass

    def setScriptTimeout(self, Duration=None):
        pass

    def setStrictFileInteractability(self, boolean=None):
        pass

    def setUnhandledPromptBehaviour(self, UnexpectedAlertBehaviour=None):
        pass

    def setUseRunningAndroidApp(self, boolean=None):
        pass

    def toJson(self, ):
        pass

    def toString(self, ):
        pass

