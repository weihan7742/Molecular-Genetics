# Suffix Trie - Molecular Genetics 
In Molecular Genetics, there is a notion of an Open Reading Frame (ORF). An ORF is a
portion of DNA that is used as the blueprint for a protein. All ORFs start with a particular
sequence, and end with a particular sequence.

In this task, we wish to find all sections of a genome which start with a given sequence of
characters, and end with a (possibly) different given sequence of characters.

## Input
**genome** is a single non-empty string consisting only of uppercase [A-D]. genome is passed as an
arguement to the __init__ method of OrfFinder (i.e. it gets used when creating an instance
of the class).

**start** and **end** are each a single non-empty string consisting of only uppercase [A-D].

## Output
**find** returns a list of strings. This list contains all the substrings of genome which have start
as a prefix and end as a suffix. There is no particular requirement for the order of these strings.
start and end must not overlap in the substring (see the last two cases of the example below).
 
## Example
```
genome1 = OrfFinder("AAABBBCCC")
genome1.find("AAA","BB")
>>> ["AAABB","AAABBB"]
genome1.find("BB","A")
>>>[]
genome1.find("AA","BC")
>>>["AABBBC","AAABBBC"]
genome1.find("A","B")
>>> ["AAAB","AAABB","AAABBB","AAB","AABB","AABBB","AB","ABB","ABBB"]
genome1.find("AA","A")
>>> ["AAA"]
#note that "AA" is not valid, since start and end would need to overlap
genome1.find("AAAB","BBB")
>>> []
# note that "AAABBB" is not valid, since start and end would need to overlap
```

## Complexity
- The __init__ method of OrfFinder must run in O(N2) time, where N is the length of
genome.
- find must run in (len(start) + len(end) + U) time, where U is the number of characters
in the output list.

As an example of what the complexity for find means, consider a string consisting of N
2 "B"s
followed by N
2 "A"s.
If we call find("A","B"), the output is empty, so U is O(1). On the other hand, if we call
find("B", "A") then U is O(N2).

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

