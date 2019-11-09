from sys import exit

import pygame

from gomoku_ai import *
from gomoku import *
from render import GameRender


def play(hparams):
    gomoku = Gomoku(hparams)
    render = GameRender(gomoku, hparams)

    # change the AI here, bigger the depth stronger the AI
    ai = gomokuAI(gomoku, BoardState.BLACK, 2)
    second_ai = gomokuAI(gomoku, BoardState.WHITE, 2)

    result = BoardState.EMPTY

    # AI plays first
    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()

    while True:
        if hparams['enable_second_ai']:
            second_ai.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print(result, "wins")
                break
            if hparams['enable_ai']:
                ai.one_step()
                result = gomoku.get_chess_result()
                if result != BoardState.EMPTY:
                    print(result, "wins")
                    break
            else:
                render.change_state()
        # pygame event, player vs. ai section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if render.one_step():
                    result = gomoku.get_chess_result()
                else:
                    continue
                if result != BoardState.EMPTY:
                    break
                if hparams['enable_ai']:
                    ai.one_step()
                    result = gomoku.get_chess_result()
                else:
                    render.change_state()
            else:
                continue
        render.draw_chess()
        render.draw_mouse()

        if result != BoardState.EMPTY:
            render.draw_result(result)

        pygame.display.update()
