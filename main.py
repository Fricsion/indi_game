#-*- coding:utf-8 -*-

class Player:   # ロールプレイヤーのクラス
    def __init__(self):
        self.tp = 0

class Battle:
    def __init__(self):
        return None

    def playerAct(self, command):
        return None

    def animations(self):
        return None

class Bravery:  # ゲーム全体のクラス
    (TITLE, FIELD, TITLE) = (0, 1, 2)   # self.game_partで用いるステータス
    def __init__(self):
        self.game_part = TITLE
        return None

    def changePart(self, into):
        self.game_part = into

    def render(self):
        return None

    def update(self):
        return None



if __name__ == '__main__':
    Bravery()
