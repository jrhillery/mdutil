package com.leastlogic.moneydance.util;

import java.util.Optional;

/**
 * An interface to manage staged changes.
 */
public interface StagedInterface {

   /**
    * Commit any staged changes.
    *
    * @return Optional summary of the changes committed
    */
   Optional<String> commitChanges();

   /**
    * @return True when we have uncommitted changes in memory
    */
   boolean isModified();

} // end interface StagedInterface
