import random

num_dice = 4
dice_mapping = {"+": 1,
                "0": 0,
                "-": -1}

result_mapping = {-4: ">:",
                  -3: "D:",
                  -2: "]:",
                  -1: ":(",
                  0: ":|",
                  1: ":)",
                  2: ":[",
                  3: ":D",
                  4: ":>"}


def roll_dice(num_dice):
    rolls = random.choices(list(dice_mapping.keys()), k=num_dice)
    return rolls


def main():
    rolls = roll_dice(num_dice)
    values = [dice_mapping[i] for i in rolls]
    result = sum(values)
    message = f"You rolled: {"  ".join(rolls)}\n"
    message += "You rolled: {result} {result_mapping[result]}"
    print(message)


if __name__ == "__main__":
    main()
