# encoding: utf-8
# module __init__.py
class ExpectedConditions(object):
    # source:jar:file:/~/Documents/Prog/selenium-java-4.23.0/selenium-support-4.23.0.jar!/org/openqa/selenium/support/ui/ExpectedConditions.class

    @staticmethod
    def alertIsPresent():
        pass

    @staticmethod
    def attributeContains(By=None, String1=None, String2=None):
        pass

    @staticmethod
    def attributeToBe(By=None, String1=None, String2=None):
        pass

    @staticmethod
    def attributeToBeNotEmpty(WebElement=None, String1=None):
        pass

    @staticmethod
    def domAttributeToBe(WebElement=None, String1=None, String2=None):
        pass

    @staticmethod
    def domPropertyToBe(WebElement=None, String1=None, String2=None):
        pass

    @staticmethod
    def elementSelectionStateToBe(By=None, boolean1=None):
        pass

    @staticmethod
    def elementToBeClickable(By=None):
        pass

    @staticmethod
    def elementToBeSelected(By=None):
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def frameToBeAvailableAndSwitchToIt(int=None):
        pass

    def getClass(self, ):
        pass

    @staticmethod
    def invisibilityOf(WebElement=None):
        pass

    @staticmethod
    def invisibilityOfAllElements(List=None):
        pass

    @staticmethod
    def invisibilityOfElementLocated(By=None):
        pass

    @staticmethod
    def invisibilityOfElementWithText(By=None, String1=None):
        pass

    @staticmethod
    def javaScriptThrowsNoExceptions(String=None):
        pass

    @staticmethod
    def jsReturnsValue(String=None):
        pass

    @staticmethod
    def numberOfElementsToBe(By=None, Integer1=None):
        pass

    @staticmethod
    def numberOfElementsToBeLessThan(By=None, Integer1=None):
        pass

    @staticmethod
    def numberOfElementsToBeMoreThan(By=None, Integer1=None):
        pass

    @staticmethod
    def numberOfWindowsToBe(int=None):
        pass

    @staticmethod
    def presenceOfAllElementsLocatedBy(By=None):
        pass

    @staticmethod
    def presenceOfElementLocated(By=None):
        pass

    @staticmethod
    def presenceOfNestedElementLocatedBy(By=None, By1=None):
        pass

    @staticmethod
    def presenceOfNestedElementsLocatedBy(By=None, By1=None):
        pass

    @staticmethod
    def refreshed(ExpectedCondition=None):
        pass

    @staticmethod
    def stalenessOf(WebElement=None):
        pass

    @staticmethod
    def textMatches(By=None, Pattern1=None):
        pass

    @staticmethod
    def textToBe(By=None, String1=None):
        pass

    @staticmethod
    def textToBePresentInElement(WebElement=None, String1=None):
        pass

    @staticmethod
    def textToBePresentInElementLocated(By=None, String1=None):
        pass

    @staticmethod
    def textToBePresentInElementValue(By=None, String1=None):
        pass

    @staticmethod
    def titleContains(String=None):
        pass

    @staticmethod
    def titleIs(String=None):
        pass

    def toString(self, ):
        pass

    @staticmethod
    def urlContains(String=None):
        pass

    @staticmethod
    def urlMatches(String=None):
        pass

    @staticmethod
    def urlToBe(String=None):
        pass

    @staticmethod
    def visibilityOf(WebElement=None):
        pass

    @staticmethod
    def visibilityOfAllElements(List=None):
        pass

    @staticmethod
    def visibilityOfAllElementsLocatedBy(By=None):
        pass

    @staticmethod
    def visibilityOfElementLocated(By=None):
        pass

    @staticmethod
    def visibilityOfNestedElementsLocatedBy(By=None, By1=None):
        pass

class WebDriverWait(object):
    # source:jar:file:/~/Documents/Prog/selenium-java-4.23.0/selenium-support-4.23.0.jar!/org/openqa/selenium/support/ui/WebDriverWait.class

    def equals(self, Object=None):
        pass

    def getClass(self, ):
        pass

    def ignoreAll(self, Collection=None):
        pass

    def ignoring(self, Class=None, Class1=None):
        pass

    def pollingEvery(self, Duration=None):
        pass

    def toString(self, ):
        pass

    def until(self, Function=None):
        pass

    def withMessage(self, String=None):
        pass

    def withTimeout(self, Duration=None):
        pass

