import pygame

def initialize():
    pygame.init()
    pygame.mixer.init()

def load_music():
    return [
        'MyGame/music/Fujii Kaze - Garden.mp3',
        'MyGame/music/Fujii Kaze - Matsuri.mp3',
        'MyGame/music/Fujii Kaze - Shinunoga E-Wa.mp3'
    ]

def play_next_song(current_index, songs):
    next_index = (current_index + 1) % len(songs)
    return next_index

def play_previous_song(current_index, songs):
    previous_index = (current_index - 1) % len(songs)
    return previous_index

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def main():
    initialize()
    window_width = 600
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))

    songs = load_music()
    current_song_index = 0
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_pause_music()
                elif event.key == pygame.K_n:
                    current_song_index = play_next_song(current_song_index, songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_p:
                    current_song_index = play_previous_song(current_song_index, songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_s:
                    stop_music()

        window.fill((255, 255, 255))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
