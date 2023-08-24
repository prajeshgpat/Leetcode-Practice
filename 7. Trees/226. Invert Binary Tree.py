from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right subtrees
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    stack = [(root, 0)]
    while stack:
        current, index = stack.pop()
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(nodes) and nodes[left_index] is not None:
            current.left = TreeNode(nodes[left_index])
            stack.append((current.left, left_index))
        if right_index < len(nodes) and nodes[right_index] is not None:
            current.right = TreeNode(nodes[right_index])
            stack.append((current.right, right_index))
    return root


def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


testInputs = [[4, 2, 7, 1, 3, 6, 9], [2, 1, 3], []]
for nodes in testInputs:
    root = build_tree(nodes)
    inverted_tree = Solution().invertTree(root)
    result = level_order_traversal(inverted_tree)
    print(result)
