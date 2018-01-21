/*
 * Created on Jan 20, 2018
 */
package com.johns.moneydance.util;

/**
 * Class to house exceptions.
 */
public class MduException extends Exception {

	private static final long serialVersionUID = -8584381819668318356L;

	/**
	 * @param cause Exception that caused this (null if none)
	 * @param formatMessage Format string for the detail message
	 * @param params Optional parameters for the detail message
	 */
	public MduException(Throwable cause, String formatMessage, Object... params) {
		super(String.format(formatMessage, params), cause);

	} // end (Throwable, String, Object...) constructor

} // end class MduException
