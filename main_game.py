from ImprovedAE import Title, Score, game_over_text, player, enemy, \
    fire_bullet,collision, start_hand_tracking, reset_game

from mediapipe_hand_sign import hand_identifier

def main():
    game()
    controls()

def game():
    Title()
    Score()
    game_over_text()
    player()
    enemy()
    fire_bullet()
    collision()
    start_hand_tracking()
    reset_game()

def controls():
    hand_identifier()


if __name__ == "main":
    main()
