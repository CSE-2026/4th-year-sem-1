class Node {
    int key;
    Node left, right;

    public Node(int item) {
        key = item;
        left = right = null;
    }
}

class BinarySearchTree {
    Node root;

    // Constructor
    BinarySearchTree() {
        root = null;
    }

    // Insert a node into the BST
    void insert(int key) {
        root = insertRec(root, key);
    }

    // Recursive function to insert a new key in the BST
    Node insertRec(Node root, int key) {
        // If the tree is empty, return a new node
        if (root == null) {
            root = new Node(key);
            return root;
        }

        // Otherwise, recur down the tree
        if (key < root.key) {
            root.left = insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }

        // Return the (unchanged) node pointer
        return root;
    }

    // Delete a node from the BST
    void delete(int key) {
        root = deleteRec(root, key);
    }

    // Recursive function to delete a key from the BST
    Node deleteRec(Node root, int key) {
        // Base case: if the tree is empty
        if (root == null) return root;

        // Recur down the tree to find the node to be deleted
        if (key < root.key) {
            root.left = deleteRec(root.left, key);
        } else if (key > root.key) {
            root.right = deleteRec(root.right, key);
        } else {
            // Node with only one child or no child
            if (root.left == null) return root.right;
            else if (root.right == null) return root.left;

            // Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = minValue(root.right);

            // Delete the inorder successor
            root.right = deleteRec(root.right, root.key);
        }

        return root;
    }

    // Get the minimum value node
    int minValue(Node root) {
        int minValue = root.key;
        while (root.left != null) {
            minValue = root.left.key;
            root = root.left;
        }
        return minValue;
    }

    // Inorder traversal of the BST (sorted order)
    void inorder() {
        inorderRec(root);
        System.out.println();
    }

    // Recursive function for inorder traversal
    void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.key + " ");
            inorderRec(root.right);
        }
    }

    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

        // Insert elements into the BST
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);

        System.out.println("Inorder traversal after inserting elements:");
        bst.inorder(); // Output: 20 30 40 50 60 70 80

        // Delete elements from the BST
        bst.delete(20);
        System.out.println("Inorder traversal after deleting 20:");
        bst.inorder(); // Output: 30 40 50 60 70 80

        bst.delete(30);
        System.out.println("Inorder traversal after deleting 30:");
        bst.inorder(); // Output: 40 50 60 70 80

        bst.delete(50);
        System.out.println("Inorder traversal after deleting 50:");
        bst.inorder(); // Output: 40 60 70 80
    }
}
