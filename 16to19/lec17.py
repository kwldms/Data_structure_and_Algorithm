# 트리(Trees)
"""
트리
정점(node)과 간선(edge)을 이용하여 데이터의 배치 형태를 추상화한 자료 구조
뿌리(root)가 위에 있고 가지치기를 하여 잎(leaf)을 생성함.

루트 노드/리프 노드/내부(internal) 노드
뿌리에 위치한 노드/가지를 치지 않은 노드/루트도 리프도 아닌 노드

부모 노드와 자식 노드
엣지로 연결되어 뿌리쪽에 가까운 노드를 부모노드, 그와 연결된 노드를 자식 노드라고 함
자식 노드는 여러 개일 수 있지만 부모 노드는 무조건 하나이다.

노드의 수준(level)
루트 노드는 level 0이라고 정의
루트 노드와 연결된 자식 노드는 level 1이며, 자식 노드로 갈수록 하나씩 증가한다.
루트 노드로부터 거쳐야 하는 간선의 수를 해당 노드의 레벨이라고 정의한다.

트리의 높이(또는 깊이)
= 최대 수준 + 1

노드의 차수(degree)
= 자식(서브트리)의 수
차수=0인 경우, leaf node라고 부른다.

이진 트리(binary tree)
: 모든 노드의 차수가 2 이하인 트리.
: 트리는 본질적으로 재귀적인 성질을 가짐.
즉, 빈 트리(empty tree)이거나 루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리
( 단, 왼쪽과 오른쪽 서브트리 또한 이진 트리)

포화 이진 트리(full binary tree)
: 모든 레벨에서 노드들이 모두 채워져 있는 이진 트리
(높이가 k이고 노드의 개수가 2**k-1인 이진 트리

완전 이진 트리(complete binary tree)
: 높이 k인 완전 이진 트리로,
level k-2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리
level k-1(맨 밑 노드의 수준)에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리

"""