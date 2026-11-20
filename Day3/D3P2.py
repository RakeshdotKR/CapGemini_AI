def process(a,b,/,c,d=10,*args,keyword_only,**kwargs):
    """Mixed Parameter kinds in one signature"""
    print(f"a={a}, b={b}, c={c}, d={d}, args={args}, keyword_only = {keyword_only}, kwargs={kwargs}")

# def f(a,b,/)      a,b are positional-only
# c is positional or keyword
# d has a default
# *args def f(*args): variadic arguments : tuple takes extra positionals
# keyword only is a mandatory keyword
# **kwargs : keyword args takes extras

process(1,2,3,4,5,6,keyword_only="yes",extra="x")


# Positional arguments -> Positional or keyword -> default -> Keyword-only 
# -> kw args