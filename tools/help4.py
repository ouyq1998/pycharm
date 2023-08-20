class TreeNode:
    def __init__(self,val):
        self.val= val
        self.children = []
def bulid_tree(n:int ,edgs:list):
    nodes = [TreeNode(i) for i in range(1,n+1)]
    for i ,f in enumerate(edgs,start=1):
        nodes[f-1].children.append([nodes[i]])
    return nodes[0]

def dfs(node:TreeNode,depth_map:dict):
    print(node)
    if not node.children:
        depth_map[node.var]=1
        return 1
    for child in node.children:
        if node.val not in depth_map:
            depth_map[node.val]=0
        depth_map[node.val]+=dfs(child,depth_map)
    return depth_map[node.val]
if __name__ == '__main__':
    n,Q = map(int,input().split())
    edgs = list(map(int,input().split()))
    queries_a = list(map(int,input().split()))
    queries_b = list(map(int,input().split()))
    root = bulid_tree(n,edgs)
    depth_map = dict()
    dfs(root,depth_map)
    xor_sum_reult = 0
    for a,b in zip(queries_a,queries_b):
        xor_sum_reult^=depth_map[a]*depth_map[b]
    print(xor_sum_reult)