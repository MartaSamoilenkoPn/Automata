from random import randint
import time

class State:
    def __init__(self, name, time = 0) -> None:
        self.name = name
        self.next_states = []
        self.time = time

class FSM:

    def __init__(self, state) -> None:
        assert isinstance(state, State)
        self.state = state
        self.time = 0
        self.random_value_alarm = randint(0,20)
        self.random_value_sleep = randint(0,20)
        self.random_value_forgotten_meeting = randint(0,20)

    state_alarm = State('alarm')
    state_day_sleeping = State('day sleeping')
    state_meeting = State('forgotten meeting')

    def check_random(self):
        """_summary_
        """
        if self.random_value_alarm % 7 == 0:
            print(f"It's {self.time}:00 and there is air alarm, GO TO THE SHELTER")
            previous_state = self.state
            self.change_state(FSM.state_alarm)
            time.sleep(1)
            self.time += 1
            print(f"Alarm is over and it's {self.time}:00")
            self.change_state(previous_state)

        if self.random_value_sleep % 9 == 0 and self.time > 6:
            print(f"It's {self.time}:00 and you're tired, so go to sleep")
            previous_state = self.state
            self.change_state(FSM.state_day_sleeping)
            time.sleep(1)
            self.time += 1
            print(f"Good morning(day|evening) sweety, it's {self.time}:00")
            self.change_state(previous_state)

        if self.random_value_forgotten_meeting % 8 == 0 and self.time > 6:
            print(f"It's {self.time}:00 and you've forgotten the meeting))")
            previous_state = self.state
            self.change_state(FSM.state_meeting)
            time.sleep(1)
            self.time += 1
            print(f"You did such a good job for your team, it's {self.time}:00")
            self.change_state(previous_state)

        self.random_value_alarm = randint(0,20)
        self.random_value_sleep = randint(0,20)
        self.random_value_forgotten_meeting = randint(0,20)

    def change_state(self, state):
        """_summary_
        """
        self.state = state
        assert isinstance(self.state, State)
        print(f"STATE : {self.state.name}")

    def process(self):
        """_summary_
        """
        value = 0
        while True and self.time < 24:
            self.check_random()
            if self.time < 6:
                print(f"You're sleeping, it's {self.time}:00")
                time.sleep(1)
                self.time += 1

            elif self.time == 6:
                print(f"It's {self.time}:00")
                print("GOOD MORNING")
                self.time += 1

            elif self.state.name == 'sleeping' and self.time > 6:
                if self.time == 7:
                    print(f"It's {self.time}:00")
                    self.change_state(self.state.next_states[0])
                    print("You're eating, bon apetite, sweety")
                elif self.time < 10:
                    print(f"It's {self.time}:00")
                    self.change_state(self.state.next_states[1])
                    print("Coffe is always a good idea!")
                    self.change_state(self.state.next_states[0])
                else:
                    print(f"It's {self.time}:00")
                    self.change_state(self.state.next_states[2])
                    print("Oops, it's too late so go do your tasks...")

            elif self.state.name == 'breakfast':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                self.change_state(self.state.next_states[0])

            elif self.state.name == 'matan':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                self.change_state(self.state.next_states[randint(0, len(self.state.next_states)-1)])

            elif self.state.name == 'coffee':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                self.change_state(self.state.next_states[0])

            elif self.state.name == 'programming':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                self.change_state(self.state.next_states[randint(0, len(self.state.next_states)-1)])

            elif self.state.name == 'discrete':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                if self.time < 19:
                    self.change_state(self.state.next_states[randint(0, len(self.state.next_states)-1)])
                else:
                    self.change_state(self.state.next_states[1])

            elif self.state.name == 'sport':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                self.change_state(self.state.next_states[0])
            
            elif self.state.name == 'dinner':
                time.sleep(1)
                self.time += 1
                print(f"It's {self.time}:00")
                self.check_random()
                if self.time < 21:
                    self.change_state(self.state.next_states[0])
                else:
                    self.change_state(self.state.next_states[1])
            
            elif self.state.name == 'end':
                break


if __name__ == "__main__":
    state_sleeping = State('sleeping', 1)
    state_end = State('end')

    state_breakfast = State('breakfast', 1)
    state_coffee = State('coffee', 1)
    state_dinner = State('dinner', 1)

    state_sport = State('sport', 2)

    state_matan = State('matan', 3)
    state_discrete = State('discrete', 2)
    state_programming = State('programming', 2)

    state_sleeping.next_states = [state_breakfast, state_coffee, state_matan]

    state_matan.next_states = [state_programming, state_coffee]
    state_programming.next_states = [state_discrete, state_sport]
    state_discrete.next_states = [state_sport, state_dinner]

    state_breakfast.next_states = [state_matan]
    state_coffee.next_states = [state_matan, state_discrete, state_programming]
    state_dinner.next_states = [state_discrete, state_end]

    state_sport.next_states = [state_dinner]


    fsm = FSM(state = state_sleeping)
    fsm.process()