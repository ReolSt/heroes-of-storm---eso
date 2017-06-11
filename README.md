# heroes-of-storm---eso
This is a repository of an esolang named 'heros of storm - eso'
고오급 레스토랑은 항상 고급스럽고, 여유가 있습니다. 손님들은 기다릴 줄 알며, 그 기다리는 과정 또한 즐기는 사람도
있습니다. 멀리서 봐도 고급스러운 향기가 풍기는 히오스의 원칙에 맞게, heros of storm - eso (저급한 사람들을 위해
약자인 hos-eso를 자주 씁니다.) 는 난해한 프로그래밍 언어(esolang)임에도 불구하고 파이썬의 많은 것을 물려받았으며,
고급 언어로써 쓰이도록 작성되었습니다. 지금은 기능이 많지 않지만, 차후에 함수, 예외처리, 심지어 객체지향까지
구현할 계획입니다. 뭐, 영웅을 새로 만들어서 임포트....그럴 필요도 없습니다! 직접 hos_heros와 hos_interprete에
작성해서 쓰세요! 이 무한한 자유도 또한 히오스의 고급스러움에서 옵니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

언어 스펙
1. 개요
hos-eso의 소스코드의 확장자는 .hos 입니다. 우리의 고급스러운 레스토랑은 가볍다거나, 빠르다거나, 그런 저급한 것들은
용납하지 않습니다. 따라서 기본적으로 hos-eso의 숫자 자료형은 전부 float(실수)로 고정됩니다.
또한 고급스러운 파이썬의 많은 것을 물려받고, 파이썬 기본 인터프리터 위에서 돌아가며, 모든 변수들은 variables
딕셔너리에 저장됩니다. 모든 스킬-기능(skill naming-function)들은 어떤 영웅의 메소드이며, 스킬-기능은 모드(mode)를
가질수도 있고 가지지 않을 수도 있습니다. 또한 모드가 모드를 가질 수 있습니다. 만약, 어떤 영웅이 스킬을 무한적으로
가진다고 해보죠, 그러면 그 영웅의 스킬-기능은 이론적으로 무한개 만들어질 수 있습니다(모드의모드의
모드의모드의모드의............). 이 놀라운 확장성 또한 히오스의 고급스러움에서 옵니다.!!!!!!!!!!!!!!!!
2. 영웅들(Heroes)
HERO - Tassadar
변수에 관련된 것을을 다룹니다. 엘리트 중의 엘리트인 Tassadar는 사이오닉 에너지도 잘 다루지만 데이터도 잘 다룬다고
하더군요.
psiinfusion : 다양한 형태의 변수를 선언하고, 값을 변경하는 역할을 합니다.
모드를 설정하지 않은 경우에는 기본적으로 stirng 형태로 저장되므로, 문자열을 저장할 것이 아니라면 모드를 사용해야
할 것입니다.
focusedbeam 모드 : 변수의 이름과 값을 받아 그 값을 float형태로 변환하여 저장합니다.
psionicecho 모드 : 기본적인 것은 focusedbeam모드와 같지만, 구분자 storm으로 구분된 값들을 자료형을 float으로 바꾸어
                   리스트 형태로 저장합니다.
psionicechoW 모드 : 기본적인 것은 focusedbeam모드와 같지만, 구분자 storm으로 구분된 값들을 string 자료형으로 
                    리스트 형태로 저장합니다.
templarwill 모드 : 이 스킬이 psiinfusion의 모드인지, 모드가 아닌지는 좀 더 생각해 보아야 겠지만, 일단 psiinfusion 없이는
                   값을 변수에 저장할 수 없으니, psiinfusion - 파생 모드라고 하겠습니다. 이 모드는 또한 4가지 모드를 가지고
                   있습니다.
