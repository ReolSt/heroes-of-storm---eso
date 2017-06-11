고오급 레스토랑은 항상 고급스럽고, 여유가 있습니다. 손님들은 기다릴 줄 알며, 그 기다리는 과정 또한 즐기는 사람도 있습니다. 멀리서 봐도 고급스러운 향기가 풍기는 히오스의 원칙에 맞게, heros of storm - eso (저급한 사람들을 위해 약자인 hos-eso를 자주 씁니다.) 는 난해한 프로그래밍 언어(esolang)임에도 불구하고 파이썬의 많은 것을 물려받았으며, 고급 언어로써 쓰이도록 작성되었습니다. 지금은 기능이 많지 않지만, 차후에 함수, 예외처리, 심지어 객체지향까지 구현할 계획입니다. 뭐, 영웅을 새로 만들어서 임포트....그럴 필요도 없습니다! 직접 hos_heros와 hos_interprete에 작성해서 쓰세요! 이 무한한 자유도 또한 히오스의 고급스러움에서 옵니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 언어 스펙

## 1. 개요
hos-eso의 소스코드의 확장자는 .hos 입니다. 우리의 고급스러운 레스토랑은 가볍다거나, 빠르다거나, 그런 저급한 것들은 용납하지 않습니다. 따라서 기본적으로 hos-eso의 숫자 자료형은 전부 float(실수)로 고정됩니다. 또한 고급스러운 파이썬의 많은 것을 물려받고, 파이썬 기본 인터프리터 위에서 돌아가며, 모든 변수들은 variables 딕셔너리에 저장됩니다. 모든 스킬-기능(skill naming-function)들은 어떤 영웅의 메소드이며, 스킬-기능은 모드(mode)를 가질수도 있고 가지지 않을 수도 있습니다. 또한 모드가 모드를 가질 수 있습니다. 만약, 어떤 영웅이 스킬을 무한적으로 가진다고 해보죠, 그러면 그 영웅의 스킬-기능은 이론적으로 무한개 만들어질 수 있습니다(모드의모드의모드의모드의모드의............). 이 놀라운 확장성 또한 히오스의 고급스러움에서 옵니다.!!!!!!!!!!!!!!!!

## 2. 영웅들(Heroes)

### HERO - Tassadar
변수에 관련된 것들을 다룹니다. 엘리트 중의 엘리트인 Tassadar는 사이오닉 에너지도 잘 다루지만 데이터도 잘 다룬다고 하더군요.


- `psiinfusion` 다양한 형태의 변수를 선언하고, 값을 변경하는 역할을 합니다.
  - 모드를 설정하지 않은 경우에는 기본적으로 stirng 형태로 저장되므로, 문자열을 저장할 것이 아니라면 모드를 사용해야 할 것입니다.

- `focusedbeam 모드` 변수의 이름과 값을 받아 그 값을 float형태로 변환하여 저장합니다.

- `psionicecho 모드` 기본적인 것은 focusedbeam모드와 같지만, 구분자 storm으로 구분된 값들을 자료형을 float으로 바꾸어 리스트 형태로 저장합니다.

- `psionicechoW 모드` 기본적인 것은 focusedbeam모드와 같지만, 구분자 storm으로 구분된 값들을 string 자료형으로 리스트 형태로 저장합니다.

- `templarswill 모드` 이 스킬이 psiinfusion의 모드인지, 모드가 아닌지는 좀 더 생각해 보아야 겠지만, 일단 psiinfusion 없이는 값을 변수에 저장할 수 없으니, psiinfusion - 파생 모드라고 하겠습니다. 이 모드는 또한 4가지 모드를 가지고 있습니다.

  - `khalascelerity 모드` 리스트를 받아 sum(summary)을 계산하여 psiinfusion으로 보냅니다.
  - `khalasembrace 모드` khalascelerity와 기본적인 것은 같지만 len(length)을 계산합니다.
  - `khalashighlight 모드` max를 계산합니다.
  - `khalaslowlight 모드` min을 계산합니다.

### HERO - Tracer
시간 역행을 사용하여 여기저기 종횡무진하며 활약하는 우리의 고급 트레이서는 hos-eso에서도 고급스럽게 돌아다니며 제어문을 만듭니다.

* `spatialecho` 일반적인 고급 언어의 if와 비슷합니다. 첫번째 값(valuea)와 두번째 값(valueb)를 비교하여, true일 경우 그대로 진행하다가,

영웅 이름 뒤에 ;compositionb가 달려 있는 라인을 만나면 건너뛰고, 반대로 false일 경우 compostionb가 처음으로 달리는 라인부터 진행합니다.

true일 경우 false에 해당하는 라인은 전부 건너뛰어야 하기 때문에, 어디까지가 false에 해당하는 라인인지를 알아야 합니다. 따라서 false에

해당하는 라인에 compositionb를 명시해야만 합니다.

getstuffed! 모드 : valuea > valueb

getstuffed! 모드 ; valuea >= valueb

!deffutsteg 모드 : valuea < valueb

deffutsteg 모드 : valuea <= valueb

lockedandloaded 모드 : valuea == valueb

loadedandlocked 모드 : valuea != valueb


totalrecall : 일반적인 고급 언어의 while과 비슷합니다. 첫번째 값(valuea)와 두번째 값(valueb)를 비교하여, true일 동안 영웅 이름 뒤에

;compostiona가 명시되어 있는 라인을 반복해서 진행합니다. while문과 동일하게, 한번 루프가 진행될 때마다 조건을 검사합니다.

모드 : valuea > valueb

모드 : valuea >= valueb

모드 : valuea < valueb

모드 : valuea <= valueb

모드 : valuea == valueb

모드 : valuea != valueb
