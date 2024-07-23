package com.leastlogic.moneydance.util;

/**
 * Class to house small exceptions.
 */
public class MduExcepcionito extends Exception {

   /**
    * @param cause     Exception that caused this (null if none)
    * @param formatMsg Format string for the detail message
    * @param params    Optional parameters for the detail message
    */
   public MduExcepcionito(Throwable cause, String formatMsg, Object... params) {
      super(String.format(formatMsg, params), cause);

   } // end constructor

} // end class MduExcepcionito