templarwill 모드의 khalascelerity 모드 : 리스트를 받아 sum(summary)을 계산하여 psiinfusion으로 보냅니다.
templarwill 모드의 khalasembrace 모드 : khalascelerity와 기본적인 것은 같지만 len(length)을 계산합니다.
templarwill 모드의 khalashighlight 모드 : max를 계산합니다.
templarwill 모드의 khalaslowlight 모드 : min을 계산합니다.
HERO - Tracer
시간 역행을 사용하여 여기저기 종횡무진하며 활약하는 우리의 고급 트레이서는 hos-eso에서도 고급스럽게 돌아다니며 제어문을 만듭니다.
spatialecho : 일반적인 고급 언어의 if와 비슷합니다. 첫번째 값(valuea)와 두번째 값(valueb)를 비교하여, true일 경우 그대로 진행하다가,
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
미구현 모드 : valuea > valueb
미구현 모드 : valuea >= valueb
미구현 모드 : valuea < valueb
미구현 모드 : valuea <= valueb
미구현 모드 : valuea == valueb
미구현 모드 : valuea != valueb
HERO - Jaina
마법을 잘 쓰려면 일단 머리를 잘 굴려야겠죠? 우리의 고급스러운 제이나짱은 마법을 더 빠르고 강하게 쓰기 위해서 구몬
학습지를 매일 하고 암산과 주판을 배운다고 합니다.
기본적인 사칙 연산을 포함한 연산자들을 포함하는 영웅입니다. 차후에 더 많은 기능을 담당할 수도 있고 아닐수도 있고...
frostbolt : 일반적인 고급 언어의 대입 연산자와 비슷한(거의 같은) 기능을 합니다.
wintersreach 모드 : +=과 같은 기능을 합니다.
lingeringchill 모드 : -=과 같은 기능을 합니다.
deepchill 모드 : (곱셈기호)=과 같은 기능을 합니다.
conjurerspursuit 모드 : /=과 같은 기능을 합니다.
HERO - Ragnaros
우리의 고급스럽고 강력한 불의 군주님은 불도 잘뿜지만 데이터도 잘뿜습니다. 또한 기를 모아서(input) 뿜는(print)것도
잘하신다고 하네요.
print, input 데이터 입출력을 다룹니다. 파일 입출력도 구현할 생각을 하고 있긴 하지만 다른 영웅이 담당할 수도 있습니다.
livingmeteor : 일반적인 고급 언어의 print(또는 printf) 와 비슷한 기능을 합니다. default 모드는 lavasurge 입니다.
lavasurge 모드 : reading code 3 의 문자열을 그대로 출력합니다.
flamesofsulfuron 모드 : reading code 3의 문자열과 같은 이름을 가진 변수를 variables에서 찾아 그 값을 출력합니다.
handofragnaros : 이 스킬-기능은 다른 스킬-기능과는 조금 다른점이 있는데, 일반적인 고급 언어에서 쓰는 input이나 scanf
                 가 아니라 파이썬 특유의 input에 기초해 만들어졌습니다.
