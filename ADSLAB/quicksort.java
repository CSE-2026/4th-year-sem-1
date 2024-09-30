package ADSLAB;

public class quicksort {

    void quicksorting(int []arr,int low,int high){
        if(low>=high){
            return ;
        }
        int partition = partion(arr,low,high);
        quicksorting(arr,low,partition-1);
        quicksorting(arr, partition+1, high);
    }

    void swap(int a,int b){
        int temp = a;
        a=b;
        b=temp;

        
    }

    int partion(int arr[],int low,int high){
        int pivot = arr[high];
        int pivotindex= low;
        for(int i=low;i<high;i++){
            if(arr[i]<= pivot){
                swap(arr[i],arr[pivotindex]);
                pivotindex++;
            }
        }
        swap(arr[pivotindex],arr[high]);
        return pivotindex;
    }
    public static void main(String[] args){
        quicksort sort = new quicksort();
        int []arr = {1,5,2,3,4,7,6,8,9,12,11,13};
        int low=0;
        int high = arr.length-1;
        sort.quicksorting(arr,low,high);

        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
    }
}
