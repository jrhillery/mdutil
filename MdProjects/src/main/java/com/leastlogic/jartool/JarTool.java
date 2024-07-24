package com.leastlogic.jartool;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JarTool {
   private static final Pattern lParse =
      Pattern.compile("(.+)\\[class,load] (.+?) source: file:/(.+)$");

   public static void main(String[] args) throws Exception {
      TreeMap<String, TreeSet<String>> sources = new TreeMap<>();
      Path loadLog = Path.of("classLoad.log");

      try (BufferedReader reader = Files.newBufferedReader(loadLog)) {
         String line;

         while ((line = reader.readLine()) != null) {
            Matcher m = lParse.matcher(line);

            if (m.find()) {
               String src = m.group(3);

               if (src.startsWith("C:/Users/") && src.endsWith(".jar")) {
                  TreeSet<String> classSet;
                  classSet = sources.computeIfAbsent(src, k -> new TreeSet<>());

                  String clazz = m.group(2);
                  classSet.add(clazz);
               }
            }
         }
      } // end try with resources
      String dir = args.length > 0 ? args[0] : ".";

      sources.forEach((src, classSet) -> {
         String outFn = Path.of(src).getFileName() + ".lst";
         Path outLst = Path.of(dir, outFn);
         System.out.println("Writing to " + outLst);

         try (BufferedWriter writer = Files.newBufferedWriter(outLst)) {

            classSet.forEach(clazz -> {
               try {
                  writer.write(clazz);
                  writer.write('\n');
               } catch (Exception e) {
                  throw new RuntimeException(e);
               }
            });
         } catch (Exception e) {
            throw new RuntimeException(e);
         } // end try with resources
      });

   } // end main(String[])

} // end class JarTool
