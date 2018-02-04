/*
 * Created on Jan 21, 2018
 */
package com.leastlogic.moneydance.util;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStream;
import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.Properties;
import java.util.ResourceBundle;

public abstract class CsvProcessor {
	protected CsvProcessWindow importWindow;
	protected Locale locale;
	private String propertiesFileName;

	private Map<String, String> csvRowMap = new LinkedHashMap<>();
	private Properties csvProps = null;
	private ResourceBundle msgBundle = null;

	private static final String baseMessageBundleName = "com.leastlogic.moneydance.util.MdUtilMessages";
	private static final char DOUBLE_QUOTE = '"';

	/**
	 * Sole constructor.
	 *
	 * @param importWindow
	 * @param propertiesFileName
	 */
	protected CsvProcessor(CsvProcessWindow importWindow, String propertiesFileName) {
		this.importWindow = importWindow;
		this.locale = importWindow.getLocale();
		this.propertiesFileName = propertiesFileName;

	} // end (CsvProcessWindow, Locale, String, String) constructor

	/**
	 * Import this row of the comma separated value file.
	 */
	abstract protected void processRow() throws MduException;

	/**
	 * Process each row in the selected comma separated value file.
	 */
	protected void processFile() throws MduException {
		BufferedReader reader = openFile();
		if (reader == null)
			return; // nothing to import

		try {
			String[] header = readLine(reader);

			while (hasMore(reader)) {
				String[] values = readLine(reader);

				if (header != null && values != null) {
					this.csvRowMap.clear();

					for (int i = 0; i < header.length; ++i) {
						if (i < values.length) {
							this.csvRowMap.put(header[i], values[i]);
						} else {
							this.csvRowMap.put(header[i], "");
						}
					} // end for

					processRow();
				}
			} // end while
		} finally {
			close(reader);
		}

	} // end processFile()

	/**
	 * @param propKey property key for column header
	 * @return value from the csv row map with any surrounding double quotes removed
	 */
	protected String stripQuotes(String propKey) throws MduException {
		String csvColumnKey = getCsvProps().getProperty(propKey);
		String val = this.csvRowMap.get(csvColumnKey);
		if (val == null) {
			// Unable to locate column %s (%s) in %s. Found columns %s
			throw asException(null, "MDUTL11", csvColumnKey, propKey,
				this.importWindow.getFileToImport(), this.csvRowMap.keySet());
		}
		int quoteLoc = val.indexOf(DOUBLE_QUOTE);

		if (quoteLoc == 0) {
			// starts with a double quote
			quoteLoc = val.lastIndexOf(DOUBLE_QUOTE);

			if (quoteLoc == val.length() - 1) {
				// also ends with a double quote => remove them
				val = val.substring(1, quoteLoc);
			}
		}

		return val.trim();
	} // end stripQuotes(String)

	/**
	 * @return a buffered reader to read from the file selected to import
	 */
	private BufferedReader openFile() {
		BufferedReader reader = null;
		try {
			reader = new BufferedReader(new FileReader(this.importWindow.getFileToImport()));
		} catch (Exception e) {
			// Exception opening file %s. %s
			writeFormatted("MDUTL12", this.importWindow.getFileToImport(), e);
		}

		return reader;
	} // end openFile()

	/**
	 * @param reader
	 * @return true when the next read will not block for input, false otherwise
	 */
	private boolean hasMore(BufferedReader reader) throws MduException {
		try {

			return reader.ready();
		} catch (Exception e) {
			// Exception checking file %s.
			throw asException(e, "MDUTL13", this.importWindow.getFileToImport());
		}
	} // end hasMore(BufferedReader)

	/**
	 * @param reader
	 * @return the comma separated tokens from the next line in the file
	 */
	private String[] readLine(BufferedReader reader) throws MduException {
		try {
			String line = reader.readLine();

			return line == null ? null : line.split(",");
		} catch (Exception e) {
			// Exception reading from file %s.
			throw asException(e, "MDUTL14", this.importWindow.getFileToImport());
		}
	} // end readLine(BufferedReader)

	/**
	 * Close the specified reader, ignoring any exceptions.
	 *
	 * @param reader
	 */
	private static void close(BufferedReader reader) {
		try {
			reader.close();
		} catch (Exception e) { /* ignore */ }

	} // end close(BufferedReader)

	/**
	 * @return our properties
	 */
	private Properties getCsvProps() throws MduException {
		if (this.csvProps == null) {
			InputStream propsStream = getClass().getClassLoader()
				.getResourceAsStream(this.propertiesFileName);
			if (propsStream == null)
				// Unable to find %s on the class path.
				throw asException(null, "MDUTL15", this.propertiesFileName);

			this.csvProps = new Properties();
			try {
				this.csvProps.load(propsStream);
			} catch (Exception e) {
				this.csvProps = null;

				// Exception loading %s.
				throw asException(e, "MDUTL16", this.propertiesFileName);
			} finally {
				try {
					propsStream.close();
				} catch (Exception e) { /* ignore */ }
			}
		}

		return this.csvProps;
	} // end getCsvProps()

	/**
	 * @return our message bundle
	 */
	private ResourceBundle getMsgBundle() {
		if (this.msgBundle == null) {
			this.msgBundle = MdUtil.getMsgBundle(baseMessageBundleName, this.locale);
		}

		return this.msgBundle;
	} // end getMsgBundle()

	/**
	 * @param cause Exception that caused this (null if none)
	 * @param key The resource bundle key (or message)
	 * @param params Optional parameters for the detail message
	 */
	private MduException asException(Throwable cause, String key, Object... params) {

		return new MduException(cause, retrieveMessage(key), params);
	} // end asException(Throwable, String, Object...)

	/**
	 * @param key The resource bundle key (or message)
	 * @return message for this key
	 */
	private String retrieveMessage(String key) {
		try {

			return getMsgBundle().getString(key);
		} catch (Exception e) {
			// just use the key when not found
			return key;
		}
	} // end retrieveMessage(String)

	/**
	 * @param key The resource bundle key (or message)
	 * @param params Optional array of parameters for the message
	 */
	private void writeFormatted(String key, Object... params) {
		this.importWindow.addText(String.format(this.locale, retrieveMessage(key), params));

	} // end writeFormatted(String, Object...)

	/**
	 * @param amount
	 * @return a currency number format with the number of fraction digits in amount
	 */
	protected NumberFormat getCurrencyFormat(BigDecimal amount) {
		DecimalFormat formatter = (DecimalFormat) NumberFormat.getCurrencyInstance(this.locale);
		int amtScale = amount.scale();

		if (amtScale < 2) {
			amtScale = 2; // some quotes omit the trailing zeros
		}
		formatter.setMinimumFractionDigits(amtScale);

		return formatter;
	} // end getCurrencyFormat(BigDecimal)

	/**
	 * @param value
	 * @return a number format with the number of fraction digits in value
	 */
	protected NumberFormat getNumberFormat(BigDecimal value) {
		DecimalFormat formatter = (DecimalFormat) NumberFormat.getNumberInstance(this.locale);
		formatter.setMinimumFractionDigits(value.scale());

		return formatter;
	} // end getNumberFormat(BigDecimal)

} // end class CsvProcessor
