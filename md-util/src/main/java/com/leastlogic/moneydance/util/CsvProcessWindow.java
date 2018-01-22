/*
 * Created on Jan 21, 2018
 */
package com.leastlogic.moneydance.util;

import java.io.File;
import java.util.Locale;

public interface CsvProcessWindow {

	/**
	 * @return The file selected to import
	 */
	File getFileToImport();

	/**
	 * @param Text HTML text to append to the output log text area
	 */
	void addText(String text);

	/**
	 * @return The Locale object that is associated with this window
	 */
	Locale getLocale();

} // end interface CsvProcessWindow
