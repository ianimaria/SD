class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object): 

    # aflam inaltimea arborelui 

    def getHeight(self, root):

        if not root:
            return 0
        return root.height
    
    # aflam diferenta de inaltime dintre doi fii

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # aflam nodul cu valoarea minima

    def getMinValueNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # rotatie la dreapta

    def rightrotate(self, y):

        z = y.left 
        T3 = z.right 
  
        
        z.right = y 
        y.left = T3 
  
       
        y.height = 1 + max(self.getHeight(y.left),  self.getHeight(y.right)) 
        z.height = 1 + max(self.getHeight(z.left),  self.getHeight(z.right)) 
  
        return z 

    # rotatie la stanga

    def leftRotate(self, y): 
  
        z = y.right 
        T2 = z.left 
   
        z.left = y 
        y.right = T2 
   
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
  
        
        return z 

    # inserarea unui element

    def insert(self, root, key): 
          
      
        if not root: 
            return TreeNode(key) 
        if key < root.val: 
            root.left = self.insert(root.left, key) 
        elif key > root.val: 
            root.right = self.insert(root.right, key) 
        else:
            return root
  
     
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  

        balance = self.getBalance(root) 
  
        # Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    # stergerea unui element

    def delete(self, root, key): 
  
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 

            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, temp.val) 
  
        if root is None: 
            return root 
   
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
       
        balance = self.getBalance(root) 
  
        #  Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        #  Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root  
    
    # verificam daca o valoare exista in AVL sau nu
                              
    def cautare(self, root, key):

        if not root:
            return "Elementul nu exista in AVL"
        
        elif root.val == key:
            return "Elementul exista in AVL"
            

        elif root.val < key:
            return self.cautare(root.right, key)
        
        else:
            return self.cautare(root.left, key)

    # aflam succesorul din AVL al unei valori date

    def Succesor(self, root, key):

        succ = None

        if root is None:
            return "Nu exista noduri"

        while (1):

            if root.val < key:
                if root.right:
                    root = root.right
                else:
                    break


            elif root.val > key :
                succ = root.val
                if root.left:
                    root = root.left
                else:
                    break
            
            else:
                
                succ = root.val
                break

        if succ != None:
            print("Succesorul lui %s este:" %key, end=" ")
            return succ
        else:
            return "Nu are succesor"

    # aflam predecesorul din AVL al unei valori date
        
    def predecesor(self, root, key):

        pred = None
        
        if root is None:
            return "Nu exista noduri"

        while (1):

            if root.val < key:
                pred = root.val
                if root.right:    
                    root = root.right
                else:
                    break

            elif root.val > key:
                if root.left:
                    root= root.left
                else:
                    break

            else:
                pred = root.val
                break

        if pred != None:
            print("Predecesorul lui %s este:" %key, end=" ")
            return pred
            
        else:
            return "Nu are predecesor"

    # afisam valorile din AVL cuprinse intr-un interval 

    def interval(self, root, a, b):
        
        if root is None:
            "Nu exista noduri"
        else:
            if root.val <= a :
                self.interval(root.right, a, b)
        
            elif root.val >= b:
                self.interval(root.left, a, b)

            else:  
                self.interval(root.left, a, b)         
                print(root.val, end=" ")
                self.interval(root.right, a, b)  
               
   

print(" Tipuri de operatii",
      "1. Insereaza valoarea in AVL",
      "2. Sterge toate aparitiile unui element din AVL",
      "3. Verifica daca valoarea exista in AVL",
      "4. Aflati succesorul unei valori",
      "5. Aflati predecesorul unei valori",
      "6. Afisati valorile din interval", sep='\n')

print()

avl = AVL_Tree() 
root = None

n= int(input(" N = "))

for i in range(n):

    print("Introduceti operatia:", end=" ")
    option = int(input())

    if option < 6:

        print("Introduceti valoarea:", end=" ")
        value = input()

        if option == 1:
            root = avl.insert(root, value)
            print()
            

        if option == 2:
            k=0
            if avl.cautare(root, value) == "Elementul nu exista in AVL":
                print("Elementul nu exista in AVL")
            else:
                while avl.cautare(root,value) == "Elementul exista in AVL":
                    k+=1
                    root = avl.delete(root, value)
                    if k==1:
                        print("Elementul %s avea o aparitie" %value)
                    else:
                        print("Elementul %s avea %s aparitii" %(value,k))
            
               
        elif option == 3:
            print(avl.cautare(root, value))
            print()

        elif option == 4:
            print(avl.Succesor(root, value))
            print()

        elif option == 5:
            print(avl.predecesor(root, value))
            print()
        

    elif option == 6:
        print("Introduceti intervalul:",end=" ")
        value1, value2 = input().split()
        
        avl.interval(root, value1, value2)
        print()
    
    else:
        print("Nu ai introdus o optiune valida")
        print()
      
      
       
        

