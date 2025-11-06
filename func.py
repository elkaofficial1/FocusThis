import os
import textwrap
import re
import sys
import load_config
from colorama import init, Fore, Back, Style

init()
a = load_config.Load_Color_Back()
b = load_config.Load_Color_Fore()

MARGIN = 2
HIGHLIGHT_COLOR = f"{Back.__getattribute__(a)} + {Fore.__getattribute__(b)}"


LARGE_TEXT = str(load_config.load_text())

def get_terminal_size():
    try:
        return os.get_terminal_size().columns, os.get_terminal_size().lines
    except OSError:
        return 80, 24

def split_sentences(text):
    return [p.strip() for p in re.split(r'(?<=[.!?])\s+', text) if p.strip()]

def getch():
    try:
        if os.name == 'nt':
            import msvcrt
            return msvcrt.getch().decode('utf-8')
        else:
            import termios, tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except:
        return input()[0] if input() else ''

def display_state(current, paragraphs, text_width, text_height):
    sent_idx = 0
    marked_paragraphs = []
    for para in paragraphs:
        para_sents = split_sentences(para)
        marked_para = []
        for sent in para_sents:
            if sent_idx == current:
                marked_para.append(f"{HIGHLIGHT_COLOR}{sent}{Style.RESET_ALL}")
            else:
                marked_para.append(sent)
            sent_idx += 1
        marked_paragraphs.append(' '.join(marked_para))

    formatted_paras = [textwrap.fill(p, width=text_width) for p in marked_paragraphs]
    lines = '\n\n'.join(formatted_paras).split('\n')

    highlight_line = next((i for i, line in enumerate(lines) if HIGHLIGHT_COLOR in line), 0)

    start_line = 0
    if len(lines) > text_height:
        start_line = max(0, highlight_line - text_height // 2)
        start_line = min(start_line, len(lines) - text_height)

    end_line = start_line + text_height

    os.system('cls' if os.name == 'nt' else 'clear')

    visible_lines = lines[start_line:end_line]
    for line in visible_lines:
        print(' ' * MARGIN + line)

    print('\n' * (text_height - len(visible_lines)), end='')

def main():
    width, height = get_terminal_size()
    text_width = width - 2 * MARGIN
    text_height = height - 2

    sentences = split_sentences(LARGE_TEXT)
    paragraphs = LARGE_TEXT.split('\n\n')
    total = len(sentences)
    current = 0

    while True:
        display_state(current, paragraphs, text_width, text_height)

        if current >= total - 1:
            break

        key = getch()
        if key.lower() == 'q':
            break

        current += 1


if __name__ == "__main__":
    main()
