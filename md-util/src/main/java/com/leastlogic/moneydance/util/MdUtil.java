/*
 * Created on Jan 10, 2018
 */
package com.leastlogic.moneydance.util;

import static com.infinitekind.moneydance.model.Account.AccountType.ASSET;
import static java.math.RoundingMode.HALF_EVEN;

import java.io.InputStream;
import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Iterator;
import java.util.List;
import java.util.Locale;
import java.util.NoSuchElementException;
import java.util.Properties;
import java.util.ResourceBundle;

import com.infinitekind.moneydance.model.Account;
import com.infinitekind.moneydance.model.Account.AccountType;
import com.infinitekind.moneydance.model.AccountBook;
import com.infinitekind.moneydance.model.AccountUtil;
import com.infinitekind.moneydance.model.CurrencySnapshot;
import com.infinitekind.moneydance.model.CurrencyType;

/**
 * Collection of common utility methods handy for Moneydance extensions.
 */
public class MdUtil {

	public static final String IBOND_TICKER_PREFIX = "IBond";

	/**
	 * @param security       The Moneydance security
	 * @param latestSnapshot The last currency snapshot for the supplied security
	 * @return The price in latestSnapshot
	 */
	public static BigDecimal validateCurrentUserRate(CurrencyType security,
			CurrencySnapshot latestSnapshot) {
		if (latestSnapshot == null)
			return BigDecimal.ONE; // default price to 1 when no snapshot

		BigDecimal price = convRateToPrice(latestSnapshot.getRate());
		BigDecimal oldPrice = convRateToPrice(security.getRelativeRate());

		if (price.compareTo(oldPrice) != 0) {
			security.setRelativeRate(latestSnapshot.getRate());
			DecimalFormat priceFmt = (DecimalFormat) NumberFormat.getCurrencyInstance();
			priceFmt.setMinimumFractionDigits(8);

			System.err.format("Changed security %s (%s) current price from %s to %s.%n",
				security.getName(), security.getTickerSymbol(), priceFmt.format(oldPrice),
				priceFmt.format(price));
		}

		return price;
	} // end validateCurrentUserRate(CurrencyType, CurrencySnapshot)

	/**
	 * @param rate The Moneydance currency rate for a security
	 * @return The security price rounded to the tenth place past the decimal point
	 */
	public static BigDecimal convRateToPrice(double rate) {

		return roundPrice(1 / rate);
	} // end convRateToPrice(double)

	/**
	 * @param price The price
	 * @return Price rounded to the tenth place past the decimal point
	 */
	public static BigDecimal roundPrice(double price) {
		BigDecimal bd = BigDecimal.valueOf(price);

		return bd.setScale(10, HALF_EVEN);
	} // end roundPrice(double)

	/**
	 * Returns a currency format for the specified locale.
	 *
	 * @param l Desired locale
	 * @param value Reference value
	 * @return A currency number format with the number of fraction digits in value
	 */
	public static NumberFormat getCurrencyFormat(Locale l, BigDecimal value) {
		DecimalFormat formatter = (DecimalFormat) NumberFormat.getCurrencyInstance(l);
		int valScale = value.scale();

		if (valScale < 2) {
			valScale = 2; // some quotes omit the trailing zeros
		}
		formatter.setMinimumFractionDigits(valScale);

		return formatter;
	} // end getCurrencyFormat(Locale, BigDecimal)

	/**
	 * @param dateInt The numeric date value in decimal form YYYYMMDD
	 * @return The corresponding local date
	 */
	public static LocalDate convDateIntToLocal(int dateInt) {
		int year = dateInt / 10000;
		int month = (dateInt % 10000) / 100;
		int dayOfMonth = dateInt % 100;

		return LocalDate.of(year, month, dayOfMonth);
	} // end convDateIntToLocal(int)

	/**
	 * @param date The local date value
	 * @return The corresponding numeric date value in decimal form YYYYMMDD
	 */
	public static int convLocalToDateInt(LocalDate date) {

		return date.getYear() * 10000
			+ date.getMonthValue() * 100
			+ date.getDayOfMonth();
	} // end convLocalToDateInt(LocalDate)

	/**
	 * @param book The overall container for the Moneydance data file
	 * @param type The type of accounts to return
	 * @return The Moneydance accounts with the specified type in the book
	 */
	public static List<Account> getAccounts(AccountBook book, AccountType type) {
		List<Account> subs = new ArrayList<>();
		Iterator<Account> accounts = AccountUtil.getAccountIterator(book);

		while (accounts.hasNext()) {
			Account subAcct = accounts.next();

			if (subAcct.getAccountType() == type)
				subs.add(subAcct);
		}

		return subs;
	} // end getAccounts(AccountBook, AccountType)

	/**
	 * @param account      The parent account
	 * @param securityName Security name
	 * @return The Moneydance security sub-account with the specified name
	 */
	public static Account getSubAccountByName(Account account, String securityName) {
		Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

		while (accounts.hasNext()) {
			Account subAcct = accounts.next();
			String acctName = subAcct.getAccountName();

			if (acctName.equalsIgnoreCase(securityName))
				return subAcct;
		}

		return null;
	} // end getSubAccountByName(Account, String)

