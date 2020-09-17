# %% [markdown]
# [Python Home Page](httpswww.kaggle.comlearnpython)
# 
# ---
# 

# %% [markdown]
# # Try It Yourself
# 
# Things get more interesting with lists. See if you can solve the questions below. Remember to run the following cell first.

# %% [code]
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import 
print('Setup complete.')

# %% [markdown]
# # Exercises

# %% [markdown]
# ## 1.
# 
# Complete the function below according to its docstring.

# %% [code]
def select_second(L)
    Return the second element of the given list. If the list has no second
    element, return None.
    
    if len(L)1
        return L[1] 
    else
        None

# Check your answer
q1.check()

# %% [code]
q1.hint()
q1.solution()

# %% [markdown]
# ## 2.
# 
# You are analyzing sports teams.  Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. 
# These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Complete the function below to select the captain of the worst team.

# %% [code]
def losing_team_captain(teams)
    Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    
    losers=teams[len(teams)-1]
    return losers[1]
    

# Check your answer
q2.check()

# %% [code]
t1=[a1,a2,a3]
t2=[b1,b2,b3]
t3=[c1,c2,c3]
teams=[[t1],[t2],[t3]]
print(teams)
#losers=teams[len(teams)-1]
i=len(teams)
print(i)
print(teams[2])
print(teams[i-1])
print(teams[len(teams)-1])

#def losing_team_captain(teams)
    #Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    #from the last listed team
    #
    #losers=teams[len(teams)+1]
    #return teams[len(teams)+1]

#print(losing_team_captain(teams))

# %% [code]
#q2.hint()
q2.solution()

# %% [markdown]
# ## 3.
# 
# The next iteration of Mario Kart will feature an extra-infuriating new item, the Purple Shell. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.

# %% [code]
def purple_shell(racers)
    Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
     r = [Mario, Bowser, Luigi]
     purple_shell(r)
     r
    [Luigi, Bowser, Mario]
    
    c=racers[0]
    racers[0]=racers[len(racers)-1]
    racers[len(racers)-1]=c
    pass
# Check your answer
q3.check()

# %% [code]
x=['a','b','c','d','e','f']
c=x[1]
x[1]=x[0]
x[0]=c
print(x)


# %% [code]
q3.hint()
q3.solution()

# %% [markdown]
# ## 4.
# 
# What are the lengths of the following lists Fill in the variable `lengths` with your predictions. (Try to make a prediction for each list without just calling `len()` on it.)

# %% [code]
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,2]

# Check your answer
q4.check()

# %% [code]
# line below provides some explanation
#q4.solution()

# %% [markdown]
# ## 5. span title=A bit spicy style=color darkgreen 🌶️span
# 
# We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive
# 
#     party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# 
# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
# 
# Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

# %% [code]
L=['a','b','c','d','e']
print(L[02])
print(round(int(5)2,0))
print(round(int(7)2))
print(round(2.5))

# %% [code]
def fashionably_late(arrivals, name)
    Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    
    
    last_index=(len(arrivals)-1)
    if len(arrivals)%2==1
        lower_range=int(len(arrivals)2)+1
    else lower_range=int(len(arrivals)2)
    return name in arrivals[lower_rangelast_index]
      

# Check your answer
q5.check()

# %% [code]
#q5.hint()
q5.solution()

# %% [markdown]
# # Keep Going
# 
# That's it for lists and tuples! Now you have the baseline knowledge to [learn about loops](httpswww.kaggle.comcolinmorrisloops-and-list-comprehensions), which is where lists and tuples get really interesting. 

# %% [markdown]
# ---
# [Python Home Page](httpswww.kaggle.comlearnpython)
# 
# 
# 
# 
# 
# Have questions or comments Visit the [Learn Discussion forum](httpswww.kaggle.comlearn-forum) to chat with other Learners.