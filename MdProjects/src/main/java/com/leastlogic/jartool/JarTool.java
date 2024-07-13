package com.leastlogic.jartool;

import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.TreeSet;

public class JarTool {

   public static void main(String[] args) throws Exception {
      TreeSet<String> sources = new TreeSet<>();
      Path loadLog = Paths.get("classLoad.log");

      try (BufferedReader reader = Files.newBufferedReader(loadLog)) {
         String line;

         while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" source: ");

            if (parts.length > 1) {
               sources.add(parts[1]);
            }
         }
      } // end try with resources

      for (String source : sources) {
         System.out.println(source);
      }

   } // end main(String[])

} // end class JarTool
