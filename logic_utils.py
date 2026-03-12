# FIX: used claude move the logic to logic_utills.py but gave a custom prompt to change the difficulty settings according to my requirements instead of the original one suggested by claude.
def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive (low, high) number range for a given difficulty level.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) where low and high are the inclusive bounds
        of the secret number range. Defaults to (1, 100) for unknown values.

    Example:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
        >>> get_range_for_difficulty("Hard")
        (1, 100)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


#FIX: added parse_guess to convert user input into an int, and updated check_guess to return a message along with the outcome and used claude to write and explain the logic for the conditions in the functions.
def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """Parse raw text input from the user into an integer guess.

    Handles empty input, non-numeric strings, decimal numbers (truncated to int),
    and negative numbers. Does not validate whether the number is within the
    game range — that is the caller's responsibility.

    Args:
        raw: The raw string entered by the user (e.g. "42", "7.5", "abc", "").

    Returns:
        A tuple (ok, guess_int, error_message) where:
        - ok (bool): True if parsing succeeded, False otherwise.
        - guess_int (int | None): The parsed integer, or None on failure.
        - error_message (str | None): A human-readable error, or None on success.

    Example:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("abc")
        (False, None, 'That is not a number.')
        >>> parse_guess("")
        (False, None, 'Enter a guess.')
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Compare the player's guess against the secret number.

    Args:
        guess: The player's integer guess.
        secret: The secret integer the player is trying to find.

    Returns:
        A tuple (outcome, message) where:
        - outcome (str): "Win", "Too High", or "Too Low".
        - message (str): A display message with emoji for the player.

    Example:
        >>> check_guess(50, 50)
        ('Win', '🎉 Correct!')
        >>> check_guess(60, 50)
        ('Too High', '📉 Go LOWER!')
        >>> check_guess(40, 50)
        ('Too Low', '📈 Go HIGHER!')
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


#FIX: fixed the case where it was giving free points during Too high case in even attempts.
def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Calculate the new score based on the outcome of a guess.

    Winning scores points based on how quickly the player guessed — earlier
    wins are worth more. Wrong guesses always deduct 5 points.

    Args:
        current_score: The player's score before this guess.
        outcome: One of "Win", "Too High", or "Too Low".
        attempt_number: The 1-based count of how many guesses have been made.

    Returns:
        The updated integer score after applying the outcome.

    Example:
        >>> update_score(0, "Win", 1)
        80
        >>> update_score(100, "Too High", 3)
        95
        >>> update_score(100, "Too Low", 2)
        95
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    return current_score
