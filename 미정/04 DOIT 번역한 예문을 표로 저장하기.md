# 번역한 예문을 표로 저장하기


```
import re, os, usecsv
```


```
import csv, os

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    
def writecsv(filename, the_list):
    with open(filename, 'w', newline= '') as f:
        a = csv.writer(f, delimiter =',')
        a.writerows(the_list)
        
def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return listName


```


```
English = 'She is a vegetarian. She does not eat meat. She thinks that the animals should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughted at her. She realized they couldn\'t give up meat'
# 영문을 English 객체에 저장

Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이면 안된다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었습니다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'
# 영문을 구글 번역기로 번역해 Korean 객체에 저장

os.chdir(r'C:\Users\rlagu\OneDrive\Documents\Python\Python')
# CSV 파일을 저장하고 싶은 폴더로 이동
```


```
Korean_list = re.split('\.', Korean)
# split()함수로 한글 문장을 나눠서 Korean_list에 저장

English_list = re.split('\.', English)
# 영문도 마침표를 기준으로 나눠서 English_list에 저장

print(Korean_list)
```

    ['그녀는 채식주의자입니다', ' 그녀는 고기를 먹지 않습니다', ' 그녀는 동물을 죽이면 안된다고 생각합니다', ' 그녀가 사람들과 어울리는 것은 어렵습니다', ' 많은 사람들이 고기를 좋아합니다', ' 그녀는 부모에게 고기를 먹지 말라고 말했습니다', ' 그들은 그녀를 비웃었습니다', ' 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다', '']
    


```
total = []
# CSV형 리스트를 저장할 빈 리스트 생성

for i in range(len(English_list)):
# for문을 English_list 객체에 들어있는 문장 수만큼 생성
    total.append([English_list[i], Korean_list[i]])
#첫번째 열에 영어 문장, 두 번째 열에 한국어 문장이 들어 있는 리스트를 total에 추가

usecsv.writecsv('Korean_English.csv', total)
```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


```

```
