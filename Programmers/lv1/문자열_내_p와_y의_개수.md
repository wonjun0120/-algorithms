[문제 이동](https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3)
### solution
```python3
def solution(s):
    answer = True
    np = ny = 0
    for i in s:
        if i == 'p' or i == 'P':np += 1
        if i == 'y' or i == 'Y':ny += 1
    return np == ny 
```

### 풀이과정 
1. 입력받은 문자열 순회, i
2. i가 p, P인 경우 np += 1
3. i가 y, Y인 경우 ny += 1
4. np와 ny가 같으면 True 아니면 False

### 다른 방법
```python3
def solution(s):
  return s.lower().count('p') == s.lower().count('y')
```
 -> lower과 count사용
