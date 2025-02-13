

public class Main{
    public static void getMinMax(int[] array, int size , int[] minMax){
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(int i=0;i< size;i++){
            if (array[i]< min){
                min = array[i];
            }
            if (array[i] > max){
                max = array[i];
            }
        }

        minMax[0] = min;
        minMax[1] = max;
    }
    public static void main(String[] args){
        int[] array1 = {3, 5, 4, 1, 9};
        int[] array2 = {22, 14, 8, 17, 35, 3};

        int[] minMax = new int[2];

        getMinMax(array1, array1.length, minMax);
        System.out.println("array1 :min " + minMax[0]+ "  max = "+ minMax[1]);

        getMinMax(array2, array2.length, minMax);
        System.out.println("array2 :min  " + minMax[0]  + " max = "+ minMax[1]);


    }
}