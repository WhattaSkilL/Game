#Задача 10.1 Вариант 3.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.
#Серх задания была написанна игра осно
# Gilfanov A. I.
# 29.09.2016

import random

#Другие переменные
path=1;locat1="неизвестную сторону";kolarm=31;kolweap=24;name="?";expup=500;exp=0;magicdmg=0;vozvrat=0

#Враг
    #Состояние врага
EnemyStatus=[0,0,0,0,0,0,0,0,0,0]
EFire=0;EBleed=0;EPois=0
EFear=0;EToss=0;EStun=0;ESile=0;EDisarm=0;EArmless=0;EBlind=0
    #Время негативных эффектов на враге
EnemyTimeStatus=[0,0,0,0,0,0,0,0,0,0]
EFireT=0;EBleedT=0;EPoisT=0
EFearT=0;ETossT=0;EStunT=0;ESileT=0;EDisarmT=0;EArmlessT=0;EBlindT=0
    #Сопротивления врага
EnemyResistance=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0

#Персонаж
    #Состояние персонажа
Status=[0,0,0,0,0,0,0,0,0,0]
Fire=0;Bleed=0;Pois=0
Fear=0;Toss=0;Stun=0;Sile=0;Disarm=0;Armless=0;Blind=0
    #Время негативных эффектов
TimeStatus=[0,0,0,0,0,0,0,0,0,0]
FireT=0;BleedT=0;PoisT=0
FearT=0;TossT=0;StunT=0;SileT=0;DisarmT=0;ArmlessT=0;BlindT=0
    #Сопротивления
Resistance=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
FireRes=0;WaterRes=0;EarthRes=0;AirRes=0;PhisRes=0;BleedRes=0;PoisRes=0
FearRes=0;TossRes=0;StunRes=0;SileRes=0;DisarmRes=0;ArmlessRes=0;BlindRes=0
    #Характеристики
P=30;SP=3;SAP=1;S=0;M=0;A=0;H=0;E=0;lvl=1;exp=0;safy=1;atk=0;classname="Свой"
AS=[0,0,0,0,0,0];AA=[0,0,0,0,0,0];AH=[0,0,0,0,0,0];AM=[0,0,0,0,0,0]
    #Способности пассивные
S0=[];SID=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #Способности активные
SA0=[];SAID=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Предметы и их ИД
legendaryweapon=["Меч Демигодов", "Последний герой", "Клинок древних богов", "Тёмное время", "Топор лесоруба", "Головоруб", "Призвание палача",\
 "Гильотина", "Западная звезда", "Костедробитель", "Молот Погнороса", "Крушитель миров", "Скипетр пустоты", "Скипетр истинной магии", "ТаоБо",\
 "Смертельный костыль", "Лук снайпера", "Армагедон", "Пожиратель заклятий", "Круглый", "Щит Дорана", "Знамение Рандуина", "Стена боли", "Малыш"]
legendaryweaponID=["115","116","125","126","135","136","145","146","155","156","165"\
 ,"166","175","176","185","186","195","196","215","216","225","226","235","236"]
weaponlist=["Деревянный меч", "Ржавый меч", "Стальной меч", "Обсидиановый клинок", "Двуручный деревянный меч", "Двуручный ржавый меч"\
 ,"Двуручный стальной меч", "Двуручный обсидиановый клинок", "Деревянный топор", "Ржавый топор", "Стальной топор", "Обсидиановый топор"\
 ,"Двуручный деревянный топор", "Двуручный ржавый топор", "Двуручный стальной топор", "Двуручный обсидиановый топор", "Деревянная палица"\
 ,"Ржавая булава", "Стальная булава", "Обсидиановая булава", "Двуручная деревянная палица", "Двуручный ржавый молот", "Двуручный стальной молот",\
 "Великая обсидиановая булава", "Стальной скипетр", "Скипетр с сапфиром", "Скипетр с алмазом", "Скипетр с камнем душ", "Деревянный посох",\
 "Укреплённый деревянный посох", "Стальной шест", "Посох из драконьей стали", "Деревянный лук", "Боевой лук", "Составной лук", "Тяжёлый лук",\
 "Деревянный баклер", "Стальной баклер", "Серебряный баклер", "Алмазный баклер", "Деревянный щит", "Стальной щит", "Серебряный щит",\
 "Алмазный щит", "Деревянный башенный щит", "Стальной башенный щит", "Серебряный башенный щит", "Алмазный башенный щит","Нож","Кинжал","Боевой нож",\
 "Клинок убийцы","Потрошитель","Последнее воспоминание"]
weaponlistID=["111","112","113","114","121","122","123","124","131","132","133","134",\
 "141","142","143","144","151","152","153","154","161","162","163","164",\
 "171","172","173","174","181","182","183","184","191","192","193","194",\
 "211","212","213","214","221","222","223","224","231","232","233","234",\
 "101","102","103","104","105","106"]
legendaryarmor=["Корона короля стихий", "Диадема власти", "Капюшон убийцы", "Маска ночи", "Шлем авантюриста", "Шляпа мушкетёра", "Шлем командора",\
 "Шлем обезумевшего рыцаря", "Роба короля стихий", "Роба магистра", "Накидка убийцы", "Митриловая броня", "Нагрудник авантюриста", "Дичка",\
 "Доспех командора", "Доспех обезумевшего рыцаря", "Руковицы короля стихий", "Перчатки колдовства", "Перчатки убийцы", "Перчатки похитителя жизни"\
 , "Перчатки авантюриста", "Перчатки смелого", "Перчатки командора", "Перчатки обезумевшего рыцаря", "Ботинки короля\
 стихий", "Сапоги убийцы", "Сапоги проворности", "Ботинки авантюриста", "Волшебные сапоги", "Сапоги командора", "Сапоги обезумевшего рыцаря"]
legendaryarmorID=["314","315","325","326","335","336","345","346","415","416","425","426","435",\
 "436","445","446","515","516","525","526","535","536","545","546","615","624","625","635","636","645","646"]
armorlist=["Простая шляпа","Венец","Шляпа с широкими полями"," Кожаный шлем","Шлем из дублёной кожи","Шлем из паутины","Шлем из ткани безны",\
 "Железный шлем","Стальной шлем","Кольчужный капюшон","Шлем скорпиона","Тяжёлый стальной шлем","Тяжёлый шлем из пластин","Тяжёлый ониксовый шлем",\
 "Тяжёлый титановый шлем","Простая рубаха","Роба","Плащ","Роба мага","Кожаная броня","Броня из дублёной кожи","Броня из паутины","Броня из ткани безны",\
 "Железный нагрудник","Стальной нагрудник","Кольчужная рубаха","Кираса скорпиона","Тяжёлый стальной доспех","Тяжёлый пластинчатый доспех",\
 "Тяжёлый ониксовый доспех","Тяжёлый титановый доспех","Простые перчатки","Кожаные перчатки","Винтажные перчатки","Перчатки мага","Кожаные перчатки",\
 "Перчатки из дублёной кожи","Перчатки из паутины","Перчатки из ткани бездны","Железные перчатки","Стальные перчатки","Кольчужные перчатки","Перчатки скорпиона"\
 ,"Тяжёлые стальные перчатки","Тяжёлые пластинчатые перчатки","Тяжёлые ониксовые перчатки","Тяжёлые титановые перчатки","Простые ботинки","Сапоги",\
 "Крепкие сапоги","Зачарованные сандали","Кожаные сапоги","Сапоги из дублёной кожи","Сапоги из паутины","Сапоги из ткани бездны","Железные ботинки",\
 "Стальные ботинки","Ботинки укреплённые кольчугой","Ботинки скориона","Тяжёлые стальные ботинки","Тяжёлые пластинчатые ботинки","Тяжёлые ониксовые ботинки","Тяжёлые титановые ботинки"]
armorlistID=["311","312","313","321","322","323","324","331","332","333","334","341","342","343"\
 ,"344","411","412","413","414","421","422","423","424","431","432","433","434","441","442",\
 "443","444","511","512","513","514","521","522","523","524","531","532","533","534","541","542",\
 "543","544","611","612","613","614","621","622"," 623","624","631","632","633","634","641","642","643","644"]

def active(AbNom): #Активные способности
    global MP, FireDMG, WaterDMG, AirDMG, EarthDMG, DarkDMG, PhisDMG, TrueDMG, EFire, EFireT, SA16dop, vozvrat
    vozvrat=0
    z=SA0[AbNom-1]
    if z=="Шар стихии" or z=="Шар стихии lvl 2" or z=="Шар стихии lvl 3": #Огонь, вода, воздух, земля
        if z=="Шар стихии":
            FireDMG=10*SID[14];WaterDMG=10*SID[17];EarthDMG=10*SID[15];AirDMG=10*SID[16];vozvrat=0
        elif z=="Шар стихии lvl 2":
            FireDMG=15*SID[14];WaterDMG=15*SID[17];EarthDMG=15*SID[15];AirDMG=15*SID[16];vozvrat=0
        elif z=="Шар стихии lvl 3":
            FireDMG=20*SID[14];WaterDMG=20*SID[17];EarthDMG=20*SID[15];AirDMG=20*SID[16];vozvrat=0
    elif z=="Искра" or z=="Искра lvl 2" or z=="Искра lvl 3": #Огонь, понижение брони
        if z=="Искра":
            FireDMG=20*SID[14];EArmless=10;EArmlessT=1;vozvrat=0
        elif z=="Искра lvl 2":
            FireDMG=30*SID[14];EArmless=15;EArmlessT=1;vozvrat=0
        elif z=="Искра lvl 3":
            FireDMG=40*SID[14];EArmless=20;EArmlessT=1;vozvrat=0
    elif z=="Поток пламени" or z=="Поток пламени lvl 2" or z=="Поток пламени lvl 3": #Огонь, поджог, понижение брони
        if z=="Поток пламени":
            FireDMG=15*SID[14];EArmless=15;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=10;EFireT=1
        elif z=="Поток пламени lvl 2":
            FireDMG=20*SID[14];EArmless=20;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=15;EFireT=2
        elif z=="Поток пламени lvl 3":
            FireDMG=25*SID[14];EArmless=25;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=20;EFireT=2
    elif z=="Дыхание дракона" or z=="Дыхание дракона lvl 2" or z=="Дыхание дракона lvl 3": #Огонь, поджог, ужас, понижение брони
        if z=="Дыхание дракона":
            FireDMG=15*SID[14];EArmless=15;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=10;EFireT=1
            if random.randint(0,100)>70:
                EFear=10;EFearT=1
        elif z=="Дыхание дракона lvl 2":
            FireDMG=20*SID[14];EArmless=15;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=15;EFireT=1
            if random.randint(0,100)>70:
                EFear=15;EFearT=1
        elif z=="Дыхание дракона lvl 3":
            FireDMG=20*SID[14];EArmless=15;EArmlessT=2;vozvrat=0
            if random.randint(0,100)>50:
                EFire=20;EFireT=2
            if random.randint(0,100)>70:
                EFear=20;EFearT=2
    elif z=="Порез ветром" or z=="Порез ветром lvl 2" or z=="Порез ветром lvl 3": #Воздух, кровотечение
        if z=="Порез ветром":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
        elif z=="Порез ветром lvl 2":
            AirDMG=SID[16]*15;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=15;EBleedT=2
        elif z=="Порез ветром lvl 3":
            AirDMG=SID[16]*20;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=20;EBleedT=2
    elif z=="Сносящий поток" or z=="Сносящий поток lvl 2" or z=="Сносящий поток lvl 3": #Воздух, обезоруживание
        if z=="Сносящий поток":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EDisarm=10;EDisarmT=1
        elif z=="Сносящий поток lvl 2":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EDisarm=10;EDisarmT=1
        elif z=="Сносящий поток lvl 3":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EDisarm=10;EDisarmT=1
    elif z=="Смерч" or z=="Смерч lvl 2" or z=="Смерч lvl 3": #Воздух, кровотечение, оглушение или обезоруживание
        if z=="Смерч":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Смерч lvl 2":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Смерч lvl 3":
            AirDMG=SID[16]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
    elif z=="Бросок камня" or z=="Бросок камня lvl 2" or z=="Бросок камня lvl 3": #Земля, оглушение
        if z=="Бросок камня":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
        elif z=="Бросок камня lvl 2":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
        elif z=="Бросок камня lvl 3":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
    elif z=="Столб земли" or z=="Столб земли lvl 2" or z=="Столб земли lvl 3": #Земля, оглушение или обезоруживание
        if z=="Столб земли":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Столб земли lvl 2":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Столб земли lvl 3":
            EarthDMG=SID[15]*10;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
    elif z=="Землетрясение" or z=="Землетрясение lvl 2" or z=="Землетрясение lvl 3": #Земля за ход, оглушение за ход или обезоруживание
        if z=="Землетрясение":
            EarthDMG=SID[15]*10; Quake=3;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Землетрясение lvl 2":
            EarthDMG=SID[15]*10; Quake=3;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
        elif z=="Землетрясение lvl 3":
            EarthDMG=SID[15]*10; Quake=3;vozvrat=0
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EDisarm=10;EDisarmT=1
                else:
                    EStun=10;EStunT=1
    elif z=="Всплеск" or z=="Всплеск lvl 2" or z=="Всплеск lvl 3": #Вода, -поджог, ослепление
        if z=="Всплеск":
            WaterDMG=SID[17]*10; EFire=0; EFireT=0;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
        elif z=="Всплеск lvl 2":
            WaterDMG=SID[17]*10; EFire=0; EFireT=0;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
        elif z=="Всплеск lvl 3":
            WaterDMG=SID[17]*10; EFire=0; EFireT=0;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
    elif z=="Гейзер" or z=="Гейзер lvl 2" or z=="Гейзер lvl 3": #Вода, подброс или обезоруживание
        if z=="Гейзер":
            WaterDMG=SID[17]*10;vozvrat=0
            if random.randint(0,1)>0:
                EDisarm=10;EDisarmT=1
            else:
                EToss=10;ETossT=1
        elif z=="Гейзер lvl 2":
            WaterDMG=SID[17]*10;vozvrat=0
            if random.randint(0,1)>0:
                EDisarm=10;EDisarmT=1
            else:
                EToss=10;ETossT=1
        elif z=="Гейзер lvl 3":
            WaterDMG=SID[17]*10;vozvrat=0
            if random.randint(0,1)>0:
                EDisarm=10;EDisarmT=1
            else:
                EToss=10;ETossT=1
    elif z=="Смертельный дождь" or z=="Смертельный дождь lvl 2" or z=="Смертельный дождь lvl 3": #Вода за ход, кровотечение, понижение брони
        if z=="Смертельный дождь":
            WaterDMG=SID[17]*10; DeathRain=3;vozvrat=0
            if random.randint(0,100)>50:
                EArmless=10;EArmlessT=1
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
        elif z=="Смертельный дождь lvl 2":
            WaterDMG=SID[17]*10; DeathRain=3;vozvrat=0
            if random.randint(0,100)>50:
                EArmless=10;EArmlessT=1
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
        elif z=="Смертельный дождь lvl 3":
            WaterDMG=SID[17]*10; DeathRain=3;vozvrat=0
            if random.randint(0,100)>50:
                EArmless=10;EArmlessT=1
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
    elif z=="Сгусток тени" or z=="Сгусток тени lvl 2" or z=="Сгусток тени lvl 3": #Тьма, ослепление
        if z=="Сгусток тени":
            DarkDMG=SID[18]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
        elif z=="Сгусток тени lvl 2":
            DarkDMG=SID[18]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
        elif z=="Сгусток тени lvl 3":
            DarkDMG=SID[18]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBlind=10;EBlindT=1
    elif z=="Похищение здоровья" or z=="Похищение здоровья lvl 2" or z=="Похищение здоровья lvl 3": #Тьма, вампиризм
        if z=="Похищение здоровья":
            DarkDMG=SID[18]*10;vozvrat=0
            if HP==FHP or DarkDMG+HP>FHP:
                HP=FHP
            else:
                HP+=DarkDMG
        elif z=="Похищение здоровья lvl 2":
            DarkDMG=SID[18]*10;vozvrat=0
            if HP==FHP or DarkDMG+HP>FHP:
                HP=FHP
            else:
                HP+=DarkDMG
        elif z=="Похищение здоровья lvl 3":
            DarkDMG=SID[18]*10;vozvrat=0
            if HP==FHP or DarkDMG+HP>FHP:
                HP=FHP
            else:
                HP+=DarkDMG
    elif z=="Прикосновение смерти" or z=="Прикосновение смерти lvl 2" or z=="Прикосновение смерти lvl 3": #Тьма, увеличение урона
        if z=="Прикосновение смерти":
            DarkDMG=SID[18]*10+SA16dop; VragProverka=1;vozvrat=0
        elif z=="Прикосновение смерти lvl 2":
            DarkDMG=SID[18]*10+SA16dop; VragProverka=1;vozvrat=0
        elif z=="Прикосновение смерти lvl 3":
            DarkDMG=SID[18]*10+SA16dop; VragProverka=1;vozvrat=0
    elif z=="Тычёк щитом" or z=="Тычёк щитом lvl 2" or z=="Тычёк щитом lvl 3":    #Физический, оглушить или молчание
        if z=="Тычёк щитом":
            PhisDMG=SID[8]*10
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EStun=10;EStunT=1
                else:
                    ESile=10;ESileT=1
        elif z=="Тычёк щитом lvl 2":
            PhisDMG=SID[8]*10
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EStun=10;EStunT=1
                else:
                    ESile=10;ESileT=1
        elif z=="Тычёк щитом lvl 3":
            PhisDMG=SID[8]*10
            if random.randint(0,100)>50:
                if random.randint(0,1)>0:
                    EStun=10;EStunT=1
                else:
                    ESile=10;ESileT=1
    elif z=="Бросок щита" or z=="Бросок щита lvl 2" or z=="Бросок щита lvl 3": #Физический, обезоруживание
        if Equipment[1]=="Баклер":
            if z=="Бросок щита":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EDisarm=10;EDisarmT=1
            elif z=="Бросок щита lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EDisarm=10;EDisarmT=1
            elif z=="Бросок щита lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EDisarm=10;EDisarmT=1
        else:
            vozvrat=1
    elif z=="Удар щитом" or z=="Удар щитом lvl 2" or z=="Удар щитом lvl 3": #Физический, оглушить или молчание или обезоруживание
        if Equipment[1]=="Щит":
            if z=="Удар щитом":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    z=random.randint(0,2)
                    if z==0:
                        EDisarm=10;EDisarmT=1
                    elif z==1:
                        ESile=10;ESileT=1
                    elif z==2:
                        EStun=10;EStunT=1
            elif z=="Удар щитом lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    z=random.randint(0,2)
                    if z==0:
                        EDisarm=10;EDisarmT=1
                    elif z==1:
                        ESile=10;ESileT=1
                    elif z==2:
                        EStun=10;EStunT=1
            elif z=="Удар щитом lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    z=random.randint(0,2)
                    if z==0:
                        EDisarm=10;EDisarmT=1
                    elif z==1:
                        ESile=10;ESileT=1
                    elif z==2:
                        EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Оглушение" or z=="Оглушение lvl 2" or z=="Оглушение lvl 3": #Физический, оглушить
        if Equipment[1]=="Щит" or Equipment[1]=="Башенный щит":
            if z=="Оглушение":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Оглушение lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Оглушение lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Таран" or z=="Таран lvl 2" or z=="Таран lvl 3": #Физический, оглушить
        if Equipment[1]=="Башенный щит":
            if z=="Таран":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Таран lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Таран lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Рассекающий порез" or z=="Рассекающий порез lvl 2" or z=="Рассекающий порез lvl 3": #Физический, кровотечение
        if Equipment[0]=="Одноручный меч" or Equipment[0]=="Двуручный меч" or Equipment[0]=="Кинжал":
            if z=="Рассекающий порез":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Рассекающий порез lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Рассекающий порез lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
        else:
            vozvrat=1
    elif z=="Разрубающий удар" or z=="Разрубающий удар lvl 2" or z=="Разрубающий удар lvl 3": #Физический, кровотечение
        if Equipment[0]=="Одноручный меч" or Equipment[0]=="Двуручный меч":
            if z=="Разрубающий удар":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Разрубающий удар lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Разрубающий удар lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
        else:
            vozvrat=1
    elif z=="Заряженный взмах" or z=="Заряженный взмах lvl 2" or z=="Заряженный взмах lvl 3": #Физический, огонь, вода, воздух, земля
        if Equipment[0]=="Одноручный меч" or Equipment[0]=="Двуручный меч":
            if z=="Заряженный взмах":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
            elif z=="Заряженный взмах lvl 2":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
            elif z=="Заряженный взмах lvl 3":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
        else:
            vozvrat=1
    elif z=="Рубитькромсать" or z=="Рубитькромсать lvl 2" or z=="Рубитькромсать lvl 3": #Физический, кровотечение
        if Equipment[0]=="Одноручный топор" or Equipment[0]=="Двуручный топор":
            if z=="Рубитькромсать":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Рубитькромсать lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Рубитькромсать lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
        else:
            vozvrat=1
    elif z=="Сильный удар" or z=="Сильный удар lvl 2" or z=="Сильный удар lvl 3": #Физический, оглушение
        if Equipment[0]=="Одноручный топор" or Equipment[0]=="Двуручный топор" or Equipment[0]=="Одноручная булава" or Equipment[0]=="Двуручная булава":
            if z=="Сильный удар":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Сильный удар lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Сильный удар lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Удар с плеча" or z=="Удар с плеча lvl 2" or z=="Удар с плеча lvl 3": #Физический, сильное кровотечение
        if Equipment[0]=="Одноручный топор" or Equipment[0]=="Двуручный топор":
            if z=="Удар с плеча":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Удар с плеча lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
            elif z=="Удар с плеча lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EBleed=10;EBleedT=1
        else:
            vozvrat=1
    elif z=="Удар с размаха" or z=="Удар с размаха lvl 2" or z=="Удар с размаха lvl 3": #Физический, оглушение
        if Equipment[0]=="Одноручная булава" or Equipment[0]=="Двуручная булава":
            if z=="Удар с размаха":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Удар с размаха lvl 2":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Удар с размаха lvl 3":
                PhisDMG=SID[8]*10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Громовой удар" or z=="Громовой удар lvl 2" or z=="Громовой удар lvl 3": #Физический, огонь, вода, воздух, земля, оглушение
        if Equipment[0]=="Одноручная булава" or Equipment[0]=="Двуручная булава":
            if z=="Громовой удар":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Громовой удар lvl 2":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
            elif z=="Громовой удар lvl 3":
                PhisDMG=SID[8]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
                if random.randint(0,100)>50:
                    EStun=10;EStunT=1
        else:
            vozvrat=1
    elif z=="Проникающий удар" or z=="Проникающий удар lvl 2" or z=="Проникающий удар lvl 3": #Удар наносит чистый урон
        if Equipment[0]=="Кинжал":
            if z=="Проникающий удар":
                TrueDMG=SID[28]*10;vozvrat=0
            elif z=="Проникающий удар lvl 2":
                TrueDMG=SID[28]*10;vozvrat=0
            elif z=="Проникающий удар lvl 3":
                TrueDMG=SID[28]*10;vozvrat=0
        else:
            vozvrat=1
    elif z=="Перерезание глотки" or z=="Перерезание глотки lvl 2" or z=="Перерезание глотки lvl 3": #Физический урон игнорируя броню, кровотечение, молчание
        if Equipment[0]=="Кинжал":
            if z=="Перерезание глотки":
                TrueDMG=SID[28]*10;vozvrat=0
                if random.randint(0,100)>50:
                        ESile=10;ESileT=1
                if random.randint(0,100)>50:
                        EBleed=10;EBleedT=1
            elif z=="Перерезание глотки lvl 2":
                TrueDMG=SID[28]*10;vozvrat=0
                if random.randint(0,100)>50:
                        ESile=10;ESileT=1
                if random.randint(0,100)>50:
                        EBleed=10;EBleedT=1
            elif z=="Перерезание глотки lvl 3":
                TrueDMG=SID[28]*10;vozvrat=0
                if random.randint(0,100)>50:
                        ESile=10;ESileT=1
                if random.randint(0,100)>50:
                        EBleed=10;EBleedT=1
        else:
            vozvrat=1
    elif z=="Меткий выстрел" or z=="Меткий выстрел lvl 2" or z=="Меткий выстрел lvl 3": #Физический урон игнорируя броню, ослепление
        if Equipment[0]=="Лук":
            if z=="Меткий выстрел":
                TrueDMG=SID[29]*10;vozvrat=0
                if random.randint(0,100)>50:
                        EBlind=10;EBlindT=1
            elif z=="Меткий выстрел lvl 2":
                TrueDMG=SID[29]*10;vozvrat=0
                if random.randint(0,100)>50:
                        EBlind=10;EBlindT=1
            elif z=="Меткий выстрел lvl 3":
                TrueDMG=SID[29]*10;vozvrat=0
                if random.randint(0,100)>50:
                        EBlind=10;EBlindT=1
        else:
            vozvrat=1
    elif z=="Заряженная стрела" or z=="Заряженная стрела lvl 2" or z=="Заряженная стрела lvl 3": #Физический, огонь, вода, воздух, земля
        if Equipment[0]=="Лук":
            if z=="Заряженная стрела":
                PhisDMG=SID[29]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
            elif z=="Заряженная стрела lvl 2":
                PhisDMG=SID[29]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
            elif z=="Заряженная стрела lvl 3":
                PhisDMG=SID[29]*10;FireDMG=10;WaterDMG=10;EarthDMG=10;AirDMG=10;vozvrat=0
        else:
            vozvrat=1
    elif z=="Тройной выстрел" or z=="Тройной выстрел lvl 2" or z=="Тройной выстрел lvl 3": #Физический х3
        if Equipment[0]=="Лук":
            if z=="Тройной выстрел":
                PhisDMG=SID[29]*10*3;vozvrat=0
            elif z=="Тройной выстрел lvl 2":
                PhisDMG=SID[29]*10*3;vozvrat=0
            elif z=="Тройной выстрел lvl 3":
                PhisDMG=SID[29]*10*3;vozvrat=0
        else:
            vozvrat=1
    elif z=="Прикосновение духа" or z=="Прикосновение духа lvl 2" or z=="Прикосновение духа lvl 3": #Чистый урон
        if z=="Прикосновение духа":
            TrueDMG=SID[29]*10;vozvrat=0
        elif z=="Прикосновение духа lvl 2":
            TrueDMG=SID[29]*10;vozvrat=0
        elif z=="Прикосновение духа lvl 3":
            TrueDMG=SID[29]*10;vozvrat=0
    elif z=="Разрез духа" or z=="Разрез духа lvl 2" or z=="Разрез духа lvl 3": #Чистый урон, кровотечение
        if z=="Разрез духа":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
        elif z=="Разрез духа lvl 2":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
        elif z=="Разрез духа lvl 3":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EBleed=10;EBleedT=1
    elif z=="Удар духа" or z=="Удар духа lvl 2" or z=="Удар духа lvl 3": #Чистый урон, оглушение
        if z=="Удар духа":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
        elif z=="Удар духа lvl 2":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
        elif z=="Удар духа lvl 3":
            TrueDMG=SID[29]*10;vozvrat=0
            if random.randint(0,100)>50:
                EStun=10;EStunT=1
    