engulfingflame 모드 : printstring을 받아서 그것을 출력하고 값을 입력받습니다. 이 때 입력받은 값은 float 자료형으로 
                      reading code 4의 문자열이 이름인 변수를 만들어 값을 저장합니다(이미 있는 변수에도 저장할 수
                      있습니다.
3. 문법
heros of storm - eso는 고급스러운 그 컨셉에 맞게 문법도 엄격하고 코드도 깁니다. 또한 기품을 유지하기 위해 가독성을
떨어뜨려 세심하게 보지 않으면 이해하기 어렵게 만들어졌습니다.
고급스러운 pyos-eso interpreter는 코드를 4줄씩 끊어서 읽습니다. 다만 맨 첫줄(리스트 인덱싱으로 0번째)에는 hos-eso코드임을
알리기 위해 무조건 heros of storm 이라고 작성해야 합니다. 그런 다음에 그 다음 줄부터 4줄씩 끊어 읽는 작업을 합니다.
Tassadar 클래스의 psiinfusion의 focusbeam을 예로 들어보죠.
Tassadarpsiinfusion;focusbeama30
보시는 바와 같이 맨 윗줄에는 영웅의 이름, 그 다음줄에는 스킬-기능과 모드를 명시합니다. 다만 구분자에는 한 글자인 어떤 글자가
와도 상관 없습니다.(그러나 아스키코드에 포함되지 않는 문자나 특수문자는 사용하지 않기를 권합니다.) 또한 인터프리터를 수정해서
유니코드, 특수문자, 그 외에 기괴한 문자들, 한글자 이상의 문자열을 구분자로 사용할 수 있습니다(꽤 귀찮은 작업이지만요).
그리고 그 다음 줄에는 값을 저장한 변수의 이름, 그 다음 줄에는 저장할 값을 입력해야 합니다.
pyos-eso interpreter가 현재 읽고 있는 4개의 줄을 통틀어 reading code 라고 부르고, 1,2,3,4번째 줄을 각각 reading code 1,
reading code 2, reading code 3, reading code 4 라고 합니다.
이번엔 Tracer의 spatialecho 스킬 - 기능의 getstuffed! 모드를 예로 들어보죠.
Tassadarpsiinfusion;focusbeama5Tassadarpsiinfusion;focusbeamb7Tracerspatialecho;getstuffed!astormb4storm8TassadarpsiinfusionctrueTassadar;compositionbpsiinfusioncfalseTassadar;compositionbpsiinfusiondfalsenexus
먼저 Tracer을 사용하는 reading code를 봅시다.Tracerspatialecho;getstuffed!astormb4storm8
reading code 1,2 에서는 위에서 설명한 것처럼 영웅이름과 스킬-기능, 모드에 대해 작성했지만, 3,4번째 줄에는 앞에서 보지 못했던 것들이 등장합니다.
astormb4storm8
이것인데요,
hos-eso는 시.공.좋.아 라서 reading code 3,4에서는 storm을 구분자로 사용합니다. 물론 무한한 자유도를 제공하는 hos-eso는 인터프리터를
수정해서 storm을 다른 글자로 바꿀 수 있게 해 놓았습니다. 그래도 reading code 1,2 에서 사용하는 구분자를 수정하는 것보다는 덜 귀찮
습니다.
이야기가 시공으로 벗어났네요, 다시 본론으로 들어가서, 먼저 reading code 3를 봅시다.
astormb
Tracer 클래스는 storm구분자로 구분된 두 문자열을 이름으로 가진 변수로 찾아 모드에 따라 그 둘을 비교합니다. 그런 뒤에 위에서 설명한
대로 스킬-기능이 작동하죠.
이제 reading code 4 를 봅시다.
4storm8
storm 구분자로 구분된 두 숫자는 각각 다른 의미를 가집니다. 먼저 첫번째 숫자인 4는 true일 경우 실행하는 reading code의 갯수를 뜻합니다.
그리고 두번째 숫자인 8은 false일 경우 실행할 reading code의 갯수를 뜻합니다. false일 경우에 실행할 reading code들의 reading code 1에는
compostionb가 명시되어야 함은 당연하겠죠?
이제 가장 마지막 줄인 nexus를 봅시다.
nexus
어라?
reading code는 4개의 line으로 구성되어있다고 했는데,
달랑 한줄이네요?
이유를 설명해 드리죠.
pyos-eso interpreter는 reading code를 읽어서 리스트 형태로 저장하기 전에, 첫번째 줄이 nexus인지 아닌지를 검사합니다. 맞게 쓰는 건지
모르겠지만, 저는 이것을 eof check라고 부릅니다.
만약 첫번째 줄이 nexus면 해석을 종료합니다.
설명은 끝났으니, 이제 결과를 봅시다.
.......
출력 함수도 안썼는데 어떻게 보냐고요?
당신은 pyos-eso interpreter의 강력한 기능을 아직 모르는군요,
pyos-eso interpreter는 변수들을 저장하는 딕셔너리를 해석이 끝난 뒤에 variables를 파이썬의 print 빌트인 함수를 이용해 출력합니다.
인터프리터를 수정에 중간에 print(variables)를 끼워넣어서 변수들이 어떻게 변화하는지를 볼 수 있죠.
자, 봅시다.
{'a': '5', 'b': '7', 'c': 'false', 'd': 'false'}
getstuffed! 모드를 사용하여 > 비교 연산자로 비교한 결과, 5 > 7 의 결과는 false 이므로. compostionb가 명시된 reading code로 넘어갑니다.
그런 뒤에 두 reading code를 수행한 후, nexus를 만나 프로그램을 종료합니다.
이번엔 a와 b의 값을 서로 바꿔볼까요?
{'a': '7', 'b': '5', 'c': 'true', 'e': 'hello'}
너무나도 잘 실행됩니다.
'e' : 'hello'는 제작자(본인)이 테스트를 위해 넣은 것이니 갑자기 튀어나왔다고 놀라지 마세요.
마지막으로 너무나도 유명한 hello, world 가 아니라, heroes of storm을 출력하는 예제로 설명을 마치도록 하죠.
heroes of stormRagnaroslivingmeteor;lavasurgeheroes of stormstormnexus
reading code 4가 storm인 이유는 livingmeteor는 reading code 4가 필요 없기 때문입니다. 이렇게 reading code에서 필요 없는 라인이 발생할
경우 storm을 입력할 것을 매우 강력히 권장합니다. 사실 뭐 아무 문자나 써도 되고 공백이어도 상관 없지만 되도록이면 storm을 입력해 주세요.
이제 결과를 봅시다.
heroes of storm{}
잘 실행되는군요.
variables가 비어있는건 변수를 입력하지 않았기 때문임을 고급스러운 사용자분들은 다 아실테니 구지 설명하지 않겠습니다.]

이로써 heroes of storm - eso의 설명을 마칩니다. 읽어주셔서 감사합니다.
