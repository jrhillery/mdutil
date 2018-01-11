/*
 * Created on Jan 10, 2018
 */
package com.johns.moneydance.util;

import static java.math.RoundingMode.HALF_EVEN;

import java.math.BigDecimal;
import java.text.NumberFormat;
import java.time.LocalDate;
import java.util.Enumeration;
import java.util.List;
import java.util.ResourceBundle;

import com.infinitekind.moneydance.model.Account;
import com.infinitekind.moneydance.model.AcctFilter;
import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

/**
 * Collection of common utility methods handy for Moneydance extensions.
 */
public class MdUtil {
	private static final double[] centMult = { 1, 10, 100, 1000, 10000 };

	/**
	 * @param security
	 * @param latestSnapshot
	 * @param priceFmt
	 * @return the price in latestSnapshot
	 */
	public static double validateCurrentUserRate(CurrencyType security,
			CurrencySnapshot latestSnapshot, NumberFormat priceFmt) {
		double price = convRateToPrice(latestSnapshot.getUserRate());
		double oldPrice = convRateToPrice(security.getUserRate());

		if (price != oldPrice) {
			security.setUserRate(latestSnapshot.getUserRate());

			System.err.format("Changed security %s current price from %s to %s.%n",
				security.getName(), priceFmt.format(oldPrice), priceFmt.format(price));
		}

		return price;
	} // end validateCurrentUserRate(CurrencyType, CurrencySnapshot, NumberFormat)

	/**
	 * @param rate the Moneydance currency rate for a security
	 * @return the security price rounded to the tenth place past the decimal point
	 */
	public static double convRateToPrice(double rate) {

		return roundPrice(1 / rate);
	} // end convRateToPrice(double)

	/**
	 * @param price
	 * @return price rounded to the tenth place past the decimal point
	 */
	public static double roundPrice(double price) {
		BigDecimal bd = BigDecimal.valueOf(price);

		return bd.setScale(10, HALF_EVEN).doubleValue();
	} // end roundPrice(double)

	/**
	 * @param dateInt the numeric date value in decimal form YYYYMMDD
	 * @return the corresponding local date
	 */
	public static LocalDate convDateIntToLocal(int dateInt) {
		int year = dateInt / 10000;
		int month = (dateInt % 10000) / 100;
		int dayOfMonth = dateInt % 100;

		return LocalDate.of(year, month, dayOfMonth);
	} // end convDateIntToLocal(int)

	/**
	 * @param date the local date value
	 * @return the corresponding numeric date value in decimal form YYYYMMDD
	 */
	public static int convLocalToDateInt(LocalDate date) {
		int dateInt = date.getYear() * 10000
				+ date.getMonthValue() * 100
				+ date.getDayOfMonth();

		return dateInt;
	} // end convLocalToDateInt(LocalDate)

	/**
	 * @param security the Moneydance security
	 * @return the last currency snap shot for the supplied security
	 */
	public static CurrencySnapshot getLatestSnapshot(CurrencyType security) {
		List<CurrencySnapshot> snapShots = security.getSnapshots();

		return snapShots.get(snapShots.size() - 1);
	} // end getLatestSnapshot(CurrencyType)

	/**
	 * @param account the parent account
	 * @param securityName
	 * @return the Moneydance security subaccount with the specified name
	 */
	public static Account getSubAccountByName(Account account, String securityName) {
		List<Account> subs = account.getSubAccounts(new AcctFilter() {

			public boolean matches(Account acct) {
				String acctName = acct.getAccountName();

				return acctName.equalsIgnoreCase(securityName);
			} // end matches(Account)

			public String format(Account acct) {

				return acct.getFullAccountName();
			} // end format(Account)
		}); // end new AcctFilter() {...}

		return subs == null || subs.isEmpty() ? null : subs.get(0);
	} // end getSubAccountByName(Account, String)

	/**
	 * @param account the root account
	 * @param accountNum
	 * @return the Moneydance investment account with the specified number
	 */
	public static Account getSubAccountByInvestNumber(Account account, String accountNum) {
		List<Account> subs = account.getSubAccounts(new AcctFilter() {

			public boolean matches(Account acct) {
				String acctNum = acct.getInvestAccountNumber();

				return acctNum.equalsIgnoreCase(accountNum);
			} // end matches(Account)

			public String format(Account acct) {

				return acct.getFullAccountName();
			} // end format(Account)
		}); // end new AcctFilter() {...}

		return subs == null || subs.isEmpty() ? null : subs.get(0);
	} // end getSubAccountByInvestNumber(Account, String)

	/**
	 * @param account
	 * @return the current account balance
	 */
	public static double getCurrentBalance(Account account) {
		int decimalPlaces = account.getCurrencyType().getDecimalPlaces();

		return account.getUserCurrentBalance() / centMult[decimalPlaces];
	} // end getCurrentBalance(Account)

	/**
	 * @param baseBundleName
	 * @return a resource bundle instance for the specified base bundle name
	 */
	public static ResourceBundle getMsgBundle(String baseBundleName) {
		ResourceBundle messageBundle;

		try {
			messageBundle = ResourceBundle.getBundle(baseBundleName);
		} catch (Exception e) {
			System.err.format("Unable to load message bundle %s. %s%n", baseBundleName, e);

			messageBundle = new ResourceBundle() {
				protected Object handleGetObject(String key) {
					// just use the key since we have no message bundle
					return key;
				}

				public Enumeration<String> getKeys() {
					return null;
				}
			}; // end new ResourceBundle() {...}
		} // end catch

		return messageBundle;
	} // end getMsgBundle(String)

} // end class MdUtil
