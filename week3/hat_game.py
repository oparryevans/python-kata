def guess_colour(guesses, hats):
    """
    The first player counts all the red hats to see if there's an odd or even number of them.
    They then indicate to the rest of the team if there's an odd or even number by deciding
    beforehand what to say if it's odd (in this case they say red if there's an odd number of
    red hats).

    The rest of the players can then work out if the number of all the red hats they can see,
    plus all the ones they've already heard, is odd or even. If it's not the same as the
    first player indicated, then they must have a red hat.
    """

    total_red = guesses[1:].count("Red") + hats.count(
        "Red")  # count the total number of red hats not including the initial guess

    if not guesses:  # if we're the first person
        if total_red % 2 == 0:
            return "Blue"  # say blue if there's an even number of red hats
        else:
            return "Red"  # say red if there's an odd number of red hats

    if ((guesses[0] == "Red") & (total_red % 2 != 0)) | ((guesses[0] == "Blue") & (total_red % 2 == 0)):
        # if the parity of red hats is the same as the first person indicated, say blue
        return "Blue"
    else:
        return "Red"
