# Problem Set 4A
# Name: Caleb Bibb
# Collaborators:
# Time Spent: 3 hours

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    # If length is less than 2 return sequence
    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations
    # Else Strip off the first digit
    else:
        second_sequence = sequence[1:]
        first_seq = sequence[:1]
        # Find new permutations
        permutations = get_permutations(second_sequence)
        permutations_new = []
        # Add old stuff + single
        for item in permutations:
            i = 0
            for char in item:
                # put stuff in the middle
                my_new_permutation = item[0:i] + first_seq + item[i:]
                i += 1
                permutations_new.append(my_new_permutation)
            # put stuff on the end
            end = item + first_seq
            permutations_new.append(end)
        return permutations_new

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

