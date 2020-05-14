# Requirements

Implement a Merkle tree to detect differences between directories. The detection mechanism is solely focused on the file content and ignores file and directory names. You must use _hashlib.sha256_ for all hashing.

> You must use given hash_files.py and test_merkle_trees.py to validate your solution. Although you are allowed to change anything inside merkle_trees.py, any modifications to hash_files.py and test_merkle_trees.py will negatively impact your score.

# Test Data

All directories have the same number of files with the same name. However, dir_C/file3.txt has

```
Merkleeeeeeeee
```

while the other file3.txt in dir_A and dir_B has

```
Merkle
```


# Expected Output

```sh
python3 test_merkle_trees.py 
dir_A/file2.txt
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524
dir_A/file3.txt
728beae3756e9ea17b15ecbc095a5c0d7bba2c3182b83606baf199560ba868ba
dir_A/file1.txt
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
dir_A/file4.txt
109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a
A:root_hash=cc17dcfce23ead93ebe280fe0ce60e61ef94303e0a97eab19e844170277d1424

cc17dcfce23ead93ebe280fe0ce60e61ef94303e0a97eab19e844170277d1424 
--------------------
ca75583f7ed36fc3234bf06ed6460ea222430e53a7e5eadd6f0c8a5ffa36e7ef b621554f096c88f48aae852488a4753cdac568a918648363f886665aef15a50f 
--------------------
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524 728beae3756e9ea17b15ecbc095a5c0d7bba2c3182b83606baf199560ba868ba 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969 109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a 
--------------------
dir_B/file2.txt
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524
dir_B/file3.txt
728beae3756e9ea17b15ecbc095a5c0d7bba2c3182b83606baf199560ba868ba
dir_B/file1.txt
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
dir_B/file4.txt
109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a
B:root_hash=cc17dcfce23ead93ebe280fe0ce60e61ef94303e0a97eab19e844170277d1424

cc17dcfce23ead93ebe280fe0ce60e61ef94303e0a97eab19e844170277d1424 
--------------------
ca75583f7ed36fc3234bf06ed6460ea222430e53a7e5eadd6f0c8a5ffa36e7ef b621554f096c88f48aae852488a4753cdac568a918648363f886665aef15a50f 
--------------------
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524 728beae3756e9ea17b15ecbc095a5c0d7bba2c3182b83606baf199560ba868ba 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969 109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a 
--------------------
dir_C/file2.txt
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524
dir_C/file3.txt
87e4b0c5a8378e9c12a9eba2f8943f5b568c6168749a974cf367ea77d36d232c
dir_C/file1.txt
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
dir_C/file4.txt
109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a
C:root_hash=48b78e427b81c3dfd8589c902d3709a89f61ec6c4bfea955a7a11f3d05bf6561

48b78e427b81c3dfd8589c902d3709a89f61ec6c4bfea955a7a11f3d05bf6561 
--------------------
4f7f63dcbc4d85888616a42e3c20b5d3a3c1941300351e4103dcf71d228f0704 b621554f096c88f48aae852488a4753cdac568a918648363f886665aef15a50f 
--------------------
78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524 87e4b0c5a8378e9c12a9eba2f8943f5b568c6168749a974cf367ea77d36d232c 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969 109d6f455ed8c31a49197e9d1ca5241f95e8e593dc23412ef206aa9d07563b5a 
--------------------

##### DIFF #####
dir_A/file3.txt
dir_C/file3.txt
```
