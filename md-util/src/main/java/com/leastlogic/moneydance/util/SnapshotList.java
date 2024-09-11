/*
 * Created on Oct 20, 2018
 */
package com.leastlogic.moneydance.util;

import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

import java.time.LocalDate;
import java.util.TreeMap;

/**
 * Utility class to house a list of snapshots for a Moneydance security.
 */
public class SnapshotList {

	private final CurrencyType security;
	private final TreeMap<Integer, CurrencySnapshot> snapshots = new TreeMap<>();

	/**
	 * Sole constructor.
	 *
	 * @param security The Moneydance security for this instance
	 */
	public SnapshotList(CurrencyType security) {
		this.security = security;

      security.getSnapshots().forEach(snapShot ->
			this.snapshots.put(snapShot.getDateInt(), snapShot));

	} // end (CurrencyType) constructor

	/**
	 * @param dateInt The desired date
	 * @return The currency snapshot for our security on the specified date
	 */
	public CurrencySnapshot getSnapshotForDate(int dateInt) {
		Integer snapshotDate = this.snapshots.floorKey(dateInt);

		return snapshotDate == null ? null : this.snapshots.get(snapshotDate);
	} // end getSnapshotForDate(int)

	/**
	 * @return The last currency snapshot for our security before, or on, today
	 */
	public CurrencySnapshot getTodaysSnapshot() {
		int today = MdUtil.convLocalToDateInt(LocalDate.now());

		return getSnapshotForDate(today);
	} // end getTodaysSnapshot()

	/**
	 * @return Our Moneydance security
	 */
	public CurrencyType getSecurity() {

		return this.security;
	} // end getSecurity()

	/**
	 * @return A string representation of this SnapshotList
	 */
	public String toString() {

		return this.security.getTickerSymbol() + '[' + this.snapshots.size() + ']';
	} // end toString()

} // end class SnapshotList
