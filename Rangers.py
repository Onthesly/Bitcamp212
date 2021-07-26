# 모듈 가져오기(파이게임,랜덤)
import os
import random
from time import sleep
import pygame
from pygame.locals import *
# 스크린의 크기
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
# 문자색 지정
BLACK = (0, 0, 0)
WHITE = (250, 255, 255)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)
# 몬스터가 오는 다섯갈래길 설정
LINE = [0, 20, 115, 210, 300, 400, 480]
Choice = 3
# FPS
FPS = 60
# 레인저 지정하는 화살표 클래스
class Select(pygame.sprite.Sprite):
    def __init__(self):
        super(Select, self).__init__()      # 화살표 이미지, 위치 지정
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets','select.png')), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = LINE[3]
        self.rect.y = SCREEN_HEIGHT - 160
    
    def update(self):                       # 매번 바뀔 부분
        global Choice
        self.rect.x = LINE[Choice]
        # 화살표가 화면밖으로 안나가게 함
        if Choice < 1:
            Choice = 1
        elif Choice > 5:
            Choice = 5

    def draw(self, screen):                 # 이미지 화면에 표시하는 함수 -> 전역
        screen.blit(self.image, self.rect)
# 레인저가 발사하는 무기 클래스
class Weapon(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed, line):
        super(Weapon, self).__init__()      # 레인저 별로 다른 무기 이미지를 불러온다
        weapon_images = ['WeaponYellow.png', 'WeaponBlack.png', 'WeaponRed.png', 'WeaponBlue.png', 'WeaponPink.png']
        self.line = line
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', weapon_images[self.line])), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound(os.path.join('assets','weapon.mp3'))

    def launch(self):                       # 무기가 발사될때 소리가 나온다
        self.sound.play()

    def update(self):                       # 매번 바뀔 부분
        self.rect.y -= self.speed           # 무기가 화면밖으로 나가면 없앤다
        if self.rect.y + self.rect.height < 0:
            self.kill()
    
    def collide(self, sprites):             # 무기가 몬스터와 충돌할때
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
# 레인저가 발사하는 레이저 클래스
class Laser(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Laser, self).__init__()                       # 레이저 이미지 불러온다
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets','laser.png')), (480, 1140))
        self.rect = self.image.get_rect()
        self.rect.x = -5
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound(os.path.join('assets','laser.wav'))        # 레이저 사운드
        self.sound2 = pygame.mixer.Sound(os.path.join('assets','vulcan.wav'))      # 레이저 쏘기전 음성

    def launch(self):               # 레이저 쏘기전 음성출력을 위해 2초 멈춤
        self.sound2.play()
        sleep(2)
        self.sound.play()

    def update(self):               # 레이저도 화면 밖으로 나가면 없앰
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:
            self.kill()
    
    def collide(self, sprites):     # 레이저가 몬스터와 충돌할때
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
# 초급 몬스터들 클래스(내부 코딩은 이하 몬스터들 동일)
class Monster0(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Monster0, self).__init__()    # 귀여운 몬스터들 이미지 랜덤 추출
        monster_images = ('Monster00.png', 'Monster01.png', 'Monster02.png', 'Monster03.png', 'Monster04.png', 'Monster05.png',\
            'Monster06.png', 'Monster07.png', 'Monster08.png', 'Monster09.png')
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', random.choice(monster_images))), (50, 50))
        self.rect = self.image.get_rect()   # 이미지 크기 가져옴
        self.rect.x = xpos                  # 이미지 가로 크기
        self.rect.y = ypos                  # 이미지 세로 크기
        self.speed = speed                  # 몬스터 떨어지는 속도

    def update(self):                       # 몬스터가 떨어진다
        self.rect.y += self.speed

    def out_of_screen(self):                # 몬스터가 레인저에 닿을때
        if self.rect.y > SCREEN_HEIGHT - 150:
            return True 
