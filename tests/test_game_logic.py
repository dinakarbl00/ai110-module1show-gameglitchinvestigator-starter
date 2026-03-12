from logic_utils import check_guess, update_score

# --- existing tests (fixed to unpack the tuple check_guess returns) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- tests for the hint-message reversal bug (was: Too High → "Go HIGHER!", Too Low → "Go LOWER!") ---

def test_too_high_message_says_go_lower():
    # Guess is above the secret, so the player needs to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # Guess is below the secret, so the player needs to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_too_high_does_not_say_go_higher():
    # Regression: old bug had "Go HIGHER!" when guess was too high
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message

def test_too_low_does_not_say_go_lower():
    # Regression: old bug had "Go LOWER!" when guess was too low
    _, message = check_guess(1, 99)
    assert "LOWER" not in message

# --- tests for the int-vs-string type bug (secret was converted to str on even attempts) ---

def test_check_guess_secret_is_int():
    # Both guess and secret must be ints — no TypeError should be raised
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_int_comparison_too_high():
    # Ensures numeric comparison, not alphabetical (e.g. "7" > "50" alphabetically but 7 < 50)
    outcome, message = check_guess(7, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_int_comparison_too_low():
    outcome, message = check_guess(99, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# --- tests for the update_score bug (Too High on even attempts was rewarding +5 instead of -5) ---

def test_update_score_too_high_always_deducts():
    # Regression: old bug gave +5 on even attempts for a wrong "Too High" guess
    score_odd  = update_score(100, "Too High", 1)   # odd attempt
    score_even = update_score(100, "Too High", 2)   # even attempt (was bugged)
    assert score_odd  == 95
    assert score_even == 95  # must also deduct, not reward

def test_update_score_too_low_always_deducts():
    assert update_score(100, "Too Low", 1) == 95
    assert update_score(100, "Too Low", 2) == 95
