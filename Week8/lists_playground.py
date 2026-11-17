seq = [2, 'a', 4, [1, 2]]
print("len(seq):", len(seq))
print("seq[3]:", seq[3])
print("seq[-1]:", seq[-1])
print("seq[3][0]:", seq[3][0])
try:
    print("seq[4]:", seq[4])
except IndexError as error:
    print("seq[4]:", type(error).__name__)
print("seq[1]:", seq[1])
print("seq[-2:]:", seq[-2:])
print("seq[1:3]:", seq[1:3])
print(seq)
import pdb
pdb.set_trace()
