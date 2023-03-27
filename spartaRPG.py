import random


class Monster:
    """
     몬스터의 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"당신이 패배했습니다.")

    def magic_attack(self, other):
        magic_damage = random.randint(self.power - 2, self.power + 2)
        other.mp = max(other.mp - magic_damage, 0)

        print(f"{self.name}의 공격! {other.name}에게 {magic_damage}의 데미지를 입혔습니다.")
        if other.mp == 0:
            print(f"당신이 패배했습니다.")

    def show_status(self):

        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} ")


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, mp, magic_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다. 당신이 승리했습니다! ")

    def magic_attack(self, other):
        damage = random.randint(self.magic_power - 2, self.magic_power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다. 당신이 승리했습니다! ")

    def jattack(self):
        print("기본 공격")
    def skill(self):
        print("기본 스킬")
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


# 캐릭터와 상속 관계에 있는 클래스 3개 만들기 (기사, 마법사, 도적)

# 마법사 클래스
class Magician(Character):
    def __init__(self, name, hp, power, mp, magic_power, job):
        super().__init__(name, hp, power, mp, magic_power)
        self.job = job

    def get_JOB(self):
        print("마법사로 전직했습니다.")
        return "{}로 전직했습니다.".format(self.job)

    def jattack(self):
        print("마법사 공격: 에너지 볼트  ")

    def skill(self):
        print("스킬: 메테오")


# 기사 클래스
class Knight(Character):
    def __init__(self, name, hp, power, mp, magic_power, job):
        super().__init__(name, hp, power, mp, magic_power)
        self.job = job

    def get_JOB(self):
        print("기사로 전직했습니다. ")
        return "{}로 전직했습니다.".format(self.job)

    def jattack(self):
        print("기사 공격: 삼단 베기  ")

    def skill(self):
        print("스킬: 발도")


# 도적 클래스
class Thief(Character):
    def __init__(self, name, hp, power, mp, magic_power, job):
        super().__init__(name, hp, power, mp, magic_power)
        self.job = job

    def get_JOB(self):
        print("도둑으로 전직했습니다.")
        return "{}로 전직했습니다.".format(self.job)

    def jattack(self):
        print("도적 공격: 표창 던지기  ")

    def skill(self):
        print("스킬: 세비지 블로우")


# ------------살향부 시작

# 선택하기
while True:

    print("===========SPARTA RPG GAME============")
    print("        1. 플레이어 생성하기 ")
    print("        2. 몬스터 생성 ")
    print("        3. 전직하기(직업선택) ")
    print("        4. 전투 진행 하기 ")
    print("        5. 풀레이어 정보 보기 ")
    print("        6. 몬스터 정보 보기 ")
    print("        7. 종료 ")
    print("===========SPARTA RPG GAME============")
    print("숫자로 입력해주세요. >> ")
    ans = int(input())

    # 1번 선택했을 때
    if ans == 1:
        # 플레이어로 부터 정보 입력받기
        print("이름을 입력해 주세요: ")
        name = str(input(" "))

        # 기본 스텟 랜덤으로 부여받기

        while True:
            hp = random.randrange(100, 150)
            power = random.randrange(8, 30)
            mp = random.randrange(100, 150)
            magic_power = random.randrange(8, 30)

            print(f"hp = {hp}, power = {power} , mp = {mp}, magic_power= {magic_power} ")
            print(" 스텟을 다시 부여받겠습니까? y = 네, n = 아니오")
            ans = str(input())

            if ans == 'y':
                continue
            elif ans == 'n':
                print(f"""
              {name} 님의 [기본 스텟]
              hp = {hp}  power = {power} mp = {mp} magic_power= {magic_power} 
            """)
                break
        ch = Character(name, hp, power, mp, magic_power)
        print(ch.name)
        ch.show_status()
    # 2번 선택했을 때
    elif ans == 2:
        # 몬스터 생성하기
        print("생성할 몬스터 이름을 입력해 주세요: ")
        m_name = str(input(" "))
        while True:
            m_hp = random.randrange(100, 150)
            m_power = random.randrange(8, 20)

            print(f"hp = {m_hp}, power = {m_power} ")
            print(" 스텟을 다시 부여받겠습니까? y = 네, n = 아니오")
            ans = str(input())

            if ans == 'y':
                continue
            elif ans == 'n':
                print(f"""
              몬스터 {m_name}  [기본 스텟]
              hp = {m_hp}  power = {m_power}
            """)
                break

        monster = Monster(m_name, m_hp, m_power)
    # 3번 선택했을 때
    elif ans == 3:
        print("전직할 직업을 골라주세요.")
        print("1. 기사  2. 도적  3. 마법사")
        number = int(input("→   "))
        if number == 1:
            j = "기사"

            ch = Knight(name, hp, power, mp, magic_power, j)
            #  j가 저장되는 이유: 상속에서 상위 클래스는 어디서 파생된건지 알고있기 때문에 하위클래스 접근이 가능
            ch.get_JOB()
            ch.jattack()
            ch.skill()
            continue
        elif number == 2:
            j = '도적'
            ch = Thief(name, hp, power, mp, magic_power, j)
            #  j가 저장되는 이유: 상속에서 상위 클래스는 어디서 파생된건지 알고있기 때문에 하위클래스 접근이 가능
            ch.get_JOB()
            ch.jattack()
            ch.skill()
            continue
        elif number == 3:
            j = '마법사'
            ch = Magician(name, hp, power, mp, magic_power, j)
            #  j가 저장되는 이유: 상속에서 상위 클래스는 어디서 파생된건지 알고있기 때문에 하위클래스 접근이 가능
            ch.get_JOB()
            ch.jattack()
            ch.skill()
            continue
        else:
            print("번호를 다시 선택해주세요.")
    # 4번 전투하기 선택했을 떄
    elif ans == 4:
        print("전투를 시작합니다.")
        print("공격 방식을 선택해주세요.(숫자입력) : 1. 일반공격 2. 마법공격")

        num = int(input())
        if num == 1:
            ch.jattack()
            ch.skill()
            ch.attack(monster)
            monster.attack(ch)
            ch.show_status()
            monster.show_status()

            if ch.hp == 0:
                print("당신이 패배했습니다. 전투를 종료합니다.")
                break
            elif monster.hp == 0:
                print("당신이 승리했습니다. 전투를 종료합니다. ")
                break
            else:
                continue

        elif num == 2:
            ch.magic_attack(monster)
            monster.magic_attack(ch)
            ch.show_status()
            monster.show_status()
            if ch.mp == 0:
                print("당신이 패배했습니다. 전투를 종료합니다.")
                break
            elif monster.hp == 0:
                print("당신이 승리했습니다. 전투를 종료합니다. ")
                break
            continue
    # 5번 플레이어 정보 보기 선택했을 때
    elif ans == 5:
        print("플레이어 이름: ", ch.name)
        print("hp:" , ch.hp)
        print("mp: ", ch.mp)
        print("attack: ")
        ch.jattack()
        print("skill: ")
        ch.skill()
        continue
    # 6번 몬스터 정보 보기 선택했을 때
    elif ans == 6:
        print("몬스터 이름: ", monster.name)
        print("몬스터 HP: ", monster.hp)
        continue
    # 7번 종료하기 눌렀을 때
    elif ans == 7:
        print("게임을 종료합니다.")
        break

    # 잘못 눌렀을 때
    else:
        print(" 1~7 의 숫자만 입력 가능합니다.")
