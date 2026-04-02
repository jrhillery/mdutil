/*
 * Created on Jan 21, 2018
 */
package io.github.jrhillery.mdimport;

import java.nio.file.Path;
import java.util.Locale;

public interface CsvProcessWindow {

	/**
	 * @return The file selected to import
	 */
	Path getFileToImport();

	/**
	 * @param text HTML-text to append to the output log text area
	 */
	void addText(String text);

	/**
	 * @return The Locale object that is associated with this window
	 */
	Locale getLocale();

	/**
	 * Store an object with resources to close.
	 *
	 * @param closeable The object managing closeable resources
	 */
	void addCloseableResource(AutoCloseable closeable);

} // end interface CsvProcessWindow
