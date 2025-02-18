from antelop import antelop_analysis

@antelop_analysis
class Greeting:
    """
    This is Antelop's hello world function.
    """

    name = "hello_from_github"
    query = "Experimenter"
    returns = {"greeting": str}
    args = {"excited": bool}

    def run(key, excited=True):
        full_name = (Experimenter & key).fetch1("full_name")
        if excited:
            return f"Hello from GitHub, {full_name}!"
        else:
            return f"Hello from GitHub, {full_name}."
