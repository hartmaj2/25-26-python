# Count equivalence classes of the relation x ~ y iff log_2(x/y) \in Z

# First divide into equivalence classes

# Then check if really the condition holds for the members of the equivalence classes

import math

s = [x for x in range(1,1001)]

def generate_classes(base_set : list[int]):
    classes = []
    while len(base_set) > 0:
        cls = []
        cur = base_set[0]
        while cur in base_set:
            base_set.remove(cur)
            cls.append(cur)
            cur *= 2
        # print(cls)
        classes.append(cls)
    return classes

def check_class(cls : list[int]):
    for i in range(len(cls)):
        for j in range(i+1,len(cls)):
            res = math.log2(cls[i]/cls[j])
            if not res.is_integer():
                return False
            # print(f"{cls[i]} and {cls[j]} : {res}")
            # print(f"{res} is integer: {res.is_integer()}")
    # print(f"{cls} is valid class")
    return True


classes = generate_classes(s)

for cls in classes:
    if not check_class(cls):
        print(f"{cls} is invalid")

print(f"Num classes: {len(classes)}")

