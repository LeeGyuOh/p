music = 0

while True:
   order = input("당신의 지금 기분은 어떠신가요? 예) 기쁘다, 슬프다, 화난다, 우울하다, 설렌다 >>>>>")
   if order == '기쁘다':
       order = input("얼마나 기쁘신가요? 예) 매우, 보통, 조금 >>>>>")
       if order == '매우':
           music = 'Schubert -Scherzo N. "Allegretto"'
       elif order == '보통':
           music = 'Chopin Etude op.25 no.9'
       else :
           music = 'mozart piano sonata k.330 1st movement'
       print(f"추천드릴 곡은 {music} 입니다, 계속하려면 Y를 입력하세요, 그만두려면 N을 입력하세요")
       order = input(">>>>")
       if order == 'N':
           break

  

   elif order == '슬프다':
       order = input("얼마나 슬프신가요? 예) 매우, 보통, 조금 >>>>>")
       if order == '매우':
         music = 'Beethoven- Piano Sonata No.14 in C#minor Op.27 No.2'
       elif order == '보통':
         music = 'Handel -Suite No.1 in Bb Major, HWV434: IV. Menuet-Vadim Chaimovich'
       else :
         music = 'Chopin- 24 Preludes Op.28 No.4'
       print(f"추천드릴 곡은 {music} 입니다, 계속하려면 Y를 입력하세요, 그만두려면 N을 입력하세요")
       order = input(">>>>")
       if order == 'N':
           break

  

   elif order == '화난다':
       order = input("얼마나 화가 나셨나요? 예) 매우, 보통, 조금 >>>>>")
       if order == '매우':
           music = 'rachmaninoff moment musicaux no.4'
       elif order == '보통':
           music = 'Beethoven- Sonata No.14 "Moonlight" Sonata 3rd Movement'
       else :
           music = 'List- Mephisto Waltz'
       print(f"추천드릴 곡은 {music} 입니다, 계속하려면 Y를 입력하세요, 그만두려면 N을 입력하세요")
       order = input(">>>>")
       if order == 'N':
           break

    
   elif order == '우울하다':
       order = input("얼마나 우울하신가요? 예) 매우, 보통, 조금 >>>>>")
       if order == '매우':
           music = 'Vitali Chaconne in G Minor'
       elif order == '보통':
           music = 'Chopin-Nocturne in e minor , Op. 72 No.1 '
       else :
           music = 'Liszt-"Consolation" No.3 in Db Major'
       print(f"추천드릴 곡은 {music} 입니다, 계속하려면 Y를 입력하세요, 그만두려면 N을 입력하세요")
       order = input(">>>>")
       if order == 'N':
           break


   else :
       order = input("얼마나 설레신가요? 예) 매우, 보통, 조금 >>>>>")
       if order == '매우':
          music = 'Respighi: 6 Pieces for Piano Valse Caressante. Lilting and quintessentially salon-esque.'
       elif order == '보통':
          music = 'List/Schumann-  Liebeslied "Widmung" S.566'
       else :
          music = 'Bach /Gonoud- Ave Maria Faure Romance Sans Parole No. 3 Op.17'
       print(f"추천드릴 곡은 {music} 입니다, 계속하려면 Y를 입력하세요, 그만두려면 N을 입력하세요")
       order = input(">>>>")
       if order == 'N':
           break


   

