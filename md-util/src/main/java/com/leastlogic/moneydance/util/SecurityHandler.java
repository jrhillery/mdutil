/*
 * Created on Jan 20, 2018
 */
package com.leastlogic.moneydance.util;

import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

/**
 * This object handles deferred updates to a Moneydance security.
 */
public class SecurityHandler {
	private final SnapshotList snapshotList;
	private final CurrencyType security;

	private double newPrice = 0;
	private int newDate = 0;
	private long newVolume = 0;
	private double newHighPrice = 0;
	private double newLowPrice = 0;
	private boolean newCurrentPrice = true;

	/**
	 * Sole constructor.
	 *
	 * @param snapshotList The list of snapshots to use
	 */
	public SecurityHandler(SnapshotList snapshotList) {
		this.snapshotList = snapshotList;
		this.security = snapshotList.getSecurity();

	} // end (SnapshotList) constructor

	/**
	 * Store a deferred price quote for a specified date integer.
	 *
	 * @param newPrice Price quote
	 * @param newDate Date integer
	 * @return This instance
	 */
	public SecurityHandler storeNewPrice(double newPrice, int newDate) {
		this.newPrice = newPrice;
		this.newDate = newDate;

		return this;
	} // end storeNewPrice(double, int)

	/**
	 * Store a deferred price quote with volume, high and low prices too.
	 *
	 * @param newPrice Price quote
	 * @param newDate Date integer
	 * @param newVolume Daily volume
	 * @param newHighPrice Daily high price
	 * @param newLowPrice Daily low price
	 */
	public void storeNewPrice(double newPrice, int newDate, long newVolume,
			double newHighPrice, double newLowPrice) {
		this.newPrice = newPrice;
		this.newDate = newDate;
		this.newVolume = newVolume;
		this.newHighPrice = newHighPrice;
		this.newLowPrice = newLowPrice;

	} // end storeNewPrice(double, int, long, double, double)

	/**
	 * Mark that this security handler does not contain a current price.
	 * These are typically future prices; past prices are handled in applyUpdate.
	 */
	public void priceNotCurrent() {
		this.newCurrentPrice = false;

	} // end priceNotCurrent()

	/**
	 * Apply the stored update.
	 */
	public void applyUpdate() {
		CurrencySnapshot todaysSnapshot = this.snapshotList.getTodaysSnapshot();
		CurrencySnapshot newSnapshot = this.security.setSnapshotInt(this.newDate,
			1 / this.newPrice);

		if (this.newHighPrice > 0 && this.newLowPrice > 0) {
			newSnapshot.setDailyVolume(this.newVolume);
			newSnapshot.setDailyHigh(1 / this.newHighPrice);
			newSnapshot.setDailyLow(1 / this.newLowPrice);
		}
		newSnapshot.syncItem();

		if (this.newCurrentPrice) {
			if (todaysSnapshot == null || this.newDate >= todaysSnapshot.getDateInt()) {
				this.security.setRelativeRate(1 / this.newPrice);
			}
		}

	} // end applyUpdate()

	/**
	 * @return This handler's security
	 */
	public CurrencyType getSecurity() {

		return this.security;
	} // end getSecurity()

	/**
	 * @return A string representation of this SecurityHandler
	 */
	public String toString() {

		return this.security.getTickerSymbol() + ':' + this.newPrice;
	} // end toString()

} // end class SecurityHandler
