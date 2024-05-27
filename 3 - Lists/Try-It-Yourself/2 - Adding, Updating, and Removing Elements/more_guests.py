guests = ["Grandfather", "Alan Turing", "Steve Jobs"]

print(f"{guests[0]}, I request to invite you for a dinner.")
print(f"{guests[1]}, I request to invite you for a dinner.")
print(f"{guests[2]}, I request to invite you for a dinner.")

print(f"\n{guests[1]} cannot make it.\n")

guests[1] = "Albert Einstein."
print(f"{guests[0]}, I request to invite you for a dinner.")
print(f"{guests[1]}, I request to invite you for a dinner.")
print(f"{guests[2]}, I request to invite you for a dinner.")

guests.insert(0, "Emary Nabrissa Caber")
guests.insert(len(guests) // 2, "Maria Theresa Caber")
guests.append("Emmanuel Caber")


print(f"\n{guests[0]}, I request to invite you for a dinner.")
print(f"{guests[1]}, I request to invite you for a dinner.")
print(f"{guests[2]}, I request to invite you for a dinner.")
print(f"{guests[3]}, I request to invite you for a dinner.")
print(f"{guests[4]}, I request to invite you for a dinner.")
print(f"{guests[5]}, I request to invite you for a dinner.")