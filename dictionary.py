# house_traits = {
#     "Gryffin": {"brave", "daring", "chivalrous"},
#     "Raven": {"wise", "intelligent", "creative"},
#     "Huff": {"loyal", "kind", "hardworking"},
#     "Sly": {"cunning", "resourceful", "ambitious"}
# }

# def assign_house(student_name, student_traits):
#     student_traits_set = set(trait.lower() for trait in student_traits)
#     match_counts = {}

#     for house, traits in house_traits.items():
#         match_count = len(student_traits_set & traits)
#         match_counts[house] = match_count

#     max_matches = max(match_counts.values())
#     top_houses = [house for house, count in match_counts.items() if count == max_matches]

#     assigned_house = top_houses[0] if len(top_houses) == 1 else "Undecided"
#     print(f"{student_name} → {assigned_house}")

# student_name = input("Enter student name: ").strip()
# print("Enter 3 traits (one at a time):")
# traits = [input(f"Trait {i+1}: ").strip().lower() for i in range(3)]

# assign_house(student_name, traits)