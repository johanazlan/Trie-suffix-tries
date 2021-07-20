# DNA Fragments 
#Node data structure
class Node:
    def __init__(self, data = None, freq = None, size = 5, leaf = None):
        """
        The __init__ method is used to initialize the link, data, freq and leaf attributes of the Node object. link has a size of 5 because 
        [A-D] contains 4 letters and $ takes up 1 space, data stores the string added into the database for the terminal node, freq stores the
        freq of the word added into the database. leaf is used as a pointer or reference to the terminal node. 

        Complexity: O(1) because this method is just creating Node attributes which are self.link, self.data, self.freq and self.leaf for
                    the Node object. 
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """

        # terminal $ at index 0
        # A,B,C,D takes up 4 spaces and $ 1 space. 
        self.link = [None] * size 
        #data payload 
        self.data = data
        # frequency of word. 
        self.freq = freq
        #keeps track of the leaf node reference 
        self.leaf = leaf

#SequenceDatabase is a Trie data structure that represents the database 
class SequenceDatabase:

    def __init_(self):
        """
        The __init__ method is used to initialize the root of the trie by creating a Node object.

        Complexity: O(1) because this method is just creating a Node object for self.root.
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """
        self.root = Node() #create a Node object for the root 

    def addSequence(self, s, freq = 0, data = None, leaf = None):
        """
        This function takes an input of a single nonempty string of uppercase letters in uppercase [A-D]. s is used to
        represent the nonempty string. This function is used to add the non empty string s into the database. Each letter 
        in the trie will have a reference to a leaf node. Each node contains a letter and a terminal symbol is used to represent 
        the end of the string to be added. Each node also contains the frequency of the current reference to the leaf node. Each 
        letter will have a reference to the leaf node with the highest frequency. If two leaf node's have the same frequency, check which
        string is lexicographically smaller. The leaf node of the lexicographically smaller string will be the reference to the node. 
        This function does not return anything. It just adds the string into the database and saves all the links to the leaf node in order
        to make the searching process easier and faster. This function calls addSequence_recur_aux which does the recursion.


        Complexity: O(len(s)) where s is the non empty string which is added to the database. Each time a letter is added, there will be a 
                     recursion call until it reaches the length of string s which is the base case to the recursion.
        Auxiliary Space: O(N) where N is the number of nodes added. Each node has a link that is an array of size 5
        """

        current = self.root #initialize current as the root of the trie.
        i = 0 #reset i = 0 once a new word is added.
        current.leaf = self.addSequence_recur_aux(current, s, i, freq, data, leaf) #Call the function addSeequence_recur_aux() and return the output to current.leaf.

    def addSequence_recur_aux(self, current, s, i, freq, data, leaf):
        """
        This function takes an input of a single nonempty string of uppercase letters in uppercase [A-D]. s is used to
        represent the nonempty string. This function is used to add the non empty string s into the database. Each letter 
        in the trie will have a reference to a leaf node. Each node contains a letter and a terminal symbol is used to represent 
        the end of the string to be added. Each node also contains the frequency of the current reference to the leaf node. Each 
        letter will have a reference to the leaf node with the highest frequency. If two leaf node's have the same frequency, check which
        string is lexicographically smaller. The leaf node of the lexicographically smaller string will be the reference to the node. 
        This function does not return anything. It just adds the string into the database and saves all the links to the leaf node in order
        to make the searching process easier and faster. This function calls implements the recursion and pass the result to addSequence().

        Complexity: O(len(s)) where s is the non empty string which is added to the database. Each time a letter is added, there will be a 
                    recursion call until it reaches the length of string s which is the base case to the recursion.
        Auxiliary space: O(N) where N is the number of nodes added. Each node has a link that is an array of size 5
        """
        
        #base case is when i which is used to iterate through each letter of s reaches the length of s.
        if i == len(s):
            #what happens when i gone through all of my alpha in key
            index = 0 #The terminal character will use index = 0 as it's ascii value is smaller than all alphabetical characters. 
            if current.link[index] is not None: #Checks if a path exists
                current = current.link[index] #Assign current.link[index] to current since there is a Node already.
                current.freq = current.freq + 1 #increment current.freq by 1 everytime there is a same word

            # if path doesnt exist
            else:
                #create a new node at position of current.link[index]
                current.link[index] = Node(freq= freq)
                current = current.link[index]  #Assign current to refer to position of the Node.
                current.freq = 1 #current.freq = 1 means that were changing the freq of the Node from 0 to 1 because a new word is added. 
            
            current.data = s #assign current.data of the terminal node to contain s
            current.leaf = current #Assign the reference position of the terminal node to current.leaf
            return current.leaf #return the reference of the terminal node.

        else:
            #calculate index for each alphabet of the string
            # $ = 0, a = 1, b = 2, ...
            index = ord(s[i]) - 65 + 1 

            # if path exist
            #if the position of index for current.link contains a node, then current is referring to current.link[index] 
            if current.link[index] is not None: 
                current = current.link[index]

                #leaf refers to the terminal reference of the current string which is added. Return the recursive output to leaf.
                leaf = self.addSequence_recur_aux(current, s, i+1, freq, data, leaf) 

                #if current freq is smaller than freq of leaf, then update current.freq to the freq of leaf.
                if current.leaf.freq < leaf.freq:
                    current.leaf = leaf #change the reference of current.leaf to refer to leaf
                  
                #check for lexicographically smaller string
                if current.leaf.freq == leaf.freq: #check if current freq is smaller than freq of leaf
                    if len(current.leaf.data) <= len(leaf.data): #check if current data is smaller or equal to the data of leaf
                        #if i is lesser than the length of (current.leaf.data - 1) and if the next letter of current.leaf.data is greater than 
                        #leaf.data, then assign current.leaf to leaf which is the new leaf reference for this node.
                        if i < len(current.leaf.data) - 1 and ord(current.leaf.data[i+1]) > ord(leaf.data[i+1]): 
                            current.leaf = leaf

                    elif len(current.leaf.data) > len(leaf.data): #Check if current data is greater than the data of leaf.
                        #if i is lesser than the length of (leaf.data - 1) and if the next letter of current.leaf.data is greater than 
                        #leaf.data, then assign current.leaf to leaf which is the new leaf reference for this node.
                        if i < len(leaf.data) - 1 and ord(current.leaf.data[i+1]) > ord(leaf.data[i+1]):
                            current.leaf = leaf

                #print(current.leaf) #current.leaf points to AAB
                # print(leaf) #leaf points towards ABC

            # if path doesnt exist
            else:
                #if the position of index for current.link does not contain a node, create a new node
                current.link[index] = Node() 
                current = current.link[index] #current refers to current.link[index] where the new node is created.
                
                #only when u create a new node, have to reference current.leaf to the terminal.
                #when recursion on the way back to the root, store the terminal reference at current.leaf of every node. 
                current.leaf = self.addSequence_recur_aux(current, s, i+1, freq, data, leaf)

            return current.leaf     


    def query(self, q, freq = 0, data = None, leaf = None, index = 0):
        """
        This function takes an input q which is a single (possibly empty) string of uppercase letters in uppercase [A-D]. This function is used
        to search for the string which is added to the database while only traversing up to the length of query. Once it traverse until the end 
        of length of query, get the reference to the leaf node which is stored in current.leaf of the node. The output of this function will be 
        the string which is referenced in current.leaf of the node. If there is no such string in the database, return None. 

        Complexity: O(len(q)) where q is the length of the query. The process to search for the string is in O(len(q)) because to search for the 
                    string which is added to the database, only traverse up to the length of query.
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """

        current = self.root #self.root of the trie is assigned to current
        
        if current.leaf is None: #check if current.leaf which is used to store the reference to the string added to the database is None or not.
            return None

        else: #if current.leaf is not None
            for char in q: #Loop through each character of the string q of the query
                #calculate index 
                # $ = 0, a = 1, b = 2, ...
                index = ord(char) - 65 + 1

                # if path exist
                if current.link[index] is not None: #if the position of index for current.link contains a node, then current is referring to current.link[index] 
                    current = current.link[index] #Assign current to the node which is at position index of current.link[index].

                else: #if path doesnt exist, return None. This means there is no such word in the database.
                    return None

            #if current.leaf contains a reference to the leaf node, return current.leaf.data which contains the string added to the database.
            return current.leaf.data 


