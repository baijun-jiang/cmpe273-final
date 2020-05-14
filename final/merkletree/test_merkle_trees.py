from hash_files import read_files_and_hash
from merkle_trees import MerkleTrees

def read(path):
    return read_files_and_hash(path)

def test():
    merkletree_A = MerkleTrees()
    # FIXME: Use full path if your OS/setup does not work with relative path
    merkletree_A.build(read("./dir_A"))
    print(f'A:root_hash={merkletree_A.get_root_hash()}\n')
    assert merkletree_A.get_root_hash() != None
    merkletree_A.print_level_order()

    merkletree_B = MerkleTrees()
    merkletree_B.build(read("./dir_B"))
    print(f'B:root_hash={merkletree_B.get_root_hash()}\n')
    assert merkletree_B.get_root_hash() != None
    merkletree_B.print_level_order()
    
    assert merkletree_A.get_root_hash() == merkletree_B.get_root_hash()
    diff = MerkleTrees.compare(merkletree_A, merkletree_B)
    assert len(diff) == 0

    # dir_C/file3.txt contains different data than files in dir_A and dir_B
    merkletree_C = MerkleTrees()
    merkletree_C.build(read("./dir_C"))
    print(f'C:root_hash={merkletree_C.get_root_hash()}\n')
    assert merkletree_C.get_root_hash() != None
    merkletree_C.print_level_order()
    
    assert merkletree_A.get_root_hash() != merkletree_C.get_root_hash()
    diff = MerkleTrees.compare(merkletree_A, merkletree_C)
    assert len(diff) == 3

    list1, list2 = zip(*diff)
    print('\n##### DIFF #####')
    for x in list1:
        result = merkletree_A.txns.get(x)
        if result: print(result)
    
    for x in list2:
        result = merkletree_C.txns.get(x)
        if result: print(result)


if __name__ == "__main__":
    test()