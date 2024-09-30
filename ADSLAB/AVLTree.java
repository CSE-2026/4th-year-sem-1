
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

    Node minvaluenode(Node node){
        Node current =  node;
        while(current.left !=null){
            current = current.left;
        }
        return current;
    }

    Node delete(Node root,int val){
        if(root==null){
            return root;
        }
        if(val < root.val){
            root.left = delete( root.left, val);
        }else if(val > root.val){
            root.right = delete(root.right, val);
        }else{

            if(root.left == null || root.right==null){
                Node temp = (root.left !=null)? root.left:root.right;

                if(temp == null){
                    temp =root;
                    root=null;

                }else{
                    root=temp;
                }


            }else{
                Node temp = minvaluenode(root.right);

                root.val = temp.val;
                root.right = delete(root.right, temp.val);
            }

        }
        if(root ==null){
            return root;
        }

        root.height = max(height(root.left),height( root.right))+1;

        int balance = getbalancefac(root );

        if(balance > 1 && val > root.left.val){
            root.left = leftrotate(root.left);
            return rightrotate(root);

        }if(balance > 1 && val < root.left.val){
            return rightrotate(root);

        }if(balance <-1 && val > root.right.val){
            return leftrotate(root);

        }if(balance<-1 && val < root.right.val){
            root.right = rightrotate(root.right);
            return leftrotate(root);

        }

        return root;

    }

    void preorder(Node node){
       if(node!= null){
        
        preorder(node.left);
        System.out.println(node.val);
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
        app.delete(root,5);
        app.preorder(root);

        //System.out.println(a.search(root,100));


    
    }


}