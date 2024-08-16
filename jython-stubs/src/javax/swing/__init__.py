# encoding: utf-8
# module __init__.py
class GroupLayout(object):
    DEFAULT_SIZE = None
    PREFERRED_SIZE = None

    class Alignment(object):
        BASELINE = None
        CENTER = None
        LEADING = None
        TRAILING = None
    
        class EnumDesc(object):
        
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

    class Group(object):
    
        def addComponent(self, Component=None, int1=None, int2=None, int3=None):
            pass
    
        def addGap(self, int=None, int1=None, int2=None):
            pass
    
        def addGroup(self, Group=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def toString(self, ):
            pass

    class ParallelGroup(object):
    
        def addComponent(self, Component=None, Alignment1=None, int2=None, int3=None, int4=None):
            pass
    
        def addGap(self, int=None, int1=None, int2=None):
            pass
    
        def addGroup(self, Alignment=None, Group1=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def toString(self, ):
            pass

    class SequentialGroup(object):
    
        def addComponent(self, boolean=None, Component1=None, int2=None, int3=None, int4=None):
            pass
    
        def addContainerGap(self, int=None, int1=None):
            pass
    
        def addGap(self, int=None, int1=None, int2=None):
            pass
    
        def addGroup(self, boolean=None, Group1=None):
            pass
    
        def addPreferredGap(self, JComponent=None, JComponent1=None, ComponentPlacement2=None, int3=None, int4=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def toString(self, ):
            pass

    def __init__(self, Container=None):
        pass

    def addLayoutComponent(self, Component=None, Object1=None):
        pass

    def createBaselineGroup(self, boolean=None, boolean1=None):
        pass

    def createParallelGroup(self, Alignment=None, boolean1=None):
        pass

    def createSequentialGroup(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getAutoCreateContainerGaps(self, ):
        pass

    def getAutoCreateGaps(self, ):
        pass

    def getClass(self, ):
        pass

    def getHonorsVisibility(self, ):
        pass

    def getLayoutAlignmentX(self, Container=None):
        pass

    def getLayoutAlignmentY(self, Container=None):
        pass

    def getLayoutStyle(self, ):
        pass

    def invalidateLayout(self, Container=None):
        pass

    def layoutContainer(self, Container=None):
        pass

    def linkSize(self, int=None, Component1=None):
        pass

    def maximumLayoutSize(self, Container=None):
        pass

    def minimumLayoutSize(self, Container=None):
        pass

    def preferredLayoutSize(self, Container=None):
        pass

    def removeLayoutComponent(self, Component=None):
        pass

    def replace(self, Component=None, Component1=None):
        pass

    def setAutoCreateContainerGaps(self, boolean=None):
        pass

    def setAutoCreateGaps(self, boolean=None):
        pass

    def setHonorsVisibility(self, Component=None, Boolean1=None):
        pass

    def setHorizontalGroup(self, Group=None):
        pass

    def setLayoutStyle(self, LayoutStyle=None):
        pass

    def setVerticalGroup(self, Group=None):
        pass

    def toString(self, ):
        pass

class JButton(object):
    ABORT = None
    ALLBITS = None
    BORDER_PAINTED_CHANGED_PROPERTY = None
    BOTTOM = None
    BOTTOM_ALIGNMENT = None
    CENTER = None
    CENTER_ALIGNMENT = None
    CONTENT_AREA_FILLED_CHANGED_PROPERTY = None
    DISABLED_ICON_CHANGED_PROPERTY = None
    DISABLED_SELECTED_ICON_CHANGED_PROPERTY = None
    EAST = None
    ERROR = None
    FOCUS_PAINTED_CHANGED_PROPERTY = None
    FRAMEBITS = None
    HEIGHT = None
    HORIZONTAL = None
    HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY = None
    HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY = None
    ICON_CHANGED_PROPERTY = None
    LEADING = None
    LEFT = None
    LEFT_ALIGNMENT = None
    MARGIN_CHANGED_PROPERTY = None
    MNEMONIC_CHANGED_PROPERTY = None
    MODEL_CHANGED_PROPERTY = None
    NEXT = None
    NORTH = None
    NORTH_EAST = None
    NORTH_WEST = None
    PRESSED_ICON_CHANGED_PROPERTY = None
    PREVIOUS = None
    PROPERTIES = None
    RIGHT = None
    RIGHT_ALIGNMENT = None
    ROLLOVER_ENABLED_CHANGED_PROPERTY = None
    ROLLOVER_ICON_CHANGED_PROPERTY = None
    ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY = None
    SELECTED_ICON_CHANGED_PROPERTY = None
    SOMEBITS = None
    SOUTH = None
    SOUTH_EAST = None
    SOUTH_WEST = None
    TEXT_CHANGED_PROPERTY = None
    TOOL_TIP_TEXT_KEY = None
    TOP = None
    TOP_ALIGNMENT = None
    TRAILING = None
    UNDEFINED_CONDITION = None
    VERTICAL = None
    VERTICAL_ALIGNMENT_CHANGED_PROPERTY = None
    VERTICAL_TEXT_POSITION_CHANGED_PROPERTY = None
    WEST = None
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT = None
    WHEN_FOCUSED = None
    WHEN_IN_FOCUSED_WINDOW = None
    WIDTH = None

    class AccessibleJComponent(object):
        ACCESSIBLE_ACTION_PROPERTY = None
        ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY = None
        ACCESSIBLE_CARET_PROPERTY = None
        ACCESSIBLE_CHILD_PROPERTY = None
        ACCESSIBLE_COMPONENT_BOUNDS_CHANGED = None
        ACCESSIBLE_DESCRIPTION_PROPERTY = None
        ACCESSIBLE_HYPERTEXT_OFFSET = None
        ACCESSIBLE_INVALIDATE_CHILDREN = None
        ACCESSIBLE_NAME_PROPERTY = None
        ACCESSIBLE_SELECTION_PROPERTY = None
        ACCESSIBLE_STATE_PROPERTY = None
        ACCESSIBLE_TABLE_CAPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_MODEL_CHANGED = None
        ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_ROW_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_SUMMARY_CHANGED = None
        ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED = None
        ACCESSIBLE_TEXT_PROPERTY = None
        ACCESSIBLE_VALUE_PROPERTY = None
        ACCESSIBLE_VISIBLE_DATA_PROPERTY = None
    
        def addFocusListener(self, FocusListener=None):
            pass
    
        def addPropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def contains(self, Point=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def firePropertyChange(self, String=None, Object1=None, Object2=None):
            pass
    
        def getAccessibleAction(self, ):
            pass
    
        def getAccessibleAt(self, Point=None):
            pass
    
        def getAccessibleChild(self, int=None):
            pass
    
        def getAccessibleChildrenCount(self, ):
            pass
    
        def getAccessibleComponent(self, ):
            pass
    
        def getAccessibleDescription(self, ):
            pass
    
        def getAccessibleEditableText(self, ):
            pass
    
        def getAccessibleIcon(self, ):
            pass
    
        def getAccessibleIndexInParent(self, ):
            pass
    
        def getAccessibleKeyBinding(self, ):
            pass
    
        def getAccessibleName(self, ):
            pass
    
        def getAccessibleParent(self, ):
            pass
    
        def getAccessibleRelationSet(self, ):
            pass
    
        def getAccessibleRole(self, ):
            pass
    
        def getAccessibleSelection(self, ):
            pass
    
        def getAccessibleStateSet(self, ):
            pass
    
        def getAccessibleTable(self, ):
            pass
    
        def getAccessibleText(self, ):
            pass
    
        def getAccessibleValue(self, ):
            pass
    
        def getBackground(self, ):
            pass
    
        def getBounds(self, ):
            pass
    
        def getClass(self, ):
            pass
    
        def getCursor(self, ):
            pass
    
        def getFont(self, ):
            pass
    
        def getFontMetrics(self, Font=None):
            pass
    
        def getForeground(self, ):
            pass
    
        def getLocale(self, ):
            pass
    
        def getLocation(self, ):
            pass
    
        def getLocationOnScreen(self, ):
            pass
    
        def getSize(self, ):
            pass
    
        def getTitledBorderText(self, ):
            pass
    
        def getToolTipText(self, ):
            pass
    
        def isEnabled(self, ):
            pass
    
        def isFocusTraversable(self, ):
            pass
    
        def isShowing(self, ):
            pass
    
        def isVisible(self, ):
            pass
    
        def removeFocusListener(self, FocusListener=None):
            pass
    
        def removePropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def requestFocus(self, ):
            pass
    
        def setAccessibleDescription(self, String=None):
            pass
    
        def setAccessibleName(self, String=None):
            pass
    
        def setAccessibleParent(self, Accessible=None):
            pass
    
        def setBackground(self, Color=None):
            pass
    
        def setBounds(self, Rectangle=None):
            pass
    
        def setCursor(self, Cursor=None):
            pass
    
        def setEnabled(self, boolean=None):
            pass
    
        def setFont(self, Font=None):
            pass
    
        def setForeground(self, Color=None):
            pass
    
        def setLocation(self, Point=None):
            pass
    
        def setSize(self, Dimension=None):
            pass
    
        def setVisible(self, boolean=None):
            pass
    
        def toString(self, ):
            pass

    class BaselineResizeBehavior(object):
        CENTER_OFFSET = None
        CONSTANT_ASCENT = None
        CONSTANT_DESCENT = None
        OTHER = None
    
        class EnumDesc(object):
        
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

    def __init__(self, String=None, Icon1=None):
        pass

    def action(self, Event=None, Object1=None):
        pass

    def add(self, Component=None, Object1=None, int2=None):
        pass

    def addActionListener(self, ActionListener=None):
        pass

    def addAncestorListener(self, AncestorListener=None):
        pass

    def addChangeListener(self, ChangeListener=None):
        pass

    def addComponentListener(self, ComponentListener=None):
        pass

    def addContainerListener(self, ContainerListener=None):
        pass

    def addFocusListener(self, FocusListener=None):
        pass

    def addHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def addHierarchyListener(self, HierarchyListener=None):
        pass

    def addInputMethodListener(self, InputMethodListener=None):
        pass

    def addItemListener(self, ItemListener=None):
        pass

    def addKeyListener(self, KeyListener=None):
        pass

    def addMouseListener(self, MouseListener=None):
        pass

    def addMouseMotionListener(self, MouseMotionListener=None):
        pass

    def addMouseWheelListener(self, MouseWheelListener=None):
        pass

    def addNotify(self, ):
        pass

    def addPropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def addVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def applyComponentOrientation(self, ComponentOrientation=None):
        pass

    def areFocusTraversalKeysSet(self, int=None):
        pass

    def bounds(self, ):
        pass

    def checkImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def computeVisibleRect(self, Rectangle=None):
        pass

    def contains(self, int=None, int1=None):
        pass

    def countComponents(self, ):
        pass

    def createImage(self, int=None, int1=None):
        pass

    def createToolTip(self, ):
        pass

    def createVolatileImage(self, int=None, int1=None, ImageCapabilities2=None):
        pass

    def deliverEvent(self, Event=None):
        pass

    def disable(self, ):
        pass

    def dispatchEvent(self, AWTEvent=None):
        pass

    def doClick(self, int=None):
        pass

    def doLayout(self, ):
        pass

    def enable(self, boolean=None):
        pass

    def enableInputMethods(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    def findComponentAt(self, int=None, int1=None):
        pass

    def firePropertyChange(self, String=None, byte1=None, byte2=None):
        pass

    def getAccessibleContext(self, ):
        pass

    def getAction(self, ):
        pass

    def getActionCommand(self, ):
        pass

    def getActionForKeyStroke(self, KeyStroke=None):
        pass

    def getActionListeners(self, ):
        pass

    def getActionMap(self, ):
        pass

    def getAlignmentX(self, ):
        pass

    def getAlignmentY(self, ):
        pass

    def getAncestorListeners(self, ):
        pass

    def getAutoscrolls(self, ):
        pass

    def getBackground(self, ):
        pass

    def getBaseline(self, int=None, int1=None):
        pass

    def getBaselineResizeBehavior(self, ):
        pass

    def getBorder(self, ):
        pass

    def getBounds(self, Rectangle=None):
        pass

    def getChangeListeners(self, ):
        pass

    def getClass(self, ):
        pass

    def getClientProperty(self, Object=None):
        pass

    def getColorModel(self, ):
        pass

    def getComponent(self, int=None):
        pass

    def getComponentAt(self, int=None, int1=None):
        pass

    def getComponentCount(self, ):
        pass

    def getComponentListeners(self, ):
        pass

    def getComponentOrientation(self, ):
        pass

    def getComponentPopupMenu(self, ):
        pass

    def getComponentZOrder(self, Component=None):
        pass

    def getComponents(self, ):
        pass

    def getConditionForKeyStroke(self, KeyStroke=None):
        pass

    def getContainerListeners(self, ):
        pass

    def getCursor(self, ):
        pass

    def getDebugGraphicsOptions(self, ):
        pass

    @staticmethod
    def getDefaultLocale():
        pass

    def getDisabledIcon(self, ):
        pass

    def getDisabledSelectedIcon(self, ):
        pass

    def getDisplayedMnemonicIndex(self, ):
        pass

    def getDropTarget(self, ):
        pass

    def getFocusCycleRootAncestor(self, ):
        pass

    def getFocusListeners(self, ):
        pass

    def getFocusTraversalKeys(self, int=None):
        pass

    def getFocusTraversalKeysEnabled(self, ):
        pass

    def getFocusTraversalPolicy(self, ):
        pass

    def getFont(self, ):
        pass

    def getFontMetrics(self, Font=None):
        pass

    def getForeground(self, ):
        pass

    def getGraphics(self, ):
        pass

    def getGraphicsConfiguration(self, ):
        pass

    def getHeight(self, ):
        pass

    def getHideActionText(self, ):
        pass

    def getHierarchyBoundsListeners(self, ):
        pass

    def getHierarchyListeners(self, ):
        pass

    def getHorizontalAlignment(self, ):
        pass

    def getHorizontalTextPosition(self, ):
        pass

    def getIcon(self, ):
        pass

    def getIconTextGap(self, ):
        pass

    def getIgnoreRepaint(self, ):
        pass

    def getInheritsPopupMenu(self, ):
        pass

    def getInputContext(self, ):
        pass

    def getInputMap(self, int=None):
        pass

    def getInputMethodListeners(self, ):
        pass

    def getInputMethodRequests(self, ):
        pass

    def getInputVerifier(self, ):
        pass

    def getInsets(self, Insets=None):
        pass

    def getItemListeners(self, ):
        pass

    def getKeyListeners(self, ):
        pass

    def getLabel(self, ):
        pass

    def getLayout(self, ):
        pass

    def getListeners(self, Class=None):
        pass

    def getLocale(self, ):
        pass

    def getLocation(self, Point=None):
        pass

    def getLocationOnScreen(self, ):
        pass

    def getMargin(self, ):
        pass

    def getMaximumSize(self, ):
        pass

    def getMinimumSize(self, ):
        pass

    def getMnemonic(self, ):
        pass

    def getModel(self, ):
        pass

    def getMouseListeners(self, ):
        pass

    def getMouseMotionListeners(self, ):
        pass

    def getMousePosition(self, boolean=None):
        pass

    def getMouseWheelListeners(self, ):
        pass

    def getMultiClickThreshhold(self, ):
        pass

    def getName(self, ):
        pass

    def getNextFocusableComponent(self, ):
        pass

    def getParent(self, ):
        pass

    def getPopupLocation(self, MouseEvent=None):
        pass

    def getPreferredSize(self, ):
        pass

    def getPressedIcon(self, ):
        pass

    def getPropertyChangeListeners(self, String=None):
        pass

    def getRegisteredKeyStrokes(self, ):
        pass

    def getRolloverIcon(self, ):
        pass

    def getRolloverSelectedIcon(self, ):
        pass

    def getRootPane(self, ):
        pass

    def getSelectedIcon(self, ):
        pass

    def getSelectedObjects(self, ):
        pass

    def getSize(self, Dimension=None):
        pass

    def getText(self, ):
        pass

    def getToolTipLocation(self, MouseEvent=None):
        pass

    def getToolTipText(self, MouseEvent=None):
        pass

    def getToolkit(self, ):
        pass

    def getTopLevelAncestor(self, ):
        pass

    def getTransferHandler(self, ):
        pass

    def getTreeLock(self, ):
        pass

    def getUI(self, ):
        pass

    def getUIClassID(self, ):
        pass

    def getVerifyInputWhenFocusTarget(self, ):
        pass

    def getVerticalAlignment(self, ):
        pass

    def getVerticalTextPosition(self, ):
        pass

    def getVetoableChangeListeners(self, ):
        pass

    def getVisibleRect(self, ):
        pass

    def getWidth(self, ):
        pass

    def getX(self, ):
        pass

    def getY(self, ):
        pass

    def gotFocus(self, Event=None, Object1=None):
        pass

    def grabFocus(self, ):
        pass

    def handleEvent(self, Event=None):
        pass

    def hasFocus(self, ):
        pass

    def hide(self, ):
        pass

    def imageUpdate(self, Image=None, int1=None, int2=None, int3=None, int4=None, int5=None):
        pass

    def insets(self, ):
        pass

    def inside(self, int=None, int1=None):
        pass

    def invalidate(self, ):
        pass

    def isAncestorOf(self, Component=None):
        pass

    def isBackgroundSet(self, ):
        pass

    def isBorderPainted(self, ):
        pass

    def isContentAreaFilled(self, ):
        pass

    def isCursorSet(self, ):
        pass

    def isDefaultButton(self, ):
        pass

    def isDefaultCapable(self, ):
        pass

    def isDisplayable(self, ):
        pass

    def isDoubleBuffered(self, ):
        pass

    def isEnabled(self, ):
        pass

    def isFocusCycleRoot(self, Container=None):
        pass

    def isFocusOwner(self, ):
        pass

    def isFocusPainted(self, ):
        pass

    def isFocusTraversable(self, ):
        pass

    def isFocusTraversalPolicyProvider(self, ):
        pass

    def isFocusTraversalPolicySet(self, ):
        pass

    def isFocusable(self, ):
        pass

    def isFontSet(self, ):
        pass

    def isForegroundSet(self, ):
        pass

    def isLightweight(self, ):
        pass

    @staticmethod
    def isLightweightComponent(Component=None):
        pass

    def isManagingFocus(self, ):
        pass

    def isMaximumSizeSet(self, ):
        pass

    def isMinimumSizeSet(self, ):
        pass

    def isOpaque(self, ):
        pass

    def isOptimizedDrawingEnabled(self, ):
        pass

    def isPaintingForPrint(self, ):
        pass

    def isPaintingTile(self, ):
        pass

    def isPreferredSizeSet(self, ):
        pass

    def isRequestFocusEnabled(self, ):
        pass

    def isRolloverEnabled(self, ):
        pass

    def isSelected(self, ):
        pass

    def isShowing(self, ):
        pass

    def isValid(self, ):
        pass

    def isValidateRoot(self, ):
        pass

    def isVisible(self, ):
        pass

    def keyDown(self, Event=None, int1=None):
        pass

    def keyUp(self, Event=None, int1=None):
        pass

    def layout(self, ):
        pass

    def list(self, PrintStream=None, int1=None):
        pass

    def locate(self, int=None, int1=None):
        pass

    def location(self, ):
        pass

    def lostFocus(self, Event=None, Object1=None):
        pass

    def minimumSize(self, ):
        pass

    def mouseDown(self, Event=None, int1=None, int2=None):
        pass

    def mouseDrag(self, Event=None, int1=None, int2=None):
        pass

    def mouseEnter(self, Event=None, int1=None, int2=None):
        pass

    def mouseExit(self, Event=None, int1=None, int2=None):
        pass

    def mouseMove(self, Event=None, int1=None, int2=None):
        pass

    def mouseUp(self, Event=None, int1=None, int2=None):
        pass

    def move(self, int=None, int1=None):
        pass

    def nextFocus(self, ):
        pass

    def paint(self, Graphics=None):
        pass

    def paintAll(self, Graphics=None):
        pass

    def paintComponents(self, Graphics=None):
        pass

    def paintImmediately(self, int=None, int1=None, int2=None, int3=None):
        pass

    def postEvent(self, Event=None):
        pass

    def preferredSize(self, ):
        pass

    def prepareImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def printAll(self, Graphics=None):
        pass

    def printComponents(self, Graphics=None):
        pass

    def putClientProperty(self, Object=None, Object1=None):
        pass

    def registerKeyboardAction(self, ActionListener=None, String1=None, KeyStroke2=None, int3=None):
        pass

    def remove(self, MenuComponent=None):
        pass

    def removeActionListener(self, ActionListener=None):
        pass

    def removeAll(self, ):
        pass

    def removeAncestorListener(self, AncestorListener=None):
        pass

    def removeChangeListener(self, ChangeListener=None):
        pass

    def removeComponentListener(self, ComponentListener=None):
        pass

    def removeContainerListener(self, ContainerListener=None):
        pass

    def removeFocusListener(self, FocusListener=None):
        pass

    def removeHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def removeHierarchyListener(self, HierarchyListener=None):
        pass

    def removeInputMethodListener(self, InputMethodListener=None):
        pass

    def removeItemListener(self, ItemListener=None):
        pass

    def removeKeyListener(self, KeyListener=None):
        pass

    def removeMouseListener(self, MouseListener=None):
        pass

    def removeMouseMotionListener(self, MouseMotionListener=None):
        pass

    def removeMouseWheelListener(self, MouseWheelListener=None):
        pass

    def removeNotify(self, ):
        pass

    def removePropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def removeVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def repaint(self, long=None, int1=None, int2=None, int3=None, int4=None):
        pass

    def requestDefaultFocus(self, ):
        pass

    def requestFocus(self, boolean=None):
        pass

    def requestFocusInWindow(self, Cause=None):
        pass

    def resetKeyboardActions(self, ):
        pass

    def reshape(self, int=None, int1=None, int2=None, int3=None):
        pass

    def resize(self, int=None, int1=None):
        pass

    def revalidate(self, ):
        pass

    def scrollRectToVisible(self, Rectangle=None):
        pass

    def setAction(self, Action=None):
        pass

    def setActionCommand(self, String=None):
        pass

    def setActionMap(self, ActionMap=None):
        pass

    def setAlignmentX(self, float=None):
        pass

    def setAlignmentY(self, float=None):
        pass

    def setAutoscrolls(self, boolean=None):
        pass

    def setBackground(self, Color=None):
        pass

    def setBorder(self, Border=None):
        pass

    def setBorderPainted(self, boolean=None):
        pass

    def setBounds(self, int=None, int1=None, int2=None, int3=None):
        pass

    def setComponentOrientation(self, ComponentOrientation=None):
        pass

    def setComponentPopupMenu(self, JPopupMenu=None):
        pass

    def setComponentZOrder(self, Component=None, int1=None):
        pass

    def setContentAreaFilled(self, boolean=None):
        pass

    def setCursor(self, Cursor=None):
        pass

    def setDebugGraphicsOptions(self, int=None):
        pass

    def setDefaultCapable(self, boolean=None):
        pass

    @staticmethod
    def setDefaultLocale(Locale=None):
        pass

    def setDisabledIcon(self, Icon=None):
        pass

    def setDisabledSelectedIcon(self, Icon=None):
        pass

    def setDisplayedMnemonicIndex(self, int=None):
        pass

    def setDoubleBuffered(self, boolean=None):
        pass

    def setDropTarget(self, DropTarget=None):
        pass

    def setEnabled(self, boolean=None):
        pass

    def setFocusCycleRoot(self, boolean=None):
        pass

    def setFocusPainted(self, boolean=None):
        pass

    def setFocusTraversalKeys(self, int=None, Set1=None):
        pass

    def setFocusTraversalKeysEnabled(self, boolean=None):
        pass

    def setFocusTraversalPolicy(self, FocusTraversalPolicy=None):
        pass

    def setFocusTraversalPolicyProvider(self, boolean=None):
        pass

    def setFocusable(self, boolean=None):
        pass

    def setFont(self, Font=None):
        pass

    def setForeground(self, Color=None):
        pass

    def setHideActionText(self, boolean=None):
        pass

    def setHorizontalAlignment(self, int=None):
        pass

    def setHorizontalTextPosition(self, int=None):
        pass

    def setIcon(self, Icon=None):
        pass

    def setIconTextGap(self, int=None):
        pass

    def setIgnoreRepaint(self, boolean=None):
        pass

    def setInheritsPopupMenu(self, boolean=None):
        pass

    def setInputMap(self, int=None, InputMap1=None):
        pass

    def setInputVerifier(self, InputVerifier=None):
        pass

    def setLabel(self, String=None):
        pass

    def setLayout(self, LayoutManager=None):
        pass

    def setLocale(self, Locale=None):
        pass

    def setLocation(self, int=None, int1=None):
        pass

    def setMargin(self, Insets=None):
        pass

    def setMaximumSize(self, Dimension=None):
        pass

    def setMinimumSize(self, Dimension=None):
        pass

    def setMixingCutoutShape(self, Shape=None):
        pass

    def setMnemonic(self, char=None):
        pass

    def setModel(self, ButtonModel=None):
        pass

    def setMultiClickThreshhold(self, long=None):
        pass

    def setName(self, String=None):
        pass

    def setNextFocusableComponent(self, Component=None):
        pass

    def setOpaque(self, boolean=None):
        pass

    def setPreferredSize(self, Dimension=None):
        pass

    def setPressedIcon(self, Icon=None):
        pass

    def setRequestFocusEnabled(self, boolean=None):
        pass

    def setRolloverEnabled(self, boolean=None):
        pass

    def setRolloverIcon(self, Icon=None):
        pass

    def setRolloverSelectedIcon(self, Icon=None):
        pass

    def setSelected(self, boolean=None):
        pass

    def setSelectedIcon(self, Icon=None):
        pass

    def setSize(self, int=None, int1=None):
        pass

    def setText(self, String=None):
        pass

    def setToolTipText(self, String=None):
        pass

    def setTransferHandler(self, TransferHandler=None):
        pass

    def setUI(self, ButtonUI=None):
        pass

    def setVerifyInputWhenFocusTarget(self, boolean=None):
        pass

    def setVerticalAlignment(self, int=None):
        pass

    def setVerticalTextPosition(self, int=None):
        pass

    def setVisible(self, boolean=None):
        pass

    def show(self, boolean=None):
        pass

    def size(self, ):
        pass

    def toString(self, ):
        pass

    def transferFocus(self, ):
        pass

    def transferFocusBackward(self, ):
        pass

    def transferFocusDownCycle(self, ):
        pass

    def transferFocusUpCycle(self, ):
        pass

    def unregisterKeyboardAction(self, KeyStroke=None):
        pass

    def update(self, Graphics=None):
        pass

    def updateUI(self, ):
        pass

    def validate(self, ):
        pass

class JFrame(object):
    ABORT = None
    ALLBITS = None
    BOTTOM_ALIGNMENT = None
    CENTER_ALIGNMENT = None
    CROSSHAIR_CURSOR = None
    DEFAULT_CURSOR = None
    DISPOSE_ON_CLOSE = None
    DO_NOTHING_ON_CLOSE = None
    ERROR = None
    EXIT_ON_CLOSE = None
    E_RESIZE_CURSOR = None
    FRAMEBITS = None
    HAND_CURSOR = None
    HEIGHT = None
    HIDE_ON_CLOSE = None
    ICONIFIED = None
    LEFT_ALIGNMENT = None
    MAXIMIZED_BOTH = None
    MAXIMIZED_HORIZ = None
    MAXIMIZED_VERT = None
    MOVE_CURSOR = None
    NE_RESIZE_CURSOR = None
    NORMAL = None
    NW_RESIZE_CURSOR = None
    N_RESIZE_CURSOR = None
    PROPERTIES = None
    RIGHT_ALIGNMENT = None
    SE_RESIZE_CURSOR = None
    SOMEBITS = None
    SW_RESIZE_CURSOR = None
    S_RESIZE_CURSOR = None
    TEXT_CURSOR = None
    TOP_ALIGNMENT = None
    WAIT_CURSOR = None
    WIDTH = None
    W_RESIZE_CURSOR = None

    class BaselineResizeBehavior(object):
        CENTER_OFFSET = None
        CONSTANT_ASCENT = None
        CONSTANT_DESCENT = None
        OTHER = None
    
        class EnumDesc(object):
        
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

    class Type(object):
        NORMAL = None
        POPUP = None
        UTILITY = None
    
        class EnumDesc(object):
        
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

    def __init__(self, String=None, GraphicsConfiguration1=None):
        pass

    def action(self, Event=None, Object1=None):
        pass

    def add(self, Component=None, Object1=None, int2=None):
        pass

    def addComponentListener(self, ComponentListener=None):
        pass

    def addContainerListener(self, ContainerListener=None):
        pass

    def addFocusListener(self, FocusListener=None):
        pass

    def addHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def addHierarchyListener(self, HierarchyListener=None):
        pass

    def addInputMethodListener(self, InputMethodListener=None):
        pass

    def addKeyListener(self, KeyListener=None):
        pass

    def addMouseListener(self, MouseListener=None):
        pass

    def addMouseMotionListener(self, MouseMotionListener=None):
        pass

    def addMouseWheelListener(self, MouseWheelListener=None):
        pass

    def addNotify(self, ):
        pass

    def addPropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def addWindowFocusListener(self, WindowFocusListener=None):
        pass

    def addWindowListener(self, WindowListener=None):
        pass

    def addWindowStateListener(self, WindowStateListener=None):
        pass

    def applyComponentOrientation(self, ComponentOrientation=None):
        pass

    def applyResourceBundle(self, String=None):
        pass

    def areFocusTraversalKeysSet(self, int=None):
        pass

    def bounds(self, ):
        pass

    def checkImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def contains(self, int=None, int1=None):
        pass

    def countComponents(self, ):
        pass

    def createBufferStrategy(self, int=None, BufferCapabilities1=None):
        pass

    def createImage(self, int=None, int1=None):
        pass

    def createVolatileImage(self, int=None, int1=None, ImageCapabilities2=None):
        pass

    def deliverEvent(self, Event=None):
        pass

    def disable(self, ):
        pass

    def dispatchEvent(self, AWTEvent=None):
        pass

    def dispose(self, ):
        pass

    def doLayout(self, ):
        pass

    def enable(self, boolean=None):
        pass

    def enableInputMethods(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    def findComponentAt(self, int=None, int1=None):
        pass

    def firePropertyChange(self, String=None, byte1=None, byte2=None):
        pass

    def getAccessibleContext(self, ):
        pass

    def getAlignmentX(self, ):
        pass

    def getAlignmentY(self, ):
        pass

    def getBackground(self, ):
        pass

    def getBaseline(self, int=None, int1=None):
        pass

    def getBaselineResizeBehavior(self, ):
        pass

    def getBounds(self, Rectangle=None):
        pass

    def getBufferStrategy(self, ):
        pass

    def getClass(self, ):
        pass

    def getColorModel(self, ):
        pass

    def getComponent(self, int=None):
        pass

    def getComponentAt(self, int=None, int1=None):
        pass

    def getComponentCount(self, ):
        pass

    def getComponentListeners(self, ):
        pass

    def getComponentOrientation(self, ):
        pass

    def getComponentZOrder(self, Component=None):
        pass

    def getComponents(self, ):
        pass

    def getContainerListeners(self, ):
        pass

    def getContentPane(self, ):
        pass

    def getCursor(self, ):
        pass

    def getCursorType(self, ):
        pass

    def getDefaultCloseOperation(self, ):
        pass

    def getDropTarget(self, ):
        pass

    def getExtendedState(self, ):
        pass

    def getFocusCycleRootAncestor(self, ):
        pass

    def getFocusListeners(self, ):
        pass

    def getFocusOwner(self, ):
        pass

    def getFocusTraversalKeys(self, int=None):
        pass

    def getFocusTraversalKeysEnabled(self, ):
        pass

    def getFocusTraversalPolicy(self, ):
        pass

    def getFocusableWindowState(self, ):
        pass

    def getFont(self, ):
        pass

    def getFontMetrics(self, Font=None):
        pass

    def getForeground(self, ):
        pass

    @staticmethod
    def getFrames():
        pass

    def getGlassPane(self, ):
        pass

    def getGraphics(self, ):
        pass

    def getGraphicsConfiguration(self, ):
        pass

    def getHeight(self, ):
        pass

    def getHierarchyBoundsListeners(self, ):
        pass

    def getHierarchyListeners(self, ):
        pass

    def getIconImage(self, ):
        pass

    def getIconImages(self, ):
        pass

    def getIgnoreRepaint(self, ):
        pass

    def getInputContext(self, ):
        pass

    def getInputMethodListeners(self, ):
        pass

    def getInputMethodRequests(self, ):
        pass

    def getInsets(self, ):
        pass

    def getJMenuBar(self, ):
        pass

    def getKeyListeners(self, ):
        pass

    def getLayeredPane(self, ):
        pass

    def getLayout(self, ):
        pass

    def getListeners(self, Class=None):
        pass

    def getLocale(self, ):
        pass

    def getLocation(self, Point=None):
        pass

    def getLocationOnScreen(self, ):
        pass

    def getMaximizedBounds(self, ):
        pass

    def getMaximumSize(self, ):
        pass

    def getMenuBar(self, ):
        pass

    def getMinimumSize(self, ):
        pass

    def getModalExclusionType(self, ):
        pass

    def getMostRecentFocusOwner(self, ):
        pass

    def getMouseListeners(self, ):
        pass

    def getMouseMotionListeners(self, ):
        pass

    def getMousePosition(self, boolean=None):
        pass

    def getMouseWheelListeners(self, ):
        pass

    def getName(self, ):
        pass

    def getOpacity(self, ):
        pass

    def getOwnedWindows(self, ):
        pass

    def getOwner(self, ):
        pass

    @staticmethod
    def getOwnerlessWindows():
        pass

    def getParent(self, ):
        pass

    def getPreferredSize(self, ):
        pass

    def getPropertyChangeListeners(self, String=None):
        pass

    def getRootPane(self, ):
        pass

    def getShape(self, ):
        pass

    def getSize(self, Dimension=None):
        pass

    def getState(self, ):
        pass

    def getTitle(self, ):
        pass

    def getToolkit(self, ):
        pass

    def getTransferHandler(self, ):
        pass

    def getTreeLock(self, ):
        pass

    def getType(self, ):
        pass

    def getWarningString(self, ):
        pass

    def getWidth(self, ):
        pass

    def getWindowFocusListeners(self, ):
        pass

    def getWindowListeners(self, ):
        pass

    def getWindowStateListeners(self, ):
        pass

    @staticmethod
    def getWindows():
        pass

    def getX(self, ):
        pass

    def getY(self, ):
        pass

    def gotFocus(self, Event=None, Object1=None):
        pass

    def handleEvent(self, Event=None):
        pass

    def hasFocus(self, ):
        pass

    def hide(self, ):
        pass

    def imageUpdate(self, Image=None, int1=None, int2=None, int3=None, int4=None, int5=None):
        pass

    def insets(self, ):
        pass

    def inside(self, int=None, int1=None):
        pass

    def invalidate(self, ):
        pass

    def isActive(self, ):
        pass

    def isAlwaysOnTop(self, ):
        pass

    def isAlwaysOnTopSupported(self, ):
        pass

    def isAncestorOf(self, Component=None):
        pass

    def isAutoRequestFocus(self, ):
        pass

    def isBackgroundSet(self, ):
        pass

    def isCursorSet(self, ):
        pass

    @staticmethod
    def isDefaultLookAndFeelDecorated():
        pass

    def isDisplayable(self, ):
        pass

    def isDoubleBuffered(self, ):
        pass

    def isEnabled(self, ):
        pass

    def isFocusCycleRoot(self, Container=None):
        pass

    def isFocusOwner(self, ):
        pass

    def isFocusTraversable(self, ):
        pass

    def isFocusTraversalPolicyProvider(self, ):
        pass

    def isFocusTraversalPolicySet(self, ):
        pass

    def isFocusable(self, ):
        pass

    def isFocusableWindow(self, ):
        pass

    def isFocused(self, ):
        pass

    def isFontSet(self, ):
        pass

    def isForegroundSet(self, ):
        pass

    def isLightweight(self, ):
        pass

    def isLocationByPlatform(self, ):
        pass

    def isMaximumSizeSet(self, ):
        pass

    def isMinimumSizeSet(self, ):
        pass

    def isOpaque(self, ):
        pass

    def isPreferredSizeSet(self, ):
        pass

    def isResizable(self, ):
        pass

    def isShowing(self, ):
        pass

    def isUndecorated(self, ):
        pass

    def isValid(self, ):
        pass

    def isValidateRoot(self, ):
        pass

    def isVisible(self, ):
        pass

    def keyDown(self, Event=None, int1=None):
        pass

    def keyUp(self, Event=None, int1=None):
        pass

    def layout(self, ):
        pass

    def list(self, PrintStream=None, int1=None):
        pass

    def locate(self, int=None, int1=None):
        pass

    def location(self, ):
        pass

    def lostFocus(self, Event=None, Object1=None):
        pass

    def minimumSize(self, ):
        pass

    def mouseDown(self, Event=None, int1=None, int2=None):
        pass

    def mouseDrag(self, Event=None, int1=None, int2=None):
        pass

    def mouseEnter(self, Event=None, int1=None, int2=None):
        pass

    def mouseExit(self, Event=None, int1=None, int2=None):
        pass

    def mouseMove(self, Event=None, int1=None, int2=None):
        pass

    def mouseUp(self, Event=None, int1=None, int2=None):
        pass

    def move(self, int=None, int1=None):
        pass

    def nextFocus(self, ):
        pass

    def pack(self, ):
        pass

    def paint(self, Graphics=None):
        pass

    def paintAll(self, Graphics=None):
        pass

    def paintComponents(self, Graphics=None):
        pass

    def postEvent(self, Event=None):
        pass

    def preferredSize(self, ):
        pass

    def prepareImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def printAll(self, Graphics=None):
        pass

    def printComponents(self, Graphics=None):
        pass

    def remove(self, int=None):
        pass

    def removeAll(self, ):
        pass

    def removeComponentListener(self, ComponentListener=None):
        pass

    def removeContainerListener(self, ContainerListener=None):
        pass

    def removeFocusListener(self, FocusListener=None):
        pass

    def removeHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def removeHierarchyListener(self, HierarchyListener=None):
        pass

    def removeInputMethodListener(self, InputMethodListener=None):
        pass

    def removeKeyListener(self, KeyListener=None):
        pass

    def removeMouseListener(self, MouseListener=None):
        pass

    def removeMouseMotionListener(self, MouseMotionListener=None):
        pass

    def removeMouseWheelListener(self, MouseWheelListener=None):
        pass

    def removeNotify(self, ):
        pass

    def removePropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def removeWindowFocusListener(self, WindowFocusListener=None):
        pass

    def removeWindowListener(self, WindowListener=None):
        pass

    def removeWindowStateListener(self, WindowStateListener=None):
        pass

    def repaint(self, long=None, int1=None, int2=None, int3=None, int4=None):
        pass

    def requestFocus(self, Cause=None):
        pass

    def requestFocusInWindow(self, Cause=None):
        pass

    def reshape(self, int=None, int1=None, int2=None, int3=None):
        pass

    def resize(self, int=None, int1=None):
        pass

    def revalidate(self, ):
        pass

    def setAlwaysOnTop(self, boolean=None):
        pass

    def setAutoRequestFocus(self, boolean=None):
        pass

    def setBackground(self, Color=None):
        pass

    def setBounds(self, int=None, int1=None, int2=None, int3=None):
        pass

    def setComponentOrientation(self, ComponentOrientation=None):
        pass

    def setComponentZOrder(self, Component=None, int1=None):
        pass

    def setContentPane(self, Container=None):
        pass

    def setCursor(self, int=None):
        pass

    def setDefaultCloseOperation(self, int=None):
        pass

    @staticmethod
    def setDefaultLookAndFeelDecorated(boolean=None):
        pass

    def setDropTarget(self, DropTarget=None):
        pass

    def setEnabled(self, boolean=None):
        pass

    def setExtendedState(self, int=None):
        pass

    def setFocusCycleRoot(self, boolean=None):
        pass

    def setFocusTraversalKeys(self, int=None, Set1=None):
        pass

    def setFocusTraversalKeysEnabled(self, boolean=None):
        pass

    def setFocusTraversalPolicy(self, FocusTraversalPolicy=None):
        pass

    def setFocusTraversalPolicyProvider(self, boolean=None):
        pass

    def setFocusable(self, boolean=None):
        pass

    def setFocusableWindowState(self, boolean=None):
        pass

    def setFont(self, Font=None):
        pass

    def setForeground(self, Color=None):
        pass

    def setGlassPane(self, Component=None):
        pass

    def setIconImage(self, Image=None):
        pass

    def setIconImages(self, List=None):
        pass

    def setIgnoreRepaint(self, boolean=None):
        pass

    def setJMenuBar(self, JMenuBar=None):
        pass

    def setLayeredPane(self, JLayeredPane=None):
        pass

    def setLayout(self, LayoutManager=None):
        pass

    def setLocale(self, Locale=None):
        pass

    def setLocation(self, int=None, int1=None):
        pass

    def setLocationByPlatform(self, boolean=None):
        pass

    def setLocationRelativeTo(self, Component=None):
        pass

    def setMaximizedBounds(self, Rectangle=None):
        pass

    def setMaximumSize(self, Dimension=None):
        pass

    def setMenuBar(self, MenuBar=None):
        pass

    def setMinimumSize(self, Dimension=None):
        pass

    def setMixingCutoutShape(self, Shape=None):
        pass

    def setModalExclusionType(self, ModalExclusionType=None):
        pass

    def setName(self, String=None):
        pass

    def setOpacity(self, float=None):
        pass

    def setPreferredSize(self, Dimension=None):
        pass

    def setResizable(self, boolean=None):
        pass

    def setShape(self, Shape=None):
        pass

    def setSize(self, int=None, int1=None):
        pass

    def setState(self, int=None):
        pass

    def setTitle(self, String=None):
        pass

    def setTransferHandler(self, TransferHandler=None):
        pass

    def setType(self, Type=None):
        pass

    def setUndecorated(self, boolean=None):
        pass

    def setVisible(self, boolean=None):
        pass

    def show(self, boolean=None):
        pass

    def size(self, ):
        pass

    def toBack(self, ):
        pass

    def toFront(self, ):
        pass

    def toString(self, ):
        pass

    def transferFocus(self, ):
        pass

    def transferFocusBackward(self, ):
        pass

    def transferFocusDownCycle(self, ):
        pass

    def transferFocusUpCycle(self, ):
        pass

    def update(self, Graphics=None):
        pass

    def validate(self, ):
        pass

class JPanel(object):
    ABORT = None
    ALLBITS = None
    BOTTOM_ALIGNMENT = None
    CENTER_ALIGNMENT = None
    ERROR = None
    FRAMEBITS = None
    HEIGHT = None
    LEFT_ALIGNMENT = None
    PROPERTIES = None
    RIGHT_ALIGNMENT = None
    SOMEBITS = None
    TOOL_TIP_TEXT_KEY = None
    TOP_ALIGNMENT = None
    UNDEFINED_CONDITION = None
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT = None
    WHEN_FOCUSED = None
    WHEN_IN_FOCUSED_WINDOW = None
    WIDTH = None

    class AccessibleJComponent(object):
        ACCESSIBLE_ACTION_PROPERTY = None
        ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY = None
        ACCESSIBLE_CARET_PROPERTY = None
        ACCESSIBLE_CHILD_PROPERTY = None
        ACCESSIBLE_COMPONENT_BOUNDS_CHANGED = None
        ACCESSIBLE_DESCRIPTION_PROPERTY = None
        ACCESSIBLE_HYPERTEXT_OFFSET = None
        ACCESSIBLE_INVALIDATE_CHILDREN = None
        ACCESSIBLE_NAME_PROPERTY = None
        ACCESSIBLE_SELECTION_PROPERTY = None
        ACCESSIBLE_STATE_PROPERTY = None
        ACCESSIBLE_TABLE_CAPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_MODEL_CHANGED = None
        ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_ROW_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_SUMMARY_CHANGED = None
        ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED = None
        ACCESSIBLE_TEXT_PROPERTY = None
        ACCESSIBLE_VALUE_PROPERTY = None
        ACCESSIBLE_VISIBLE_DATA_PROPERTY = None
    
        def addFocusListener(self, FocusListener=None):
            pass
    
        def addPropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def contains(self, Point=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def firePropertyChange(self, String=None, Object1=None, Object2=None):
            pass
    
        def getAccessibleAction(self, ):
            pass
    
        def getAccessibleAt(self, Point=None):
            pass
    
        def getAccessibleChild(self, int=None):
            pass
    
        def getAccessibleChildrenCount(self, ):
            pass
    
        def getAccessibleComponent(self, ):
            pass
    
        def getAccessibleDescription(self, ):
            pass
    
        def getAccessibleEditableText(self, ):
            pass
    
        def getAccessibleIcon(self, ):
            pass
    
        def getAccessibleIndexInParent(self, ):
            pass
    
        def getAccessibleKeyBinding(self, ):
            pass
    
        def getAccessibleName(self, ):
            pass
    
        def getAccessibleParent(self, ):
            pass
    
        def getAccessibleRelationSet(self, ):
            pass
    
        def getAccessibleRole(self, ):
            pass
    
        def getAccessibleSelection(self, ):
            pass
    
        def getAccessibleStateSet(self, ):
            pass
    
        def getAccessibleTable(self, ):
            pass
    
        def getAccessibleText(self, ):
            pass
    
        def getAccessibleValue(self, ):
            pass
    
        def getBackground(self, ):
            pass
    
        def getBounds(self, ):
            pass
    
        def getClass(self, ):
            pass
    
        def getCursor(self, ):
            pass
    
        def getFont(self, ):
            pass
    
        def getFontMetrics(self, Font=None):
            pass
    
        def getForeground(self, ):
            pass
    
        def getLocale(self, ):
            pass
    
        def getLocation(self, ):
            pass
    
        def getLocationOnScreen(self, ):
            pass
    
        def getSize(self, ):
            pass
    
        def getTitledBorderText(self, ):
            pass
    
        def getToolTipText(self, ):
            pass
    
        def isEnabled(self, ):
            pass
    
        def isFocusTraversable(self, ):
            pass
    
        def isShowing(self, ):
            pass
    
        def isVisible(self, ):
            pass
    
        def removeFocusListener(self, FocusListener=None):
            pass
    
        def removePropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def requestFocus(self, ):
            pass
    
        def setAccessibleDescription(self, String=None):
            pass
    
        def setAccessibleName(self, String=None):
            pass
    
        def setAccessibleParent(self, Accessible=None):
            pass
    
        def setBackground(self, Color=None):
            pass
    
        def setBounds(self, Rectangle=None):
            pass
    
        def setCursor(self, Cursor=None):
            pass
    
        def setEnabled(self, boolean=None):
            pass
    
        def setFont(self, Font=None):
            pass
    
        def setForeground(self, Color=None):
            pass
    
        def setLocation(self, Point=None):
            pass
    
        def setSize(self, Dimension=None):
            pass
    
        def setVisible(self, boolean=None):
            pass
    
        def toString(self, ):
            pass

    class BaselineResizeBehavior(object):
        CENTER_OFFSET = None
        CONSTANT_ASCENT = None
        CONSTANT_DESCENT = None
        OTHER = None
    
        class EnumDesc(object):
        
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

    def __init__(self, LayoutManager=None, boolean1=None):
        pass

    def action(self, Event=None, Object1=None):
        pass

    def add(self, Component=None, Object1=None, int2=None):
        pass

    def addAncestorListener(self, AncestorListener=None):
        pass

    def addComponentListener(self, ComponentListener=None):
        pass

    def addContainerListener(self, ContainerListener=None):
        pass

    def addFocusListener(self, FocusListener=None):
        pass

    def addHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def addHierarchyListener(self, HierarchyListener=None):
        pass

    def addInputMethodListener(self, InputMethodListener=None):
        pass

    def addKeyListener(self, KeyListener=None):
        pass

    def addMouseListener(self, MouseListener=None):
        pass

    def addMouseMotionListener(self, MouseMotionListener=None):
        pass

    def addMouseWheelListener(self, MouseWheelListener=None):
        pass

    def addNotify(self, ):
        pass

    def addPropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def addVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def applyComponentOrientation(self, ComponentOrientation=None):
        pass

    def areFocusTraversalKeysSet(self, int=None):
        pass

    def bounds(self, ):
        pass

    def checkImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def computeVisibleRect(self, Rectangle=None):
        pass

    def contains(self, int=None, int1=None):
        pass

    def countComponents(self, ):
        pass

    def createImage(self, int=None, int1=None):
        pass

    def createToolTip(self, ):
        pass

    def createVolatileImage(self, int=None, int1=None, ImageCapabilities2=None):
        pass

    def deliverEvent(self, Event=None):
        pass

    def disable(self, ):
        pass

    def dispatchEvent(self, AWTEvent=None):
        pass

    def doLayout(self, ):
        pass

    def enable(self, boolean=None):
        pass

    def enableInputMethods(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    def findComponentAt(self, int=None, int1=None):
        pass

    def firePropertyChange(self, String=None, byte1=None, byte2=None):
        pass

    def getAccessibleContext(self, ):
        pass

    def getActionForKeyStroke(self, KeyStroke=None):
        pass

    def getActionMap(self, ):
        pass

    def getAlignmentX(self, ):
        pass

    def getAlignmentY(self, ):
        pass

    def getAncestorListeners(self, ):
        pass

    def getAutoscrolls(self, ):
        pass

    def getBackground(self, ):
        pass

    def getBaseline(self, int=None, int1=None):
        pass

    def getBaselineResizeBehavior(self, ):
        pass

    def getBorder(self, ):
        pass

    def getBounds(self, Rectangle=None):
        pass

    def getClass(self, ):
        pass

    def getClientProperty(self, Object=None):
        pass

    def getColorModel(self, ):
        pass

    def getComponent(self, int=None):
        pass

    def getComponentAt(self, int=None, int1=None):
        pass

    def getComponentCount(self, ):
        pass

    def getComponentListeners(self, ):
        pass

    def getComponentOrientation(self, ):
        pass

    def getComponentPopupMenu(self, ):
        pass

    def getComponentZOrder(self, Component=None):
        pass

    def getComponents(self, ):
        pass

    def getConditionForKeyStroke(self, KeyStroke=None):
        pass

    def getContainerListeners(self, ):
        pass

    def getCursor(self, ):
        pass

    def getDebugGraphicsOptions(self, ):
        pass

    @staticmethod
    def getDefaultLocale():
        pass

    def getDropTarget(self, ):
        pass

    def getFocusCycleRootAncestor(self, ):
        pass

    def getFocusListeners(self, ):
        pass

    def getFocusTraversalKeys(self, int=None):
        pass

    def getFocusTraversalKeysEnabled(self, ):
        pass

    def getFocusTraversalPolicy(self, ):
        pass

    def getFont(self, ):
        pass

    def getFontMetrics(self, Font=None):
        pass

    def getForeground(self, ):
        pass

    def getGraphics(self, ):
        pass

    def getGraphicsConfiguration(self, ):
        pass

    def getHeight(self, ):
        pass

    def getHierarchyBoundsListeners(self, ):
        pass

    def getHierarchyListeners(self, ):
        pass

    def getIgnoreRepaint(self, ):
        pass

    def getInheritsPopupMenu(self, ):
        pass

    def getInputContext(self, ):
        pass

    def getInputMap(self, int=None):
        pass

    def getInputMethodListeners(self, ):
        pass

    def getInputMethodRequests(self, ):
        pass

    def getInputVerifier(self, ):
        pass

    def getInsets(self, Insets=None):
        pass

    def getKeyListeners(self, ):
        pass

    def getLayout(self, ):
        pass

    def getListeners(self, Class=None):
        pass

    def getLocale(self, ):
        pass

    def getLocation(self, Point=None):
        pass

    def getLocationOnScreen(self, ):
        pass

    def getMaximumSize(self, ):
        pass

    def getMinimumSize(self, ):
        pass

    def getMouseListeners(self, ):
        pass

    def getMouseMotionListeners(self, ):
        pass

    def getMousePosition(self, boolean=None):
        pass

    def getMouseWheelListeners(self, ):
        pass

    def getName(self, ):
        pass

    def getNextFocusableComponent(self, ):
        pass

    def getParent(self, ):
        pass

    def getPopupLocation(self, MouseEvent=None):
        pass

    def getPreferredSize(self, ):
        pass

    def getPropertyChangeListeners(self, String=None):
        pass

    def getRegisteredKeyStrokes(self, ):
        pass

    def getRootPane(self, ):
        pass

    def getSize(self, Dimension=None):
        pass

    def getToolTipLocation(self, MouseEvent=None):
        pass

    def getToolTipText(self, MouseEvent=None):
        pass

    def getToolkit(self, ):
        pass

    def getTopLevelAncestor(self, ):
        pass

    def getTransferHandler(self, ):
        pass

    def getTreeLock(self, ):
        pass

    def getUI(self, ):
        pass

    def getUIClassID(self, ):
        pass

    def getVerifyInputWhenFocusTarget(self, ):
        pass

    def getVetoableChangeListeners(self, ):
        pass

    def getVisibleRect(self, ):
        pass

    def getWidth(self, ):
        pass

    def getX(self, ):
        pass

    def getY(self, ):
        pass

    def gotFocus(self, Event=None, Object1=None):
        pass

    def grabFocus(self, ):
        pass

    def handleEvent(self, Event=None):
        pass

    def hasFocus(self, ):
        pass

    def hide(self, ):
        pass

    def imageUpdate(self, Image=None, int1=None, int2=None, int3=None, int4=None, int5=None):
        pass

    def insets(self, ):
        pass

    def inside(self, int=None, int1=None):
        pass

    def invalidate(self, ):
        pass

    def isAncestorOf(self, Component=None):
        pass

    def isBackgroundSet(self, ):
        pass

    def isCursorSet(self, ):
        pass

    def isDisplayable(self, ):
        pass

    def isDoubleBuffered(self, ):
        pass

    def isEnabled(self, ):
        pass

    def isFocusCycleRoot(self, Container=None):
        pass

    def isFocusOwner(self, ):
        pass

    def isFocusTraversable(self, ):
        pass

    def isFocusTraversalPolicyProvider(self, ):
        pass

    def isFocusTraversalPolicySet(self, ):
        pass

    def isFocusable(self, ):
        pass

    def isFontSet(self, ):
        pass

    def isForegroundSet(self, ):
        pass

    def isLightweight(self, ):
        pass

    @staticmethod
    def isLightweightComponent(Component=None):
        pass

    def isManagingFocus(self, ):
        pass

    def isMaximumSizeSet(self, ):
        pass

    def isMinimumSizeSet(self, ):
        pass

    def isOpaque(self, ):
        pass

    def isOptimizedDrawingEnabled(self, ):
        pass

    def isPaintingForPrint(self, ):
        pass

    def isPaintingTile(self, ):
        pass

    def isPreferredSizeSet(self, ):
        pass

    def isRequestFocusEnabled(self, ):
        pass

    def isShowing(self, ):
        pass

    def isValid(self, ):
        pass

    def isValidateRoot(self, ):
        pass

    def isVisible(self, ):
        pass

    def keyDown(self, Event=None, int1=None):
        pass

    def keyUp(self, Event=None, int1=None):
        pass

    def layout(self, ):
        pass

    def list(self, PrintStream=None, int1=None):
        pass

    def locate(self, int=None, int1=None):
        pass

    def location(self, ):
        pass

    def lostFocus(self, Event=None, Object1=None):
        pass

    def minimumSize(self, ):
        pass

    def mouseDown(self, Event=None, int1=None, int2=None):
        pass

    def mouseDrag(self, Event=None, int1=None, int2=None):
        pass

    def mouseEnter(self, Event=None, int1=None, int2=None):
        pass

    def mouseExit(self, Event=None, int1=None, int2=None):
        pass

    def mouseMove(self, Event=None, int1=None, int2=None):
        pass

    def mouseUp(self, Event=None, int1=None, int2=None):
        pass

    def move(self, int=None, int1=None):
        pass

    def nextFocus(self, ):
        pass

    def paint(self, Graphics=None):
        pass

    def paintAll(self, Graphics=None):
        pass

    def paintComponents(self, Graphics=None):
        pass

    def paintImmediately(self, int=None, int1=None, int2=None, int3=None):
        pass

    def postEvent(self, Event=None):
        pass

    def preferredSize(self, ):
        pass

    def prepareImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def printAll(self, Graphics=None):
        pass

    def printComponents(self, Graphics=None):
        pass

    def putClientProperty(self, Object=None, Object1=None):
        pass

    def registerKeyboardAction(self, ActionListener=None, String1=None, KeyStroke2=None, int3=None):
        pass

    def remove(self, MenuComponent=None):
        pass

    def removeAll(self, ):
        pass

    def removeAncestorListener(self, AncestorListener=None):
        pass

    def removeComponentListener(self, ComponentListener=None):
        pass

    def removeContainerListener(self, ContainerListener=None):
        pass

    def removeFocusListener(self, FocusListener=None):
        pass

    def removeHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def removeHierarchyListener(self, HierarchyListener=None):
        pass

    def removeInputMethodListener(self, InputMethodListener=None):
        pass

    def removeKeyListener(self, KeyListener=None):
        pass

    def removeMouseListener(self, MouseListener=None):
        pass

    def removeMouseMotionListener(self, MouseMotionListener=None):
        pass

    def removeMouseWheelListener(self, MouseWheelListener=None):
        pass

    def removeNotify(self, ):
        pass

    def removePropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def removeVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def repaint(self, long=None, int1=None, int2=None, int3=None, int4=None):
        pass

    def requestDefaultFocus(self, ):
        pass

    def requestFocus(self, boolean=None):
        pass

    def requestFocusInWindow(self, Cause=None):
        pass

    def resetKeyboardActions(self, ):
        pass

    def reshape(self, int=None, int1=None, int2=None, int3=None):
        pass

    def resize(self, int=None, int1=None):
        pass

    def revalidate(self, ):
        pass

    def scrollRectToVisible(self, Rectangle=None):
        pass

    def setActionMap(self, ActionMap=None):
        pass

    def setAlignmentX(self, float=None):
        pass

    def setAlignmentY(self, float=None):
        pass

    def setAutoscrolls(self, boolean=None):
        pass

    def setBackground(self, Color=None):
        pass

    def setBorder(self, Border=None):
        pass

    def setBounds(self, int=None, int1=None, int2=None, int3=None):
        pass

    def setComponentOrientation(self, ComponentOrientation=None):
        pass

    def setComponentPopupMenu(self, JPopupMenu=None):
        pass

    def setComponentZOrder(self, Component=None, int1=None):
        pass

    def setCursor(self, Cursor=None):
        pass

    def setDebugGraphicsOptions(self, int=None):
        pass

    @staticmethod
    def setDefaultLocale(Locale=None):
        pass

    def setDoubleBuffered(self, boolean=None):
        pass

    def setDropTarget(self, DropTarget=None):
        pass

    def setEnabled(self, boolean=None):
        pass

    def setFocusCycleRoot(self, boolean=None):
        pass

    def setFocusTraversalKeys(self, int=None, Set1=None):
        pass

    def setFocusTraversalKeysEnabled(self, boolean=None):
        pass

    def setFocusTraversalPolicy(self, FocusTraversalPolicy=None):
        pass

    def setFocusTraversalPolicyProvider(self, boolean=None):
        pass

    def setFocusable(self, boolean=None):
        pass

    def setFont(self, Font=None):
        pass

    def setForeground(self, Color=None):
        pass

    def setIgnoreRepaint(self, boolean=None):
        pass

    def setInheritsPopupMenu(self, boolean=None):
        pass

    def setInputMap(self, int=None, InputMap1=None):
        pass

    def setInputVerifier(self, InputVerifier=None):
        pass

    def setLayout(self, LayoutManager=None):
        pass

    def setLocale(self, Locale=None):
        pass

    def setLocation(self, int=None, int1=None):
        pass

    def setMaximumSize(self, Dimension=None):
        pass

    def setMinimumSize(self, Dimension=None):
        pass

    def setMixingCutoutShape(self, Shape=None):
        pass

    def setName(self, String=None):
        pass

    def setNextFocusableComponent(self, Component=None):
        pass

    def setOpaque(self, boolean=None):
        pass

    def setPreferredSize(self, Dimension=None):
        pass

    def setRequestFocusEnabled(self, boolean=None):
        pass

    def setSize(self, int=None, int1=None):
        pass

    def setToolTipText(self, String=None):
        pass

    def setTransferHandler(self, TransferHandler=None):
        pass

    def setUI(self, PanelUI=None):
        pass

    def setVerifyInputWhenFocusTarget(self, boolean=None):
        pass

    def setVisible(self, boolean=None):
        pass

    def show(self, boolean=None):
        pass

    def size(self, ):
        pass

    def toString(self, ):
        pass

    def transferFocus(self, ):
        pass

    def transferFocusBackward(self, ):
        pass

    def transferFocusDownCycle(self, ):
        pass

    def transferFocusUpCycle(self, ):
        pass

    def unregisterKeyboardAction(self, KeyStroke=None):
        pass

    def update(self, Graphics=None):
        pass

    def updateUI(self, ):
        pass

    def validate(self, ):
        pass

class JScrollPane(object):
    ABORT = None
    ALLBITS = None
    BOTTOM_ALIGNMENT = None
    CENTER_ALIGNMENT = None
    COLUMN_HEADER = None
    ERROR = None
    FRAMEBITS = None
    HEIGHT = None
    HORIZONTAL_SCROLLBAR = None
    HORIZONTAL_SCROLLBAR_ALWAYS = None
    HORIZONTAL_SCROLLBAR_AS_NEEDED = None
    HORIZONTAL_SCROLLBAR_NEVER = None
    HORIZONTAL_SCROLLBAR_POLICY = None
    LEFT_ALIGNMENT = None
    LOWER_LEADING_CORNER = None
    LOWER_LEFT_CORNER = None
    LOWER_RIGHT_CORNER = None
    LOWER_TRAILING_CORNER = None
    PROPERTIES = None
    RIGHT_ALIGNMENT = None
    ROW_HEADER = None
    SOMEBITS = None
    TOOL_TIP_TEXT_KEY = None
    TOP_ALIGNMENT = None
    UNDEFINED_CONDITION = None
    UPPER_LEADING_CORNER = None
    UPPER_LEFT_CORNER = None
    UPPER_RIGHT_CORNER = None
    UPPER_TRAILING_CORNER = None
    VERTICAL_SCROLLBAR = None
    VERTICAL_SCROLLBAR_ALWAYS = None
    VERTICAL_SCROLLBAR_AS_NEEDED = None
    VERTICAL_SCROLLBAR_NEVER = None
    VERTICAL_SCROLLBAR_POLICY = None
    VIEWPORT = None
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT = None
    WHEN_FOCUSED = None
    WHEN_IN_FOCUSED_WINDOW = None
    WIDTH = None

    class AccessibleJComponent(object):
        ACCESSIBLE_ACTION_PROPERTY = None
        ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY = None
        ACCESSIBLE_CARET_PROPERTY = None
        ACCESSIBLE_CHILD_PROPERTY = None
        ACCESSIBLE_COMPONENT_BOUNDS_CHANGED = None
        ACCESSIBLE_DESCRIPTION_PROPERTY = None
        ACCESSIBLE_HYPERTEXT_OFFSET = None
        ACCESSIBLE_INVALIDATE_CHILDREN = None
        ACCESSIBLE_NAME_PROPERTY = None
        ACCESSIBLE_SELECTION_PROPERTY = None
        ACCESSIBLE_STATE_PROPERTY = None
        ACCESSIBLE_TABLE_CAPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_MODEL_CHANGED = None
        ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED = None
        ACCESSIBLE_TABLE_ROW_HEADER_CHANGED = None
        ACCESSIBLE_TABLE_SUMMARY_CHANGED = None
        ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED = None
        ACCESSIBLE_TEXT_PROPERTY = None
        ACCESSIBLE_VALUE_PROPERTY = None
        ACCESSIBLE_VISIBLE_DATA_PROPERTY = None
    
        def addFocusListener(self, FocusListener=None):
            pass
    
        def addPropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def contains(self, Point=None):
            pass
    
        def equals(self, Object=None):
            pass
    
        def firePropertyChange(self, String=None, Object1=None, Object2=None):
            pass
    
        def getAccessibleAction(self, ):
            pass
    
        def getAccessibleAt(self, Point=None):
            pass
    
        def getAccessibleChild(self, int=None):
            pass
    
        def getAccessibleChildrenCount(self, ):
            pass
    
        def getAccessibleComponent(self, ):
            pass
    
        def getAccessibleDescription(self, ):
            pass
    
        def getAccessibleEditableText(self, ):
            pass
    
        def getAccessibleIcon(self, ):
            pass
    
        def getAccessibleIndexInParent(self, ):
            pass
    
        def getAccessibleKeyBinding(self, ):
            pass
    
        def getAccessibleName(self, ):
            pass
    
        def getAccessibleParent(self, ):
            pass
    
        def getAccessibleRelationSet(self, ):
            pass
    
        def getAccessibleRole(self, ):
            pass
    
        def getAccessibleSelection(self, ):
            pass
    
        def getAccessibleStateSet(self, ):
            pass
    
        def getAccessibleTable(self, ):
            pass
    
        def getAccessibleText(self, ):
            pass
    
        def getAccessibleValue(self, ):
            pass
    
        def getBackground(self, ):
            pass
    
        def getBounds(self, ):
            pass
    
        def getClass(self, ):
            pass
    
        def getCursor(self, ):
            pass
    
        def getFont(self, ):
            pass
    
        def getFontMetrics(self, Font=None):
            pass
    
        def getForeground(self, ):
            pass
    
        def getLocale(self, ):
            pass
    
        def getLocation(self, ):
            pass
    
        def getLocationOnScreen(self, ):
            pass
    
        def getSize(self, ):
            pass
    
        def getTitledBorderText(self, ):
            pass
    
        def getToolTipText(self, ):
            pass
    
        def isEnabled(self, ):
            pass
    
        def isFocusTraversable(self, ):
            pass
    
        def isShowing(self, ):
            pass
    
        def isVisible(self, ):
            pass
    
        def removeFocusListener(self, FocusListener=None):
            pass
    
        def removePropertyChangeListener(self, PropertyChangeListener=None):
            pass
    
        def requestFocus(self, ):
            pass
    
        def setAccessibleDescription(self, String=None):
            pass
    
        def setAccessibleName(self, String=None):
            pass
    
        def setAccessibleParent(self, Accessible=None):
            pass
    
        def setBackground(self, Color=None):
            pass
    
        def setBounds(self, Rectangle=None):
            pass
    
        def setCursor(self, Cursor=None):
            pass
    
        def setEnabled(self, boolean=None):
            pass
    
        def setFont(self, Font=None):
            pass
    
        def setForeground(self, Color=None):
            pass
    
        def setLocation(self, Point=None):
            pass
    
        def setSize(self, Dimension=None):
            pass
    
        def setVisible(self, boolean=None):
            pass
    
        def toString(self, ):
            pass

    class BaselineResizeBehavior(object):
        CENTER_OFFSET = None
        CONSTANT_ASCENT = None
        CONSTANT_DESCENT = None
        OTHER = None
    
        class EnumDesc(object):
        
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

    def __init__(self, Component=None, int1=None, int2=None):
        pass

    def action(self, Event=None, Object1=None):
        pass

    def add(self, Component=None, Object1=None, int2=None):
        pass

    def addAncestorListener(self, AncestorListener=None):
        pass

    def addComponentListener(self, ComponentListener=None):
        pass

    def addContainerListener(self, ContainerListener=None):
        pass

    def addFocusListener(self, FocusListener=None):
        pass

    def addHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def addHierarchyListener(self, HierarchyListener=None):
        pass

    def addInputMethodListener(self, InputMethodListener=None):
        pass

    def addKeyListener(self, KeyListener=None):
        pass

    def addMouseListener(self, MouseListener=None):
        pass

    def addMouseMotionListener(self, MouseMotionListener=None):
        pass

    def addMouseWheelListener(self, MouseWheelListener=None):
        pass

    def addNotify(self, ):
        pass

    def addPropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def addVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def applyComponentOrientation(self, ComponentOrientation=None):
        pass

    def areFocusTraversalKeysSet(self, int=None):
        pass

    def bounds(self, ):
        pass

    def checkImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def computeVisibleRect(self, Rectangle=None):
        pass

    def contains(self, int=None, int1=None):
        pass

    def countComponents(self, ):
        pass

    def createHorizontalScrollBar(self, ):
        pass

    def createImage(self, int=None, int1=None):
        pass

    def createToolTip(self, ):
        pass

    def createVerticalScrollBar(self, ):
        pass

    def createVolatileImage(self, int=None, int1=None, ImageCapabilities2=None):
        pass

    def deliverEvent(self, Event=None):
        pass

    def disable(self, ):
        pass

    def dispatchEvent(self, AWTEvent=None):
        pass

    def doLayout(self, ):
        pass

    def enable(self, boolean=None):
        pass

    def enableInputMethods(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    def findComponentAt(self, int=None, int1=None):
        pass

    def firePropertyChange(self, String=None, byte1=None, byte2=None):
        pass

    def getAccessibleContext(self, ):
        pass

    def getActionForKeyStroke(self, KeyStroke=None):
        pass

    def getActionMap(self, ):
        pass

    def getAlignmentX(self, ):
        pass

    def getAlignmentY(self, ):
        pass

    def getAncestorListeners(self, ):
        pass

    def getAutoscrolls(self, ):
        pass

    def getBackground(self, ):
        pass

    def getBaseline(self, int=None, int1=None):
        pass

    def getBaselineResizeBehavior(self, ):
        pass

    def getBorder(self, ):
        pass

    def getBounds(self, Rectangle=None):
        pass

    def getClass(self, ):
        pass

    def getClientProperty(self, Object=None):
        pass

    def getColorModel(self, ):
        pass

    def getColumnHeader(self, ):
        pass

    def getComponent(self, int=None):
        pass

    def getComponentAt(self, int=None, int1=None):
        pass

    def getComponentCount(self, ):
        pass

    def getComponentListeners(self, ):
        pass

    def getComponentOrientation(self, ):
        pass

    def getComponentPopupMenu(self, ):
        pass

    def getComponentZOrder(self, Component=None):
        pass

    def getComponents(self, ):
        pass

    def getConditionForKeyStroke(self, KeyStroke=None):
        pass

    def getContainerListeners(self, ):
        pass

    def getCorner(self, String=None):
        pass

    def getCursor(self, ):
        pass

    def getDebugGraphicsOptions(self, ):
        pass

    @staticmethod
    def getDefaultLocale():
        pass

    def getDropTarget(self, ):
        pass

    def getFocusCycleRootAncestor(self, ):
        pass

    def getFocusListeners(self, ):
        pass

    def getFocusTraversalKeys(self, int=None):
        pass

    def getFocusTraversalKeysEnabled(self, ):
        pass

    def getFocusTraversalPolicy(self, ):
        pass

    def getFont(self, ):
        pass

    def getFontMetrics(self, Font=None):
        pass

    def getForeground(self, ):
        pass

    def getGraphics(self, ):
        pass

    def getGraphicsConfiguration(self, ):
        pass

    def getHeight(self, ):
        pass

    def getHierarchyBoundsListeners(self, ):
        pass

    def getHierarchyListeners(self, ):
        pass

    def getHorizontalScrollBar(self, ):
        pass

    def getHorizontalScrollBarPolicy(self, ):
        pass

    def getIgnoreRepaint(self, ):
        pass

    def getInheritsPopupMenu(self, ):
        pass

    def getInputContext(self, ):
        pass

    def getInputMap(self, int=None):
        pass

    def getInputMethodListeners(self, ):
        pass

    def getInputMethodRequests(self, ):
        pass

    def getInputVerifier(self, ):
        pass

    def getInsets(self, Insets=None):
        pass

    def getKeyListeners(self, ):
        pass

    def getLayout(self, ):
        pass

    def getListeners(self, Class=None):
        pass

    def getLocale(self, ):
        pass

    def getLocation(self, Point=None):
        pass

    def getLocationOnScreen(self, ):
        pass

    def getMaximumSize(self, ):
        pass

    def getMinimumSize(self, ):
        pass

    def getMouseListeners(self, ):
        pass

    def getMouseMotionListeners(self, ):
        pass

    def getMousePosition(self, boolean=None):
        pass

    def getMouseWheelListeners(self, ):
        pass

    def getName(self, ):
        pass

    def getNextFocusableComponent(self, ):
        pass

    def getParent(self, ):
        pass

    def getPopupLocation(self, MouseEvent=None):
        pass

    def getPreferredSize(self, ):
        pass

    def getPropertyChangeListeners(self, String=None):
        pass

    def getRegisteredKeyStrokes(self, ):
        pass

    def getRootPane(self, ):
        pass

    def getRowHeader(self, ):
        pass

    def getSize(self, Dimension=None):
        pass

    def getToolTipLocation(self, MouseEvent=None):
        pass

    def getToolTipText(self, MouseEvent=None):
        pass

    def getToolkit(self, ):
        pass

    def getTopLevelAncestor(self, ):
        pass

    def getTransferHandler(self, ):
        pass

    def getTreeLock(self, ):
        pass

    def getUI(self, ):
        pass

    def getUIClassID(self, ):
        pass

    def getVerifyInputWhenFocusTarget(self, ):
        pass

    def getVerticalScrollBar(self, ):
        pass

    def getVerticalScrollBarPolicy(self, ):
        pass

    def getVetoableChangeListeners(self, ):
        pass

    def getViewport(self, ):
        pass

    def getViewportBorder(self, ):
        pass

    def getViewportBorderBounds(self, ):
        pass

    def getVisibleRect(self, ):
        pass

    def getWidth(self, ):
        pass

    def getX(self, ):
        pass

    def getY(self, ):
        pass

    def gotFocus(self, Event=None, Object1=None):
        pass

    def grabFocus(self, ):
        pass

    def handleEvent(self, Event=None):
        pass

    def hasFocus(self, ):
        pass

    def hide(self, ):
        pass

    def imageUpdate(self, Image=None, int1=None, int2=None, int3=None, int4=None, int5=None):
        pass

    def insets(self, ):
        pass

    def inside(self, int=None, int1=None):
        pass

    def invalidate(self, ):
        pass

    def isAncestorOf(self, Component=None):
        pass

    def isBackgroundSet(self, ):
        pass

    def isCursorSet(self, ):
        pass

    def isDisplayable(self, ):
        pass

    def isDoubleBuffered(self, ):
        pass

    def isEnabled(self, ):
        pass

    def isFocusCycleRoot(self, Container=None):
        pass

    def isFocusOwner(self, ):
        pass

    def isFocusTraversable(self, ):
        pass

    def isFocusTraversalPolicyProvider(self, ):
        pass

    def isFocusTraversalPolicySet(self, ):
        pass

    def isFocusable(self, ):
        pass

    def isFontSet(self, ):
        pass

    def isForegroundSet(self, ):
        pass

    def isLightweight(self, ):
        pass

    @staticmethod
    def isLightweightComponent(Component=None):
        pass

    def isManagingFocus(self, ):
        pass

    def isMaximumSizeSet(self, ):
        pass

    def isMinimumSizeSet(self, ):
        pass

    def isOpaque(self, ):
        pass

    def isOptimizedDrawingEnabled(self, ):
        pass

    def isPaintingForPrint(self, ):
        pass

    def isPaintingTile(self, ):
        pass

    def isPreferredSizeSet(self, ):
        pass

    def isRequestFocusEnabled(self, ):
        pass

    def isShowing(self, ):
        pass

    def isValid(self, ):
        pass

    def isValidateRoot(self, ):
        pass

    def isVisible(self, ):
        pass

    def isWheelScrollingEnabled(self, ):
        pass

    def keyDown(self, Event=None, int1=None):
        pass

    def keyUp(self, Event=None, int1=None):
        pass

    def layout(self, ):
        pass

    def list(self, PrintStream=None, int1=None):
        pass

    def locate(self, int=None, int1=None):
        pass

    def location(self, ):
        pass

    def lostFocus(self, Event=None, Object1=None):
        pass

    def minimumSize(self, ):
        pass

    def mouseDown(self, Event=None, int1=None, int2=None):
        pass

    def mouseDrag(self, Event=None, int1=None, int2=None):
        pass

    def mouseEnter(self, Event=None, int1=None, int2=None):
        pass

    def mouseExit(self, Event=None, int1=None, int2=None):
        pass

    def mouseMove(self, Event=None, int1=None, int2=None):
        pass

    def mouseUp(self, Event=None, int1=None, int2=None):
        pass

    def move(self, int=None, int1=None):
        pass

    def nextFocus(self, ):
        pass

    def paint(self, Graphics=None):
        pass

    def paintAll(self, Graphics=None):
        pass

    def paintComponents(self, Graphics=None):
        pass

    def paintImmediately(self, int=None, int1=None, int2=None, int3=None):
        pass

    def postEvent(self, Event=None):
        pass

    def preferredSize(self, ):
        pass

    def prepareImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def printAll(self, Graphics=None):
        pass

    def printComponents(self, Graphics=None):
        pass

    def putClientProperty(self, Object=None, Object1=None):
        pass

    def registerKeyboardAction(self, ActionListener=None, String1=None, KeyStroke2=None, int3=None):
        pass

    def remove(self, MenuComponent=None):
        pass

    def removeAll(self, ):
        pass

    def removeAncestorListener(self, AncestorListener=None):
        pass

    def removeComponentListener(self, ComponentListener=None):
        pass

    def removeContainerListener(self, ContainerListener=None):
        pass

    def removeFocusListener(self, FocusListener=None):
        pass

    def removeHierarchyBoundsListener(self, HierarchyBoundsListener=None):
        pass

    def removeHierarchyListener(self, HierarchyListener=None):
        pass

    def removeInputMethodListener(self, InputMethodListener=None):
        pass

    def removeKeyListener(self, KeyListener=None):
        pass

    def removeMouseListener(self, MouseListener=None):
        pass

    def removeMouseMotionListener(self, MouseMotionListener=None):
        pass

    def removeMouseWheelListener(self, MouseWheelListener=None):
        pass

    def removeNotify(self, ):
        pass

    def removePropertyChangeListener(self, String=None, PropertyChangeListener1=None):
        pass

    def removeVetoableChangeListener(self, VetoableChangeListener=None):
        pass

    def repaint(self, long=None, int1=None, int2=None, int3=None, int4=None):
        pass

    def requestDefaultFocus(self, ):
        pass

    def requestFocus(self, boolean=None):
        pass

    def requestFocusInWindow(self, Cause=None):
        pass

    def resetKeyboardActions(self, ):
        pass

    def reshape(self, int=None, int1=None, int2=None, int3=None):
        pass

    def resize(self, int=None, int1=None):
        pass

    def revalidate(self, ):
        pass

    def scrollRectToVisible(self, Rectangle=None):
        pass

    def setActionMap(self, ActionMap=None):
        pass

    def setAlignmentX(self, float=None):
        pass

    def setAlignmentY(self, float=None):
        pass

    def setAutoscrolls(self, boolean=None):
        pass

    def setBackground(self, Color=None):
        pass

    def setBorder(self, Border=None):
        pass

    def setBounds(self, int=None, int1=None, int2=None, int3=None):
        pass

    def setColumnHeader(self, JViewport=None):
        pass

    def setColumnHeaderView(self, Component=None):
        pass

    def setComponentOrientation(self, ComponentOrientation=None):
        pass

    def setComponentPopupMenu(self, JPopupMenu=None):
        pass

    def setComponentZOrder(self, Component=None, int1=None):
        pass

    def setCorner(self, String=None, Component1=None):
        pass

    def setCursor(self, Cursor=None):
        pass

    def setDebugGraphicsOptions(self, int=None):
        pass

    @staticmethod
    def setDefaultLocale(Locale=None):
        pass

    def setDoubleBuffered(self, boolean=None):
        pass

    def setDropTarget(self, DropTarget=None):
        pass

    def setEnabled(self, boolean=None):
        pass

    def setFocusCycleRoot(self, boolean=None):
        pass

    def setFocusTraversalKeys(self, int=None, Set1=None):
        pass

    def setFocusTraversalKeysEnabled(self, boolean=None):
        pass

    def setFocusTraversalPolicy(self, FocusTraversalPolicy=None):
        pass

    def setFocusTraversalPolicyProvider(self, boolean=None):
        pass

    def setFocusable(self, boolean=None):
        pass

    def setFont(self, Font=None):
        pass

    def setForeground(self, Color=None):
        pass

    def setHorizontalScrollBar(self, JScrollBar=None):
        pass

    def setHorizontalScrollBarPolicy(self, int=None):
        pass

    def setIgnoreRepaint(self, boolean=None):
        pass

    def setInheritsPopupMenu(self, boolean=None):
        pass

    def setInputMap(self, int=None, InputMap1=None):
        pass

    def setInputVerifier(self, InputVerifier=None):
        pass

    def setLayout(self, LayoutManager=None):
        pass

    def setLocale(self, Locale=None):
        pass

    def setLocation(self, int=None, int1=None):
        pass

    def setMaximumSize(self, Dimension=None):
        pass

    def setMinimumSize(self, Dimension=None):
        pass

    def setMixingCutoutShape(self, Shape=None):
        pass

    def setName(self, String=None):
        pass

    def setNextFocusableComponent(self, Component=None):
        pass

    def setOpaque(self, boolean=None):
        pass

    def setPreferredSize(self, Dimension=None):
        pass

    def setRequestFocusEnabled(self, boolean=None):
        pass

    def setRowHeader(self, JViewport=None):
        pass

    def setRowHeaderView(self, Component=None):
        pass

    def setSize(self, int=None, int1=None):
        pass

    def setToolTipText(self, String=None):
        pass

    def setTransferHandler(self, TransferHandler=None):
        pass

    def setUI(self, ScrollPaneUI=None):
        pass

    def setVerifyInputWhenFocusTarget(self, boolean=None):
        pass

    def setVerticalScrollBar(self, JScrollBar=None):
        pass

    def setVerticalScrollBarPolicy(self, int=None):
        pass

    def setViewport(self, JViewport=None):
        pass

    def setViewportBorder(self, Border=None):
        pass

    def setViewportView(self, Component=None):
        pass

    def setVisible(self, boolean=None):
        pass

    def setWheelScrollingEnabled(self, boolean=None):
        pass

    def show(self, boolean=None):
        pass

    def size(self, ):
        pass

    def toString(self, ):
        pass

    def transferFocus(self, ):
        pass

    def transferFocusBackward(self, ):
        pass

    def transferFocusDownCycle(self, ):
        pass

    def transferFocusUpCycle(self, ):
        pass

    def unregisterKeyboardAction(self, KeyStroke=None):
        pass

    def update(self, Graphics=None):
        pass

    def updateUI(self, ):
        pass

    def validate(self, ):
        pass

class LayoutStyle(object):

    class ComponentPlacement(object):
        INDENT = None
        RELATED = None
        UNRELATED = None
    
        class EnumDesc(object):
        
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

    def equals(self, Object=None):
        pass

    def getClass(self, ):
        pass

    def getContainerGap(self, JComponent=None, int1=None, Container2=None):
        pass

    @staticmethod
    def getInstance():
        pass

    def getPreferredGap(self, JComponent=None, JComponent1=None, ComponentPlacement2=None, int3=None, Container4=None):
        pass

    @staticmethod
    def setInstance(LayoutStyle=None):
        pass

    def toString(self, ):
        pass

class SwingUtilities(object):
    BOTTOM = None
    CENTER = None
    EAST = None
    HORIZONTAL = None
    LEADING = None
    LEFT = None
    NEXT = None
    NORTH = None
    NORTH_EAST = None
    NORTH_WEST = None
    PREVIOUS = None
    RIGHT = None
    SOUTH = None
    SOUTH_EAST = None
    SOUTH_WEST = None
    TOP = None
    TRAILING = None
    VERTICAL = None
    WEST = None

    @staticmethod
    def calculateInnerArea(JComponent=None, Rectangle1=None):
        pass

    @staticmethod
    def computeDifference(Rectangle=None, Rectangle1=None):
        pass

    @staticmethod
    def computeIntersection(int=None, int1=None, int2=None, int3=None, Rectangle4=None):
        pass

    @staticmethod
    def computeStringWidth(FontMetrics=None, String1=None):
        pass

    @staticmethod
    def computeUnion(int=None, int1=None, int2=None, int3=None, Rectangle4=None):
        pass

    @staticmethod
    def convertMouseEvent(Component=None, MouseEvent1=None, Component2=None):
        pass

    @staticmethod
    def convertPoint(Component=None, int1=None, int2=None, Component3=None):
        pass

    @staticmethod
    def convertPointFromScreen(Point=None, Component1=None):
        pass

    @staticmethod
    def convertPointToScreen(Point=None, Component1=None):
        pass

    @staticmethod
    def convertRectangle(Component=None, Rectangle1=None, Component2=None):
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def findFocusOwner(Component=None):
        pass

    @staticmethod
    def getAccessibleAt(Component=None, Point1=None):
        pass

    @staticmethod
    def getAccessibleChild(Component=None, int1=None):
        pass

    @staticmethod
    def getAccessibleChildrenCount(Component=None):
        pass

    @staticmethod
    def getAccessibleIndexInParent(Component=None):
        pass

    @staticmethod
    def getAccessibleStateSet(Component=None):
        pass

    @staticmethod
    def getAncestorNamed(String=None, Component1=None):
        pass

    @staticmethod
    def getAncestorOfClass(Class=None, Component1=None):
        pass

    def getClass(self, ):
        pass

    @staticmethod
    def getDeepestComponentAt(Component=None, int1=None, int2=None):
        pass

    @staticmethod
    def getLocalBounds(Component=None):
        pass

    @staticmethod
    def getRoot(Component=None):
        pass

    @staticmethod
    def getRootPane(Component=None):
        pass

    @staticmethod
    def getUIActionMap(JComponent=None):
        pass

    @staticmethod
    def getUIInputMap(JComponent=None, int1=None):
        pass

    @staticmethod
    def getUnwrappedParent(Component=None):
        pass

    @staticmethod
    def getUnwrappedView(JViewport=None):
        pass

    @staticmethod
    def getWindowAncestor(Component=None):
        pass

    @staticmethod
    def invokeAndWait(Runnable=None):
        pass

    @staticmethod
    def invokeLater(Runnable=None):
        pass

    @staticmethod
    def isDescendingFrom(Component=None, Component1=None):
        pass

    @staticmethod
    def isEventDispatchThread():
        pass

    @staticmethod
    def isLeftMouseButton(MouseEvent=None):
        pass

    @staticmethod
    def isMiddleMouseButton(MouseEvent=None):
        pass

    @staticmethod
    def isRectangleContainingRectangle(Rectangle=None, Rectangle1=None):
        pass

    @staticmethod
    def isRightMouseButton(MouseEvent=None):
        pass

    @staticmethod
    def layoutCompoundLabel(JComponent=None, FontMetrics1=None, String2=None, Icon3=None, int4=None, int5=None, int6=None, int7=None, Rectangle8=None, Rectangle9=None, Rectangle10=None, int11=None):
        pass

    @staticmethod
    def notifyAction(Action=None, KeyStroke1=None, KeyEvent2=None, Object3=None, int4=None):
        pass

    @staticmethod
    def paintComponent(Graphics=None, Component1=None, Container2=None, int3=None, int4=None, int5=None, int6=None):
        pass

    @staticmethod
    def processKeyBindings(KeyEvent=None):
        pass

    @staticmethod
    def replaceUIActionMap(JComponent=None, ActionMap1=None):
        pass

    @staticmethod
    def replaceUIInputMap(JComponent=None, int1=None, InputMap2=None):
        pass

    def toString(self, ):
        pass

    @staticmethod
    def updateComponentTreeUI(Component=None):
        pass

    @staticmethod
    def windowForComponent(Component=None):
        pass

class SwingWorker(object):

    class StateValue(object):
        DONE = None
        PENDING = None
        STARTED = None
    
        class EnumDesc(object):
        
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

    def addPropertyChangeListener(self, PropertyChangeListener=None):
        pass

    def cancel(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    def exceptionNow(self, ):
        pass

    def execute(self, ):
        pass

    def firePropertyChange(self, String=None, Object1=None, Object2=None):
        pass

    def get(self, long=None, TimeUnit1=None):
        pass

    def getClass(self, ):
        pass

    def getProgress(self, ):
        pass

    def getPropertyChangeSupport(self, ):
        pass

    def getState(self, ):
        pass

    def isCancelled(self, ):
        pass

    def isDone(self, ):
        pass

    def removePropertyChangeListener(self, PropertyChangeListener=None):
        pass

    def resultNow(self, ):
        pass

    def run(self, ):
        pass

    def state(self, ):
        pass

    def toString(self, ):
        pass

class WindowConstants(object):
    DISPOSE_ON_CLOSE = None
    DO_NOTHING_ON_CLOSE = None
    EXIT_ON_CLOSE = None
    HIDE_ON_CLOSE = None

