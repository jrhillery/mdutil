
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Spliterator;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

public class TstStream {

    public static void main(String[] args) {
        List<String> baseStrings = Arrays.asList("one", "two", "three", "four", "five");
        Iterable<String> stringIterable = baseStrings::iterator;
        Spliterator<String> stringSpliterator = baseStrings.spliterator();
        stringSpliterator.forEachRemaining(System.out::println);
        stringSpliterator = stringIterable.spliterator();
        stringSpliterator.forEachRemaining(System.out::println);
        Stream<String> stringStream = StreamSupport.stream(stringIterable.spliterator(), false);
        Iterator<String> stringIterator = stringStream.iterator();

        while (stringIterator.hasNext()) {
            System.out.println(stringIterator.next());
        }
        stringStream = baseStrings.stream();
        stringStream.forEach(System.out::println);
        stringIterator = baseStrings.listIterator();

        while (stringIterator.hasNext()) {
            System.out.println(stringIterator.next());
        }
        stringIterator = baseStrings.iterator();

        while (stringIterator.hasNext()) {
            System.out.println(stringIterator.next());
        }

    }

}
