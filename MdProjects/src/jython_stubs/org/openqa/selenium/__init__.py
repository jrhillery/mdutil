# encoding: utf-8
# module __init__.py
class By:

    @staticmethod
    def className(String=None):
        pass

    @staticmethod
    def cssSelector(String=None):
        pass

    def equals(self, Object=None):
        pass

    def findElement(self, SearchContext=None):
        pass

    def findElements(self, SearchContext=None):
        pass

    @staticmethod
    def id(String=None):
        pass

    @staticmethod
    def linkText(String=None):
        pass

    @staticmethod
    def name(String=None):
        pass

    @staticmethod
    def partialLinkText(String=None):
        pass

    @staticmethod
    def tagName(String=None):
        pass

    @staticmethod
    def xpath(String=None):
        pass

class WebDriverException:
    DRIVER_INFO = None
    SESSION_ID = None

    def addInfo(self, String=None, String1=None):
        pass

    def addSuppressed(self, Throwable=None):
        pass

    def equals(self, Object=None):
        pass

    def fillInStackTrace(self, ):
        pass

    def getAdditionalInformation(self, ):
        pass

    def getBuildInformation(self, ):
        pass

    def getCause(self, ):
        pass

    @staticmethod
    def getDriverName(StackTraceElement=None):
        pass

    @staticmethod
    def getHostInformation():
        pass

    def getLocalizedMessage(self, ):
        pass

    def getMessage(self, ):
        pass

    def getRawMessage(self, ):
        pass

    def getStackTrace(self, ):
        pass

    def getSupportUrl(self, ):
        pass

    def getSuppressed(self, ):
        pass

    def getSystemInformation(self, ):
        pass

    def initCause(self, Throwable=None):
        pass

    def printStackTrace(self, PrintStream=None):
        pass

    def setStackTrace(self, StackTraceElement=None):
        pass

class WebElement:

    def clear(self, ):
        pass

    def click(self, ):
        pass

    def findElement(self, By=None):
        pass

    def findElements(self, By=None):
        pass

    def getAccessibleName(self, ):
        pass

    def getAriaRole(self, ):
        pass

    def getAttribute(self, String=None):
        pass

    def getCssValue(self, String=None):
        pass

    def getDomAttribute(self, String=None):
        pass

    def getDomProperty(self, String=None):
        pass

    def getLocation(self, ):
        pass

    def getRect(self, ):
        pass

    def getScreenshotAs(self, OutputType=None):
        pass

    def getShadowRoot(self, ):
        pass

    def getSize(self, ):
        pass

    def getTagName(self, ):
        pass

    def getText(self, ):
        pass

    def isDisplayed(self, ):
        pass

    def isEnabled(self, ):
        pass

    def isSelected(self, ):
        pass

    def sendKeys(self, CharSequence=None):
        pass

    def submit(self, ):
        pass

