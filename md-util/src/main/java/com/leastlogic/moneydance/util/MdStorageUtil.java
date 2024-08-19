package com.leastlogic.moneydance.util;

import com.google.gson.Gson;

import java.util.Map;

/**
 * Utility class for dealing with Moneydance local storage. A reference to this
 * storage is returned by getContext().getCurrentAccountBook().getLocalStorage()
 */
public class MdStorageUtil {

   private final String folder;
   private final Map<String, String> localStorage;

   private final Gson gson = new Gson();

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
    * Remove persisted data object from the specified folder and file name.
    *
    * @param name file name
    */
   @SuppressWarnings("unused")
   public void remove(String name) {
      String key = this.folder + '.' + name;

      if (this.localStorage != null) {
         boolean contained = this.localStorage.containsKey(key);
         String dataStr = this.localStorage.remove(key);

         if (contained) {
            System.err.format("Removed %s (%s) from Moneydance local storage.%n",
               key, dataStr);
         }
      }

   } // end remove(String)

} // end class MdStorageUtil
