# encoding: utf-8
# module __init__.py
class HTMLPane:
    ABORT = None
    ALLBITS = None
    BOTTOM_ALIGNMENT = None
    CENTER_ALIGNMENT = None
    DEFAULT_KEYMAP = None
    ERROR = None
    FOCUS_ACCELERATOR_KEY = None
    FRAMEBITS = None
    HEIGHT = None
    HONOR_DISPLAY_PROPERTIES = None
    LEFT_ALIGNMENT = None
    PROPERTIES = None
    RIGHT_ALIGNMENT = None
    SOMEBITS = None
    TOOL_TIP_TEXT_KEY = None
    TOP_ALIGNMENT = None
    UNDEFINED_CONDITION = None
    W3C_LENGTH_UNITS = None
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT = None
    WHEN_FOCUSED = None
    WHEN_IN_FOCUSED_WINDOW = None
    WIDTH = None

    def action(self, Event=None, Object1=None):
        pass

    def add(self, Component=None, Object1=None, int2=None):
        pass

    def addAncestorListener(self, AncestorListener=None):
        pass

    def addCaretListener(self, CaretListener=None):
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

    def addHyperlinkListener(self, HyperlinkListener=None):
        pass

    def addInputMethodListener(self, InputMethodListener=None):
        pass

    def addKeyListener(self, KeyListener=None):
        pass

    @staticmethod
    def addKeymap(String=None, Keymap1=None):
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

    def addText(self, String=None):
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

    def clearText(self, ):
        pass

    def computeVisibleRect(self, Rectangle=None):
        pass

    def contains(self, int=None, int1=None):
        pass

    def copy(self, ):
        pass

    def countComponents(self, ):
        pass

    @staticmethod
    def createEditorKitForContentType(String=None):
        pass

    def createImage(self, int=None, int1=None):
        pass

    def createToolTip(self, ):
        pass

    def createVolatileImage(self, int=None, int1=None, ImageCapabilities2=None):
        pass

    def cut(self, ):
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

    def fireHyperlinkUpdate(self, HyperlinkEvent=None):
        pass

    def firePropertyChange(self, String=None, byte1=None, byte2=None):
        pass

    def getAccessibleContext(self, ):
        pass

    def getActionForKeyStroke(self, KeyStroke=None):
        pass

    def getActionMap(self, ):
        pass

    def getActions(self, ):
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

    def getCaret(self, ):
        pass

    def getCaretColor(self, ):
        pass

    def getCaretListeners(self, ):
        pass

    def getCaretPosition(self, ):
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

    def getContentType(self, ):
        pass

    def getCursor(self, ):
        pass

    def getDebugGraphicsOptions(self, ):
        pass

    @staticmethod
    def getDefaultLocale():
        pass

    def getDisabledTextColor(self, ):
        pass

    def getDocument(self, ):
        pass

    def getDragEnabled(self, ):
        pass

    def getDropLocation(self, ):
        pass

    def getDropMode(self, ):
        pass

    def getDropTarget(self, ):
        pass

    def getEditorKit(self, ):
        pass

    @staticmethod
    def getEditorKitClassNameForContentType(String=None):
        pass

    def getEditorKitForContentType(self, String=None):
        pass

    def getFocusAccelerator(self, ):
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

    def getHighlighter(self, ):
        pass

    def getHyperlinkListeners(self, ):
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

    @staticmethod
    def getKeymap(String=None):
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

    def getNavigationFilter(self, ):
        pass

    def getNextFocusableComponent(self, ):
        pass

    def getPage(self, ):
        pass

    def getParent(self, ):
        pass

    def getPopupLocation(self, MouseEvent=None):
        pass

    def getPreferredScrollableViewportSize(self, ):
        pass

    def getPreferredSize(self, ):
        pass

    def getPrintable(self, MessageFormat=None, MessageFormat1=None):
        pass

    def getPropertyChangeListeners(self, String=None):
        pass

    def getRegisteredKeyStrokes(self, ):
        pass

    def getRootPane(self, ):
        pass

    def getScrollableBlockIncrement(self, Rectangle=None, int1=None, int2=None):
        pass

    def getScrollableTracksViewportHeight(self, ):
        pass

    def getScrollableTracksViewportWidth(self, ):
        pass

    def getScrollableUnitIncrement(self, Rectangle=None, int1=None, int2=None):
        pass

    def getSelectedText(self, ):
        pass

    def getSelectedTextColor(self, ):
        pass

    def getSelectionColor(self, ):
        pass

    def getSelectionEnd(self, ):
        pass

    def getSelectionStart(self, ):
        pass

    def getSize(self, Dimension=None):
        pass

    @staticmethod
    def getSpanCl(BigDecimal=None, BigDecimal1=None):
        pass

    def getText(self, int=None, int1=None):
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

    def isEditable(self, ):
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

    @staticmethod
    def loadKeymap(Keymap=None, KeyBinding1=None, Action2=None):
        pass

    def locate(self, int=None, int1=None):
        pass

    def location(self, ):
        pass

    def lostFocus(self, Event=None, Object1=None):
        pass

    def minimumSize(self, ):
        pass

    def modelToView(self, int=None):
        pass

    def modelToView2D(self, int=None):
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

    def moveCaretPosition(self, int=None):
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

    def paste(self, ):
        pass

    def postEvent(self, Event=None):
        pass

    def preferredSize(self, ):
        pass

    def prepareImage(self, Image=None, int1=None, int2=None, ImageObserver3=None):
        pass

    def print(self, MessageFormat=None, MessageFormat1=None, boolean2=None, PrintService3=None, PrintRequestAttributeSet4=None, boolean5=None):
        pass

    def printAll(self, Graphics=None):
        pass

    def printComponents(self, Graphics=None):
        pass

    def putClientProperty(self, Object=None, Object1=None):
        pass

    def read(self, InputStream=None, Object1=None):
        pass

    @staticmethod
    def readResourceImage(String=None, Class1=None):
        pass

    @staticmethod
    def reduceHeight(JComponent=None, int1=None):
        pass

    @staticmethod
    def registerEditorKitForContentType(String=None, String1=None, ClassLoader2=None):
        pass

    def registerKeyboardAction(self, ActionListener=None, String1=None, KeyStroke2=None, int3=None):
        pass

    def remove(self, MenuComponent=None):
        pass

    def removeAll(self, ):
        pass

    def removeAncestorListener(self, AncestorListener=None):
        pass

    def removeCaretListener(self, CaretListener=None):
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

    def removeHyperlinkListener(self, HyperlinkListener=None):
        pass

    def removeInputMethodListener(self, InputMethodListener=None):
        pass

    def removeKeyListener(self, KeyListener=None):
        pass

    @staticmethod
    def removeKeymap(String=None):
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

    def replaceSelection(self, String=None):
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

    def scrollToReference(self, String=None):
        pass

    def select(self, int=None, int1=None):
        pass

    def selectAll(self, ):
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

    def setCaret(self, Caret=None):
        pass

    def setCaretColor(self, Color=None):
        pass

    def setCaretPosition(self, int=None):
        pass

    def setComponentOrientation(self, ComponentOrientation=None):
        pass

    def setComponentPopupMenu(self, JPopupMenu=None):
        pass

    def setComponentZOrder(self, Component=None, int1=None):
        pass

    def setContentType(self, String=None):
        pass

    def setCursor(self, Cursor=None):
        pass

    def setDebugGraphicsOptions(self, int=None):
        pass

    @staticmethod
    def setDefaultLocale(Locale=None):
        pass

    def setDisabledTextColor(self, Color=None):
        pass

    def setDocument(self, Document=None):
        pass

    def setDoubleBuffered(self, boolean=None):
        pass

    def setDragEnabled(self, boolean=None):
        pass

    def setDropMode(self, DropMode=None):
        pass

    def setDropTarget(self, DropTarget=None):
        pass

    def setEditable(self, boolean=None):
        pass

    def setEditorKit(self, EditorKit=None):
        pass

    def setEditorKitForContentType(self, String=None, EditorKit1=None):
        pass

    def setEnabled(self, boolean=None):
        pass

    def setFocusAccelerator(self, char=None):
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

    def setHighlighter(self, Highlighter=None):
        pass

    def setIgnoreRepaint(self, boolean=None):
        pass

    def setInheritsPopupMenu(self, boolean=None):
        pass

    def setInputMap(self, int=None, InputMap1=None):
        pass

    def setInputVerifier(self, InputVerifier=None):
        pass

    def setKeymap(self, Keymap=None):
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

    def setName(self, String=None):
        pass

    def setNavigationFilter(self, NavigationFilter=None):
        pass

    def setNextFocusableComponent(self, Component=None):
        pass

    def setOpaque(self, boolean=None):
        pass

    def setPage(self, String=None):
        pass

    def setPreferredSize(self, Dimension=None):
        pass

    def setRequestFocusEnabled(self, boolean=None):
        pass

    def setSelectedTextColor(self, Color=None):
        pass

    def setSelectionColor(self, Color=None):
        pass

    def setSelectionEnd(self, int=None):
        pass

    def setSelectionStart(self, int=None):
        pass

    def setSize(self, int=None, int1=None):
        pass

    def setText(self, String=None):
        pass

    def setToolTipText(self, String=None):
        pass

    def setTransferHandler(self, TransferHandler=None):
        pass

    def setUI(self, TextUI=None):
        pass

    def setVerifyInputWhenFocusTarget(self, boolean=None):
        pass

    def setVisible(self, boolean=None):
        pass

    def show(self, boolean=None):
        pass

    def size(self, ):
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

    def viewToModel(self, Point=None):
        pass

    def viewToModel2D(self, Point2D=None):
        pass

    def write(self, Writer=None):
        pass