# Open Reading Frames
#Node data structure for OrfFinder
class Node_OrfFinder:
    def __init__(self, size = 5):
        """
        The __init__ method is used to initialize the link, prefixes, suffixes attributes of the Node_OrfFinder object. link has a size of 5 
        because [A-D] contains 4 letters and $ takes up 1 space, prefixes creates an empty list when a Node is created to store the prefixes 
        when doing a prefix search on suffix tree, suffixes creates an empty list when a Node is created to store the suffixes 
        when doing a suffix search on prefix tree.

        Complexity: O(1) because this method is just creating Node attributes which are self.link, self.prefixes and self.suffixes for
                    the Node object. 
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """
        # terminal $ at index 0
        # A,B,C,D takes up 4 spaces and $ 1 space. 
        self.link = [None] * size  
        self.prefixes = [] #An empty list which is created to store the prefixes when doing a prefix search on suffix tree
        self.suffixes = [] #An empty list which is created to store the suffixes when doing a suffix search on prefix tree

#Suffix Trie
class suffixTrie:
    def __init__(self, genome):
        """
        The __init__ method is used to initialize the root of the Suffixtrie by creating a Node object and initialize self.word as genome.

        Complexity: O(1) because this method is just creating a Node object for self.root and initializing self.word as genome.
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """

        self.root = Node_OrfFinder() #initialize a Node object at the root of the suffixTrie.
        self.word = genome #initialize self.word as genome

    def add_prefix(self):
        """
        This function is used to create a suffix trie by adding all the suffixes into the trie. For each letter of a suffix, the prefix which is the index of the letter
        is added into self.prefixes which is a list of prefixes that can be traversed by that letter. The index which is added into the prefix list corresponds to the letter
        at that index until the end of the word. Once all the suffixes and each node contains a prefix list, then it is easier to implement the find function in OrfFinder
        because the prefix list for the start can be obtained easily. This function does not return anything as an output as it only adds all the suffixes and does a prefix 
        search on the suffixes.

        Complexity: O(N^2) where N is the length of the genome. This is because to add all suffixes into the trie, need to have a nested for loop where the inner loop
                    traverses through the whole genome and the outer loop only traverses when the inner loop completes its iteration. 
        Auxiliary Space: O(N) where N is the number of nodes added. Each node has a link that is an array of size 5

        """

        current = self.root #The root of the suffixTrie is assigned to current
        word = self.word #create a variable word and assign self.word to it.
        for j in range(len(word)): #Loop through each alphabet of the word once the inner loop is done. 
            current = self.root #Assign the root to current
            i = j #Ensures that i starts at position j after each loop
            for i in range(i, len(word)): #Loop through the word from i to j.
                #calculate index for each alphabet of the string
                # $ = 0, a = 1, b = 2, ...
                index = ord(word[i]) - 65 + 1 

                # if path exist
                #if the position of index for current.link contains a node, then current is referring to current.link[index] 
                if current.link[index] is not None: 
                    current = current.link[index]

                # if path doesnt exist
                else:
                    #if the position of index for current.link does not contain a node, create a new node
                    current.link[index] = Node_OrfFinder() #Create a new Node object and assign it to current.link[index]
                    current = current.link[index] #current refers to current.link[index] where the new node is created.

                current.prefixes.append(j) #Append j to each current.prefix. j is the index of the letter which is the start of the suffix of the word being added.

            #index = 0 is for the terminal node to indicate when a suffix reaches the end. 
            index = 0 
            # if path exist
            #if the position of index for current.link contains a node, then current is referring to current.link[index] 
            if current.link[index] is not None: 
                current = current.link[index]

            #create a new node
            else:
                current.link[index] = Node_OrfFinder() #new suffix added because new terminal created.
                current = current.link[index]  #current refers to the Node.
            
            current.prefixes.append(j) #Append j to each current.prefix. j is the index of the letter which is the start of the suffix of the word being added.

