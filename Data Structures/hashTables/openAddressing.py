# #######Linear Probing 
# In linear probing, collision is resolved by checking the next slot.

# h(k, i) = (h′(k) + i) mod m

# where

# i = {0, 1, ….}
# h'(k) is a new hash function
# If a collision occurs at h(k, 0), then h(k, 1) is checked. In this way, the value of i is incremented linearly.

# The problem with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table.



# #######Quadratic Probing 
# It works similar to linear probing but the spacing between the slots is increased (greater than one) by using the following relation.

# h(k, i) = (h′(k) + c1i + c2i2) mod m

# where,

# c1 and c2 are positive auxiliary constants,
# i = {0, 1, ….}



# #######Double Hashing
# If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot.

# h(k, i) = (h1(k) + ih2(k)) mod m