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


    # attack 함수 실행부에서 break 되도록 하고 싶은데 불가능
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"현재 HP: 0, MP:0 ")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} ")


    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.max_hp,
            self.power
        )


# 몬스터 도감 만들기 (리스트 활용)
# 싸웠던 몬스터 목록들 정보를 리스트에 넣기
# 2번 몬스터 인스턴스 생성시, 리스트 안에 append 하도록 하고
# 7번 몬스터 도감 출력시, __str__()의 정보를 출력하도록 하기
monsters = []


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, mp, magic_power, job):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        self.job = job

    # attack 함수 실행부에서 break 되도록 하고 싶은데 불가능
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다. ")

    # 마법공격 사용시, mp는 1씩 줄어들게 하기
    def magic_attack(self, other):
        damage = random.randint(self.magic_power - 2, self.magic_power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다. ")
        print("마법공격을 써서 mp가 1 줄어듭니다.")
        # mp 1씩 줄어들도록 설정함
        self.mp -= 1
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다. ")

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
        super().__init__(name, hp, power, mp, magic_power, job)
        self.job = job

    def get_JOB(self):
        print("마법사로 전직했습니다.")
        return "{}로 전직했습니다.".format(self.job)

    def jattack(self):
        print("마법사 공격: [에너지 볼트]  ")

    def skill(self):
        print("스킬: [메테오]")


# 기사 클래스
class Knight(Character):
    def __init__(self, name, hp, power, mp, magic_power, job):
        super().__init__(name, hp, power, mp, magic_power, job)
        self.job = job

    def get_JOB(self):
        print("기사로 전직했습니다. ")
        return "{}로 전직했습니다.".format(self.job)

    def jattack(self):
        print("기사 공격: [삼단 베기]  ")

    def skill(self):
        print("스킬: [발도]")


# 도적 클래스
class Thief(Character):
    def __init__(self, name, hp, power, mp, magic_power, job):
        super().__init__(name, hp, power, mp, magic_power, job)
        self.job

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
    print("        7. 몬스터 도감 보기")
    print("        8. 종료 ")
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
            mp = random.randrange(50, 100)
            magic_power = random.randrange(3, 8)
            job = "평민"

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
        ch = Character(name, hp, power, mp, magic_power, job)
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
            else:
                print("y/n 중 하나만 입력해주세요!")
                continue

        monster = Monster(m_name, m_hp, m_power)
        monsters.append(monster)
    # 3번 선택했을 때
    elif ans == 3:
        if ch.job == "평민":
            print("전직할 직업을 골라주세요.")
            print("1. 기사  2. 도적  3. 마법사")
            number = int(input("→   "))
            if number == 1:
                job = "기사"
                ch = Knight(name, hp, power, mp, magic_power, job)
                ch.get_JOB()
                ch.jattack()
                ch.skill()
                continue
            elif number == 2:
                job = "도적"
                ch = Thief(name, hp, power, mp, magic_power, job)
                ch.get_JOB()
                ch.jattack()
                ch.skill()
                continue
            elif number == 3:
                job = "마법사"
                ch = Magician(name, hp, power, mp, magic_power, job)
                ch.get_JOB()
                ch.jattack()
                ch.skill()
                continue
            else:
                print("번호를 다시 선택해주세요.")
        else:
            print(f"이미 [{ch.job}]로 전직했습니다.")
            print("전직은 한번만 가능합니다.")
            continue


    # 4번 전투하기 선택했을 떄
    elif ans == 4:
        print("전투를 시작합니다.")
        print("공격 방식을 선택해주세요.(숫자입력) : 1. 일반공격 2. 마법공격")

        num = int(input())
        if num == 1:
            # hp 또는 mp가 0일 때 전투 종료하도록 만듦
            # Character의 attack 함수를 종료시킬 방법 중 최선으로 생각해냄
            if ch.hp == 0:
                print("당신이 패배했습니다. 전투를 종료합니다.")
                break
            elif monster.hp == 0:
                print("축하합니다. 전투에서 승리하셨습니다.")
                print("전투를 종료하시겠습니까? (y/n)")
                answer = str(input())
                if answer == 'y':
                    print(" 전투를 종료합니다. ")
                    break
                elif answer == 'n':
                    print("몬스터를 생성해주세요(2번 선택)")
                    continue

            else:
                ch.jattack()
                ch.skill()
                ch.attack(monster)
                monster.attack(ch)
                ch.show_status()
                monster.show_status()
                continue

        elif num == 2:
            if ch.hp == 0:
                print("당신이 패배했습니다. 전투를 종료합니다.")
                break
            elif monster.hp == 0:
                print("당신이 승리했습니다. 전투를 종료합니다. ")
                break
            else:
                ch.magic_attack(monster)
                monster.attack(ch)
                ch.show_status()
                monster.show_status()
                continue
    # 5번 플레이어 정보 보기 선택했을 때
    elif ans == 5:
        print("플레이어 이름: ", ch.name)
        print("직업: ", ch.job)
        print("hp:", ch.hp)
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
    # 7번 몬스터 도감 보기
    # 전투했던 몬스터 정보들이 나옴
    elif ans == 7:
        print("[몬스터 도감]")
        print("이름", "HP", "power")
        # monsters 리스트에 정보 저장
        for monster in monsters:
            print(str(monster))
        continue
    # 8번 종료하기 눌렀을 때
    elif ans == 8:
        print("게임을 종료합니다.")
        break

    # 잘못 눌렀을 때
    else:
        print(" 1~7 의 숫자만 입력 가능합니다.")
