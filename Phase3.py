import time
import random
import tracemalloc

# TreeNode class for Binary Search Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinarySearchTree class with insert, search, and traversal methods
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

# Testing class for Binary Search Tree with test cases
class TestBST:
    def __init__(self, bst_class):
        self.bst_class = bst_class
    
    def test_insertion(self, elements):
        bst = self.bst_class()
        start_time = time.time()
        for element in elements:
            bst.insert(element)
        end_time = time.time()
        print(f"Insertion of {len(elements)} elements took {end_time - start_time:.4f} seconds")
        return bst
    
    def test_search(self, bst, elements):
        start_time = time.time()
        for element in elements:
            bst.search(element)
        end_time = time.time()
        print(f"Search in {len(elements)} elements took {end_time - start_time:.4f} seconds")
    
    def test_memory_usage(self, elements):
        tracemalloc.start()
        bst = self.bst_class()
        for element in elements:
            bst.insert(element)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 10**6:.2f} MB, Peak memory usage: {peak / 10**6:.2f} MB")
        tracemalloc.stop()
        return bst

# Test cases
def run_tests():
    test_bst = TestBST(BinarySearchTree)
    
    # Test with a smaller dataset
    small_dataset = [random.randint(1, 1000) for _ in range(1000)]
    bst_small = test_bst.test_insertion(small_dataset)
    test_bst.test_search(bst_small, random.sample(small_dataset, 100))  # Test searching 100 elements
    test_bst.test_memory_usage(small_dataset)
    
    print("\n" + "="*30 + "\n")

    # Test with a larger dataset
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    bst_large = test_bst.test_insertion(large_dataset)
    test_bst.test_search(bst_large, random.sample(large_dataset, 1000))  # Test searching 1000 elements
    test_bst.test_memory_usage(large_dataset)

if __name__ == "__main__":
    run_tests()