# 중급 몬스터들 클래스
class Monster1(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Monster1, self).__init__()    # 조금 안귀여운 몬스터들 이미지 랜덤 추출
        monster_images = ('Monster10.png', 'Monster11.png', 'Monster12.png', 'Monster13.png', 'Monster14.png', 'Monster15.png')
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', random.choice(monster_images))), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > SCREEN_HEIGHT - 200:
            return True
# 상급 몬스터들 클래스
class Monster2(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Monster2, self).__init__()    # 징그러운 몬스터들 이미지 랜덤 추출
        monster_images = ('Monster20.png', 'Monster21.png', 'Monster22.png')
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', random.choice(monster_images))), (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > SCREEN_HEIGHT - 250:
            return True      
# 텍스트를 출력하는 함수 정의
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)
# 무기로 몬스터를 맞추었을때
def occur_hit(surface, x, y):       # 맞추었을때 이미지랑 소리를 설정한다
    hit_image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'hit.png')), (80, 80))
    hit_rect = hit_image.get_rect()
    hit_rect.x = x
    hit_rect.y = y
    surface.blit(hit_image, hit_rect)
    hit_sound = pygame.mixer.Sound(os.path.join('assets', 'hit.wav'))
    hit_sound.play()
# 몬스터가 죽었을때
def occur_kill(surface, x, y):      # 몬스터가 죽었을때 이미지와 소리를 설정한다
    kill_image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'kill.png')), (60, 60))
    kill_rect = kill_image.get_rect()
    kill_rect.x = x
    kill_rect.y = y
    surface.blit(kill_image, kill_rect)
    kill_sound = pygame.mixer.Sound(os.path.join('assets', 'kill.wav'))
    kill_sound.play()
