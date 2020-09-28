# Sort

> 정렬은 n개의 숫자를 사용자가 지정한 기준에 맞게 나열하는 알고리즘이다. 



## Array.sort()

> js에서 배열에 들어있는 원소들을 정렬하여 반환하는 메소드이다.
>
> 기본 정렬순서는 문자열의 유니코드 코드 포인트를 따른다.



`arr.sort([compareFunction])`

#### 매개변수

`compareFunction` [optional]

> 정렬순서를 정의하는 함수
>
> 생략시 문자열 변환에 따라 각 문자의 유니코드 코드 포인트 값을 따라 정렬

#### 반환 값

> 정렬한 배열, 원 배열이 정렬됨, 복사본이 생성되는 것이 아님

#### compareFunction

`compareFunction(a,b)`이 0보다 작은 경우 => a를 b보다 낮은 색인으로 정렬

`compareFunction(a,b)`이 0인 경우 => 서로에 대해 변경하지 않음

`compareFunction(a,b)`이 0보다 큰 경우 => b를 a보다 낮은 인덱스로 소트

#### EX Code

```javascript
let numbers = [4,2,5,1,3];
numbers.sort((a, b) => {
  return a - b;
}); // [1,2,3,4,5]

numbers.sort((a, b) => {
  return b - a;
}); // [5,4,3,2,1]
```



## Selection Sort

> 선택정렬

![Selection sort animation.gif](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Selection_sort_animation.gif/220px-Selection_sort_animation.gif)

![img](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)



#### 시간복잡도

__최악 시간복잡도__: O(n^2)

__최선 시간복잡도__: O(n^2)

__평균 시간복잡도__: O(n^2)



#### 예제

| 패스 |        테이블         | 최솟값 |
| :--: | :-------------------: | :----: |
|  0   | [**9,1,6,8,4,3,2,0**] |   0    |
|  1   | [0,**1,6,8,4,3,2,9**] |   1    |
|  2   | [0,1,**6,8,4,3,2,9**] |   2    |
|  3   | [0,1,2,**8,4,3,6,9**] |   3    |
|  4   | [0,1,2,3,**4,8,6,9**] |   4    |
|  5   | [0,1,2,3,4,**8,6,9**] |   6    |
|  6   | [0,1,2,3,4,6,**8,9**] |   8    |

#### Code

1. 주어진 리스트 중에 최소값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.



```javascript
function selectionSort(arr){
  let minIdx;	
  let tmp;
  
  for(let i = 0; i < arr.length - 1; i++){
    let minIdx = i;
    
    for(let j = i + 1; j < arr.length; j++){
      if(arr[j] < arr[minIdx]) minIdx = j;
    }
    
    tmp = arr[minIdx];
    arr[minIdx] = arr[i];
    arr[i] = tmp;
    console.log(arr);
  }
  return arr;
}
```



## Insertion Sort

> 삽입정렬

