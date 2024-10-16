/*
 * Created on Oct 20, 2018
 */
package com.leastlogic.moneydance.util;

import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.Optional;
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
	 * @return Optional currency snapshot for our security on the specified date
	 */
	public Optional<CurrencySnapshot> getSnapshotForDate(int dateInt) {

		return Optional.ofNullable(this.snapshots.floorKey(dateInt)).map(this.snapshots::get);
	} // end getSnapshotForDate(int)

	/**
	 * @return Optional last currency snapshot for our security before, or on, today
	 */
	public Optional<CurrencySnapshot> getTodaysSnapshot() {
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
	 * @param snapshot Currency snapshot to use
	 * @return The security price for the given snapshot
	 */
	public static BigDecimal getPrice(CurrencySnapshot snapshot) {

		return MdUtil.convRateToPrice(snapshot.getRate());
	} // end getPrice(CurrencySnapshot)

	/**
	 * @return A string representation of this SnapshotList
	 */
	public String toString() {

		return this.security.getTickerSymbol() + '[' + this.snapshots.size() + ']';
	} // end toString()

} // end class SnapshotList
