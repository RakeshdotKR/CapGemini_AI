# Frozenset: is a Immutable version of set

VALID_ROLES = frozenset({"admin","manager","employee","guest"})
# print("admin" in VALID_ROLES, "security" in VALID_ROLES)
# print(type(VALID_ROLES))
# print(sorted((VALID_ROLES) | {"guest"}))
# print(VALID_ROLES)
# VALID_ROLES.add("guest")

# print(type({"editor","guest"} & VALID_ROLES))
# print(type(VALID_ROLES & {"editor","guest"}))
print(VALID_ROLES & {"editor","guest"})

