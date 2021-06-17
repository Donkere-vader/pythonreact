import PythonReact


class MyComponent(PythonReact.Component):
    def __init__(self):
        self.state = {
            "name": "Donkere",
        }

        super().__init__()

    def render(self) -> list:
        return [
            f"Hello {self.state['name']}!",
        ]


my_comp = MyComponent()
my_comp.set_state({"name": "New Name"})
