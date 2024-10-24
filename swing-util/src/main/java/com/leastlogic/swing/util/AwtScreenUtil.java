package com.leastlogic.swing.util;

import com.infinitekind.util.AppDebug;
import com.leastlogic.moneydance.util.MdStorageUtil;
import com.leastlogic.moneydance.util.MduException;

import java.awt.*;

public class AwtScreenUtil {
   private final Frame win;

   private static final String WIN_BOUNDS = "win.bounds";

   /**
    * Sole constructor.
    *
    * @param win Window to use
    */
   public AwtScreenUtil(Frame win) {
      this.win = win;

   } // end constructor

   /**
    * Retrieve the usable boundaries on the current screen.
    *
    * @return Rectangle with the usable boundaries
    */
   private Rectangle getUsableScreenBounds() {
      GraphicsConfiguration graphicsConfig = this.win.getGraphicsConfiguration();
      Rectangle bounds = graphicsConfig.getBounds();
      Insets insets = this.win.getToolkit().getScreenInsets(graphicsConfig);

      // allow 7 extra pixels on the left, right and bottom
      int overage = 7;
      insets.left -= overage;
      insets.right -= overage;
      insets.bottom -= overage;

      bounds.x += insets.left;
      bounds.y += insets.top;
      bounds.width -= insets.left + insets.right;
      bounds.height -= insets.top + insets.bottom;

      return bounds;
   } // end getUsableScreenBounds()

   /**
    * @param a value 'a'
    * @param b value 'b'
    * @return amount by which value 'a' exceeds value 'b'
    */
   private static int getExcessDelta(int a, int b) {

      return (a > b) ? a - b : 0;
   } // end getExcessDelta(int, int)

   /**
    * Adjust the bounding rectangle, so it fits on the usable area of the current screen.
    *
    * @param windowBounds bounding rectangle for a proposed Window
    */
   public void fitOnScreen(Rectangle windowBounds) {
      Rectangle screenBounds = getUsableScreenBounds();

      if (!screenBounds.contains(windowBounds)) {
         if (windowBounds.width > screenBounds.width)
            windowBounds.width = screenBounds.width;

         if (windowBounds.height > screenBounds.height)
            windowBounds.height = screenBounds.height;

         int dx = getExcessDelta(screenBounds.x, windowBounds.x);
         int dy = getExcessDelta(screenBounds.y, windowBounds.y);

         if (dx == 0)
            dx = -getExcessDelta(windowBounds.x + windowBounds.width,
                                 screenBounds.x + screenBounds.width);
         if (dy == 0)
            dy = -getExcessDelta(windowBounds.y + windowBounds.height,
                                 screenBounds.y + screenBounds.height);
         windowBounds.translate(dx, dy);
      }

   } // end fitOnScreen(Rectangle)

   /**
    * Store the size and location of the specified window as persistent values.
    *
    * @param mdStorage MdStorageUtil to use
    */
   public void persistWindowCoordinates(MdStorageUtil mdStorage) {

      try {
         if ((this.win.getExtendedState() & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH)
            // don't want to persist a maximized window's bounds
            this.win.setExtendedState(Frame.NORMAL);

         mdStorage.persistData(this.win.getBounds(), WIN_BOUNDS);
      } catch (MduException e) {
         AppDebug.ALL.log(e.getLocalizedMessage());
      }

   } // end persistWindowCoordinates(MdStorageUtil)

   /**
    * Set the size and location of the specified window to persisted values.
    *
    * @param mdStorage     MdStorageUtil to use
    * @param defaultWidth  default width to use
    * @param defaultHeight default height to use
    */
   public void setWindowCoordinates(MdStorageUtil mdStorage,
                                    int defaultWidth, int defaultHeight) {
      try {
         Rectangle windowBounds = mdStorage.retrieveData(WIN_BOUNDS, Rectangle.class);
         fitOnScreen(windowBounds);
         this.win.setBounds(windowBounds);
      } catch (MduException e) {
         AppDebug.ALL.log(e.getLocalizedMessage());
         this.win.setSize(defaultWidth, defaultHeight);
      }

   } // end setWindowCoordinates(MdStorageUtil, int, int)

} // end class AwtScreenUtil