# 게임 중
def game_loop():
    global Choice   # 갈래길 선택하는 변수를 가져옴
    background_image = pygame.image.load(os.path.join('assets', 'background.jpg'))  # 배경 이미지
    rangers_image = pygame.image.load(os.path.join('assets', 'Rangers.png'))        # 레인저 이미지
    gameover_sound = pygame.mixer.Sound(os.path.join('assets', 'gameover.wav'))     # 게임오버 소리
    pygame.mixer.music.load(os.path.join('assets', 'music.mp3'))                   # 배경 소리
    pygame.mixer.music.play(-1)                             # 배경 반복으로 틀어놈
    fps_clock = pygame.time.Clock()                         # 시간 변수 

    select = Select()                                       # 화살표 클래스 가져오기
    weapons = pygame.sprite.Group()                         # 무기들의 그룹
    lasers = pygame.sprite.Group()                          # 레이저 그룹
    monsters0 = pygame.sprite.Group()                       # 초급몬스터 그룹
    monsters1 = pygame.sprite.Group()                       # 중급몬스터 그룹
    monsters2 = pygame.sprite.Group()                       # 고급몬스터 그룹

    occur_prob0 = 100                   # 초급몬스터 생성 확률 숫자 높을수록 낮음
    occur_prob1 = 200                   # 중급몬스터 ''
    occur_prob2 = 300                   # 고급몬스터 ''
    onHit_count1 = 0            # 중급몬스터를 맞춘 횟수(여러번 때리면 죽게 하려고 설정함)
    onHit_count2 = 0            # 고급몬스터 ''
    score_count = 0             # 점수
    laser_gaze = 0              # 레이저 충전 게이지
    life_ranger = 3             # 레인저 생명

    done = False
    while not done:             # done이 True될때까지 반복
        for event in pygame.event.get():            # 여기부터는 이벤트
            if event.type in [pygame.QUIT]:         # 게임 프로그램 종료
                pygame.quit()
            if event.type == pygame.KEYDOWN:        # 키를 누를때만 설정함
                if event.key == pygame.K_LEFT:      # 왼쪽 방향키를 누르면 왼쪽 레인저 선택
                    Choice -= 1
                elif event.key == pygame.K_RIGHT:   # 오른쪽 ''
                    Choice += 1
                elif event.key == pygame.K_SPACE:   # 스페이스키 누를때 레인저에 따라 다른 무기 발사
                    if Choice == 1:                 # 옐로
                        weapon = Weapon(select.rect.x + 10, select.rect.y, 10, 0)
                        weapon.launch()             # 무기클래스 가져오고 소리출력
                        weapons.add(weapon)         # 발사한 무기를 그룹에 넣는다(이하 동일)
                    elif Choice == 2:               # 블랙
                        weapon = Weapon(select.rect.x + 10, select.rect.y, 10, 1)
                        weapon.launch()
                        weapons.add(weapon)
                    elif Choice == 3:               # 레드
                        weapon = Weapon(select.rect.x + 10, select.rect.y, 10, 2)
                        weapon.launch()
                        weapons.add(weapon)
                    elif Choice == 4:               # 블루
                        weapon = Weapon(select.rect.x + 10, select.rect.y, 10, 3)
                        weapon.launch()
                        weapons.add(weapon)        
                    else:                           # 핑크
                        weapon = Weapon(select.rect.x + 10, select.rect.y, 10, 4)
                        weapon.launch()
                        weapons.add(weapon)
                elif event.key == ord('z'):         # z키를 누르면 레이저 발사
                    if laser_gaze == 100:           # 레이저게이지 100%일때
                        laser = Laser(0, select.rect.y, 10)     # 레이저 클래스 가져옴
                        vulcan_image = pygame.transform.scale(pygame.image.load(os.path.join('assets','vulcan.png')), (440, 380))
                        screen.blit(vulcan_image, (20,90))      
                        pygame.display.update()                 # 레이저 발사전 이미지 출력                 
                        laser.launch()                          # 레이저 발사전 소리 출력
                        lasers.add(laser)                       # 레이저를 그룹에 담는다
                        laser_gaze -= 100                       # 레이저 게이지 초기화
        
        screen.blit(background_image, background_image.get_rect())  # 배경 넣음
        # 초급몬스터 생성 확률&내려오는 최저속도,최고속도 변수(점수에 따라 모두 증가함)
        occur_of_monsters0 = 1 + int(score_count / 300)
        min_monster_speed0 = 1 + int(score_count / 200)
        max_monster_speed0 = 1 + int(score_count / 100)
        # 중급몬스터 ''
        occur_of_monsters1 = 1 + int(score_count / 600)
        min_monster_speed1 = 1 + int(score_count / 300)
        max_monster_speed1 = 1 + int(score_count / 200)
        # 고급몬스터 ''
        occur_of_monsters2 = 1 + int(score_count / 900)
        min_monster_speed2 = 1 + int(score_count / 400)
        max_monster_speed2 = 1 + int(score_count / 300)
        # 위에 설정한 변수에 따라 초급몬스터 생성(이하 동일)
        if random.randint(1, occur_prob0) == 1:                                 # 메인루프 초반부에 설정한 확률에 따라 생성
            for i in range(occur_of_monsters0):
                speed = random.randint(min_monster_speed0, max_monster_speed0)  # 최저속도,최고속도 안에서 속도 랜덤설정
                monster0 = Monster0(random.choice(LINE[1:5])+5, 0, speed)       # 초급몬스터가 내려올 경로 설정&만듬
                monsters0.add(monster0)                                         # 초급몬스터를 그룹에 담는다
        # 중급몬스터 생성 ''
        if random.randint(1, occur_prob1) == 50:
            for i in range(occur_of_monsters1):
                speed = random.randint(min_monster_speed1, max_monster_speed1)
                monster1 = Monster1(random.choice(LINE[1:5])-20, 0, speed)
                monsters1.add(monster1)
        # 고급몬스터 생성 ''
        if random.randint(1, occur_prob2) == 100:
            for i in range(occur_of_monsters2):
                speed = random.randint(min_monster_speed2, max_monster_speed2)
                monster2 = Monster2(random.choice(LINE[1:5])-40, 0, speed)
                monsters2.add(monster2)                 
        # 무기그룹에 있는 무기들이 초급몬스터 그룹과 충돌할 경우(이하 동일, 다른점 설명)
        for weapon in weapons:
            monster0 = weapon.collide(monsters0)
            if monster0:            
                weapon.kill()       # 몬스터에 닿으면 무기 사라짐
                monster0.kill()     # 초급몬스터라 한방에 사라짐
                occur_kill(screen, monster0.rect.x, monster0.rect.y)    # 위에서 정의한 몬스터가 죽었을때 이미지와 소리 출력
                score_count += 1    # 점수 1 오름
        # 무기그룹이 중급몬스터 그룹과 충돌
        for weapon in weapons:
            monster1 = weapon.collide(monsters1)
            if monster1:
                weapon.kill()
                occur_hit(screen, monster1.rect.x, monster1.rect.y)
                onHit_count1 += 1       # 중급몬스터라 타격횟수만 올림
                if onHit_count1%2 == 0: # 중급몬스터가 두번 맞았을 때 죽음
                    weapon.kill()
                    monster1.kill()
                    occur_kill(screen, monster1.rect.x + 20, monster1.rect.y)
                    score_count += 3    # 점수 3 오름
        # 무기그룹이 고급몬스터 그룹과 충돌
        for weapon in weapons:
            monster2 = weapon.collide(monsters2)
            if monster2:
                weapon.kill()
                occur_hit(screen, monster2.rect.x, monster2.rect.y + 30)
                onHit_count2 += 1
                if onHit_count2%3 == 0: # 고급몬스터가 세번 맞았을 때 죽음
                    weapon.kill()
                    monster2.kill()
                    occur_kill(screen, monster2.rect.x + 40, monster2.rect.y)
                    score_count += 5    # 점수 5 오름
        # 레이저가 초급몬스터 그룹과 충돌할 경우(무기와 동일, 다른점 설명)
        for laser in lasers:
            monster0 = laser.collide(monsters0)
            if monster0:
                monster0.kill()
                occur_kill(screen, monster0.rect.x, monster0.rect.y)
                score_count += 1
        # 레이저가 중급몬스터 그룹과 충돌
        for laser in lasers:
            monster1 = laser.collide(monsters1)
            if monster1:
                monster1.kill()     # 레이저는 강해서 중급,고급몬스터 한방에 죽음
                occur_kill(screen, monster1.rect.x + 20, monster1.rect.y)
                score_count += 3
        # 레이저가 고급몬스터 그룹과 충돌
        for laser in lasers:
            monster2 = laser.collide(monsters2)
            if monster2:
                monster2.kill()
                occur_kill(screen, monster2.rect.x + 40, monster2.rect.y)
                score_count += 5
        # 초급몬스터 그룹에 있는 초급몬스터가 레인저에 닿았을 때(이하 동일)
        for monster0 in monsters0:
            if monster0.out_of_screen():        # 초급몬스터 클래스에서 가져옴
                monster0.kill()                 # 초급몬스터 사라짐
                missed_sound = pygame.mixer.Sound(os.path.join('assets', 'missed.wav')) # 레인저 생명력 줄어드는 소리
                missed_sound.play()
                life_ranger -= 1                # 레인저 생명력 -1
        # 중급몬스터가 레인저에 닿았을 때
        for monster1 in monsters1:
            if monster1.out_of_screen():
                monster1.kill()
                missed_sound = pygame.mixer.Sound(os.path.join('assets', 'missed.wav'))
                missed_sound.play()
                life_ranger -= 1
        # 고급몬스터가 레인저에 닿았을 때
        for monster2 in monsters2:
            if monster2.out_of_screen():
                monster2.kill()
                missed_sound = pygame.mixer.Sound(os.path.join('assets', 'missed.wav'))
                missed_sound.play()
                life_ranger -= 1
        # 레이저 충전게이지
        if laser_gaze < 100:        # 레이저 충전율 100% 이하일때 시간에 따라 자동충전
            laser_gaze += 0.1       # 시간당 충전율
        else:
            laser_gaze = 100
        # 클래스에서 정의한 화면에서 바뀌는 화면에 출력할 것들(업뎃&그림)
        monsters0.update()  # 초급몬스터
        monsters0.draw(screen)
        monsters1.update()  # 중급몬스터
        monsters1.draw(screen)
        monsters2.update()  # 고급몬스터
        monsters2.draw(screen)
        lasers.update()     # 레이저
        lasers.draw(screen)
        weapons.update()    # 무기
        weapons.draw(screen)
        select.update()     # 화살표
        select.draw(screen)
        screen.blit(rangers_image, (12, 530))   # 레인저 이미지
        # 화면에 출력하는 개체들은 아래에 적을수록 위에 출력되므로 폰트를 맨마지막에 코딩
        draw_text('점수: {}'.format(score_count), font_30, screen, 60, 20, YELLOW)
        draw_text('레인저 생명: {}'.format(life_ranger), font_30, screen, 390, 20, RED)
        draw_text('레이저 충전율: {}%'.format(int(laser_gaze)), font_30, screen, 130, 60, WHITE)
        # 화면 출력
        pygame.display.flip()
        # 레인저 생명력이 0이 되었을 때
        if  life_ranger == 0:
            pygame.mixer_music.stop()
            explosion_image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'explosion.png')), (200, 200))
            explosion_rect = explosion_image.get_rect()     
            explosion_rect.x = SCREEN_WIDTH / 4
            explosion_rect.y = SCREEN_HEIGHT / 4
            screen.blit(explosion_image, explosion_rect)    
            pygame.display.update()         # 폭발 이미지 불러옴&출력
            gameover_sound.play()           # 게임종료 사운드 출력
            sleep(2)                        # 2초 멈춤
            done = True                     # 메인루프(반복) 종료
        # FPS에 따라 시계 돌림
        fps_clock.tick(FPS)     
    # 게임종료시 초기화면으로 돌아감
    return 'game_menu'          
