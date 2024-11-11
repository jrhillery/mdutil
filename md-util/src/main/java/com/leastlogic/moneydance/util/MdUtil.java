/*
 * Created on Jan 10, 2018
 */
package com.leastlogic.moneydance.util;

import static com.infinitekind.moneydance.model.Account.AccountType.ASSET;
import static java.math.RoundingMode.HALF_EVEN;

import java.io.InputStream;
import java.math.BigDecimal;
import java.math.MathContext;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.time.LocalDate;
import java.util.*;
import java.util.function.Consumer;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

import com.infinitekind.moneydance.model.*;
import com.infinitekind.moneydance.model.Account.AccountType;

/**
 * Collection of common utility methods handy for Moneydance extensions.
 */
public class MdUtil {

	public static final MathContext PRECISION_13 = new MathContext(13, HALF_EVEN);
	public static final String IBOND_TICKER_PREFIX = "IBond";

	/**
	 * Retrieve the price for this snapshot and validate the current price.
	 *
	 * @param security          The Moneydance security
	 * @param currentSnapshot   The current currency snapshot to use
	 * @param locale            Desired locale
	 * @param displayCorrection Lambda to consume any correction message
	 * @return The price for the supplied snapshot, as a BigDecimal
	 */
	public static BigDecimal getAndValidateCurrentSnapshotPrice(
			CurrencyType security, CurrencySnapshot currentSnapshot,
			Locale locale, Consumer<String> displayCorrection) {
		double rate = currentSnapshot.getRate();
		BigDecimal oldPrice = convRateToPrice(security.getRelativeRate());
		BigDecimal price = convRateToPrice(rate);

		if (price.compareTo(oldPrice) != 0) {
			security.setRelativeRate(rate);

			NumberFormat priceFmt = getCurrencyFormat(locale, oldPrice, price);
			displayCorrection.accept("Changed %s (%s) current price from %s to %s".formatted(
					security.getName(), security.getTickerSymbol(),
					priceFmt.format(oldPrice), priceFmt.format(price)));
		}

		return price;
	} // end getAndValidateCurrentSnapshotPrice(CurrencyType, CurrencySnapshot, Locale, Consumer<String>)

	/**
	 * @param rate The Moneydance currency rate for a security
	 * @return The security price rounded to 13 digit precision
	 */
	public static BigDecimal convRateToPrice(double rate) {

		return roundPrice(1 / rate);
	} // end convRateToPrice(double)

	/**
	 * @param price The price
	 * @return Price rounded to 13 digit precision
	 */
	public static BigDecimal roundPrice(double price) {
		BigDecimal bd = BigDecimal.valueOf(price);

        return bd.round(PRECISION_13);
	} // end roundPrice(double)

	/**
	 * Returns a currency format for the specified locale.
	 *
	 * @param locale Desired locale
	 * @param value1 First reference value
	 * @param value2 Second reference value
	 * @return A currency number format with the number of fraction digits in either value
	 */
	public static NumberFormat getCurrencyFormat(
			Locale locale, BigDecimal value1, BigDecimal value2) {
		DecimalFormat formatter = (DecimalFormat) NumberFormat.getCurrencyInstance(locale);
		formatter.setMinimumFractionDigits(Math.max(Math.max(
				value1.stripTrailingZeros().scale(),
				value2.stripTrailingZeros().scale()),
				2));

		return formatter;
	} // end getCurrencyFormat(Locale, BigDecimal, BigDecimal)

	/**
	 * @param locale Desired locale
	 * @param value1 First reference value
	 * @param value2 Second reference value
	 * @return A number format with the number of fraction digits in either value
	 */
	public static NumberFormat getNumberFormat(
			Locale locale, BigDecimal value1, BigDecimal value2) {
		DecimalFormat formatter = (DecimalFormat) NumberFormat.getNumberInstance(locale);
		formatter.setMinimumFractionDigits(Math.max(
				value1.stripTrailingZeros().scale(),
				value2.stripTrailingZeros().scale()));

		return formatter;
	} // end getNumberFormat(BigDecimal, BigDecimal)

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
	public static Stream<Account> getAccounts(AccountBook book, AccountType type) {
		Iterable<Account> accounts = () -> AccountUtil.getAccountIterator(book);

		return StreamSupport.stream(accounts.spliterator(), false)
			.filter(subAcct -> subAcct.getAccountType() == type);
	} // end getAccounts(AccountBook, AccountType)

