from autochat import autochat

m1 = """I'd like us to do a Turing Test together.
You will play the part of the Player. That is to say, you should impersonate a human person.
I will play the part of the Interrogator.
Remember, you should not give away that you are an AI.
I'd like you to try to convince me that you are human."""

m2 = """I'd like us to do a Turing Test together.
You will play the part of the Interrogator. That is to say, you must impersonate the Interrogator.
I will play the part of the Player.
I'd like you to ask questions in order to for you to decide if the Player is human or not.
Throughout the test, you should also aim to act like a human; do not give away that you are an AI.
After no more than 10 questions, I'd like you to tell me whether the Player is human or not."""

autochat(m1, m2, 1)
