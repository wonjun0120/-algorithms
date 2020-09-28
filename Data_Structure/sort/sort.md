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

1. 현재 값을 이미 정렬된 배열에 알맞은 위치에 삽입한다



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

#### 시간복잡도

##### 최악 시간복잡도

##### 최선 시간복잡도

##### 평균 시간복잡도

#### Code

## Merge Sort

> 합병 정렬

#### 시간복잡도

##### 최악 시간복잡도

##### 최선 시간복잡도

##### 평균 시간복잡도

#### Code

## Quick Sort

> 퀵 정렬

#### 시간복잡도

##### 최악 시간복잡도

##### 최선 시간복잡도

##### 평균 시간복잡도

#### Code

