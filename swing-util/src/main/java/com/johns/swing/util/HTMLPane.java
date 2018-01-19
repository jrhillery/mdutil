/*
 * Created on Jan 5, 2018
 */
package com.johns.swing.util;

import static javax.swing.text.StyleConstants.NameAttribute;
import static javax.swing.text.html.HTML.Tag.BODY;

import java.awt.Dimension;

import javax.swing.JComponent;
import javax.swing.JEditorPane;
import javax.swing.text.Element;
import javax.swing.text.html.HTMLDocument;
import javax.swing.text.html.StyleSheet;

/**
 * Swing component with HTML output style control.
 */
public class HTMLPane extends JEditorPane {

	public static final String CL_INCREASE = "incrs";
	public static final String CL_DECREASE = "decrs";

	private static final long serialVersionUID = -1872591747328518613L;

	/**
	 * Sole constructor.
	 */
	public HTMLPane() {
		super("text/html", null);
		setEditable(false);
		HTMLDocument doc = (HTMLDocument) getDocument();
		StyleSheet ss = doc.getStyleSheet();
		ss.addRule("p { margin-top: 0; white-space: nowrap; }");
		ss.addRule("p { font-family: Tahoma, Geneva, sans-serif; font-size: small; }");
		ss.addRule('.' + CL_INCREASE + " { color: green; }");
		ss.addRule('.' + CL_DECREASE + " { color: rgb(221,0,0); }");

	} // end () constructor

	/**
	 * @param text HTML text to append to the output log text area
	 */
	public void addText(String text) {
		HTMLDocument doc = (HTMLDocument) getDocument();
		StringBuilder htmlText = new StringBuilder("<p>");
		htmlText.append(text);
		htmlText.append("</p>");
		try {
			if (doc.getLength() == 0) {
				doc.setInnerHTML(getBody(doc), htmlText.toString());
			} else {
				doc.insertBeforeEnd(getBody(doc), htmlText.toString());
			}
		} catch (Exception e) {
			e.printStackTrace(System.err);
		}

	} // end addText(String)

	/**
	 * @param doc
	 * @return the body element of doc
	 */
	private Element getBody(HTMLDocument doc) {
		Element root = doc.getDefaultRootElement();

		return doc.getElement(root, NameAttribute, BODY);
	} // end getBody(HTMLDocument)

	/**
	 * Clear the output log text area.
	 */
	public void clearText() {
		HTMLDocument doc = (HTMLDocument) getDocument();

		if (doc.getLength() > 0) {
			try {
				// show prior HTML content to help maintain this code
				getEditorKit().write(System.err, doc, 0, doc.getLength());
			} catch (Exception e) {
				e.printStackTrace(System.err);
			}
			try {
				doc.setInnerHTML(getBody(doc), "<p />");
			} catch (Exception e) {
				e.printStackTrace(System.err);
			}
		}

	} // end clearText()

	/**
	 * Reduce the minimum, preferred and maximum size of the supplied button to a
	 * specified lower height.
	 *
	 * @param button
	 * @param lowerHeight
	 */
	public static void reduceHeight(JComponent button, int lowerHeight) {
		Dimension buttonDim = button.getMinimumSize();

		if (buttonDim.height > lowerHeight) {
			buttonDim.height = lowerHeight;
			button.setMinimumSize(buttonDim);
		}
		buttonDim = button.getPreferredSize();

		if (buttonDim.height > lowerHeight) {
			buttonDim.height = lowerHeight;
			button.setPreferredSize(buttonDim);
		}
		buttonDim = button.getMaximumSize();

		if (buttonDim.height > lowerHeight) {
			buttonDim.height = lowerHeight;
			button.setMaximumSize(buttonDim);
		}

	} // end reduceHeight(JComponent, int)

} // end class HTMLPane
