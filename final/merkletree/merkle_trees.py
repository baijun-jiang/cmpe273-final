import hashlib
from dataclasses import dataclass
from hash_files import read_files_and_hash

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        # Hash value of the node via hashlib.sha256(xxxxxx.encode()).hexdigest()
        self.val = val
        # Left node
        self.left = left
        # Right node
        self.right = right

    def __str__(self):
        return f':val={self.val},left={self.left},right={self.right}:'


class MerkleTrees(object):
    def __init__(self):
        self.root = None
        # txns dict: { hash_val -> 'file_path' } 
        self.txns = None
        self.nodes = []
        
    def get_root_hash(self):
        return self.root.val if self.root else None

    def build(self, txns):
        """
        Construct a Merkle tree using the ordered txns from a given txns dictionary.
        """
        # save the original txns(files) dict while building a Merkle tree.
        self.txns = txns
        txns_list = list(txns.keys())
        if len(txns_list)%2 != 0:
            txns_list.append(txns_list[-1])
        
        nodes = []

        for index in range(0, len(txns_list)-1, 2):
            left = txns_list[index]
            right = txns_list[index+1]
            combine = left + right
            root = hashlib.sha256(combine.encode()).hexdigest()
            current_node = Node(root, Node(left), Node(right))
            self.nodes.append(current_node)
            nodes.append(current_node)
        
        if len(nodes) >= 2:
            roots = self.build_nodes(nodes)
            self.root = roots[0]
            return roots[0]
    
    def build_nodes(self, nodes):

        if len(nodes) == 1:
            return nodes

        results = []

        for index in range(0, len(nodes) - 1, 2):
            left = nodes[index]
            right = nodes[index+1]
            combine = left.val + right.val
            root = hashlib.sha256(combine.encode()).hexdigest()
            current_node = Node(root, Node(left.val), Node(right.val))
            self.nodes.append(current_node)
            results.append(current_node)
        
        return self.build_nodes(results)


    def print_level_order(self):
        """
          1             1
         / \     -> --------------------    
        2   3       2 3
        """
        height = self.get_tree_height(self.root)
        for i in range(1, height + 1):
            self.print_val_at_level(self.root, i)
    

    def print_val_at_level(self, root, level):
        if root == None:
            return 
        
        if level == 1:
            print(root.val)
        
        if level > 1:
            self.print_val_at_level(root.left, level - 1)
            self.print_val_at_level(root.right, level - 1)
    

    def get_tree_height(self, node):
        
        if node == None:
            return 0
        
        l_height = self.get_tree_height(node.left)
        r_height = self.get_tree_height(node.right)

        return max(l_height, r_height) + 1
        

    @staticmethod
    def compare(x, y):
        """
        Compare a given two merkle trees x and y.
        x: A Merkle Tree
        y: A Merkle Tree
        Pre-conditions: You can assume that number of nodes and heights of the given trees are equal.
        
        Return: A list of pairs as Python tuple type(xxxxx, yyyy) that hashes are not match.
        https://realpython.com/python-lists-tuples/#python-tuples
        """
        diff = []
        if x.get_root_hash() == y.get_root_hash():
            diff_left = MerkleTrees.compare_nodes(x.root, y.root)
            diff_right = MerkleTrees.compare_nodes(x.root, y.root)

            return diff_left + diff_right
        
        elif x.get_root_hash() != y.get_root_hash():
            diff.append((x.get_root_hash(), y.get_root_hash()))

            diff_left = MerkleTrees.compare_nodes(x.root, y.root)
            diff_right = MerkleTrees.compare_nodes(x.root, y.root)

            return diff + diff_left + diff_right
        
        
        return diff

    @staticmethod
    def compare_nodes(x, y):

        if x == None:
            return []

        diff = [] 

        if x.val != y.val:
            diff.append((x.val, y.val))
            
        diff_left = MerkleTrees.compare_nodes(x.left, y.left)
        diff_right = MerkleTrees.compare_nodes(x.right, y.right)

        if len(diff) > 0:
            return diff_left + diff + diff_right
        
        return diff_left + diff_right