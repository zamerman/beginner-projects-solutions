public class NinetyNineBottles {

    static String bottleWatch(int bottles) {
        if (bottles != 1) {
            return String.format("%s bottles", bottles);
        }else {
            return String.format("%s bottle", bottles);
        }
    }

    public static void main(String args[]) {
        System.out.println();
        for (int bottles = 99; bottles > 0; bottles--) {
            String songLine;
            songLine = String.format("%s of beer on the wall, %s of beer." +
                                     "\nTake one down, pass it around, %s " +
                                     "of beer on the wall...\n",
                                     bottleWatch(bottles),
                                     bottleWatch(bottles),
                                     bottleWatch(bottles - 1));
            System.out.println(songLine);
        }
    }
}
