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

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
