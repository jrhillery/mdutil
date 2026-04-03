package com.moneydance.modules.features.nwsync;

import com.sun.star.comp.helper.BootstrapException;
import com.sun.star.uno.XComponentContext;
import ooo.connector.BootstrapSocketConnector;
import ooo.connector.server.OOoServer;

public class BootstrapSocketConnectorFix extends BootstrapSocketConnector {

    /**
     * Constructs a bootstrap socket connector which connects to the specified
     * OOo server.
     *
     * @param   oooServer   The OOo server
     */
    public BootstrapSocketConnectorFix(OOoServer oooServer) {

        super(oooServer);
    }

    /**
     * Connects to an OOo server using the specified host and port for the
     * socket and returns a component context for using the connection to the
     * OOo server.
     *
     * @param   host   The host
     * @param   port   The port
     * @return         The component context
     * @throws BootstrapException     If no service manager is found
     */
    public XComponentContext connect(String host, int port) throws BootstrapException {

        // host and port
        String hostAndPort = "host="+host+",port="+port;

        // accept option needs double dash
        String oooAcceptOption = "--accept=socket,"+hostAndPort+";urp;";

        // connection string
        String unoConnectString = "uno:socket,"+hostAndPort+";urp;StarOffice.ComponentContext";

        return connect(oooAcceptOption, unoConnectString);
    }

} // end class BootstrapSocketConnectorFix
