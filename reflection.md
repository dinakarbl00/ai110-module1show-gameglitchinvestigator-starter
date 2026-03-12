# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- A: The game looks like a guessing game. We have to guess a number between 1 and 100.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  (for example: "the secret number kept changing" or "the hints were backwards").
- A: --The hint is mismathced, it says to go higher if theguess is high and to go lower if the guess is low.  --Once you guess correctly, the submit button and hints stop working from the next game onwards.  --The difficulty of the game is messed up, hard level is actually easier than normal level and the new game button does not consider difficulty level at all.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- A: Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- A: Claude said the string conversion in app.py in lines 158-161 to check the guess for the hints is a bug, it was. Verified it through the debug info panel and attempts to confirm the hint was wrong.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- A: Claude suggested to change difficulty paramters to numbers 1-20 being hard difficulty and 1-.50 being easy and 1-100 being normal. I think that is wrong, well, logically having to guess 1 in 20 numbers is easier than having to guess 1 in 100 numbers right. I had the difficulty settings be channged to easy: 1-20, normal: 1-50, hard: 1-100.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- A: I checked manually by rerunning the scennarios which caused the bug, and also wrote tests in pytests wherever it applied.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- A: After changing the hints and game difficulty level settings, I checked through the game interface again if the hints were correct or not for each guess.
- Did AI help you design or understand any tests? How?
- A: Yes, AI helped in understanding the design and logic of testing for these bug fixes for some general and extreme cases which are sometimes difficult to identify. AI wrote and explained the reason behind every test case and teh expected outcome.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- A: Streamlit reruns the code on every click of the mouse. So everything gets refreshed and goes back to how it was when the site/ webpage opens for the first time. The only thing which records the history or holds the values and variables are things given in session state. Session state does not get refreshed.
- What change did you make that finally gave the game a stable secret number?
- A: The fix was wrapping the secret generation inside a guard: `if "secret" not in st.session_state: st.session_state.secret = random.randint(low, high)`. This means the random number is only generated once on the very first load. Every subsequent rerun reads the already-saved value from session_state instead of picking a new one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- A: For me, that would be to ask AI or prompt it to give test cases/ steps to verify the results after editing and to see if it matches your expectaions.
- What is one thing you would do differently next time you work with AI on a coding task?
- A: I would ask AI to generate the reasons and code for appropriate testing and verification of the code changes done.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- A: While AI generated code feels mostly correct, it is not very accurate and efficient at first run. I came across a lot of improvements or chages I would have done personally to make the code better or match my standards and expectations.

---

## 6. AI Model Comparison

For the hint bug (the `str()` conversion on even attempts), I compared the output of two AI tools:

**Claude (Claude Code):**
Claude immediately pinpointed lines 158–161 in `app.py` as the cause, explaining that converting the secret to a string triggered alphabetical comparison inside the `except TypeError` fallback — giving a precise, code-level explanation. It also noted the reversed hint messages as a separate bug in `check_guess`. The fix it suggested (remove the conversion entirely and always pass the integer secret) was correct and clean on the first attempt.

**Original AI-generated code (the starter code author):**
The original AI embedded the bug intentionally as a challenge — but the way it was written (hiding it inside a `% 2 == 0` branch) made it look like intentional feature code rather than a bug. When I first described the symptom to the original model ("hints are wrong sometimes"), it suggested checking `parse_guess` for type issues, which was a red herring. The actual cause was upstream in how the secret was passed, not in how the guess was parsed.

**Which was more Pythonic?**
Claude's fix was more Pythonic — it removed unnecessary branching and trusted that `parse_guess` always returns an `int`, leading to simpler, flatter code. The original AI's approach of adding a `try/except TypeError` fallback was over-engineered and masked the real bug.

**Which explanation was easier to understand?**
Claude's explanation was easier because it cited specific line numbers, explained *why* alphabetical string comparison produces wrong results with a concrete example (`"7" > "50"` is True), and separated the two distinct bugs clearly.