# Prefix Trie
class prefixTrie:
    def __init__(self, genome):
        """
        The __init__ method is used to initialize the root of the Suffixtrie by creating a Node object and initialize self.word as genome.

        Complexity: O(1) because this method is just creating a Node object for self.root and initializing self.word as genome.
        Auxiliary Space: O(1) because all the operations in this method is done in-place and no extra storage is required.

        """

        self.root = Node_OrfFinder() # initialize a Node object at the root of the suffixTrie.
        self.word = genome #initialize self.word as genome

    def add_suffix(self):
        """
        This function is used to create a prefix trie by adding all the prefixes into the trie in reverse order by starting to add from the back of the string. For each 
        letter of a prefix, the suffix which is the index of the letter is added into self.suffixes which is a list of suffixes that can be traversed by that letter. 
        The index which is added into the suffix list corresponds to the letter at that index until the end of the word. Once all the suffixes and each node contains 
        a suffix list, then it is easier to implement the find function in OrfFinder because the suffix list for end can be obtained easily. This function does not 
        return anything as an output as it only adds all the prefixes and does a suffix search on the prefixes.

        Complexity: O(N^2) where N is the length of the genome. This is because to add all prefixes into the trie in reverse order, need to have a nested for loop 
                    where the inner loop traverses through the whole genome and the outer loop only traverses when the inner loop completes its iteration. The traversal
                    is done from the back to front in order to add the prefixes in reversed order into the prefix trie.
        Auxiliary Space: O(N) where N is the number of nodes added. Each node has a link that is an array of size 5

        """

        current = self.root #The root of the prefixTrie is assigned to current
        word = self.word #self.word is assigned to word

        for j in range(len(word)-1, -1, -1): #The outer loop loops from the end of the word until the start of the word. Loops once after the inner loop completes its iteration
            current = self.root #The root of the prefixTrie is assigned to current
            i = j #Assign i = j after every iteration because j will move one step towards the front and i needs to start from position of j to get all the reversed prefixes
            for i in range(i, -1, -1): #The inner loop loops from position of i until the start of the word from back to front.
                #calculate index for each alphabet of the string
                # $ = 0, a = 1, b = 2, ...
                index = ord(word[i]) - 65 + 1 

                # if path exist
                #if the position of index for current.link contains a node, then current is referring to current.link[index] 
                if current.link[index] is not None: 
                    current = current.link[index]

                # if path doesnt exist
                else:
                    #if the position of index for current.link does not contain a node, create a new node
                    current.link[index] = Node_OrfFinder() #Create a new Node object and assign it to current.link[index]
                    current = current.link[index] #current refers to current.link[index] where the new node is created.

                current.suffixes.append(j) #Append j to each current.suffix where j is the index of the current starting letter of the reversed prefix being added

            #index = 0 is for the terminal node to indicate when a reversed prefix reaches the end. 
            index = 0
            # if path exist
            #if the position of index for current.link contains a node, then current is referring to current.link[index] 
            if current.link[index] is not None:
                current = current.link[index]

            # if path doesnt exist
            else:
                current.link[index] = Node_OrfFinder() #new reversed prefix added because new terminal created.
                current = current.link[index]  #current refers to the Node.
            
            current.suffixes.append(j) #Append j to each current.suffix where j is the index of the current starting letter of the reversed prefix being added


