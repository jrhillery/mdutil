# encoding: utf-8
# module __init__.py
class AutoCloseable:

    def close(self, ):
        pass

class InterruptedException:

    def addSuppressed(self, Throwable=None):
        pass

    def equals(self, Object=None):
        pass

    def fillInStackTrace(self, ):
        pass

    def getCause(self, ):
        pass

    def getLocalizedMessage(self, ):
        pass

    def getMessage(self, ):
        pass

    def getStackTrace(self, ):
        pass

    def getSuppressed(self, ):
        pass

    def initCause(self, Throwable=None):
        pass

    def printStackTrace(self, PrintStream=None):
        pass

    def setStackTrace(self, StackTraceElement=None):
        pass

    def toString(self, ):
        pass

class Runnable:

    def run(self, ):
        pass

class System:
    err = None
    out = None

    @staticmethod
    def arraycopy(Object=None, int1=None, Object2=None, int3=None, int4=None):
        pass

    @staticmethod
    def clearProperty(String=None):
        pass

    @staticmethod
    def console():
        pass

    @staticmethod
    def currentTimeMillis():
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def exit(int=None):
        pass

    @staticmethod
    def gc():
        pass

    @staticmethod
    def getLogger(String=None, ResourceBundle1=None):
        pass

    @staticmethod
    def getProperties():
        pass

    @staticmethod
    def getProperty(String=None, String1=None):
        pass

    @staticmethod
    def getSecurityManager():
        pass

    @staticmethod
    def getenv(String=None):
        pass

    @staticmethod
    def identityHashCode(Object=None):
        pass

    @staticmethod
    def inheritedChannel():
        pass

    @staticmethod
    def lineSeparator():
        pass

    @staticmethod
    def load(String=None):
        pass

    @staticmethod
    def loadLibrary(String=None):
        pass

    @staticmethod
    def mapLibraryName(String=None):
        pass

    @staticmethod
    def nanoTime():
        pass

    @staticmethod
    def runFinalization():
        pass

    @staticmethod
    def setErr(PrintStream=None):
        pass

    @staticmethod
    def setIn(InputStream=None):
        pass

    @staticmethod
    def setOut(PrintStream=None):
        pass

    @staticmethod
    def setProperties(Properties=None):
        pass

    @staticmethod
    def setProperty(String=None, String1=None):
        pass

    @staticmethod
    def setSecurityManager(SecurityManager=None):
        pass

    def toString(self, ):
        pass

class Thread:
    MAX_PRIORITY = None
    MIN_PRIORITY = None
    NORM_PRIORITY = None

    @staticmethod
    def activeCount():
        pass

    def checkAccess(self, ):
        pass

    def countStackFrames(self, ):
        pass

    @staticmethod
    def currentThread():
        pass

    @staticmethod
    def dumpStack():
        pass

    @staticmethod
    def enumerate(Thread=None):
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def getAllStackTraces():
        pass

    def getContextClassLoader(self, ):
        pass

    @staticmethod
    def getDefaultUncaughtExceptionHandler():
        pass

    def getId(self, ):
        pass

    def getName(self, ):
        pass

    def getPriority(self, ):
        pass

    def getStackTrace(self, ):
        pass

    def getState(self, ):
        pass

    def getThreadGroup(self, ):
        pass

    def getUncaughtExceptionHandler(self, ):
        pass

    @staticmethod
    def holdsLock(Object=None):
        pass

    def interrupt(self, ):
        pass

    @staticmethod
    def interrupted():
        pass

    def isAlive(self, ):
        pass

    def isDaemon(self, ):
        pass

    def isInterrupted(self, ):
        pass

    def isVirtual(self, ):
        pass

    def join(self, long=None, int1=None):
        pass

    @staticmethod
    def ofPlatform():
        pass

    @staticmethod
    def ofVirtual():
        pass

    @staticmethod
    def onSpinWait():
        pass

    def resume(self, ):
        pass

    def run(self, ):
        pass

    def setContextClassLoader(self, ClassLoader=None):
        pass

    def setDaemon(self, boolean=None):
        pass

    @staticmethod
    def setDefaultUncaughtExceptionHandler(UncaughtExceptionHandler=None):
        pass

    def setName(self, String=None):
        pass

    def setPriority(self, int=None):
        pass

    def setUncaughtExceptionHandler(self, UncaughtExceptionHandler=None):
        pass

    @staticmethod
    def sleep(long=None, int1=None):
        pass

    def start(self, ):
        pass

    @staticmethod
    def startVirtualThread(Runnable=None):
        pass

    def stop(self, ):
        pass

    def suspend(self, ):
        pass

    def threadId(self, ):
        pass

    def toString(self, ):
        pass

class Throwable:

    def addSuppressed(self, Throwable=None):
        pass

    def equals(self, Object=None):
        pass

    def fillInStackTrace(self, ):
        pass

    def getCause(self, ):
        pass

    def getLocalizedMessage(self, ):
        pass

    def getMessage(self, ):
        pass

    def getStackTrace(self, ):
        pass

    def getSuppressed(self, ):
        pass

    def initCause(self, Throwable=None):
        pass

    def printStackTrace(self, PrintStream=None):
        pass

    def setStackTrace(self, StackTraceElement=None):
        pass

    def toString(self, ):
        pass