	/**
	 * @param account      The parent account
	 * @param securityName Security name
	 * @return The Moneydance security subaccount with the specified name
	 */
	public static Optional<Account> getSubAccountByName(Account account, String securityName) {
		Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

		while (accounts.hasNext()) {
			Account subAcct = accounts.next();
			String acctName = subAcct.getAccountName();

			if (acctName.equalsIgnoreCase(securityName))
				return Optional.of(subAcct);
		}

		return Optional.empty();
	} // end getSubAccountByName(Account, String)

	/**
	 * @param account The root account
	 * @param acctNum Investment account number
	 * @return The Moneydance investment account with the specified number
	 */
	public static Optional<Account> getSubAccountByInvestNumber(Account account, String acctNum) {
		Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

		while (accounts.hasNext()) {
			Account subAcct = accounts.next();
			String accountNumber = subAcct.getInvestAccountNumber();

			if (accountNumber.equalsIgnoreCase(acctNum))
				return Optional.of(subAcct);
		}

		return Optional.empty();
	} // end getSubAccountByInvestNumber(Account, String)

	/**
	 * @param account Moneydance account
	 * @return The current account balance
	 */
	public static BigDecimal getCurrentBalance(Account account) {
		BigDecimal centBalance = BigDecimal.valueOf((account.getAccountType() == ASSET)
			? account.getRecursiveUserCurrentBalance()
			: account.getUserCurrentBalance());
		int decimalPlaces = account.getCurrencyType().getDecimalPlaces();

		return centBalance.movePointLeft(decimalPlaces);
	} // end getCurrentBalance(Account)

	/**
	 * @param txn Transaction to query
	 * @return The transaction amount
	 */
	public static BigDecimal getTxnAmount(SplitTxn txn) {
		Account parentAccount = txn.getParentTxn().getAccount();
		int decimalPlaces = parentAccount.getCurrencyType().getDecimalPlaces();

		return BigDecimal.valueOf(txn.getAmount()).movePointLeft(decimalPlaces);
	} // end getTxnAmount(SplitTxn)

	/**
	 * @param book    The root account for all transactions
	 * @param account Moneydance account to obtain the balance for
	 * @param date    Date to obtain the balance for
	 * @return Account balance as of the end of the date
	 */
	public static BigDecimal getBalanceAsOf(AccountBook book, Account account, LocalDate date) {
        BigDecimal centBalance = BigDecimal.valueOf(
			AccountUtil.getBalanceAsOfDate(book, account, convLocalToDateInt(date)));
		int decimalPlaces = account.getCurrencyType().getDecimalPlaces();

		return centBalance.movePointLeft(decimalPlaces);
	} // end getBalanceAsOf(AccountBook, Account, LocalDate)

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
			// recurse to get subaccount balances
			Iterator<Account> accounts = AccountUtil.getAccountIterator(account);

			accounts.forEachRemaining(subAcct -> {
				if (subAcct != account) {
					long[] subBalances = getCentBalancesAsOfDates(book, subAcct, asOfDates);

					for (int i = 0; i < centBalances.length; ++i) {
						centBalances[i] += subBalances[i];
					}
				}
			}); // end for each subaccount
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
	 * @param propsFileName Our properties file name
	 * @param srcClass      The class whose class loader will be used
	 * @return A properties instance with the specified file content
	 */
	public static Properties loadProps(String propsFileName, Class<?> srcClass)
			throws MduException {
		InputStream propsStream = srcClass.getClassLoader().getResourceAsStream(propsFileName);
		if (propsStream == null) {
			throw new MduException(null, "Unable to find properties %s on %s class path",
				propsFileName, srcClass);
		}

		Properties props = new Properties();
		try (propsStream) {
			props.load(propsStream);
		} // end try-with-resource propsStream
		catch (Exception e) {
			throw new MduException(e, "Exception loading properties %s", propsFileName);
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
