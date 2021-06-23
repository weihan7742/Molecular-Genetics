#%%
class SuffixNode: 
    """
    A class representing a SuffixNode which stores some payloads 
    """
    def __init__(self,size=5) -> None:
        """
        Initialization of a SuffixNode object.

        :param size: Size of the array to be initialized

        Best/Worst Time Complexity: O(size)
        Total Space Complexity: O(size)
        Auxiliary Space Complexity: O(size)
        """
        self.link = [None]*size
        self.id = []

class OrfFinder:
    """
    A class which stores and find sections of a genome which start and ends with a particular sequence.
    """
    def __init__(self,genome):
        """
        Initialization of OrfFinder object

        :param genome: a single non-empty string consisting only of uppercase [A-D]

        Time Complexity: O(N^2)
        N - length of genome
        Total Space Complexity: O(N^2)
        Auxiliary Space Complexity: O(N^2)

        """
        self.root = SuffixNode()
        self.word = genome
        # Build a suffix trie
        for i in range(len(genome)):
            self.insert(i)

    def find(self,start,end):
        """
        Time Complexity: O(len(start)+len(end)+U)
        U - number of characters in the output list

        :param start: single non-empty string consisting of only uppercase [A-D]
        :param end: single non-empty string consisting of only uppercase [A-D]
        :return: a list of strings containing all substring of genome which have start as 
        prefix and end as suffix.

        Best/Worst Time Complexity: O(len(start)+len(end)+U)
        U - The number of characters in the output list
        Total Space Complexity: O(len(start)+len(end)+U)
        Auxiliary Space Complexity: O(len(start)+len(end)+U)
        """
        start_list = self.search(start)
        end_list = self.search(end)

        res = []

        if start_list is not None and end_list is not None:
            # Iterate over start_list
            for i in range(len(start_list)):
                start_count = start_list[i] + len(start) - 1
                for j in range(len(end_list)-1,-1,-1):
                    end_count = end_list[j]
                    if end_count > start_count:
                        end_item = end_count + len(end)
                        res.append(self.word[start_list[i]:end_item])
        
        return res

    def insert(self,id):
        """
        Inserting a suffix into a Trie data structure.

        :param id: The first index of suffix in a word

        Best/Worst Time Complexity: O(s)
        s - The length of the substring from index s to end of the string  
        Total Space Complexity: O(s)
        Auxiliary Space Complexity: O(s)

        """

        current = self.root
        self.insert_recur_aux(current,id,id)

    def insert_recur_aux(self,current,id,idx):
        """
        Auxiliary function of insert.

        :param current: The current SuffixNode to be linked with
        :param id: The first index of suffix in a word
        :param idx: The index of each character in a word

        Best/Worst Time Complexity: O(s)
        s - The length of the substring from index s to end of the string  
        Total Space Complexity: O(s)
        Auxiliary Space Complexity: O(s)

        """
        if idx == len(self.word):
            # if no existing word
            if current.link[0] is None:
                current.link[0] = SuffixNode()
            current = current.link[0]
            return current

        else: 
            index = ord(self.word[idx]) - 65 + 1
            # if path exist
            if current.link[index] is not None: 
                current = current.link[index]
            # IF path does not exist
            else: 
                current.link[index] = SuffixNode()
                current = current.link[index]

            # Add id to SuffixNode
            current.id.append(id)

            self.insert_recur_aux(current,id,idx+1)

    def search(self,key):
        """
        Find if a substring exists in a string

        :param key: Substring to be searched
        :return: A list of id; None if doesn't exist

        Best Time Complexity: O(1) - when string is found in the first SuffixNode
        Worst Time Complexity: O(n)
        n - The length of substring to be found
        Total Space Complexity: O(n)
        Auxiliary Space Complexity: O(1) 
        """
        # begin from root
        current = self.root
        # Go through the key 1 by 1
        for char in key: 
            index = ord(char) - 65 + 1
            # If path exist
            if current.link[index] is not None: 
                current = current.link[index]
            else: 
                return None
        
        return current.id