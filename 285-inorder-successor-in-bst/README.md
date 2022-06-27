<h2><a href="https://leetcode.com/problems/inorder-successor-in-bst/">285. Inorder Successor in BST</a></h2><h3>Medium</h3><hr><div><p>Given the <code>root</code> of a <mark id="aad36ef9-43ae-45f9-ba8e-bb062bc61edb" data-private-id="e0114d50-bb2a-4a8a-93cd-31767a3e6805" class="a20a9c51-fba4-4bb1-81ec-4c4c160ccb78 f5ac9b20-8bc7-4594-9e0b-942250b12742 default-orange-da01945e-1964-4d27-8a6c-3331e1fe7f14" tabindex="0">binary search tree</mark> and a node <code>p</code> in it, return <em>the in-order successor of that node in the BST</em>. If the given node has no in-order successor in the tree, return <code>null</code>.</p>

<p>The successor of a node <code>p</code> is the node with the smallest key greater than <code>p.val</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG" style="width: 122px; height: 117px;">
<pre><strong>Input:</strong> root = [2,1,3], p = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG" style="width: 246px; height: 229px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,null,1], p = 6
<strong>Output:</strong> null
<strong>Explanation:</strong> There is no in-order successor of the current node, so the answer is <code>null</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><mark id="b7fa12dc-8ea4-472b-955b-453e81ad5550" data-private-id="d129800c-9012-46c5-91bb-a006879125c0" class="a20a9c51-fba4-4bb1-81ec-4c4c160ccb78 f5ac9b20-8bc7-4594-9e0b-942250b12742 default-orange-da01945e-1964-4d27-8a6c-3331e1fe7f14" tabindex="0">All Nodes will have unique values</mark>.</li>
</ul>
</div>