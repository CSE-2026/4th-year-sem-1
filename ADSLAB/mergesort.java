package ADSLAB;

public class mergesort {
    void merge(int arr[],int l,int mid ,int r){
        int n1=mid-l+1;
        int n2= r-mid;

        int []left = new int[n1];
        int []right = new int[n2];
        int k=l;

        for(int i=0;i<n1;i++){
            left[i]=arr[k++];
        }
        for(int j=0;j<n2;j++){
            right[j]= arr[k++];
        }

        int i=0;
        int j=0;
        k=l;
        while(i<n1 && j<n2){
            if(left[i] <= right[j]){
                arr[k]=left[i];
                i++;
            }else{
                arr[k]=right[j];
                j++;
            }
            k++;
        }
        while(i<n1){
            arr[k]=left[i];
            i++;
            k++;
        }
        while(j<n2){
            arr[k]=right[j];
            j++;
            k++;
        }

    }

    void  mergesorting(int arr[],int l,int r){
        if(l>=r){
            return;
        }
        int mid = (l+r)/2;
        mergesorting(arr,l,mid);
        mergesorting(arr,mid+1,r);
        merge(arr,l,mid,r);
    }

    public static void main(String[]  args){
        mergesort sort = new mergesort();
        int []arr ={1,4,2,3,5,6,17,12,11,23};
        int n=arr.length;
        sort.mergesorting(arr,0,arr.length-1);

        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }
    }
}
