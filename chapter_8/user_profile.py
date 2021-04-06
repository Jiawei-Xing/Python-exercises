def build_profile(first_name, last_name, **information):
    profile = {'first_name': first_name, 'last_name': last_name}
    for key, value in information.items():
        profile[key] = value
    return profile
    
    
# ~ first_name = input("first name: ")
# ~ last_name = input("last_name: ")
# ~ user_profile = build_profile(
    # ~ first_name, last_name, location = 'beijing', age = 22, major = "microbiology"
    # ~ )
# ~ print(user_profile)
