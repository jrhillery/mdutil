# encoding: utf-8
# module __init__.py
class AutoCloseable:

    def close(self, ):
        pass

class InterruptedException(Exception):

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

    class Logger:
    
        class Level:
            ALL = None
            DEBUG = None
            ERROR = None
            INFO = None
            OFF = None
            TRACE = None
            WARNING = None
        
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
        
            def getName(self, ):
                pass
        
            def getSeverity(self, ):
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
    
        def getName(self, ):
            pass
    
        def isLoggable(self, Level=None):
            pass
    
        def log(self, Level=None, ResourceBundle1=None, String2=None, Object3=None):
            pass

    class LoggerFinder:
    
        def equals(self, Object=None):
            pass
    
        def getLocalizedLogger(self, String=None, ResourceBundle1=None, Module2=None):
            pass
    
        def getLogger(self, String=None, Module1=None):
            pass
    
        @staticmethod
        def getLoggerFinder():
            pass
    
        def toString(self, ):
            pass

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

    class Builder:
    
        class OfPlatform:
        
            def daemon(self, boolean=None):
                pass
        
            def factory(self, ):
                pass
        
            def group(self, ThreadGroup=None):
                pass
        
            def inheritInheritableThreadLocals(self, boolean=None):
                pass
        
            def name(self, String=None, long1=None):
                pass
        
            def priority(self, int=None):
                pass
        
            def stackSize(self, long=None):
                pass
        
            def start(self, Runnable=None):
                pass
        
            def uncaughtExceptionHandler(self, UncaughtExceptionHandler=None):
                pass
        
            def unstarted(self, Runnable=None):
                pass
    
        class OfVirtual:
        
            def factory(self, ):
                pass
        
            def inheritInheritableThreadLocals(self, boolean=None):
                pass
        
            def name(self, String=None, long1=None):
                pass
        
            def start(self, Runnable=None):
                pass
        
            def uncaughtExceptionHandler(self, UncaughtExceptionHandler=None):
                pass
        
            def unstarted(self, Runnable=None):
                pass
    
        def factory(self, ):
            pass
    
        def inheritInheritableThreadLocals(self, boolean=None):
            pass
    
        def name(self, String=None, long1=None):
            pass
    
        def start(self, Runnable=None):
            pass
    
        def uncaughtExceptionHandler(self, UncaughtExceptionHandler=None):
            pass
    
        def unstarted(self, Runnable=None):
            pass

    class State:
        BLOCKED = None
        NEW = None
        RUNNABLE = None
        TERMINATED = None
        TIMED_WAITING = None
        WAITING = None
    
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

    class UncaughtExceptionHandler:
    
        def uncaughtException(self, Thread=None, Throwable1=None):
            pass

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

class Throwable(Exception):

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