class OrfFinder:
    def __init__(self, genome):
        """
        The __init__ method is used to create a root attribute and initialize it with a Node object, initialize word as genome, create an instance of suffixTrie and 
        implements the add_prefix() method. This method also creates an instance of prefixTrie and implements the add_suffix() method.

        Complexity: O(N^2) where N is the length of the genome. The complexity of creating an instance of suffixTrie and implementing the add_prefix() method is O(N^2).
                    The complexity of creating an instance of prefixTrie and implementing the add_suffix() method is also O(N^2).
        Auxiliary Space: O(N) where N is the number of nodes added. Each node has a link that is an array of size 5

        """

        self.root = Node_OrfFinder() # initialize a Node object as the root 
        self.word = genome #initialize word as genome
        self.prefix = suffixTrie(self.word) #Create an instance of suffixTrie 
        self.prefix.add_prefix() #implementing the add_prefix() method for suffixTrie instance
        self.suffix = prefixTrie(self.word) #Create an instance of prefixTrie 
        self.suffix.add_suffix() #implementing the add_suffix() method for prefixTrie instance

    def find(self, start, end):
        """
        This function takes as input start and end which are each a single non-empty string consisting of only uppercase [A-D]. start is the prefix of the substring 
        and end is the suffix of the substring that is supposed to be returned. The output of find(self, start, end) is a list of strings. The list contains all 
        the substrings of genome which have start as a prefix and end as a suffix. This function gets all the prefixes by looping through start and assigning current1.prefixes
        to prefix for each iteration and gets all the suffixes by looping through end from back to front and assigning current2.suffixes to suffix for each iteration.
        Then, loop through prefix and suffix to obtain a substring. Check if the length of the substring is greater than the length of start + length of end. If it is greater,
        add the substring into the substring list and return the substring list once the loop terminates.

        Complexity: (O(len(start)) + O(len(end)) + O(U)) time where start is the prefix which is given in the input, end is the suffix which is given in the input and
                    U is the number of characters in the output list. start is used to get all the prefixes by looping through start and checking the suffixTrie for the 
                    list of prefix at each Node. end is used to get all the suffixes by looping through end from the back to front and checking the prefixTrie for the 
                    list of suffix at each Node. 
        Auxiliary Space: O(N) where N is the length of substring list. 

        """

        current1 = self.prefix.root #current1 contains the root for the instance of suffixTrie
        current2 = self.suffix.root #current2 contains the root for the instance of prefixTrie
        word = self.word #Assign self.word to word
        substring_list = [] #initialize substring list to contain an empty list. This is used to store all the substrings

        for i in range(len(start)): #Loop through the start
            if current1 is not None: #check if current1 is not None
                #calculate index for each alphabet of the string
                # $ = 0, a = 1, b = 2, ...
                index = ord(start[i]) - 65 + 1  
                current1 = current1.link[index] #Assign current1.link[index] to current1 if there is a node.
                prefix = current1.prefixes #Assign current1.prefixes to a variable called prefix
           
        for j in range(len(end)-1, -1, -1): #Loop through the end from back to front
            if current2 is not None: # Check if current2 is not None
                #calculate index for each alphabet of the string
                # $ = 0, a = 1, b = 2, ...
                index = ord(end[j]) - 65 + 1 
                current2 = current2.link[index] #Assign current2.link[index] to current2 if there is a node.
                suffix = current2.suffixes #Assign current2.prefixes to a variable called suffix

        #Print out the substring
        for i in range(len(prefix)): #Loop through prefix
            for j in range(len(suffix)): #Loop through suffix
                substring = word[prefix[i]:suffix[j]+1] #substring is a substring of the word from index i to j of the word.
                if len(substring) >= len(start) + len(end): #Check if length of substring is greater than length start and length end
                    substring_list.append(substring) #If it meets the if statement then append the substring to the substring_list
        
        return substring_list #Return a list of substrings 

