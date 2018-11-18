def is_subseq(candidate, seq):
    it = iter(seq)
    return all(c in it for c in candidate)
    # if c is NOT in it, next(it) will be called internally again and again up to the and of the array
    # if c is in it, iterator won't be called anymore in current loop execution
