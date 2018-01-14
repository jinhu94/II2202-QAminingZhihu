# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""
import csv
from zhihu_oauth import ZhihuClient

client = ZhihuClient()

client.load_token('token.pkl')

a1 = client.answer(126638629)
print (a1.content)
<p>10/13日的演讲，下面这段感动了很多人。大致翻译一下：我加入竞选前，有人警告我，说参加总统竞选会把我打入地狱。我商业经营很成功，旗下多家公司，家庭也很幸福。我本来可以不来趟这场浑水，每天坐在家里舒舒服服享受生活。但这个国家现在千疮百孔，我个人的成功既然得益于国家强盛，现在就必须回馈她。我本来也是掌控这个国家的少数上层人士之一，但我现在跟他们决裂了。我从那个小团体出来，深知这个国家肮脏到了什么程度。也正因为我从那里出来，我也是治理这个国家的最佳人选。</p><p>This is our moment of reckoning as a society and as a civilization 
itself.   I didn't need to do this, folks, believe me — believe me.   I 
built a great company and I had a wonderful life.   I could have enjoyed 
the fruits and benefits of years of successful business deals and 
businesses for myself and my family.   Instead of going through this 
absolute horror show of lies, deceptions, malicious attacks — who would 
have thought?   I'm doing it because this country has given me so much, 
and I feel so strongly that it's my turn to give back to the country 
that I love.</p><p>Many of my friends and many political experts warned me that this 
campaign would be a journey to hell – said that.   But they're wrong.   It 
will be a journey to heaven, because we will help so many people that 
are so desperately in need of help. </p><p>In my former life, I was an insider as much as anybody else.   And I knew
 what it's like, and I still know what it's like to be an insider.   It's 
not bad.   It's not bad.   Now I'm being punished for leaving the special 
club and revealing to you the terrible things that are going on having 
to do with our country.   Because I used to be part of the club, I'm the 
only one that can fix it.</p><p>前不久看到有人对此次竞选发出了"凤凰男女真不适合当政治一把手"的感叹，虽然不能一棍子都打死，但统计上还是有点道理的。以人性而言，拥有过再选择放下会相对容易，佛祖正因为生为王子方能舍去一切去参悟救世。Trump的出身和本人的能力、经历决定了他的视野。有心人汇总了他年轻时（四十岁前后）的电视采访内容，对美国的种种担心和今天在演讲中说的高度一致（油管，watch?v=mxf1XmVZ9qY）。他表面上是个肤浅粗俗的花花公子，实际上是个能够严肃思考、缜密分析的聪明人。身为商人却有诸多义举，较那些满口仁义道德的虚伪政客要高尚得多。</p><p>Trump本可以继续留在超级富豪俱乐部里，对本国中产插管吸血，享受全球化带来的好处，却在古稀之年站出来揭穿皇帝新衣的谎言，开启人生最后一场大战。没有大金主支持，几乎所有媒体都敌对，更糟的是象党内不少“自己人”也半心半意，甚至在离投票日不到一个月的关键时刻还在他背后捅刀子。唐吉珂德单枪匹马大战风车巨人，莫过如是。这样的背景下，10/13日的这段讲话平添了几分悲壮。</p><p>面对重重大山般的困难，Trump采取了最笨的办法，就是一个城市一个城市去跑，用最平实的语言去宣讲自己的理念。一场又一场造势集会上，人们看到一颗拳拳的爱国之心，一腔不畏强敌的过人勇气，一个能够厘清庞杂的明晰大脑。越来越多的选民被唤醒，民心渐渐向他聚拢，他们要与Trump一起完成那看似不可能的任务。美利坚正站在继续下滑和重新振奋的十字路口，有这样一个牛人横空出世，真是受上天眷顾的国家。</p>
