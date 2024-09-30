package ADSLAB;
class AVLTree{
    class Node{

        int val,height;
        Node left,right;

        Node(int d){
            val =d;
            height=1;
        }
    }

    private Node root ;

    int height(Node node){
        if(node == null){
            return 0;
        }
        return node.height;
    }

    int max(int a , int b){
        return (a>b)?a:b;
    }

    int getbalancefac(Node node){
        if(node == null) return 0;
        return (height(node.left) - height(node.right));
    }

    Node rightrotate(Node y){
        Node x =y.left;
        Node t=x.right;

        x.right = y;
        y.left = t;

        x.height = max(height(x.left),height(x.right))+1;
        y.height = max(height(y.left),height(y.right))+1;

        return x;
    }

    Node leftrotate(Node x){
        Node y = x.right;
        Node t = y.left;

        y.left = x;
        x.right = t;

        x.height = max(height(x.left),height(x.right))+1;
        y.height = max(height(y.left),height(y.right))+1;

        
        return y;
    }

    Node insert(Node node,int val){
        if(node == null){
            return (new Node(val));
        }

        if(val < node.val){
            node.left=insert(node.left,val);
        }else if(val > node.val){
            node.right=insert(node.right,val);
        }else{
            return node;
        }

        node.height = max(height(node.left),height(node.right))+1;

        int balance = getbalancefac(node);

        if(balance > 1 && val > node.left.val){
            node.left = leftrotate(node.left);
            return rightrotate(node);

        }if(balance > 1 && val < node.left.val){
            return rightrotate(node);

        }if(balance <-1 && val > node.right.val){
            return leftrotate(node);

        }if(balance<-1 && val < node.right.val){
            node.right = rightrotate(node.right);
            return leftrotate(node);

        }

        return node;
    }

    void preorder(Node node){
       if(node!= null){
        System.out.println(node.val);
        preorder(node.left);
        preorder( node.right);
       }

    }

    public static void main(String[] args){
        AVLTree app = new AVLTree();

        Node root = null;
        root = app.insert(root,10);
        root = app.insert(root,20);
        root = app.insert(root,5);
        root = app.insert(root,1);
        root = app.insert(root,100);
        root = app.insert(root,15);
        app.preorder(root);
        //a.delete(5);
        //a.preorder(root);

        //System.out.println(a.search(root,100));


    
    }


}