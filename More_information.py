import streamlit as st
from PIL import Image
import time


def more_information():
    st.title('Quiz Answer')
    st.text("***********************************************************************************")
    st.text_area("","""Q1. If you hold your pet in your arms when you go for a walk with your pet, you don't need a leash.
    (반려동물과 산책할 때 반려동물을 품에 안고 있다면, 목줄이 없어도 된다.)""")
    st.subheader("X")
    st.write("","""Why? 
    
    꼭 목줄을 해야 합니다. 또한, 본인이 기르는 개가 맹견으로 포함된다면 목줄과 입마개를 필시 착용해야 하며 이를 어길 시 안전조치 위반으로 50만 원 이하의 과태료가 부과됩니다.
                (You must have a leash. In addition, if your dog is included as a fierce dog, a leash and a muzzle must be worn. Failure to do so will result in a fine of not more than 500,000 won as a violation of safety measures.)
            """)
    
    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q2. Subsidies are available for those who adopt an animal that is being cared for by an animal protection center directly operated by a local government or entrusted with a designated animal protection center.
    (지방자치단체에서 직접 운영하거나 위탁 지정한 동물보호센터에서 보호 중인 동물을 입양한 경우에 지원금을 받을 수 있다.)""")
    st.subheader("O")
    st.write("","""Why?
    
    해당되는 경우, 입양확인서를 받아 동물등록을 완료하고 입양비청구서를 작성, 
    6개월 내에 신청하면 입양비가 지급됩니다.(If applicable, receive an adoption confirmation letter, complete animal registration, fill out an adoption fee claim,
    If you apply within 6 months, the adoption fee will be paid.)
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q3. If you do not register your dog with the city/gu office, you will be fined up to 600,000 won.
    (본인이 기르는 반려견을 시·구청에 등록하지 않았다면 60만 원 이하의 과태료가 부과된다.)""")
    st.subheader("O")
    st.write("","""<반려견 등록하는 두 가지 방법>

    내장칩 – 동물병원 방문(대부분의 동물병원이 동물등록대행업체로 지정되어 있음)

    외장칩·인식표 – 시·구청에 방문해, 관련 부서에 미리 확인을 받고 등록

    <Two ways to register your dog>

    Built-in chip – Visits to veterinary hospitals (most veterinary hospitals are designated as animal registrars)
    
    External Chip/Identification Tag – Visit the city/gu office, get confirmation in advance from the relevant department and register
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q4. Fierce Dogs have the right as companion animals, so they can enter wherever other companion animals are allowed. 
    (맹견도 반려동물로써의 권리가 있으므로, 다른 반려동물들이 출입 가능한 모든 곳에 맹견 또한 출입이 가능하다.)""")
    st.subheader("X")
    st.write("","""Why? 

    맹견의 소유자등은 맹견의 공격으로부터 취약한 노약자나 어린이 등이 이용하는 장소에는 맹견을 출입하지 않도록 해야 한다. 현행 동물보호법에서는 출입금지장소를 어린이집, 유치원, 초등학교 및 특수학교, 그 밖에 시·도의 조례로 정하는 장소로 규정하고 있다. 이 사항을 준수하지 않은 소유주에게는 1차 100만원, 2차 200만원, 3차 300만원의 과태료가 부과될 수 있다.
    
    (Owners of the fierce dogs, etc., should not allow them to enter places used by the elderly or children who are vulnerable to attack by dogs. The current Animal Protection Act stipulates that places where entry is prohibited include daycare centers, kindergartens, elementary schools and special schools, and other places determined by city/provincial ordinances. Owners who do not comply with this rule may be fined 1 million won for the first, 2 million won for the second, and 3 million won for the third.)
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q5. In the case of a fierce dog causing physical harm to humans, it is possible to quarantine the dog with the consent of the owner.
    (맹견이 사람에게 신체적 피해를 주는 경우, 소유자의 동의를 얻으면, 맹견에 대한 격리조치가 가능하다.)""")
    st.subheader("X")
    st.write("","""Why?

    맹견이 사람에게 신체적 피해를 주는 경우 소유자 동의 없이도 맹견에 대한 격리조치가 가능하다.
    (If the fierce dog causes physical harm to people, it is possible to quarantine the dog without the owner's consent.)
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q6. If a person dies as a result of violating the use of a leash for a dog or violating a leash or muzzle for a dog, imprisonment for not more than 3 years or a fine of not more than 30 million won will be imposed. fine is imposed
    (반려견의 목줄 착용 위반 및 맹견의 목줄·입마개 착용 위반으로 인한 사고로 사람이 사망할 경우, 3년 이하의 징역 또는 3000만원 이하의 벌금이 부과되며 부상 시에는 2년 이하의 징역 또는 2000만원 이하의 벌금이 부과된다.)""")
    st.subheader("O")
    st.write("","""
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q7. If you are adopting a new pet, it is preferable to have an “older” cat or dog rather than a kitten or puppy.
    (만약 애완동물을 새로 입양하려 한다면, 새끼 고양이나 새끼 강아지를 들이는 것보다 “좀 나이가 든” 고양이나 개를 들이는 것이 바람직하다.) """)
    st.subheader("O")
    st.write("","""Why?
    다 자란 애완동물일수록 병에 잘안걸리고, 병을 옮기는 일도 드물기때문이다.
    (adult pets are less susceptible to diseases and rarely transmit diseases.)
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q8. 다음 빈칸에 들어갈 단어로 알맞은 것은?
    [                  ]는동물보호·복지 대국민 온라인 교육 플랫폼이다. 농식품부는 2018년부터 ‘동물보호복지 온라인’ 누리집을 통해 반려동물 관련업 종사자와 맹견소유자 등에게 의무교육을 제공해 왔다. 최근 반려동물을 양육하는 가구가 증가되는 상황을 고려, 의무교육프로그램 외에도 동물병원, 동물약국 등 다양한 정보를 포함하는 플랫폼으로 누리집을 전면 개편했다. [                  ]에는 수의사와 훈련사가 참여하는 반려견 입양 전 교육과 초등학생에게 생명 존중의 의미를 가르치는 인성교육 프로그램이 신설됐다. 아울러 동물병원, 동물약국, 미용업소, 위탁관리업소, 동물보호센터의 위치정보를 제공해 내 주변에서 이용 가능한 시설을 검색할 수 있는 편의 기능도 제공하고 있다.
    """)
    st.subheader("동물사랑배움터")
    st.write("","""
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q9. 강아지의 중성화수술 권장 시기는 언제일까?
    """)
    st.subheader("생후 5개월 ~ 9개월")
    st.write("","""Why?

    중성화수술은 소변마킹등의 성적 행동이 보이기 직전인 생후 5-9개월 무렵에 하도록 권장하고 있습니다
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q10. 다음 중 강아지가 먹으면 안되는 음식으로 옳지 않은 것은?
    """)
    st.subheader("계란")
    st.write("","""Why?

    계란 속에는 강아지에게도 아주 좋은 단백질원이 풍부해 반려견의 시력, 모질 개선, 노화 방지, 면역력 강화 등 다양한 효과를 볼 수 있습니다. 프라이나 계란보다는 삶은 계란을 주는 것이 좋습니다.

    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q11. 다음 중 강아지 입양에 대한 설명으로 옳지 않은 것은?
    """)
    q11 = st.write("","""
    1) 강아지를 입양할 때는 외모가 내가 원하는 반려동물의 모습인지를 판단하는 것이 제일 중요하다.
    2) 일반적으로 어미나 형제와 함께 충분한 시간을 보낸 후 생후 8-12주령에 입양하는게 가장 좋다.
    3) 공공장소, 공원 등에서 구조되거나 유기된 애완동물은 유기동물보호소(동물보호센터)에 보호되는데 일정기간이 지나도 소유자가 나타나지 않으면 일반인이 분양받을수 있다.
    4) 펫샵이나 동물판매업자에게 구입할경우 먼저 그 판매업소가 등록이 되어있는지 확인해야 한다.
    5) 펫샵에서 구입할 경우 1차 이상 예방접종을 한 강아지인지, 건강한 상태인지 주의깊게 확인하는 것이 좋다.""")
    # 1
    st.subheader("강아지를 입양할 때는 외모가 내가 원하는 반려동물의 모습인지를 판단하는 것이 제일 중요하다.")
    st.write("","""Why?

    외모 보다는 가족과 본인의 생활스타일에 맞는 품종별 특징이나 성격, 암컷인지 수컷인지 등을 충분히 알아본 후 에 입양하는 것이 좋습니다.
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q12. 다음 중 강아지 목욕/샤워에 대한 설명으로 옳지 않은 것은?
    """)
    q12 = st.write("","""
    1) 강아지는 일주일에 한 번 이상 꼭 씻어야 한다.
    2) 가능하다면 좁은 공간에서 목욕시킨다.
    3) 목욕 전 털을 빗겨 엉키고 엉겨 붙은 털을 정리해준다.
    4) 손톱 정리가 필요하다면 목욕 전에 다듬는 것이 좋다.
    5) 강아지의 귀가 젖으면 중이염의 위험이 높아지게 된다.솜을 귀에 넣어 목욕 시 외이도에 물이 들어가지 않도록 한다.""")
    # 1
    st.subheader("강아지는 일주일에 한 번 이상 꼭 씻어야 한다.")
    st.write("","""Why?
    
    야외 활동이 잦은 강아지는 그만큼 목욕을 자주 하는 것이 좋으나 반대로 실내에서만 생활하는 강아지는 몇 달에 한번이면 충분하다
    """)

    st.text('-----------------------------------------------------------------------------------------------------')
    st.text_area("","""Q13. 빈칸에 들어갈 말로 알맞은 것은? 
    개는 육식동물로서 몸의 근육을 유지하는데 필수적으로 [           ]이 필요하다. 강한 뼈와 건강한 치아를 위해서는 칼슘과 인, 충분한 비타민의 주의 깊은 균형이 필요하며, 지방과 오일은 활성 및 대형견을 위한 중요한 에너지원이 된다.
    고양이도 육식동물로서  [           ]이 필요한데, 개보다도 2배 이상 필요하다. 비타민A는 필요하지만 지나치면 해로울 수 있고, 비타민 같은 물질인 타우린은 눈과 심장질환예방에 좋다.
    """)
    st.subheader("단백질")
    st.write("","""
    """)