![img](https://upload.wikimedia.org/wikipedia/commons/2/25/Insertion_sort_animation.gif)

![img](https://upload.wikimedia.org/wikipedia/commons/e/ea/Insertion_sort_001.PNG)

#### 시간복잡도

__최악 시간복잡도__: O(n^2)

__최선 시간복잡도__: O(n) 비교, O(1) 교환

__평균 시간복잡도__: O(n^2)



#### 예제

31 25 12 22 11 -> 처음 상태

31 __25__ 12 22 11 -> 두 번째 원소를 부분 리스트에서 적절한 위치에 삽입한다

__25__ 31 __12__ 22 11 -> 세 번째 원소를 부분 리스트에서 적절한 위치에 삽입한다

__12__ 25 31 __22__ 11 -> 네 번째 원소를 부분 리스트에서 적절한 위치에 삽입한다

12 __22__ 25 31 __11__ -> 마지막 원소를 부분 리스트에서 적절한 위치에 삽입한다

__11__ 12 22 25 31 -> 종료



#### Code

현재 값을 이미 정렬된 배열에 알맞은 위치에 삽입한다



```javascript
function insertionSort(arr){
    for(let i = 1; i < arr.length; i++){
        let temp = arr[i];
        let cur = i - 1;
        
        while((cur >= 0) && (arr[cur] > temp)){
            arr[cur+1] = arr[cur];
            cur -= 1;
        }
        arr[cur + 1] = temp;
    }
}
```



## Bubble Sort

> 버블 정렬

![img](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif)



#### 예제

```
55 07 78 12 42  초기값[파란색은 sorting]
07 55 78 12 42  첫 번째 패스(pass)
07 55 78 12 42
07 55 12 78 42
07 55 12 42 78  두 번째 패스(pass)
07 55 12 42 78
07 12 55 42 78
07 12 42 55 78  세 번째 패스(pass)
07 12 42 55 78  네 번째 패스(pass)
07 12 42 55 78  다섯 번째 패스(pass)
07 12 42 55 78  정렬 끝
```



#### 시간복잡도

__최악 시간복잡도__: O(n^2)

__최선 시간복잡도__: O(n) 비교, O(1) 교환

__평균 시간복잡도__: O(n^2)



#### Code

현재 값과 다음 값을 비교하여 정렬, 이 과정을 배열의 길이만큼 반복



```javascript
function bubbleSort(arr){
    let tmp = 0;
    for(let i = 0; i < arr.length; i++){
        for(let j = 1; j < arr.length - i; j++){
            if(arr[j] < arr[j - 1]){
                temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}
```



## Merge Sort

> 합병 정렬

![Merge-sort-example-300px.gif](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif)



#### 시간복잡도

__최악 시간복잡도__: O(nlog n)

__최선 시간복잡도__: O(nlog n)

__평균 시간복잡도__: O(nlog n)



#### Code

__n-way 합병 정렬의 개념은 다음과 같다.__

1. 정렬되지 않은 리스트를 각각 하나의 원소만 포함하는 n개의 부분리스트로 분할한다. (한 원소만 든 리스트는 정렬된 것과 같으므로)
2. 부분리스트가 하나만 남을 때까지 반복해서 병합하며 정렬된 부분리스트를 생성한다. 마지막 남은 부분리스트가 정렬된 리스트이다.

__흔히 쓰이는 하향식 2-way 합병 정렬은 다음과 같이 작동한다.__

1. 리스트의 길이가 1 이하이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
2. 분할(divide) : 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
3. 정복(conquer) : 각 부분 리스트를 [재귀](https://ko.wikipedia.org/wiki/재귀함수)적으로 합병 정렬을 이용해 정렬한다.
4. 결합(combine) : 두 부분 리스트를 다시 하나의 정렬된 리스트로 [합병](https://ko.wikipedia.org/w/index.php?title=합병_알고리즘&action=edit&redlink=1)한다. 이때 정렬 결과가 임시배열에 저장된다.
5. 복사(copy) : 임시 배열에 저장된 결과를 원래 배열에 복사한다.



```javascript
let mergeSort = function(arr) {
  if (arr.length < 2) return arr; 
  let pivot = Math.floor(arr.length / 2); 
  let left = arr.slice(0, pivot); 
  let right = arr.slice(pivot, arr.length); 
  
  return merge(mergeSort(left), mergeSort(right)); 
}

function merge(left, right) {
  let result = [];
  while (left.length && right.length) {
    if (left[0] <= right[0]) { 
      result.push(left.shift()); 
    } else {
      result.push(right.shift()); 
    }
  }
  while (left.length) result.push(left.shift()); 
  while (right.length) result.push(right.shift()); 
  return result;
};
```



## Quick Sort

> 퀵 정렬

![Sorting quicksort anim.gif](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Sorting_quicksort_anim.gif/220px-Sorting_quicksort_anim.gif)



#### 시간복잡도

__최악 시간복잡도__: O(n^2)

__최선 시간복잡도__: O(nlog n)

__평균 시간복잡도__: O(nlog n)



#### 예제

피벗은 p, 리스트 왼쪽 끝과 오른쪽 끝에서 시작한 인덱스들을 i,j라고 하자.

```
5 - 3 - 7 - 6 - 2 - 1 - 4 
                        p 
```

리스트 왼쪽에 있는 i 위치의 값이 피벗 값보다 크고, 오른쪽에 있는 j 위치의 값은 피벗 값보다 작으므로 둘을 교환한다.

```
5 - 3 - 7 - 6 - 2 - 1 - 4 
i                   j   p 
1 - 3 - 7 - 6 - 2 - 5 - 4 
i                   j   p 
```

j 위치의 값이 피벗 값보다 작지만, i 위치의 값도 피벗값보다 작으므로 교환하지 않는다.

```
1 - 3 - 7 - 6 - 2 - 5 - 4 
    i           j       p 
```

i위치를 피벗 값보다 큰 값이 나올 때까지 진행해 j 위치의 값과 교환한다.

```
1 - 3 - 7 - 6 - 2 - 5 - 4 
        i       j       p 
1 - 3 - 2 - 6 - 7 - 5 - 4 
        i       j       p 
```

i위치가 j 위치보다 커지면, i 위치의 값과 피벗 값을 교환한다.

```
1 - 3 - 2 - 6 - 7 - 5 - 4 
                        p 
1 - 3 - 2 - 4 - 7 - 5 - 6 
            p             
```

피벗 값 좌우의 리스트에 대해 각각 퀵 정렬을 재귀적으로 수행한다.

```
1 - 3 - 2       7 - 5 - 6
1 - 2 - 3       5 - 6 - 7
```

완성된 리스트는 다음과 같다.

```
1 - 2 - 3 - 4 - 5 - 6 - 7
```



#### Code

__퀵 정렬은 [분할 정복(divide and conquer)](https://ko.wikipedia.org/wiki/분할_정복_알고리즘) 방법을 통해 리스트를 정렬한다.__

1. 리스트 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 **피벗**이라고 한다.
2. 피벗 앞에는 피벗보다 값이 작은 모든 원소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 모든 원소들이 오도록 피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 리스트를 둘로 나누는 것을 **분할**이라고 한다. 분할을 마친 뒤에 피벗은 더 이상 움직이지 않는다.
3. 분할된 두 개의 작은 리스트에 대해 [재귀(Recursion)](https://ko.wikipedia.org/wiki/재귀함수)적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1이 될 때까지 반복된다.

재귀 호출이 한번 진행될 때마다 최소한 하나의 원소는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.



```javascript
let partition = function(array, left, right, pivotIndex) { 
  let temp;
  let pivot = array[pivotIndex];
  while (left <= right) { 
    while (array[left] < pivot)
      left++;
    while (array[right] > pivot)
      right--;
    if (left <= right) { 
      temp = array[left];
      array[left] = array[right];
      array[right] = temp; 
      left++;
      right--;
    }
  }
  temp = array[left];
  array[left] = array[pivotIndex];
  array[pivotIndex] = temp; 
  return left;
};

let quickSort = function(array, left, right) {
  if (!left) left = 0;
  if (!right) right = array.length - 1;
  let pivotIndex = right; 
  pivotIndex = partition(array, left, right - 1, pivotIndex); 
  if (left < pivotIndex - 1)
    quickSort(array, left, pivotIndex - 1); 
  if (pivotIndex + 1 < right)
    quickSort(array, pivotIndex + 1, right);
  return array;
};
```

