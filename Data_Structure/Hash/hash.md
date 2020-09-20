# Hash



## Hash-Function

> 해시함수는 임의의 길이를 가진 데이터를 고정된 길이의 데이터로 매핑하는 함수를 말한다. 
>
> 해시함수의 input값을 `key`, output값을 `해시`, `해시값`, `해시 코드`, `해시 체크섬` 이라고 한다. 
>
> 해시함수를 사용하면 무조건 정해져있는 길이의 데이터가 반환되기때문에 이미 저장된 데이터를 검색할 때 사용하면 검색시간을 고속화할 수 있다. (`해시 테이블`)
>
> 해시 값을 가지고 어떤 `key`(해시 함수의 input)였는지 알아내기 힘든 점을 사용하여 암호화에 사용한다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Hash_table_4_1_1_0_0_1_0_LL.svg/1920px-Hash_table_4_1_1_0_0_1_0_LL.svg.png" width=500 />



## Hash-Table

> 해시 테이블은 해시함수를 사용하여 키를 값에 매핑할 수 있는 자료 구조를 의미한다. 
>
> 해시는 해시함수를 사용하는 것을 의미하고, 테이블은 키-값 쌍으로 저장되는 구조를 의미한다. 
>
> 해시 테이블은 해시 함수의 input으로 key값을 사용했을 때 얻어지는 해시 값(output)을 value가 저장되는 주소에 사용한다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1920px-Hash_table_3_1_1_0_1_0_0_SP.svg.png" width=500 />

### Code

```javascript

```





### Time Complexity

|             | 탐색 | 삽입 | 삭제 |
| ----------- | ---- | ---- | ---- |
| 최선의 경우 | O(1) | O(1) | O(1) |
| 최악의 경우 | O(n) | O(n) | O(n) |

__최선의 경우__: 서로 다른 key로 얻어지는 해시 값이 모두 다른 경우 (해당 저장공간당 1개의 `value`)

__최악의 경우__: 서로 다른 key로 얻어지는 해시 값이 모두 같은 경우 (1개의 저장공간에 모든 `value`가 저장되는 경우)