	/**
	 * @param account    The root account
	 * @param accountNum Investment account number
	 * @return The Moneydance investment account with the specified number
	 */
	public static Account getSubAccountByInvestNumber(Account account, String accountNum) {
		Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

		while (accounts.hasNext()) {
			Account subAcct = accounts.next();
			String acctNum = subAcct.getInvestAccountNumber();

			if (acctNum.equalsIgnoreCase(accountNum))
				return subAcct;
		}

		return null;
	} // end getSubAccountByInvestNumber(Account, String)

	/**
	 * @param account Moneydance account
	 * @return The current account balance
	 */
	public static BigDecimal getCurrentBalance(Account account) {
		BigDecimal centBalance;

		if (account.getAccountType() == ASSET) {
			centBalance = BigDecimal.valueOf(account.getRecursiveUserCurrentBalance());
		} else {
			centBalance = BigDecimal.valueOf(account.getUserCurrentBalance());
		}
		int decimalPlaces = account.getCurrencyType().getDecimalPlaces();

		return centBalance.movePointLeft(decimalPlaces);
	} // end getCurrentBalance(Account)

	/**
	 * @param book      The root account for all transactions
	 * @param account   Moneydance account to obtain the balance for
	 * @param asOfDates The dates to obtain the balance for
	 * @return Account cent balances as of the end of each date in asOfDates
	 */
	private static long[] getCentBalancesAsOfDates(AccountBook book, Account account,
			int[] asOfDates) {
		long[] centBalances = AccountUtil.getBalancesAsOfDates(book, account, asOfDates);

		if (account.getAccountType() == ASSET) {
			// recurse to get sub-account balances
			Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

			while (accounts.hasNext()) {
				Account subAcct = accounts.next();

				if (subAcct != account) {
					long[] subBalances = getCentBalancesAsOfDates(book, subAcct, asOfDates);

					for (int i = 0; i < centBalances.length; ++i) {
						centBalances[i] += subBalances[i];
					}
				}
			}
		}

		return centBalances;
	} // end getCentBalancesAsOfDates(AccountBook, Account, int[])

	/**
	 * @param book      The root account for all transactions
	 * @param account   Moneydance account to obtain the balance for
	 * @param asOfDates The dates to obtain the balance for
	 * @return Account balances as of the end of each date in asOfDates
	 */
	public static BigDecimal[] getBalancesAsOfDates(AccountBook book, Account account,
			int[] asOfDates) {
		long[] centBalances = getCentBalancesAsOfDates(book, account, asOfDates);
		BigDecimal[] balances = new BigDecimal[centBalances.length];
		int decimalPlaces = account.getCurrencyType().getDecimalPlaces();

		for (int i = 0; i < balances.length; ++i) {
			BigDecimal centBalance = BigDecimal.valueOf(centBalances[i]);
			balances[i] = centBalance.movePointLeft(decimalPlaces);
		} // end for

		return balances;
	} // end getBalancesAsOfDates(AccountBook, Account, int[])

	/**
	 * @param baseBundleName The base name of the resource bundle, a fully qualified class name
	 * @param locale         The locale for which a resource bundle is desired
	 * @return A resource bundle instance for the specified base bundle name
	 */
	public static ResourceBundle getMsgBundle(String baseBundleName, Locale locale) {
		ResourceBundle messageBundle;

		try {
			messageBundle = ResourceBundle.getBundle(baseBundleName, locale);
		} catch (Exception e) {
			System.err.format(locale, "Unable to load message bundle %s. %s%n", baseBundleName, e);

			messageBundle = new ResourceBundle() {
				@SuppressWarnings("NullableProblems")
				protected Object handleGetObject(String key) {
					// just use the key since we have no message bundle
					return key;
				}

				@SuppressWarnings("NullableProblems")
				public Enumeration<String> getKeys() {
					return new Enumeration<>() {
						public boolean hasMoreElements() { return false; }
						public String nextElement() { throw new NoSuchElementException(); }
					};
				} // end getKeys()
			}; // end new ResourceBundle() {...}
		} // end catch

		return messageBundle;
	} // end getMsgBundle(String, Locale)

	/**
	 * @param propsFileName Our properties file name
	 * @param srcClass      The class whose class loader will be used
	 * @return A properties instance with the specified file content
	 */
	public static Properties loadProps(String propsFileName, Class<?> srcClass)
			throws MduException {
		InputStream propsStream = srcClass.getClassLoader().getResourceAsStream(propsFileName);
		if (propsStream == null) {
			throw new MduException(null, "Unable to find properties %s on %s class path.",
				propsFileName, srcClass);
		}

		Properties props = new Properties();
		try (propsStream) {
			props.load(propsStream);
		} // end try-with-resource propsStream
		catch (Exception e) {
			throw new MduException(e, "Exception loading properties %s.", propsFileName);
		}

		return props;
	} // end loadProps(String, Class<?>)

	/**
	 * Check if a ticker symbol matches our prefix for Series I savings
	 * bond ticker symbols, in the format IBondYYYYMM ignoring case.
	 *
	 * @param ticker Ticker symbol to check
	 * @return true when ticker is a valid I bond ticker symbol
	 */
	public static boolean isIBondTickerPrefix(String ticker) {

		return ticker != null
			&& IBOND_TICKER_PREFIX.regionMatches(true, 0, ticker, 0,
				IBOND_TICKER_PREFIX.length());
	} // end isIBondTickerPrefix(String)

} // end class MdUtil
