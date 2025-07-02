from typing import List,Optional
def names(n:List[str],seperator:Optional[str]=' ')->str:
    return seperator.join(n)
print(names(['Ram','Prasanna','vinay']))
print(names(['78','IT'],seperator='-'))