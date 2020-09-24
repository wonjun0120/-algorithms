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



## Insertion Sort

> 삽입정렬



## Bubble Sort

> 버블 정렬



## Merge Sort

> 합병 정렬



## Quick Sort

> 퀵 정렬



