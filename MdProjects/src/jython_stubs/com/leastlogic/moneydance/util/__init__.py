# encoding: utf-8
# module __init__.py
class MdUtil:

    @staticmethod
    def convDateIntToLocal(int=None):
        pass

    @staticmethod
    def convLocalToDateInt(LocalDate=None):
        pass

    @staticmethod
    def convRateToPrice(double=None):
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def getAccounts(AccountBook=None, AccountType1=None):
        pass

    @staticmethod
    def getBalancesAsOfDates(AccountBook=None, Account1=None, int2=None):
        pass

    @staticmethod
    def getCurrentBalance(Account=None):
        pass

    @staticmethod
    def getMsgBundle(String=None, Locale1=None):
        pass

    @staticmethod
    def getSubAccountByInvestNumber(Account=None, String1=None):
        pass

    @staticmethod
    def getSubAccountByName(Account=None, String1=None):
        pass

    @staticmethod
    def loadProps(String=None, Class1=None):
        pass

    @staticmethod
    def roundPrice(double=None):
        pass

    @staticmethod
    def validateCurrentUserRate(CurrencyType=None, CurrencySnapshot1=None):
        pass

class SnapshotList:

    def equals(self, Object=None):
        pass

    def getLatestSnapshot(self, ):
        pass

    def getSecurity(self, ):
        pass

    def getSnapshotForDate(self, int=None):
        pass

