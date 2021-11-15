import os


def try_me(name='you'):
    home_dir = os.getenv("HOME")
    word_tokens = home_dir.split("/")
    print(
        f"I would like to give a shout out to {word_tokens[(len(word_tokens)-1)]}!"
    )


if __name__ == "__main__":
    try_me()
