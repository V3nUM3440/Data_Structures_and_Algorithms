# 
# Author ------- Shuber Ali Mirza
# tree.py ------ Contains class for binary search tree
# Created ------ 11/FEB/2021
# Last Updated - 14/FEB/2021
# 

# Reference 1: https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
# Reference 2: https://stackoverflow.com/questions/12879903/binary-tree-counting-nodes-on-a-level

class DSATreeNode():
    
    def __init__(self , inKey , inValue):
        self.key = inKey
        self.value = inValue
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Key: " + str(self.key) + " Value: "+ str(self.value))
    
class DSABST(DSATreeNode):
    
    def __init__(self):
        self.root = None
        
    def find(self , key):
        return self._findRec(key , self.root)
    
    def _findRec(self , key , cur):
        value = None
        try:
            if cur == None:
                raise Exception

            elif key == cur.key:
                value = cur

            elif key < cur.key:
                value = self._findRec(key , cur.left)

            else:
                value = self._findRec(key , cur.right)
        except Exception:
            print('Key ', key , ' not found')
        
        return value
    
    def insert(self , key , value):
        try:
            if self.root == None:
                self.root = DSATreeNode(key , value)
                print('ROOT node ADDED with key' , key)
            else:
                self._insertRec(key , value , self.root)
        except:
            print('ERROR - Incorrect key or value')
    
    def _insertRec(self , key , value , cur):
        try:
            if key == cur.key:
                raise Exception
            elif key < cur.key:
                if cur.left != None:
                    self._insertRec(key , value , cur.left)
                else:
                    cur.left = DSATreeNode(key , value)
                    print('Node with key' , key , 'ADDED')
            else:
                if cur.right != None:
                    self._insertRec(key , value , cur.right)
                else:
                    cur.right = DSATreeNode(key , value)
                    print('Node with key' , key , 'ADDED')
        except Exception:
            print('ERROR - Node with key '+key+' already present')
    
    def pre_order(self):
        return self._preOrder(self.root)
    
    def _preOrder(self , cur):
        try:
            print(cur)
            if cur.left != None:
                self._preOrder(cur.left)
            if cur.right != None:
                self._preOrder(cur.right)
        except:
            print('ERROR - Tree empty')
    
    def in_order(self):
        return self._inOrder(self.root)
    
    def _inOrder(self , cur):
        try:
            if cur.left != None:
                self._inOrder(cur.left)
            print(cur)
            if cur.right != None:
                self._inOrder(cur.right)
        except:
            print('ERROR - Tree empty')
    
    def post_order(self):
        return self._postOrder(self.root)
    
    def _postOrder(self , cur):
        try:
            if cur.left != None:
                self._postOrder(cur.left)
            if cur.right != None:
                self._postOrder(cur.right)
            print(cur)
        except:
            print('ERROR - Tree empty')
    
    def minIter(self):
        return self._minRec(self.root)
    
    def _minRec(self , cur):
        if cur.left != None:
            minKey = self._minRec(cur.left)
        else:
            minKey = cur.key
        return minKey
    
    def maxIter(self):
        return self._maxRec(self.root)
    
    def _maxRec(self , cur):
        if cur.right != None:
            maxKey = self._maxRec(cur.right)
        else:
            maxKey = cur.key
        return maxKey
    
    def height(self):
        return self._heightRec(self.root)
    
    def _heightRec(self , cur):
        if cur == None:
            ht = -1
        else:
            leftHt = self._heightRec(cur.left)
            rightHt = self._heightRec(cur.right)
            if leftHt > rightHt:
                ht = leftHt + 1
            else:
                ht = rightHt + 1
        return ht
    
    def delete(self , key):
        return self._deleteRec(key , self.root)
    
    def _promote(self , cur):
        succ = cur
        if cur.left == None:
            succ = cur
        else:
            if cur.left != None:
                succ = self._promote(cur.left)
                if succ == cur.left:
                    cur.left = succ.right
        return succ
    
    def _deleteNode(self , key , delNode):
        update = None
        if delNode.left == None and delNode.right == None:
            update = None
        elif delNode.left != None and delNode.right == None:
            update = delNode.left
        elif delNode.left == None and delNode.right != None:
            update = delNode.right
        else:
            update = self._promote(delNode.right)
            if update != delNode.right:
                update.right = delNode.right
            update.left = delNode.left
        print('Node with key' , key , 'DELETED')
        return update
    
    def _deleteRec(self , key , cur):
        update = cur
        try:
            if cur == None:
                raise Exception
            elif key == self.root.key:
                raise Exception
            elif key == cur.key:
                update = self._deleteNode(key , cur)
            elif key < cur.key:
                cur.left = self._deleteRec(key , cur.left)
            else:
                cur.right = self._deleteRec(key , cur.right)
        except Exception:
            print('ERROR - Node doesn\'t exist or root key entered')
        return update
    
    def _getCount(self , r , cur , goal):
        value = None
        if r == None:
            value = 0
        elif cur == goal:
            value = 1
        else:
            value = self._getCount(r.left , cur+1 , goal) + self._getCount(r.right , cur+1 , goal)
        return value
    
    def balance(self):
        if self.height() == 0:
            print('Tree is 100% balanced')
        else:
            v = (self._getCount(self.root , 0 , self.height())) / (2**(self.height()))
            p = v*100
            print('Tree is '+ str(p) + '% balanced')
