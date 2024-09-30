package ADSLAB;

import java.util.*;

public class heapsort {
    public static void heapSorting(int[] arr){
        PriorityQueue<Integer> minheap = new PriorityQueue<>();

        for(int i=0;i<arr.length;i++){
            minheap.add(arr[i]);
        }

        for(int i=0;i<arr.length;i++){
            arr[i] = minheap.poll();
        }

    }


public static void main(String[] args){
    int [] arr = {10,7,11,30,8,38,2,45};
    heapsort.heapSorting(arr);

    for(int i=0;i<arr.length;i++){
        System.out.println(arr[i] +" ");
    }
}

}