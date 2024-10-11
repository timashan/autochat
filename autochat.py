import json
from dotenv import load_dotenv

from persona import Persona
from colors import Bcolors


load_dotenv()


def autochat(
    m1,
    m2,
    iterations=1,
    c1_name="c1",
    c2_name="c2",
    model="gpt-4",
    save=True,
    path="./autochat.json",
    verbose=True,
    single_token_price=0.002 / 1000,
):

    def cost_calc(num_tokens: int) -> float:
        return num_tokens * single_token_price

    character1 = Persona(name=c1_name, model=model)
    character1.give_mission(m1)

    character2 = Persona(name=c2_name, color=Bcolors.OKGREEN, model=model)
    character2.give_mission(m2)

    data = {"hist": []}

    c2 = "Hello."
    for i in range(iterations):
        c1 = character1.chat(prompt=c2, verbose=verbose)
        c2 = character2.chat(prompt=c1, verbose=verbose)
        data["hist"].append({character1.name: c1, character2.name: c2})

        if "<END>" in c1:
            break

    if save:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()

    total_tokens_used = character1.cumulative_tokens + character2.cumulative_tokens
    if verbose:
        print("\nTotal tokens used:", total_tokens_used)
        print("Cost incurred (USD):", cost_calc(total_tokens_used))

    return data
