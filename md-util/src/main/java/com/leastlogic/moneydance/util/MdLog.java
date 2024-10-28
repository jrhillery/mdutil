package com.leastlogic.moneydance.util;

import com.infinitekind.util.AppDebug;

import java.util.function.Supplier;

public class MdLog {

    private static String prefix = "";

    /**
     * Set a message prefix for logging.
     * @param newPrefix Prefix to use
     */
    public static void setPrefix(String newPrefix) {
        prefix = newPrefix;

    } // end setPrefix(String)

    /**
     * Log into the Moneydance internal logging mechanism.
     * @param msg Message to log
     */
    public static void all(String msg) {
        AppDebug.ALL.log(prefix + msg);

    } // end all(String)

    /**
     * Log into the Moneydance internal logging mechanism.
     * @param msg Message to log
     * @param error Exception to detail with message
     */
    public static void all(String msg, Throwable error) {
        AppDebug.ALL.log(prefix + msg, error);

    } // end all(String, Throwable)

    /**
     * Log into the Moneydance internal logging mechanism when debug is enabled.
     * @param msg Message to log
     */
    public static void debug(String msg) {
        AppDebug.DEBUG.log(() -> prefix + msg);

    } // end debug(String)

    /**
     * Log into the Moneydance internal logging mechanism when debug is enabled.
     * The supplier can be a lambda, which is only called if debug is enabled.
     * @param msgSupplier Producer of a message to log
     */
    public static void debug(Supplier<String> msgSupplier) {
        AppDebug.DEBUG.log(() -> prefix + msgSupplier.get());

    } // end debug(Supplier<String>)

} // end class MdLog
