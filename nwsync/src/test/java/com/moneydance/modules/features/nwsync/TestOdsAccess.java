package com.moneydance.modules.features.nwsync;

import io.github.jrhillery.moneydance.MdUtil;
import io.github.jrhillery.moneydance.MduException;
import com.sun.star.comp.helper.Bootstrap;
import com.sun.star.container.XEnumeration;
import com.sun.star.frame.XDesktop2;
import com.sun.star.frame.XModel;
import com.sun.star.lang.XMultiComponentFactory;
import com.sun.star.lang.XServiceInfo;
import com.sun.star.sheet.XSpreadsheetDocument;
import com.sun.star.uno.XComponentContext;
import ooo.connector.server.OOoServer;

import java.util.Arrays;
import java.util.List;
import java.util.Properties;

import static com.sun.star.uno.UnoRuntime.queryInterface;

public class TestOdsAccess {
    private static final String propertiesFileName = "nw-sync.properties";

    public static void main(String[] args) throws MduException {
        try {
            final String OFFICE_PATH = "office.install.path";
            final Properties nwSyncProps = MdUtil.loadProps(propertiesFileName, TestOdsAccess.class);
            String officeInstallPath = nwSyncProps.getProperty(OFFICE_PATH);
            if (officeInstallPath == null)
                throw new MduException(null, "Unable to obtain %s from %s on the class path",
                        OFFICE_PATH, propertiesFileName);

            XComponentContext remoteContext;
            try {
                List<String> oooOptions = Arrays.asList(Bootstrap.getDefaultOptions());
                remoteContext = new BootstrapSocketConnectorFix(
                        new OOoServer(officeInstallPath, oooOptions)).connect();
            } catch (Throwable e) {
                throw new MduException(e, "Exception obtaining office context");
            }
            if (remoteContext == null)
                throw new MduException(null, "Unable to obtain office context");

            XMultiComponentFactory remoteServiceMgr = remoteContext.getServiceManager();
            if (remoteServiceMgr == null)
                throw new MduException(null, "Unable to obtain office service manager");

            XDesktop2 libreOfficeDesktop;
            try {
                libreOfficeDesktop = queryInterface(XDesktop2.class, remoteServiceMgr
                        .createInstanceWithContext("com.sun.star.frame.Desktop", remoteContext));
            } catch (Exception e) {
                throw new MduException(e, "Exception obtaining office desktop");
            }
            if (libreOfficeDesktop == null)
                throw new MduException(null, "Unable to obtain office desktop");

            XEnumeration compItr = libreOfficeDesktop.getComponents().createEnumeration();

            if (!compItr.hasMoreElements()) {
                // no components so we probably started the desktop => terminate it
                libreOfficeDesktop.terminate();
            } else {
                do {
                    XServiceInfo comp = OdsAccessor.next(XServiceInfo.class, compItr);

                    if (comp.supportsService("com.sun.star.sheet.SpreadsheetDocument")) {
                        XSpreadsheetDocument doc = queryInterface(XSpreadsheetDocument.class, comp);
                        String urlString = queryInterface(XModel.class, doc).getURL();
                        System.out.println(urlString);
                    }
                } while (compItr.hasMoreElements());
            }
        } finally {
            OdsAccessor.closeOfficeConnection();
        }
        System.out.println("Done");

    } // end main(String[])

} // end class TestOdsAccess
