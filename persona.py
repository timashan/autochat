from colors import Bcolors
import openai


class Persona:
    name: str

    def __init__(
        self,
        name: str,
        color=Bcolors.OKBLUE,
        model="gpt-4",
    ):
        self.name = name
        self.color = color
        self.hist = []
        self.cumulative_tokens = 0
        self.model = model

    def give_mission(self, mission: str):
        self.__update_hist(role="system", content=mission)

    def __update_hist(self, role: str, content: str):
        assert role in ["system", "assistant", "user"]
        self.hist.append({"role": role, "content": content})

    def chat(self, prompt: str, verbose=True) -> str:
        self.__update_hist(role="user", content=prompt)
        completion = openai.chat.completions.create(
            model=self.model, messages=self.hist, temperature=1
        )
        if completion.usage:
            self.cumulative_tokens += int(completion.usage.total_tokens)
        response = completion.choices[0].message.content
        if not response:
            return ""

        if verbose:
            print(self.color + self.name + ": " + response + Bcolors.ENDC)
        self.__update_hist(role="assistant", content=response)
        return response
