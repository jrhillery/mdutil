/*
 * Created on Oct 20, 2018
 */
package com.leastlogic.moneydance.util;

import java.util.Comparator;
import java.util.List;

import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

/**
 * Utility class to house a list of snapshots for a Moneydance security
 */
public class SnapshotList {

	private CurrencyType security;
	private List<CurrencySnapshot> snapshots;

	/**
	 * Sole constructor.
	 *
	 * @param security The Moneydance security for this instance
	 */
	public SnapshotList(CurrencyType security) {
		this.security = security;
		this.snapshots = getSnapshots(security);

	} // end (CurrencyType) constructor

	/**
	 * @param security The Moneydance security
	 * @return Sorted list of snapshots for the specified security
	 */
	private static List<CurrencySnapshot> getSnapshots(CurrencyType security) {
		List<CurrencySnapshot> snapShots = security.getSnapshots();
		snapShots.sort(Comparator.comparing(CurrencySnapshot::getDateInt));

		return snapShots;
	} // end getSnapshots(CurrencyType)

	/**
	 * @return The last currency snapshot for our security
	 */
	public CurrencySnapshot getLatestSnapshot() {

		if (this.snapshots.size() == 0)
			return null;
		else
			return this.snapshots.get(this.snapshots.size() - 1);
	} // end getLatestSnapshot()

	/**
	 * @param dateInt The desired date
	 * @return The currency snapshot for our security on the specified date
	 */
	public CurrencySnapshot getSnapshotForDate(int dateInt) {
		int index = this.snapshots.size();

		if (index == 0)
			return null;

		// start with the latest snapshot
		CurrencySnapshot candidate = this.snapshots.get(--index);
		MdUtil.validateCurrentUserRate(this.security, candidate);

		while (candidate.getDateInt() > dateInt && index > 0) {
			// examine the prior snapshot
			candidate = this.snapshots.get(--index);
		}

		return candidate;
	} // end getSnapshotForDate(int)

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