def drop(): #Выпадение предметов
        global meshok, meshokID, legendaryarmor, legendaryarmorID, legendaryweapon, legendaryweaponID, kolarm, kolweap
        armwea=random.randint(1,2)
        if random.randint(0,100)<98:
            if armwea==1:
                PhisRes=random.randint(1,63)
                meshok.append(armorlist[PhisRes])
                meshokID.append(armorlistID[PhisRes])
                print("Ваша добыча: ", armorlist[PhisRes])
            elif armwea==2:
                wea=random.randint(1,54)
                meshok.append(weaponlist[wea])
                meshokID.append(weaponlistID[wea])
                print("Ваша добыча: ", weaponlist[wea])
        else:
            if armwea==1:
                PhisRes=random.randint(1,kolarm)
                meshok.append(legendaryarmor[PhisRes])
                meshokID.append(legendaryarmorID[PhisRes])
                print("Поздравляю вы выбили легендарный предмет!", legendaryarmor[PhisRes])
                legendaryarmor.pop(PhisRes)
                legendaryarmorID.pop(PhisRes)
                kolarm-=1
            elif armwea==2:
                wea=random.randint(1,kolweap)
                meshok.append(legendaryweapon[wea])
                meshokID.append(legendaryweaponID[wea])
                print("Поздравляю вы выбили легендарный предмет!", legendaryweapon[wea])
                legendaryweapon.pop(wea)
                legendaryweaponID.pop(wea)
                kolweap-=1

#Битвы                
def fight1(x):         
    global Pois,Stun,Fire,Bleed,Blind,lvl,HP,exp,PhisRes,atk,magicdmg,path,EFire,EBleed,EPois,EFear,EToss,EStun,ESile,EDisarm,EArmless,EBlind,EFireT,EBleedT,EPoisT,EFearT,ETossT,EStunT,ESileT,EDisarmT,EArmlessT,EBlindT
    vihod=1;proverka=0
    if x==1: #Волк
        print("Ваш противник волк") 
        ZV=20*lvl;AV=5*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    elif x==2: #Медведь
        print("Ваш противник медведь")
        ZV=25*lvl;AV=7*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    elif x==3: #Кабан
        print("Ваш противник кабан")
        ZV=20*lvl;AV=10*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    elif x==4: #Змея
        print("Ваш противник змея")
        ZV=20*lvl;AV=5*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    elif x==5: #Орёл
        print("Ваш противник орёл")
        ZV=15*lvl;AV=10*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    elif x==6: #Слизень
        print("Ваш противник слизень")
        ZV=10*lvl;AV=5*lvl
        EFireRes=0;EWaterRes=0;EEarthRes=0;EAirRes=0;EPhisRes=0;EBleedRes=0;EPoisRes=0
        EFearRes=0;ETossRes=0;EStunRes=0;ESileRes=0;EDisarmRes=0;EArmlessRes=0;EBlindRes=0
        EnemyType="Животное"
        i=1
    while True:
        if ZV==0 or HP==0 or ZV<0 or HP<0:
            if ZV==0 or ZV<0:
                print("-----------Вы победили-----------")
                exp+=100
                if random.randint(0,100)>80:
                    drop()
                    print("---------------------------------")
                    break
                else:
                    break
            elif HP==0 or HP<0:
                print("-----------Вы проиграли-----------")
                path=0
                break
        else:
            if i%2==1:
                print("Ваш ход")
                if EFireT>0 or EBleedT>0 or EPoisT>0 or EFearT>0 or ETossT>0 or EStunT>0 or ESileT>0 or EDisarmT>0 or EArmlessT>0 or EBlindT>0:
                    if EFire>0 and EFireT>0: #Проверка на горение врага
                        if EFireRes>EFire:
                            if EFireRes>EFire*2:
                                EFire=0
                                EFireT=0
                            elif EFireRes>EFire:
                                EFire/=2
                    if EBleed>0 and EBleedT>0: #Проверка на кровотечение врага
                        if EnemyType=="Нежить" and EnemyType=="Механизм":
                            EBleed=0; EBleedT=0
                            print("Это существо невосприимчиво к кровотечению")
                        else:
                            if EBleedRes>EBleed:
                                if EBleedRes>EBleed*2:
                                    EBleed=0
                                    EBleedT=0
                                elif EBleedRes>EBleed:
                                    EBleed/=2
                    if EPois>0 and EPoisT>0: #Проверка на отравление врага
                        if EnemyType=="Нежить" and EnemyType=="Механизм":
                            EPois=0; EPoisT=0
                            print("Это существо невосприимчиво к отравлению")
                        else:
                            if EPoisRes>EPois:
                                if EPoisRes>EPois*2:
                                    EPois=0
                                    EPoisT=0
                                elif EPoisRes>EPois:
                                    EPois/=2
                    if EFear>0 and EFearT>0: #Проверка на страх врага
                        if EnemyType=="Нежить" and EnemyType=="Механизм":
                            EFear=0; EFearT=0
                            print("Это существо невосприимчиво к страху")
                        else:
                            if EFearRes>EFear:
                                if EFearRes>EFear*2:
                                    EFear=0
                                    EFearT=0
                                elif EFearRes>EFear:
                                    EFearT/=2 
                    if EToss>0 and ETossT>0: #Проверка на подброс врага
                        if ETossRes>EToss:
                            if ETossRes>EToss*2:
                                EToss=0
                                ETossT=0
                            elif ETossRes>EToss:
                                EFearT/=2
                    if EStun>0 and EStunT>0: ##Проверка на оглушение врага
                        if EStunRes>EStun:
                            if EStunRes>EStun*2:
                                EStun=0
                                EStunT=0
                            elif EStunRes>EStun:
                                EStunT/=2
                    if ESile>0 and ESileT>0: #Проверка на молчание врага
                        if ESileRes>ESile:
                            if ESileRes>ESile*2:
                                ESile=0
                                ESileT=0
                            elif ESileRes>ESile:
                                ESileT/=2
                    if EDisarm>0 and EDisarmT>0: #Проверка на обезоруживание врага
                        if EDisarmRes>EDisarm:
                            if EDisarmRes>EDisarm*2:
                                EDisarm=0
                                EDisarmT=0
                            elif EDisarmRes>EDisarm:
                                EDisarmT/=2
                    if EArmless>0 and EArmlessT>0: #Проверка на снижение брони врага
                        if EArmlessRes>EArmless:
                            if EArmlessRes>EArmless*2:
                                EArmless=0
                                EArmlessT=0
                            elif EArmlessRes>EArmless:
                                EArmless/=2
                    if EBlind>0 and EBlindT>0: #Проверка на слепоту врага
                        if EnemyType=="Нежить" and EnemyType=="Механизм":
                            EBlind=0; EBlindT=0
                            print("Это существо невосприимчиво к слепоте")
                        else:
                            if EBlindRes>EBlind:
                                if EBlindRes>EBlind*2:
                                    EBlind=0
                                    EBlindT=0
                                elif EBlindRes>EBlind:
                                    EPois/=2
                    if EFireT>0 or EBleedT>0 or EPoisT>0 or EFearT>0 or ETossT>0 or EStunT>0 or ESileT>0 or EDisarmT>0 or EArmlessT>0 or EBlindT>0:
                        if EFireT>0:
                            EFireT-=1
                        if EBleedT>0:
                            EBleedT-=1
                        if EPoisT>0:
                            EPoisT-=1
                        if EFearT>0:
                            EFearT-=1
                        if ETossT>0:
                            ETossT-=1
                        if EStunT>0:
                            EStunT-=1
                        if ESileT>0:
                            ESileT-=1
                        if EDisarmT>0:
                            EDisarmT-=1
                        if EArmlessT>0:
                            EArmlessT-=1
                        if EBlindT>0:
                            EBlindT-=1
                        i+=1
                if SID[27]==1:
                    print("Ваше здоровье: ",HP,"Здоровье врага: ",ZV)
                else:
                    print("Ваше здоровье: ",HP,"Здоровье врага: ","X")
                print("Выберите место для удара \n1)Голова\n2)Тело\n3)Низ\n4)Применить умение\n",name,": ")
                block=random.randint(1,3)
                CSS=int(input())
                print(block)
                if CSS==4:
                    print("Выберите навык: ",SA0)
                    CSS=int(input())
                    if CSS>len(SA0):
                        print("Выберите другое место")
                    else:
                        active(CSS)
                        if vozvrat==1:
                            print("Вы не можете использовать этот навык")
                            FireDMG=0;WaterDMG=0;AirDMG=0;EarthDMG=0;DarkDMG=0;PhisDMG=0;TrueDMG=0;EFire=0;EFireT=0
                        elif vozvrat==0:
                            print("Вы использовали: ",SA0[CSS-1])
                            if FireDMG>0:
                                if EFireRes>=FireDMG:
                                    print("Огненный урон не прошёл слишком большая защита")
                                elif EFireRes<FireDMG:
                                    ZV=ZV-(FireDMG-EFireRes)
                                    print("Нанесенно: ",FireDMG-EFireRes," огненного урона")
                            if WaterDMG>0:
                                if EWaterRes>=WaterDMG:
                                    print("Водяной урон не прошёл слишком большая защита")
                                elif EWaterRes<WaterDMG:
                                    ZV=ZV-(WaterDMG-EWaterRes)
                                    print("Нанесенно: ",WaterDMG-EWaterRes," водяного урона")
                            if AirDMG>0:
                                if EAirRes>=AirDMG:
                                    print("Воздушный урон не прошёл слишком большая защита")
                                elif EAirRes<AirDMG:
                                    ZV=ZV-(AirDMG-EAirRes)
                                    print("Нанесенно: ",AirDMG-EAirRes," воздушного урона")
                            if EarthDMG>0:
                                if EEarthRes>=EarthDMG:
                                    print("Земляной урон не прошёл слишком большая защита")
                                elif EEarthRes<EarthDMG:
                                    ZV=ZV-(EarthDMG-EEarthRes)
                                    print("Нанесенно: ",EarthDMG-EEarthRes," земляного урона")
                            if PhisDMG>0:
                                if EPhisRes>=PhisDMG:
                                    print("Физический урон не прошёл слишком большая защита")
                                elif EPhisRes<PhisDMG:
                                    ZV=ZV-(PhisDMG-EPhisRes)
                                    print("Нанесенно: ",PhishDMG-EPhisRes," физического урона")
                            if DarkDMG>0:
                                ZV=ZV-DarkDMG
                                print("Нанесенно: ",DarkDMG," тёмного урона")
                            if TrueDMG>0:
                                ZV=ZV-TrueDMG
                                print("Нанесенно: ",TrueDMG," тёмного урона")
                            totalDMG=FireDMG+WaterDMG+AirDMG+EarthDMG+PhisDMG+DarkDMG+TrueDMG
                            print("Всего нанесено: ", totalDMG, " урона!")
                            i+=1
                elif CSS==1 or CSS==2 or CSS==3:
                    if CSS==block:
                        print("Удар был заблокирован")
                        i+=1
                    else:
                        print("Удар прошёл благополучно")
                        if weapon=="power":
                            ZV-=urons
                            i+=1
                        elif weapon=="agility":
                            ZV-=urona
                            i+=1
                        elif weapon=="magic":
                            ZV-=uronm
                            i+=1
                else:
                    print("Выберете другое место")
                    continue
            else:
                print("Ваш ход")
                if SID[27]==1:
                    print("Ваше здоровье: ",HP,"Здоровье врага: ",ZV)
                else:
                    print("Ваше здоровье: ",HP,"Здоровье врага: ","X")
                print("Выберите место для блока \n1)Голова\n2)Тело\n3)Низ\n",name,": ")
                atack=random.randint(1,3)
                CSS=int(input())
                print(atack)
                if CSS==1 or CSS==2 or CSS==3:
                    if CSS==atack:
                        print("Удар был заблокирован")
                        i+=1
                        continue
                    else:
                        dmg=AV-PhisRes
                        print("Вы получили удар. Урон: ",dmg)
                        HP-=dmg
                        i+=1
                else:
                    print("Выберете другое место")
                    continue
