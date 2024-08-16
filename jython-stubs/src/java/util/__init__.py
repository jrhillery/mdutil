# encoding: utf-8
# module __init__.py
class Map(object):

    class Entry(object):
    
        @staticmethod
        def comparingByKey(Comparator=None):
            pass
    
        @staticmethod
        def comparingByValue(Comparator=None):
            pass
    
        @staticmethod
        def copyOf(Entry=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getKey(self, ):
            pass
    
        def getValue(self, ):
            pass
    
        def setValue(self, Object=None):
            pass

    def clear(self, ):
        pass

    def compute(self, Object=None, BiFunction1=None):
        pass

    def computeIfAbsent(self, Object=None, Function1=None):
        pass

    def computeIfPresent(self, Object=None, BiFunction1=None):
        pass

    def containsKey(self, Object=None):
        pass

    def containsValue(self, Object=None):
        pass

    @staticmethod
    def copyOf(Map=None):
        pass

    @staticmethod
    def entry(Object=None, Object1=None):
        pass

    def entrySet(self, ):
        pass

    def equals(self, Object=None):
        pass

    def forEach(self, BiConsumer=None):
        pass

    def get(self, Object=None):
        pass

    def getOrDefault(self, Object=None, Object1=None):
        pass

    def isEmpty(self, ):
        pass

    def keySet(self, ):
        pass

    def merge(self, Object=None, Object1=None, BiFunction2=None):
        pass

    @staticmethod
    def of(Object=None, Object1=None, Object2=None, Object3=None, Object4=None, Object5=None, Object6=None, Object7=None, Object8=None, Object9=None, Object10=None, Object11=None, Object12=None, Object13=None, Object14=None, Object15=None, Object16=None, Object17=None, Object18=None, Object19=None):
        pass

    @staticmethod
    def ofEntries(Entry=None):
        pass

    def put(self, Object=None, Object1=None):
        pass

    def putAll(self, Map=None):
        pass

    def putIfAbsent(self, Object=None, Object1=None):
        pass

    def remove(self, Object=None, Object1=None):
        pass

    def replace(self, Object=None, Object1=None, Object2=None):
        pass

    def replaceAll(self, BiFunction=None):
        pass

    def size(self, ):
        pass

    def values(self, ):
        pass

