package com.leastlogic.moneydance.util;

import com.google.gson.Gson;

import java.awt.*;
import java.util.Map;

/**
 * Utility class for dealing with Moneydance local storage. A reference to this
 * storage is returned by getContext().getCurrentAccountBook().getLocalStorage()
 */
public class MdStorageUtil {

   private final String folder;
   private final Map<String, String> localStorage;

   private final Gson gson = new Gson();
   private static final String SIZE = "win.size";
   private static final String LOCATION = "win.location";

   /**
    * Sole constructor.
    *
    * @param folder       module folder name
    * @param localStorage Moneydance local storage
    */
   public MdStorageUtil(String folder, Map<String, String> localStorage) {
      this.folder = folder;
      this.localStorage = localStorage;

   } // end constructor

   /**
    * Store persistent data to the specified folder and file name.
    *
    * @param data data object to store
    * @param name file name
    */
   public void persistData(Object data, String name) throws MduException {
      String key = this.folder + '.' + name;
      String dataStr = this.gson.toJson(data);

      if (this.localStorage == null)
         throw new MduException(null, "No local storage present for %s: %s.", key, dataStr);

      this.localStorage.put(key, dataStr);

   } // end persistData(Object, String)

   /**
    * Retrieve persisted data object from the specified folder and file name.
    *
    * @param <T>      type of object to return
    * @param name     file name
    * @param classOfT class of return type
    * @return Specified persisted data object
    */
   public <T> T retrieveData(String name, Class<T> classOfT) throws MduException {
      String key = this.folder + '.' + name;

      if (this.localStorage == null)
         throw new MduException(null, "No local storage present with %s.", key);

      String dataStr = this.localStorage.get(key);

      if (dataStr == null)
         throw new MduException(null, "Persisted data not found for %s.", key);

      return this.gson.fromJson(dataStr, classOfT);
   } // end retrieveData(String, Class)

   /**
    * Store the size and location of the specified window as persistent values.
    *
    * @param win window to use
    */
   public void persistWindowCoordinates(Window win) {

      try {
         persistData(win.getSize(), SIZE);
         persistData(win.getLocation(), LOCATION);
      } catch (MduException e) {
         System.err.format("%s%n", e.getLocalizedMessage());
      }

   } // end persistWindowCoordinates(Window)

   /**
    * Set the size and location of the specified window to persisted values.
    *
    * @param win           window to set
    * @param defaultWidth  default width to use
    * @param defaultHeight default height to use
    */
   public void setWindowCoordinates(Window win, int defaultWidth, int defaultHeight) {
      try {
         win.setSize(retrieveData(SIZE, Dimension.class));
         win.setLocation(retrieveData(LOCATION, Point.class));
      } catch (MduException e) {
         System.err.format("%s%n", e.getLocalizedMessage());
         win.setSize(defaultWidth, defaultHeight);
      }

   } // end setWindowCoordinates(Window, int, int)

} // end class MdStorageUtil
