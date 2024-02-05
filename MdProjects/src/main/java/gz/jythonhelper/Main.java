package gz.jythonhelper;

public class Main {

   public static final String PATH_SEPARATOR = System.getProperty("path.separator");

   private static void generatePy(String outputDir, String... files) {
      EasyJython ej = new EasyJython(outputDir);
      ej.setLibs(new String[0]);
      ej.generatePys(files);

   } // end generatePy(String, String[], String...)

   public static void main(String[] args) {
      if (args.length > 1) {
         String outputDir = args[0];
         String[] files = args[1].split(PATH_SEPARATOR);
         generatePy(outputDir, files);
      } else {
         System.out.println("Missing argument; need <output directory> and <source directories path>");
      }

   } // end main(String[])

} // end class Main
