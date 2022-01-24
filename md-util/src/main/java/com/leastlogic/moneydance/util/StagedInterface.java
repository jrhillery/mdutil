package com.leastlogic.moneydance.util;

/**
 * An interface to manage staged changes.
 */
public interface StagedInterface {

   /**
    * Commit any staged changes.
    *
    * @return A summary of the changes committed
    */
   String commitChanges();

   /**
    * @return True when we have uncommitted changes in memory
    */
   boolean isModified();

} // end interface StagedInterface
