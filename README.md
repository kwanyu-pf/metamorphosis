# 개요

프로젝트 트로이 진행 도중, finda에서 온 API Request에 대해서 inapi와 PFLoanApplication(향후 loan-agent)의 sync를 맞추는 데 어려움이 있습니다.

해당 시나리오는 이벤트를 이용해서 쉽게 해결 가능할 것 같은데, Kafka 활용이 미숙하여 REST API로 구현되었습니다.

같은 시나리오를 구현한 후 test까지 진행하여 Kafka의 효용성을 파악합니다. 만약 성공적일 경우, 실제 Kafka를 실제 서비스에 쉽게 도입할 수 있을 것 같습니다.

# 시나리오

## 신규유저

1. 신규 유저가 핀다에서 가심사까지 FEPInstitution을 호출하며 진행한다.
2. 유저가 PFLoanApplication으로 넘어와서 회원가입을 진행한다.
3. 기존의 가심사 결과부터 진행한다.

## 기존유저

1. 기존 유저가 핀다에서 가심사까지 FEPInstitution을 호출하며 진행한다.
2. 유저가 PFLoanApplication으로 넘어와서 로그인을 진행한다.
3. 기존의 가심사 결과부터 진행한다.