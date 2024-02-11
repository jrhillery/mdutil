# encoding: utf-8
# module __init__.py
class ActionEvent:
    ACTION_EVENT_MASK = None
    ACTION_FIRST = None
    ACTION_LAST = None
    ACTION_PERFORMED = None
    ADJUSTMENT_EVENT_MASK = None
    ALT_MASK = None
    COMPONENT_EVENT_MASK = None
    CONTAINER_EVENT_MASK = None
    CTRL_MASK = None
    FOCUS_EVENT_MASK = None
    HIERARCHY_BOUNDS_EVENT_MASK = None
    HIERARCHY_EVENT_MASK = None
    INPUT_METHOD_EVENT_MASK = None
    INVOCATION_EVENT_MASK = None
    ITEM_EVENT_MASK = None
    KEY_EVENT_MASK = None
    META_MASK = None
    MOUSE_EVENT_MASK = None
    MOUSE_MOTION_EVENT_MASK = None
    MOUSE_WHEEL_EVENT_MASK = None
    PAINT_EVENT_MASK = None
    RESERVED_ID_MAX = None
    SHIFT_MASK = None
    TEXT_EVENT_MASK = None
    WINDOW_EVENT_MASK = None
    WINDOW_FOCUS_EVENT_MASK = None
    WINDOW_STATE_EVENT_MASK = None

    def equals(self, Object=None):
        pass

    def getActionCommand(self, ):
        pass

    def getClass(self, ):
        pass

    def getID(self, ):
        pass

    def getModifiers(self, ):
        pass

    def getSource(self, ):
        pass

    def getWhen(self, ):
        pass

    def paramString(self, ):
        pass

    def setSource(self, Object=None):
        pass

    def toString(self, ):
        pass

class WindowEvent:
    ACTION_EVENT_MASK = None
    ADJUSTMENT_EVENT_MASK = None
    COMPONENT_EVENT_MASK = None
    COMPONENT_FIRST = None
    COMPONENT_HIDDEN = None
    COMPONENT_LAST = None
    COMPONENT_MOVED = None
    COMPONENT_RESIZED = None
    COMPONENT_SHOWN = None
    CONTAINER_EVENT_MASK = None
    FOCUS_EVENT_MASK = None
    HIERARCHY_BOUNDS_EVENT_MASK = None
    HIERARCHY_EVENT_MASK = None
    INPUT_METHOD_EVENT_MASK = None
    INVOCATION_EVENT_MASK = None
    ITEM_EVENT_MASK = None
    KEY_EVENT_MASK = None
    MOUSE_EVENT_MASK = None
    MOUSE_MOTION_EVENT_MASK = None
    MOUSE_WHEEL_EVENT_MASK = None
    PAINT_EVENT_MASK = None
    RESERVED_ID_MAX = None
    TEXT_EVENT_MASK = None
    WINDOW_ACTIVATED = None
    WINDOW_CLOSED = None
    WINDOW_CLOSING = None
    WINDOW_DEACTIVATED = None
    WINDOW_DEICONIFIED = None
    WINDOW_EVENT_MASK = None
    WINDOW_FIRST = None
    WINDOW_FOCUS_EVENT_MASK = None
    WINDOW_GAINED_FOCUS = None
    WINDOW_ICONIFIED = None
    WINDOW_LAST = None
    WINDOW_LOST_FOCUS = None
    WINDOW_OPENED = None
    WINDOW_STATE_CHANGED = None
    WINDOW_STATE_EVENT_MASK = None

    def equals(self, Object=None):
        pass

    def getClass(self, ):
        pass

    def getComponent(self, ):
        pass

    def getID(self, ):
        pass

    def getNewState(self, ):
        pass

    def getOldState(self, ):
        pass

    def getOppositeWindow(self, ):
        pass

    def getSource(self, ):
        pass

    def getWindow(self, ):
        pass

    def paramString(self, ):
        pass

    def setSource(self, Object=None):
        pass

    def toString(self, ):
        pass