# 초기화면을 구성
def game_menu():
    global font_30  # 폰트 메인에서도 쓰려고...
    start_image = pygame.image.load(os.path.join('assets', 'background.jpg'))
    screen.blit(start_image, [0, 0])    # 초기화면 이미지 넣음(메인이랑 같은것 씀)
    draw_x = int(SCREEN_WIDTH / 2)      # 텍스트 출력을 위한 좌표 설정
    draw_y = int(SCREEN_HEIGHT / 4)
    # 초기화면에 넣을 텍스트 폰트
    font_70 = pygame.font.Font(os.path.join('assets', 'Maplestory Bold.ttf'), 70)
    font_30 = pygame.font.Font(os.path.join('assets', 'Maplestory Light.ttf'), 30)
    # 텍스트 출력
    draw_text('도와줘요!', font_70, screen, draw_x, draw_y, YELLOW)
    draw_text('비트레인저!!', font_70, screen, draw_x, draw_y + 70, YELLOW)
    draw_text('좌우:방향키 스페이스:공격 z:레이저', font_30, screen, draw_x, draw_y + 200, WHITE)
    draw_text('엔터키를 누르면 게임이 시작됩니다', font_30, screen, draw_x, draw_y + 300, WHITE)
    # 화면 출력
    pygame.display.update()
    # 초기화면에서 엔터키를 누르면 게임 시작, x누르면 종료
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'play'
        if event.type == QUIT:
            return 'quit'

    return 'game_menu'
# 기초만든다
def main():
    global screen   # 여기서 설정한 screen을 실행시 코딩에 씀    

    pygame.init()   # 구동, 스크린크기,제목 설정
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Rangers')
    # 위에서 리턴한 문자들을 가지고 메뉴&실행 결정
    action = 'game_menu'
    while action != 'quit':
        if action == 'game_menu':
            action = game_menu()
        elif action == 'play':
            action = game_loop()
    # quit면 끔
    pygame.quit()
# 인터프리터에서 직접 실행했을 경우만 실행(임포트x)
if __name__ == "__main__":
    main()