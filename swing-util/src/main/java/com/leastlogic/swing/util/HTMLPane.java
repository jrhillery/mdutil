/*
 * Created on Jan 5, 2018
 */
package com.leastlogic.swing.util;

import static javax.swing.text.StyleConstants.NameAttribute;
import static javax.swing.text.html.HTML.Tag.BODY;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.image.BufferedImage;
import java.io.InputStream;
import java.io.Serial;
import java.math.BigDecimal;

import javax.imageio.ImageIO;
import javax.swing.JComponent;
import javax.swing.JEditorPane;
import javax.swing.text.Element;
import javax.swing.text.html.HTMLDocument;
import javax.swing.text.html.StyleSheet;

/**
 * Swing component with HTML output style control.
 */
public class HTMLPane extends JEditorPane {

	@SuppressWarnings("SpellCheckingInspection")
	private static final String CL_INCREASE = "incrs";
	@SuppressWarnings("SpellCheckingInspection")
	private static final String CL_DECREASE = "decrs";

	@Serial
	private static final long serialVersionUID = -1872591747328518613L;

	/**
	 * Sole constructor.
	 */
	public HTMLPane() {
		super("text/html", null);
		Color darkerColor = getBackground().darker().darker();
		setBackground(darkerColor);
		setEditable(false);
		HTMLDocument doc = (HTMLDocument) getDocument();
		StyleSheet ss = doc.getStyleSheet();
		ss.addRule("p { margin-top: 0; white-space: nowrap; }");
		ss.addRule("p { font-family: Tahoma, Geneva, sans-serif; font-size: 13pt; }");
		ss.addRule('.' + CL_INCREASE + " { color: rgb(0,217,0); }");
		ss.addRule('.' + CL_DECREASE + " { color: red; }");

	} // end () constructor

	/**
	 * @param text HTML-text to append to the output log text area
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
	 * @param doc An HTML document instance
	 * @return The body element of doc
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
	 * @param newPrice The new price
	 * @param oldPrice The old price
	 * @return the html class for the price change
	 */
	public static String getSpanCl(BigDecimal newPrice, BigDecimal oldPrice) {

		return switch (newPrice.compareTo(oldPrice)) {
			case 1 -> CL_INCREASE;
			case -1 -> CL_DECREASE;
			default -> "";
		};
	} // end getSpanCl(BigDecimal, BigDecimal)

	/**
	 * @param imgFileName The image file name
	 * @param srcClass    The class whose class loader will be used
	 * @return The named image from the class loader
	 */
	public static BufferedImage readResourceImage(String imgFileName, Class<?> srcClass) {
		BufferedImage image = null;
		InputStream imgStream = srcClass.getResourceAsStream(imgFileName);

		if (imgStream == null) {
			System.err.format("Unable to find image %s on %s class path.%n", imgFileName,
				srcClass);
		} else {
			try (imgStream) {
				image = ImageIO.read(imgStream);
			} // end try-with-resource imgStream
			catch (Exception e) {
				System.err.format("Exception reading image %s: %s%n", imgFileName, e);
			}
		}

		return image;
	} // end readResourceImage(String, Class<?>)

	/**
	 * Reduce the minimum, preferred and maximum size of the supplied button to a
	 * specified lower height.
	 *
	 * @param button      The button to change
	 * @param lowerHeight The maximum height for the result
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