def fight2(x):
    print()
def fight3(x):
    print()

#Экипировка персонажа
Equipment=["Пусто","Пусто","Пусто","Пусто","Пусто","Пусто"]
invent=["Правая рука","Левая рука","Голова","Торс","Руки","Ноги"]
inventID=["000","000","000","000","000","000"]
meshok=[]
meshokID=[]
def inventar(): #Инвентарь
    global invent, inventID, meshok, meshokID, AS, AM, AA, AH, HP, atk, PhisRes, weapon, AS,AM,AA,AH,Equipment
    while True:
        AS[0]=AS[1]+AS[2]+AS[3]+AS[4]+AS[5]+AS[6]; AM[0]=AM[1]+AM[2]+AM[3]+AM[4]+AM[5]+AM[6]; AA[0]=AA[1]+AA[2]+AA[3]+AA[4]+AA[5]+AA[6]; AH[0]=AH[1]+AH[2]+AH[3]+AH[4]+AH[5]+AH[6]
        FS=S+AS[0]; FM=M+AM[0]; FA=A+AA[0]; FH=H+AH[0]; urons=FS*2+atk; uronm=FM*2+atk; urona=FA*2+atk; FHP=FH*5; FMP=FM*5
        print ("Инвентарь: \n",invent,"\nТип экипировки: \n",Equipment,"\nЧто вы хотите сделать?\n1)Надеть вещь\n2)Снять вещь\n3)О персонаже\n4)Выход")
        CSS=int(input())
        if CSS==1: #Одеть шмот
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|  Какую вещь вы хотите надеть? (Наберите номер вещи по счёту)                        |")
            print("|",meshok)
            print("|  Введите 0 для отмены                                                               |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print(name,": ")
            CSS=int(input())
            if CSS==0:
                continue
            else:
                try:
                    x=meshok[CSS-1]
                    y=meshokID[CSS-1]
                    z=y[:1]
                    if z=="1":
                        if inventID[0]=="000":
                            if y[1:2]=="1":
                                if z==y[2:3]=="1":
                                    atk=5
                                    invent[0]=x
                                    inventID[0]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Одноручный меч"
                                elif z==y[2:3]=="2":
                                    if SID[1]==1:
                                        atk=13
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный меч"
                                    else:
                                        print("Нужен навык одноручные мечи")
                                        continue
                                elif z==y[2:3]=="3":
                                    if SID[1]==2:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный меч"
                                    else:
                                        print("Нужен навык одноручные мечи lvl 2")
                                        continue
                                elif z==y[2:3]=="4":
                                    if SID[1]==3:
                                        atk=25
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный меч"
                                    else:
                                        print("Нужен навык одноручные мечи lvl 3")
                                        continue
                                elif z==y[2:3]=="5":
                                    if SID[1]==2:
                                        atk=35
                                        AS[1]=10
                                        AA[1]=7
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный меч"
                                    else:
                                        print("Нужен навык одноручные мечи lvl 2")
                                        continue
                                elif z==y[2:3]=="6":
                                    if SID[1]==2:
                                        atk=35
                                        AS[1]=7
                                        AA[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный меч"
                                    else:
                                        print("Нужен навык одноручные мечи lvl 2")
                                        continue
                            elif y[1:2]=="2":
                                if z==y[2:3]=="1":
                                    atk=10
                                    invent[0]=x
                                    inventID[0]=y
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Двуручный меч"
                                    Equipment[1]="Двуручный меч"
                                elif z==y[2:3]=="2":
                                    if SID[0]==1:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный меч"
                                        Equipment[1]="Двуручный меч"
                                    else:
                                        print("Нужен навык двуручные мечи")
                                        continue
                                elif z==y[2:3]=="3":
                                    if SID[0]==2:
                                        atk=26
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный меч"
                                        Equipment[1]="Двуручный меч"
                                    else:
                                        print("Нужен навык двуручные мечи lvl 2")
                                        continue
                                elif z==y[2:3]=="4":
                                    if SID[0]==3:
                                        atk=35
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный меч"
                                        Equipment[1]="Двуручный меч"
                                    else:
                                        print("Нужен навык двуручные мечи lvl 3")
                                        continue
                                elif z==y[2:3]=="5":
                                    if SID[0]==2:
                                        atk=48
                                        AS[1]=15
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный меч"
                                        Equipment[1]="Двуручный меч"
                                    else:
                                        print("Нужен навык двуручные мечи lvl 2")
                                        continue
                                elif z==y[2:3]=="6":
                                    if SID[0]==3:
                                        atk=56
                                        AS[1]=20
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный меч"
                                        Equipment[1]="Двуручный меч"
                                    else:
                                        print("Нужен навык двуручные мечи lvl 3")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    atk=5
                                    invent[0]=x
                                    inventID[0]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Одноручный топор"
                                elif y[2:3]=="2":
                                    if SID[5]==1:
                                        atk=13
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный топор"
                                    else:
                                        print("Нужен навык одноручные топоры")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[5]==2:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный топор"
                                    else:
                                        print("Нужен навык одноручные топоры lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[5]==3:
                                        atk=25
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный топор"
                                    else:
                                        print("Нужен навык одноручные топоры lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[5]==2:
                                        atk=40
                                        AS[1]=10
                                        AH[1]=7
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный топор"
                                    else:
                                        print("Нужен навык одноручные топоры lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[5]==3:
                                        atk=35
                                        AS[1]=15
                                        AH[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручный топор"
                                    else:
                                        print("Нужен навык одноручные топоры lvl 3")
                                        continue
                            elif y[1:2]=="4":
                                if y[2:3]=="1":
                                    atk=10
                                    invent[0]=x
                                    inventID[0]=y
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Двуручный топор"
                                    Equipment[1]="Двуручный топор"
                                elif y[2:3]=="2":
                                    if SID[4]==1:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный топор"
                                        Equipment[1]="Двуручный топор"
                                    else:
                                        print("Нужен навык двуручные топоры")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[4]==2:
                                        atk=26
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный топор"
                                        Equipment[1]="Двуручный топор"
                                    else:
                                        print("Нужен навык двуручные топоры lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[4]==3:
                                        atk=35
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный топор"
                                        Equipment[1]="Двуручный топор"
                                    else:
                                        print("Нужен навык двуручные топоры lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[4]==2:
                                        atk=48
                                        AS[1]=15
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный топор"
                                        Equipment[1]="Двуручный топор"
                                    else:
                                        print("Нужен навык двуручные топоры lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[4]==3:
                                        atk=56
                                        AS[1]=20
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручный топор"
                                        Equipment[1]="Двуручный топор"
                                    else:
                                        print("Нужен навык двуручные топоры lvl 3")
                                        continue
                            elif y[1:2]=="5":
                                if y[2:3]=="1":
                                    atk=5
                                    invent[0]=x
                                    inventID[0]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Одноручная булава"
                                elif y[2:3]=="2":
                                    if SID[3]==1:
                                        atk=13
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручная булава"
                                    else:
                                        print("Нужен навык одноручные булавы")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[3]==2:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручная булава"
                                    else:
                                        print("Нужен навык одноручные булавы lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[3]==3:
                                        atk=25
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручная булава"
                                    else:
                                        print("Нужен навык одноручные булавы lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[3]==2:
                                        atk=40
                                        AS[1]=10
                                        AH[1]=7
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручная булава"
                                    else:
                                        print("Нужен навык одноручные булавы lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[3]==3:
                                        atk=35
                                        AS[1]=15
                                        AH[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Одноручная булава"
                                    else:
                                        print("Нужен навык одноручные булавы lvl 3")
                                        continue
                            elif y[1:2]=="6":
                                if y[2:3]=="1":
                                    atk=10
                                    invent[0]=x
                                    inventID[0]=y
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="power"
                                    Equipment[0]="Двуручная булава"
                                    Equipment[1]="Двуручная булава"
                                elif y[2:3]=="2":
                                    if SID[2]==1:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручная булава"
                                        Equipment[1]="Двуручная булава"
                                    else:
                                        print("Нужен навык двуручные булавы")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[2]==2:
                                        atk=26
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручная булава"
                                        Equipment[1]="Двуручная булава"
                                    else:
                                        print("Нужен навык двуручные булавы lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[2]==3:
                                        atk=35
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручная булава"
                                        Equipment[1]="Двуручная булава"
                                    else:
                                        print("Нужен навык двуручные булавы lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[2]==2:
                                        atk=48
                                        AS[1]=15
                                        AH[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручная булава"
                                        Equipment[1]="Двуручная булава"
                                    else:
                                        print("Нужен навык двуручные булавы lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[2]==3:
                                        atk=56
                                        AS[1]=20
                                        AH[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="power"
                                        Equipment[0]="Двуручная булава"
                                        Equipment[1]="Двуручная булава"
                                    else:
                                        print("Нужен навык двуручные булавы lvl 3")
                                        continue
                            elif y[1:2]=="7":
                                if y[2:3]=="1":
                                    atk=5
                                    invent[0]=x
                                    inventID[0]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="magic"
                                    Equipment[0]="Скипетр"
                                elif y[2:3]=="2":
                                    if SID[7]==1:
                                        atk=13
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Скипетр"
                                    else:
                                        print("Нужен навык скипетры")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[7]==2:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Скипетр"
                                    else:
                                        print("Нужен навык скипетры lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[7]==3:
                                        atk=25
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Скипетр"
                                    else:
                                        print("Нужен навык скипетры lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[7]==2:
                                        atk=40
                                        AM[1]=15
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Скипетр"
                                    else:
                                        print("Нужен навык скипетры lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[7]==3:
                                        atk=35
                                        AM[1]=15
                                        AH[1]=6
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Скипетр"
                                    else:
                                        print("Нужен навык скипетры lvl 3")
                                        continue
                            elif y[1:2]=="8":
                                if y[2:3]=="1":
                                    atk=10
                                    invent[0]=x
                                    inventID[0]=y
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="magic"
                                    Equipment[0]="Боевой посох"
                                    Equipment[1]="Боевой посох"
                                elif y[2:3]=="2":
                                    if SID[6]==1:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Боевой посох"
                                        Equipment[1]="Боевой посох"
                                    else:
                                        print("Нужен навык боевой посох")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[6]==2:
                                        atk=26
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Боевой посох"
                                        Equipment[1]="Боевой посох"
                                    else:
                                        print("Нужен навык боевой посох lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[6]==3:
                                        atk=35
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Боевой посох"
                                        Equipment[1]="Боевой посох"
                                    else:
                                        print("Нужен навык боевой посох lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[6]==2:
                                        atk=48
                                        AM[1]=14
                                        AH[1]=5
                                        AA[1]=14
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Боевой посох"
                                        Equipment[1]="Боевой посох"
                                    else:
                                        print("Нужен навык боевой посох lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[6]==3:
                                        atk=56
                                        AA[1]=20
                                        AH[1]=10
                                        AM[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="magic"
                                        Equipment[0]="Боевой посох"
                                        Equipment[1]="Боевой посох"
                                    else:
                                        print("Нужен навык боевой посох lvl 3")
                                        continue
                            elif y[1:2]=="9":
                                if y[2:3]=="1":
                                    atk=10
                                    invent[0]=x
                                    inventID[0]=y
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="agility"
                                    Equipment[0]="Лук"
                                    Equipment[1]="Лук"
                                elif y[2:3]=="2":
                                    if SID[29]==1:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Лук"
                                        Equipment[1]="Лук"
                                    else:
                                        print("Нужен навык луки")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[29]==2:
                                        atk=26
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Лук"
                                        Equipment[1]="Лук"
                                    else:
                                        print("Нужен навык луки lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[29]==3:
                                        atk=35
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Лук"
                                        Equipment[1]="Лук"
                                    else:
                                        print("Нужен навык луки lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[29]==2:
                                        atk=54
                                        AH[1]=5
                                        AA[1]=18
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Лук"
                                        Equipment[1]="Лук"
                                    else:
                                        print("Нужен навык луки lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[29]==3:
                                        atk=66
                                        AA[1]=20
                                        invent[0]=x
                                        inventID[0]=y
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Лук"
                                        Equipment[1]="Лук"
                                    else:
                                        print("Нужен навык луки lvl 3")
                                        continue
                            elif y[1:2]=="0":
                                if y[2:3]=="1":
                                    atk=5
                                    invent[0]=x
                                    inventID[0]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    weapon="agility"
                                    Equipment[0]="Кинжал"
                                elif y[2:3]=="2":
                                    if SID[28]==1:
                                        atk=13
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Кинжал"
                                    else:
                                        print("Нужен навык кинжалы")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[28]==2:
                                        atk=18
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Кинжал"
                                    else:
                                        print("Нужен навык кинжалы lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[28]==3:
                                        atk=25
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Кинжал"
                                    else:
                                        print("Нужен навык кинжалы lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[28]==2:
                                        atk=35
                                        AS[1]=10
                                        AA[1]=7
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Кинжал"
                                    else:
                                        print("Нужен навык кинжалы lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[28]==2:
                                        atk=50
                                        AS[1]=7
                                        AA[1]=10
                                        invent[0]=x
                                        inventID[0]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        weapon="agility"
                                        Equipment[0]="Кинжал"
                                    else:
                                        print("Нужен навык кинжалы lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                    elif z=="2":
                        if inventID[1]=="000":
                            if y[1:2]=="1":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[1]="Баклер"
                                elif y[2:3]=="2":
                                    if SID[8]==1:
                                        PhisRes=13
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Баклер"
                                    else:
                                        print("Нужен навык баклеры")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[8]==2:
                                        PhisRes=18
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Баклер"
                                    else:
                                        print("Нужен навык баклеры lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[8]==3:
                                        PhisRes=25
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Баклер"
                                    else:
                                        print("Нужен навык баклеры lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[8]==2:
                                        PhisRes=35
                                        AS[2]=11
                                        AA[2]=7
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Баклер"
                                    else:
                                        print("Нужен навык баклеры lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[8]==2:
                                        PhisRes=35
                                        AS[2]=7
                                        AA[2]=11
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Баклер"
                                    else:
                                        print("Нужен навык баклеры lvl 2")
                                        continue
                            elif y[1:2]=="2":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[1]="Щит"
                                elif y[2:3]=="2":
                                    if SID[9]==1:
                                        PhisRes=13
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Щит"
                                    else:
                                        print("Нужен навык щиты")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[9]==2:
                                        PhisRes=18
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Щит"
                                    else:
                                        print("Нужен навык щиты lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[9]==3:
                                        PhisRes=25
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Щит"
                                    else:
                                        print("Нужен навык щиты lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[9]==2:
                                        PhisRes=35
                                        AS[2]=11
                                        AA[2]=7
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Щит"
                                    else:
                                        print("Нужен навык щиты lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[9]==2:
                                        PhisRes=35
                                        AS[2]=7
                                        AA[2]=11
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Щит"
                                    else:
                                        print("Нужен навык щиты lvl 2")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[1]=x
                                    inventID[1]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[1]="Башенный щит"
                                elif y[2:3]=="2":
                                    if SID[10]==1:
                                        PhisRes=13
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Башенный щит"
                                    else:
                                        print("Нужен навык башенные щиты")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[10]==2:
                                        PhisRes=18
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Башенный щит"
                                    else:
                                        print("Нужен навык башенные щиты lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[10]==3:
                                        PhisRes=25
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Башенный щит"
                                    else:
                                        print("Нужен навык башенные щиты lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[10]==2:
                                        PhisRes=35
                                        AS[2]=11
                                        AA[2]=7
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Башенный щит"
                                    else:
                                        print("Нужен навык башенные щиты lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[10]==2:
                                        PhisRes=35
                                        AS[2]=7
                                        AA[2]=11
                                        invent[1]=x
                                        inventID[1]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[1]="Башенный щит"
                                    else:
                                        print("Нужен навык башенные щиты lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                    elif z=="3":
                        if inventID[2]=="000":
                            if y[1:2]=="1":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Одежда"
                                elif y[2:3]=="2":
                                    PhisRes=18
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Одежда"
                                elif y[2:3]=="3":
                                    PhisRes=25
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Одежда"
                                elif y[2:3]=="4":
                                    PhisRes=35
                                    AS[3]=11
                                    AA[3]=7
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Одежда"
                                elif y[2:3]=="5":
                                    PhisRes=35
                                    AS[3]=7
                                    AA[3]=11
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Одежда"
                            elif y[1:2]=="2":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Лёгкая броня"
                                elif y[2:3]=="2":
                                    if SID[11]==1:
                                        PhisRes=13
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[11]==2:
                                        PhisRes=18
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[11]==3:
                                        PhisRes=25
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[3]=11
                                        AA[3]=7
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[3]=7
                                        AA[3]=11
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Средняя броня"
                                elif y[2:3]=="2":
                                    if SID[12]==1:
                                        PhisRes=13
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[12]==2:
                                        PhisRes=18
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[12]==3:
                                        PhisRes=25
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[3]=11
                                        AA[3]=7
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[3]=7
                                        AA[3]=11
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                            elif y[1:2]=="4":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[2]=x
                                    inventID[2]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[2]="Тяжёлая броня"
                                elif y[2:3]=="2":
                                    if SID[13]==1:
                                        PhisRes=13
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[13]==2:
                                        PhisRes=18
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[13]==3:
                                        PhisRes=25
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[3]=11
                                        AA[3]=7
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[3]=7
                                        AA[3]=11
                                        invent[2]=x
                                        inventID[2]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[2]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                    elif z=="4":
                        if inventID[3]=="000":
                            if y[1:2]=="1":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Одежда"
                                elif y[2:3]=="2":
                                    PhisRes=18
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Одежда"
                                elif y[2:3]=="3":
                                    PhisRes=25
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Одежда"
                                elif y[2:3]=="4":
                                    PhisRes=35
                                    AS[4]=11
                                    AA[4]=7
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Одежда"
                                elif y[2:3]=="5":
                                    PhisRes=35
                                    AS[4]=7
                                    AA[4]=11
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Одежда"
                            elif y[1:2]=="2":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Лёгкая броня"
                                elif y[2:3]=="2":
                                    if SID[11]==1:
                                        PhisRes=13
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[11]==2:
                                        PhisRes=18
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[11]==3:
                                        PhisRes=25
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[4]=11
                                        AA[4]=7
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[4]=7
                                        AA[4]=11
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Средняя броня"
                                elif y[2:3]=="2":
                                    if SID[12]==1:
                                        PhisRes=13
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[12]==2:
                                        PhisRes=18
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[12]==3:
                                        PhisRes=25
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[4]=11
                                        AA[4]=7
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[4]=7
                                        AA[4]=11
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                            elif y[1:2]=="4":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[3]=x
                                    inventID[3]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[3]="Тяжёлая броня"
                                elif y[2:3]=="2":
                                    if SID[13]==1:
                                        PhisRes=13
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[13]==2:
                                        PhisRes=18
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[13]==3:
                                        PhisRes=25
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[4]=11
                                        AA[4]=7
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[4]=7
                                        AA[4]=11
                                        invent[3]=x
                                        inventID[3]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[3]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                    elif z=="5":
                        if inventID[4]=="000":
                            if y[1:2]=="1":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Одежда"
                                elif y[2:3]=="2":
                                    PhisRes=18
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Одежда"
                                elif y[2:3]=="3":
                                    PhisRes=25
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Одежда"
                                elif y[2:3]=="4":
                                    PhisRes=35
                                    AS[5]=11
                                    AA[5]=7
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Одежда"
                                elif y[2:3]=="5":
                                    PhisRes=35
                                    AS[5]=7
                                    AA[5]=11
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Одежда"
                            elif y[1:2]=="2":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Лёгкая броня"
                                elif y[2:3]=="2":
                                    if SID[11]==1:
                                        PhisRes=13
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[11]==2:
                                        PhisRes=18
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[11]==3:
                                        PhisRes=25
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[5]=11
                                        AA[5]=7
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[5]=7
                                        AA[5]=11
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Средняя броня"
                                elif y[2:3]=="2":
                                    if SID[12]==1:
                                        PhisRes=13
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[12]==2:
                                        PhisRes=18
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[12]==3:
                                        PhisRes=25
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[5]=11
                                        AA[5]=7
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[5]=7
                                        AA[5]=11
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                            elif y[1:2]=="4":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[4]=x
                                    inventID[4]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[4]="Тяжёлая броня"
                                elif y[2:3]=="2":
                                    if SID[13]==1:
                                        PhisRes=13
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[13]==2:
                                        PhisRes=18
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[13]==3:
                                        PhisRes=25
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[5]=11
                                        AA[5]=7
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[5]=7
                                        AA[5]=11
                                        invent[4]=x
                                        inventID[4]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[4]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                    elif z=="6":
                        if inventID[5]=="000":
                            if y[1:2]=="1":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Одежда"
                                elif y[2:3]=="2":
                                    PhisRes=18
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Одежда"
                                elif y[2:3]=="3":
                                    PhisRes=25
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Одежда"
                                elif y[2:3]=="4":
                                    PhisRes=35
                                    AS[6]=11
                                    AA[6]=7
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Одежда"
                                elif y[2:3]=="5":
                                    PhisRes=35
                                    AS[6]=7
                                    AA[6]=11
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Одежда"
                            elif y[1:2]=="2":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Лёгкая броня"
                                elif y[2:3]=="2":
                                    if SID[11]==1:
                                        PhisRes=13
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[11]==2:
                                        PhisRes=18
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[11]==3:
                                        PhisRes=25
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[6]=11
                                        AA[6]=7
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[11]==2:
                                        PhisRes=35
                                        AS[6]=7
                                        AA[6]=11
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Лёгкая броня"
                                    else:
                                        print("Нужен навык лёгкая броня lvl 2")
                                        continue
                            elif y[1:2]=="3":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Средняя броня"
                                elif y[2:3]=="2":
                                    if SID[12]==1:
                                        PhisRes=13
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[12]==2:
                                        PhisRes=18
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[12]==3:
                                        PhisRes=25
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[6]=11
                                        AA[6]=7
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[12]==2:
                                        PhisRes=35
                                        AS[6]=7
                                        AA[6]=11
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Средняя броня"
                                    else:
                                        print("Нужен навык средняя броня lvl 2")
                                        continue
                            elif y[1:2]=="4":
                                if y[2:3]=="1":
                                    PhisRes=5
                                    invent[5]=x
                                    inventID[5]=y
                                    meshokID.pop(CSS-1)
                                    meshok.pop(CSS-1)
                                    Equipment[5]="Тяжёлая броня"
                                elif y[2:3]=="2":
                                    if SID[13]==1:
                                        PhisRes=13
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня")
                                        continue
                                elif y[2:3]=="3":
                                    if SID[13]==2:
                                        PhisRes=18
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="4":
                                    if SID[13]==3:
                                        PhisRes=25
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 3")
                                        continue
                                elif y[2:3]=="5":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[6]=11
                                        AA[6]=7
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                                elif y[2:3]=="6":
                                    if SID[13]==2:
                                        PhisRes=35
                                        AS[6]=7
                                        AA[6]=11
                                        invent[5]=x
                                        inventID[5]=y
                                        meshokID.pop(CSS-1)
                                        meshok.pop(CSS-1)
                                        Equipment[5]="Тяжёлая броня"
                                    else:
                                        print("Нужен навык тяжёлая броня lvl 2")
                                        continue
                        else:
                            print("Этот слот экипирован")
                            continue
                except IndexError:
                    print("Введите правильный номер")
                    print("------------------------")
                    continue
        elif CSS==2: #Снять шмот
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|  Экипировка: ")
            print("|",invent)
            print("|  Тип экипировки: ")
            print("|",Equipment)
            print("|---------------------------------\n|  Какую ячейку выхотите освободить?\n|  1)Правую руку\n|  2)Левую руку\n|  3)Голова   ") 
            print("|  4)Торс\n|  5)Перчатки\n|  6)Сапоги\n|  Введите 0 для отмены                         ")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print(name,": ")
            CSS=int(input())
            if CSS==0:
                continue
            else:
                if CSS==1 and invent[0]!="Правая рука":
                    if y[1:2]=="2" or y[1:2]=="4" or y[1:2]=="6" or y[1:2]=="8" or y[1:2]=="9":
                        meshokID.append(inventID[0])
                        meshok.append(invent[0])
                        invent[0]="Правая рука"
                        inventID[0]="000"
                        invent[1]="Левая рука"
                        inventID[1]="000"
                        AS[1]=0
                        AA[1]=0
                        AM[1]=0
                        AH[1]=0
                        Equipment[0]="Пусто"
                        Equipment[1]="Пусто"
                        print("------------------------")
                    else:
                        meshokID.append(inventID[0])
                        meshok.append(invent[0])
                        invent[0]="Правая рука"
                        inventID[0]="000"
                        AS[1]=0
                        AA[1]=0
                        AM[1]=0
                        AH[1]=0
                        Equipment[0]="Пусто"
                        print("------------------------")
                elif CSS==2 and invent[1]!="Левая рука":
                    if (y[:1]=="1" and y[1:2]=="2") or (y[:1]=="1" and y[1:2]=="4") or (y[:1]=="1" and y[1:2]=="6") or (y[:1]=="1" and y[1:2]=="8") or (y[:1]=="1" and y[1:2]=="9"):
                        meshokID.append(inventID[0])
                        meshok.append(invent[0])
                        invent[0]="Правая рука"
                        inventID[0]="000"
                        invent[1]="Левая рука"
                        inventID[1]="000"
                        AS[1]=0
                        AA[1]=0
                        AM[1]=0
                        AH[1]=0
                        Equipment[0]="Пусто"
                        Equipment[1]="Пусто"
                        print("------------------------")
                    else:
                        meshokID.append(inventID[1])
                        meshok.append(invent[1])
                        invent[1]="Левая рука"
                        inventID[1]="000"
                        AS[2]=0
                        AA[2]=0
                        AM[2]=0
                        AH[2]=0
                        Equipment[1]="Пусто"
                        print("------------------------")
                elif CSS==3 and invent[2]!="Голова":
                    meshokID.append(inventID[2])
                    meshok.append(invent[2])
                    invent[2]="Голова"
                    inventID[2]="000"
                    AS[3]=0
                    AA[3]=0
                    AM[3]=0
                    AH[3]=0
                    Equipment[2]="Пусто"
                    print("------------------------")
                elif CSS==4 and invent[3]!="Торс":
                    meshokID.append(inventID[3])
                    meshok.append(invent[3])
                    invent[3]="Торс"
                    inventID[3]="000"
                    AS[4]=0
                    AA[4]=0
                    AM[4]=0
                    AH[4]=0
                    Equipment[3]="Пусто"
                    print("------------------------")
                elif CSS==5 and invent[4]!="Руки":
                    meshokID.append(inventID[4])
                    meshok.append(invent[4])
                    invent[4]="Руки"
                    inventID[4]="000"
                    AS[5]=0
                    AA[5]=0
                    AM[5]=0
                    AH[5]=0
                    Equipment[4]="Пусто"
                    print("------------------------")
                elif CSS==6 and invent[5]!="Ноги":
                    meshokID.append(inventID[5])
                    meshok.append(invent[5])
                    invent[5]="Ноги"
                    inventID[5]="000"
                    AS[6]=0
                    AA[6]=0
                    AM[6]=0
                    AH[6]=0
                    Equipment[5]="Пусто"
                    print("------------------------")
                else:
                    print("Действие невозможно")
                    print("------------------------")
                    continue
        elif CSS==3: #О персонаже
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|  Имя персонажа: ",name,"\n|  Название класса: ",classname,"\n|  Ваш уровень: ",lvl,"\n|  Опыт: ",exp,"/",expup,"\n|---------------","\n|  Текущие значения: ","\n|  Сила(Свои/предметы)",FS," (",S,"/",AS[0],")","\n|  Ловкость(Свои/предметы)",FA," (",A,"/",AA[0],")","\n|  Мудрость(Свои/предметы)",FM," (",M,"/",AM[0],")","\n|  Здоровье(Свои/предметы)",FH," (",H,"/",AH[0],")","\n|---------------","\n|  Способности: ",S0,"\n|  Активные способности: ",SA0,"\n|---------------","\n|  Очки здоровья: ",HP,"/",FHP,"\n|  Очки маны/духа: ",MP,"/",FMP)
            if weapon=="power":
                print("|  Урон(Свой/предметы): ",urons," (",S*2,"/",AS[0]*2+atk,")")
            elif weapon=="agility":
                print("|  Урон(Свой/предметы): ",urona," (",A*2,"/",AA[0]*2+atk,")")
            elif weapon=="magic":
                print("|  Урон(Свой/предметы): ",urona," (",M*2,"/",AM[0]*2+atk,")")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            input("\nНажмите enter для дальнейших действий")
            continue
        elif CSS==4:
            break     
def lvlup(): #Прокачка персонажа  
        #Характеристики
    global P,SP,SAP,S,M,A,H
        #Способности пассивные
    global S0,SID
    #Способности активные
    global SA0,SAID
    while True:
        FS=S+AS[0]; FM=M+AM[0]; FA=A+AA[0]; FH=H+AH[0]; urons=FS*2+atk; uronm=FM*2+atk; urona=FA*2+atk; FHP=FH*5; FMP=FM*5
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|  Ваш уровень: ",lvl,"                                                                     |")
        print("|  Опыт: ",exp,"/",expup,"                                                                      |")
        print("|  Количество очков характеристик: ",P,"                                                  |")
        print("|  Количество очков пассивных способностей: ",SP,"                                         |")
        print("|  Количество очков активных способностей: ",SAP,"                                          |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\nЧто вы желаете распределить:\n1)Очки характеристик\n2)Очки пассивных способностей\n3)Очки активных способностей\n4)О персонаже\n5)Выход")
        print(name,": ")
        CSS=input()
        if CSS=="1": #Раскачка характеристик
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("\n|  Имя персонажа: ",name,"\n|  Название класса: ",classname,"\n|  Текущие значения: ","\n|  Количество очков характеристик: ",P,"\n|  Сила",S,"\n|  Ловкость",A,"\n|  Мудрость",M,"\n|  Здоровье",H,"\n---------------")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("\nКакую характеристику изменить?\n1)Стать сильнее\n2)Стать ловче\n3)Стать мудрее\n4)Стать выносливее")
            print(name,":")
            CSS=input()
            if (CSS == "Сила" or CSS == "Ловкость" or CSS == "Мудрость" or CSS == "Здоровье" or CSS=="1" or CSS=="2" or CSS=="3" or CSS=="4"):
                print("Какое количество очков ты желаешь вложить?")
                print(name,": ")
                CSS2=int(input())
                if CSS2>P:
                    print("Действие невозможно")
                elif CSS2<=P:
                    if CSS=="Сила" or CSS=="1": 
                        S+=CSS2
                        P-=CSS2
                    elif CSS=="Ловкость" or CSS=="2":
                        A+=CSS2
                        P-=CSS2
                    elif CSS=="Мудрость" or CSS=="3":
                        M+=CSS2
                        P-=CSS2
                    elif CSS=="Здоровье" or CSS=="4":
                        H+=CSS2
                        P-=CSS2
            else:
                print("Неизвестный: Такой характеристики нету")
        elif CSS=="2": #Раскачка способностей
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|  Имя персонажа: ",name)
            print("|  Название класса: ",classname)
            print("|  Текущие значения: ")
            print("|  Очки пассивных способностей: ",SP)
            print("|  Способности: ",S0,)
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("\nСпособности: ")
            print("Экипировка:\n1)Двуручные мечи  2)Одноручные мечи\n3)Двуручные булавы  4)Одноручные булавы\n5)Двуручные топоры  6)Одноручные топоры\n7)Боевые посохи  8)Скипетры\n9)Баклеры       10)Щиты\n11)Башенные щиты  12)Лёгкая броня\n13)Средняя броня  14)Тяжёлая броня\nМагия:\n15)Магия огня  16)Магия земли\n17)Магия воздуха  18)Магия воды\n19)Магия тьмы\nВспомогательные:\n20)Чтение свитков  21)Скрытность\n22)Критический удар  23)Вскрытие замков\n24)Использование ловушек  25)Наблюдательность\n26)Лечение  27)Парирование\n28)Оценка  29)Кинжалы\n30)Луки  31)Дух")
            print(name,": ")
            CSS=input()
            if CSS=="1" or CSS=="Двуручные мечи":
                if SID[0]<4:
                    print("Навык двуручные мечи отвечает за возможность использования двуручных мечей и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[0]+=1
                        SP-=1
                        if SID[0]==1:
                            S0.append("Двуручные мечи")
                        if SID[0]==2:
                            S0.remove("Двуручные мечи")
                            S0.append("Двуручные мечи 2 lvl")
                        if SID[0]==3:
                            S0.remove("Двуручные мечи 2 lvl")
                            S0.append("Двуручные мечи 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="2" or CSS=="Одноручные мечи":
                if SID[1]<4:
                    print("Навык одноручные мечи отвечает за возможность использования одноручных мечей и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[1]+=1
                        SP-=1
                        if SID[1]==1:
                            S0.append("Одноручные мечи")
                        if SID[1]==2:
                            S0.remove("Одноручные мечи")
                            S0.append("Одноручные мечи 2 lvl")
                        if SID[1]==3:
                            S0.remove("Одноручные мечи 2 lvl")
                            S0.append("Одноручные мечи 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="3" or CSS=="Двуручные булавы":
                if SID[2]<4:
                    print("Навык двуручные булавы отвечает за возможность использования двуручных булав и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[2]+=1
                        SP-=1
                        if SID[2]==1:
                            S0.append("Двуручные булавы")
                        if SID[2]==2:
                            S0.remove("Двуручные булавы")
                            S0.append("Двуручные булавы 2 lvl")
                        if SID[2]==3:
                            S0.remove("Двуручные булавы 2 lvl")
                            S0.append("Двуручные булавы 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="4" or CSS=="Одноручные булавы":
                if SID[3]<4:
                    print("Навык одноручные булавы отвечает за возможность использования одноручных булав и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[3]+=1
                        SP-=1
                        if SID[3]==1:
                            S0.append("Одноручные булавы")
                        if SID[3]==2:
                            S0.remove("Одноручные булавы")
                            S0.append("Одноручные булавы 2 lvl")
                        if SID[3]==3:
                            S0.remove("Одноручные булавы 2 lvl")
                            S0.append("Одноручные булавы 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="5" or CSS=="Двуручные топоры":
                if SID[4]<4:
                    print("Навык двуручные топоры отвечает за возможность использования двуручных топоров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[4]+=1
                        SP-=1
                        if SID[4]==1:
                            S0.append("Двуручные топоры")
                        if SID[4]==2:
                            S0.remove("Двуручные топоры")
                            S0.append("Двуручные топоры 2 lvl")
                        if SID[4]==3:
                            S0.remove("Двуручные топоры 2 lvl")
                            S0.append("Двуручные топоры 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="6" or CSS=="Одноручные топоры":
                if SID[5]<4:
                    print("Навык одноручные топоры отвечает за возможность использования одноручных топоров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[5]+=1
                        SP-=1
                        if SID[5]==1:
                            S0.append("Одноручные топоры")
                        if SID[5]==2:
                            S0.remove("Одноручные топоры")
                            S0.append("Одноручные топоры 2 lvl")
                        if SID[5]==3:
                            S0.remove("Одноручные топоры 2 lvl")
                            S0.append("Одноручные топоры 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="7" or CSS=="Боевые посохи":
                if SID[6]<4:
                    print("Навык боевые посохи отвечает за возможность использования боевых посохов и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[6]+=1
                        SP-=1
                        if SID[6]==1:
                            S0.append("Боевые посохи")
                        if SID[6]==2:
                            S0.remove("Боевые посохи")
                            S0.append("Боевые посохи 2 lvl")
                        if SID[6]==3:
                            S0.remove("Боевые посохи 2 lvl")
                            S0.append("Боевые посохи 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="8" or CSS=="Скипетры":
                if SID[7]<4:
                    print("Навык скипетры отвечает за возможность использования скипетров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[7]+=1
                        SP-=1
                        if SID[7]==1:
                            S0.append("Скипетры")
                        if SID[7]==2:
                            S0.remove("Скипетры")
                            S0.append("Скипетры 2 lvl")
                        if SID[7]==3:
                            S0.remove("Скипетры 2 lvl")
                            S0.append("Скипетры 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="9" or CSS=="Баклеры":
                if SID[8]<4:
                    print("Навык баклеры отвечает за возможность использования баклеров и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[8]+=1
                        SP-=1
                        if SID[8]==1:
                            S0.append("Баклеры")
                        if SID[8]==2:
                            S0.remove("Баклеры")
                            S0.append("Баклеры 2 lvl")
                        if SID[8]==3:
                            S0.remove("Баклеры 2 lvl")
                            S0.append("Баклеры 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="10" or CSS=="Щиты":
                if SID[9]<4:
                    print("Навык щиты отвечает за возможность использования щитов и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[9]+=1
                        SP-=1
                        if SID[9]==1:
                            S0.append("Щиты")
                        if SID[9]==2:
                            S0.remove("Щиты")
                            S0.append("Щиты 2 lvl")
                        if SID[9]==3:
                            S0.remove("Щиты 2 lvl")
                            S0.append("Щиты 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="11" or CSS=="Башенные щиты":
                if SID[10]<4:
                    print("Навык башенные щиты отвечает за возможность использования башенных щитов и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[10]+=1
                        SP-=1
                        if SID[10]==1:
                            S0.append("Башенные щиты")
                        if SID[10]==2:
                            S0.remove("Башенные щиты")
                            S0.append("Башенные щиты 2 lvl")
                        if SID[10]==3:
                            S0.remove("Башенные щиты 2 lvl")
                            S0.append("Башенные щиты 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="12" or CSS=="Лёгкая броня":
                if SID[11]<4:
                    print("Навык лёгкая броня отвечает за возможность использования лёгкой брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[11]+=1
                        SP-=1
                        if SID[11]==1:
                            S0.append("Лёгкая броня")
                        if SID[11]==2:
                            S0.remove("Лёгкая броня")
                            S0.append("Лёгкая броня 2 lvl")
                        if SID[11]==3:
                            S0.remove("Лёгкая броня 2 lvl")
                            S0.append("Лёгкая броня 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="13" or CSS=="Средняя броня":
                if SID[12]<4:
                    print("Навык средняя броня отвечает за возможность использования средней брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[12]+=1
                        SP-=1
                        if SID[12]==1:
                            S0.append("Средняя броня")
                        if SID[12]==2:
                            S0.remove("Средняя броня")
                            S0.append("Средняя броня 2 lvl")
                        if SID[12]==3:
                            S0.remove("Средняя броня 2 lvl")
                            S0.append("Средняя броня 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="14" or CSS=="Тяжёлая броня":
                if SID[13]<4:
                    print("Навык тяжёлая броня отвечает за возможность использования тяжёлой брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[13]+=1
                        SP-=1
                        if SID[13]==1:
                            S0.append("Тяжёлая броня")
                        if SID[13]==2:
                            S0.remove("Тяжёлая броня")
                            S0.append("Тяжёлая броня 2 lvl")
                        if SID[13]==3:
                            S0.remove("Тяжёлая броня 2 lvl")
                            S0.append("Тяжёлая броня 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="15" or CSS=="Магия огня":
                if SID[14]<4:
                    print("Навык магия огня отвечает за возможность использования магии огня и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[14]+=1
                        SP-=1
                        if SID[14]==1:
                            S0.append("Магия огня")
                        if SID[14]==2:
                            S0.remove("Магия огня")
                            S0.append("Магия огня 2 lvl")
                        if SID[14]==3:
                            S0.remove("Магия огня 2 lvl")
                            S0.append("Магия огня 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="16" or CSS=="Магия земли":
                if SID[15]<4:
                    print("Навык магия земли отвечает за возможность использования магии земли и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[15]+=1
                        SP-=1
                        if SID[15]==1:
                            S0.append("Магия земли")
                        if SID[15]==2:
                            S0.remove("Магия земли")
                            S0.append("Магия земли 2 lvl")
                        if SID[15]==3:
                            S0.remove("Магия земли 2 lvl")
                            S0.append("Магия земли 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="17" or CSS=="Магия воздуха":
                if SID[16]<4:
                    print("Навык магия воздуха отвечает за возможность использования магии воздуха и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[16]+=1
                        SP-=1
                        if SID[16]==1:
                            S0.append("Мания воздуха")
                        if SID[16]==2:
                            S0.remove("Мания воздуха")
                            S0.append("Мания воздуха 2 lvl")
                        if SID[16]==3:
                            S0.remove("Мания воздуха 2 lvl")
                            S0.append("Мания воздуха 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="18" or CSS=="Магия воды":
                if SID[17]<4:
                    print("Навык магия воды отвечает за возможность использования магии воды и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[17]+=1
                        SP-=1
                        if SID[17]==1:
                            S0.append("Мания воды")
                        if SID[17]==2:
                            S0.remove("Мания воды")
                            S0.append("Мания воды 2 lvl")
                        if SID[17]==3:
                            S0.remove("Мания воды 2 lvl")
                            S0.append("Мания воды 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="19" or CSS=="Магия тьмы":
                if SID[18]<4:
                    print("Навык магия тьмы отвечает за возможность использования магии тьмы и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[18]+=1
                        SP-=1
                        if SID[18]==1:
                            S0.append("Магия тьмы")
                        if SID[18]==2:
                            S0.remove("Магия тьмы")
                            S0.append("Магия тьмы 2 lvl")
                        if SID[18]==3:
                            S0.remove("Магия тьмы 2 lvl")
                            S0.append("Магия тьмы 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="20" or CSS=="Чтение свитков":
                if SID[19]<4:
                    print("Навык чтение свитков отвечает за возможность использования свитков\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[19]+=1
                        SP-=1
                        if SID[19]==1:
                            S0.append("Чтение свитков")
                        if SID[19]==2:
                            S0.remove("Чтение свитков")
                            S0.append("Чтение свитков 2 lvl")
                        if SID[19]==3:
                            S0.remove("Чтение свитков 2 lvl")
                            S0.append("Чтение свитков 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="21" or CSS=="Скрытность":
                if SID[20]<4:
                    print("Навык скрытность отвечает за возможность использования скрытности и возможности избегать битвы\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[20]+=1
                        SP-=1
                        if SID[20]==1:
                            S0.append("Скрытность")
                        if SID[20]==2:
                            S0.remove("Скрытность")
                            S0.append("Скрытность 2 lvl")
                        if SID[20]==3:
                            S0.remove("Скрытность 2 lvl")
                            S0.append("Скрытность 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="22" or CSS=="Критический удар":
                if SID[21]<4:
                    print("Навык критический удар отвечает за возможность выпадения критического удара во время атаки\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[21]+=1
                        SP-=1
                        if SID[21]==1:
                            S0.append("Критический удар")
                        if SID[21]==2:
                            S0.remove("Критический удар")
                            S0.append("Критический удар 2 lvl")
                        if SID[21]==3:
                            S0.remove("Критический удар 2 lvl")
                            S0.append("Критический удар 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="23" or CSS=="Вскрытие замков":
                if SID[22]<4:
                    print("Навык вскрытие замков отвечает за возможность вскрытия дверей и сундуков без ключей\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[22]+=1
                        SP-=1
                        if SID[22]==1:
                            S0.append("Вскрытие замков")
                        if SID[22]==2:
                            S0.remove("Вскрытие замков")
                            S0.append("Вскрытие замков 2 lvl")
                        if SID[22]==3:
                            S0.remove("Вскрытие замков 2 lvl")
                            S0.append("Вскрытие замков 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="24" or CSS=="Использование ловушек":
                if SID[23]<4:
                    print("Навык использование ловушек отвечает за возможность разминировать ловушки и устанавливать их\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[23]+=1
                        SP-=1
                        if SID[23]==1:
                            S0.append("Использование ловушек")
                        if SID[23]==2:
                            S0.remove("Использование ловушек")
                            S0.append("Использование ловушек 2 lvl")
                        if SID[23]==3:
                            S0.remove("Использование ловушек 2 lvl")
                            S0.append("Использование ловушек 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="25" or CSS=="Наблюдательность":
                if SID[24]<4:
                    print("Навык наблюдательность отвечает за возможность нахождения скрытых контейнеров и проходов\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[24]+=1
                        SP-=1
                        if SID[24]==1:
                            S0.append("Наблюдательность")
                        if SID[24]==2:
                            S0.remove("Наблюдательность")
                            S0.append("Наблюдательность 2 lvl")
                        if SID[24]==3:
                            S0.remove("Наблюдательность 2 lvl")
                            S0.append("Наблюдательность 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="26" or CSS=="Лечение":
                if SID[25]<4:
                    print("Навык лечение отвечает за количество восстановленного здоровь путём отдыха и аптечек\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[25]+=1
                        SP-=1
                        if SID[25]==1:
                            S0.append("Лечение")
                        if SID[25]==2:
                            S0.remove("Лечение")
                            S0.append("Лечение 2 lvl")
                        if SID[25]==3:
                            S0.remove("Лечение 2 lvl")
                            S0.append("Лечение 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="27" or CSS=="Парирование":
                if SID[26]<4:
                    print("Навык парирование даёт шанс польностью избежать урона если удар совпал с ударом противника\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[26]+=1
                        SP-=1
                        if SID[26]==1:
                            S0.append("Парирование")
                        if SID[26]==2:
                            S0.remove("Парирование")
                            S0.append("Парирование 2 lvl")
                        if SID[26]==3:
                            S0.remove("Парирование 2 lvl")
                            S0.append("Парирование 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="28" or CSS=="Оценка":
                if SID[27]<4:
                    print("Оценка позволяет узнать характеристики врага во время битвы\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[27]+=1
                        SP-=1
                        if SID[27]==1:
                            S0.append("Оценка")
                        if SID[27]==2:
                            S0.remove("Оценка")
                            S0.append("Оценка 2 lvl")
                        if SID[27]==3:
                            S0.remove("Оценка 2 lvl")
                            S0.append("Оценка 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="29" or CSS=="Кинжалы":
                if SID[28]<4:
                    print("Навык кинжалы отвечает за возможность использования кинжалов и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[28]+=1
                        SP-=1
                        if SID[28]==1:
                            S0.append("Кинжалы")
                        if SID[28]==2:
                            S0.remove("Кинжалы")
                            S0.append("Кинжалы 2 lvl")
                        if SID[28]==3:
                            S0.remove("Кинжалы 2 lvl")
                            S0.append("Кинжалы 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="30" or CSS=="Луки":
                if SID[29]<4:
                    print("Навык луки отвечает за возможность использования луков и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[29]+=1
                        SP-=1
                        if SID[29]==1:
                            S0.append("Луки")
                        if SID[29]==2:
                            S0.remove("Луки")
                            S0.append("Луки 2 lvl")
                        if SID[29]==3:
                            S0.remove("Луки 2 lvl")
                            S0.append("Луки 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="31" or CSS=="Дух":
                if SID[30]<4:
                    print("Навык дух отвечает за возможность использования духа\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                    print(name,": ")
                    CSS=input()
                    if CSS=="Да" or CSS=="1":
                        SID[30]+=1
                        SP-=1
                        S0.append("Дух")
                        if SID[30]==1:
                            S0.append("Дух")
                        if SID[30]==2:
                            S0.remove("Дух")
                            S0.append("Дух 2 lvl")
                        if SID[30]==3:
                            S0.remove("Дух 2 lvl")
                            S0.append("Дух 3 lvl")
                    elif CSS=="Нет" or CSS=="2":
                        continue
                    else:
                        print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            else:
                print("Выберите правильное действие")
                continue
        elif CSS=="3": #Раскачка активных способностей
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("\n|  Имя персонажа: ",name,"\n|  Название класса: ",classname,"\n|  Текущие значения: ","\n|  Очки активных способностей: ",SAP,"\n|  Способности: ",SA0)
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("Активные способности:   \nМагия огня 1)Шар стихии 2)Искра 3)Поток пламени 4)Дыхание дракона\nМагия воздуха 1)Шар стихии 5)Порез ветром 6)Сносящий поток 7)Смерч\nМагия земли 1)Шар стихии 8)Бросок камня 9)Столб земли 10)Землетрясение\nМагия воды 1)Шар стихии 11)Всплеск 12)Гейзер 13)Смертельный дождь\nМагия тьмы 1)Шар стихии 14)Сгуток тени 15)Похищение здоровья 16)Прикосновене смерти\nБаклеры 17)Тычёк щитом 18)Бросок щита\nЩиты 19)Удар щитом 20)Оглушение\nБашенные щиты 21)Таран 20)Оглушение\nМечи 22)Рассекающий порез 23)Разрубающий удар 24)Заряженный взмах\nТопоры 25)Рубитькромсать 26)Сильный удар 27)Удар с плеча\nБулавы 28)Удар с размаха 26)Сильный удар 29)Громовой удар\nКинжалы 22)Рассекающий порез 30)Проникающий удар 31)Перерезание глотки\nЛуки 32)Меткий выстрел 33)Заряженная стрела 34)Тройной выстрел\nДух 35)Прикосновение духа 36)Разрез духа 37)Удар духа")
            print(name,": ")
            CSS=input()
            if CSS=="1" or CSS=="Шар стихии": #Огонь, вода, воздух, земля
                if SAID[0]<4:
                    print("Стандартное заклинание которым овладевают все школы магии наносит урон взависимости от тех школ которыми владеет маг")
                    if SID[14]==0 and SID[15]==0 and SID[16]==0 and SID[17]==0 and SID[18]==0:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна одна из школ магии")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[0]+=1
                            SAP-=1
                            if SAID[0]==1:
                                SA0.append("Шар стихии")
                            if SAID[0]==2:
                                SA0.remove("Шар стихии")
                                SA0.append("Шар стихии 2 lvl")
                            if SAID[0]==3:
                                SA0.remove("Шар стихии 2 lvl")
                                SA0.append("Шар стихии 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="2" or CSS=="Искра": #Огонь, понижение брони
                if SAID[1]<4:
                    print("Способность которой овладевают новички школы огня которая выпускает небольшой пучок огня который наносит противнику урон огнём")
                    if SID[14]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия огня")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[1]+=1
                            SAP-=1
                            if SAID[1]==1:
                                SA0.append("Искра")
                            if SAID[1]==2:
                                SA0.remove("Искра")
                                SA0.append("Искра 2 lvl")
                            if SAID[1]==3:
                                SA0.remove("Искра 2 lvl")
                                SA0.append("Искра 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="3" or CSS=="Поток пламени": #Огонь, поджог, понижение брони
                if SAID[2]<4:
                    print("Поток пламени это способность которой обладают маги которые более углубились в изучении огненной магии. Это заклинание наносит огненный урон противнику и поджигает его")
                    if SID[14]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия огня lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[2]+=1
                            SAP-=1
                            if SAID[2]==1:
                                SA0.append("Поток пламени")
                            if SAID[2]==2:
                                SA0.remove("Поток пламени")
                                SA0.append("Поток пламени 2 lvl")
                            if SAID[2]==3:
                                SA0.remove("Поток пламени 2 lvl")
                                SA0.append("Поток пламени 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="4" or CSS=="Дыхание дракона": #Огонь, поджог, ужас, понижение брони
                if SAID[3]<4:
                    print("Дыхание драконо это то заклинание постич которое желает каждый маг который посвятил свою жизнь огненной магии. Дыхание дракона наносит противнику большой урон от огня, поджигает, а так же имеет шанс повергнуть противника в ужас")
                    if SID[14]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия огня lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[3]+=1
                            SAP-=1
                            if SAID[3]==1:
                                SA0.append("Дыхание дракона")
                            if SAID[3]==2:
                                SA0.remove("Дыхание дракона")
                                SA0.append("Дыхание дракона 2 lvl")
                            if SAID[3]==3:
                                SA0.remove("Дыхание дракона 2 lvl")
                                SA0.append("Дыхание дракона 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="5" or CSS=="Порез ветром": #Воздух, кровотечение
                if SAID[4]<4:
                    print("Порез ветром это начальное заклинание магов школы воздуха. Оно наносит урон от магии воздуха и вызывает кровотечение")
                    if SID[16]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воздуха")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[4]+=1
                            SAP-=1
                            if SAID[4]==1:
                                SA0.append("Порез ветром")
                            if SAID[4]==2:
                                SA0.remove("Порез ветром")
                                SA0.append("Порез ветром 2 lvl")
                            if SAID[4]==3:
                                SA0.remove("Порез ветром 2 lvl")
                                SA0.append("Порез ветром 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="6" or CSS=="Сносящий поток": #Воздух, обезоруживание
                if SAID[5]<4:
                    print("Заклинание среднего уровня школы воздуха, наносит противнику урон от магии воздуха и с некоторым шансом может оглушить")
                    if SID[16]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воздуха lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[5]+=1
                            SAP-=1
                            if SAID[5]==1:
                                SA0.append("Сносящий поток")
                            if SAID[5]==2:
                                SA0.remove("Сносящий поток")
                                SA0.append("Сносящий поток 2 lvl")
                            if SAID[5]==3:
                                SA0.remove("Сносящий поток 2 lvl")
                                SA0.append("Сносящий поток 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="7" or CSS=="Смерч": #Воздух, кровотечение, оглушение или обезоруживание
                if SAID[6]<4:
                    print("Смерч это сильнейшее заклинание школы воздуха оно наносит большой урон от магии воздуха, вызывает кровотечение и имеет шанс оглушить врага")
                    if SID[16]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воздуха lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[6]+=1
                            SAP-=1
                            if SAID[6]==1:
                                SA0.append("Смерч")
                            if SAID[6]==2:
                                SA0.remove("Смерч")
                                SA0.append("Смерч 2 lvl")
                            if SAID[6]==3:
                                SA0.remove("Смерч 2 lvl")
                                SA0.append("Смерч 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="8" or CSS=="Бросок камня": #Земля, оглушение
                if SAID[7]<4:
                    print("Бросок камня заклинание начального уровня наносящее урон от магии земли и с небольшим шансом оглушить")
                    if SID[15]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия земли")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[7]+=1
                            SAP-=1
                            if SAID[7]==1:
                                SA0.append("Бросок камня")
                            if SAID[7]==2:
                                SA0.remove("Бросок камня")
                                SA0.append("Бросок камня 2 lvl")
                            if SAID[7]==3:
                                SA0.remove("Бросок камня 2 lvl")
                                SA0.append("Бросок камня 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="9" or CSS=="Столб земли": #Земля, оглушение или обезоруживание
                if SAID[8]<4:
                    print("Столб земли это заклинание наносящее урон от магии земли и с высоким шансом оглушить противника")
                    if SID[15]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия земли lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[8]+=1
                            SAP-=1
                            if SAID[8]==1:
                                SA0.append("Столб земли")
                            if SAID[8]==2:
                                SA0.remove("Столб земли")
                                SA0.append("Столб земли 2 lvl")
                            if SAID[8]==3:
                                SA0.remove("Столб земли 2 lvl")
                                SA0.append("Столб земли 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="10" or CSS=="Землетрясение": #Земля за ход, оглушение за ход или обезоруживание
                if SAID[9]<4:
                    print("Высшее заклинание школы земли наносящее противнику постепенный урон от магии земли каждый ход, помимо этого есть шанс оглушить противника во время действия")
                    if SID[15]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия земли lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[9]+=1
                            SAP-=1
                            if SAID[9]==1:
                                SA0.append("Землетрясение")
                            if SAID[9]==2:
                                SA0.remove("Землетрясение")
                                SA0.append("Землетрясение 2 lvl")
                            if SAID[9]==3:
                                SA0.remove("Землетрясение 2 lvl")
                                SA0.append("Землетрясение 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="11" or CSS=="Всплеск": #Вода, -поджог, ослепление
                if SAID[10]<4:
                    print("Всплеск это заклинание начального уровня наносящее урон от магии воды, если цель горит то она будет потушена")
                    if SID[17]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воды")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[10]+=1
                            SAP-=1
                            if SAID[10]==1:
                                SA0.append("Всплеск")
                            if SAID[10]==2:
                                SA0.remove("Всплеск")
                                SA0.append("Всплеск 2 lvl")
                            if SAID[10]==3:
                                SA0.remove("Всплеск 2 lvl")
                                SA0.append("Всплеск 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="12" or CSS=="Гейзер": #Вода, подброс или обезоруживание
                if SAID[11]<4:
                    print("Гейзер это заклинание среднего уровня школы воды наносящее противнику урон от воды и с высоким шансом оглушить цель")
                    if SID[17]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воды lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[11]+=1
                            SAP-=1
                            if SAID[11]==1:
                                SA0.append("Гейзер")
                            if SAID[11]==2:
                                SA0.remove("Гейзер")
                                SA0.append("Гейзер 2 lvl")
                            if SAID[11]==3:
                                SA0.remove("Гейзер 2 lvl")
                                SA0.append("Гейзер 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="13" or CSS=="Смертельный дождь": #Вода за ход, кровотечение, понижение брони
                if SAID[12]<4:
                    print("Смертельный дождь это высшее заклинание школы воды наносящее высокий урон противнику от воды в течении нескольких ходов и вызывающее кровотечение")
                    if SID[17]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия воды lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[12]+=1
                            SAP-=1
                            if SAID[12]==1:
                                SA0.append("Смертельный дождь")
                            if SAID[12]==2:
                                SA0.remove("Смертельный дождь")
                                SA0.append("Смертельный дождь 2 lvl")
                            if SAID[12]==3:
                                SA0.remove("Смертельный дождь 2 lvl")
                                SA0.append("Смертельный дождь 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="14" or CSS=="Сгусток тени": #Тьма, ослепление
                if SAID[13]<4:
                    print("Сгусток тени это заклинание начального уровня наносящее урон от тьмы противнику")
                    if SID[18]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия тьмы")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[13]+=1
                            SAP-=1
                            if SAID[13]==1:
                                SA0.append("Сгусток тени")
                            if SAID[13]==2:
                                SA0.remove("Сгусток тени")
                                SA0.append("Сгусток тени 2 lvl")
                            if SAID[13]==3:
                                SA0.remove("Сгусток тени 2 lvl")
                                SA0.append("Сгусток тени 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="15" or CSS=="Похищение здоровья": #Тьма, вампиризм
                if SAID[14]<4:
                    print("Похищение здоровья заклинание наносящее противнику урон от тёмной магии и если цель является живой восстанавливает здоровье")
                    if SID[18]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия тьмы lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[14]+=1
                            SAP-=1
                            if SAID[14]==1:
                                SA0.append("Похищение здоровья")
                            if SAID[14]==2:
                                SA0.remove("Похищение здоровья")
                                SA0.append("Похищение здоровья 2 lvl")
                            if SAID[14]==3:
                                SA0.remove("Похищение здоровья 2 lvl")
                                SA0.append("Похищение здоровья 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="16" or CSS=="Прикосновение смерти": #Тьма, увеличение урона
                if SAID[15]<4:
                    print("Прикосновение смерти высшее заклинание тёмной магии наносит высокий урон противнику от тёмной маии и если цель умерла урон от заклинания увеличивается (не действует на механойдов и нежить)")
                    if SID[18]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна магия тьмы lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[15]+=1
                            SAP-=1
                            if SAID[15]==1:
                                SA0.append("Прикосновение смерти")
                            if SAID[15]==2:
                                SA0.remove("Прикосновение смерти")
                                SA0.append("Прикосновение смерти 2 lvl")
                            if SAID[15]==3:
                                SA0.remove("Прикосновение смерти 2 lvl")
                                SA0.append("Прикосновение смерти 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="17" or CSS=="Тычёк щитом": #Физический, оглушить или молчание
                if SAID[16]<4:
                    print("Способность тычёк щитом наносит урон противнику и с малой вероятностью может оглушить")
                    if SID[8]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна баклеры")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[16]+=1
                            SAP-=1
                            if SAID[16]==1:
                                SA0.append("Тычёк щитом")
                            if SAID[16]==2:
                                SA0.remove("Тычёк щитом")
                                SA0.append("Тычёк щитом 2 lvl")
                            if SAID[16]==3:
                                SA0.remove("Тычёк щитом 2 lvl")
                                SA0.append("Тычёк щитом 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="18" or CSS=="Бросок щита": #Физический, обезоруживание
                if SAID[17]<4:
                    print("Бросок щита наносит противнику физический урон")
                    if SID[8]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна баклеры lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[17]+=1
                            SAP-=1
                            if SAID[17]==1:
                                SA0.append("Бросок щита")
                            if SAID[17]==2:
                                SA0.remove("Бросок щита")
                                SA0.append("Бросок щита 2 lvl")
                            if SAID[17]==3:
                                SA0.remove("Бросок щита 2 lvl")
                                SA0.append("Бросок щита 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="19" or CSS=="Удар щитом": #Физический, оглушить или молчание или обезоруживание
                if SAID[18]<4:
                    print("Удар щитом наносит урон противнику с небольшой вероятностью оглушить")
                    if SID[9]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна щиты")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[18]+=1
                            SAP-=1
                            if SAID[18]==1:
                                SA0.append("Удар щитом")
                            if SAID[18]==2:
                                SA0.remove("Удар щитом")
                                SA0.append("Удар щитом 2 lvl")
                            if SAID[18]==3:
                                SA0.remove("Удар щитом 2 lvl")
                                SA0.append("Удар щитом 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="20" or CSS=="Оглушение": #Физический, оглушить
                if SAID[19]<4:
                    print("Наносит противнику урон и с большой вероятностью может оглушить цель")
                    if SID[9]<2 and SID[10]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна ,башенные щиты lvl 2 или щиты lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[19]+=1
                            SAP-=1
                            if SAID[19]==1:
                                SA0.append("Оглушение")
                            if SAID[19]==2:
                                SA0.remove("Оглушение")
                                SA0.append("Оглушение 2 lvl")
                            if SAID[19]==3:
                                SA0.remove("Оглушение 2 lvl")
                                SA0.append("Оглушение 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="21" or CSS=="Таран": #Физический, оглушить
                if SAID[20]<4:
                    print("Таран наносит удар на ходу по противнику оглушая его")
                    if SID[10]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужна башенные щиты")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[20]+=1
                            SAP-=1
                            if SAID[20]==1:
                                SA0.append("Таран")
                            if SAID[20]==2:
                                SA0.remove("Таран")
                                SA0.append("Таран 2 lvl")
                            if SAID[20]==3:
                                SA0.remove("Таран 2 lvl")
                                SA0.append("Таран 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="22" or CSS=="Рассекающий порез": #Физический, кровотечение
                if SAID[21]<4:
                    print("Наносит противнику удар который наносит физический урон, помимо этого у противника открывается кровотечение")
                    if SID[0]<1 and SID[28]<1 and SID[1]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны кинжалы, одноручные или двуручные мечи")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[21]+=1
                            SAP-=1
                            if SAID[21]==1:
                                SA0.append("Рассекающий порез")
                            if SAID[21]==2:
                                SA0.remove("Рассекающий порез")
                                SA0.append("Рассекающий порез 2 lvl")
                            if SAID[21]==3:
                                SA0.remove("Рассекающий порез 2 lvl")
                                SA0.append("Рассекающий порез 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="23" or CSS=="Разрубающий удар": #Физический, кровотечение
                if SAID[22]<4:
                    print("Разрубающий удар наносит противнику высокий урон и открывает кровотечение")
                    if SID[0]<2 and SID[1]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные мечи lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[22]+=1
                            SAP-=1
                            if SAID[22]==1:
                                SA0.append("Разрубающий удар")
                            if SAID[22]==2:
                                SA0.remove("Разрубающий удар")
                                SA0.append("Разрубающий удар 2 lvl")
                            if SAID[22]==3:
                                SA0.remove("Разрубающий удар 2 lvl")
                                SA0.append("Разрубающий удар 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="24" or CSS=="Заряженный взмах": #Физический, огонь, вода, воздух, земля
                if SAID[23]<4:
                    print("Наносит противнику физический урон, а так же урон от 4 стихий сверху")
                    if SID[0]<3 and SID[1]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные мечи lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[23]+=1
                            SAP-=1
                            if SAID[23]==1:
                                SA0.append("Заряженный взмах")
                            if SAID[23]==2:
                                SA0.remove("Заряженный взмах")
                                SA0.append("Заряженный взмах 2 lvl")
                            if SAID[23]==3:
                                SA0.remove("Заряженный взмах 2 lvl")
                                SA0.append("Заряженный взмах 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="25" or CSS=="Рубитькромсать": #Физический, кровотечение
                if SAID[24]<4:
                    print("Наносит противнику большой урон и есть возможноть кровотечение")
                    if SID[4]<1 and SID[5]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные топоры")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[24]+=1
                            SAP-=1
                            if SAID[24]==1:
                                SA0.append("Рубитькромсать")
                            if SAID[24]==2:
                                SA0.remove("Рубитькромсать")
                                SA0.append("Рубитькромсать 2 lvl")
                            if SAID[24]==3:
                                SA0.remove("Рубитькромсать 2 lvl")
                                SA0.append("Рубитькромсать 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="26" or CSS=="Сильный удар": #Физический, оглушение
                if SAID[25]<4:
                    print("Сильный удар наносит противнику урон и имеет шанс оглушать цель")
                    if SID[4]<2 and SID[5]<2 and SID[2]<2 and SID[3]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные топоры, а так же булавы lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[25]+=1
                            SAP-=1
                            if SAID[25]==1:
                                SA0.append("Сильный удар")
                            if SAID[25]==2:
                                SA0.remove("Сильный удар")
                                SA0.append("Сильный удар 2 lvl")
                            if SAID[25]==3:
                                SA0.remove("Сильный удар 2 lvl")
                                SA0.append("Сильный удар 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="27" or CSS=="Удар с плеча": #Физический, сильное кровотечение
                if SAID[26]<4:
                    print("Наносит противнику рубаящий удар и вызывает сильное кровотечение")
                    if SID[4]<3 and SID[5]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные топоры lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[26]+=1
                            SAP-=1
                            if SAID[26]==1:
                                SA0.append("Удар с плеча")
                            if SAID[26]==2:
                                SA0.remove("Удар с плеча")
                                SA0.append("Удар с плеча 2 lvl")
                            if SAID[26]==3:
                                SA0.remove("Удар с плеча 2 lvl")
                                SA0.append("Удар с плеча 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="28" or CSS=="Удар с размаха": #Физический, оглушение
                if SAID[27]<4:
                    print("Удар с размаха наносит противнику урон и с большой вероятностью оглушает цель")
                    if SID[2]<1 and SID[3]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные булавы")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[27]+=1
                            SAP-=1
                            if SAID[27]==1:
                                SA0.append("Удар с размаха")
                            if SAID[27]==2:
                                SA0.remove("Удар с размаха")
                                SA0.append("Удар с размаха 2 lvl")
                            if SAID[27]==3:
                                SA0.remove("Удар с размаха 2 lvl")
                                SA0.append("Удар с размаха 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="29" or CSS=="Громовой удар": #Физический, огонь, вода, воздух, земля, оглушение
                if SAID[28]<4:
                    print("Громовой удар наносит противнику физический урон, урон от стихий и с большой вероятностью оглушает цель")
                    if SID[2]<3 and SID[3]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны одноручные или двуручные булавы lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[28]+=1
                            SAP-=1
                            if SAID[28]==1:
                                SA0.append("Громовой удар")
                            if SAID[28]==2:
                                SA0.remove("Громовой удар")
                                SA0.append("Громовой удар 2 lvl")
                            if SAID[28]==3:
                                SA0.remove("Громовой удар 2 lvl")
                                SA0.append("Громовой удар 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="30" or CSS=="Проникающий удар": #Физический урон игнорируя броню
                if SAID[29]<4:
                    print("Проникающий удар наносит урон противнику игнорируя его броню")
                    if SID[28]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны кинжалы lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[29]+=1
                            SAP-=1
                            if SAID[29]==1:
                                SA0.append("Проникающий удар")
                            if SAID[29]==2:
                                SA0.remove("Проникающий удар")
                                SA0.append("Проникающий удар 2 lvl")
                            if SAID[29]==3:
                                SA0.remove("Проникающий удар 2 lvl")
                                SA0.append("Проникающий удар 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="31" or CSS=="Перерезание глотки": #Физический урон игнорируя броню, кровотечение, молчание
                if SAID[30]<4:
                    print("Перерезание глотки наносит физический урон цели игнорируя броню противника и наносит урон от кровотечения")
                    if SID[28]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны кинжалы lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[30]+=1
                            SAP-=1
                            SA0.append("Перерезание глотки")
                            if SAID[30]==1:
                                SA0.append("Перерезание глотки")
                            if SAID[30]==2:
                                SA0.remove("Перерезание глотки")
                                SA0.append("Перерезание глотки 2 lvl")
                            if SAID[30]==3:
                                SA0.remove("Перерезание глотки 2 lvl")
                                SA0.append("Перерезание глотки 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="32" or CSS=="Меткий выстрел": #Физический урон игнорируя броню, ослепление
                if SAID[31]<4:
                    print("Меткий выстрел наносит противнику урон игнорируя броню противника")
                    if SID[29]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны луки")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[31]+=1
                            SAP-=1
                            SA0.append("Меткий выстрел")
                            if SAID[31]==1:
                                SA0.append("Меткий выстрел")
                            if SAID[31]==2:
                                SA0.remove("Меткий выстрел")
                                SA0.append("Меткий выстрел 2 lvl")
                            if SAID[31]==3:
                                SA0.remove("Меткий выстрел 2 lvl")
                                SA0.append("Меткий выстрел 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="33" or CSS=="Заряженная стрела": #Физический, огонь, вода, воздух, земля
                if SAID[32]<4:
                    print("Заряженная стрела наносит физический урон а так же урон от стихий")
                    if SID[29]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны луки lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[32]+=1
                            SAP-=1
                            if SAID[32]==1:
                                SA0.append("Заряженная стрела")
                            if SAID[32]==2:
                                SA0.remove("Заряженная стрела")
                                SA0.append("Заряженная стрела 2 lvl")
                            if SAID[32]==3:
                                SA0.remove("Заряженная стрела 2 lvl")
                                SA0.append("Заряженная стрела 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="34" or CSS=="Тройной выстрел": #Физический х3
                if SAID[33]<4:
                    print("Тройной выстрел наносит урон сразу в 3 точки противника")
                    if SID[29]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны луки lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[33]+=1
                            SAP-=1
                            if SAID[33]==1:
                                SA0.append("Тройной выстрел")
                            if SAID[33]==2:
                                SA0.remove("Тройной выстрел")
                                SA0.append("Тройной выстрел 2 lvl")
                            if SAID[33]==3:
                                SA0.remove("Тройной выстрел 2 lvl")
                                SA0.append("Тройной выстрел 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="35" or CSS=="Прикосновение духа": #Чистый урон
                if SAID[34]<4:
                    print("Прикосновение духа наносит противнику чистый урон который не блокируется броней")
                    if SID[30]<1:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны дух")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[34]+=1
                            SAP-=1
                            if SAID[34]==1:
                                SA0.append("Прикосновение духа")
                            if SAID[34]==2:
                                SA0.remove("Прикосновение духа")
                                SA0.append("Прикосновение духа 2 lvl")
                            if SAID[34]==3:
                                SA0.remove("Прикосновение духа 2 lvl")
                                SA0.append("Прикосновение духа 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="36" or CSS=="Разрез духа": #Чистый урон, кровотечение
                if SAID[35]<4:
                    print("Разрез духа наносит чистый урон противнику и открывает кровотечение")
                    if SID[30]<2:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны дух lvl 2")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[35]+=1
                            SAP-=1
                            SA0.append("Разрез духа")
                            if SAID[35]==1:
                                SA0.append("Разрез духа")
                            if SAID[35]==2:
                                SA0.remove("Разрез духа")
                                SA0.append("Разрез духа 2 lvl")
                            if SAID[35]==3:
                                SA0.remove("Разрез духа 2 lvl")
                                SA0.append("Разрез духа 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            elif CSS=="37" or CSS=="Удар духа": #Чистый урон, оглушение
                if SAID[36]<4:
                    print("Наносит противнику чистый урон а так же имеет средний шанс оглушить")
                    if SID[30]<3:
                        print("Вы не можете выбрать эту способность. Для неё вам нужны дух lvl 3")
                    else:
                        print("Желаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SAID[36]+=1
                            SAP-=1
                            SA0.append("Удар духа")
                            if SAID[36]==1:
                                SA0.append("Удар духа")
                            if SAID[36]==2:
                                SA0.remove("Удар духа")
                                SA0.append("Удар духа 2 lvl")
                            if SAID[36]==3:
                                SA0.remove("Удар духа 2 lvl")
                                SA0.append("Удар духа 3 lvl")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Выберите правильное действие")
                else:
                    print("Уровень способности максимальный")
            else:
                print("Выберите правильное действие")
                continue
            continue
        elif CSS=="4": #О персонаже
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|Имя персонажа: ",name,"\n|Название класса: ",classname,"\n|Ваш уровень: ",lvl,"\n|Опыт: ",exp,"/",expup,"\n|---------------","\n|Текущие значения: ","\n|Сила(Свои/предметы)",FS," (",S,"/",AS[0],")","\n|Ловкость(Свои/предметы)",FA," (",A,"/",AA[0],")","\n|Мудрость(Свои/предметы)",FM," (",M,"/",AM[0],")","\n|Здоровье(Свои/предметы)",FH," (",H,"/",AH[0],")","\n|---------------","\n|Способности: ",S0,"\n|Активные способности: ",SA0,"\n|---------------","\n|Очки здоровья: ",HP,"/",FHP,"\n|Очки маны/духа: ",MP,"/",FMP)
            if weapon=="power":
                print("|Урон(Свой/предметы): ",urons," (",S*2,"/",AS[0]*2+atk,")")
            elif weapon=="agility":
                print("|Урон(Свой/предметы): ",urona," (",A*2,"/",AA[0]*2+atk,")")
            elif weapon=="magic":
                print("|Урон(Свой/предметы): ",urona," (",M*2,"/",AM[0]*2+atk,")")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            input("Нажмите enter для дальнейших действий")
            continue
        elif CSS=="5":
            break
def save():
    print("Выберите ячейку для сохранения:")
    print("1)",save1)
    print("2)",save2)
    print("3)",save3)
    CSS=input()
    if CSS==1:
        Save1P=P;Save1SP=SP;Save1SAP=SAP;Save1S=S;Save1M=M;Save1A=A;Save1H=H;Save1E=E;Save1lvl=lvl;Save1exp=exp;Save1safy=safy;Save1atk=atk;Save1AS=AS[0];Save1AA=AA[0];Save1AM=AM[0];Save1AH=AH[0];Save1classname=classname;Save1AS1=AS[1];Save1AS2=AS[2];Save1AS3=AS[3];Save1AS4=AS[4];Save1AS5=AS[5];Save1AS6=AS[6];Save1AA1=AA[1];Save1AA2=AA[2];Save1AA3=AA[3];Save1AA4=AA[4];Save1AA5=AA[5];Save1AA6=AA[6];Save1AH1=Ah1;Save1AH2=AH[2];Save1AH3=AH[3];Save1AH4=AH[4];Save1AH5=AH[5];Save1AH6=AH[6];Save1AM1=AM[1];Save1AM2=AM[2];Save1AM3=AM[3];Save1AM4=AM[4];Save1AM5=AM[5];Save1AM6=AM[6];Save1S0=S0;
print("Неизвестный: Приветствую тебя мой новый друг. Не мог бы ты назвать мне своё имя?" )
print(name,": ");name=input()
#Прокачка персонажа
while True: #Пролог
    if E==0:
        print(" ---------------","\nИмя персонажа: ",name,"\nНазвание класса: ",classname,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H,"\nОставшееся количество очков: ",P,"\nОчки способности: ",SP,"\nСпособности: ",S0,"\n","---------------")
        print('Скажи мне что ты хочешь чтобы я сделал с тобой? А может ты позволишь мне решить выбрав \n1)Повысить\n2)Вернуть\n3)Шаблон')
        print(name,": ")
        USE=input()
        if USE=="Повысить" or USE=="1": #Повышение
            classname="Свой"
            print("Неизвестный: В чём именно ты желаешь стать лучше? \n1)Стать сильнее\n2)Стать ловче\n3)Стать мудрее\n4)Стать выносливее")
            print(name,":")
            CSS=input()
            if CSS == "Сила" or CSS == "Ловкость" or CSS == "Мудрость" or CSS == "Здоровье" or CSS=="1" or CSS=="2" or CSS=="3" or CSS=="4":
                print("Неизвестный: Какое количество очков ты желаешь вложить?")
                print(name,": ")
                CSS2=int(input())
                if CSS2>P:
                    print("Неизвестный: Это не возможно")
                else:
                    if CSS=="Сила" or CSS=="1": 
                        S+=CSS2
                        P-=CSS2
                        if P==0:
                            E+=1
                    elif CSS=="Ловкость" or CSS=="2":
                        A+=CSS2
                        P-=CSS2
                        if P==0:
                            E+=1
                    elif CSS=="Мудрость" or CSS=="3":
                        M+=CSS2
                        P-=CSS2
                        if P==0:
                            E+=1
                    elif CSS=="Здоровье" or CSS=="4":
                        H+=CSS2
                        P-=CSS2
                        if P==0:
                            E+=1
            else:
                print("Неизвестный: Такой характеристики нету")
        elif USE=="Вернуть" or USE=="2": #Возвращение
            classname="Свой"
            print("Неизвестный: Что именно тебе не нравится в себе? \n1)Вернуть сильну\n2)Вернуть ловкость\n3)Вернуть мудрость\n4)Вернуть выносливость")
            print(name,":")
            CSS=input()
            if CSS == "Сила" or CSS == "Ловкость" or CSS == "Мудрость" or CSS == "Здоровье" or CSS=="1" or CSS=="2" or CSS=="3" or CSS=="4":
                print("Неизвестный: Какое количество очков ты желаешь вернуть?")
                print(name,": ",)
                CSS2=int(input())
                if CSS=="Сила" or CSS=="1": 
                    if CSS2>S:
                        print("Неизвестный: Это не возможно")
                    else:
                        S-=CSS2
                        P+=CSS2
                elif CSS=="Ловкость" or CSS=="2":
                    if CSS2>A:
                        print("Неизвестный: Это не возможно")
                    else:
                        A-=CSS2
                        P+=CSS2
                elif CSS=="Мудрость" or CSS=="3":
                    if CSS2>M:
                        print("Неизвестный: Это не возможно")
                    else:
                        M-=CSS2
                        P+=CSS2
                elif CSS=="Здоровье" or CSS=="4":
                    if CSS2>H:
                        print("Неизвестный: Это не возможно")
                    else:
                        H-=CSS2
                        P+=CSS2
        elif USE=="Шаблон" or USE=="3": #Шаблон
            print("Какой класс ты желаешь выбрать?\nСила: 01)Варвар, 02)Воин, 03)Паладин\nЛовкость: 11)Вор, 12)Убийца, 13)Стрелок\nМудрость: 21)Маг, 22)Монах, 23)Боевой Маг")
            print(name,": ")
            CLS=input()
            if CLS=="Варвар" or CLS=="01": #Варвар
                print("Варвары это северный народ. Их сила и выносливость порой заставляют трепетать. Правда непонятно трепет это от воодушивления или от страха.")
                print("Характеристики: \nСила: 15\nЛовкость: 5\nМудрость:3\nЗдоровье: 7")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Варвар"
                    S=15
                    A=5
                    M=3
                    H=7
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=1;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=1;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=1;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                    S0.clear()
                    S0.append("Двуручные топоры")
                    S0.append("Средняя броня")
                    S0.append("Критический удар")
                    weapon="power"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Воин" or CLS=="02": #Воин
                print("Воины это бравые солдаты наполняющие все окружающие нас земли. Много кого можно назвать войном однако истинные из них обладают невероятным умением управлятся с мечом и щитом.")
                print("Характеристики: \nСила: 11\nЛовкость: 8\nМудрость:4\nЗдоровье: 7")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Воин"
                    S=11
                    A=8
                    M=4
                    H=7
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=1;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=1;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=1;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                    S0.clear()
                    S0.append("Одноручные мечи")
                    S0.append("Тяжёлая броня")
                    S0.append("Щиты")
                    weapon="power"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Паладин" or CLS=="03": #Паладин
                print("Паладины это воины защитники из крепости Хеймволл. Они их обучали сражению против магических существ поэтому на их крепкость духа и выдержку можно положиться.")
                print("Характеристики: \nСила: 11\nЛовкость: 4\nМудрость:4\nЗдоровье: 11")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Паладин"
                    S=11
                    A=4
                    M=4
                    H=11
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=1;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=1;SID[11]=0;SID[12]=0;SID[13]=1;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                    S0.clear()
                    S0.append("Тяжёлая броня")
                    S0.append("Одноручные булавы")
                    S0.append("Башенные щиты")
                    weapon="power"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Вор" or CLS=="11": #Вор
                print("Воры это та прожилка общества которая способна проникнуть куда угадно и когда угодно, хотя и неплохо управляется с ножами.")
                print("Характеристики: \nСила: 8\nЛовкость: 11\nМудрость:5\nЗдоровье: 6")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Вор"
                    S=8
                    A=11
                    M=5
                    H=6
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=1;SID[21]=0;SID[22]=1;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=1;SID[29]=0;SID[30]=0
                    S0.clear()
                    S0.append("Кинжалы")
                    S0.append("Вскрытие замков")
                    S0.append("Скрытность")
                    weapon="agility"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Убийца" or CLS=="12": #Убийца
                print("Специально обученные подразделения Тёмной руки никогда не оставляют свою жертву в живых. Специализируются на тайных операциях.")
                print("Характеристики: \nСила: 9\nЛовкость: 13\nМудрость:3\nЗдоровье: 5")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Убийца"
                    S=9
                    A=13
                    M=3
                    H=5
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=1;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=1;SID[27]=0;SID[28]=1;SID[29]=0;SID[30]=0
                    S0.clear()
                    S0.append("Критический удар")
                    S0.append("Кинжалы")
                    S0.append("Парирование")
                    weapon="agility"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Стрелок" or CLS=="13": #Стрелок
                print("Стрелки это специальные королевские войска которые обучены нести дозор за областью находящейся в месте несения их службы.")
                print("Характеристики: \nСила: 7\nЛовкость: 13\nМудрость:5\nЗдоровье: 5")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Стрелок"
                    S=7
                    A=13
                    M=5
                    H=5
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=1;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=1;SID[28]=0;SID[29]=1;SID[30]=0
                    S0.clear()
                    S0.append("Луки")
                    S0.append("Критический удар")
                    S0.append("Оценка")
                    weapon="agility"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Маг" or CLS=="21": #Маг
                print("Маги это люди рождённые и открывшие в себе Дар. Это магическая энергия неизвестного происхождения но нашедшая достойное прменение в обществе. Маги годами обучаются в одной из четырёх школ: Игнитус, Аквасис, Террамус или Аэркус.")
                print("Характеристики: \nСила: 4\nЛовкость: 4\nМудрость:15\nЗдоровье: 7")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    print("Неизвестный: Какую школу магии ты предпочитаешь?\n1)Игнитус\n2)Аквасис\n3)Террамус\n4)Аэркус")
                    mag=input()
                    if mag=="1" or mag=="Игнитус":      
                        classname="Маг огня"
                        S=4
                        A=4
                        M=15
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=1;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=1;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=1;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Чтение свитков")
                        S0.append("Скипетры")
                        S0.append("Магия огня")
                        weapon="magic"
                    elif mag=="2" or mag=="Аквасис":      
                        classname="Маг воды"
                        S=4
                        A=4
                        M=15
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=1;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=1;SID[18]=0;SID[19]=1;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Чтение свитков")
                        S0.append("Скипетры")
                        S0.append("Магия воды")
                        weapon="magic"
                    elif mag=="3" or mag=="Террамус":      
                        classname="Маг земли"
                        S=4
                        A=4
                        M=15
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=1;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=1;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=1;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Чтение свитков")
                        S0.append("Скипетры")
                        S0.append("Магия земли")
                        weapon="magic"
                    elif mag=="4" or mag=="Аэркус":    
                        classname="Маг воздуха"
                        S=4
                        A=4
                        M=15
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=1;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=1;SID[17]=0;SID[18]=0;SID[19]=1;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Чтение свитков")
                        S0.append("Скипетры")
                        S0.append("Магия воздуха")
                        weapon="magic"
                    else:
                        print("Неизвестный: Я не понял твоего ответа")
                        continue
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Монах" or CLS=="22": #Монах
                print("Монахи после длительного обучения спускаются к нам с монастырей расположеных в местах где когда то давно обитали существа обладающие большой магической энергией. Монахи не обладают Даром они используют дух и мантры, а также боевые искуства для ведения боя.")
                print("Характеристики: \nСила: 4\nЛовкость: 9\nМудрость:10\nЗдоровье: 7")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    classname="Монах"
                    S=5
                    A=9
                    M=10
                    H=7
                    P=0
                    E+=1
                    SP=0
                    SID[0]=0;SID[1]=0;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=1;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=0;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=1;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=1
                    S0.clear()
                    S0.append("Боевые посохи")
                    S0.append("Чтение свитков")
                    S0.append("Дух")
                    weapon="magic"
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            elif CLS=="Боевой маг" or CLS=="23": #Боевой маг
                print("Боевые маги это особые подразделения которые являются обладателями Дара, но кроме чтения книг они были обучены превосходному владению мечом.")
                print("Характеристики: \nСила: 10\nЛовкость: 4\nМудрость:9\nЗдоровье: 7")
                print("Неизвестный: желаешь ли ты выбрать этот класс? 1)Да/2)Нет")
                print(name,': ')
                CSS=input()
                if CSS=="Да" or CSS=="1":
                    print("Неизвестный: Какую школу магии ты предпочитаешь?\n1)Игнитус\n2)Аквасис\n3)Террамус\n4)Аэркус")
                    mag=input()
                    if mag=="1" or mag=="Игнитус":      
                        classname="Боевой маг огня"
                        S=10
                        A=4
                        M=9
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=1;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=1;SID[13]=0;SID[14]=1;SID[15]=0;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Средняя броня")
                        S0.append("Одноручные мечи")
                        S0.append("Магия огня")
                        weapon="magic"
                    elif mag=="2" or mag=="Аквасис":      
                        classname="Боевой маг воды"
                        S=10
                        A=4
                        M=9
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=1;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=1;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=0;SID[17]=1;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Средняя броня")
                        S0.append("Одноручные мечи")
                        S0.append("Магия воды")
                        weapon="magic"
                    elif mag=="3" or mag=="Террамус":      
                        classname="Боевой маг земли"
                        S=10
                        A=4
                        M=9
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=1;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=1;SID[13]=0;SID[14]=0;SID[15]=1;SID[16]=0;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Средняя броня")
                        S0.append("Одноручные мечи")
                        S0.append("Магия земли")
                        weapon="magic"
                    elif mag=="4" or mag=="Аэркус":    
                        classname="Боевой маг воздуха"
                        S=10
                        A=4
                        M=9
                        H=7
                        P=0
                        E+=1
                        SP=0
                        SID[0]=0;SID[1]=1;SID[2]=0;SID[3]=0;SID[4]=0;SID[5]=0;SID[6]=0;SID[7]=0;SID[8]=0;SID[9]=0;SID[10]=0;SID[11]=0;SID[12]=1;SID[13]=0;SID[14]=0;SID[15]=0;SID[16]=1;SID[17]=0;SID[18]=0;SID[19]=0;SID[20]=0;SID[21]=0;SID[22]=0;SID[23]=0;SID[24]=0;SID[25]=0;SID[26]=0;SID[27]=0;SID[28]=0;SID[29]=0;SID[30]=0
                        S0.clear()
                        S0.append("Средняя броня")
                        S0.append("Одноручные мечи")
                        S0.append("Магия воздуха")
                        weapon="magic"
                    else:
                        print("Неизвестный: Я не понял твоего ответа")
                        continue
                elif CSS=="Нет" or CSS=="2":
                    continue
                else:
                    print("Неизвестный: Я не понял твоего ответа")
                    continue
            else:
                print("Неизвестный: Такой характеристики нету")
        else:
            print("Неизвестный: Я тебя не понял")
    elif classname=="Свой" and E==1: #Если класс не выбран то способности выбираются вручную
        if SP==0:
            E+=1
            continue
        else:
            print("Теперь мы распределим очки способностей вы можете\n1)Выбрать\n2)Убрать")
            print(name, ": ")
            CSS=input()
            if CSS=="1" or CSS=="Выбрать":
                print(" ---------------","\nИмя персонажа: ",name,"\nНазвание класса: ",classname,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H,"\nОставшееся количество очков: ",P,"\nОчки способности:",SP,"\nСпособности: ",S0,"\n","---------------")
                print("Неизвестный: Какими способностями ты хочешь обладать",name,"?")
                print("Экипировка:\n1)Двуручные мечи  2)Одноручные мечи\n3)Двуручные булавы  4)Одноручные булавы\n5)Двуручные топоры  6)Одноручные топоры\n7)Боевые посохи  8)Скипетры\n9)Баклеры       10)Щиты\n11)Башенные щиты  12)Лёгкая броня\n13)Средняя броня  14)Тяжёлая броня\nМагия:\n15)Магия огня  16)Магия земли\n17)Магия воздуха  18)Магия воды\n19)Магия тьмы\nВспомогательные:\n20)Чтение свитков  21)Скрытность\n22)Критический удар  23)Вскрытие замков\n24)Использование ловушек  25)Наблюдательность\n26)Лечение  27)Парирование\n28)Оценка  29)Кинжалы\n30)Луки  31)Дух")
                print(name,": ")
                CSS=input()
                if CSS=="1" or CSS=="Двуручные мечи":
                    if SID[0]==0:
                        print("Навык двуручные мечи отвечает за возможность использования двуручных мечей и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[0]+=1
                            SP-=1
                            S0.append("Двуручные мечи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="2" or CSS=="Одноручные мечи":
                    if SID[1]==0:
                        print("Навык одноручные мечи отвечает за возможность использования одноручных мечей и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[1]+=1
                            SP-=1
                            S0.append("Одноручные мечи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="3" or CSS=="Двуручные булавы":
                    if SID[2]==0:
                        print("Навык двуручные булавы отвечает за возможность использования двуручных булав и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[2]+=1
                            SP-=1
                            S0.append("Двуручные булавы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="4" or CSS=="Одноручные булавы":
                    if SID[3]==0:
                        print("Навык одноручные булавы отвечает за возможность использования одноручных булав и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[3]+=1
                            SP-=1
                            S0.append("Одноручные булавы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="5" or CSS=="Двуручные топоры":
                    if SID[4]==0:
                        print("Навык двуручные топоры отвечает за возможность использования двуручных топоров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[4]+=1
                            SP-=1
                            S0.append("Двуручные топоры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="6" or CSS=="Одноручные топоры":
                    if SID[5]==0:
                        print("Навык одноручные топоры отвечает за возможность использования одноручных топоров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[5]+=1
                            SP-=1
                            S0.append("Одноручные топоры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="7" or CSS=="Боевые посохи":
                    if SID[6]==0:
                        print("Навык боевые посохи отвечает за возможность использования боевых посохов и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[6]+=1
                            SP-=1
                            S0.append("Боевые посохи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="8" or CSS=="Скипетры":
                    if SID[7]==0:
                        print("Навык скипетры отвечает за возможность использования скипетров и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[7]+=1
                            SP-=1
                            S0.append("Скипетры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="9" or CSS=="Баклеры":
                    if SID[8]==0:
                        print("Навык баклеры отвечает за возможность использования баклеров и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[8]+=1
                            SP-=1
                            S0.append("Баклеры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="10" or CSS=="Щиты":
                    if SID[9]==0:
                        print("Навык щиты отвечает за возможность использования щитов и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[9]+=1
                            SP-=1
                            S0.append("Щиты")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="11" or CSS=="Башенные щиты":
                    if SID[10]==0:
                        print("Навык башенные щиты отвечает за возможность использования башенных щитов и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[10]+=1
                            SP-=1
                            S0.append("Башенные щиты")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="12" or CSS=="Лёгкая броня":
                    if SID[11]==0:
                        print("Навык лёгкая броня отвечает за возможность использования лёгкой брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[11]+=1
                            SP-=1
                            S0.append("Лёгкая броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="13" or CSS=="Средняя броня":
                    if SID[12]==0:
                        print("Навык средняя броня отвечает за возможность использования средней брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[12]+=1
                            SP-=1
                            S0.append("Средняя броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="14" or CSS=="Тяжёлая броня":
                    if SID[13]==0:
                        print("Навык тяжёлая броня отвечает за возможность использования тяжёлой брони и урон который они блокируют\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[13]+=1
                            SP-=1
                            S0.append("Тяжёлая броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="15" or CSS=="Магия огня":
                    if SID[14]==0:
                        print("Навык магия огня отвечает за возможность использования магии огня и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[14]+=1
                            SP-=1
                            S0.append("Магия огня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="16" or CSS=="Магия земли":
                    if SID[15]==0:
                        print("Навык магия земли отвечает за возможность использования магии земли и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[15]+=1
                            SP-=1
                            S0.append("Магия земли")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="17" or CSS=="Магия воздуха":
                    if SID[16]==0:
                        print("Навык магия воздуха отвечает за возможность использования магии воздуха и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[16]+=1
                            SP-=1
                            S0.append("Мания воздуха")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="18" or CSS=="Магия воды":
                    if SID[17]==0:
                        print("Навык магия воды отвечает за возможность использования магии воды и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[17]+=1
                            SP-=1
                            S0.append("Магия воды")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="19" or CSS=="Магия тьмы":
                    if SID[18]==0:
                        print("Навык магия тьмы отвечает за возможность использования магии тьмы и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[18]+=1
                            SP-=1
                            S0.append("Магия тьмы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="20" or CSS=="Чтение свитков":
                    if SID[19]==0:
                        print("Навык чтение свитков отвечает за возможность использования свитков\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[19]+=1
                            SP-=1
                            S0.append("Чтение свитков")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="21" or CSS=="Скрытность":
                    if SID[20]==0:
                        print("Навык скрытность отвечает за возможность использования скрытности и возможности избегать битвы\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[20]+=1
                            SP-=1
                            S0.append("Скрытность")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="22" or CSS=="Критический удар":
                    if SID[21]==0:
                        print("Навык критический удар отвечает за возможность выпадения критического удара во время атаки\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[21]+=1
                            SP-=1
                            S0.append("Критический удар")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="23" or CSS=="Вскрытие замков":
                    if SID[22]==0:
                        print("Навык вскрытие замков отвечает за возможность вскрытия дверей и сундуков без ключей\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[22]+=1
                            SP-=1
                            S0.append("Вскрытие замков")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="24" or CSS=="Использование ловушек":
                    if SID[23]==0:
                        print("Навык использование ловушек отвечает за возможность разминировать ловушки и устанавливать их\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[23]+=1
                            SP-=1
                            S0.append("Использование ловушек")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="25" or CSS=="Наблюдательность":
                    if SID[24]==0:
                        print("Навык наблюдательность отвечает за возможность нахождения скрытых контейнеров и проходов\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[24]+=1
                            SP-=1
                            S0.append("Наблюдательность")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="26" or CSS=="Лечение":
                    if SID[25]==0:
                        print("Навык лечение отвечает за количество восстановленного здоровь путём отдыха и аптечек\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[25]+=1
                            SP-=1
                            S0.append("Лечение")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="27" or CSS=="Парирование":
                    if SID[26]==0:
                        print("Навык парирование даёт шанс польностью избежать урона если удар совпал с ударом противника\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[26]+=1
                            SP-=1
                            S0.append("Парирование")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="28" or CSS=="Оценка":
                    if SID[27]==0:
                        print("Оценка позволяет узнать характеристики врага во время битвы\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[27]+=1
                            SP-=1
                            S0.append("Оценка")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="29" or CSS=="Кинжалы":
                    if SID[28]==0:
                        print("Навык кинжалы отвечает за возможность использования кинжалов и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[28]+=1
                            SP-=1
                            S0.append("Кинжалы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="30" or CSS=="Луки":
                    if SID[29]==0:
                        print("Навык луки отвечает за возможность использования луков и урон от них\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[29]+=1
                            SP-=1
                            S0.append("Луки")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                elif CSS=="31" or CSS=="Дух":
                    if SID[30]==0:
                        print("Навык дух отвечает за возможность использования духа\nЖелаете ли вы выбрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[30]+=1
                            SP-=1
                            S0.append("Дух")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя уже есть эта способность")
                else:
                    print("Неизвестный: Я тебя не понял")
            elif CSS=="2" or CSS=="Вернуть":
                print(" ---------------","\nИмя персонажа: ",name,"\nНазвание класса: ",classname,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H,"\nОставшееся количество очков: ",P,"\nОчки способности:",SP,"\nСпособности: ",S0,"\n","---------------")
                print("Неизвестный: Какие способности ты хочешь вернуть",name,"?")
                print("Экипировка:\n1)Двуручные мечи  2)Одноручные мечи\n3)Двуручные булавы  4)Одноручные булавы\n5)Двуручные топоры  6)Одноручные топоры\n7)Боевые посохи  8)Скипетры\n9)Баклеры       10)Щиты\n11)Башенные щиты  12)Лёгкая броня\n13)Средняя броня  14)Тяжёлая броня\nМагия:\n15)Магия огня  16)Магия земли\n17)Магия воздуха  18)Магия воды\n19)Магия тьмы\nВспомогательные:\n20)Чтение свитков  21)Скрытность\n22)Критический удар  23)Вскрытие замков\n24)Использование ловушек  25)Наблюдательность\n26)Лечение  27)Парирование\n28)Оценка  29)Кинжалы\n30)Луки  31)Дух")
                print(name,": ")
                CSS=input()
                if CSS=="1" or CSS=="Двуручные мечи":
                    if SID[0]==1:
                        print("Навык двуручные мечи отвечает за возможность использования двуручных мечей и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[0]-=1
                            SP+=1
                            S0.remove("Двуручные мечи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="2" or CSS=="Одноручные мечи":
                    if SID[1]==1:
                        print("Навык одноручные мечи отвечает за возможность использования одноручных мечей и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[1]-=1
                            SP+=1
                            S0.remove("Одноручные мечи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="3" or CSS=="Двуручные булавы":
                    if SID[2]==1:
                        print("Навык двуручные булавы отвечает за возможность использования двуручных булав и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[2]-=1
                            SP+=1
                            S0.remove("Двуручные булавы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="4" or CSS=="Одноручные булавы":
                    if SID[3]==1:
                        print("Навык одноручные булавы отвечает за возможность использования одноручных булав и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[3]-=1
                            SP+=1
                            S0.remove("Одноручные булавы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="5" or CSS=="Двуручные топоры":
                    if SID[4]==1:
                        print("Навык двуручные топоры отвечает за возможность использования двуручных топоров и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[4]-=1
                            SP+=1
                            S0.remove("Двуручные топоры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="6" or CSS=="Одноручные топоры":
                    if SID[5]==1:
                        print("Навык одноручные топоры отвечает за возможность использования одноручных топоров и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[5]-=1
                            SP+=1
                            S0.remove("Одноручные топоры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="7" or CSS=="Боевые посохи":
                    if SID[6]==1:
                        print("Навык боевые посохи отвечает за возможность использования боевых посохов и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[6]-=1
                            SP+=1
                            S0.remove("Боевые посохи")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="8" or CSS=="Скипетры":
                    if SID[7]==1:
                        print("Навык скипетры отвечает за возможность использования скипетров и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[7]-=1
                            SP+=1
                            S0.remove("Скипетры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="9" or CSS=="Баклеры":
                    if SID[8]==1:
                        print("Навык баклеры отвечает за возможность использования баклеров и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[8]-=1
                            SP+=1
                            S0.remove("Баклеры")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="10" or CSS=="Щиты":
                    if SID[9]==1:
                        print("Навык щиты отвечает за возможность использования щитов и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[9]-=1
                            SP+=1
                            S0.remove("Щиты")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="11" or CSS=="Башенные щиты":
                    if SID[10]==1:
                        print("Навык башенные щиты отвечает за возможность использования башенных щитов и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[10]-=1
                            SP+=1
                            S0.remove("Башенные щиты")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="12" or CSS=="Лёгкая броня":
                    if SID[11]==1:
                        print("Навык лёгкая броня отвечает за возможность использования лёгкой брони и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[11]-=1
                            SP+=1
                            S0.remove("Лёгкая броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="13" or CSS=="Средняя броня":
                    if SID[12]==1:
                        print("Навык средняя броня отвечает за возможность использования средней брони и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[12]-=1
                            SP+=1
                            S0.remove("Средняя броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="14" or CSS=="Тяжёлая броня":
                    if SID[13]==1:
                        print("Навык тяжёлая броня отвечает за возможность использования тяжёлой брони и урон который они блокируют\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[13]-=1
                            SP+=1
                            S0.remove("Тяжёлая броня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="15" or CSS=="Магия огня":
                    if SID[14]==1:
                        print("Навык магия огня отвечает за возможность использования магии огня и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[14]-=1
                            SP+=1
                            S0.remove("Магия огня")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="16" or CSS=="Магия земли":
                    if SID[15]==1:
                        print("Навык магия земли отвечает за возможность использования магии земли и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[15]-=1
                            SP+=1
                            S0.remove("Магия земли")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="17" or CSS=="Магия воздуха":
                    if SID[16]==1:
                        print("Навык магия воздуха отвечает за возможность использования магии воздуха и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[16]-=1
                            SP+=1
                            S0.remove("Мания воздуха")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="18" or CSS=="Магия воды":
                    if SID[17]==1:
                        print("Навык магия воды отвечает за возможность использования магии воды и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[17]-=1
                            SP+=1
                            S0.remove("Магия воды")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="19" or CSS=="Магия тьмы":
                    if SID[18]==1:
                        print("Навык магия тьмы отвечает за возможность использования магии тьмы и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[18]-=1
                            SP+=1
                            S0.remove("Магия тьмы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="20" or CSS=="Чтение свитков":
                    if SID[19]==1:
                        print("Навык чтение свитков отвечает за возможность использования свитков\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[19]-=1
                            SP+=1
                            S0.remove("Чтение свитков")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="21" or CSS=="Скрытность":
                    if SID[20]==1:
                        print("Навык скрытность отвечает за возможность использования скрытности и возможности избегать битвы\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[20]-=1
                            SP+=1
                            S0.remove("Скрытность")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="22" or CSS=="Критический удар":
                    if SID[21]==1:
                        print("Навык критический удар отвечает за возможность выпадения критического удара во время атаки\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[21]-=1
                            SP+=1
                            S0.remove("Критический удар")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="23" or CSS=="Вскрытие замков":
                    if SID[22]==1:
                        print("Навык вскрытие замков отвечает за возможность вскрытия дверей и сундуков без ключей\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[22]-=1
                            SP+=1
                            S0.remove("Вскрытие замков")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="24" or CSS=="Использование ловушек":
                    if SID[23]==1:
                        print("Навык использование ловушек отвечает за возможность разминировать ловушки и устанавливать их\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[23]-=1
                            SP+=1
                            S0.remove("Использование ловушек")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="25" or CSS=="Наблюдательность":
                    if SID[24]==1:
                        print("Навык наблюдательность отвечает за возможность нахождения скрытых контейнеров и проходов\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[24]-=1
                            SP+=1
                            S0.remove("Наблюдательность")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="26" or CSS=="Лечение":
                    if SID[25]==1:
                        print("Навык лечение отвечает за количество восстановленного здоровь путём отдыха и аптечек\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[25]-=1
                            SP+=1
                            S0.remove("Лечение")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="27" or CSS=="Парирование":
                    if SID[26]==1:
                        print("Навык парирование даёт шанс польностью избежать урона если удар совпал с ударом противника\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[26]-=1
                            SP+=1
                            S0.remove("Парирование")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="28" or CSS=="Оценка":
                    if SID[27]==1:
                        print("Оценка позволяет узнать характеристики врага во время битвы\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[27]-=1
                            SP+=1
                            S0.remove("Оценка")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="29" or CSS=="Кинжалы":
                    if SID[28]==1:
                        print("Навык кинжалы отвечает за возможность использования кинжалов и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[28]-=1
                            SP+=1
                            S0.remove("Кинжалы")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="30" or CSS=="Луки":
                    if SID[29]==1:
                        print("Навык луки отвечает за возможность использования луков и урон от них\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[29]-=1
                            SP+=1
                            S0.remove("Луки")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                elif CSS=="31" or CSS=="Дух":
                    if SID[30]==0:
                        print("Навык дух отвечает за возможность использования духа\nЖелаете ли вы убрать эту способность? 1)Да/2)Нет")
                        print(name,": ")
                        CSS=input()
                        if CSS=="Да" or CSS=="1":
                            SID[30]-=1
                            SP+=1
                            S0.remove("Дух")
                        elif CSS=="Нет" or CSS=="2":
                            continue
                        else:
                            print("Неизвестный: Я тебя не понял")
                    else:
                        print("Неизвестный: У тебя нету этой способности")
                else:
                    print("Неизвестный: Я тебя не понял")
            else:
                print("Неизвестный: Я тебя не понял") 
    else:
        print(" ---------------","\nИмя персонажа: ",name,"\nНазвание класса: ",classname,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H,"\nОставшееся количество очков: ",P,"\nОчки способности:",SP,"\nСпособности: ",S0,"\n","---------------")
        print("Неизвестный: Все очки распределены ты уверены что хочешь отправиться в путешевствие с такими характеристиками? 1)Да/2)Нет")
        print(name,": ")
        CSS=input()
        if CSS=="Да" or CSS=="1":
            E+=1
            break
        elif CSS=="Нет" or CSS=="2":
            E=0
            continue
        else:
            print("Неизвестный: Очевидно вы не поняли моего вопроса")
            continue
print("Неизвестный:",name,"ты сделал свой выбор. Впереди тебя ждёт путь полон опастностей, но ты должен помнить что преград не существует и всегда есть способ обойти препятстве.","Удачи тебе",name,"!")
print("Вы очнулись посреди обломков некого древнего храма или крепости. Стены почти полностью обрасли различной растительностью и создаётся впечатление что здесь давно никого не было.")
HP=H*5
MP=M*5
while True: #Первая глава
    FS=S+AS[0]; FM=M+AM[0]; FA=A+AA[0]; FH=H+AH[0]; urons=FS*2+atk; uronm=FM*2+atk; urona=FA*2+atk; FHP=FH*5
    if path==0:
        print("Падая на холодную землю последней мыслю было как мало вы узнали и как много вы не узнаете...")
        break
    elif exp==expup or exp>expup:
        lvl+=1
        expup=lvl*400*1.5
        SP+=1
        P+=5
        SAP+=1
        print("Поздравляю ваш уровень повышен и теперь он составляет",lvl,"!")
        print("Вы можете распределить очки сейчас или потратить их потом\n1)Распределить сейчас\n2)Распределить потом")
        CSS=input()
        if CSS=="1":
            lvlup()
            continue
        elif CSS=="2":
            continue
    elif random.randint(0,100)>80 and safy==0:
        fight1(random.randint(1,6))
    elif path==1:
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|     Вы на обломках.     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\n1)Разбить лагерь и отдонуть\n2)Покинуть обломки\n-------------------------\n3)Инвентарь\n4)Персонаж\n",name,": ")
        CSS=input()
        if CSS=="1" or CSS=="Разбить лагерь и отдохнуть":
            print("Ваше здоровье было восстановленно")
            HP=FHP
            safy=1
            continue
        elif CSS=="2" or CSS=="Покинуть обломки":
            path=2
            safy=0
            continue
        elif CSS=="3" or CSS=="Инвентарь":
            inventar()
            safy=1
            continue
        elif CSS=="4" or CSS=="Персонаж":
            lvlup()
            safy=1
            continue
        else:
            print("Действие невозможно")
            safy=1
            continue
    elif path==2:
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|  Вы находитесь на дороге неподалёку от обломков на тропе которая ведёт прямо в даль |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\n1)Вернуться\n2)Идти дальше\n-------------------------\n3)Инвентарь\n4)Персонаж\n",name,": ")
        CSS=input()
        if CSS=="1" or CSS=="Вернуться":
            path=1
            safy=0
            continue
        elif CSS=="2" or CSS=="Идти дальше":
            path=3
            safy=0
            continue
        elif CSS=="3" or CSS=="Инвентарь":
            inventar()
            safy=1
            continue
        elif CSS=="4" or CSS=="Персонаж":
            lvlup()
            safy=1
            continue
        else:
            print("Действие невозможно")
            safy=1
            continue
    elif path==3:
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|  Вы прошли дальше по тропе и обнаружили разветвление на два пути. Между ними стоит  |")
        print("|  указатель: в одну сторону храм, во вторую деревня Зайра и третий путь табличка     |")
        print("|  повреждена и неразборчива                                                          |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\n1)Вернуться на дорогу в храм\n2)Идти в деревню\n3)Идти в",locat1,"\n-------------------------\n4)Инвентарь\n5)Персонаж\n",name,": ")
        CSS=input()
        if CSS=="1" or CSS=="Вернуться на дорогу в храм":
            path=2
            safy=0
            continue
        elif CSS=="2" or CSS=="Идти в деревню":
            path=4
            safy=0
            continue
        elif CSS=="3" or CSS=="Идти в неизвестную сторону":
            path=5
            safy=0
            continue
        elif CSS=="4" or CSS=="Инвентарь":
            inventar()
            safy=1
            continue
        elif CSS=="5" or CSS=="Персонаж":
            lvlup()
            safy=1
            continue
        else:
            print("Действие невозможно")
            safy=1
            continue
    elif path==4:
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|     Вы пришли в деревню. На улице пусто и нет ниодного человека в поле зрения       |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\n1)Вернуться назад\n2)Идти в центр города\n3)Зайти в дом\n-------------------------\n4)Инвентарь\n5)Персонаж\n",name,": ")
        CSS=input()
        if CSS=="1" or CSS=="Вернуться на развилку":
            path=3
            safy=0
            continue
        elif CSS=="2" or CSS=="Идти в центр":
            path=6
            safy=0
            continue
        elif CSS=="3" or CSS=="Зайти в дом":
            path=7
            safy=0
            continue
        elif CSS=="4" or CSS=="Инвентарь":
            inventar()
            safy=1
            continue
        elif CSS=="5" or CSS=="Персонаж":
            lvlup()
            safy=1
            continue
        else:
            print("Действие невозможно")
            safy=1
            continue
    elif path==5:
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|  Вы прошли несколько километров по дороге и с каждым вашим шагом кроны деревьев     |")
        print("|                      всё больше заслоняют небо                                      |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("\n1)Вернуться на развилку\n2)Идти дальше\n-------------------------\n3)Инвентарь\n4)Персонаж\n",name,": ")
        CSS=input()
        if CSS=="1" or CSS=="Вернуться на развилку":
            path=3
            safy=0
            continue
        elif CSS=="2" or CSS=="Идти дальше":
            path=8
            safy=0
            continue
        elif CSS=="3" or CSS=="Инвентарь":
            inventar()
            safy=1
            continue
        elif CSS=="4" or CSS=="Персонаж":
            lvlup()
            safy=1
            continue
        else:
            print("Действие невозможно")
            safy=1
            continue
            
