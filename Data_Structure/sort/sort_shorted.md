# 정렬이란? 

정렬이란 데이터 집합을 대소관계에 따라 일정한 순서로 바꾸어 늘어놓는 작업을 의미한다.

데이터를 정렬하면 더 쉽게 검색할 수 있다.

값이 작은 데이터를 앞에 늘어놓는 것을 오름차순, 그 반대를 내림차순이라고 한다.

## 내부정렬? 외부정렬?

* 내부 정렬: 정렬할 모든 데이터를 하나의 배열에 저장할 수 있는 경우 사용하는 알고리즘
* 외부 정렬: 정렬할 데이터가 많아 하나의 배열에 저장할 수 없는 경우 사용하는 알고리즘

## 정렬의 기본 동작 
대부분의 정렬 알고리즘은 **교환, 선택, 삽입** 이 3가지의 동작을 응용하고 있다.

## 정렬들의 시간복잡도
|Name|Best|Avg|Worst|
|------|---|---|---|
|버블 정렬|O(n^2)|O(n^2)|O(n^2)|
|선택 정렬|O(n^2)|O(n^2)|O(n^2)|
|삽입 정렬|O(n)|O(n^2)|O(n^2)|
|셸 정렬|O(n)|O(n^1.5)|O(n^2)|
|퀵 정렬|O(nlog2n)|O(nlog2n)|O(n^2)|
|병합 정렬|O(nlog2n)|O(nlog2n)|O(nlog2n)|
|힙 정렬|O(nlog2n)|O(nlog2n)|O(nlog2n)|
|도수 정렬|O(n+k)|O(n+k)|O(n+k)|



## 정렬

---

### 버블 정렬
> 버블 정렬은 이웃한 두 원소의 대소관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘으로 단순 교환 정렬이라고도 한다.

#### 장 단점
* 장점: 구현이 쉽다, 코드가 직관적이다
* 단점: 굉장히 비효율적이다

#### 시간복잡도 
* Best: O(n^2)
* AVG: O(n^2)
* Worst: O(n^2)

--- 

### 선택 정렬
> 선택 정렬은 가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복하여 정렬하는 알고리즘이다. 

#### 장 단점
* 장점: 구현이 쉽다, 정렬을 위한 비교횟수는 많지만 실제로 교환하는 횟수는 적기 때문에 교환이 일어나야 하는 자료상태에서 효율적이다. 버블 정렬보다 조금 빠르다
* 단점: 시간복잡도가 항상 O(n^2)이다

#### 시간복잡도 
* Best: O(n^2)
* AVG: O(n^2)
* Worst: O(n^2)

---

### 삽입 정렬
> 삽입 정렬은 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하여 정렬하는 알고리즘이다. 

#### 장 단점
* 장점: 최선의 경우 O(n)이라는 굉장히 빠른 효율성을 가지고 있다. 성능이 좋아 다른 알고리즘의 일부로 사용되는 경우가 많다.
* 단점: 최악의 경우 O(n^2)의 시간복잡도를 가지게 된다. 삽입할 위치가 멀리 떨어져 있으면 이동 횟수가 많아진다.

#### 시간복잡도 
* Best: O(n)
* AVG: O(n^2)
* Worst: O(n^2)

---

### 셸 정렬
> 셸 정렬은 삽입정렬의 장점은 살리고 단점은 보완하여 더 빠르게 정렬하는 알고리즘이다.
> (장점: 최선인 경우 매우 빠름, 단점: 삽입할 위치가 멀리 떨어져 있으면 이동 횟수가 많음)
> 먼저 정렬할 배열의 원소를 그룹으로 나누어 각 그룹별로 정렬을 수행, 그 후 정렬된 그룹을 합치는 작업을 반복하여 원소의 이동 횟수를 줄이는 방법

#### 장 단점
* 장점: 삽입정렬의 단점을 보완하여 만든 정렬법으로 뛰어난 정렬법이다
* 단점: 일정한 간격에 따라서 배열을 바라봐야한다.이 간격을 잘못설정한 경우 성능이 매우 안 좋아진다.

#### 시간복잡도 
* Best: O(n)
* AVG: O(n^1.5)
* Worst: O(n^2)

---

### 퀵 정렬
>퀵 정렬은 가장 빠른 알고리즘으로 알려져 있으며 널리 사용된다.

#### 장 단점
* 장점: 실행시간이 빠른 편이다
* 단점: pivot에 의해서 성능의 차이가 심하다, 최악의 경우 O(n^2)의 시간복잡도를 가진다, 원소수가 적은 경우 그다지 빠른 정렬이 아니다

#### 시간복잡도 
* Best: O(nlog2n)
* AVG: O(nlog2n)
* Worst: O(n^2)

---

### 병합 정렬
>병합 정렬은 배열 앞부분과 뒷부분의 두 그룹으로 나누어 각각 정렬한 후 병합하는 작업을 반복하는 알고리즘이다

#### 장 단점
* 장점: 항상 O(nlog2n)으로 빠른 편이다
* 단점: 추가적인 메모리 공간을 필요로한다.

#### 시간복잡도 
* Best: O(nlog2n)
* AVG: O(nlog2n)
* Worst: O(nlog2n)

---

### 힙 정렬
>힙 정렬은 힙의 특성을 이용하여 정렬하는 알고리즘이다

#### 장 단점
* 장점: 항상 O(nlog2n)으로 빠른 편이다
* 단점: 실제 시간이 O(nlog2n)보다 느리다

#### 시간복잡도 
* Best: O(nlog2n)
* AVG: O(nlog2n)
* Worst: O(nlog2n)

---

### 도수 정렬
>도수 정렬은 원소의 대소 관계를 판단하지 않고 빠르게 정렬하는 알고리즘으로 분포수 세기 정렬이라고도 한다

#### 장 단점
* 장점: O(n+k)이라는 말도 안되는 속도를 갖는다
* 단점: 추가적인 메모리가 많이 필요하다, 데이터 타입이 일정해야 한다, 구현을 위한 조건이 많이 붙는다

#### 시간복잡도 
* Best: O(n+k)
* AVG: O(n+k)
* Worst: O(n+k)
